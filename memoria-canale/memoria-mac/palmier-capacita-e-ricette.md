---
name: palmier_pro_new_capabilities_audit
description: Audit 07/08 delle nuove capacità di Palmier Pro dopo aggiornamento utente
  — nuovi passi standard per shorts/thumbnail nei verticali soap, testati su progetto
  reale.
metadata:
  node_type: memory
  type: project
  originSessionId: pending
  modified: 2026-08-07 01:42:29.820000+00:00
permalink: palmier-pro-new-capabilities-audit
---

**Contesto:** l'utente ha aggiornato Palmier Pro (07/08) e ha chiesto di verificare le nuove capacità del tool MCP e integrarle nel workflow. Il tool espone ora 48 funzioni MCP (prima ne usavamo di fatto ~5: `generate_image`, `remove_silence`, `add_captions`, export, `manage_project`). Palmier non è una pipeline a script fisso — viene guidato in sessioni MCP interattive progetto per progetto — quindi "integrare nel workflow" qui significa: nuove regole standard da applicare nelle prossime sessioni di montaggio/generazione, non nuovi script Python. Vedi [[palmier_auto_close_housekeeper]] e [[decisione_switch_horacle_palmier_immagini]] per il contesto precedente.

**Validato dal vivo (non solo letto dalla doc)** sul progetto `ShortsFactory-Test-Palmier` (clip reale "promessa_jana_clean", 35s, dialogo soap):
- `denoise_audio` (strength default 0.6, on-device, gratis) → applicato con successo, bake in background, nessun problema.
- `inspect_color` → scope reali (istogramma luma, bilanciamento colore, zone shadows/mids/highs) utilizzabili per grading "by the numbers" invece che a occhio.
- `detect_beats` → su un clip di solo dialogo (no musica) ha trovato solo 2 beat deboli in 35s — CONFERMA che serve solo quando c'è un letto musicale reale, inutile su clip di solo parlato.

## Nuove regole standard per verticale

**Shorts editing (Serie TV Fans, Soap Opera Italia, News e Pettegolezzi, e futuri World Soap Spoilers/Telenovela ES quando la pipeline shorts parte) — già montati in Palmier (progetti `ShortsFactory-*`, `SOI_short_*`, `Mass-*`, `NewsPettegolezzi-*`):**
- Aggiungere **sempre** `denoise_audio` sulla clip audio prima delle caption, quando l'audio viene da fonte broadcast/scraping (rumore di fondo tipico) — gratis, on-device, nessun motivo per saltarlo.
- Usare `detect_beats` + `set_keyframes` per sincronizzare zoom/tagli al ritmo **solo se lo short ha un letto musicale** aggiunto (es. teaser/hook con musica) — su clip di solo dialogo è inutile, saltare.
- `inspect_color`/`apply_color`: valutare una grade di riferimento per canale (look coerente) da riusare via il parametro `color` (copia-incolla grade tra clip) — non ancora definita una grade standard, da fare quando si monta il prossimo batch se l'utente vuole un look brand più marcato.
- `upscale_media` (Topaz/Bytedance/SeedVR2) per sorgenti sotto 1080p prima del taglio in short — coerente con [[qualita_immagini_soglia_accettabile]].

**Thumbnail/immagini (tutti i verticali soap, uso attuale: Ideogram V4 via Palmier + fallback ChatGPT browser per [[chatgpt_image_generation_method]]):**
- Nuovi modelli diretti via `generate_image` senza passare dal browser: **Nano Banana Pro/2**, **GPT Image 2**, **Seedream 5.0 Pro**, **Recraft V4.1** — tutti dentro l'abbonamento Palmier già attivo, nessun costo aggiuntivo oltre ai crediti inclusi. Da provare a occhio sul prossimo batch thumbnail prima di sostituire Ideogram/ChatGPT come default — non ancora testata la qualità comparativa.

**PokerLab (lezioni Costantini, pipeline ffmpeg Ken Burns esistente, oggi FUORI da Palmier) — non prioritario ora (progetto in pausa dal 30/07, vedi [[pokerlab_watchdog_valutazione_05agosto]]):**
- Se/quando riparte: `denoise_audio` + `remove_words` (rimozione filler "ehm"/pause a livello di parola, via transcript) sarebbero un pre-pass naturale sulla registrazione grezza della lezione prima della trascrizione faster-whisper — ma richiede importare la lezione in un progetto Palmier, un passo in più rispetto alla pipeline ffmpeg attuale. Da valutare solo alla ripresa del progetto, non implementato ora.

**Storie Ispiranti (narrazione TTS Chatterbox, già pulita — niente filler da rimuovere):**
- `upscale_media` utile per le immagini riciclate a bassa risoluzione (vedi [[storie_ispiranti_riciclo_immagini_multilingua]]) prima del riuso, per rispettare [[qualita_immagini_soglia_accettabile]].
- Musica generativa Palmier (ElevenLabs Music/Lyria 3 Pro dentro `generate_audio`) è un'alternativa a Envato ma costa crediti per ogni generazione contro una libreria Envato già pagata a flat — non conviene finché Envato copre il tono richiesto; da usare solo per casi dove Envato non ha un match adatto.

**Non applicabile (nessun uso video/audio via Palmier):** KDP (solo immagini statiche via Draw Things/ChatGPT), Bulio Shop (foto prodotto), Finds Vault (pipeline immagini/render separata) — nessuna azione.

## AGGIORNAMENTO 07/08 — A/B test immagini ESEGUITO, ricetta di produzione validata
Testati **GPT Image 2** (1920×1072, quality high) e **Nano Banana Pro** (2752×1536, 2K 16:9) via `generate_image` sul progetto `test-confronto-thumbnail`, stesso prompt dei confronti precedenti, overlay `make_thumb_cinema.py` applicato: **entrambi promossi a vista** — qualità volti/luce cinematografica al livello del flusso ChatGPT-browser, Nano Banana Pro a risoluzione più alta. Consegnati all'utente per verdetto finale.

**Ricetta produzione (validata, molto più efficiente del base64):** dopo la generazione, il file FULL-RES è già su disco dentro il pacchetto progetto: `~/Documents/Palmier Pro/<progetto>.palmier/media/gen-<ASSET_ID>.jpg` — basta un `cp`, niente export né decodifica base64 (l'MCP `inspect_media` restituisce solo una preview ~1568px, NON usarla per produzione).

**Gotcha CRITICO 07/08 (generate_video):** il parametro `aspectRatio` viene IGNORATO quando si passa `startFrameMediaRef` — l'output eredita sempre le proporzioni dell'immagine di partenza, verificato con `ffprobe` reale (non fidarsi delle dimensioni riportate da `inspect_media`/`get_media`, possono essere fuorvianti). **Per un video verticale, l'immagine di riferimento DEVE essere generata nativa in 9:16** (generate_image con aspectRatio 9:16), non un'immagine 16:9 "forzata" in video verticale. Se serve lo stesso video in entrambi i formati, servono 2 immagini base separate (una per orientamento) prima di animare — costo raddoppiato sulle immagini ma il video via Kling costa uguale.

**Gotcha prompt:** con "movie poster style" entrambi i modelli inventano titoli/scritte finte in turco sull'immagine — per la produzione aggiungere sempre "no text, no titles, no lettering" al prompt (l'overlay testo lo mettiamo noi localmente).

## Non ancora deciso / da riprendere
- Nessuna grade colore standard definita per i canali soap — proporla quando si monta il prossimo batch shorts, non a freddo.
- `sync_clips`/`manage_multicam`/`change_cam` (multicam) — nessun progetto attuale ha footage multi-camera, capacità censita ma non applicabile oggi.