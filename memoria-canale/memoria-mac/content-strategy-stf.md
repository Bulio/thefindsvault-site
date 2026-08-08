---
name: serietvfans-content-strategy
description: 'Serie TV Fans: composizione batch (A/B test Trends vs storico), trend
  Forbidden Fruit, regola evergreen, CTA engagement + membership. Consolidato da 5
  memorie separate (06/08/2026).'
metadata:
  node_type: memory
  type: project
  modified: 2026-08-06 16:19:31.602000+00:00
  originSessionId: be416c77-2cb2-4bbd-9485-cb2bbc77ddb2
permalink: serietvfans-content-strategy
---

## Composizione batch — DIRETTIVA ATTUALE 06/08/2026 (A/B test, sostituisce "FF+LP+alternante" del 04/08)

Con [[google_trends_pipeline]] (interesse ricerca Google IT, 06/08) confrontate 5 soap: Far Away 38.5 > Forbidden Fruit 30.0 > La Promessa 27.6 >> Il Paradiso 7.9 ≈ L'Erede 7.8. **Nuova composizione fissa**: 1 Far Away + 1 Forbidden Fruit + 1 La Promessa per batch, tutti fissi. Il Paradiso/L'Erede escono dalla rotazione fissa (restano producibili su eventi eccezionali).

**⚠️ Contraddice lo storico views reali** (sotto: Far Away era fuori top30, Forbidden Fruit era il top performer) — trattato come **A/B test 2 settimane/2 batch**, tracciare le view reali dei 3 show in questo periodo prima di considerarlo definitivo. Se Far Away non regge, tornare alla regola precedente.

**Storico regole precedenti** (superate): 31/07 "2 Forbidden Fruit + 1"; 04/08 "FF+LP fissi + slot alternante Far Away/Paradiso" (ultimo alternante usato: Far Away, batch22/video83).

Librerie personaggi pronte: `PERSONAGGI SERIE TV FANS/FAR AWAY/` e `/IL PARADISO DELLE SIGNORE/` (elenco completo nomi in git history del file). Terra Amara: fuori rotazione fissa, libreria pronta se serve extra.

## Trend Forbidden Fruit (dato storico 31/07/2026, alla base della composizione pre-06/08)

Via NexLev `get_my_top_videos`: i 2 migliori video di fine luglio erano entrambi Forbidden Fruit (2.655 e 1.528 views/28gg), nettamente sopra La Promessa (949) e Il Paradiso (209). Traffic source dominante RELATED_VIDEO+SUBSCRIBER (non search) — l'algoritmo lo spingeva attivamente. Far Away non compariva nella top 30 in quel periodo (poi ribaltato dai dati Trends di agosto, vedi sopra).

## Regola evergreen (permanente dal 30/07)

Video devono restare cliccabili a distanza di settimane/mesi:
1. **Niente date** in titolo/thumbnail/narrazione ("le prossime puntate" invece di date assolute). Le date restano solo nelle fonti competitor interne (SEO/script, non pubbliche).
2. **Hook di curiosità nel titolo**: quote diretta, gap di curiosità, conseguenza emotiva — mai riassunto piatto.
3. **Hook in thumbnail**: frase-gancio corta, non duplica il titolo.
4. Riferimenti temporali relativi nel corpo narrazione.

## CTA engagement boost (permanente dal 31/07)

Views alte ma 0-12 commenti → tecnica migliore trovata: **domanda polarizzante a due lati netti** (non "cosa ne pensate") — riduce l'attrito, sfrutta il bisogno di prendere posizione. **Vincolo preesistente rispettato**: NO gimmick "scrivi una parola" (bocciato in passato) — la domanda resta polarizzante ma la risposta è sempre una frase libera.
1. Domande di metà video e finali con due opzioni nettamente contrapposte.
2. Vera posta in gioco dichiarata ("decidiamo il prossimo video in base ai commenti").
3. Tono diretto/assertivo, non passivo.
4. Ripetere l'invito più volte (metà+chiusura), mai formula fissa identica.

## Membership CTA (permanente dal 06/08, dosaggio "andiamoci piano")

Canale ha attivato 2 livelli membership: Base 1,99€, Fan 3,99€ (link `.../join`). Nessun competitor reale nella nicchia usa la membership YouTube (verificato su 4 competitor) — trattato come test A/B a basso rischio, non un pattern collaudato da replicare.
1. **Link in descrizione: SEMPRE**, ogni contenuto (video lunghi+Shorts), in fondo, mai sovrascrivere.
2. **Menzione parlata nello script: 1 video su 3**, mai una terza sezione promozionale a sé, tono leggero. Tracciare quali video l'hanno già avuta per rispettare il ciclo.
3. Riga fissa descrizione: `Unisciti alla community: sottoscrivi l'abbonamento per l'accesso anticipato e a contenuti pubblicati solo qui → https://www.youtube.com/channel/UCwgtJLcJWxO5p_VAILE4sdA/join`.
4. **Retrofit fatto anche sul pubblicato** (direttiva 06/08): script idempotente `YOUTUBE_API/serietvfans/add_membership_cta.py`, stato di avanzamento in [[serietvfans_batch_1_2_3_agosto_stato]].

**How to apply**: se dopo qualche settimana gli abbonati membership restano a 0, riportarlo all'utente prima di insistere — i dati mostrerebbero inefficacia in questa nicchia "mordi e fuggi". Vedi [[serietvfans_production_pipeline]] per pipeline/tooling e [[serietvfans_batch_1_2_3_agosto_stato]] per stato di produzione.