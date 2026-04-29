---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Calibrazione del colore

La calibrazione del colore assicura che i laser rosso, verde e blu del tuo proiettore emettano luce in modo fluido e prevedibile a tutti i livelli di luminosità. Proiettori diversi possono avere curve di luminosità non lineari: ad esempio, il rosso al 50% può apparire molto più luminoso o più debole della metà dell’intensità del rosso al 100%. La calibrazione corregge questo comportamento, così i colori si miscelano correttamente, i gradienti risultano fluidi e i bianchi sono bilanciati.

#### Riscaldare il proiettore

I diodi laser cambiano comportamento man mano che si riscaldano. Lascia sempre stabilizzare il proiettore prima della calibrazione:

* Proietta un frame luminoso, come il **White rectangle test pattern (11)**, per almeno **15–20 minuti**.
* In questo modo il bilanciamento del colore che imposti rimarrà stabile durante lo show.

#### Come funziona il test di calibrazione

Usa i pattern di test per la calibrazione (vedi [Pattern di test](../output-view/test-patterns.md))

* **5** – Rosso
* **6** – Verde
* **7** – Blu
* **8** – Bianco

Ciascuno di questi mostra quattro linee in movimento:

* **Linea superiore** – luminosità 100% alla massima velocità
* **Seconda linea** – luminosità 75% al 75% della velocità
* **Terza linea** – luminosità 50% al 50% della velocità
* **Quarta linea** – luminosità 25% al 25% della velocità

Poiché sia la luminosità _sia la velocità_ vengono scalate insieme, tutte le linee dovrebbero apparire con la stessa luminosità. Se una sembra più chiara o più scura, regola lo slider corrispondente finché coincidono.

Ogni pattern di test include anche una quinta linea a **0% di luminosità**, che non dovrebbe essere visibile. Serve a correggere i laser che non emettono luce ai livelli molto bassi. Se il laser rimane invisibile a bassa luminosità, aumenta gradualmente il **0% setting** finché la linea diventa appena visibile, poi riducilo leggermente finché scompare di nuovo. L’obiettivo è trovare la soglia in cui il laser inizia ad accendersi, poi restare appena sotto: così le dissolvenze partono in modo naturale senza tagliare la parte più bassa dell’intervallo.

#### Usare il pannello Colour Calibration

Il pannello ti offre controlli indipendenti per ogni canale (rosso, verde, blu) ai livelli 100, 75, 50, 25 e 0%.

1. **Seleziona un pattern di test** (inizia dal rosso).
2. **Regola gli slider** in modo che le linee 100, 75, 50 e 25% appaiano con la stessa luminosità.
3. **Ritocca lo slider 0%** se la linea “spenta” è ancora leggermente visibile.
4. **Ripeti per verde e blu.**
5. Passa al **White test pattern (8)**. Tutte e quattro le linee dovrebbero apparire uguali e il bianco dovrebbe risultare neutro (senza dominanti).

#### Regolare il bilanciamento del bianco

Puoi usare questo sistema anche per regolare il **bilanciamento del bianco**. Dopo aver calibrato singolarmente ogni canale, passa al **White test pattern (8)**. Se l’output appare con una dominante di colore (ad esempio troppo verde o troppo blu), regola i livelli relativi dei canali rosso, verde e blu finché le linee risultano di un bianco neutro. Anche se i tuoi laser hanno potenze molto diverse tra loro, la calibrazione ti aiuterà comunque ad avvicinarli e a ottenere una miscelazione dei colori più pulita e bilanciata.

#### Salvare la calibrazione

* Usa **Store** per sovrascrivere il preset corrente.
* Usa **Store As** per creare un nuovo preset (utile se lavori con più laser).
