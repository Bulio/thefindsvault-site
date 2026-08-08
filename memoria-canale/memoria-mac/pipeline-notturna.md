---
name: night_batch_serietvfans_pipeline
description: Pipeline notturna claude -p (05:00, 2 batch = 6 LUNGHI/notte, zero short,
  cap $25) sul backlog Serie TV Fans — direttiva utente 07/08 ~03:20, cron installato,
  attiva ogni notte finché l'utente non la revoca
metadata:
  type: project
  originSessionId: current
  modified: 2026-08-07 01:22:10.459000+00:00
permalink: night-batch-serietvfans-pipeline
---


**✅ AUTH HEADLESS RISOLTA (08/08 ~16:15, test verificato in env cron pulito):** il wrapper esporta `CLAUDE_CODE_OAUTH_TOKEN` da `~/.claude/night_oauth_token` (108 char, chmod 600, generato con `claude setup-token`). Storia dei fallimenti: 07/08 05:00 e 08/08 05:00 "Not logged in" (cron non vede l'OAuth interattivo); launchd = "OAuth session expired"; i test dentro la sessione utente erano FALSI POSITIVI. Procedura corretta per rigenerare il token (es. se scade/revocato): `claude setup-token | tee /tmp/out.txt` in Terminale reale, completare il flusso browser (il CODICE va incollato col pulsante di copia della pagina, non a mano), poi estrarre `sk-ant-oat01-…` dal file con grep — MAI copiare il token a mano dal Terminale (il triple-click tronca la riga a capo). Test di verifica: `env -i HOME=$HOME PATH=/usr/bin:/bin CLAUDE_CODE_OAUTH_TOKEN=$(cat ~/.claude/night_oauth_token) ~/.local/bin/claude -p "OK" < /dev/null`.

**⚠️ NUOVA MODALITÀ dal 07/08 ~03:20 (direttiva utente diretta, sostituisce tutto quanto sotto dove in conflitto):** ogni notte alle **05:00**, **2 BATCH COMPLETI di SOLI video LUNGHI** (6 video = 2× rotazione FA+FF+LP), **zero short**, cap **$25**, ricorrente **finché l'utente non si sveglia e scrive di fermarla/cambiarla**. Riga cron `0 5 * * * .../run_night_batch_serietvfans.sh` installata con successo direttamente da Claude Code il 07/08 ~03:25 (nessun blocco harness stavolta). Prompt e wrapper già aggiornati alla nuova modalità. Prima esecuzione: la mattina stessa del 07/08 alle 05:00.

---

Costruita il 07/08/2026 su decisione esplicita dell'utente ("va fatta al meglio, è una pecca grande" — il sottoutilizzo del pattern claude -p notturno). Grilling completato: lavoro = backlog Serie TV Fans (21 lunghi + 78 short mancanti al 07/08, vedi [[serietvfans_batch_1_2_3_agosto_stato]]); orario 02:00 (dopo l'upload delle 23:00, corsie libere). **CAMBIO 07/08 stesso giorno, prima dell'attivazione: priorità ai LUNGHI — 5 lunghi/notte, zero short, cap $20.** Fattibilità: nella finestra 02-08 ci sta solo se il TTS usa anche la corsia Kaggle GPU (il prompt lo impone); su sola CPU seriale chiude 3-4 su 5 — accettato, il prompt impone chiusura ordinata e checkpoint aggiornato.

**File:**
- `bin/run_night_batch_serietvfans.sh` — wrapper cron: lock anti-doppia-partenza (auto-sblocco se lock >8h = crash residuo), log in `bin/night_batch_serietvfans.log`, notifica macOS a fine run. RICORRENTE, niente auto-rimozione dal crontab.
- `bin/prompt_night_batch_serietvfans.txt` — il prompt della sessione headless: checkpoint fresco prima di tutto, pipeline standard, SOLO bozze private + containsSyntheticMedia, validate mp4, max 2 tentativi per passo, chiusura ordinata con aggiornamento checkpoint se il budget si esaurisce.
- Riga crontab: `0 2 * * * .../run_night_batch_serietvfans.sh` — installata dall'utente via Terminale reale (blocco harness noto [[crontab_writes_require_real_terminal]]).

**Dry test 07/08**: sintassi ok, `claude -p` headless risponde, lock blocca la doppia partenza.

**Dopo la prima notte (DA FARE la mattina dopo l'attivazione):** controllare `night_batch_serietvfans.log` + bozze YT; se qualità ok, scalare volume (2 lunghi + 6 short) e ritarare il cap sul consumo reale ×2. Se il pilota fallisce, il log dice dove — sistemare prima di scalare.

**Budget cap spiegato all'utente:** tetto di sicurezza anti-loop, non costo fisso — la sessione si ferma da sola al limite; consumo su piano Claude esistente.