# Finds Vault — website

Sito statico generato da `build_site.py` (nel progetto privato
`amazon_finds`). Per aggiornare:

1. Aggiungi il nuovo prodotto ai dati esistenti (`product_data/`,
   `scripts/*_metadata.json`, `affiliate_links.json`).
2. `cd website && python3 build_site.py`
3. Copia il contenuto di `website/dist/` qui dentro e fai push su `main`.

Nessun pagamento/carrello: ogni pagina prodotto linka direttamente ad
Amazon con il tag Associates. GitHub Pages serve tutto gratis dalla
branch `main`, dominio custom via file `CNAME`.
