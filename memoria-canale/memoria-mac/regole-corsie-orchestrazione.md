---
name: video-production-lanes-orchestration
description: DIRETTIVA MASTER 31/07 — tutte le corsie di calcolo per la produzione
  video (CPU locale + Colab + Kaggle, multi-account) vanno usate SEMPRE insieme in
  parallelo, mai in collisione, per ridurre al minimo il tempo di produzione totale
metadata:
  node_type: memory
  type: feedback
  originSessionId: c80be8eb-ea01-4523-9cfa-fcc2ba676e0b
  modified: 2026-08-06 21:46:53.174000+00:00
permalink: video-production-lanes-orchestration
---

Direttiva esplicita dell'utente il 31/07 pomeriggio, dopo aver visto che la corsia Kaggle
([[kaggle_tts_gpu_lane]]) ha generato in ~7 minuti due narrazioni che sulla coda CPU
locale sarebbero rimaste ferme a tempo indeterminato: **"una volta settati utilizzeremo
TUTTE le soluzioni per generare i video, gestisci tu coda e tutto, per tutti i video di
ogni chat"** + **"dobbiamo sempre utilizzarle tutte in modo tale che non si sovrappongano
mai e possano lavorare tutte insieme"**.

## ⚠️ AGGIORNAMENTO 31/07 sera — Kaggle ora si pilota via API/CLI, non più browser

Da questo momento **Kaggle non richiede più multi-account/multi-login per avere più corsie parallele**: con l'API ufficiale (`kaggle kernels push`, vedi [[kaggle_tts_gpu_lane]], sezione "METODO PRINCIPALE") si possono lanciare **più kernel in parallelo sotto lo STESSO account**, senza browser, senza i problemi di iframe/Monaco/focus rubato documentati sotto per Colab. Validato 31/07 sera: 2 kernel paralleli hanno finito un batch di 10 file (Storie Ispiranti video6-10 IT+EN) in ~3 ore che in coda CPU ne avrebbe richieste 7-11.

**Conseguenza pratica**: per Kaggle, preferire SEMPRE 1-2 kernel via API sullo stesso account invece di aprire un secondo account Google per Kaggle. Il multi-account (punti 3 e 5 sotto) resta utile SOLO per Colab, che non ha un'API ufficiale equivalente ed è quindi ancora legato al browser.

## ⚠️ Kaggle è ottimo per TTS (GPU-bound) ma SCONSIGLIATO per montaggio ffmpeg (CPU-bound) — 31/07 sera

Scoperto con un test reale su Storie Ispiranti (video10): un kernel Kaggle `enable_gpu: false` lanciato per il montaggio ffmpeg (Ken Burns + sottotitoli via `build_video.py`) era ancora RUNNING dopo 2h23min senza aver prodotto nulla, mentre lo stesso identico script sul Mac locale completa un montaggio equivalente in **3-11 minuti**. Segnalato da un'altra sessione concorrente che ha confrontato i log reali (video1-5 già fatti in locale) col tempo speso su Kaggle, confermato e il kernel abbandonato.

**Perché**: le CPU gratuite dei kernel Kaggle (poche vCPU, clock modesto) sono nettamente più deboli del Mac per un carico single-thread come l'encoding ffmpeg — il vantaggio di Kaggle è la GPU T4, che il TTS usa pesantemente (da qui i tempi ottimi per [[kaggle_tts_gpu_lane]]) ma che il montaggio non tocca affatto.

**How to apply**: usare Kaggle (o Colab) SOLO per lavoro GPU-bound (TTS, generazione immagini/video AI) — per montaggio ffmpeg, whisper, o qualsiasi altro carico CPU-bound, la coda CPU locale resta la scelta giusta anche se momentaneamente occupata da altri progetti: aspettare in coda locale batte quasi sempre spostare il lavoro su una corsia cloud CPU-only. Il kernel Kaggle CPU-only abbandonato non consuma quota GPU e può essere lasciato morire da solo senza altre azioni.

## Le corsie disponibili (stato 31/07 sera)

1. **CPU locale del Mac** — wrapper `~/Desktop/Claude/run_in_coda.sh`, FIFO, vedi
   [[coda_cpu_jobs_pesanti]]. Sempre disponibile, la più lenta.
2. **Colab, account principale** `giulianop991@gmail.com` — vedi [[colab_tts_gpu_lane]].
   Soggetto a "limiti di utilizzo GPU esauriti" nelle ore di punta. Nessuna API ufficiale:
   resta legato al browser.
