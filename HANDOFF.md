# Handoff — Finds Vault

Stato al 2026-08-29, sera. Sostituisce la versione del mattino (commit
`2f91986`), dove i 9 interventi erano ancora tutti da fare.

## ⛔ Leggi questo prima di tutto

Il vincolo su cui era costruito il piano precedente **non esiste piu'**.
Quel piano divideva gli interventi in `[G]` (solo nel generatore privato) e
`[P]` (fattibili qui con un post-processore) perche' la sessione che lo ha
scritto vedeva solo questo repo. Chi lavora dal Mac vede **entrambi**:

    ~/Desktop/Claude/YOUTUBE_API/amazon_finds/          <- generatore + dati
    ~/Desktop/Claude/YOUTUBE_API/amazon_finds/website/  <- build_site.py, deploy_site.sh

Quindi **`scripts/postprocess.py` non e' stato scritto e non serve**: tutto e'
nel generatore, dove non puo' divergere dall'output.

Questo repo resta **output generato**. Modifiche a mano ai file del sito
vengono sovrascritte al deploy successivo.

⛔ **E il deploy cancellava i file non generati.** `deploy_site.sh` fa
`rsync -a --delete dist/ clone/ --exclude .git`: tutto quello che
`build_site.py` non produce sparisce. `scripts/`, `.github/` e `404.html`
sarebbero stati cancellati al primo deploy dopo il merge — il vecchio handoff
li dava per "sopravvissuti", ma non era vero. Ora vivono nel repo privato in
`website/site_extra/` e il deploy li ricopia **dopo** il sync.

## ✅ Fatto e verificato il 29/08

`check_site.py` sull'output rigenerato: **0 errori, 0 warning**
(prima: 2 errori, 2 warning).

| # | Intervento | Stato |
|---|---|---|
| 1 | Via i prezzi congelati | ✅ HTML, `products.json`, JSON-LD, card, correlati. CTA: "See price on Amazon →". I 3 pill `Price ↓ / Price ↑ / Under $20` tolti da `index.html` e da `recompute()`: restano **Best, Newest, Random** |
| 2 | `aggregateRating: null` | ✅ la chiave si omette quando manca. Anche `offers` e' sparito (un Offer senza price non e' valido) |
| 3 | Tracking ID per categoria | ⚠️ meccanismo pronto, **gli ID vanno ancora creati** — vedi sotto |
| 4 | Immagini | ✅ resize 800px, WebP + fallback, `width`/`height` ovunque, prima immagine `eager`+`fetchpriority` |
| 5 | Prime 12 card nell'HTML | ✅ + `app.js` non le butta via al primo giro. Provato a video: 70 card, zero doppioni, filtri e ricerca ok |
| 6 | `lastmod` in sitemap | ✅ dal registro date, non dalle mtime |
| 7 | Drip | ✅ costruito e collaudato, **interruttore spento** — vedi sotto |
| 8 | Slug nel commit | ✅ `deploy_site.sh` li ricava dai prodotti nuovi (`Aggiorna sito: +owala_bottle`) |
| 9 | `404.html` nel generatore | ✅ generata da `page()`, link root-relative, `noindex` |

### Numeri delle immagini (punto 4)

| | prima | dopo |
|---|---|---|
| JPG medio | 138 KB | **71 KB** |
| WebP medio | — | **46 KB** |
| Pagina prodotto (6 foto) | ~830 KB | **~280 KB** |
| `banner.png` (og:image) | 1169 KB | **33 KB** (ora `banner.jpg`, 1200px) |
| `logo.png` | 355 KB | ~50 KB (192px) |
| Immagini senza `width`/`height` | 839 | **0** |
| Durata di un build | ~3 minuti | **1,4 secondi** |

