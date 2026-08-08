---
name: decisione_switch_horacle_palmier_immagini
description: DECISIONE 05/08 - a esaurimento crediti Horacle, passare a Palmier Pro
  per generazione immagini/thumbnail
metadata:
  node_type: memory
  type: project
  originSessionId: 635ccac3-a279-4429-ada3-9b435507458e
  modified: 2026-08-07 01:05:30.231000+00:00
permalink: decisione-switch-horacle-palmier-immagini
---

**Decisione presa il 05/08/2026:** dopo il confronto reale (generazione test via MCP, stesso prompt, pipeline overlay `make_thumb_cinema.py` applicata a entrambe le fonti), l'utente ha deciso: **quando terminano i crediti Horacle attuali, passare a Palmier Pro per la generazione immagini/thumbnail**, invece di ricaricare Horacle.

**CONFERMA DEFINITIVA 07/08/2026 (rapporto costi/tempi consegnato e approvato):** switch UFFICIALE. Configurazione: **Palmier = corsia primaria per TUTTE le immagini** (thumbnail + scene, tutti i verticali); **ChatGPT Go (account gratis) = piano B** per sfori di volume; **Horacle non si rinnova; ChatGPT Plus (account a pagamento) si disdice** dopo il primo batch reale via Palmier andato liscio. Piano Palmier attuale: **GRATIS 250cr/mese** (al 07/08: 132 usati) — quando finisce, attivare **Pro $29** (~333 img/mese, copre il fabbisogno; Max $69 solo se si aggiungono video/audio generativi). Risparmio netto stimato ~€75-80/mese + ~6h ogni 10 batch + ~85-90% di token sessione in meno. Numeri A/B e ricetta produzione (file full-res in `<progetto>.palmier/media/gen-<ID>.jpg`, prompt SEMPRE con "no text no lettering") in [[palmier_pro_new_capabilities_audit]]. **Fedeltà volti VALIDATA 07/08 stessa notte** (test Catalina+Curro La Promessa: `import_media` foto libreria → `referenceMediaRefs` su nano-banana-pro + prompt "SAME EXACT FACE" → identità riconoscibile su entrambi, scena period-drama coerente, zero scritte). **Piano PRO $29 ATTIVATO dall'utente 07/08** — corsia UNICA immagini, consumi tracciati (vedi [[palmier_credit_monitoring]]). Confronto 4 modelli fatto (premium: GPT Image 2/Nano Banana Pro; eco: Nano Banana Lite sorprendentemente buono, Ideogram V4 Turbo il più debole; Seedream non testato). Strategia proposta 2 livelli: NBP per thumbnail, NB Lite per scene in volume — default formale ancora da confermare dall'utente. Resta prima della disdetta ChatGPT Plus: un batch reale completo senza intoppi.

**ESTENSIONE AL VIDEO 07/08 ~02:40 (direttiva utente "ho caricato Palmier, usa quello d'ora in avanti"):** dopo la ricarica/attivazione Pro, Palmier è corsia primaria anche per la **generazione VIDEO** (es. clip bacio Kling V3 per [[short_test_serietv_no_voce_project]]), non solo immagini. Horacle di fatto ritirato (16cr residui, insufficienti per qualsiasi video). Primo uso reale: 2 clip bacio kling-v3 5s 9:16 da start-frame per il batch2 shorts Serie TV Fans.

**Perché (dati reali che hanno guidato la decisione):**
- Spesa reale Horacle ricalcolata: ~€87/mese (2× Starter/settimana, non 1×/mese come stimato inizialmente), ~860 immagini/mese
- Palmier Max: $69/mese (~€64), ~800 immagini incluse — volume comparabile, costo inferiore
- Editing Palmier (remove_silence, captions, export) è **gratis a vita**, indipendente dai crediti generazione
- Test reale qualità: generazione via Ideogram V4 (dentro Palmier) confrontata con pipeline overlay esistente — risultato promosso

**Setup già pronto per quando serve il passaggio** (vedi [[github_cli_reddit_scout_setup]] per i dettagli tecnici):
- Palmier Pro installato in `/Applications/PalmierPro.app`, account già autenticato (giulianop991@gmail.com)
- MCP server locale collegato a Claude Code (`palmier-pro`, http://127.0.0.1:19789/mcp) — attivo solo quando l'app è aperta
- Pipeline overlay (`make_thumb_cinema.py`) verificata compatibile con output Palmier — nessuna modifica necessaria

**Azione da fare al momento dello switch:** sottoscrivere piano Palmier (Pro $29 o Max $69, valutare in base al volume reale del momento) e aggiornare [[servizi_a_pagamento_elenco]] spostando Horacle a "non rinnovato" e aggiungendo Palmier come abbonamento attivo.

**Nota tecnica aperta:** l'ambiente di generazione thumbnail non ha `cv2` installato — il controllo automatico anti-sovrapposizione volto in `make_thumb_cinema.py` va rieseguito in un ambiente con `cv2` prima di fidarsi ciecamente su produzione volume, per ora verificato solo a occhio.

**Comando di riferimento (generazione via MCP Palmier, testato e funzionante 05/08):**
Con l'app Palmier Pro aperta, il server MCP risponde su `http://127.0.0.1:19789/mcp` (serve prima un handshake `initialize` per ottenere un `MCP-Session-Id`, poi le chiamate `tools/call` lo passano come header). Esempio di generazione:
```bash
curl -s -X POST http://127.0.0.1:19789/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "MCP-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"generate_image","arguments":{"prompt":"Dramatic Turkish soap opera scene, cinematic lighting, two actors in emotional confrontation, warm golden hour tones, movie poster style, shallow depth of field, high detail faces","model":"ideogram-v4","aspectRatio":"landscape_16_9"}}}'
```
Poi `get_media`/`inspect_media` con l'`id` restituito per recuperare l'immagine (base64 in `result.content[0].data`, decodificabile con `base64.b64decode`). Overlay finale con `python3 make_thumb_cinema.py <bg> "<TESTO SOPRA>" "<TESTO SOTTO>" <out.jpg>`.