# Handoff — Finds Vault

Stato al 2026-08-29. Branch: `claude/profilo-personale-lavoro-uobr34`.

## Contesto

Questo repo e' **output generato**, non sorgente. Il generatore e'
`build_site.py` nel repo privato `amazon_finds`; si pubblica con
`cd website && ./deploy_site.sh`. Qualunque modifica fatta a mano ai file
generati (`index.html`, `products/*/index.html`, `sitemap.xml`,
`assets/products.json`, immagini) **viene sovrascritta al prossimo deploy**.

Sopravvivono solo i file che il generatore non tocca: `CNAME`, `.nojekyll`,
`google7ea776b0abf39557.html`, `404.html`, `scripts/`, `.github/`.

## Gia' fatto e pushato

Commit `9c10aae`:

- **`scripts/check_site.py`** — controllo integrita' dell'output generato:
  link interni e `<img>` rotti (anche root-relative), pagine prodotto
  orfane, coerenza `products.json` <-> `sitemap.xml` <-> cartelle su disco,
  canonical sul dominio di produzione, link Amazon con tag affiliate e
  `rel="sponsored nofollow"`, JSON-LD parsabile e senza chiavi a `null`.
  Exit 1 su errori. Testato simulando 4 regressioni reali (canonical
  ribaltato su github.io, link interno rotto, prodotto tolto dal JSON con
  cartella rimasta, tag affiliate saltato): le rileva tutte.
- **`.github/workflows/site-check.yml`** — lo esegue a ogni push e ogni
  lunedi' 07:00 UTC.
