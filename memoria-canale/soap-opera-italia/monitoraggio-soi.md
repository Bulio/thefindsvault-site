# SOAP OPERA ITALIA — Monitoraggio SEPARATO (avviato 11/8/2026, sessione cloud)

> ⚠️ **BINARIO SEPARATO da Serie TV Fans** (direttiva utente 11/8): file, tabelle e
> check propri in `memoria-canale/soap-opera-italia/`. MAI mischiare dati SOI nei
> file STF e viceversa.
> Canale: **@soapoperaitaliaa** (`UCjid0Q5NC0No3HRHIF2_tdg`) — attenzione:
> esiste un omonimo concorrente più grande (@SoapOperaItalia, 310 iscritti,
> 45,5K viste): il nostro ha la doppia A finale.

## Baseline (rilevata 11/8/2026 ~12:00, SOLO dati pubblici)

- **2 iscritti** · 4.196 viste totali · 38 video · creato 13/6/2025, IT.
- Nicchia identica a STF (keywords: Forbidden Fruit, La Promessa, Hercai,
  Far Away, Beautiful, Paradiso) ma **canale di fatto invisibile**: gli ultimi
  25 video fanno **0–14 viste ciascuno**.
- Produzione recente intensa (~3 video/giorno dal 4/8), durata 4–10 min, angoli
  "saggio/opinione": "la mia reazione a caldo", "le teorie dei fan vs realtà",
  "ricostruito passo dopo passo", "5 indizi", "mettiti alla prova".
- ⚠️ **NON collegato a NexLev** → da qui niente retention/durata media/analytics
  interne. Collegarlo su dashboard.nexlev.io (account NexLev) per avere su SOI
  le stesse metriche di STF. Fino ad allora: solo viste/commenti pubblici.

## Osservazioni strategiche (evidenze, decisioni all'utente/Mac)

1. **Mix serie disallineato dalle lezioni STF**: il grosso della produzione
   recente è su HERCAI (serie FINITA) e Paradiso delle Signore (esclusa su STF
   perché faceva 40–130 viste). Le serie vive e ricercate (TPLMF, FF, FA) sono
   quasi assenti. Un canale a 2 iscritti vive SOLO di ricerca → servono soggetti
   che la gente cerca ADESSO.
2. **Sovrapposizione con STF** su La Promessa/FF: da chiarire il posizionamento
   (SOI = secondo canale sulla stessa nicchia? serie diverse? formato diverso?).
   Rischio di competere con se stessi nelle stesse ricerche.
3. **Titoli da search assente**: gli angoli "reaction/saggio" funzionano sui
   canali con pubblico (browse); a 2 iscritti serve il magnete di ricerca
   (serie + evento cercato; su STF le date settimanali — qui da decidere in
   coerenza con la regola evergreen).
4. Volume attuale (~3/g) senza distribuzione = lavoro a vuoto: valgono anche qui
   qualità > quantità e il rituale di lancio.

## Criteri di misura SOI (scala da canale zero — baseline propria, NON quella STF)

| # | Metrica | Baseline attuale | Target progresso (4 settimane) |
|---|---|---|---|
| 1 | Viste a 48h/video | 0–14 | ≥50 |
| 2 | Iscritti | 2 (fermi) | ≥30 |
| 3 | Commenti/video | 0 | ≥2 |
| 4 | % video sopra 100 viste lifetime | ~0% recenti | ≥25% |

## Piano check (separato da STF)

- **Check SOI**: ogni 3–4 giorni ~10:30 Italia (sfalsato dai check STF).
  Primo: VEN 14/8. Aggiorna SOLO i file di questa cartella.
- Contenuto check: viste dei nuovi video, iscritti, mix serie pubblicato,
  segnali di ricerca (quali titoli raccolgono qualcosa), tabella criteri.
- Quando NexLev sarà collegato: aggiungere durata media/retention come su STF.

## 🔌 AGGANCIO NEXLEV — autorizzato dall'utente (11/8)

- **Account Google del canale: `bulio91veo3@gmail.com`** (fornito dall'utente).
- Procedura (browser, ~2 min — la fa l'utente o la sessione Mac che ha il
  browser; il cloud non può completare l'OAuth Google):
  1. dashboard.nexlev.io/analytics → "Connect channel"
  2. Login Google con `bulio91veo3@gmail.com` → scegliere "Soap Opera Italia"
     (@soapoperaitaliaa) → autorizzare la lettura analytics.
- Al primo check dopo l'aggancio, la sessione cloud verifica con
  `list_my_youtube_channels` che il canale compaia e attiva le metriche complete
  (durata media, retention) come su STF.

## Richieste alla sessione Mac (per completare il binario)

1. **Eseguire l'aggancio NexLev qui sopra** (browser + account bulio91veo3).
2. Esportare la memoria SOI (strategia, pipeline, che ruolo ha il canale) in
   `memoria-canale/soap-opera-italia/memoria-mac-soi/` — qui non c'è NULLA su
   SOI e senza contesto i check misurano al buio.
3. Decidere il posizionamento vs STF (punto 2 delle osservazioni) e il mix serie.

## Log dei check

- **CHECK #0 — MAR 11/8 ~12:20 Italia (sessione cloud, su richiesta utente).**
  - Aggancio NexLev: ❌ non ancora attivo (SOI assente dai 10 canali collegati)
    → procedura in questo file, da eseguire con `bulio91veo3@gmail.com`.
  - Dati pubblici: 2 iscritti · 4.196 viste totali · 38 video.
  - Ultimi video: La Promessa "padre di Jana, cosa può succedere" (oggi, 4:28)
    0 viste · "verità indizio per indizio" (ieri, 4:01) 1 vista · Paradiso
    "finale/decima stagione" (ieri, 9:20) 9 viste · best recente: Paradiso
    "prima e dopo il finale" (9/8) 14 viste.
  - Mix serie ultimi 25 video: ~14 Hercai (serie finita), ~6 Paradiso, ~4
    La Promessa, 1 altro. Zero su TPLMF/FF/FA.
  - Criteri: tutti a baseline (viste 0–14 ❌ · iscritti 2 ❌ · commenti 0 ❌ ·
    % sopra 100 viste ~0% ❌). Prossimo check: VEN 14/8 ~10:30 (già armato).
