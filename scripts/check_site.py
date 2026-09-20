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


# ---------------------------------------------------------------- contenuti del sito
# ⛔ RISCRITTO IL 20/09/2026: il sito non ha piu' i 69 prodotti Amazon del vecchio Finds Vault.
# Ora ha /blog/<slug>/ (gli articoli degli episodi) e /guides/<tipologia>/ (le guide d'acquisto),
# piu' i rimandi /list/<categoria>/ che tengono vivi gli indirizzi stampati nelle descrizioni
# dei video gia' pubblicati. Il controllo vecchio cercava assets/products.json e falliva sempre.

def _cartelle(sotto):
    d = os.path.join(ROOT, sotto)
    if not os.path.isdir(d):
        return []
    return sorted(x for x in os.listdir(d)
                  if os.path.isdir(os.path.join(d, x))
                  and os.path.isfile(os.path.join(d, x, "index.html")))

blog_slugs = _cartelle("blog")
guide_slugs = _cartelle("guides")
list_slugs = _cartelle("list")

if not blog_slugs:
    err("nessun articolo in /blog/: il sito non ha contenuto")
if not guide_slugs:
    err("nessuna guida in /guides/: sparirebbero tutti i link di affiliazione")

# ⛔ Una pagina ORFANA e' una pagina online che nessuno linka. Il 20/09 sei pagine sono state
# online per giorni senza un solo link che ci portasse, e rispondevano 200: un 200 non dice
# che la pagina sia raggiungibile. Si verifica cercando l'indirizzo dentro le ALTRE pagine.
_tutto_html = ""
for _p in html_files():
    with open(_p, encoding="utf-8") as _fh:
        _tutto_html += _fh.read()
for slug in blog_slugs:
    if ("blog/%s/" % slug) not in _tutto_html:
        err("blog/%s/ e' online ma nessuna pagina la linka (pagina orfana)" % slug)
for slug in guide_slugs:
    if ("guides/%s/" % slug) not in _tutto_html:
        err("guides/%s/ e' online ma nessuna pagina la linka (pagina orfana)" % slug)

# I rimandi /list/ devono essere noindex e NON stare in sitemap: sono duplicati voluti.
for slug in list_slugs:
    with open(os.path.join(ROOT, "list", slug, "index.html"), encoding="utf-8") as fh:
        testo = fh.read()
    if "noindex" not in testo:
        err("list/%s/ e' un rimando ma non ha noindex: Google indicizzerebbe un doppione" % slug)
    if "http-equiv=\"refresh\"" not in testo:
        err("list/%s/ non rimanda a nulla: chi arriva dal video resta fermo li'" % slug)

# La sitemap deve contenere le pagine vere e NON i rimandi.
sitemap_path = os.path.join(ROOT, "sitemap.xml")
sitemap = ""
if os.path.isfile(sitemap_path):
    with open(sitemap_path, encoding="utf-8") as fh:
        sitemap = fh.read()
    for slug in blog_slugs:
        if ("/blog/%s/" % slug) not in sitemap:
            err("blog/%s/ non e' in sitemap.xml" % slug)
    for slug in guide_slugs:
        if ("/guides/%s/" % slug) not in sitemap:
            err("guides/%s/ non e' in sitemap.xml" % slug)
    for slug in list_slugs:
        if ("/list/%s/" % slug) in sitemap:
            err("list/%s/ e' noindex ma sta in sitemap: si chiede a Google di indicizzare "
                "una pagina che gli dice di non farlo" % slug)
else:
    err("sitemap.xml manca")

# ---------------------------------------------------------------- regole Amazon
# ⛔ Un link di affiliazione senza rel="sponsored" (o nofollow) viola insieme la regola Google
# e quella Amazon Associates, e una pagina che ne ha senza dichiararlo viola la FTC.
_amz = re.compile(r'<a[^>]+href="([^"]*(?:amazon\.[a-z.]+|amzn\.to)[^"]*)"[^>]*>')
# ⛔ Non tutti i link ad Amazon sono link di affiliazione: la pagina privacy, le condizioni
# d'uso e le pagine di aiuto sono RIFERIMENTI, e metterci un tag= sarebbe sbagliato (oltre che
# vietato: non si guadagna su una policy). Si escludono per indirizzo, non per intenzione.
_amz_non_commerciali = re.compile(
    r'amazon\.[a-z.]+/(privacy|gp/help|help|conditions|cookies|legal)', re.I)
for _p in html_files():
    with open(_p, encoding="utf-8") as _fh:
        _raw = _fh.read()
    # findall dà l'href; per il rel serve il tag intero, quindi si ricerca a coppie
    _tag = re.findall(r'<a[^>]+href="[^"]*(?:amazon\.[a-z.]+|amzn\.to)[^"]*"[^>]*>', _raw)
    _href = _amz.findall(_raw)
    _coppie = [(h, t) for h, t in zip(_href, _tag) if not _amz_non_commerciali.search(h)]
    if not _coppie:
        continue
    _link = [t for _, t in _coppie]
    _senza = [a for a in _link if "sponsored" not in a and "nofollow" not in a]
    if _senza:
        err("%s: %d link Amazon senza rel sponsored/nofollow" % (rel(_p), len(_senza)))
    if "Amazon Associate" not in _raw:
        err("%s: ha %d link di affiliazione ma nessuna disclosure nel testo" % (rel(_p), len(_link)))

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
            # ⛔ Le pagine di policy di Amazon (privacy, condizioni, aiuto) sono RIFERIMENTI,
            # non link di affiliazione: metterci un tag= sarebbe sbagliato e non si guadagna
            # su una policy. Si riconoscono dall'indirizzo.
            if _amz_non_commerciali.search(href):
                continue
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
    # I confronti su /blog/ e /guides/ li fa gia' il blocco "contenuti del sito" qui sopra.
    for loc in locs:
        pezzo = loc.replace(CANONICAL_HOST, "").strip("/")
        if pezzo.startswith("blog/") and pezzo.split("/")[-1] not in blog_slugs + [""]:
            err("sitemap.xml: elenca %s che non esiste piu'" % loc)
        if pezzo.startswith("guides/") and pezzo.split("/")[-1] not in guide_slugs + [""]:
            err("sitemap.xml: elenca %s che non esiste piu'" % loc)

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
print("The Lifetime List -- controllo sito")
print("%d articoli, %d guide, %d rimandi, %d pagine HTML analizzate\n"
      % (len(blog_slugs), len(guide_slugs), len(list_slugs), len(pages)))
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