3. **Colab, account dedicato** `imperodigitale4@gmail.com` — aggiunto il 31/07 sera come
   sessione Google separata nello stesso Chrome (via "Aggiungi un altro account", non
   sostituisce l'account principale) proprio per avere una quota GPU Colab indipendente
   da usare in parallelo alla 2.
4. **Kaggle, account principale** `giulianop991@gmail.com` — vedi [[kaggle_tts_gpu_lane]]
   (ora via API ufficiale, non più notebook browser). Si possono lanciare 2+ kernel
   paralleli su questo stesso account invece di servire una seconda corsia Kaggle.
5. **Kaggle/Colab, account** `imperodigitale01@gmail.com` — stessa email già usata per il
   canale News e Pettegolezzi (upload YouTube), aggiunta come sessione Google separata il
   31/07 sera. Utile ancora per Colab (che lo richiede); per Kaggle non più necessaria di
   norma, dato il punto 4.

Login di account aggiuntivi: usare `https://accounts.google.com/AddSession` (NON la
pagina normale di login, che spesso reindirizza all'account già loggato) — apre il flusso
"Aggiungi un altro account" mantenendo tutte le sessioni Google attive in parallelo nello
stesso Chrome. Pre-compilare solo l'email (è dato non sensibile), MAI la password: quella
la inserisce sempre l'utente.

## REGOLA CRITICA — mai condividere lo stesso notebook/account tra sessioni concorrenti

Scoperto il 31/07 sera con un incidente reale: ho detto a un'altra sessione Claude Code
attiva ("video 1 - 2", Storie Ispiranti) di usare il MIO stesso notebook Kaggle
`chatterbox-tts-bridge` con lo STESSO account. Risultato: l'altra sessione ha modificato
i file di test condivisi nel dataset mentre io stavo generando un batch, causando
"Failed to save draft" e testo estraneo comparso nel mio notebook. Non ha rotto la mia
generazione solo per fortuna (i miei testi erano incorporati inline nel codice, non letti
da file condivisi) — con un'altra struttura di codice avrebbe potuto corrompere l'output.

**Regola non negoziabile**: ogni sessione/progetto che usa una corsia Colab o Kaggle deve
avere il **proprio notebook indipendente** (via "File → Copy and Edit"/"Fork" per
duplicare in un attimo un notebook già pronto) e, quando possibile, il **proprio
dataset/account dedicato** — non riusare mai lo stesso notebook cloud di un'altra sessione
attiva contemporaneamente. Account condivisi (stesso login Google) vanno bene SOLO se i
notebook/dataset all'interno sono comunque separati per progetto.

## Come smistare il lavoro (protocollo operativo)

Prima di lanciare un job TTS pesante, in ordine:
1. Controllare `cat ~/Desktop/Claude/.coda_cpu.lock/name` — se libera o è il proprio job, ok usarla.
2. Controllare se una delle corsie Colab/Kaggle è libera (nessun'altra sessione la sta
   usando in quel momento) — coordinarsi via `mcp__ccd_session_mgmt__send_message` con le
   altre sessioni attive (`list_sessions`) se c'è ambiguità su chi sta usando cosa.
3. Assegnare il lavoro alla corsia più veloce disponibile in quel momento, **mai lasciare
   una corsia libera mentre un'altra ha una coda** — l'obiettivo è che tutte lavorino
   sempre in parallelo su progetti/batch diversi.
4. Se un progetto ha priorità dichiarata (es. Serie TV Fans, vedi
   [[coda_cpu_jobs_pesanti]]), quella priorità vale solo all'interno della STESSA corsia
   (es. non scavalcare un batch Serie TV Fans già in coda CPU) — non blocca le altre
   corsie, che restano libere per altri progetti.

## Qualità non negoziabile anche con più corsie (promemoria)

Aggiungere sempre la cattura dei timing per-frase (`timings.json`, vedi
generate_narration_discorsivo.py e la sezione "sottotitoli sincronizzati" in
[[kaggle_tts_gpu_lane]]) in QUALSIASI script di generazione veloce su una nuova corsia,
non solo l'audio — altrimenti `build_video.py` usa il fallback proporzionale e i
sottotitoli non sono più perfettamente sincronizzati, violando [[video_subtitles_requirement]].
Scoperto e corretto lo stesso giorno: la prima versione del notebook Kaggle non salvava i
timing, i due video del batch2 News e Pettegolezzi sono stati rigenerati da zero per
correggerlo.

**How to apply**: ogni volta che si apre una nuova sessione Claude Code che deve produrre
video/audio, leggere questa memoria per primo insieme a [[preferenza_corsia_colab_vs_coda]]
per sapere quali corsie esistono e come usarle senza calpestarsi a vicenda.

## AGGIORNAMENTO 04/08 — lock automatico anche per Colab (prima solo Kaggle ce l'aveva)
Il coordinamento "manuale via send_message" per Colab (regola critica sopra) era l'unico punto debole rispetto a Kaggle, che ha `kaggle_gpu_slot.sh`. Aggiunto `~/Desktop/Claude/colab_lane_lock.sh` (stessa cartella, stesso pattern a directory-lock): `acquire <account_email> <label>` prima di iniziare a pilotare un notebook Colab, `release <account_email>` a fine lavoro. A differenza di Kaggle, Colab non ha un'API di stato kernel quindi **non c'è auto-release su slot "probabilmente morto"** — se uno slot risulta BUSY da ore, verificare a mano che l'altra sessione non stia più lavorando prima di `force-release`, non assumerlo. Anche `bridge_server.py` ora espone `GET /health` (risponde `{"status":"ok"}`) per verificare che il ponte sia vivo prima di un push/pull, invece di scoprire un fetch appeso a metà lavoro.

**How to apply**: prima di aprire/usare un notebook Colab da una nuova sessione, lanciare `colab_lane_lock.sh acquire <account> "<progetto/label>"` — se risponde BUSY, non procedere su quell'account, usare l'altro account Colab disponibile o la coda CPU/Kaggle. Rilasciare sempre a fine lavoro (anche in caso di errore, non solo a completamento pulito).

## AGGIORNAMENTO 06/08 — tentativo di "raddoppiare tutte le corsie", decisioni prese (grilling)

L'utente ha chiesto esplicitamente di raddoppiare tutte le corsie di produzione (non per un progetto specifico, cambiamento infrastrutturale generale). Intervistato punto per punto, decisioni:

1. **CPU locale (TTS/whisper)**: resta a 1 slot, nessuna modifica — l'evidenza empirica in [[coda_cpu_jobs_pesanti]] (parallelismo rallenta invece di velocizzare) pesa più del desiderio generico di raddoppiare.
2. **Kaggle bulio9111**: tentato un aumento del lock da 2 a 4 slot, POI ANNULLATO — scoperto (vedi [[kaggle_secondo_account_bulio9111]], aggiornamento 06/08) che il tetto di 2 sessioni GPU concorrenti è imposto da Kaggle stesso (errore reale `Maximum batch GPU session count of 2 reached`), non una scelta del lock script. Resta a 2 slot.
3. **Kaggle, secondo account pianificato**: `imperodigitale4@gmail.com` (già usato per Colab, punto 3 sopra) — unico modo reale per avere più capacità GPU parallela (quota 30h/settimana indipendente + proprio tetto di 2 sessioni). **Serve azione dell'utente**: signup su kaggle.com con quella email + verifica telefono (non posso creare account io). Una volta fatto, replicare per quell'account l'infrastruttura di [[kaggle_secondo_account_bulio9111]] (lock dedicato `.kaggle_imperodigitale4_gpu.lock`, dataset, kernel, script push/monitor).
4. **Colab**: nessuna modifica, restano i 3 account del punto "Le corsie disponibili" sopra — già corsie parallele indipendenti, aggiungerne altre significa più complessità di coordinamento manuale via browser senza un collo di bottiglia reale da risolvere lì.
5. **Montaggio ffmpeg** ([[build_video_hardware_encoder_speedup]]): alzato `MAXSLOTS` in `run_in_coda_montaggio.sh` da 4 a 6 come TEST — non ancora validato con un batch reale a 6 (il Mac era sotto carico alto al momento del cambio, TTS in corso + PalmierPro, non condizioni pulite per un test valido). Da validare con un batch reale la prima occasione utile con macchina libera; riportare a 4 se emerge overhead significativo.

**How to apply**: se un secondo account Kaggle risulta ancora "non attivo" in `dispatch_lanes.sh`, non riprovare ad alzare il lock di bulio9111 oltre 2 — il tetto è di piattaforma. Ricordare all'utente il signup pendente se rilevante al contesto.