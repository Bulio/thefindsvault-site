# TEST NUOVO FORMATO — Monitoraggio (TPLMF, SAB 8/8/2026 ore 18:00)

> ⚡ **SUPERATO DALLA DIRETTIVA UTENTE 8/8 SERA (~17:15, sessione Mac): "inizia a
> pubblicare nuovo formato senza test, cambiamo già strategia."** Il test TPLMF
> NON è più decisionale: la notturna è già stata riconfigurata a 1 batch/notte
> nuovo formato DA STANOTTE (9/8 05:00), e il video FF 10–14 ago è programmato
> per DOM 9/8 ore 9:00. I check 19:00/24h/48h restano UTILI come misura
> (baseline nuovo formato), quindi la sessione cloud li faccia comunque e
> committi i numeri qui — ma nessuna decisione dipende più dall'esito.

## Video sotto test

- Serie: Tutto per la mia famiglia (TPLMF)
- Uscita: sabato 8 agosto 2026, ore 18:00 (Italia)
- Formato: 18–25 min, formula competitor (hook spoiler 0:00–0:45, loop aperto,
  5 blocchi da 2,5 min, CTA teoria al min 10, chiusura troncata)
- Video ID: _da rilevare al primo check dopo la pubblicazione_
- **Video 2 del batch (FF 10-14 ago): ID k_Usdt_aAvI, programmato DOM 9/8 9:00, durata 15:10**

## Criteri di verifica a 48h (passa con ≥2/4)

| # | Criterio | Soglia | Baseline vecchio formato |
|---|----------|--------|--------------------------|
| 1 | Retention al minuto 1 | ≥65% | ~50% |
| 2 | Durata media visione | ≥5:00 | ~2:20–2:47 (140–167 sec, longs recenti) |
| 3 | Viste a 48h | ≥1.500 | 150–400 (storico); longs recenti 1–3K in 2–5 gg |
| 4 | Commenti | ≥30 | 0–12 nelle prime 48h (best: FF 12) |

## Baseline canale pre-test (rilevata 8/8/2026 ~16:30 via NexLev)

- Viste/giorno ultimi 5 gg: 33.9K (spike recupero) · 4.6K · 10.5K · 10.4K · 6.5K
  → media 7gg ~9.700/g. **Già sopra la baseline 2.200/g scritta in memoria** —
  trend in accelerazione da fine luglio (rimonetizzazione + Forbidden Fruit).
- Top long-form 1–8 agosto (viste nel periodo / durata media):
  - Forbidden Fruit "Sono vivo" (28/7): 8.516 / 2:39 — lifetime 24.4K, 60 commenti
  - Forbidden Fruit "Halit si porta via il bambino" (31/7): 4.695 / 2:32
  - Far Away "Cihan rifiuta il divorzio" (3/8): 3.108 / 2:47 — 21 commenti lifetime
  - La Promessa "Santos confessa" (30/7): 3.077 / 2:27
- Iscritti: 60.100. Viste totali: 14,11M.

## Piano dei check (sessione cloud, automatici)

1. **Check 0 — 8/8 ~19:00 Italia**: video pubblicato? Rilevare video ID, prime viste/commenti.
2. **Check 24h — 9/8 ~18:00 Italia**: viste, durata media, curva retention (min 1), commenti.
3. **Check 48h — 10/8 ~18:30 Italia**: VERDETTO sui 4 criteri → raccomandazione
   riconfigurazione notturna (1 batch/notte nuovo formato dal 17/8) o mantenimento.

## Log tempi di produzione nuovo formato (per ritarare la notturna)

| Data | Fase | Tempo | Note |
|------|------|-------|------|
| 8/8 cloud | Scelta soggetto + anti-duplicati | ~3 min | Video 2 batch (FF 10–14 ago) |
| 8/8 cloud | Script completo 20 min (2.474 parole) | ~7 min | 2 passate, formula completa |
| 8/8 cloud | TTS | n/d | Bloccata in cloud (proxy + Horacl 16cr). Da misurare sul Mac |
| 8/8 Mac | Estrazione narrazione + dispatch TTS | ~2 min | 14.779 caratteri; corsia CPU locale (Kaggle semaforo attivo); pause 0.7/1.3 |
| 8/8 Mac | TTS Chatterbox (CPU) | 68 min (17:04→18:12) | 14.779 char → 15:10 di audio (910s). Ritmo reale con pause 0.7/1.3: ~16.2 char/s |
| 8/8 Mac | Immagini 50/50 (video FF) | ~5 min | 10 generate Palmier nano-banana-lite con reference volti + 10 riusate libreria FORBIDDEN. Qualità verificata a campione |
| 8/8 Mac | Thumbnail | ~2 min | Sfondo Palmier nano-banana-pro (3 reference: Feride+Yildiz+HasanAli) + overlay make_thumb_cinema.py "LI HA VISTI" / "FERIDE SCOPRE TUTTO" + badge |
| 8/8 Mac | Montaggio (h264_videotoolbox) | 4,5 min (18:12→18:17) | 140 clip, 20 immagini ciclate, sub sync, musica, logo. Validazione ffmpeg pulita |
| 8/8 Mac | Upload+thumbnail+programmazione | ~3 min | Progetto quota SDOPPIA. **Video ID k_Usdt_aAvI, PROGRAMMATO DOM 9/8 ORE 9:00** |
| — | **TOTALE Mac (esclusa scrittura script)** | **~85 min** | di cui 68 non presidiati (TTS). Con corsia Kaggle il TTS scenderebbe a ~20-25 min |

## Log dei check

- **RICONTROLLO — 8/8 20:07 Italia: TPLMF ANCORA NON PUBBLICATO → TEST CHIUSO
  COME SALTATO** (coerente con la direttiva utente: nuovo formato attivo senza
  test). Il monitoraggio passa ai primi nuovo formato reali:
  **FF `k_Usdt_aAvI` (DOM 9/8 9:00)** → check 24h LUN 10/8 ~9:30 ·
  **FA (DOM 9/8 18:30)** → check 48h FF + 24h FA MAR 11/8 ~10:00.
  Stessi 4 criteri della tabella come metro (misura, non decisione).
  Se TPLMF uscisse più avanti, trattarlo come video normale del nuovo formato.
- **CHECK 0 — 8/8 19:02 Italia: VIDEO NON PUBBLICATO.** Nessun video TPLMF sul
  canale; l'upload più recente risale a ~7 ore prima. Utente avvisato (chat +
  push). Ricontrollo automatico alle ~20:05 Italia. Nota a margine: oggi risultano
  usciti 3 video vecchio formato (8–9 min) verso le 12:00–14:30 — FF "Ender",
  La Promessa "Leocadia/Ángela", FF "Hasan Ali holding" (titoli visti in
  auto-traduzione inglese dallo scraper, da confermare).
