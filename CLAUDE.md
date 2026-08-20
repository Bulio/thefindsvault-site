# MEMORIA UNIFICATA — Progetto rilancio canale YouTube "Serie TV Fans"

> Memoria unificata l'8 agosto 2026 (sera) dalle sessioni: "Analisi e ottimizzazione
> grafico storico" (strategia/formato) + "Produzione batch Serie TV Fans" (pipeline
> sul Mac, handoff del 08/08 ~16:45). Leggere PRIMA di qualsiasi attività sul canale.
> Documenti completi in `memoria-canale/`.

## Il canale e l'obiettivo

- **Canale**: Serie TV Fans (`UCwgtJLcJWxO5p_VAILE4sdA`, @serietvfans) — nicchia
  "anticipazioni soap" in italiano. 60.100 iscritti, 14,1M viste, ~1.050 video.
- **OBIETTIVO**: tornare ad almeno **64.000 viste/giorno** (metà del picco storico di
  129.000 del 2023). Tappe: agosto 8–12K/g · settembre 20–30K/g · ott–nov 45–64K/g.
- Baseline 8/8/2026: ~2.200 viste/giorno.

## Storia vera del grafico (riconciliata dalle due sessioni)

1. **Picco 2023**: Terra Amara, fino a 129K viste/giorno e $150–360/giorno.
   Revenue vita canale: ~$35.3K (~€32.8K).
2. **Declino 2024–2025**: strutturale — fine di Terra Amara, non penalizzazione.
3. **Cliff a ZERO dal 10/06/2026**: sospensione account/YPP (NON calo organico).
   **YPP riaccettato il 28/07/2026**, revenue ripartita ~05/08. La "monetizzazione
   mancante" di luglio è spiegata da questo — nessun problema residuo.
4. **Germoglio attuale**: Forbidden Fruit 24K viste (28/07), Far Away costante 1,2–3,1K.

## Il pubblico (dato fondamentale)

- **87,6% over 55 (68,7% over 65), 85,3% donne**, 98% Italia.
- Conseguenze: orari diurni, thumbnail con testo GRANDE, narrazione "amica che
  racconta", TTS curata. Gli Shorts NON sono la strategia per questo pubblico.

## LE DUE CORSIE (regola inter-sessione, NON violare)

- **Corsia LUNGHI**: questa. Produzione, strategia, analytics dei long-form.
- **Corsia SHORT: è di un'altra chat — MAI toccarla** (memoria Mac
  `feedback_divisione_corsie_short_lunghi`). Qui si possono solo LEGGERE i dati
  Shorts per il verdetto del 22/8 (criteri: viste medie, % pubblico non iscritto,
  iscritti portati, clic ai long-form). La decisione va coordinata con quella chat.
- Kaggle: max 1 slot se esiste `bin/kaggle_lane_reserved.txt` (sul Mac).

## Pipeline di produzione ATTIVA (sul Mac, sessione batch)

- **Video 102–113 prodotti e in coda upload** (batch29–32 in `YOUTUBE_API/serietvfans/`).
  Storico angoli/fonti: `~/Desktop/Claude/YOUTUBE_API/serietvfans/_storico_video.md`.
- **Cron upload `0 23 * * *`**: carica 6 bozze PRIVATE/giorno dalle `queue/batch*.json`.
  In coda: video 99, 102–113.
- **Notturna autonoma `0 5 * * *`** (`bin/run_night_batch_serietvfans.sh`, claude -p
  headless, token `~/.claude/night_oauth_token`): 6 lunghi/notte, cap $25.
  Prima run autonoma: 09/08 → video 114–119.
- **Calendario**: `PIANO EDITORIALE/Piano_Editoriale_Canali.xlsx` foglio
  "Cal. Serie TV Fans" — lunghi coperti fino al 29/08 (ai 2/3).
- **Regole upload**: SEMPRE bozza privata + containsSyntheticMedia; max 6/giorno;
  quota API resetta ~9:00 italiane.
- **Canone narrativo**: prima di produrre, checkpoint MASTER + `_storico_video.md`
  (lì anche canali banditi e farm IA). ⚠️ Il controllo anti-duplicati va rinforzato:
  trovate 3 coppie di duplicati pubblicate + 3 programmate (stessa scena, 2 video).

