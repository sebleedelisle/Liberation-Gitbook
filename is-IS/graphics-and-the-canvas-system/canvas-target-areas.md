---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas target areas

Við vitum hvernig við komum hlutum af Canvas inn á svæði innan hvers lasers, en til að setja efni inn á Canvas til að byrja með þarftu að nota _Canvas target areas_ — nafnið er svolítið ruglingslegt, en nákvæmt.

_Canvas target areas_ eru hlutar af Canvas sem þú getur teiknað clips inn á, og þau birtast í _CANVAS_ view sem bláir útlínurétthyrningar.

Oft þarftu kannski aðeins eitt Canvas target area og skiptir því síðan niður í mörg svæði sem eru send á mismunandi lasera.

Stundum gætirðu líka viljað nota mörg Canvas target areas fyrir mismunandi hluta byggingar, eða til að nýta zone delay á milli þeirra. (Já! Zone delay virkar áfram á milli Canvas target areas!).

### Senda clips á Canvas target areas

Ef þú skoðar clip deck, við hliðina á beam zone-hnöppunum, sérðu hnappana fyrir Canvas target areas. Þú gætir þurft að fletta output-hnöppunum til að sjá þá; notaðu `Shift + Left / Right Arrow`, eða ZONE PAGE-hnappana á skjánum, eða APC40-hnappana (sjá [apc40-reference.md](../reference/apc40-reference.md))

Úthlutaðu clips á Canvas target areas með því að kveikja eða slökkva á þessum hnöppum á nákvæmlega sama hátt og þú myndir gera með beam zone-hnöppunum.

### Bæta við / breyta Canvas target areas

Veldu _View -> Canvas Target Areas_ í efstu valmyndastikunni — þar sérðu allar stillingar fyrir hvert Canvas target area sem er í verkefninu þínu.

Efst er hnappurinn _ADD CANVAS TARGET AREA_.

Eyddu Canvas target area með rauða hnappinum með mínusmerki.

Stilltu stærð og staðsetningu með sleðunum. Tvísmelltu á sleða til að slá inn gildi.

### Scale mode

* **FIT TO AREA** - minnkar efni þannig að það passi alveg innan Canvas target area, án þess að breyta hlutföllum. (Þetta er sjálfgefna stillingin)
* **FILL AREA** - teygir efni þannig að það fylli Canvas target area, án þess að breyta hlutföllum. Efni gæti skorist af við jaðrana.
* **STRETCH TO FIT** - teygir efni þannig að það fylli allt Canvas target area og hunsar hlutföll.
