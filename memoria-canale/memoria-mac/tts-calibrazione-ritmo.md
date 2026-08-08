---
name: chatterbox-real-pace-calibration
description: 'FIX 06/08: la cadenza vocale reale di Chatterbox (voce podcast/storytelling,
  parametri standard SKILL.md) è 16.87-17.37 caratteri/secondo, non i 17-19.2 usati
  finora nelle stime — uno script da 8110 caratteri è uscito a 7:47, sotto la soglia
  minima 8:00'
metadata:
  type: project
  originSessionId: current
  modified: 2026-08-06 11:00:32.805000+00:00
permalink: chatterbox-real-pace-calibration
---

Durante la produzione notturna del 06/08 (batch23), uno script di Serie TV Fans calcolato a 8110 caratteri con la stima "17 caratteri/secondo" ha prodotto un audio reale di **467 secondi (7:47)** — sotto la soglia minima di 8:00 imposta da [[storie_ispiranti_8min_regola_mai_violare]]-style rule (vedi `SKILL.md` "VINCOLO DURATA" per Serie TV Fans). Rate reale osservato: 8110/467 = **17.37 caratteri/secondo**. Un secondo script (video85) è uscito con rate ancora più lento: 8181/484.9 = **16.87 caratteri/secondo**.

**Causa**: le stime precedenti (17-19.2 char/s) erano probabilmente tarate su una voce/cadenza diversa o su un campione insufficiente. La voce "podcast/storytelling" attuale (exaggeration=0.45, cfg=0.25, temperature=0.7, pause_sentence=0.55, pause_paragraph=1.10 — standard SKILL.md) è più lenta.

**Fix applicato**: per garantire ≥8:00 con margine reale, calcolare gli script target a **≥8300-8500 caratteri** (non fermarsi appena la stima teorica supera 8:00 di poco) usando il rate PIÙ LENTO osservato (16.87 char/s) come base prudenziale, non una media ottimistica. Con margine, 8500 caratteri / 16.87 = 8:24, sicuro anche nel caso peggiore.

**How to apply**: quando si scrive un nuovo script Serie TV Fans (o qualunque pipeline che usi la stessa voce Chatterbox podcast), calcolare i caratteri della sola sezione narrata (non contare titoli/note produzione) e puntare a 8300+ caratteri prima di passare al TTS. Se un audio già generato risulta sotto 8:00 alla verifica ffprobe, NON procedere al montaggio: ampliare lo script con contenuto reale aggiuntivo (mai padding/ripetizione, vedi [[serietvfans_production_pipeline]]), rigenerare la narrazione pulita, e ri-dispatchare il TTS da zero (il vecchio audio va scartato, non recuperabile con overlay). Vale la pena verificare SEMPRE la durata reale con `ffprobe -show_entries format=duration` prima del montaggio, mai fidarsi solo della stima a caratteri.