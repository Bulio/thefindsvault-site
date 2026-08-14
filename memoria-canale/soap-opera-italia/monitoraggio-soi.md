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

- **CHECK #1 — VEN 14/8 ~10:40 Italia (sessione cloud).**
  - **Aggancio NexLev: ❌ ancora non fatto** (SOI assente dai 10 canali
    collegati) → niente durata media/retention. Secondo sollecito.
  - **Crescita forte in 3 giorni**: iscritti **2 → 9** · viste totali
    **4.196 → 11.998 (+7.802)** · video 38 → 54.
  - ⚠️ **MA le viste NON vengono dai video lunghi**: i 25 lunghi più recenti
    sommano **959 viste in totale**. La crescita è quasi tutta **SHORTS**:
    21 short con 114–1.200 viste l'uno (~10.400 viste complessive).
    Top: "Il segreto viene fuori" 1,2K · "Yildiz non se lo aspettava" 949 ·
    "Il piano di Ender" 925. Molti su TERRA AMARA (serie finita ma ancora
    molto cercata) e Forbidden Fruit.
  - **Unico lungo che ha funzionato**: LP "La mia reazione a caldo alla
    rivelazione sul padre di Jana" (4:00 di durata, 3:51) → **754 viste**,
    cioè il 79% di tutte le viste dei lunghi recenti. Gli altri stanno a 0–41.
    Nota: è lo stesso filone ("padre di Jana") che su STF è storicamente il
    video più visto in assoluto (161K lifetime) → **il tema tira, non il canale**.
  - Mix serie lunghi ultimi 25: ~13 Hercai (finita), ~5 Paradiso, ~7 La Promessa.
    **Zero TPLMF/FF/FA** nei lunghi (FF appare solo negli Shorts).
  - Commenti: 0 su tutti.

  | Criterio | Baseline 11/8 | Oggi 14/8 | Target 4 sett. |
  |---|---|---|---|
  | Viste 48h/video (lunghi) | 0–14 | 0–28 (outlier 754) | ≥50 |
  | Iscritti | 2 | **9** ↑ | ≥30 |
  | Commenti/video | 0 | 0 | ≥2 |
  | % lunghi sopra 100 viste | ~0% | ~4% (1 su 25) | ≥25% |

  - **LETTURA**: gli Shorts stanno portando il traffico, i lunghi restano
    invisibili. Su SOI (a differenza di STF) gli Shorts sono l'unico canale
    di distribuzione che funziona — ma non convertono in viste sui lunghi.
  - **RACCOMANDAZIONI (decide utente/Mac)**: 1) collegare gli Shorts ai lunghi
    (stesso soggetto, rimando esplicito, playlist) invece di produrli su serie
    diverse; 2) spostare i lunghi dai finali di Hercai/Paradiso ai temi che
    tirano davvero (il caso "padre di Jana" lo dimostra: 754 vs 0-41);
    3) il formato lungo di SOI è 4-9 min — se si vuole replicare la lezione
    STF servono video più lunghi e verticali sul tema cercato.

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
