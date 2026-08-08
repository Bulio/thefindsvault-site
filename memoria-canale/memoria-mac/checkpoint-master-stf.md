---
name: serietvfans-batch-1-2-3-agosto-stato
description: 'CHECKPOINT 07/08 ~02:00 CHIUSURA SESSIONE: video84-101 pronti (84-94
  caricati, 95-101 montati+in coda per upload cron 23:00, video99 TTS ancora in corso
  in background alla chiusura — verificare). Canale MONETIZZATO. APRIRE PER PRIMO
  — leggere anche [[serietvfans_content_strategy]]'
metadata:
  node_type: memory
  type: project
  originSessionId: 430f487d-9c53-4a64-b4eb-fd8f5cd467bc
  modified: 2026-08-08T02:41:39.706Z
permalink: serietvfans-batch-1-2-3-agosto-stato
---

# 🏁 CHIUSURA SESSIONE 08/08 ~16:30 — STATO PULITO, LEGGERE PER PRIMO
**Prodotto in questa sessione (07-08/08): video102-113, TUTTI montati/validati/accodati** (batch29-32). Upload: 95-98+100+101 caricati il 07/08 sera (6/6); la coda smaltisce 6/giorno (99,102-104 → poi 105-110 → poi 111-113). Calendario coperto fino al 29/08 (2/3).
**NIENTE IN SOSPESO.** Prossima produzione: **video114** (FF, membership sì) — la fa la NOTTURNA autonoma (05:00, auth FUNZIONANTE via token file, vedi [[night_batch_serietvfans_pipeline]]). La prossima sessione interattiva deve solo: 1) verificare al mattino il log `bin/night_batch_serietvfans.log` e le bozze; 2) controllare gli upload 23:00; 3) se la notturna ha prodotto, aggiornare Piano Editoriale (29/08 3° slot in poi).
**Attenzioni**: token YouTube era stato revocato e ri-autorizzato 08/08 ~14:55 (se upload falliscono, ricontrollare con channels().list); semaforo `bin/kaggle_lane_reserved.txt` ancora attivo (max 1 slot Kaggle) — rimuoverlo se Storie Ispiranti ha finito; corsia SHORT = altra chat, NON toccare ([[feedback_divisione_corsie_short_lunghi]]).

---

# ⚠️⚠️⚠️ AGGIORNAMENTO 07/08 ~13:20 — VIDEO102-107 TUTTI COMPLETI E VALIDATI ✅ — LEGGERE PER PRIMO

## ✅ 6/6 PRODOTTI (102: 11:13 · 103: 9:23 · 104: 9:00 · 105: 8:41 · 106: 8:18 · 107: 8:15)
Tutti montati, `ffmpeg -v error` pulito, in coda upload (`queue/batch29.json` + `batch30.json`, file e thumbnail verificati presenti). Il cron 23:00 li distribuisce: 07/08 sera escono 95-98+100+101, poi 99+102-106, poi 107. NON riprodurre.

## ✅✅ Notturna headless: RISOLTA DAVVERO (08/08 ~16:15, verificata con test reale)
Token lunga durata (108 char) salvato in `~/.claude/night_oauth_token` (chmod 600); il wrapper lo esporta come CLAUDE_CODE_OAUTH_TOKEN. Test da env cron pulito: risponde OK. **Da stanotte (09/08 05:00) il cron produce da solo video114-119.** Lezione per il futuro: il token va estratto dall'output con `claude setup-token | tee file` (la copia manuale dal Terminale tronca la riga); i falsi positivi dei test dentro la sessione utente non valgono. NOTA 08/08: token YouTube serietvfans era stato REVOCATO e ri-autorizzato dall'utente alle ~14:55 (verificato: canale risponde) — se ricapita, upload 23:00 a rischio: verificare con channels().list.

## STORICO tentativi headless (superato — vedi sopra)
La run 08/08 05:00 è fallita di nuovo ("Not logged in"): il test del 07/08 era falso-positivo (girava nel contesto della sessione utente). Probe launchd 08/08: "OAuth session expired and could not be refreshed" → l'unica via headless è il token lunga durata ESPORTATO come CLAUDE_CODE_OAUTH_TOKEN. Il wrapper ora lo legge da `~/.claude/night_oauth_token` se esiste. **AZIONE UTENTE (2 comandi in Terminale)**: 1) `claude setup-token` e copiare il token stampato (sk-ant-oat…); 2) incollarlo in `echo 'TOKEN' > ~/.claude/night_oauth_token && chmod 600 ~/.claude/night_oauth_token`. Da quel momento il cron 05:00 funziona davvero. Test rapido di verifica: `env -i HOME=$HOME PATH=/usr/bin:/bin CLAUDE_CODE_OAUTH_TOKEN=$(cat ~/.claude/night_oauth_token) ~/.local/bin/claude -p "OK"`.

## Notturna: storico sblocco (07/08 ~13:00 — SUPERATO, vedi sopra)
L'utente ha eseguito `claude setup-token`: test `claude -p` da env pulito (stile cron) risponde OK. **Da stanotte il cron 05:00 produce da solo** (2 batch = 6 lunghi, cap $25). Se la prima notte va liscia, il checkpoint del mattino lo scriverà la notturna stessa. Residuo da pulire nel crontab (solo da Terminale reale): riga ONE-SHOT `45 4 7 8 *` e retry_thumbnails_87 (ha FINITO: tutte le thumbnail 87-94 impostate il 07/08 alle 9:02, ma l'autorimozione dal crontab è stata bloccata dal guardrail).

## ⚠️⚠️ NOTTURNA DI STANOTTE (08/08 ore 05:00): RIPARTIRE DA VIDEO114 — I VIDEO 108-113 SONO GIÀ FATTI
CAMBIO 07/08 pomeriggio: l'utente ha ordinato "inizia ora" e la sessione diurna ha prodotto ANCHE video108-113 (contrordine rispetto alla nota precedente). NON produrre 108-113: script+SEO+thumbnail+code già pronti (batch31/batch32, catena TTS/montaggi in corso, log `batch31/chain_v5.log`). **La notturna riparte da video114**: rotazione 114FF·115LP·116FA | 117FF·118LP·119FA; membership CTA: 114 sì(1), 115 no, 116 no, 117 sì, 118 no, 119 no. Fonti: ricerca fresca nuova — NON riusare gli ID in `_storico_video.md` righe [07/08] e [07/08-bis]. Canali da evitare: LA PROMESSA SPOILER (bandito), UNIVERSO FORBIDDEN FRUIT (clone IA di contenuti altrui), Velmire/Marcelli/Brixton TV (farm IA 4-12 views). Fonti LP quasi tutte INDIETRO sul canone (Lorenzo libero pre-v94): verificare sempre. Nota canone FF: NON affermare mai che la figlia segreta di Hasan Ali è Yıldız (v108 la lascia volutamente senza nome — HA è padre di Çağatay, rischio incesto narrativo da fonte inaffidabile).

