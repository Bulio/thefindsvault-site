---
name: serietvfans-production-pipeline
description: 'Full faceless-video production pipeline per Serie TV Fans: research→script→TTS→immagini→montaggio→sottotitoli→thumbnail→SEO,
  + regole permanenti su tool/stile/skill obbligatorie e cron upload giornaliero.
  Consolidato da 5 memorie separate (06/08/2026).'
metadata:
  node_type: memory
  type: project
  modified: 2026-08-06 16:18:51.640000+00:00
  originSessionId: be416c77-2cb2-4bbd-9485-cb2bbc77ddb2
permalink: serietvfans-production-pipeline
---

User owns the YouTube channel **Serie TV Fans** (channel ID `UCwgtJLcJWxO5p_VAILE4sdA`, handle @SerieTVFans, faceless "anticipazioni" IT su Il Paradiso delle Signore, Forbidden Fruit, La Promessa, Far Away). Canale monetizzato dal 28/07/2026 — vedi [[serietvfans_batch_1_2_3_agosto_stato]] per stato/numeri aggiornati e [[pietro_g_metodo_copy]] per lo stile hook/CTA.

## Pipeline standard (PASSO per PASSO, invariata nella struttura dal 2026-07-28)

1. **Research** — NexLev MCP (`youtube_search` con `upload_date: week`, ordinato per data, più affidabile di `search_videos` per questa nicchia). Sempre leggere il **transcript completo** (`get_video_transcript`/`get_bulk_video_transcripts`) dei competitor più lunghi (20-40min), non fermarsi a titolo/descrizione — unico modo per trovare angoli ricchi senza dover riempire con ripetizioni (vedi sezione "Stile script" sotto).
2. **Script** — Claude, ~1200-1500 parole, tono "anticipazioni": hook, sviluppo, domande CTA polarizzanti, chiusura. Safe-copyright: no nomi attori reali, no loghi network, no clip verbatim.
3. **Narration** — Chatterbox Multilingual TTS locale (`generate_narration.py testo.txt output.wav`, venv `tts_env`, voce clonata `clone_ref_it.wav`, parametri default exaggeration=0.35/cfg_weight=0.5/temperature=0.65). Accenti espliciti su parole ambigue, punteggiatura per pause naturali.
4. **Immagini corpo video** — MAI generate da AI (vedi regola tooling sotto): fornite dall'utente/pescate dalla libreria personaggi condivisa in cartelle `imgs_video<N>/` (convenzione reale verificata su 20+ batch — NON `immagini_video<N>_<soap>/`, quella era solo 1 batch legacy).
5. **Montage** — ffmpeg (`~/bin/ffmpeg`), Ken Burns zoompan, narrazione come unica audio track.
6. **Subtitles — MANDATORY**, vedi [[video_subtitles_requirement]].
7. **Thumbnail** — Horacle standard confermato (nano-banana-2), vedi [[thumbnail_stile_cinema_chatgpt]] per la ricetta esatta; fallback locale `make_thumb_splitbg.py` solo se crediti Horacle esauriti.
8. **SEO** — titolo/descrizione/keyword sempre cross-check contro competitor reali pubblicati la stessa settimana prima di finalizzare.

## Regole di tooling/credit-consciousness (permanenti dal 2026-07-29)

1. **No AI image generation per immagini corpo video** — solo screenshot/libreria forniti, mai generare per riempire un gap (flag il gap invece).
2. **Eccezione: le thumbnail SÌ usano generazione AI** (Horacle) — unico carve-out deliberato.
3. **Montaggio ranked by cost**: ffmpeg script (default) → DaVinci Resolve API → CapCut browser (solo su richiesta esplicita per-video).
4. **Durata minima 8:00, non negoziabile.** Se narrazione corta: espandere con fatti reali (mai filler), mai stiracchiare le immagini. Verificare sempre con `ffprobe`.
5. **Sottotitoli = unico overlay testuale nel corpo video.**

## Stile script (permanente dal 2026-07-28, rafforzato 02/08)

1. **Linguaggio semplice/scorrevole**, spoken-register italiano (audience 50-70, ascolto non lettura) — non letterario, non impoverito.
2. **Keyword SEO nel corpo testo** (nomi personaggi, show, "anticipazioni", termini di trama), non solo in titolo/tag.
3. **⚠️ MAI allungare ripetendo lo stesso concetto con parole diverse** per raggiungere il minutaggio — vietato esplicitamente (pattern trovato nei batch 13-16). Se un draft è corto, la soluzione è SEMPRE cercare più materiale reale (secondo/terzo video competitor, sviluppare personaggi secondari con fatti concreti), mai riscrivere lo stesso punto. Solo se il materiale reale è davvero esaurito, consegnare uno script più corto.
4. **Calibrazione lunghezza per il vincolo ≥8:00**: vedi [[chatterbox_real_pace_calibration]] per il target caratteri aggiornato (16.87-17.37 car/s reali, target ≥8300 caratteri) — non fidarsi della stima teorica, verificare sempre con `ffprobe` dopo il render.

## Skill pipeline obbligatoria (direttiva permanente dal 31/07)

Per ogni script, prima di considerarlo finito, invocare SEMPRE (non scrivere "a mano" quando la skill esiste):
1. `fact_checker` — cross-check contro la fonte competitor.
2. `youtube_seo_optimizer` — titolo/descrizione/tag/capitoli.
3. `thumbnail_prompt_generator` — prompt scena (resta valido lo stile [[thumbnail_stile_cinema_chatgpt]] per l'overlay locale).
4. `competitor_analyzer` a monte della scelta angoli, se non già coperto da ricerca NexLev diretta.

Vale per tutti i batch, non solo per lo script in corso quando è stata data l'istruzione.

## Cron upload giornaliero (dalle 23:00, permanente dal 31/07)

- Script: `YOUTUBE_API/serietvfans/daily_upload_6.py` (venv proprio, `google-auth` installato), legge `queue/*.json` (manifest `{video,title,description,tags,thumbnail,privacy}`), carica **max 6 video/giorno** (limite quota API), rimuove dalla coda solo gli item riusciti.
- Crontab reale del Mac (`0 23 * * *`, non `CronCreate`/agente cloud — questi non sono adatti: il primo scade in 7gg, il secondo non ha accesso al filesystem locale/token OAuth).
- La coda va popolata a mano/da sessione con un manifest JSON per batch pronto — lo script non scansiona da solo le cartelle `VIDEO * PRONTI`.
- Limiti noti: se il Mac è spento/sleep alle 23:00 il job salta quel giorno (nessun wake); macOS può chiedere "Accesso completo al disco" la prima volta.

**How to apply**: quando si riprende lavoro su Serie TV Fans, applicare queste regole di default senza richiederle ogni volta — deviare solo su richiesta esplicita dell'utente. Tutto è anche in `~/Desktop/Claude/SKILL.md` (PASSO 2-8) — tenere i due in sync se uno cambia. Vedi [[serietvfans_content_strategy]] per composizione batch/trend/CTA e [[serietvfans_batch_1_2_3_agosto_stato]] per lo stato di produzione corrente.