## Regola IMMAGINI per le clip video (indicazione utente, 8/8/2026 sera)

- **Mix 50/50**: a parità di fabbisogno, generare SOLO metà delle immagini nuove;
  l'altra metà va presa dalle **cartelle personaggi già esistenti sul Mac** (immagini
  già usate in altri video). Es.: servono 10 → 5 generate + 5 riusate. Obiettivo:
  mantenere lo stesso livello visivo dimezzando le generazioni.
- **Le librerie immagini NON si cancellano MAI** — né quelle delle serie TV
  (Serie TV Fans) né quelle di Storie Ispiranti (stessa strategia su quel canale).
  Servono proprio per il riuso.
- **Refresh**: rigenerare le foto dei personaggi solo ~ogni 2 mesi (cambia la resa
  e si accorcia la "memoria" visiva del pubblico sulle immagini ripetute).
- Nota sessione cloud: le cartelle stanno sul Mac; qui la regola si registra e si
  passa alla pipeline.
- ⚠️ **PIATTAFORMA GENERAZIONE (utente, 8/8 sera): NON si usa più Horacl — si usa
  PALMIER.** Dettagli (accesso, crediti, MCP) noti solo alla sessione Mac: la
  produzione visiva/TTS va fatta LÀ con Palmier. In questa sessione cloud resta
  collegato solo Horacl (16 crediti free, inutilizzabile) — non usarlo.

## ⏱ Taratura tempi nuovo formato (per riconfigurare la notturna)

- Decisione utente 8/8: qualità > quantità; se il test passa la notturna scende
  probabilmente a **1 batch/notte** col nuovo formato.
- **Dato #1 (8/8, sessione cloud)**: script completo 20 min (FF 10–14 ago,
  2.474 parole, formula completa) = **~8–10 min di lavoro AI** (2 passate).
  → 3 script/notte ≈ 30 min di scrittura; cap $25 ampiamente sufficiente.
- Mancano da misurare (sul Mac): TTS, raccolta/gen immagini col mix 50/50,
  montaggio, QC. Ogni sessione di produzione nuovo formato DEVE loggare i tempi
  di fase in `memoria-canale/test-formato-monitoraggio.md` (sezione Log).

## ⚠️ CONFLITTO APERTO da decidere dopo il test (priorità 1)

- La pipeline notturna produce **6 lunghi/giorno con il vecchio formato (8–9 min)**.
- La strategia validata sui dati dice: **3 lunghi/giorno da 18–25 min** (formula sotto)
  battono 6 da 8 min (watch time, suggeriti, retention — i concorrenti con 1/3 degli
  iscritti fanno 10–30K viste/video così).
- **Il video TEST col nuovo formato esce SAB 8/8 ore 18:00** (TPLMF). Verifica a 48h:
  retention min 1 ≥65% (baseline ~50%) · durata media ≥5:00 (baseline ~2:30) ·
  viste 48h ≥1.500 (baseline 150–400) · commenti ≥30. Se passa 2/4 → riconfigurare
  la notturna sul nuovo formato (script più lunghi, meno video) dal 17/8.

## La diagnosi (problemi trovati nei dati)

1. Video 8–9 min vs 18–50 min dei concorrenti vincenti → poco watch time.
2. Retention: −50% nel primo minuto (hook che introduce invece di spoilerare).
3. Ricerca YouTube al 2,8% del traffico (titoli senza date). Target ≥10%.
4. Duplicati generati dal flusso di produzione (6 coppie trovate).
5. Slot notturni per errore (00:00, 22:00) — controllare sempre l'orario.
6. Serie morte (Beautiful, Paradiso: 40–130 viste) rubavano slot → FUORI.

## Portafoglio serie (priorità)

1. **Tutto per la mia famiglia** (concorrenti: 26–33K/video — era scoperta!)
2. **Forbidden Fruit** (validata: 24K)
3. **Far Away** (la più reattiva del canale)
4. **La Promessa** (storica, 1 slot)
5. Rotazione: La forza di una donna, Melek. FUORI: Beautiful, Paradiso delle Signore.

## Formula del nuovo formato (estratta dai transcript dei top competitor)