## Lezioni operative 07/08 (per le prossime sessioni di produzione)
- **claude -p da DENTRO una sessione Claude Code non funziona**: --dangerously-skip-permissions bloccato dal classifier; i processi lanciati (anche nohup) muoiono col riavvio dell'app → per produzione survivable usare cron/Terminale reale.
- **La coda CPU è CONDIVISA con Storie Ispiranti**: dopo le 06:40 i loro job EN (50min l'uno) l'hanno occupata per ore — il TTS di 104 è rimasto orfano; risolto spostando 104+106 sulla corsia Kaggle. La notturna deve preferire Kaggle (1 slot) e non fare affidamento su CPU libera.
- **Semaforo corsie Kaggle**: `bin/kaggle_lane_reserved.txt` — se esiste, max 1 job Kaggle nostro (l'altro slot è di un'altra sessione). Rimuoverlo quando la riserva scade.

## Produzione 07/08 notte (fatta manualmente da questa sessione, video102-107)
- **Script+SEO+thumbnail+imgs PRONTI per tutti e 6**: batch29/ (102 FF Zehra-no-a-Mert CTA sì · 103 LP Petra-tetano · 104 FA terre-a-Şahin+Fikriye) e batch30/ (105 FF messaggio-anonimo CTA sì · 106 LP Petra-muore-confessione · 107 FA rinuncia-divorzio+bacio). Dettagli e fonti in `_storico_video.md` righe [07/08].
- **Catena automatica ATTIVA e staccata** (`batch29/chain_batch29_30.sh`, log `batch29/chain_batch29_30.log`): gestisce da sola TTS→montaggio→validazione per tutti e 6. Corsie: CPU (102→104→106) + UN SOLO slot Kaggle (103→105→107; l'altro slot è di Storie Ispiranti, direttiva utente — vedi `bin/kaggle_lane_reserved.txt`). audio103 già pronto (9:25). Fine stimata ~09:00-09:30.
- **Code upload GIÀ SCRITTE**: `queue/batch29.json` + `queue/batch30.json` (3+3 job completi con thumbnail, bozza privata). Il cron 23:00 carica 6/giorno: stasera 07/08 escono 95-98+100+101, poi 99+102-106 l'08/08, 107 il 09/08 (in automatico).
- **Rotazione aggiornata**: quartetti 98FA·99FF·100LP | 101FA·102FF·103LP | 104FA·105FF·106LP | 107FA· → **prossimo video108 = Forbidden Fruit**. Membership CTA: 102 sì, 103 no, 104 no, 105 sì, 106 no, 107 no → **108 = sì(1)**.
- **Lezione fonti 07/08**: molte fonti fresche sono INDIETRO sul canone (Lorenzo libero pre-v94, Ugur vivo pre-v92, corteggiamento Yıldız/Çağatay pre-v85) — controllare SEMPRE contro lo storico; SpoilerTV Italia ha mischiato un blocco La Promessa dentro un video Far Away (parzialmente IA, usare solo fatti corroborati). DramaTurca Of2eOAJrRC4 = GIÀ USATO per video93, riapparso nelle ricerche di oggi.
- Calendario: 102-107 coprono 25/08 (3° slot) + 26/08 completo + 27/08 (2 slot). Aggiornare Piano_Editoriale quando i montaggi sono validati.

---

# AGGIORNAMENTO 07/08 ~03:30 — video99 CHIUSO (storico, superato dall'aggiornamento sopra)

## Stato al 07/08 ~03:30 (sessione "baci e Serie TV Fans")
- **video99 (Forbidden Fruit): COMPLETO.** TTS finito (8:31), montato con build_video.py, validato `ffmpeg -v error` pulito, **accodato in `queue/batch28.json` (4° job, 7° totale in coda con batch27)** — il cron delle 23:00 carica max 6/giorno, il 7° slitta a domani da solo. Thumbnail e SEO erano già pronti. NON rifare.
- **Coda upload stasera 07/08 23:00**: batch27 (95,96,97) + batch28 (98,100,101) = 6 esatti. video99 = 7° → slitta.
- **⚠️ NOTTURNA RICONFIGURATA (direttiva utente 07/08 ~03:20)**: cron `0 5 * * *` INSTALLATO e attivo — ogni notte alle 05:00 `claude -p` produce **2 batch = 6 soli LUNGHI** (cap $25), finché l'utente non la revoca. Vedi [[night_batch_serietvfans_pipeline]]. **Prima run: 07/08 alle 05:00.**
- **Prossimo video da produrre: video102 = Forbidden Fruit** (chiude il quartetto 98FA·99FF·100LP·101FA), poi 103FA·104FF·105LP. **Membership CTA: video102 = sì(1)** (99 sì, 100 no, 101 no), poi 103 no(2), 104 no(3), 105 sì(1).
- **Short "baci" batch2 (progetto Short Test No Voce)**: gestiti in sessione separata, vedi [[short_test_serietv_no_voce_project]] — NON riguardano la notturna (solo lunghi).
- Crediti: **Horacle 16cr (morto)**, **Palmier ricaricato dall'utente 07/08 ~02:40 = corsia primaria immagini E video** (vedi [[decisione_switch_horacle_palmier_immagini]]).

---

# CHECKPOINT DI CHIUSURA SESSIONE 07/08 ~02:00 (storico, superato dall'aggiornamento sopra)

## ⚠️ NUOVO: pipeline notturna automatica costruita da un'altra sessione parallela — verificare prima di produrre a mano
Scoperta a fine sessione (vedi [[night_batch_serietvfans_pipeline]]): un'altra sessione ha costruito una pipeline `claude -p` headless per le 02:00, pensata per produrre 5 lunghi/notte sul backlog di questo stesso progetto (cap $20). **Alla ripresa, controllare PRIMA di tutto**:
1. `crontab -l | grep night_batch` — se la riga `0 2 * * *` è presente, la pipeline è attiva e potrebbe aver già prodotto video nella notte (controllare `bin/night_batch_serietvfans.log` e le bozze YT più recenti prima di scegliere il prossimo numero di video, per non duplicare).
2. Alla chiusura di QUESTA sessione (07/08 ~02:00) la riga cron non risultava installata (solo un dry-test fatto manualmente, lock si era pulito da solo) — ma potrebbe essere stata installata subito dopo dall'utente via Terminale reale (vedi [[crontab_writes_require_real_terminal]], il canale con cui va installata).
3. Se la pipeline notturna è attiva, valutare con l'utente se questa sessione manuale debba continuare a produrre in parallelo o lasciare campo alla notturna per evitare doppioni/conflitti di numerazione.

## Cosa manca esattamente quando si riprende
**video99 (Forbidden Fruit) — TTS ancora in corso in background alla chiusura di questa sessione** (processo locale nohup/disown, pid 63402 al momento della chiusura, sopravvive alla sessione). Script/SEO/thumbnail/imgs già pronti in `batch28/`. Alla ripresa:
1. Controllare se `batch28/audio_video99_forbiddenfruit_chatterbox.wav` esiste già (probabile, il TTS era al 30%+ dei blocchi da un pezzo). Se sì: montare con `run_in_coda_montaggio.sh` (stesso pattern di video95-101, vedi comandi sotto), validare `ffmpeg -v error`, aggiungere a `queue/batch28.json` (diventerebbe il 7° video in coda, sopra il limite di 6/giorno — va bene, il sistema lo rimanda al giorno dopo da solo).
2. Se il processo non esiste più e il file audio manca, rilanciare: `./dispatch_tts.sh "YOUTUBE_API/serietvfans/batch28/narrazione_video99_forbiddenfruit.txt" clone_ref_it.wav "YOUTUBE_API/serietvfans/batch28/audio_video99_forbiddenfruit_chatterbox.wav" --language it`

## Comando montaggio standard (riusare per video99 e ogni futuro video)
```
./run_in_coda_montaggio.sh "video99-forbiddenfruit" python3 build_video.py \
  "YOUTUBE_API/serietvfans/batch28/narrazione_video99_forbiddenfruit.txt" \
  "YOUTUBE_API/serietvfans/batch28/audio_video99_forbiddenfruit_chatterbox.wav" \
  "YOUTUBE_API/serietvfans/batch28/imgs_video99" \
  "YOUTUBE_API/serietvfans/batch28/VIDEO_FINALE_video99_forbiddenfruit_sub.mp4"
```

## Stato produzione completo (18 video totali gestiti in questa sessione: video84-101)
- **84-94**: ✅ caricati bozza privata su YouTube. Thumbnail 87-94 (8 in totale) in retry automatico via cron `2 9 * * *` (`retry_thumbnails_87_88_89_90_91.py`, si autorimuove dal crontab a lavoro finito).
- **95-98**: ✅ montati, validati, **in coda** `queue/batch27.json` (95,96,97) + `queue/batch28.json` (98,100,101) — 6 video totali, esattamente al limite giornaliero. Caricati dal cron `0 23 * * *` di stasera (07/08).
- **99**: ⏳ TTS in corso alla chiusura sessione (vedi sopra) — montaggio e coda ancora da fare.
- **100, 101**: ✅ montati, validati, già in `queue/batch28.json`.

## Composizione batch (rotazione 1 Far Away + 1 Forbidden Fruit + 1 La Promessa)
92FA·93FF·94LP | 95FA·96FF·97LP | 98FA·99FF·100LP | 101FA· — **prossimo (video102) deve essere Forbidden Fruit** per chiudere il quartetto e ripartire pulito con 103FA·104FF·105LP.

## Ciclo membership CTA (1 menzione ogni 3, sequenza cronologica di produzione)
Ultimo confermato: video99 sì(1), video100 no(2), video101 no(3) → **video102 riparte sì(1)**.

## ⚠️⚠️ LEZIONE CRITICA da applicare SEMPRE prima di scrivere un nuovo video
Scoperta due volte in questa sessione: fonti diverse (anche affidabili, es. DramaTurca e SpoilerTV Italia) a volte trattano personaggi chiave con stati contraddittori (es. Ugur vivo in una fonte, morto — 4 fonti concordi — in un'altra usata per video92). **Prima di scrivere qualunque script**, verificare lo stato dei personaggi coinvolti contro TUTTI i video già prodotti in questa sessione (84-101), non solo contro `_storico_video.md`. Se una fonte tratta un personaggio morto/arrestato/rivelato in modo diverso da come lo abbiamo già mostrato, scartare quel filone o chiedere conferma — vedi il caso Ugur (video92 morto vs fonte R5x8YxeSvcE che lo trattava vivo, scartato) come precedente.

## Fonti scartate perché di bassa qualità/probabile origine IA (annotare, evitare in futuro)
- **LA PROMESSA SPOILER** (canale YouTube) — video "Alonso fa arrestare Máximo e Leocadia" conteneva un artefatto testuale ("Se desideri, continua a riscrivere il prossimo capitolo mantenendo lo stesso stile...") che rivela contenuto generato da IA spacciato per anticipazione reale. **Non usare mai più questo canale come fonte.**
- **Valerioz TV** (video Ricardo/Pía, usato per video100) — non ha lo stesso artefatto esplicito ma è estremamente prolisso/ripetitivo, tono da bozza IA non rifinita. Usato comunque perché i fatti centrali erano verificabili e coerenti, ma riscritto per intero nel nostro stile — non fidarsi della sua prosa originale.

## Calendario aggiornato (Piano_Editoriale_Canali.xlsx, foglio "Cal. Serie TV Fans")
- 22/08 (riga 31): video91+92+93 → completo sui lunghi
- 23/08 (riga 32): video94+95+96 → completo sui lunghi
- 24/08 (riga 33): video97+98+99 → completo sui lunghi (video99 ancora in produzione ma già "prenotato" nel foglio)
- 25/08 (riga 34): video100+101 nei primi 2 slot → **manca ancora 1 lungo per completare il 25/08**
- 26/08→31/08: ancora completamente vuoti (6 giorni × 3 lunghi = 18 video lunghi mancanti) + **tutti gli short (0/78, pipeline mai definita in nessuna sessione)**

## Prossimo step quando si riprende
1. Finire video99 (vedi sopra).
2. Verificare che il cron delle 23:00 di stasera abbia caricato i 6 video in coda senza errori (`daily_upload_log.txt`).
3. Verificare che il cron delle 9:02 abbia sistemato le 8 thumbnail in sospeso (87-94) — se la riga cron è sparita dal crontab, ha funzionato.
4. Continuare la produzione: 1 lungo per completare il 25/08 (Forbidden Fruit, vedi rotazione sopra), poi 26/08→31/08 da zero.
5. Affrontare gli short (0/78) — pipeline mai definita.

---

# CHECKPOINT 07/08 ~00:50 — video84-98 tutti pronti (storico, superato dall'aggiornamento sopra)

## Aggiornamento finale: batch27 (video95-97) + video98 prodotti, calendario aggiornato fino al 24/08
Dopo batch26 (video92-94, vedi sotto), altri 4 video prodotti da zero con lo stesso standard (fact-check contro transcript completo, montati, validati `ffmpeg -v error` pulito):
- **video95 (Far Away)** — Sadakat confessa la relazione con Ekmel dopo la denuncia di Şahin, la polizia arriva alla villa, Alya scagiona Sadakat e sposa Cihan. Fonte: TV SOAP OFFICIAL (ws-7I_my38g). 8:15.
- **video96 (Forbidden Fruit)** — Hasan Ali usa la pace forzata Şahika/Mert come copertura per un piano segreto contro Ender. Fonte: L'Angolo delle Soap + DramaTurca (corroborate). 7:56 (leggermente sotto 8:00, variazione trascurabile accettata).
- **video97 (La Promessa)** — Petra nasconde una ricaduta di salute dopo la vittoria su Leocadia; in parallelo Lope scopre che il padre di Vera è un sicario sotto copertura di gioielliere. Fonte: Desy TV (95r_J3EWv3I). 8:35. **Volutamente escluso** il filone Curro/Lorenzo/fuga della stessa fonte perché precede cronologicamente l'arresto di Lorenzo già mostrato in video94.
- **video98 (Far Away)** — Alya rivela a Cihan di essere stata venduta da Fikriye per 300.000€, Sadakat la umilia pubblicamente, Cihan esplode contro sua madre. Fonte: DramaTurca (R5x8YxeSvcE). 9:03. **Volutamente escluso** un filone della stessa fonte con Ugur vivo che ricatta Alya su Deniz/Ekmel — CONFLITTO con video92 dove Ugur muore (4 fonti concordi) — scelta confermata dall'utente.

**Tutti e 4 pronti sul disco** in `batch27/` e `batch28/`, **accodati** in `queue/batch27.json` (3 video) e `queue/batch28.json` (1 video) — verranno caricati dal cron delle 23:00 di stasera (07/08), non prima (il cron delle 9:05 che avevo aggiunto è stato rimosso da un'altra sessione per evitare doppio consumo quota giornaliero, correttamente).

## ⚠️ FIX CRITICO 07/08: bug duplicati in daily_upload_6.py
Scoperto e corretto: se un upload riusciva ma la thumbnail falliva per quota, lo script rimetteva **l'intero job** in coda — il cron successivo avrebbe ricaricato un secondo video duplicato. Successo già su video92/93/94 (caricati alle 23:00 del 06/08, ID `BngPRv2mf0s`/`ho0hBomf0hI`/`EW_8909-ID4`, thumbnail fallita) — rimossi dalla coda in tempo prima del cron delle 23:00 del 07/08, spostati su `retry_thumbnails_87_88_89_90_91.py` (ora copre video87-94, 8 thumbnail). Script `daily_upload_6.py` riscritto per non ripetere mai più l'upload se il video è già stato caricato. Dettagli completi in [[serietvfans_daily_upload_duplicate_bug_fix]].

## Calendario aggiornato (Piano_Editoriale_Canali.xlsx, foglio "Cal. Serie TV Fans")
- 22/08 (riga 31): video91+92+93 → completo sui lunghi (mancano solo gli short)
- 23/08 (riga 32): video94+95+96 → completo sui lunghi
- 24/08 (riga 33): video97+98 nei primi 2 slot lunghi → **manca ancora 1 video lungo per completare il 24/08**, poi 25/08→31/08 ancora completamente vuoti (7 giorni × 3 lunghi = 21 video lunghi mancanti) + tutti gli short (mai iniziati, 0/78)

## Prossimo step quando si riprende
1. Verificare che il cron delle 23:00 di stasera abbia caricato batch27+batch28 senza errori (`daily_upload_log.txt`).
2. Verificare che il cron delle 9:02 abbia sistemato le 8 thumbnail in sospeso (87-94) — se la riga cron è sparita dal crontab, ha funzionato ed è auto-rimossa.
3. Continuare la produzione: 1 video per completare il 24/08, poi 25/08→31/08 da zero. Sempre verificare freschezza fonti (giorni/ore, non settimane) e **sempre incrociare con canone già stabilito** prima di scrivere (vedi lezione Ugur sopra — controllare stato di personaggi chiave morti/arrestati/rivelati nei video già prodotti prima di usare una fonte che li tratta diversamente).
4. Affrontare gli short (0/78) — pipeline mai definita in nessuna sessione finora.

---

# CHECKPOINT 06/08 NOTTE ~21:00 — video84-94 tutti pronti, 2 cron automatici gestiscono il resto (storico, superato dall'aggiornamento sopra)

## Aggiornamento finale sessione: batch26 (video92-94) prodotto da zero e accodato
Dopo aver chiuso l'arretrato (84-91, vedi sezione sotto), ricerca competitor fresca (2gg-poche ore) + produzione completa di 3 nuovi video, tutti fact-checked contro transcript completo della fonte, montati e validati (`ffmpeg -v error` pulito):
- **video92 (Far Away)** — Ugur muore investito mentre fugge dagli uomini di Demir, Cihan accusa Mine. Sequel diretto di video91. Fonte: Serie TV Italia (TAWAQOV0GZA) + 4 fonti corroboranti. 8:38.
- **video93 (Forbidden Fruit)** — Il tentativo di riconciliazione Hasan Ali/Çağatay fallisce, Çağatay dice a Yıldız "non credo alle relazioni serie", arriva Cenk (nuovo triangolo). Fonte: DramaTurca (Of2eOAJrRC4, 9h). Angolo photo/Feride scartato perché già coperto da video88.
- **video94 (La Promessa)** — Enora si rivela essere Nora Fuentes, agente sotto copertura, fa arrestare Lorenzo per frode al momento dell'annuncio delle nozze con Angela. Sequel naturale di video90 (Petra/Leocadia). Fonte: DIEGO TV (TkEpo-xOQtA, 1gg, 8.324 view).

**Tutti e 3 pronti sul disco** in `batch26/` (script+SEO+thumbnail+imgs+audio+VIDEO_FINALE), **accodati per l'upload automatico** in `queue/batch26.json` (formato standard `batch_upload.py`/`daily_upload_6.py`).

## ⚠️ LEZIONE su feedback utente 06/08 sera: mai un loop di retry a intervallo fisso quando si conosce già l'orario di sblocco
L'utente ha corretto un mio errore: avevo messo un retry ogni 30 minuti per le thumbnail mancanti, ma sapevo già che la quota si sblocca alle ~9:00. Sprecava chiamate API inutili per ore. **Fix applicato, da riusare come pattern standard**: quando un blocco ha un orario di sblocco noto e prevedibile (quota giornaliera, reset di mezzanotte Pacific, ecc.), usare un **cron una tantum/giornaliero all'orario esatto** (`crontab`, non un loop Python con sleep), non un polling a intervallo arbitrario. Applicato sia al fix thumbnail sia (per coerenza) all'upload dei video pronti:
- **`2 9 * * *`** → `retry_thumbnails_87_88_89_90_91.py` (ora tentativo singolo, non più loop; si autorimuove dal crontab quando tutte e 5 le thumbnail sono a posto)
- **`5 9 * * *`** → `daily_upload_6.py` (nuovo, aggiunto stasera — svuota `queue/*.json` appena la quota si sblocca, invece di aspettare il cron delle 23:00 esistente e perdere fino a 24h)

Il crontab scrive senza problemi da questa sessione (nessun blocco del guardrail descritto in [[crontab_writes_require_real_terminal]] — forse specifico a scritture più complesse, o risolto nel frattempo).

## Cosa succederà da solo domani mattina (07/08), senza intervento
1. **9:02** → le 5 thumbnail mancanti (video87/88/89/90/91) vengono impostate, riga cron si autorimuove se riesce.
2. **9:05** → `daily_upload_6.py` svuota la coda: carica video92/93/94 come bozza privata con thumbnail (max 6/giorno, questi 3 rientrano comodamente).
3. **Da verificare alla ripresa**: che entrambi i cron abbiano effettivamente girato (log: `retry_thumbnails_87_88_89_90_91.log`, `daily_upload_log.txt`), che le 8 thumbnail totali (87-91 + 92-94 se il campo thumbnail del job viene rispettato) siano a posto, e riprendere da lì con nuovi angoli (batch27) o con la playlist assignment manuale ancora in sospeso (vedi sotto).

## Ancora da fare quando si riprende (non automatizzato)
- **Playlist assignment fallita per TUTTI gli upload di oggi** (video84-91, quota) — `auto_assign_playlist` logga l'errore senza bloccare l'upload, NON è in retry automatico. Da assegnare manualmente (playlist Far Away/Forbidden Fruit/La Promessa) quando si riprende.
- **Membership CTA ciclo**: dopo video94 (no, posizione 2/3), il prossimo (video95) sarà no(3), poi video96 riparte sì(1) — vedi [[serietvfans_content_strategy]].
- **Nuova ricerca competitor per batch27**: nessun angolo ancora identificato. Fili ancora aperti non ripresi in questa sessione: Fikriye/Sadakat (Far Away, arma contro Alya), il complotto Demir/Kaya/Kadir/Muzaffer (Far Away), Ender/Zehra (Forbidden Fruit, mai risolto da video79), Leocadia (La Promessa, resta da vedere se verrà arrestata dopo la caduta di Lorenzo in video94).

---

# CHECKPOINT 06/08 SERA ~18:20 — video84-91 tutti consegnati, thumbnail in retry (storico, superato dall'aggiornamento sopra)

## Stato esatto a fine sessione
Tutti gli 8 video dell'arretrato (batch23/24/25, video84-91) sono ora **caricati come bozza privata**:
- video84 (Far Away) → `mUG8aqR68-M`, thumbnail OK
- video85 (Forbidden Fruit) → `WNYQVNr58xw`, thumbnail OK (fatto in sessione precedente)
- video86 (La Promessa) → `oA7uiUshKsI`, thumbnail OK (fatto in sessione precedente)
- video87 (Far Away) → `tUjTvEphPv8`, ⏳ thumbnail in retry
- video88 (Forbidden Fruit) → `4cPmCNO1GuY`, ⏳ thumbnail in retry
- video89 (La Promessa) → `_v5fa8q_UgA`, ⏳ thumbnail in retry
- video90 (La Promessa, Petra/Leocadia) → `Y-cUcGFxnAs`, ⏳ thumbnail in retry
- video91 (Far Away, Boran/Ekmel/Fikriye) → `tOW_skbFY3Y`, ⏳ thumbnail in retry

**Retry via cron giornaliero (non più loop 30min — corretto su feedback utente 06/08 sera, sprecava chiamate quando si sapeva già l'orario del reset)**: crontab `2 9 * * *` esegue `YOUTUBE_API/serietvfans/retry_thumbnails_87_88_89_90_91.py` un colpo solo, subito dopo il reset quota (~9:00 italiane). Lo script si autorimuove dal crontab quando tutte e 5 le thumbnail sono confermate a posto (vede `remove_self_from_crontab()`). Log: `retry_thumbnails_87_88_89_90_91.log`. Se al 07/08 mattina non è ancora tutto a posto, la riga cron resta e riprova il giorno dopo automaticamente — non serve intervento manuale a meno che la quota non si sblocchi mai (in quel caso investigare a mano).

**Quota YouTube Data API esaurita di nuovo il 06/08 pomeriggio** (dopo 5 upload consecutivi): si resetta a mezzanotte Pacific (~9:00 italiane del 07/08) — non ritentare manualmente prima, il retry loop ci pensa da solo.

**Playlist assignment fallita per TUTTI gli upload di oggi** (stessa quota, ma la funzione `auto_assign_playlist` logga l'errore senza bloccare l'upload) — NON è in retry automatico. Da assegnare manualmente quando la quota torna libera per video84-91 (playlist per soap: Far Away, Forbidden Fruit, La Promessa).

## video91 — nota qualità importante per i prossimi batch
Lo script iniziale di video91 (trovato già scritto da una sessione precedente) copriva solo metà della fonte (P3LTDOPmuqM): mancava tutto il sottofilone del ritorno di Fikriye (madre di Alya, creduta morta) e il sabotaggio del carico di Demir. Il fact-check ha rilevato l'omissione confrontando il transcript completo della fonte, lo script è stato espanso (narrazione passata da ~7.500 a 12.336 caratteri, video finale 12:19 invece dei soliti 8:00-8:20). **Lezione**: quando si eredita uno script già scritto da un'altra sessione/checkpoint, ri-verificare sempre contro il transcript completo della fonte prima di procedere al TTS, non fidarsi che sia già completo solo perché già scritto — vedi [[serietvfans_production_pipeline]].

## Personaggi senza foto in libreria (annotare per [[personaggi_library]])
Far Away: **Ekmel** (antagonista, mai avuto una foto dedicata) e **Fikriye** (madre di Alya, personaggio nuovo apparso solo in questo episodio) — per la thumbnail di video91 si è dovuto riusare Alya_Cihan invece di una scena con Ekmel. Se questi personaggi tornano in episodi futuri, cercare le foto prima di scrivere lo script.

## Prossimo step: batch26 (video92+)
Nessuna ricerca competitor ancora fatta per il prossimo batch. Angoli aperti/cliffhanger da questa sessione riprendibili: Ugur ("non ha finito di parlare"), Fikriye/Sadakat (arma contro Alya), Demir/complotto (Kaya-Kadir-Muzaffer), Ender/Zehra (Forbidden Fruit, sempre aperto da video79). Verificare stato reale canale (`youtube_channel_videos`) prima di scegliere, non solo la memoria locale.

---

# CHECKPOINT 06/08 mattina — batch23+24 (video84-88) IN PRODUZIONE (storico, superato dall'aggiornamento sopra)

## ⚠️ AGGIORNAMENTO 06/08 ~13:08 — leggere questo PRIMA della sezione sotto (che resta valida per il dettaglio ma alcuni dati sono superati)

**Stato produzione (6 video totali, batch23 video84-86 + batch24 video87-89) — AGGIORNATO 13:25, quasi tutto finito**:
| Video | Soap | Script/SEO/Thumb | Montaggio | Upload |
|---|---|---|---|---|
| 84 | Far Away (Meryem/confessione tribunale) | ✅ | ✅ 8:10 validato | da fare (quota esaurita) |
| 85 | Forbidden Fruit (matrimonio segreto) | ✅ | ✅ 8:09 validato | ✅ FATTO, ID WNYQVNr58xw |
| 86 | La Promessa (Lope/Curro/Angela) | ✅ | ✅ 8:21 validato | ✅ FATTO, ID oA7uiUshKsI |
| 87 | Far Away (Zerrin/Demir prima notte) | ✅ | ✅ 8:21 validato | ⚠️ caricato ID tUjTvEphPv8 MA thumbnail non impostata (quota) |
| 88 | Forbidden Fruit (foto/Feride) | ✅ | TTS locale in corso (~5/29 blocchi alle 13:25) | da fare |
| 89 | La Promessa (Angela ribellione) | ✅ | ✅ 8:04 validato | da fare (quota esaurita) |

**Restano da fare quando la quota YouTube torna libera (~09:00 italiane di domani 07/08, non prima)**: upload video84, 88, 89, 90; fix thumbnail su video87 (`batch24/thumbnail_video87_faraway.jpg`); continuare il retrofit membership CTA (fermo a 309/~1086).

## ⚠️⚠️ AGGIORNAMENTO FINALE 06/08 ~13:35 — stato di chiusura sessione, riprendere da qui

**7 video totali prodotti in questa sessione** (batch23 video84-86, batch24 video87-89, batch25 video90 — quest'ultimo aperto per continuare oltre il piano iniziale):
- ✅ **Completi e VALIDATI (script+SEO+thumbnail+montaggio ffmpeg -v error pulito)**: video84 (8:10), 85 (8:09, upload OK), 86 (8:21, upload OK), 87 (8:21, upload fatto ma thumbnail da rifare), 89 (8:04).
- ⏳ **In coda locale, non ancora pronti**: video88 (TTS ~11/29 blocchi alle 13:35), video90 (TTS in coda dietro video88, non ancora partito).
- **Angoli batch25 aggiuntivi già identificati per quando si riprende** (non ancora scritti): Forbidden Fruit → "Hasan Ali fa pace con tutti per colpire Ender" (fonte: L'Angolo delle Soap, epTJBiQCJSg); Far Away → "Alya scopre chi è il vero padre di Boran e fugge con Deniz" (fonte: DramaTurca, P3LTDOPmuqM).

**Prossimi step quando si riprende questa sessione o se ne apre una nuova**:
1. Aspettare/verificare che video88 e video90 finiscano il TTS locale (usare `until [ -f ... ]; do sleep 10; done` o controllare `.dispatch_local_audio_video88...log` / il file audio stesso).
2. Lanciare il montaggio di entrambi con `run_in_coda_montaggio.sh` (stesso pattern degli altri: narrazione+audio+cartella imgs+output → build_video.py), validare con `ffprobe`/`ffmpeg -v error`.
3. Verificare la quota YouTube reale (un tentativo di upload secco, non assumere) prima di procedere con: upload video84/88/89/90, fix thumbnail video87, ripresa retrofit membership CTA.
4. Se la quota è libera e c'è ancora margine (crediti Horacle: ~906 all'ultimo check, plenty), continuare con i 2 angoli batch25 già identificati sopra, poi proseguire con nuova ricerca competitor per i giorni successivi del calendario (06/08→31/08 ancora in gran parte scoperto).
5. Il canale ha ora la membership CTA visibile su ~309+ video già pubblicati (retrofit in corso, riprenderlo appena la quota lo permette) — vedi [[serietvfans_content_strategy]].

**Lezioni tecniche fissate in questa sessione (tutte salvate in memoria dedicata)**: [[chatterbox_real_pace_calibration]] (target ≥8300 caratteri, non fidarsi della stima teorica), [[serietvfans_batch_1_2_3_agosto_stato]] (cartelle VIDEO 6-22AGOSTO da non toccare senza verifica), cron/Full Disk Access risolto manualmente dall'utente (watchdog dovrebbero aver ripreso a funzionare, non riverificato con un ciclo naturale).

---

# ⚠️⚠️⚠️ CHECKPOINT DI CHIUSURA SESSIONE 06/08 ~14:15 — LEGGERE PER PRIMO SE SI RIPRENDE

**Sessione chiusa su richiesta esplicita dell'utente** ("salva tutta la memoria e apriamo nuova sessione") — tutto quello che segue è lo stato esatto lasciato in sospeso.

## Mappatura REALE video↔calendario (fonte: Piano_Editoriale_Canali.xlsx, foglio "Cal. Serie TV Fans", aggiornato in questa sessione)
- **19/08/2026** (riga 28): slot mancante (12:00 Lungo) completato con **video84 (Far Away)** → riga ora "3/6 programmati (mancano gli short)"
- **20/08/2026** (riga 29): **video85 (Forbidden Fruit) + video86 (La Promessa) + video87 (Far Away)** → "3/6 programmati (mancano gli short)"
- **21/08/2026** (riga 30): **video88 (Forbidden Fruit) + video89 (La Promessa) + video90 (La Promessa)** → "3/6 programmati (mancano gli short)" — nota: 2 La Promessa di fila in questo giorno, rottura minore della regola di composizione "1FF+1Promessa+1FarAway", accettata per allineare alla numerazione sequenziale
- **22/08/2026** (riga 31): **video91 (Far Away)** nel primo slot lungo → "1/6 programmati (mancano 2 lunghi + short)"

**⚠️ Questa mappatura è una RICOSTRUZIONE fatta a ritroso dallo slot mancante del 19/08, confermata dall'utente con "ok hai ragione tu" ma senza una verifica riga-per-riga incrociata — se in una sessione futura emerge un disallineamento, ri-verificare con l'utente prima di continuare a scrivere sul foglio.**

## Cosa manca per l'obiettivo (fino al 31/08/2026)
- **Video lunghi**: 2 per completare il 22/08 (video92, video93) + 9 giorni interi (23/08→31/08) × 3 = 27 → **29 video lunghi totali**
- **Short**: tutti e 78 (26 giorni × 3), **zero fatti finora** — pipeline short non ancora rodata in questa sessione, servirà definirla (probabilmente più leggera/veloce dei lunghi ma stesso overhead fisso di ricerca+script+thumbnail)

## Stato produzione tecnica esatto a fine sessione
Tutti i video 84-90 **completi, validati (ffmpeg -v error pulito) e pronti**. Video91 solo scriptato (script✅ SEO da fare, TTS da fare). Upload fatti: video85 (WNYQVNr58xw), 86 (oA7uiUshKsI), 87 (tUjTvEphPv8, **manca thumbnail**). Da caricare quando la quota YouTube è libera: video84, 88, 89, 90 (tutti pronti sul disco in `batch23/` e `batch24/`).

**Quota YouTube**: esaurita ~13:15 del 06/08, si resetta a mezzanotte Pacific (~09:00 italiane del 07/08) — verificare con un tentativo secco prima di assumere sia tornata libera.

**Crediti Horacle**: ~900 residui alle 13:35 (partiti da 1186), ampio margine, nessun fallback necessario per ora. Se finiscono: fallback Palmier Pro, NON Draw Things (vedi [[decisione_switch_horacle_palmier_immagini]]).

## Corsie disponibili — AGGIORNAMENTO IMPORTANTE DALL'UTENTE
L'utente userà tra 3-4 ore da questo checkpoint (quindi indicativamente dopo le ~18:00 del 06/08) **libererà una seconda corsia Kaggle** attualmente occupata da un altro progetto — da quel momento saranno disponibili 2 corsie Kaggle piene per Serie TV Fans invece di 1, oltre alla corsia CPU locale. Ritmo misurato finora: **~16 min/video con 1 corsia attiva** (vedi [[serietvfans_batch_1_2_3_agosto_stato]]) — con 2 corsie Kaggle libere il ritmo dovrebbe migliorare sensibilmente. L'utente vuole usare questi dati per decidere se in futuro è meglio dedicare Claude a un solo progetto per volta o dividerlo su più canali in parallelo — non è stata presa una decisione, resta una domanda aperta da affrontare con più dati.

## Prossimi step immediati quando si riprende
1. Verificare la quota YouTube reale (tentativo secco).
2. Se libera: caricare video84, 88, 89, 90 (bozza privata), fixare la thumbnail di video87, riprendere il retrofit membership CTA (fermo a 309/~1086, script idempotente `YOUTUBE_API/serietvfans/add_membership_cta.py`).
3. Completare video91 (SEO + TTS + montaggio + thumbnail — script già pronto, manca solo la pipeline).
4. Scrivere video92 (Forbidden Fruit, per completare il trio del 22/08 — nessun angolo ancora cercato) e video93 (terzo slot 22/08).
5. Continuare giorno per giorno verso il 31/08, aggiornando SEMPRE questo foglio Piano Editoriale man mano (non a fine sessione come stanotte) — l'utente lo ha chiesto esplicitamente.
6. In parallelo o dopo, affrontare gli short (78 mancanti) — nessuna pipeline ancora definita in questa sessione, da impostare.

Tutte le cartelle `imgs_videoNN` popolate dalla libreria personaggi. Tutte le thumbnail generate via Horacle + overlay `make_thumb_cinema.py`, badge soap verificato su ognuna.

**⚠️ LEZIONE CRITICA da applicare a OGNI video futuro**: il primo audio di video86 è uscito a 7:47 (sotto 8:00) nonostante lo script sembrasse sufficiente al calcolo teorico — vedi [[chatterbox_real_pace_calibration]] per il fix (target ≥8300 caratteri di narrazione pura, non fermarsi al primo superamento teorico di 8:00). Verificare SEMPRE con `ffprobe -show_entries format=duration` prima di lanciare il montaggio, mai fidarsi solo della stima a caratteri.

**Regola membership CTA applicata**: video84 sì(1), 85 no(2), 86 no(3), 87 sì(nuovo ciclo,1), 88 no(2), 89 no(3) — prossimo ciclo riparte da video90. Ciclo 1-ogni-3 sull'intera sequenza cronologica di produzione, non per singolo batch — vedi [[serietvfans_content_strategy]].

**Prossimo nella coda competitor per batch25 (non ancora scritto)**: nessun angolo ancora identificato — fare nuova ricerca competitor su Far Away/Forbidden Fruit/La Promessa prima di scrivere altri script (verificare sempre contro `_storico_video.md` E contro i video realmente live sul canale, non solo per data).

**✅ Upload FATTI prima che la quota si esaurisse di nuovo (06/08 ~13:10-13:15)**:
- video85 (FF) → ID WNYQVNr58xw, bozza privata, thumbnail OK
- video86 (Promessa) → ID oA7uiUshKsI, bozza privata, thumbnail OK
- video87 (Far Away) → ID tUjTvEphPv8, bozza privata caricata MA **thumbnail NON impostata** (quota esaurita a metà chiamata) — da rifare quando la quota torna libera: `youtube.thumbnails().set(videoId="tUjTvEphPv8", ...)` con `batch24/thumbnail_video87_faraway.jpg`.
- Retrofit membership CTA: arrivato a 309/~1086 (skip 167 già fatti in run precedenti + 142 nuovi), fermato di nuovo per quota.

**⚠️ Quota YouTube esaurita di NUOVO (~13:15)** dopo: 2 upload + set thumbnail parziale + un'altra sessione di retrofit. La quota Google si resetta a mezzanotte Pacific Time (~09:00 ora italiana il giorno dopo, NON alle 9:00 di oggi come pensato prima) — **non ritentare upload/retrofit finché non si verifica la quota reale** (un tentativo secco, se fallisce con quotaExceeded fermarsi subito, non insistere). Nel frattempo continuare SOLO con lavoro che non tocca l'API YouTube: script, TTS, montaggio, thumbnail locali (Horacle + overlay, quello è un'API diversa e ha ancora ~900 crediti). Video88 e video89 completati (script/SEO/thumbnail/audio o montaggio) restano in coda pronti per l'upload quando la quota torna, insieme al fix della thumbnail di video87.

## Stato esatto (06/08 ~12:45, sessione notturna post-ricarica crediti 5:30) — dettaglio storico, vedi aggiornamento sopra per lo stato più recente
Cartella: `YOUTUBE_API/serietvfans/batch23/`. Composizione: 1 Far Away + 1 Forbidden Fruit + 1 La Promessa (regola A/B confermata da Trends: Far Away ora il più forte, Il Paradiso ESCLUSO dalla rotazione, crollato a interesse ~4/100).
- **video84 (Far Away)** — Cihan confessa amore in tribunale + rivelazione Meryem/CD in cantina. Script ✅ fact-checked ✅ (corretta una fusione errata di 2 fonti in conflitto, vedi script per dettaglio) SEO ✅ thumbnail ✅ (bg_video84_faraway.png + thumbnail_video84_faraway.jpg, badge FAR AWAY forzato manualmente perché il filename senza spazio non veniva auto-rilevato) TTS: **in corso, coda locale**, partito ~12:23, richiede 35-40 min da quell'orario (log: `.dispatch_local_audio_video84_faraway_chatterbox.wav.log`). Menzione membership INCLUSA (1/3 del batch).
- **video85 (Forbidden Fruit)** — matrimonio segreto Yıldız/Çağatay, Feride si trasferisce. Script ✅ SEO ✅ thumbnail ✅ TTS: **in corso su Kaggle** (account bulio9111, slot 0, job Xy2Lug), partito ~12:26. Nessuna menzione membership (solo link descrizione).
- **video86 (La Promessa)** — Lope convince Curro, lui e Angela riprovano a fuggire; Leocadia blocca il ritorno di Pía. Script ✅ SEO ✅ thumbnail ✅ TTS: **in corso su Kaggle** (slot 1, job qHFeLW), partito ~12:33. Nessuna menzione membership.
- **PROSSIMO STEP quando i 3 .wav sono pronti**: validare audio, montaggio ffmpeg (`run_in_coda_montaggio.sh`), validazione ffmpeg -v error, poi upload bozza privata — **la quota YouTube Data API personale è ESAURITA** (usata dal retrofit membership stamattina), si resetta di solito verso le 9:00 ora italiana ma qui è già mattina inoltrata: ricontrollare `check_channel_monetization`/prova upload prima di assumere quota libera.
- **Retrofit membership CTA sul pubblicato**: 156/1086 video aggiornati (script `YOUTUBE_API/serietvfans/add_membership_cta.py`, idempotente, riprendibile), fermato per quota esaurita. Da rilanciare quando la quota torna libera — vedi [[serietvfans_content_strategy]].
- **Angoli batch24 (07/08) già individuati** (via competitor_analyzer, non ancora scritti): Far Away → prima notte di Zerrin ("la frase più gelida della stagione", L'Angolo delle Soap); Forbidden Fruit → "la foto finisce a Feride, per Yıldız è la fine" (sequel diretto di video85, L'Angolo delle Soap, freschissimo); La Promessa → Ángela si ribella apertamente a Lorenzo e Leocadia (Film Analizzato / Film Zone HD).
- **Cron delle 5:30 fallito per un bug di sistema**: vedi nuova voce separata da cercare in memoria (Full Disk Access di `cron` revocato, bloccava ANCHE i watchdog esistenti) — risolto manualmente dall'utente in System Settings + `sudo launchctl kickstart -k system/com.vix.cron`, non ancora riverificato con un ciclo naturale.
- **Scoperta importante**: esiste una pipeline vecchia/orfana nelle cartelle `VIDEO 6AGOSTO`→`VIDEO 22AGOSTO` (diversa numerazione, video31-56+) parzialmente sovrapposta/duplicata rispetto al canale reale — vedi [[serietvfans_batch_1_2_3_agosto_stato]], NON toccare senza verifica angolo-per-angolo.

---

# CHECKPOINT (precedente) — batch19-22 (video72-83) TUTTI COMPLETI, nessun lavoro pendente

## ✅ Stato finale confermato
Batch19, 20, 21, 22 (video72-83, 12 video totali): tutti caricati come bozza privata su YouTube CON thumbnail impostate correttamente (il retry automatico di batch22 è riuscito al tentativo 27, `thumbnails_retry_loop_22.sh` terminato con successo e non più in esecuzione). Nessuno script in background da controllare per questi batch. **Prossima sessione: iniziare direttamente il batch23** (video84-86).

## 🎉 CANALE MONETIZZATO (comunicato dall'utente il 06/08)
Non ancora verificato con dati diretti da questa sessione (`check_channel_monetization`/`get_my_channel_overview`). Alla ripresa: confermare lo stato reale in YouTube Studio/Nexlev, e valutare se cambia qualcosa nella strategia (es. più peso a watch-time/RPM ora che genera revenue reale, non solo crescita).

## ⚠️ Composizione batch: la regola è CAMBIATA dopo il 04/08 — vedi [[serietvfans_content_strategy]] per intero
Non fidarsi della vecchia indicazione "alternanza Far Away/Paradiso" scritta in questo checkpoint in una versione precedente: è stata superata il 06/08 da un'altra sessione, basata su dati Google Trends. **Regola attuale**: ogni batch fisso = 1 Far Away + 1 Forbidden Fruit + 1 La Promessa (Il Paradiso esce dalla rotazione fissa). Dichiarato **A/B test 2 settimane/2 batch** contro i dati views reali storici (che davano invece Far Away come peggior performer) — il file linkato ha i dettagli e dove tracciare l'esito.

## ⚠️ NOTA: make_thumb_cinema.py modificato da un'altra sessione (dopo la scrittura di questo checkpoint)
Un'altra sessione concorrente ha esteso lo script condiviso `make_thumb_cinema.py` con: badge automatico nome-soap (rilevato dal testo, vedi array `SOAPS` nel file — aggiungere lì se arriva una soap nuova), zona di esclusione volto ristretta alla sola fascia occhi (non più mezza faccia) per lasciare più libertà al posizionamento testo, margine inferiore ridotto e testo leggermente spostato a destra, contorno testo più spesso (benchmark contro LuLu News via Nexlev Thumbnail Tester, vedi [[nexlev_thumbnail_tools]]). La firma ora include un argomento opzionale `BADGE:NOME SOAP` per forzare il badge se il rilevamento automatico sbaglia. **Prima di richiamare lo script nella prossima sessione, rileggerlo per intero** (potrebbe essere cambiato ulteriormente nel frattempo, essendo condiviso tra sessioni concorrenti).

## Metodo thumbnail: CONFERMATO Horacle come standard (chiarito dopo un equivoco)
L'utente ha chiesto conferma se le thumbnail si stessero facendo con ChatGPT — chiarito che NON è mai stato deciso ChatGPT come standard (era stato solo "da provare" in una sessione precedente), e che il fallback locale usato per batch22 era solo per crediti Horacle esauriti. L'utente ha scelto esplicitamente **Horacle** come metodo confermato e ha ricaricato i crediti (da 8 a 2508). Le 3 thumbnail di batch22 sono state RIGENERATE con scene Horacle (2 personaggi, espressioni forti) sostituendo il fallback split-screen. **Per i prossimi batch usare sempre Horacle**, non chiedere più conferma su questo — solo se `get_credits` torna sotto i 40 disponibili avvisare l'utente e proporre il fallback `make_thumb_splitbg.py` come piano B temporaneo.

## Stato finale batch22
Tutti e 3 caricati come bozza privata (ID: video81=TS_xcizSnF8, video82=6AI8YRf-Eqg, video83=q1UpPk_Ie1s). **Thumbnail (versione Horacle aggiornata) e assegnazione playlist falliti per quota YouTube esaurita** (di nuovo, come già capitato per batch19-20 e prima ancora batch15-16 — pattern ricorrente, sera/notte dopo il cron upload delle 23:00). Retry automatico in corso in background: `YOUTUBE_API/serietvfans/thumbnails_retry_loop_22.sh` (ogni 30 min fino a successo, log in `thumbnails_retry_loop_22.log`). Se si riprende e non è ancora andato a buon fine, ricontrollare quel log o rilanciare `retry_thumbnails_22agosto.py` a mano dopo il reset quota (~9:00 ora italiana).

**Nota**: `batch_upload.py` ora tenta anche di creare/assegnare automaticamente una playlist per soap (aggiunta da un'altra sessione, non testata da questa) — ha fallito per la stessa quota esaurita ma non ha bloccato l'upload del video. Se ricapita, verificare se le playlist vanno sistemate manualmente insieme alle thumbnail.

## ⚠️⚠️ NUOVA COMPOSIZIONE BATCH dal 04/08 — vedi [[serietvfans_content_strategy]] per la regola completa
Sostituita la regola "2 Forbidden Fruit + 1": ora ogni batch = **1 Forbidden Fruit + 1 La Promessa + 1 slot alternante Far Away/Il Paradiso delle Signore**. Batch22 ha usato Far Away (l'utente ha notato buone performance). **Batch23 deve usare Il Paradiso delle Signore** nello slot 3, poi batch24 di nuovo Far Away, ecc. — aggiornare la riga "ultimo usato" in [[serietvfans_content_strategy]] dopo ogni batch.

## ⚠️ Horacle: crediti esauriti il 04/08 (8 disponibili, ne servono 40/immagine)
Le thumbnail di batch22 sono state fatte con un **fallback locale a costo zero**: `make_thumb_splitbg.py` (due foto reali affiancate, NO AI) + lo stesso overlay `make_thumb_cinema.py` (bianco/giallo, no box). Qualità inferiore alle scene generate da Horacle ma funzionale. Se si riprende e i crediti sono tornati disponibili (`get_credits`), tornare al metodo Horacle standard per i prossimi batch — il fallback split-screen resta comunque un'opzione valida se i crediti scarseggiano di nuovo.

## ⚠️ Kaggle: NON più bloccato di default, ma verificare quale account
[[kaggle_api_key_403_blocker]] riguardava l'account primario. `dispatch_tts.sh` ora smista automaticamente anche su un secondo account `bulio9111` (vedi [[kaggle_secondo_account_bulio9111]]) che risulta funzionante al 04/08. Usare sempre `dispatch_tts.sh` invece di gestire Kaggle a mano — decide da solo dove instradare (vedi [[dispatch_tts_automation]]).

## Direttiva utente 04/08: analizzare sempre i metadati/trend dei competitor migliori
Per ogni batch, scegliere gli angoli guardando quali video competitor stanno performando meglio (view count, freschezza) e costruire titoli/hook che possano superarli, non solo angoli "liberi" qualsiasi. Applicato per la prima volta su batch22: LP scelto da una fonte a 3.959 view/1 giorno (Diego TV, Jana/matrimonio), FF e FarAway da fonti dense ma con titoli clickbait fuorvianti rispetto al contenuto reale (riscritti sui fatti verificati, non sul titolo clickbait).

## Batch22 — dettaglio fonti (riferimento per continuità di canone)
- Video81 (FF): Şahika convince Mert a svuotare la Argun Holding, Ender costretta a firmare la fusione, Hasan Ali prende la sede. Sequel diretto del thread Zehra/Mert aperto in video79 (dubbio mai risolto). Fonte: sub-plot corporate da un video con titolo fuorviante su Yıldız (non usato quel filone, già coperto in video78).
- Video82 (LP): Curro, spinto da un sogno/visione di Jana (non letteralmente risorta), interrompe il matrimonio di Angela e Lorenzo all'altare. Fonte: Diego TV, alta qualità, 3.959 view.
- Video83 (Far Away): Sadakat chiede a Cihan di eliminare Ugur per proteggere il segreto sulla vera paternità di Boran; Demir ricatta Zerrin con un matrimonio forzato per liberare Şahin. Fonte: stesso video della sentenza di divorzio Alya/Cihan già coperta da un nostro video precedente — riusata SOLO la parte sul segreto Boran/ricatto Zerrin, non la scena del tribunale.

---

# CHECKPOINT 03/08/2026 ~15:30 — batch19-20-21 (video72-80) TUTTI CONSEGNATI

## Stato finale di questa sessione
- **Batch 19 (video72-74), batch 20 (video75-77), batch 21 (video78-80): tutti e 9 caricati come bozza privata con thumbnail impostate correttamente.** Nessun lavoro pendente su questi batch.
- **Batch 21 è stata la prima produzione interamente da zero gestita in autonomia in questa sessione** (competitor research → script → fact-check → SEO → thumbnail → TTS Kaggle → montaggio → upload) — vedi dettaglio più sotto, utile come riferimento per il prossimo batch (22 agosto, video81-83, comporre 2 Forbidden Fruit + 1 La Promessa/Terra Amara).
- **⚠️ Errore fatto e corretto in questa sessione, da non ripetere**: nella produzione da zero mi sono dimenticato di popolare `imgs_videoNN/` (le foto multiple per il montaggio/slideshow, PESCATE DALLA LIBRERIA PERSONAGGI — non generate — vedi [[personaggi_library]]), diverse dalla singola immagine di sfondo della thumbnail. Il montaggio fallisce subito con "nessuna immagine trovata" se questo step viene saltato. **Checklist produzione da zero completa**: script → fact_checker → youtube_seo_optimizer → thumbnail (Horacle bg + overlay) → **imgs_videoNN dalla libreria personaggi (NON dimenticare)** → TTS Kaggle → montaggio → validazione ffmpeg → upload.

## ⚠️⚠️ NUOVO STILE THUMBNAIL dal 03/08 (sostituisce il box rosso) — vedi [[thumbnail_stile_cinema_chatgpt]] per la ricetta completa
Su richiesta esplicita dell'utente, il box rosso è stato eliminato: **testo sopra BIANCO + testo sotto GIALLO `(255,210,0)`, nessun riquadro/sfondo colorato**, solo Impact con bordo nero direttamente sulla scena. `make_thumb_cinema.py` riscritto con nuova firma `main(bg, top_text, bottom_text, out, nologo=False)`. Rilevamento volto OpenCV esteso anche al testo in basso. Mantenere sempre 2-3 personaggi per scena ("selezione doppia"), puntando sull'espressione più forte dello script.

**Espressioni rabbia/tristezza rafforzate via Horacle** (non ChatGPT — troppo fragile, vedi storico conflitti sessioni in [[thumbnail_stile_cinema_chatgpt]]): prompt MOLTO espliciti ("VISIBLY ANGRY, jaw clenched" invece di "disapproving") danno risultati nettamente migliori. Validato su video78 (Feride) e video79 (Zehra in lacrime). Se in futuro mancano crediti Horacle per rigenerare (capitato 03/08, 38/40 disponibili), va bene tenere la versione precedente se già decente.

## Batch 21 — dettaglio fonti (riferimento per continuità di canone)
- Video78 (FF): Şahika si infiltra tramite Feride per sabotare Yıldız/Çağatay, matrimonio segreto, Feride si trasferisce in casa loro. Fonte: L'Angolo delle Soap (`GKAd9xmefhQ`).
- Video79 (FF): Ender/Şahika rivelano a Zehra che Mert ha un figlio segreto, dubbio radicato non risolto (cliffhanger aperto, riprendibile in un batch futuro). Fonte: Ashford TV (`N0pFdCDP2aQ`, qualità narrativa bassa, riscritto sui fatti).
- Video80 (LP): sequel diretto di video75 (batch20) — Manuel strappa l'ordine di Cristóbal contro Pía, lo caccia dal corridoio. Fonte: La Promessa Oggi! (`Oou-UXYtW1A`, altissima qualità, 21K view sul competitor).
- Scartata: fonte `iGVIQvDwrvA` (TRAME PROIBITE) per conflitto di canone (Halit dato per morto, contraddice il nostro canone "Halit vivo").

## Prossimo batch: 22 agosto (video81-83)
Nessuna ricerca ancora fatta. Ricordarsi di verificare lo stato REALE del canale (`youtube_channel_videos` sul channelId `UCwgtJLcJWxO5p_VAILE4sdA`) prima di scegliere gli angoli, non solo `_storico_video.md` locale — la memoria locale può essere indietro rispetto a cron/altre sessioni.

## Ancora aperto (mai confermato)
Chiedere se l'utente ha eliminato le 3 bozze duplicate di batch12 (Nadir `Vb4PcQGB14I`, Duca `tDjM0xs6Mos`, Ángela `2Cx7qS8O_aw`).

## kaggle CLI
Reinstallato in sessione precedente con `pip3 install --user kaggle`, eseguibile in `/Users/giulianopuggioni/Library/Python/3.8/bin/kaggle` — aggiungere al `$PATH` prima di ogni chiamata.

## Upload YouTube: venv dedicato obbligatorio
`batch_upload.py`/`retry_thumbnails_*.py` vanno lanciati con `YOUTUBE_API/serietvfans/.venv/bin/python3`, non col python3 di sistema (manca `google.auth`).

## Corsia Kaggle GPU dedicata a Serie TV Fans — rodata su 6 batch consecutivi (13-14, 15-16, 17-18, 19-20, 21)
Dataset `giulianopuggioni/serietvfans-batch1314`, kernel `giulianopuggioni/serietvfans-tts-batch1314` (GPU T4x2), cartella locale `SERIETVFANS_KAGGLE/`. Procedura: sostituire i .txt (versione FLAT senza paragrafi, non la `_paragrafi.txt`) nel dataset, aggiornare `JOBS` in `kaggle_batch_serietvfans.py`, `kaggle datasets version -p ... -m "..."`, poi `kaggle kernels push -p SERIETVFANS_KAGGLE/kernel_batch1314`, poi `kaggle kernels output ... -p <cartella>` per scaricare i .wav+.timings.json una volta `COMPLETE`. **Kaggle limita a 2 sessioni GPU contemporanee sull'intero account**: se altri batch (es. Soap Opera Italia) stanno già usando le 2 sessioni, il push fallisce con "Maximum batch GPU session count of 2 reached" — mettersi in un loop di retry, MAI interrompere i kernel altrui. **Montaggio ffmpeg resta SEMPRE locale** (CPU-bound), tramite `run_in_coda_montaggio.sh` (fino a 4 slot paralleli, stesso discorso: se altri batch occupano tutti gli slot, aspettare senza interrompere).

## ⚠️⚠️ DIRETTIVA PERMANENTE più importante: MAI ripetere per allungare, SEMPRE cercare transcript completi
Vedi [[serietvfans_production_pipeline]] per il metodo completo.

---

# Appendice: note durature (consolidate da 4 memorie separate, 06/08/2026)

## Canale monetizzato (comunicato dall'utente 06/08)
Non ancora riverificato con `check_channel_monetization`/`get_my_channel_overview` diretto da nessuna sessione. Cambia il quadro economico: non più solo crescita/watch-hours in vista di soglia, ora revenue reale collegata a RPM/watch-time — da tenere a mente nelle decisioni su composizione batch (vedi [[serietvfans_content_strategy]]). Se emergono report di revenue, tracciarli qui.

## Throughput misurato (notte 06/08, per pianificazione capacità)
7 video lunghi completi/validati in 1h50min = **~16 min/video** con 1 sessione Claude Code ma parallelismo sotto (1 corsia TTS locale + fino 2 Kaggle GPU contemporanee, scrittura script sovrapposta alle attese di render). Con 2 corsie Kaggle piene dedicate (liberate dall'utente nel pomeriggio del 06/08) il ritmo dovrebbe migliorare. **Domanda aperta dell'utente**: meglio 1 sessione mono-progetto o dividere su più canali in parallelo (pattern normale, vedi [[dispatch_lanes_unified_queue]])? Nessuna decisione presa — raccogliere ritmo reale (video completi/tempo) in ogni sessione di produzione lunga futura per rispondere con dati.

## Audit revenue e ottimizzazioni (02/08/2026, ChatGPT agent-to-agent)
**Causa reale "revenue zero" (verificata su YouTube Studio, non un bug Nexlev/OAuth)**: canale accettato nel YPP il 28/07/2026, sotto soglia 4.000 ore/365gg qualificate (aveva 3.205, mancavano ~795, ritmo ~2.000h/28gg → soglia raggiunta da sola in ~10-12gg senza intervento tecnico). AdSense già collegato e pronto.
**Storico revenue completo (2023-2026, via `get_my_revenue_report`)**: 2023 (da giugno) $24.004 (picco virale, $150-360/giorno autunno 2023), 2024 $10.641 (declino), 2025 gen-lug $551 (quasi spento), cliff a zero assoluto dal 10/06/2026 (sospensione account, non calo organico). **Totale vita canale ~$35.330** — dimostra che €3-7k/mese è raggiungibile con engagement alto, non un tetto strutturale della nicchia. Motiva anche l'espansione EN/ES parallela ([[worldsoapspoilers_en_checkpoint]]).
**Ottimizzazioni CONFERMATE e implementate (stesso giorno)**: thumbnail via Horacle invece di ChatGPT (già in [[serietvfans_production_pipeline]]); hook primi 60s ristrutturato (rivelazione diretta 0-10s, niente saluti — vedi [[pietro_g_metodo_copy]]); SEO su query reali esterne (Keywordtool.io/Google Suggest) validate via Nexlev prima del titolo finale. Tutte già in `SKILL.md`/skill dedicate, non serve rifare i video già pubblicati.

## ⚠️ Pipeline orfana/duplicata da NON toccare senza verifica
Cartelle `VIDEO 6AGOSTO/` → `VIDEO 22AGOSTO/` (video31-56+, prodotte 31/07-02/08 con `generate_narration_discorsivo.py`) sono un ramo di produzione parallelo e più vecchio, scollegato dalla pipeline attuale (video72+). **Verificato**: più angoli duplicano video REALMENTE già live sul canale (es. video38/37 = contenuti già pubblicati con altro titolo). Anche doppioni interni tra batch6/batch8. Stato per cartella: 6AGOSTO/7AGOSTO mai caricate ma duplicate (non caricare as-is); 8AGOSTO/9AGOSTO confermate già pubblicate (folder-naming non corrisponde a data reale); 10AGOSTO→22AGOSTO non ancora controllate. **Lezione**: il nome cartella NON è la data di pubblicazione reale — verificare sempre con `youtube_channel_videos` sul canale reale prima di caricare o produrre da queste cartelle. Se materiale genuinamente nuovo, va bene riusarlo; altrimenti scartare o chiedere all'utente prima di eliminare (vedi [[feedback_elimina_dati_progetti_scartati]]).

---

# Storico compresso (batch precedenti, tutti CONSEGNATI e CARICATI — non rifare)
Batch 1-21 (video1-80) + evergreen weekend (TA/BB) + redo 15 thumbnail: tutti completi. Dettagli angoli/fonti in `_storico_video.md` (righe `[N/08]`). Regole di stile permanenti attive: [[pietro_g_metodo_copy]] · [[serietvfans_content_strategy]] · [[thumbnail_stile_cinema_chatgpt]] (nuovo stile no-box dal 03/08, face-detection obbligatoria) · [[serietvfans_production_pipeline]] · [[coda_cpu_jobs_pesanti]] (mai pkill generico, sempre `run_in_coda.sh`/`run_in_coda_montaggio.sh`) · [[serietvfans_production_pipeline]] (metodo transcript-completo, DIRETTIVA PIÙ IMPORTANTE) · [[validate_mp4_before_upload]] · [[serietvfans_content_strategy]] (2 Forbidden Fruit + 1 La Promessa/Terra Amara) · [[personaggi_library]] (imgs_videoNN dalla libreria, non generate) · narratrice ANONIMA (nessun nome).