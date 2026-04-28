---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Býr til áhrif í „laser harp“-stíl þar sem MIDI-nótur sem berast kveikja á geislum eða formum yfir ákveðið svið. Hnúturinn notar það efni sem þú sendir inn í hann sem _uppsprettu_ fyrir hverja nótu - sendu inn punkt og þú færð röð af punktum. Sendu inn form eins og hring og þú færð röð af hringjum; flóknari form eru afrituð á sama hátt.

Þú getur valið hvaða MIDI-tengi Liberation hlustar á í **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **midi channel** – hvaða MIDI-rás á að hlusta á (0 = allar rásir, 1–16 = tiltekin rás)
* **width** – heildarbreiddin sem nóturnar dreifast yfir.
* **midi note min / max** – lægsta og hæsta MIDI-nótugildi í sviðinu.
* **ignore out of range notes** – síar út allar nótur utan skilgreinda sviðsins. Ef þetta er óvirkt eru nótur utan sviðs „klemmdar“ að næstu tiltæku nótu (háar nótur kveikja efst í sviðinu, lágar nótur neðst).
* **auto extend range** – víkkar sviðið sjálfkrafa ef spilaðar eru nótur utan þess.

{% hint style="info" %}
Ertu ekki viss hvaða nótusvið þú ert að fá? Kveiktu á **auto extend range**, stilltu **midi note min** mjög hátt og **midi note max** mjög lágt og spilaðu svo nóturnar þínar. Kerfið grípur þær allar og stækkar sviðið fyrir þig. Þegar allt er komið inn slekkurðu einfaldlega á **auto extend range** til að læsa sviðinu.
{% endhint %}

* **leave all notes visible** – býr til geisla eða form fyrir allar nótur í sviðinu, hvort sem verið er að spila þær eða ekki, og gefur þannig „laser harp“-áhrif.
* **hit colour** – liturinn sem birtist þegar kveikt er á nótu.
* **hit colour hold time** – hversu lengi hit-liturinn helst í fullri birtu áður en hann dofnar. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._
* **hit colour decay time** – hversu lengi hit-liturinn er að dofna aftur eftir biðtímann. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._

{% hint style="info" %}
Ef efnið þitt er þegar alveg hvítt skiptir engu máli að stilla hit-liturinn á hvítt. Til að fá bestu útkomuna skaltu nota mettaðan lit fyrir efnið og stilla hit-liturinn á hvítt - þannig færðu mjög skemmtilegt blikkáhrif þegar kveikt er á nótum.
{% endhint %}

* **note off fade out time** – hversu lengi nótan er að dofna eftir að henni er sleppt. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._
* **hit scale factor** – hversu mikið nótan stækkar þegar kveikt er á henni (t.d. 2 = tvöföld stærð).
* **hit scale hold time** – hversu lengi nótan helst stækkuð áður en hún minnkar aftur. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._
* **hit scale decay time** – hversu lengi nótan er að fara aftur í upprunalega stærð. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._
* **note off shrink time** – hversu lengi nótan er að minnka aftur í upprunalega stærð eftir að henni hefur verið sleppt. Gildið er í sekúndum (0–1). _100% = 1 sekúnda._ (Hefur engin áhrif þegar **leave all notes visible** er virkt.)

{% hint style="info" %}
Stærðarkvörðun - Athugaðu að ef efnið þitt er einn punktur hefur stærðarkvörðun engin áhrif!
{% endhint %}
