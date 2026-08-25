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

## 🔌 AGGANCIO NEXLEV — procedura definitiva (verificata 17/8)

**Perché non lo fa il cloud**: NexLev NON espone alcun tool di connessione via
MCP (`list_my_youtube_channels` è in sola lettura e rimanda a
dashboard.nexlev.io/analytics). L'aggancio richiede un **OAuth Google nel
browser**, impossibile da una sessione cloud senza browser né credenziali Google.
Lo fa l'utente o la sessione Mac. **Due minuti.**

**Passi (account del canale: `bulio91veo3@gmail.com`)**
1. ⚠️ **Aprire una finestra ANONIMA/in incognito** — è il punto dove si sbaglia:
   se il browser è già loggato con l'account Google principale (quello dei 10
   canali già collegati), Google seleziona quello e SOI non compare nella lista.
2. Andare su **https://dashboard.nexlev.io/analytics** e fare login su NexLev
   con **lo stesso account NexLev di sempre** (non uno nuovo: SOI deve stare
   accanto a Serie TV Fans, non in un account separato).
3. Cliccare **"Connect channel"** / "Connect YouTube".
4. Nel popup Google scegliere **`bulio91veo3@gmail.com`**; se non è in elenco,
   "Usa un altro account" e inserirlo.
5. Selezionare il canale **Soap Opera Italia — @soapoperaitaliaa** (attenzione:
   NON @SoapOperaItalia, che è il concorrente omonimo) e concedere i permessi
   di lettura YouTube Analytics.
6. Fatto: al successivo check il cloud lo rileva da solo.

**Verifica automatica**: la sessione cloud controlla a ogni check con
`list_my_youtube_channels`. Appena `UCjid0Q5NC0No3HRHIF2_tdg` compare, attiva
per SOI le stesse metriche di STF (durata media, retention, traffic source) e
aggiorna la tabella criteri di questo file.

**Se dopo il tentativo il canale non compare**, i due motivi tipici sono:
(a) il login Google è avvenuto con l'account sbagliato → rifare in incognito;
(b) SOI è un canale-brand e serve accedere come proprietario del brand account.

## Richieste alla sessione Mac (per completare il binario)

1. **Eseguire l'aggancio NexLev qui sopra** (browser + account bulio91veo3).
2. Esportare la memoria SOI (strategia, pipeline, che ruolo ha il canale) in
   `memoria-canale/soap-opera-italia/memoria-mac-soi/` — qui non c'è NULLA su
   SOI e senza contesto i check misurano al buio.
3. Decidere il posizionamento vs STF (punto 2 delle osservazioni) e il mix serie.

## 🔎 RILIEVO INTERMEDIO — LUN 24/8/2026 (confluito nel CHECK #4)

**Stato canale**: **58 iscritti** (erano 44 il 21/8) · 31 video nella tab Video.

### 🔴 SCOPERTA NUOVA: i video escono SENZA MINIATURA PERSONALIZZATA
Verificato dall'utente in Studio il 24/8 sul video `8QPs8UvILjc`: **nessuna
miniatura caricata**, YouTube mostra un fotogramma automatico. Il file della
thumbnail **non esiste sul Mac** (cercato con `find`: nessun risultato né per
nome file né per cartella).

È lo **stesso bug già visto su Serie TV Fans coi video 87-94**: l'upload riesce,
la chiamata `thumbnails.set` fallisce per quota API esaurita, il video resta
pubblicato con un frame. Su STF fu risolto con un cron alle **9:02** (subito
dopo il reset quota delle ~9:00 italiane) che riprova una volta sola e si
autorimuove — vedi `memoria-mac/checkpoint-master-stf.md`.

⚠️ **Da verificare**: se il problema riguarda TUTTI i video SOI o solo gli
ultimi. Se è sistemico, non si risolve a mano video per video: va portato su
SOI lo stesso cron di retry di STF.

**Conseguenza sulla lettura dei dati**: un video senza miniatura personalizzata
ha CTR depresso per costruzione. Finché il bug è aperto, **le viste dei video
SOI non misurano l'angolo né il formato** — misurano l'assenza di copertina.
Non trarre conclusioni sul contenuto da questi numeri.

### 🟠 ANGOLO: i Terra Amara settimanali non funzionano su SOI