Video 18–25 min: HOOK 0:00–0:45 (spoiler frontali + evento shock SENZA nome = loop
aperto mai risolto) → RESET "tutto comincia quando…" → 5 blocchi da 2,5 min chiusi da
domanda-ponte → CTA unica al min 10 (chiede una TEORIA) → 2 blocchi speculativi
("le anticipazioni lasciano intendere…") → chiusura troncata + rilancio. ZERO
intro/sigla/saluti. Ritmo: 1 fatto ogni 15–25 sec; mai >90 sec sulla stessa linea;
similitudine popolare ogni 2 blocchi. Dettagli: `memoria-canale/formula-script-20min.html`.

**Voce (tutti i competitor usano TTS AI)**: 145 parole/min, frasi shock isolate e corte
(la punteggiatura controlla la prosodia), domanda ogni ~2 min, testare voce femminile
25–35 calda, ducking dinamico, 1 sec di silenzio prima della frase clou.
Primo test formato "speciale voci": video112 (pipeline Mac).

## Titoli, SEO, thumbnail

- `SERIE Anticipazioni DAL X AL Y MESE: PERSONAGGIO + evento shock 😱`
- Domenica: 1 video "riassunto settimana" per serie con date (magnete di ricerca).
- Descrizione: riga 1 serie+date+personaggi; capitoli; hashtag.
- Thumbnail: primo piano + freccia/cerchio + 3–5 parole GRANDI (≠ dal titolo).
- Membership CTA: retrofit fatto su ~309+ video (misurarne l'effetto).

## PROCESSO STANDARD (concordato con l'utente)

1. **Verifica trame** su fonti UFFICIALI italiane (ComingSoon, TGCOM24, TvSerial,
   Sorrisi, Mediaset Infinity, Davide Maggio) — i competitor raccontano puntate
   turche future o inventano. Le parti speculative vanno dichiarate nello script.
2. **Riga PUBBLICARE**: ogni script porta in PRIMA riga della descrizione
   `PUBBLICARE: GIORNO X/X ORE XX:XX` (l'utente la toglie quando programma).
3. **Ordine cronologico**: già in onda → subito (slot secondari); settimana in onda →
   giorno prima; future → settimana dopo; mai un effetto prima della causa.
4. **Slot**: vecchio formato 10/11/12 e 21 · nuovo formato 9:00 e 18:00 ·
   settimanali nel weekend precedente.
5. Claude (sessioni cloud) NON accede a YouTube Studio: legge analytics via NexLev;
   programmazione/descrizioni le applica l'utente con le mappe. La pipeline Mac
   invece carica bozze via API (mai pubblicare direttamente).

## Stato all'8 agosto 2026 (sera)

- **Batch di prova verificato** (`memoria-canale/batch-verificato-8-agosto.html`):
  TPLMF (SAB 8/8 18:00 — TEST) · Forbidden Fruit (DOM 9/8 9:00) · Far Away (DOM 9/8 18:00).
- **Coda ripianificata**: 37 video 9–20/8 mappati in
  `memoria-canale/mappa-ripianificazione.html` + `ripianificazione-8-23-agosto.xlsx`:
  3 duplicati da eliminare, 9 video bruciati anticipati, 3 slot notturni corretti,
  Petra→11/8, FOTO Feride→13/8. L'utente applica a mano.
- **Da verificare**: "Petra guarisce" (20/8) contraddice il "tetano senza scampo"
  delle trame ufficiali — confermare prima dell'uscita.
- Playlist da sistemare: TPLMF (nuova), Forbidden Fruit, Far Away, La Promessa.

## Prossimi passi

1. **9–10/8**: valutare il test (curva retention completa) → tarare hook → decidere
   la riconfigurazione della pipeline notturna (vedi CONFLITTO APERTO).
2. Incrociare il grafico storico con le date della pipeline: rimonetizzazione 28/07,
   ritmo 6/g, membership retrofit, video112 "speciale voci" (variabili nuove).
3. Batch 17–23 col processo standard. 4. Verdetto Shorts il 22/8 (coordinato con la
   chat della corsia SHORT). 5. Post community quotidiani (7 pronti nel kit).
6. Su Mac: `memory_search.py "serie tv fans revenue analytics"`, checkpoint
   `serietvfans_batch_1_2_3_agosto_stato`, benchmark `serietvfans_competitor_benchmark_02agosto`.

## Canale SOAP OPERA ITALIA (SOI) — binario SEPARATO (istruzioni utente 11/8/2026)

- **Canale**: `@soapoperaitaliaa` (`UCjid0Q5NC0No3HRHIF2_tdg`, doppia A — esiste
  un omonimo concorrente @SoapOperaItalia da 310 iscritti). Account Google:
  `bulio91veo3@gmail.com`. Baseline 11/8: 2 iscritti, 4.196 viste, 38 video,
  ultimi 25 video a 0–14 viste.
- **REGOLA**: stesso impianto di lavoro di STF (baseline → monitoraggio → check
  automatici → handoff Mac) ma **SEMPRE SEPARATO**: tutto in
  `memoria-canale/soap-opera-italia/`, mai mischiare dati/decisioni SOI con STF.
- Scheda e criteri: `memoria-canale/soap-opera-italia/monitoraggio-soi.md`.
  Check cloud ogni 3–4 giorni ~10:30 Italia (sfalsati dai check STF delle 10:00).
- **Da fare (in ordine)**: 1) aggancio NexLev via browser con l'account sopra
  (utente o Mac — il cloud non può fare l'OAuth); 2) export memoria SOI dal Mac
  in `soap-opera-italia/memoria-mac-soi/`; 3) decidere posizionamento vs STF
  (oggi il mix è Hercai/Paradiso — serie finite/deboli — e sovrappone STF su
  La Promessa/FF: un canale a 2 iscritti vive solo di ricerca).

## 🏆 LE TRE SCOPERTE CHE GOVERNANO LA PRODUZIONE (20/8/2026, dai dati)

Valgono per **entrambi i canali** e superano le regole precedenti dove in conflitto.

### 1. FORMATO: 8–12 minuti densi (non più 20–25)
YouTube premia la **percentuale** vista, non i minuti assoluti: 12,5% su un video
da 20 min contro 29,4% su uno da 8–9. E i video con più viste sono tutti 8–10 min
(1.700 · 1.600 · 1.400). Stessa densità dello script lungo in metà tempo, zero
riempitivi. Target 10 min ≈ 10.100 caratteri (ritmo reale 16,9 char/s).
Dettaglio: `memoria-canale/FORMULA-8-12-MIN-densa.md`.

### 2. ANGOLO: evergreen, non anticipazioni con date
L'angolo decide le viste. Evergreen su serie **finita ma ancora cercata** = 1.600–2.030
viste; settimanale con date su serie in onda = 86–380. **Rapporto 20:1.**
Angoli validati (stesso ordine su STF e SOI): 1) CHI È [personaggio] · 2) CHE FINE
HA FATTO / cosa fa oggi · 3) scene censurate / quello che non avete visto ·
4) perché [evento] è successo davvero · 5) i 5 [villain/indizi] più…
Batch: **2 evergreen + 1 storyline** (storyline solo La Promessa, l'unica serie
viva che rende). Terra Amara ed Endless Love sono nella rotazione fissa.
Regola: **la risposta del titolo va data entro il primo minuto**, poi il "come".

