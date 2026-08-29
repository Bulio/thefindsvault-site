# Finds Vault — website

Sito statico generato da `build_site.py` (nel progetto privato
`amazon_finds`). Per aggiornare:

1. Aggiungi il nuovo prodotto ai dati esistenti (`product_data/`,
   `scripts/*_metadata.json`, `affiliate_links.json`).
2. `cd website && ./deploy_site.sh`

⛔ Questo repo e' **output generato**: qualunque modifica fatta a mano ai
file del sito viene sovrascritta al deploy successivo. Le uniche eccezioni
sono i file in `site_extra/` del repo privato (`scripts/`, `.github/`,
`HANDOFF.md`), che il deploy ricopia dopo il sync.

Nessun pagamento/carrello: ogni pagina prodotto linka direttamente ad
Amazon con il tag Associates. GitHub Pages serve tutto gratis dalla
branch `main`, dominio custom via file `CNAME`.