| Uscita | Video | Durata | Viste |
|---|---|---|---|
| 23/8 | TA "5 indizi tragedia Mujgan" `8QPs8UvILjc` | 9:46 | **22** |
| 23/8 | TA "Fikret, vendetta abbandonata" `N6Eq8tqlK00` | 9:21 | **17** |
| 22/8 | TA "Zuleyha lascia Demir" `_GD745xzv-w` | 9:57 | 72 |
| 21/8 | TA "Dopo la tragedia di Mujgan" `OsF6H6VufLc` | 9:37 | 117 |
| 20/8 | EL "Prima e dopo Neslihan e Burak" `F-VWLhob_h0` | 9:08 | **1.700** |
| 16/8 | EL "Scene censurate Kemal e Nihan" `qNYc4F20QB0` | 9:47 | **4.400** |
| 16/8 | EL "Cosa provano davvero gli attori" `pjPy6kDuDPc` | 10:03 | **1.600** |

Stessa durata, stesso formato, **rapporto 200:1**. Non è il formato 8–12 min:
è l'angolo. I Terra Amara sono scritti come **settimanali di trama**; su SOI
funziona solo il **dietro le quinte** (scene censurate · attori oggi · prima e
dopo · cosa non avete visto).

⚠️ **Differenza da STF, non contraddizione**: su Serie TV Fans i settimanali
con le date sono tornati a funzionare (regola 3 di CLAUDE.md) perché lì c'è un
pubblico di 60.400 iscritti che li riceve nel feed. **SOI a 58 iscritti non ha
feed: vive solo di ricerca**, e la ricerca premia l'evergreen. La regola del mix
NON si applica a SOI finché il canale non ha un pubblico proprio.