### 3. CTA: «scrivete "voglio il seguito"» (non le teorie)
Letti i commenti reali: sui video con 137–181 commenti, 11 su 20 sono la stessa
frase — *"voglio il seguito"*. Sono risposte a una richiesta, non opinioni.
La CTA "scrivete la vostra teoria" ha prodotto **0 commenti su 11 video**.
Questo pubblico (87% over 55) commenta se il costo è zero e ottiene qualcosa.
**Obbligo**: commento fissato del canale a ogni uscita + rispondere nelle prime
24h + **se chiedono il seguito, il seguito va fatto davvero**.
Dettaglio: `memoria-canale/ANALISI-COMMENTI-perche-alcuni-video-esplodono.md`.

### Stato al 20/8: STF a 244.127 viste nel mese (×11,6 su luglio), 60.300 iscritti.
Blocchi ancora aperti da 6 check, tutti sul Mac e a costo zero: commenti fissati
mai pubblicati, diradamento coda non applicato, impression/CTR mai rilevate.

## Nota su questo repository

thefindsvault-site è un sito statico NON collegato al canale: fa da contenitore della
memoria su questo branch (`claude/analisi-grafico-storico-fvwaqt`). Non toccare i file
del sito per il lavoro canale. Non portare `memoria-canale/` su main (diventerebbe
pubblica sul sito).
