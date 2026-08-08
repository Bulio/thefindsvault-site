---
name: preferenza-corsia-colab-vs-coda
description: 'DIRETTIVA 31/07 (estesa): quando la coda CPU locale è occupata, usare
  Colab E Kaggle in parallelo tra loro e con la coda, senza chiedere conferma, preferendo
  quella più veloce/disponibile in quel momento — MA solo sopra una soglia minima
  di durata (vedi sezione soglia)'
metadata:
  node_type: memory
  type: feedback
  originSessionId: 22e7ab1f-8ed5-4336-a607-6af1f42c02e0
  modified: 2026-07-31 18:28:53.201000+00:00
permalink: preferenza-corsia-colab-vs-coda
---

Quando un job TTS pesante (o altro lavoro spostabile su GPU) troverebbe la coda CPU locale ([[coda_cpu_jobs_pesanti]]) occupata da altri progetti per un tempo lungo, **scegliere sempre di attivare/usare una corsia GPU gratuita — Colab ([[colab_tts_gpu_lane]]) o Kaggle ([[kaggle_tts_gpu_lane]]) — invece di aspettare in coda, senza chiedere conferma all'utente**.

**Why**: la notte del 31/07, con la coda locale occupata per potenzialmente ore da un batch di un altro progetto, ho chiesto all'utente se aspettare o attivare Colab — ha risposto "attiva Colab" e poi ha aggiunto esplicitamente "scegli sempre questa soluzione senza chiedermelo". Il 31/07 pomeriggio, con Colab che dava "limiti di utilizzo GPU esauriti", è stata costruita una seconda corsia equivalente su Kaggle; l'utente ha poi chiesto esplicitamente di dare il comando a **tutte le chat/sessioni** di usare entrambe le corsie in parallelo tra loro (non solo come fallback l'una dell'altra) e con la coda CPU locale, scegliendo quella più veloce disponibile in quel momento, **mantenendo sempre la qualità** (mai tagliare angoli su voce/parametri per guadagnare velocità).

**How to apply**: la prossima volta che la coda locale è occupata (controllare `cat ~/Desktop/Claude/.coda_cpu.lock/name` e se il job che la occupa non è il mio):
1. Controllare quale tra Colab e Kaggle è disponibile/più veloce in quel momento (es. Colab può dare "limiti GPU esauriti" a orari di punta — in tal caso passare direttamente a Kaggle senza insistere).
2. Se entrambe le corsie GPU sono libere e ci sono più testi da generare, usarle **in parallelo tra loro** (un batch su Colab, un altro su Kaggle) oltre che in parallelo con la coda CPU locale — tre corsie indipendenti possono lavorare contemporaneamente su progetti diversi.
3. Solo se nessuna delle due GPU è disponibile/praticabile (sessioni scadute e non riattivabili in tempi ragionevoli, errori bloccanti su entrambe) tornare ad aspettare in coda CPU o informare l'utente.

Vedi [[colab_tts_gpu_lane]] e [[kaggle_tts_gpu_lane]] per le procedure operative dettagliate (setup, gotcha, comandi esatti) di ciascuna corsia.

## Soglia minima di durata (aggiunta 31/07 sera, dopo analisi produttività 3 giorni)

**Attivare una corsia GPU extra (Colab/Kaggle) SOLO se il testo da narrare supera ~5-6 minuti stimati di audio.** Sotto quella soglia, restare in coda CPU locale (o aspettare) invece di aprire/configurare una corsia GPU.

**Why**: il pomeriggio del 31/07 un intero pomeriggio è stato speso a inseguire corsie GPU parallele (Colab multi-account, poi Kaggle) per due narrazioni News e Pettegolezzi da 3-4 minuti ciascuna (`gfvip-agg-batch2`, `isola2026-batch2`) — il tempo di setup/troubleshooting (notebook condivisi, bug torch, iframe Kaggle inaffidabile) ha superato di gran lunga il tempo che si sarebbe risparmiato, con risultato netto nullo per quel batch specifico. Il confronto con gli altri due giorni (29-31/07) ha mostrato che le corsie GPU pagano solo su batch lunghi (es. narrazioni PokerLab 8-10 min, batch multipli Storie Ispiranti da 1400-2000 parole), non su testi brevi.

**How to apply**: prima di aprire Colab/Kaggle per un job TTS, stimare la durata audio attesa (circa 19-20 caratteri/secondo per Chatterbox). Se stimata < 5-6 minuti → coda CPU locale via `run_in_coda.sh`, non aprire corsie GPU. Se >= 5-6 minuti E la coda CPU è occupata → seguire il protocollo sopra (Colab/Kaggle in parallelo). Vedi anche [[video_production_lanes_orchestration]] per il protocollo completo di smistamento tra le 5 corsie.