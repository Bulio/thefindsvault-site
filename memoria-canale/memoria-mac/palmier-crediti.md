---
name: palmier_credit_monitoring
description: DIRETTIVA 07/08 - Palmier Pro attivo ($29, 5.000cr/mese) come corsia
  UNICA immagini; OGNI generazione va registrata nel ledger per l'analisi consumi
  che l'utente chiederà a giorni
metadata:
  type: feedback
  originSessionId: current
  modified: 2026-08-07 00:33:12.374000+00:00
permalink: palmier-credit-monitoring
---

Direttiva utente 07/08 (subito dopo aver attivato il piano Pro): "Utilizziamolo unicamente per adesso. Vediamo quanto dura e se supporta tutta la produzione. Monitora i consumi perché fra qualche giorno faremo paragoni e analisi."

**How to apply (OGNI sessione che genera immagini/video/audio via Palmier):**
1. **Corsia unica**: tutte le immagini si generano su Palmier — niente ChatGPT (nemmeno Go) salvo emergenza dichiarata all'utente. Obiettivo: misurare se 5.000cr/mese coprono la produzione reale.
2. **Ledger obbligatorio**: dopo ogni `generate_*`, aggiungere una riga a `~/Desktop/Claude/palmier_credit_ledger.tsv` (data, modello, risoluzione, scopo, crediti stimati). Se l'utente comunica il contatore reale dell'app, riportarlo nella colonna crediti_reali e ricalibrare le stime.
3. **Costi reali per modello sconosciuti** (Palmier non li pubblica): la calibrazione avviene confrontando il contatore dell'app (menu account, in alto a destra) con le righe del ledger — chiedere il numero all'utente ogni manciata di generazioni, non a ogni singola.
4. **Analisi attesa a giorni**: consumo cumulativo, media per immagine per modello, proiezione fine mese (bastano i 5.000cr? serve Max?), confronto con i vecchi costi ChatGPT/Horacle. I dati del periodo gratis (8 img ≈ 250cr, media ~30cr/img mix premium) sono le prime righe del ledger.
5. Contesto strategia: [[decisione_switch_horacle_palmier_immagini]] (Palmier primario, Go piano B sospeso per ora, Plus in disdetta post-validazione), [[palmier_pro_new_capabilities_audit]] (ricetta produzione), [[feedback_immagini_sempre_senza_scritte_originali]] (no-text obbligatorio).