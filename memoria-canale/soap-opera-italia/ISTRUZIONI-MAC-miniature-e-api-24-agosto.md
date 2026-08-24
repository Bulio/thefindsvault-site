# 🔧 ISTRUZIONI SESSIONE MAC — miniature SOI + dati mancanti (24/8/2026)

> Scritte dalla sessione cloud, che NON ha disco, browser né credenziali.
> Qui il Mac deve solo eseguire: le decisioni sono già prese.

---

## 1️⃣ DIAGNOSI — quanti video SOI sono senza miniatura personalizzata

Verificato dall'utente in Studio il 24/8: il video `8QPs8UvILjc` (TERRA AMARA
"5 indizi tragedia Mujgan", uscito il 23/8) **non ha miniatura** — YouTube
mostra un fotogramma automatico. Il file non esiste sul disco: cercato con
`find` per nome e per cartella, nessun risultato.

**È il bug già noto**: upload OK, `thumbnails.set` fallisce per quota API
esaurita, il video resta pubblicato col frame. Identico ai video 87-94 di
Serie TV Fans (vedi `memoria-mac/checkpoint-master-stf.md`).

**Da fare per primo**: elencare TUTTI i video SOI privi di miniatura
personalizzata, non fermarsi agli ultimi due. Con le credenziali del canale
(`bulio91veo3@gmail.com`) basta `videos.list` sui video del canale e il
confronto con i file thumbnail effettivamente presenti nelle cartelle di batch.

## 2️⃣ FIX SISTEMICO — portare su SOI il retry di STF

Non risolvere a mano video per video: si riforma al prossimo batch.
Replicare per SOI il pattern che su STF ha funzionato:

- cron **`2 9 * * *`** (subito dopo il reset quota delle ~9:00 italiane)
- **un solo tentativo**, non un loop con sleep
- lo script si autorimuove dal crontab quando tutte le miniature sono a posto
- log dedicato

E soprattutto: **la pipeline SOI non deve considerare "completato" un upload
senza miniatura** — deve accodare il retry da sola, come fa STF.

## 3️⃣ LE MINIATURE MANCANTI VANNO CREATE, NON RECUPERATE

Non esistono da nessuna parte. Regola non negoziabile del canale:
**foto REALI dei personaggi, mai volti AI**, primo piano, 3-5 parole GRANDI
diverse dal titolo. Partire dalle librerie personaggi già sul disco
(che NON vanno mai cancellate) e applicare l'overlay `make_thumb_cinema.py`.

Per `8QPs8UvILjc` (Mujgan / Terra Amara): foto reale di Mujgan in primo piano,
testo suggerito **"NESSUNO SE N'ERA ACCORTO"**.
Per `N6Eq8tqlK00` (Fikret / Terra Amara): foto reale di Fikret,
testo suggerito **"TROPPO TARDI"**.

⚠️ Se sul Mac non esiste una libreria Terra Amara, dirlo esplicitamente al
prossimo handoff: significa che la produzione SOI gira altrove e la sessione
cloud sta ragionando su un'infrastruttura che non conosce.

## 4️⃣ DATI CHE SOLO IL MAC PUÒ PRENDERE (bloccati da 4 check)

Con le credenziali già sul disco, via **YouTube Analytics API**:
- `impressions` e `impressionClickThroughRate` per i video nuovo formato
  → è l'ultimo dato mancante, la scheda precompilata è in
  `azioni-sbloccanti-15-agosto.md`
- gli stessi dati per SOI (durata media, retention, traffic sources): con le
  API dirette **l'aggancio NexLev diventa opzionale**

## 5️⃣ ANGOLO TERRA AMARA SU SOI — correzione

| Uscita | Video | Viste |
|---|---|---|
| 23/8 | TA "5 indizi tragedia Mujgan" | 22 |
| 23/8 | TA "Fikret, vendetta abbandonata" | 17 |
| 20/8 | EL "Prima e dopo Neslihan e Burak" | 1.700 |
| 16/8 | EL "Scene censurate Kemal e Nihan" | 4.400 |

Stessa durata, stesso formato, rapporto 200:1. **Su SOI Terra Amara va scritto
come dietro le quinte** (attori oggi · scene tagliate · com'era il set · prima
e dopo), mai come settimanale di trama.

⚠️ Non è in contraddizione con la regola 3 di CLAUDE.md: su Serie TV Fans i
settimanali funzionano perché ci sono 60.400 iscritti che li ricevono nel feed.
**SOI a 58 iscritti non ha feed: vive solo di ricerca**, e la ricerca premia
l'evergreen. Il mix si introduce quando SOI avrà un pubblico suo.

⚠️ **Nota di metodo**: finché il bug delle miniature è aperto, le viste dei
video SOI non misurano né l'angolo né il formato — misurano l'assenza di
copertina. Rifare il confronto dopo il fix.

## 6️⃣ RESIDUI APERTI (non chiusi da settimane)

- **Memoria SOI mai esportata** in `soap-opera-italia/memoria-mac-soi/`: la
  sessione cloud non sa NULLA della pipeline SOI e misura al buio.
- **Commenti fissati mai pubblicati** (testi pronti in
  `azioni-sbloccanti-15-agosto.md`).
- **6 script del batch priorità del 20/8** mai prodotti.
