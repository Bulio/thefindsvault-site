# Finds Vault — Amazon Associates site (memory)

## What this repo is

This is the **generated static output** for thefindsvault.com — an Amazon
Associates affiliate site. It is published to GitHub Pages from the `main`
branch. It is **not** the source of truth: the real content pipeline
(product research, copy, images, `affiliate_links.json`) lives in a
separate **private** repo called `amazon_finds`, and this site is produced
from it by `build_site.py` → `website/deploy_site.sh`.

Implication for any coding session in *this* repo: hand-editing
`products/*/index.html`, `assets/products.json`, or `sitemap.xml` directly
is a dead end — those are build artifacts and get overwritten on the next
deploy from `amazon_finds`. Real content changes belong upstream. Small,
site-only fixes (CSS, `app.js` behavior, page chrome/nav/footer, meta tags
on the static pages) are fine to make here.

## Amazon Associates mechanics

- **Associates tag**: `findsvault0e-20` — appended as `?tag=findsvault0e-20`
  on every outbound Amazon link.
- **Link format**: `https://www.amazon.com/dp/<ASIN>?tag=findsvault0e-20`
- **Required link attributes**: `target="_blank" rel="nofollow sponsored noopener"`
  on every Amazon CTA — `sponsored` is the FTC/Amazon-required rel value for
  paid/affiliate links, `nofollow` avoids passing SEO credit, `noopener`
  is the tab-hijack safety attr.
- **No cart or checkout on-site** — every product page links straight out
  to the Amazon listing; checkout happens entirely on Amazon (see
  `about.html`).
- **Disclosure**: `disclosure.html` carries the FTC-style Associates
  disclosure. The same one-line disclosure ("As an Amazon Associate, Finds
  Vault earns from qualifying purchases") also appears in the footer of
  *every* page and as `<p class="fine-print">` on each product page — keep
  all three in sync if the wording ever changes.
- **Structured data**: each product page embeds a `Product` JSON-LD block
  (`application/ld+json`) with `offers.url` pointing at the same tagged
  Amazon link, plus `aggregateRating`/`price`. Ratings/reviews/price are a
  snapshot "at time of writing" (stated in the disclosure) — they are not
  live and are not expected to be.

## Site structure

- `index.html` — homepage; the product grid is rendered client-side by
  `assets/app.js`, which fetches `assets/products.json` and infinite-scrolls
  cards in batches of 6, filterable by category pill.
- `products/<slug>/index.html` — one static page per product, each with its
  own gallery (`assets/products/<slug>/1.jpg`, `2.jpg`, …), price, star
  rating, the tagged Amazon CTA, and a "Why we picked it" features list.
- `assets/products.json` — the array driving the homepage grid: `slug`,
  `title`, `hook`, `price`, `rating`, `reviews`, `image`, `category`,
  `youtube` (nullable link to a related YouTube Short/video).
- `videos.html`, `about.html`, `disclosure.html` — static pages, same
  header/nav/footer shell as everything else.
- `sitemap.xml` / `robots.txt` — sitemap lists every static page plus every
  `products/<slug>/` URL; regenerated alongside the rest at deploy time.
- `CNAME` — intentionally **absent** right now; custom domain
  `thefindsvault.com` isn't registered yet, so GitHub Pages serves off the
  default `*.github.io` domain until it's added back (per `README.md`).

## Deploy workflow

1. Content/product changes happen in the private `amazon_finds` repo:
   `product_data/`, `scripts/*_metadata.json`, `affiliate_links.json`.
2. From there: `cd website && ./deploy_site.sh` — this runs `build_site.py`
   and pushes the regenerated static output to this repo's `main` branch.
3. GitHub Pages serves it for free straight off `main`. No CI/build step
   happens in *this* repo.
