#!/usr/bin/env python3
"""Controlli di integrita' del sito statico Finds Vault.

Gira sull'output gia' generato (questo repo), non sul generatore.
Uso:  python3 scripts/check_site.py
Exit 1 se trova errori, 0 se trova solo warning.

Cosa NON fa: non contatta Amazon. I link Amazon vanno verificati da un IP
residenziale o via PA-API -- da GitHub Actions Amazon risponde 503/captcha
e otterresti solo falsi positivi.
"""

import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANONICAL_HOST = "https://thefindsvault.com"
IMG_WARN_BYTES = 200 * 1024

errors = []
warnings = []
# warning che si ripetono identici su decine di pagine: si contano e si
# stampano una volta sola, altrimenti il report diventa illeggibile e
# nessuno lo legge (che e' come non averlo).
tallies = {}


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def tally(key, pages=1, items=0):
    t = tallies.setdefault(key, {"pages": 0, "items": 0})
    t["pages"] += pages
    t["items"] += items


def rel(path):
    return os.path.relpath(path, ROOT)


def resolve(href, page_dir):
    """Percorso su disco di un href locale.

    I link che iniziano con '/' sono relativi alla root del sito, non alla
    cartella della pagina -- 404.html li usa per forza, perche' GitHub Pages
    la serve da URL a profondita' arbitraria.
    """
    if href.startswith("/"):
        return os.path.normpath(os.path.join(ROOT, href.lstrip("/")))
    return os.path.normpath(os.path.join(page_dir, href))


