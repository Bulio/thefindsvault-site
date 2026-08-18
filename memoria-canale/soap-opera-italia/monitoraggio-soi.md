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

## Log dei check

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