- **`404.html`** — mancava. Usa link root-relative (obbligatorio: GitHub
  Pages la serve da URL a profondita' arbitraria).

### Cosa trova oggi

```
ERRORE  products/owala_bottle/index.html: JSON-LD "aggregateRating": null
ERRORE  products/stanley_quencher/index.html: JSON-LD "aggregateRating": null
WARN    839 immagini su 75 pagine senza width/height
WARN    70 immagini sopra 200 KB (57.4 MB totali); banner.png da 1169 KB
WARN    sitemap.xml senza lastmod
```

## Audit — numeri di partenza

| | |
|---|---|
| Prodotti | 70, tutti con video YouTube collegato |
| Immagini | 415 JPG, media 138 KB, **57.4 MB**; nessun WebP, nessun resize |
| `width`/`height` | 0 su 839 immagini |
| Analytics | **nessuna** (ne' GA, ne' Plausible, ne' altro) |
| Tracking ID Associates | **uno solo**, `findsvault0e-20`, su tutti i 140 link |
| Home page | zero prodotti nell'HTML, tutto da `fetch(products.json)` |
| Sitemap | 74 URL, zero `lastmod` |
| JS | 195 righe, zero dipendenze, zero build step |
| `rel` sui link Amazon | gia' corretto (`nofollow sponsored noopener`) |

## Da fare — i 9 interventi

Legenda destinazione:
**[G]** = solo in `build_site.py` (repo privato)
**[P]** = fattibile qui via post-processore idempotente chiamato da
`deploy_site.sh` dopo `build_site.py`

### 1. [P/G] Togliere i prezzi — priorita' massima

Ogni pagina mostra un prezzo congelato al giorno della generazione
(`$29.99` su Owala, scritto il 6 agosto). L'Operating Agreement Amazon
Associates vuole prezzo e disponibilita' dalla PA-API con orario di
recupero e disclaimer. Un prezzo scraped e statico su 70 pagine e' una
causa tipica di chiusura account — che azzera tutto il sito, non una pagina.

Scelta fatta: **rimozione**, non PA-API.

Da fare:
- pagine prodotto: via il blocco `<p class="price-big">`, al suo posto la
  CTA `See price on Amazon →`
- `assets/products.json`: rimuovere `price` e `priceNum`
- `assets/app.js`: nella card, `<span class="price">` diventa un
  affordance testuale senza cifra
- **conseguenza da non dimenticare**: i pill di ordinamento
  `price-low`, `price-high` e `under20` restano senza dato. Vanno tolti da
  `index.html` e i rispettivi rami da `recompute()` in `app.js`.
  Restano `Best`, `Newest`, `Random`.
- JSON-LD: un `Offer` senza `price` non e' valido. Togliere l'intero blocco
  `offers` e tenere `Product` con `name`/`image`/`description`/`url`
  (`url` = canonical della pagina prodotto).

**Ancora aperto, non incluso in questo giro:** rating e numero di recensioni
sono anch'essi dati Amazon congelati (stelle e `(45,289)` sulle card).
Stessa categoria di rischio del prezzo. Non toccati perche' fuori dallo
scope confermato.

### 2. [G] `aggregateRating: null`

`build_site.py` deve **omettere la chiave** quando il valore manca, non
emetterla a `null`. Structured data con `null` viene scartato da Google e
segna un errore sul dominio. Dopo il fix `check_site.py` passa verde.

Nota a parte: marcare `aggregateRating` per prodotti che non vendi tu e'
comunque contro le linee guida Google sulle self-serving reviews. La scelta
migliore e' non emetterlo affatto.

### 3. [P] Tracking ID per categoria

Oggi tutti i link usano `tag=findsvault0e-20`: non c'e' modo di sapere
quale prodotto o categoria converte, quindi le scelte editoriali sono a
intuito quando Amazon darebbe il dato gratis.

Obiettivo: `findsvault-{category}-20` derivato dal campo `category` gia'
presente in `products.json`.

> **ATTENZIONE — rischio ricavi.** I tracking ID devono **prima** essere
> creati nella dashboard Amazon Associates. Un `tag=` che non esiste
> nell'account non traccia e **non paga la commissione**. Non riscrivere i
> tag prima di aver creato gli ID.
>
> Implementazione sicura: un file `scripts/tracking_ids.json` che mappa
> categoria -> tag, inizializzato con `findsvault0e-20` per tutte e 9 le
> categorie (Beauty, Fitness & Outdoor, Home, Hydration, Kids & Play,
> Kitchen, Pets, Style, Tech). Si sostituiscono le voci man mano che gli ID
> vengono creati. `check_site.py` va esteso per verificare che ogni `tag=`
> presente nell'HTML sia nella mappa.

### 4. [P] Immagini

57.4 MB, media 138 KB, la peggiore 405 KB, `banner.png` da 1169 KB. Una
pagina prodotto scarica 6 foto full-size. Nessuna immagine ha
`width`/`height` -> layout shift su tutto il sito.

- resize a max 800px lato lungo, JPEG qualita' ~82
- generare `.webp` accanto e servirlo con `<picture>` + fallback JPG
- `width`/`height` sempre presenti
- la prima immagine visibile (hero / prima card / prima foto galleria):
  `loading="eager" fetchpriority="high"` al posto di `loading="lazy"`
  — oggi l'immagine LCP e' lazy, che e' il modo esatto di rallentarla
- comprimere `banner.png` (e' solo l'`og:image`, non serve 1.1 MB)

Serve Pillow: **non e' installato nell'ambiente**, va aggiunto
(`pip install Pillow`) sia in locale sia nel workflow se il resize gira in CI.

Nota: il resize in place lascia comunque i blob originali nella storia git,
il `.git` non si sgonfia. Il guadagno e' sulla banda servita agli utenti.

### 5. [P] Prime card nell'HTML

La home non contiene un solo prodotto: tutto arriva da
`fetch('assets/products.json')`. Google esegue il JS ma in un secondo
passaggio e con meno priorita'.

Il post-processore stampa le prime 12 card (ordinamento `best`:
rating desc, poi reviews desc) direttamente in `#grid`.
`app.js` va adattato: al primo giro, se ci sono card pre-renderizzate e
`activeCat === 'All' && activeSort === 'best' && !query`, **non** fare
`grid.innerHTML = ''` — impostare `shown` al numero di card gia' presenti e
continuare ad appendere da li'. Il reset resta su ogni interazione utente.

Attenzione al drift: il markup generato dal post-processore deve
rispecchiare `cardHTML()` in `app.js`. Se uno dei due cambia, cambiare
anche l'altro.

### 6. [P] `lastmod` in sitemap

Il sito promette *"new ones drop daily"* ma la sitemap non ha un solo
`<lastmod>`: non c'e' modo di dire a Google che e' uscito qualcosa.
Popolarlo dalla data di pubblicazione del prodotto.

### 7. [P+G] Drip: disaccoppiare produzione e pubblicazione

**E' l'intervento che sposta di piu' l'ago.** Pattern di lavoro osservato:
45 commit su 50 in tre giorni (6-7-8 agosto), poi nove giorni di silenzio,
poi 5 commit sparsi. Il sito ha bisogno di cadenza quotidiana; tu lavori a
raffiche. Non vanno messi d'accordo cambiando abitudini, ma mettendo una
coda in mezzo.

- **[G]** `build_site.py` aggiunge a ogni prodotto un flag `queued: true`
  quando viene generato in blocco
- **[P]** `scripts/publish_next.py`: prende il prodotto in coda con `order`
  piu' basso, mette `queued: false` e `publishedAt` a oggi
- **[P]** le pagine dei prodotti ancora in coda ricevono
  `<meta name="robots" content="noindex">` finche' non escono
- **[P]** `.github/workflows/daily-drip.yml`: cron giornaliero che esegue
  `publish_next.py`, rigenera la sitemap e committa

Risultato: produci 15-20 prodotti in una sessione di sprint, il sito ne
pubblica uno al giorno per tre settimane.

### 8. [G] Slug nel commit message

44 commit su 50 hanno lo stesso identico messaggio autogenerato
(`Aggiorna sito: nuovo prodotto/video (timestamp)`): la storia e'
illeggibile e `git bisect` inutilizzabile. In `deploy_site.sh`, passare lo
slug: `Aggiorna sito: +owala_bottle`.

### 9. [G] `404.html` nel generatore

Copiare `404.html` (gia' in questo repo) nell'output di `build_site.py`,
altrimenti prima o poi un deploy la porta via.

## Approccio consigliato: `scripts/postprocess.py`

Tutti i punti marcati [P] possono stare in un unico script **idempotente**
invocato da `deploy_site.sh` subito dopo `build_site.py`, senza toccare il
repo privato:

```
build_site.py            # genera il sito come adesso
python3 scripts/postprocess.py   # <-- una riga da aggiungere
python3 scripts/check_site.py    # blocca il deploy se qualcosa e' rotto
git add -A && git commit && git push
```

Ordine delle trasformazioni dentro `postprocess.py`:

1. prezzi via (HTML, `products.json`, JSON-LD, pill di ordinamento)
2. chiavi `null` via dal JSON-LD
3. riscrittura `tag=` da `scripts/tracking_ids.json`
4. immagini: resize, WebP, `width`/`height`, `eager`+`fetchpriority`
5. iniezione delle prime 12 card in `index.html`
6. `lastmod` in `sitemap.xml`
7. `noindex` sui prodotti ancora in coda

Idempotenza obbligatoria: gira a ogni deploy, deve poter girare due volte
di fila senza cambiare nulla la seconda.

**Non ancora iniziato.** Al momento dell'handoff era stata fatta solo la
verifica delle dipendenze (Pillow assente).

## Fuori dai 9 punti, ancora aperto

- **Nessuna analytics.** Va aggiunto qualcosa (Plausible o GA4) o resti
  cieco sul traffico anche dopo aver sistemato i tracking ID, che coprono
  solo le conversioni Amazon.
- **Rating e recensioni congelati** — vedi nota al punto 1.
- **Liveness degli ASIN.** `check_site.py` non contatta Amazon di
  proposito: dai runner GitHub le richieste tornano 503/captcha e sarebbero
  solo falsi positivi. La verifica che i 70 ASIN siano ancora acquistabili
  va fatta via PA-API o da un IP residenziale. Un link morto e' traffico
  convertito a zero senza che nessuno se ne accorga.
- **Categorie sbilanciate**: `Style` ha 2 prodotti e `Pets` 5 — filtri
  quasi vuoti.

## Comandi

```bash
python3 scripts/check_site.py        # exit 1 se ci sono errori
git log --oneline -5
```