⭐ Il secondo numero e' il piu' utile: le immagini ottimizzate stanno in
`website/.cache_img/`, validata **sui byte del sorgente, non sulle mtime**
(la cartella e' dentro iCloud, che le mtime le riscrive). Il build ricopia
invece di rilavorare. Un deploy ora e' istantaneo.

⛔ **Pillow c'era gia'.** Il vecchio handoff lo dava per assente: era stato
cercato nell'ambiente sbagliato. `python3` di sistema — quello che lancia
`deploy_site.sh` — ha Pillow 10.4.0. Il `.venv` del progetto no, ma il build
non lo usa.

## ⚠️ Punto 3 — i tracking ID esistono come mappa, non come ID

`amazon_finds/tracking_ids.json` mappa le 9 categorie a un tag. **Tutte e 9
sono ancora sul tag storico `findsvault0e-20`**, che funziona e paga.

⛔ Un `tag=` che non esiste nell'account Associates **non traccia e non paga
la commissione**. Gli ID vanno creati PRIMA nella dashboard
(Account > Manage Tracking IDs), poi scritti qui, **una categoria alla volta**.
Ogni build stampa quante categorie sono ancora sul tag storico.

## 🚦 Punto 7 — il drip c'e', ma e' spento

Interruttore: `"drip": true` in `amazon_finds/catalogo_date.json`.
E' spento apposta: acceso, un prodotto nuovo **non esce piu' il giorno
stesso**, e quello cambia un'abitudine di lavoro. Va acceso quando decidi tu.

Acceso, un prodotto nuovo nasce `queued`: la pagina si genera lo stesso ma con
`noindex`, e resta fuori da home, filtri, correlati, videos e sitemap. Poi:

```bash
python3 pubblica_prossimo.py                # dice chi uscirebbe, non tocca niente
python3 pubblica_prossimo.py --fai --deploy # lo fa uscire e ripubblica
```

Ordine di uscita: quello di inserimento in `affiliate_links.json`.
Collaudato: 2 messi in coda → spariti da home/sitemap/correlati, pagina
`noindex`; `--fai` ne rilascia uno; il registro vero e' stato ripristinato.

⛔ **Il cron NON e' stato installato.** Un lavoro che ogni giorno pubblica e
pusha da solo e' un'automazione permanente: la accende l'utente. Con il drip
acceso, la riga da agganciare alla catena giornaliera e':
`cd .../amazon_finds/website && python3 pubblica_prossimo.py --fai --deploy`

⭐ E oggi non servirebbe comunque a niente: i 70 prodotti sono **tutti gia'
pubblicati**, la coda e' vuota. Il drip vale dal prossimo lotto in poi.

## ⏸️ Ancora aperto

- **Niente e' andato online.** Tutto quanto sopra e' nel repo privato e
  verificato in locale: il sito vivo mostra ancora i prezzi. Serve
  `cd website && ./deploy_site.sh`, che ora si ferma da solo se
  `check_site.py` trova errori.
- **Rating e recensioni sono ancora li'.** Stelle e `(45,289)` sulle card sono
  dati Amazon congelati esattamente come lo era `$29.99`. ⛔ Toglierli ha un
  costo preciso, che il vecchio handoff non diceva: **l'ordinamento "Best" e'
  rating desc + reviews desc**, e senza rating resterebbero solo Newest e
  Random. Sparirebbero anche il badge "Top Rated", la scelta della foto nei
  tile in evidenza e l'ordine dei prodotti correlati. Decisione da prendere,
  non da eseguire di slancio.
- **Nessuna analytics.** I tracking ID coprono le conversioni Amazon, non il
  traffico.
- **Liveness degli ASIN**: `check_site.py` non contatta Amazon apposta (dai
  runner GitHub arrivano 503/captcha). Va fatto via PA-API o da IP
  residenziale.
- **Categorie sbilanciate**: `Style` 2 prodotti, `Pets` 5.

## Comandi

```bash
cd ~/Desktop/Claude/YOUTUBE_API/amazon_finds/website
python3 build_site.py                 # 1,4 s
python3 dist/scripts/check_site.py    # 0 errori attesi
./deploy_site.sh                      # build + check + push (si ferma sugli errori)
```
