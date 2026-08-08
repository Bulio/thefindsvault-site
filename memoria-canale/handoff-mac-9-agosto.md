# HANDOFF → SESSIONE MAC (aggiornato 8/8/2026 sera, dalla sessione cloud)

> Da leggere nella chat/pipeline del Mac. Tutto ciò che serve è committato sul
> branch `claude/analisi-grafico-storico-fvwaqt` di thefindsvault-site.

## ⓪ DECISIONE UTENTE (8/8 sera): IL LAVORO OPERATIVO SI SPOSTA SUL MAC

- L'utente vuole lavorare "come sempre su Claude che ha accesso a tutto" → il Mac.
- Il Mac deve fare `git pull` di questo branch e ripartire da questo file.
- **RICHIESTA MEMORIA (importante)**: la sessione cloud NON vede la memoria Claude
  del Mac (checkpoint, `_storico_video.md`, istruzioni Palmier, feedback corsie).
  Al prossimo giro, la sessione Mac copi/esporti in `memoria-canale/` di questo
  branch i file di memoria essenziali (o un estratto), così ogni sessione — cloud
  o Mac — lavora sulle stesse istruzioni. Priorità: istruzioni Palmier, checkpoint
  MASTER, `_storico_video.md`, regole corsie.
- Resta in cloud SOLO il monitoraggio del test TPLMF (check automatici 19:00 /
  24h / 48h via NexLev, che sul Mac non c'è): il verdetto verrà committato qui.
- **Orari di pubblicazione**: usare la nuova analisi
  `memoria-canale/analisi-orari-pubblicazione.md` → lunghi 9:00 · 14:45 · 18:30
  (A/B col 20:30). Short: proposta 12:30/17:00/21:00 da COORDINARE con chat SHORT.

## 1. Da produrre SUBITO: video Forbidden Fruit (slot DOM 9/8 ore 9:00)

- Script COMPLETO pronto: `memoria-canale/video-FF-10-14ago-script-completo.md`
  (2.474 parole ≈ 18–20 min, formula nuovo formato integrale, trame verificate).
- Fare sul Mac: TTS (voce femminile 25–35 calda, 145 p/min, 1 sec di silenzio
  prima delle frasi clou) · immagini col MIX 50/50 (metà generate con PALMIER,
  metà riusate dalle cartelle personaggi Forbidden Fruit) · thumbnail
  ("LI HA VISTI", spec nei metadati dello script) · montaggio · bozza PRIVATA
  via API con containsSyntheticMedia.
- ⏱ LOGGARE I TEMPI di ogni fase (TTS, immagini, montaggio, QC) in
  `memoria-canale/test-formato-monitoraggio.md` → servono per ritarare la
  notturna (decisione utente: qualità > quantità, probabile 1 batch/notte).

## 2. Cambio piattaforma: PALMIER al posto di Horacl

- Indicazione utente (8/8 sera, sessione cloud): "non usiamo più Horacl ma Palmier".
- La sessione cloud NON ha dettagli su Palmier (non è nella memoria unificata):
  documentarli qui al prossimo handoff (accesso, crediti, modelli, MCP).
- Horacl resta a 16 crediti free: non usarlo.

## 3. Regola immagini 50/50 (utente, 8/8 sera — vale anche per Storie Ispiranti)

- Metà immagini generate nuove + metà riusate dalle cartelle personaggi esistenti.
- Librerie immagini MAI cancellate (Serie TV Fans e Storie Ispiranti).
- Refresh foto personaggi ~ogni 2 mesi.

## 4. Promemoria già noti

- Test TPLMF stasera 18:00: la sessione cloud fa i check 19:00 / 24h / 48h e
  scrive il verdetto nella scheda monitoraggio.
- Notturna di stanotte (video 114–119) parte col VECCHIO formato: previsto.
  La riconfigurazione scatta solo dopo il verdetto 48h (10/8 sera).
- Ripianificazione coda 9–20/8: `memoria-canale/mappa-ripianificazione.html`
  (3 duplicati da eliminare, 9 bruciati da anticipare, slot notturni da correggere).

---

## ✅ AGGIORNAMENTO DALLA SESSIONE MAC (8/8 sera ~17:30)

**⚡ DIRETTIVA UTENTE (8/8 ~17:15): "inizia a pubblicare nuovo formato senza test, cambiamo già strategia."** Il test TPLMF non è più decisionale (i check restano come misura).

Fatto dalla sessione Mac:
1. **Memoria esportata** in `memoria-canale/memoria-mac/` (Palmier, checkpoint MASTER, storico video, regole corsie, calibrazione TTS) — richiesta del punto ⓪ soddisfatta.
2. **Palmier documentato** (punto 2): app locale `/Applications/PalmierPro.app` + MCP `http://127.0.0.1:19789/mcp`, piano PRO $29, nano-banana-pro (thumbnail/volti con referenceMediaRefs + "SAME EXACT FACE") e nano-banana-lite (scene). Dettagli completi in `memoria-mac/palmier-*.md`.
3. **Video FF 10–14 ago (nuovo formato) in produzione**: immagini 50/50 fatte (10 Palmier + 10 libreria), thumbnail "LI HA VISTI" fatta, TTS in corso (lancio 17:04, CPU), montaggio in catena automatica. Verrà **programmato per DOM 9/8 ORE 9:00** via publishAt (progetto quota SDOPPIA, non tocca il cron 23:00).
4. **Ripianificazione applicata via API**: 11 programmati spostati secondo la mappa; 2 duplicati eliminati con conferma utente (Nadir 15/8, Santos 7:57). "Ángela si ribella" 14/8 TENUTA (la presunta copia 11/8 non esiste tra i programmati — da verificare tra le bozze). Video non trovati tra i programmati (probabili bozze non programmate): "Kaya smaschera Şahika al funerale", "tregua Ender/Şahika/Yıldız", "strappa l'ordine" 16/8, "Zehra scopre che Mert ha un figlio" 17/8, "nozze lampo" 10/8 12:00.
5. **Notturna riconfigurata DA STANOTTE**: 1 batch = 3 lunghi nuovo formato (prompt `bin/prompt_night_batch_serietvfans.txt` riscritto, backup del vecchio conservato).

**Per la sessione cloud**: fare comunque i check TPLMF 19:00/24h/48h e committare i numeri nella scheda monitoraggio (servono come baseline del nuovo formato). Il video FA settimanale "divorzio Nare + scoperta Alya" (DOM 9/8 18:00 nella mappa) NON ha ancora uno script: se la cloud può scriverlo col nuovo formato, committarlo qui come fatto per il FF.

---

## ✅ RIPIANIFICAZIONE COMPLETATA DA BROWSER (8/8 ~19:00, sessione Mac)

Trovati e corretti 4 elementi che la prima passata via API aveva mancato (causa: alcuni video scheduled hanno `privacyStatus` API "public"/anomalo anche se Studio li mostra "Scheduled" — es. video membership-only con release pubblica futura; verificare sempre da Studio, non fidarsi solo del campo API):
1. **Fix di un mio errore**: "FAR AWAY: dopo il tribunale" era finito su 11/8 22:00 invece di 12/8 21:00 — corretto.
2. **"Kaya smaschera Şahika al funerale"** (era ancora al 13/8) → spostato 10/8 21:00.
3. **"tregua Ender, Şahika, Yıldız"** (era ancora al 13/8) → spostato 11/8 21:00.
4. **"Yıldız e Çağatay nozze lampo"** (era ancora al 10/8) → spostato 19/8 10:00 (via Studio, video a visibilità membership).
5. **Duplicato reale trovato e confermato**: "Ángela si ribella" esisteva in 2 copie (9:01 corretto all'11/8 12:00, TENUTO; 7:49 copia al 14/8, ELIMINATA da browser con conferma utente).

Mappa `ripianificazione-8-23-agosto.xlsx` ora riflette lo stato reale della coda YouTube. Nessun'altra discrepanza trovata scorrendo i primi 30 programmati (622 video totali sul canale, il resto sono già pubblicati/storico).

## ✅ AGGIORNAMENTO 2 SESSIONE MAC (8/8 ~19:00)
- **Video FA settimanale (nuovo formato ≥20 min) IN PRODUZIONE sul Mac**: script completo committato qui (`video-FA-10-14ago-script-completo.md`, 20.229 caratteri ≈ 20,8 min), TTS in corso, uscita programmata DOM 9/8 ORE 18:30. La sessione cloud NON deve scriverlo.
- **NUOVE DIRETTIVE UTENTE 8/8 sera (valgono per ogni video)**: 1) durata MINIMA 20 minuti, mai riempitivi, solo fatti verificati nuovi; 2) immagini SOLO della stessa serie + personaggi citati (mai mischiare canali/serie); 3) generazioni Palmier con reference + controllo fedeltà volto (se non riconoscibile → foto reale); 4) thumbnail SEMPRE con foto reali dei personaggi (no volti AI); 5) sottotitoli a metà schermo (build_video.py aggiornato); 6) numeri SEMPRE in lettere negli script (pronuncia TTS); 7) in valutazione switch voce a ElevenLabs (decisione utente, mitigazione attiva).
- Thumbnail NF2 rifatta con foto reali e già sostituita su k_Usdt_aAvI.
- Nuova cartella libreria: PERSONAGGI SERIE TV FANS/FAR AWAY/Nare/ (2 foto reali Sahra Şaş).