class Tags(HTMLParser):
    """Raccoglie <img src/width/height>, <a href/rel> e i blocchi ld+json."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.imgs = []
        self.links = []
        self.canonicals = []
        self.ldjson = []
        self._in_ld = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img":
            self.imgs.append(a)
        elif tag == "a" and a.get("href"):
            self.links.append(a)
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonicals.append(a.get("href", ""))
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_ld = False

    def handle_data(self, data):
        if self._in_ld and data.strip():
            self.ldjson.append(data)


def null_paths(node, prefix=""):
    """Chiavi con valore null dentro una struttura JSON-LD."""
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            p = prefix + "." + k if prefix else k
            if v is None:
                out.append(p)
            else:
                out.extend(null_paths(v, p))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            out.extend(null_paths(v, "%s[%d]" % (prefix, i)))
    return out


def html_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", ".github", "scripts")]
        for f in filenames:
            if f.endswith(".html"):
                yield os.path.join(dirpath, f)


# ---------------------------------------------------------------- products.json
products_path = os.path.join(ROOT, "assets", "products.json")
products = []
try:
    with open(products_path, encoding="utf-8") as fh:
        products = json.load(fh)
except Exception as exc:
    err("assets/products.json non si legge: %s" % exc)

REQUIRED = ("slug", "title", "image", "category")
seen_slugs = {}
for i, p in enumerate(products):
    for field in REQUIRED:
        if not p.get(field):
            err("products.json[%d]: campo '%s' mancante o vuoto" % (i, field))
    slug = p.get("slug")
    if not slug:
        continue
    if slug in seen_slugs:
        err("products.json: slug duplicato '%s' (indici %d e %d)" % (slug, seen_slugs[slug], i))
    seen_slugs[slug] = i

    page = os.path.join(ROOT, "products", slug, "index.html")
    if not os.path.isfile(page):
        err("products.json: '%s' non ha la pagina products/%s/index.html" % (slug, slug))

    img = p.get("image")
    if img and not os.path.isfile(os.path.join(ROOT, img)):
        err("products.json: '%s' punta a un'immagine che non esiste (%s)" % (slug, img))

    if not p.get("youtube"):
        warn("products.json: '%s' non ha un video YouTube collegato" % slug)

# pagine prodotto orfane (cartella presente, non piu' nel JSON)
products_dir = os.path.join(ROOT, "products")
if os.path.isdir(products_dir):
    for d in sorted(os.listdir(products_dir)):
        if os.path.isdir(os.path.join(products_dir, d)) and d not in seen_slugs:
            err("products/%s/ esiste ma non e' in products.json (pagina orfana, indicizzabile)" % d)

# cartelle immagini orfane
assets_products = os.path.join(ROOT, "assets", "products")
if os.path.isdir(assets_products):
    for d in sorted(os.listdir(assets_products)):
        if os.path.isdir(os.path.join(assets_products, d)) and d not in seen_slugs:
            warn("assets/products/%s/ e' rimasta dopo la rimozione del prodotto (peso morto nel repo)" % d)

# ---------------------------------------------------------------- pagine HTML
amazon_re = re.compile(r"amazon\.[a-z.]+|amzn\.to")
pages = sorted(html_files())
for path in pages:
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    page_dir = os.path.dirname(path)
    parser = Tags()
    try:
        parser.feed(raw)
    except Exception as exc:
        err("%s: HTML non parsabile (%s)" % (rel(path), exc))
        continue

    for c in parser.canonicals:
        if c and not c.startswith(CANONICAL_HOST):
            err("%s: canonical punta a un host diverso da %s (%s)" % (rel(path), CANONICAL_HOST, c))

    missing_dims = 0
    for img in parser.imgs:
        src = img.get("src", "")
        if not src or src.startswith(("http://", "https://", "data:")):
            continue
        target = resolve(src.split("?")[0], page_dir)
        if not os.path.isfile(target):
            err("%s: <img> rotta -> %s" % (rel(path), src))
        if not img.get("alt"):
            tally("img_alt", pages=0, items=1)
        if not (img.get("width") and img.get("height")):
            missing_dims += 1
    if missing_dims:
        tally("img_dims", items=missing_dims)

    for a in parser.links:
        href = a.get("href", "")
        relv = (a.get("rel") or "").lower()
        if amazon_re.search(href):
            if "tag=" not in href:
                err("%s: link Amazon senza tag affiliate -> %s" % (rel(path), href[:80]))
            missing = [t for t in ("sponsored", "nofollow") if t not in relv]
            if missing:
                err("%s: link Amazon senza rel=%s -> %s" % (rel(path), "/".join(missing), href[:80]))
            continue
        if href.startswith(("http://", "https://", "mailto:", "#", "tel:")):
            continue
        target = resolve(href.split("#")[0].split("?")[0], page_dir)
        if os.path.isdir(target):
            target = os.path.join(target, "index.html")
        if not os.path.isfile(target):
            err("%s: link interno rotto -> %s" % (rel(path), href))

    for block in parser.ldjson:
        try:
            data = json.loads(block)
        except Exception as exc:
            err("%s: JSON-LD non valido (%s)" % (rel(path), exc))
            continue
        for p in null_paths(data):
            err("%s: JSON-LD ha '%s': null -- la chiave va omessa, non messa a null" % (rel(path), p))

# ---------------------------------------------------------------- sitemap
sitemap_path = os.path.join(ROOT, "sitemap.xml")
if not os.path.isfile(sitemap_path):
    err("sitemap.xml mancante")
else:
    with open(sitemap_path, encoding="utf-8") as fh:
        sitemap = fh.read()
    locs = re.findall(r"<loc>(.*?)</loc>", sitemap)
    if "<lastmod>" not in sitemap:
        warn("sitemap.xml: nessun <lastmod> -- Google non ha modo di sapere cosa e' cambiato")
    for loc in locs:
        if not loc.startswith(CANONICAL_HOST):
            err("sitemap.xml: URL su host sbagliato -> %s" % loc)
    listed = {loc.rstrip("/").rsplit("/", 1)[-1] for loc in locs if "/products/" in loc}
    for slug in seen_slugs:
        if slug not in listed:
            err("sitemap.xml: manca il prodotto '%s'" % slug)
    for slug in sorted(listed - set(seen_slugs)):
        err("sitemap.xml: elenca '%s' che non esiste piu'" % slug)

# ---------------------------------------------------------------- peso immagini
heavy = []
total = 0
for dirpath, _, filenames in os.walk(os.path.join(ROOT, "assets")):
    for f in filenames:
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            size = os.path.getsize(os.path.join(dirpath, f))
            total += size
            if size > IMG_WARN_BYTES:
                heavy.append((size, rel(os.path.join(dirpath, f))))
if heavy:
    heavy.sort(reverse=True)
    warn("%d immagini sopra %d KB (%.1f MB di asset in totale). Le 3 peggiori: %s"
         % (len(heavy), IMG_WARN_BYTES // 1024, total / 1048576,
            ", ".join("%s (%d KB)" % (p, s // 1024) for s, p in heavy[:3])))

if not os.path.isfile(os.path.join(ROOT, "404.html")):
    warn("404.html assente: un link morto manda l'utente sulla pagina di default di GitHub Pages")

# ---------------------------------------------------------------- aggregati
if "img_dims" in tallies:
    t = tallies["img_dims"]
    warn("%d immagini su %d pagine senza width/height -> layout shift (CLS). "
         "Si risolve nel generatore, non a mano." % (t["items"], t["pages"]))
if "img_alt" in tallies:
    warn("%d immagini senza attributo alt" % tallies["img_alt"]["items"])

# ---------------------------------------------------------------- report
print("Finds Vault -- controllo sito")
print("%d prodotti, %d pagine HTML analizzate\n" % (len(products), len(pages)))
for w in warnings:
    print("  WARN   %s" % w)
if warnings:
    print("")
for e in errors:
    print("  ERRORE %s" % e)
if errors:
    print("")
print("%d errori, %d warning" % (len(errors), len(warnings)))
sys.exit(1 if errors else 0)
