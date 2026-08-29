# Finds Vault — website

Sito statico generato da `build_site.py` (nel progetto privato
`amazon_finds`). Per aggiornare:

1. Aggiungi il nuovo prodotto ai dati esistenti (`product_data/`,
   `scripts/*_metadata.json`, `affiliate_links.json`).
2. `cd website && ./deploy_site.sh`

Nessun pagamento/carrello: ogni pagina prodotto linka direttamente ad
Amazon con il tag Associates. GitHub Pages serve tutto gratis dalla
branch `main`, dominio custom via file `CNAME` (rimosso finche' il
dominio thefindsvault.com non e' registrato).

## Controllo integrita'

`python3 scripts/check_site.py` verifica l'output generato: link interni e
immagini rotte, pagine prodotto orfane, coerenza fra `products.json`,
`sitemap.xml` e le cartelle su disco, canonical sul dominio giusto, link
Amazon con tag affiliate e `rel="sponsored nofollow"`, JSON-LD valido.
Esce con codice 1 se trova errori. Gira da solo a ogni push e ogni lunedi'
(`.github/workflows/site-check.yml`).

Non contatta Amazon: da GitHub Actions le richieste vengono bloccate con
503/captcha e otterresti solo falsi positivi. La verifica che gli ASIN
siano ancora vivi va fatta via PA-API o da un IP residenziale.
