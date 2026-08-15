# 🔓 AZIONI SBLOCCANTI — pronte da eseguire (cloud → Mac, 15/8/2026)

> I 3 blocchi aperti da 4 check sono il motivo per cui i video nuovo formato
> fanno 100–700 viste invece di migliaia. Qui sono trasformati in materiale
> pronto: **il Mac deve solo incollare/eseguire, non decidere nulla.**

---

## 1️⃣ COMMENTI FISSATI — testi pronti per gli 11 video nuovo formato

**Come si fa** (API YouTube, la pipeline ha già le credenziali): pubblicare il
commento come canale sul video, poi `setModerationStatus`/pin dal Studio.
**Regola permanente**: da ora ogni video nuovo formato esce CON il commento già
fissato — fa parte del rituale di lancio, non è un'operazione a parte.

**Formula** (da content-strategy-stf): domanda POLARIZZANTE a due lati netti +
posta in gioco dichiarata. Mai "cosa ne pensate". Risposta = frase libera.

| Video | Commento da fissare |
|---|---|
| `rb_DyZPzb8U` LP Leocadia smascherata | 📌 Secondo voi Leocadia pagherà davvero per quello che ha fatto, oppure se la caverà ancora una volta come ha sempre fatto? Scrivetelo qui sotto: se vince il "se la caverà", il prossimo video lo dedico alle sue prossime mosse. |
| `pwnUjTOE-D0` FA Nare si spara | 📌 Sadakat lo sapeva e non ha fatto niente. Per voi è una madre che ha sbagliato tutto, o una donna che ha protetto la famiglia nell'unico modo che conosceva? Due risposte, nessuna via di mezzo. |
| `wBXmUdkv7so` FF Chi è Zehra | 📌 Zehra: vittima diventata carnefice, o è sempre stata così e nessuno se n'era accorto? Ditemi la vostra — dal personaggio più votato parte il prossimo racconto. |
| `y1S_J8gUn9o` FA Sadakat ordina un omicidio | 📌 Fikriye ha salvato una vita ma ha tradito la famiglia Albora. Ha fatto bene o ha firmato la sua condanna? Scrivetelo, perché su questo la serie si spaccherà in due. |
| `r3z8_Zs3Cng` FF Feride trova la foto | 📌 Feride ha visto quella foto e ha già deciso tutto. Voi al posto suo parlereste subito con Cagatay, o restereste in silenzio ad aspettare? |
| `ihBWpAhHKq4` FA Il vero padre di Boran | 📌 Ecmel padre di Boran: la verità andava detta subito o era meglio il silenzio? Il commento più votato decide l'angolo del prossimo video. |
| `FOTb_qTankc` Endless Love | 📌 Kemal si fidanza con Asu senza amarla. Vendetta legittima o sta rovinando anche se stesso? Due lati, scegliete il vostro. |
| `JCLMPIkk3oU` Terra Amara villain | 📌 Il numero uno della classifica vi ha convinti o avreste messo un altro nome al primo posto? Ditemelo: la prossima classifica la costruisco sui vostri commenti. |
| `k_Usdt_aAvI` FF Feride sorprende Yildiz | 📌 Feride ha frainteso tutto — ma se foste al posto di Yildiz, andreste a spiegarvi o lascereste che pensi quello che vuole? |
| `eLgMjgdEHbg` FF Manette per Yildiz | 📌 Arrestata il giorno del suo matrimonio: per voi è una trappola di Sahika o Yildiz stavolta ha davvero esagerato? |
| `4TgmGtPa56E` FA Perché Zerrin ha sposato Demir | 📌 Zerrin si è sacrificata per Sahin. Gesto d'amore o l'errore più grande della sua vita? Nessuna risposta neutra, per favore. |

---

## 2️⃣ DIRADAMENTO — stato reale al 15/8 e cosa resta da fare

**Progresso**: da ~6 vecchio formato/giorno a ~3. **Non basta.**
**Obiettivo**: **massimo 1 vecchio formato al giorno, sempre alle 21:00.**
Gli slot 9:00 · 14:45 · 18:30 restano esclusivi del nuovo formato.

**Azioni concrete:**
1. **Verificare il cron delle 23:00**: se carica ancora 6 bozze/giorno, portarlo
   a **1/giorno** (o spegnerlo e programmare a mano). Finché resta a 6, la coda
   si riforma da sola e ogni diradamento manuale viene annullato il giorno dopo.
2. **Riprogrammare i vecchio formato in eccesso** secondo
   `diradamento-coda-vecchio-formato.md`: 1/giorno alle 21:00, ordine
   causa→effetto invariato, i "già in onda" slittano in coda alla lista.
3. ⚠️ **Durate intermedie**: il 14–15/8 sono usciti video da 11:37 e 12:12 —
   né vecchio (8-9 min) né nuovo formato (≥20 min). Decidere: o si portano
   sopra i 20 min, o restano nella quota "1 vecchio/giorno alle 21:00".
   **Non devono occupare gli slot del nuovo formato.**

---

## 3️⃣ IMPRESSION / CTR — scheda di rilevazione precompilata

Solo da **YouTube Studio → Analytics → tab "Copertura"** (non è nell'API
pubblica, quindi il cloud non può leggerlo). Per ciascun video: filtrare
"Dalla pubblicazione".

| Video | Impression | CTR % | % Browse | % Suggeriti | % Ricerca |
|---|---|---|---|---|---|
| `rb_DyZPzb8U` LP (729 viste) | | | | | |
| `pwnUjTOE-D0` FA (542) | | | | | |
| `wBXmUdkv7so` FF Zehra evergreen (390) | | | | | |
| `y1S_J8gUn9o` FA (150) | | | | | |
| `k_Usdt_aAvI` FF (90) | | | | | |

**Come si legge il risultato** (decide la prossima mossa, quindi va fatto):
- **Impression basse (<3.000) + CTR normale (4-8%)** → problema di
  DISTRIBUZIONE: YouTube non mostra il video → agire su diradamento, rituale
  di lancio, end-screen dai video più visti.
- **Impression alte + CTR <3%** → problema di THUMBNAIL/TITOLO → rifare le
  thumbnail (testo più grande, volto in primo piano, 3-5 parole).
- **% Ricerca alta sul video evergreen "CHI È ZEHRA"** → conferma che la linea
  evergreen intercetta la ricerca → raddoppiare su quel formato.

Compilare qui e committare: è l'ultimo dato mancante per il verdetto del 20/8.
