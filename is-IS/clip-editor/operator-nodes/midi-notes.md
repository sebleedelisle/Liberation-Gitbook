---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Býr til áhrif eins og í „laser harp“, þar sem innkomandi MIDI-nótur kveikja á geislum eða formum yfir tiltekið svið. Þetta node notar efnið sem þú sendir inn sem uppruna fyrir hverja nótu: sendirðu inn punkt færðu röð af punktum. Sendirðu inn form eins og hring færðu röð af hringjum, og flóknari form eru endurtekin á sama hátt.

Þú getur valið hvaða MIDI-viðmót Liberation hlustar á í **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – hvaða MIDI-rás á að hlusta á (0 = allar rásir, 1–16 = tiltekin rás)
* **width** – heildarbreiddin sem nóturnar dreifast yfir.
* **MIDI note min / max** – lægsta og hæsta MIDI-nótugildi á sviðinu.
* **ignore out of range notes** – síar út allar nótur utan stillta sviðsins. Ef þetta er óvirkt eru nótur utan sviðs „klemmdar“ að næstu tiltæku nótu (háar nótur kveikja efst á sviðinu, lágar nótur neðst).
* **auto extend range** – víkkar sviðið sjálfkrafa ef spilaðar eru nótur utan þess.

{% hint style="info" %}
Ertu ekki viss um hvaða nótusvið þú færð inn? Kveiktu á **auto extend range**, stilltu **MIDI note min** mjög hátt og **MIDI note max** mjög lágt og spilaðu svo í gegnum nóturnar. Kerfið grípur þær allar og víkkar sviðið fyrir þig. Þegar allt er komið inn slekkurðu einfaldlega á **auto extend range** til að festa sviðið.
{% endhint %}

* **leave all notes visible** – býr til geisla eða form fyrir allar nótur á sviðinu, hvort sem þær eru í spilun eða ekki, sem gefur „laser harp“-áhrif.
* **hit colour** – liturinn sem birtist þegar nóta er virkjuð.
* **hit colour hold time** – hversu lengi hit colour helst í fullri birtu áður en hann dofnar. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._
* **hit colour decay time** – hversu langan tíma það tekur fyrir hit colour að dofna aftur eftir biðtímann. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._

{% hint style="info" %}
Ef efnið þitt er þegar alveg hvítt skiptir engu að stilla hit colour á hvítt. Bestur árangur fæst með því að nota mettaðan lit í efninu og stilla hit colour á hvítt; þannig færðu mjög fallegt leiftur þegar nótur eru virkjaðar.
{% endhint %}

* **note off fade out time** – hversu langan tíma það tekur fyrir nótuna að dofna eftir að henni er sleppt. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._
* **hit scale factor** – hversu mikið nótan stækkar þegar hún er virkjuð (t.d. 2 = tvöföld stærð).
* **hit scale hold time** – hversu lengi nótan helst stækkuð áður en hún minnkar aftur. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._
* **hit scale decay time** – hversu langan tíma það tekur fyrir nótuna að fara aftur í upprunalega stærð. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._
* **note off shrink time** – hversu langan tíma það tekur að minnka aftur í upprunalega stærð eftir að nótunni hefur verið sleppt. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._ (Hefur engin áhrif þegar **leave all notes visible** er virkt.)

{% hint style="info" %}
Stækkun og minnkun – athugaðu að ef efnið þitt er stakur punktur hefur scaling engin áhrif!
{% endhint %}