**Decisione**: su SOI, Terra Amara va riscritto sull'angolo dietro-le-quinte
(attori oggi, scene tagliate, com'era davvero il set), non sulla trama della
settimana.

### 🔴 NEXLEV — 7° SOLLECITO
Verificato oggi con `list_my_youtube_channels`: **10 canali collegati, SOI non
c'è**. Procedura invariata qui sotto (finestra in incognito). Avviato con
l'utente il 24/8, esito da confermare al prossimo check.

---

## 🚨 CHECK #4 — MAR 25/8/2026 ~10:30 Italia

| Metrica | 11/8 | 18/8 | 21/8 | **25/8** |
|---|---|---|---|---|
| Iscritti | 2 | 25 | 44 | **64** |
| Viste totali | 4.196 | 14.654 | 20.003 | **26.750** |
| Video totali | 38 | 66 | 70 | **74** (31 lunghi + 21 Shorts in tab) |

Crescita sana e continua: **+20 iscritti e +6.747 viste in 4 giorni**. Ma il
motore è sempre più concentrato, e sotto la crescita ci sono tre problemi.

---

### 🔴 1. PROBLEMA GRAVE E CONFERMATO: rischio diffamazione sugli attori

Il video **`pjPy6kDuDPc` — "Neslihan e Burak: cosa provano DAVVERO gli attori"**
(1.600 viste, 16 commenti) sta producendo esattamente ciò che era stato
segnalato come rischio il 21/8. Commenti reali, letti oggi:

- *"non lo nego che mi sarebbe piaciuto che avessero continuato ad amarsi nella
  vita reale"*
- *"se c'è qualcosa… e se c'è, beati loro"*
- *"dopo 10 anni non si frequentano, non si parlano, evitano le interviste,
  rifiutano le manifestazioni pubbliche per non incontrarsi"*
- un commento lungo che specula apertamente su tradimenti coniugali

**Burak Özçivit e Neslihan Atagül sono due persone reali, entrambe sposate con
altre persone.** Un titolo che promette di rivelare "cosa provano davvero" tra
loro fa dedurre al pubblico una relazione che non esiste, e il pubblico lo sta
scrivendo nero su bianco sotto il video. Non è materiale verificabile: è
speculazione sulla vita privata di persone identificabili. **È il tipo di
contenuto che fa arrivare una segnalazione e mette a rischio l'intero canale.**

**Regola, già in CLAUDE.md, da applicare adesso**: su persone reali si parla di
**lavoro, censura, dichiarazioni pubbliche verificabili** — MAI di sentimenti
privati o rapporti coniugali.

**Azioni concrete:**
1. **Rititolare `pjPy6kDuDPc`** togliendo l'ambiguità sentimentale. Es.
   *"Neslihan e Burak: cosa hanno detto davvero su Kemal e Nihan"* — stessa
   curiosità, zero deduzioni sulla vita privata.
2. **Moderare i commenti** che affermano relazioni o tradimenti: non sono
   opinioni sulla serie, sono affermazioni su persone reali pubblicate sul
   nostro canale.
3. **Nessun altro video su questa linea.** Il gemello sano esiste già ed è il
   più forte: *"Prima e dopo — come sono cambiati"* (2.000 viste) parla di
   aspetto e carriera, cioè fatti pubblici. **Quello si replica, l'altro no.**

---

### 🟠 2. IL VERO PROBLEMA DI PRODUZIONE: l'80% dei video non serve a niente

Non è "Terra Amara vs Endless Love" come sembrava ieri. Classificando i 30
lunghi più recenti **per modello di titolo**, il taglio è netto:

**Modelli che FUNZIONANO** (6 video su 30 = 20% della produzione):
| Video | Modello | Viste |
|---|---|---|
| `qNYc4F20QB0` | scene censurate — la verità mai raccontata | **4.600** |
| `F-VWLhob_h0` | prima e dopo: come sono cambiati gli attori | **2.000** |
| `pjPy6kDuDPc` | cosa provano davvero gli attori ⚠️ da rititolare | 1.600 |
| `tF5nNxdq4gI` | il fatto frontale (Manuel scopre suo padre) | 1.300 |
| `KJHzbJtIQ4Y` | 5 scene che la censura non voleva farvi vedere | 983 |
| `X0UDMCNQYBs` | cosa resta oggi di X | 925 |

**Modelli che NON funzionano** (media viste per modello):
| Modello di titolo | Esempi | Media |
|---|---|---|
| "Prima e dopo — i rapporti nella famiglia" (senza attori) | 22 · 7 | **15** |
| "[Personaggio] — da X a Y" (ritratto) | 32 · 27 | **30** |
| "5 indizi che avevano già svelato…" | 33 · 33 · 70 | **45** |
| "Le teorie dei fan contro la realtà" | 33 · 64 | **49** |
| "Avevi previsto…? Mettiti alla prova" (quiz) | 12 · 54 · 114 · 27 | **52** |
| "Dopo X, cosa può succedere adesso" | 130 · 69 | **100** |

**I numeri complessivi**: 6 video fanno **11.400 viste**; gli altri 24 ne fanno
**2.300 in totale**. Mediana per video: **100 viste**. **Metà dei video sta
sotto le 100 viste.**

**Conclusione**: si producono 4-5 video attorno allo stesso evento, ma **solo
quello frontale vive**; i satelliti (quiz, indizi, teorie, "cosa succede
adesso") sono lavoro buttato — TTS, immagini, montaggio, upload per 30 viste.

**Decisione**: **eliminare i modelli satellite dalla produzione SOI.** Meglio
1 video forte al giorno che 4 di cui 3 morti. Il tempo liberato va sul filone
che funziona: **censura · attori (fatti pubblici) · cosa resta oggi · il fatto
frontale**.

⚠️ La correzione di ieri su Terra Amara resta valida ma va precisata: i Terra
Amara falliscono **perché sono quasi tutti satelliti** (quiz, 5 indizi,
ritratto, "cosa succede adesso"). L'unico frontale — "Zuleyha lascia Demir, la
tragica morte di Mujgan" — è anche il migliore del gruppo (111).

---

### 🟠 3. SHORTS NON ALLINEATI — e i lunghi vincenti non ne hanno nessuno

21 Shorts, **~11.700 viste** (44% del totale canale), da 122 a 1.200 l'uno:
tengono su i numeri meglio di gran parte dei lunghi. Ma:
- gli **8 Shorts più recenti sono di Forbidden Fruit** (Ender, Yildiz, Halit,
  Mert) — serie che sui lunghi non esiste;
- i Terra Amara ci sono ma più vecchi;
- **di Endless Love, il filone che fa il 60% delle viste lunghe, non esiste
  nemmeno uno Short.**

**Azione**: gli Shorts vanno agganciati al lungo del giorno, e la priorità è
Endless Love / censura. ⚠️ Decisione da coordinare con la **chat SHORT**
(regola delle due corsie).

---

### 🔴 4. NEXLEV — 8° RILIEVO
`list_my_youtube_channels` oggi: **10 canali collegati, SOI non c'è.** Il
tentativo avviato con l'utente il 24/8 non è stato completato.
**Novità utile**: verificato il 24/8 che da questa sessione le API di Google
sono raggiungibili (`oauth2.googleapis.com`, `youtube.googleapis.com`
rispondono). Con le credenziali del canale, **l'aggancio NexLev diventa
superfluo**: Analytics e persino impression/CTR arriverebbero via API. La via
scelta con l'utente è però che **le API le usi la sessione Mac**, che le
credenziali le ha già — vedi
`ISTRUZIONI-MAC-miniature-e-api-24-agosto.md`.

### 🔴 5. COMMENTO FISSATO — ancora assente
Nessun commento del canale tra i top di `pjPy6kDuDPc` (16 commenti). Il rituale
di lancio continua a non essere applicato su SOI.

### 🔴 6. MEMORIA SOI — `memoria-mac-soi/` ancora inesistente
Ottavo check consecutivo senza contesto sulla pipeline SOI.

---

## 🎯 CRITERI NUOVI — i vecchi sono superati (fissati il 25/8, verifica al 22/9)

I criteri di 4 settimane fa (fissati quando il canale aveva 2 iscritti) sono
stati raggiunti in dieci giorni. Nuova asticella, tarata sui dati di oggi:

| Criterio | Oggi (25/8) | **Target 22/9** |
|---|---|---|
| Iscritti | 64 | **250** |
| Viste totali | 26.750 | **60.000** |
| **Mediana viste/video** | **100** | **400** |
| Video sotto le 100 viste | **50%** | **max 20%** |
| Commenti per video | ~1 (16 sul migliore) | **8 di media** |
| Video con commento fissato | 0% | **100%** |
| Shorts allineati al lungo del giorno | 0% | **100%** |

**La mediana è il criterio che conta.** Le viste totali salgono anche con un
solo video fortunato; la mediana sale solo se si smette di produrre video morti.

---

## Log dei check

- **CHECK #3 — VEN 21/8 ~10:35 Italia (sessione cloud).**

  ### 🚀 IL CANALE È ESPLOSO

  | Metrica | 11/8 | 14/8 | 18/8 | **21/8** |
  |---|---|---|---|---|
  | Iscritti | 2 | 9 | 25 | **44** |
  | Viste totali | 4.196 | 11.998 | 14.654 | **20.003** |
  | Video | 38 | 54 | 66 | 70 |

  **+19 iscritti e +5.349 viste in 3 giorni.** Da 2 a 44 iscritti in dieci giorni.

  ### La causa è una sola: il filone Endless Love "dietro le quinte"

  | Video | 18/8 | **21/8** |
  |---|---|---|
  | "Le scene censurate tra Kemal e Nihan" | 1.200 | **3.100** |
  | "Neslihan e Burak — cosa provano davvero gli attori" | 304 | **1.100** |
  | "5 scene che la censura non voleva farvi vedere" | 313 | **736** |
  | "Cosa resta oggi di Kemal e Nihan" | 310 | **687** |
  | "Prima e dopo — come sono cambiati" (nuovo) | — | 495 |

  Nello stesso periodo Hercai e Paradiso: **3–10 viste**. Il filone vale ~6.200
  viste, tutto il resto quasi zero.
  ✅ **Raccomandazione #1 del check #2 (raddoppiare sul filone): APPLICATA**, ed
  è ciò che ha fatto esplodere il canale.

  ### 💬 COMMENTI: 31 su un solo video (su STF erano 0 su 11 video)

  E non sono commenti di cortesia: sono lunghi, appassionati, con risposte tra
  utenti. *"Kemal e Nihan forever"* · *"Sarebbe stato bello vedere le scene
  d'amore, ma la violenza quella sì l'abbiamo vista"* · *"più baci e abbracci e
  meno violenza"* · una spettatrice scrive dieci righe su cosa ha significato
  quella serie per lei. **Il tema "censura" fa discutere perché tocca un'opinione
  che tutti hanno già.**

  ### 🚨 ATTENZIONE — il filone sta scivolando sul gossip privato

  Diversi commenti parlano di **sentimenti veri tra i due attori**, di gelosia
  dei rispettivi coniugi, di Burak Özçivit "condizionato dalla moglie". Il video
  "cosa provano davvero gli attori" alimenta questa lettura.

  **È un rischio serio e va gestito ora, non dopo:**
  1. Sono **persone reali e sposate**: insinuare una relazione tra loro è
     diffamatorio, non verificabile, e può attirare segnalazioni.
  2. Su un canale che vive di fiducia, farsi la fama di "quelli che inventano"
     brucia il vantaggio costruito.
  3. **Regola da applicare subito**: parlare del *lavoro* degli attori, delle
     regole di censura, delle loro dichiarazioni pubbliche — MAI dei loro
     sentimenti privati o dei rapporti coniugali. Se il pubblico ci va per conto
     suo nei commenti va bene: è il canale che non deve alimentarlo.

  ### Stato delle raccomandazioni del check #2

  | Raccomandazione | Stato |
  |---|---|
  | Raddoppiare sul filone dietro le quinte | ✅ fatta, ed è il motore |
  | Allineare gli Shorts ai lunghi | ❔ da verificare (Shorts non aggiornati di recente) |
  | Commento fissato del canale | ❌ ancora assente (i 31 commenti sono spontanei) |
  | Durata verso 15–20 min | ➖ superata: la nuova formula è **8–12 min** e i video stanno a 9–10, quindi sono già a norma |

  ### Tabella criteri

  | Criterio | Baseline 11/8 | **21/8** | Target 4 sett. |
  |---|---|---|---|
  | Viste 48h/video | 0–14 | fino a 495 il primo giorno | ≥50 ✅ |
  | Iscritti | 2 | **44** | ≥30 ✅ **superato** |
  | Commenti/video | 0 | **31** sul migliore | ≥2 ✅ **superato** |
  | % lunghi sopra 100 viste | ~0% | ~30% | ≥25% ✅ |

  **Tutti e quattro i criteri a quattro settimane sono stati raggiunti in dieci
  giorni.** Servono criteri nuovi, più alti, dal prossimo check.

  ### Prossimi 3 soggetti consigliati (il filone regge, si continua)

  1. **"TERRA AMARA: le scene che in Italia non avete visto"** — angolo n.1 sulla
     serie già validata dagli Shorts del canale. Script pronto:
     `batch-priorita-20-agosto/SOI-2-terra-amara-censura.md`.
  2. **"ENDLESS LOVE: la scena più discussa e perché ha diviso il pubblico"** —
     resta sul tema che funziona senza toccare la vita privata.
  3. **"CHE FINE HANNO FATTO gli attori di Terra Amara"** — script pronto:
     `soap-opera-italia/script-SOI-1-terra-amara-attori-oggi.md` (11:37).

  ### Blocchi
  - **NexLev: ancora NON agganciato (5° rilievo)** — con 20.003 viste e 44
    iscritti ora servirebbe davvero: senza, non vediamo durata media, retention
    e soprattutto **da dove arriva questo traffico** (ricerca? suggeriti?).
  - **Memoria SOI dal Mac**: non pervenuta.
  - **Commento fissato**: mai pubblicato. Con 31 commenti spontanei, l'innesco
    esplicito moltiplicherebbe il risultato.


- **CHECK #2 — MAR 18/8 ~10:35 Italia (sessione cloud).**

  ### 🎯 SVOLTA: i video LUNGHI hanno iniziato a funzionare

  | Metrica | 11/8 | 14/8 | **18/8** |
  |---|---|---|---|
  | Iscritti | 2 | 9 | **25** |
  | Viste totali | 4.196 | 11.998 | **14.654** |
  | Video | 38 | 54 | 66 |

  - **+12 iscritti in 24h** (13 → 25): il ritmo più alto da quando esiste il canale.
  - ⚡ **La crescita ora viene dai LUNGHI, non più dagli Shorts**: dei +2.656
    viste dal 14/8, circa **2.180 arrivano da un solo filone: ENDLESS LOVE**.
    Gli Shorts sono praticamente fermi (~10.400 → ~10.900 viste totali).

  ### Il filone che ha sbloccato il canale: Endless Love "dietro le quinte"

  | Video | Viste |
  |---|---|
  | "Le scene censurate tra Kemal e Nihan — la verità mai raccontata" | **1.200** |
  | "5 scene che la censura turca non voleva farvi vedere" | 313 |
  | "Cosa resta oggi di Kemal e Nihan, e perché se ne parla ancora" | 310 |
  | "Neslihan e Burak — cosa provano davvero gli attori" | 304 |

  Nel frattempo Hercai e Paradiso, sugli stessi giorni, fanno **0–16 viste**.
  → **Rapporto 75:1 tra il filone giusto e quello sbagliato.**

  **Perché funziona** (ed è lo stesso meccanismo visto su STF con "CHI È ZEHRA"
  1.314 viste e Terra Amara 762): sono contenuti **evergreen su serie finite ma
  ancora molto cercate**, con angoli da *dietro le quinte* — censura, attori
  veri, "che fine ha fatto". Non anticipazioni, non finali di stagione.
  Su un canale senza pubblico, che vive solo di ricerca, è l'unica linea che
  porta traffico.

  ### Stato delle raccomandazioni del check #1

  | Raccomandazione | Stato |
  |---|---|
  | Spostare i lunghi dai finali Hercai/Paradiso ai temi che tirano | ✅ **applicata** (virata su Endless Love: è ciò che ha sbloccato il canale) |
  | Collegare gli Shorts ai lunghi sullo stesso soggetto | ❌ no: gli Shorts restano su Terra Amara/Forbidden Fruit mentre i lunghi sono su Endless Love |
  | Aumentare la durata dei lunghi oltre i 4–9 min | ❌ no: restano 9–10 min |

  ### Tabella criteri

  | Criterio | Baseline 11/8 | **18/8** | Target 4 sett. |
  |---|---|---|---|
  | Viste 48h/video (lunghi) | 0–14 | **5–1.200** (mediana ~300 sul filone giusto) | ≥50 ✅ superato sul filone Endless Love |
  | Iscritti | 2 | **25** | ≥30 — quasi raggiunto |
  | Commenti/video | 0 | 0 | ≥2 ❌ |
  | % lunghi sopra 100 viste | ~0% | ~20% (4 su 20) | ≥25% — vicino |

  ### Raccomandazioni per il prossimo giro

  1. **Raddoppiare sul filone "dietro le quinte" di serie finite molto cercate**:
     dopo Endless Love, i candidati naturali sono Terra Amara (già validata dagli
     Shorts di questo canale) e Brave and Beautiful/Daydreamer. Angoli che
     funzionano: scene censurate · gli attori nella vita vera · che fine ha fatto ·
     5 indizi che nessuno aveva notato.
  2. **Allineare gli Shorts ai lunghi**: se il lungo è su Endless Love, gli Short
     della stessa giornata devono essere su Endless Love e rimandare al lungo.
     Oggi sono su serie diverse: traffico sprecato.
  3. **Commento fissato con domanda polarizzante** su ogni lungo (stessa regola
     STF): con 1.200 viste e 0 commenti, è il primo innesco mancante.
  4. Portare i lunghi del filone forte verso i 15–20 min: chi cerca "scene
     censurate" resta, e il watch time è l'unico modo per far crescere un canale
     a 25 iscritti.

  ### Blocchi

  - **NexLev: ancora NON agganciato** (4° rilievo) — niente durata media,
    retention, traffic sources. Procedura in questo file (finestra incognito).
  - **Memoria SOI dal Mac: non pervenuta** (`memoria-mac-si/` inesistente).


- **CHECK #1-bis — DOM 17/8 ~01:55 Italia (check rapido su richiesta utente).**
  - Iscritti **9 → 13** · viste totali **11.998 → 13.154 (+1.156)** · video
    54 → 63. Crescita continua ma **rallentata** (+1.156 in 3 giorni contro
    +7.800 dei 3 precedenti).
  - NexLev: **ancora non agganciato** (3° rilievo) · memoria SOI dal Mac:
    **ancora non arrivata** (cartella `memoria-mac-si/` inesistente).
  - 💡 **Trasferire subito su SOI la scoperta di STF**: lì i video "CHI È
    [personaggio]" e "CHE FINE HA FATTO" fanno 5-10× i settimanali (Zehra 1.314,
    Terra Amara 762 su una serie finita). SOI ha già dimostrato lo stesso
    pattern con "il padre di Jana" (754 viste). **Su un canale a 13 iscritti,
    che vive solo di ricerca, l'evergreen è l'unica linea sensata.**

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
