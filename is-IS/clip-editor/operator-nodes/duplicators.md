---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Býr til speglað afrit af öllu efninu. Sjálfgefið er spegilásinn lóðrétt lína í miðjunni.

* **angle** - horn spegilássins.
* **offset position** - hliðrar spegilásnum (færir hann hornrétt á ásinn)
* **delay** - tímaseinkun speglaða efnisins. Athugaðu að þetta hefur aðeins áhrif ef efnið er með einhvers konar hreyfingu.

#### 3D-valkostir (í boði þegar 3D er valið)

* **angle X / angle Y** - spegilásinn verður að fleti og þú getur notað þessar stillingar til að snúa fletinum í 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Afritar efni í hringlaga mynstri.

* **radius** - fjarlægðin frá miðjupunktinum sem efninu er hliðrað áður en því er snúið.
* **count** - fjöldi afrita sem á að búa til af hlutnum.
* **use each objects pivot point** - þegar þetta er valið er hverju elementi hliðrað og því snúið um eigin miðjupunkt. (Hefur aðeins áhrif þegar verið er að afrita mörg element)
* **delay** - bætir við sífellt lengri tímaseinkun á hvert afritað element. Athugaðu að efnið þarf að vera með einhvers konar hreyfingu til að þetta hafi sýnileg áhrif.
* **rotation** - viðbótarsnúningur sem bætt er við elementin.

#### 3D-valkostir (í boði þegar 3D er valið)

* **rotation x / rotation y** - snýr öllu hringlaga mynstrinu um x- og y-ásana.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Afritar efni í reitamynstri með röðum og dálkum.

* **spacing** - fjarlægðin á milli elementanna
* **count X**- fjöldi afrita lárétt (dálkar)
* **count Y**- fjöldi afrita lóðrétt (raðir)
* **horizontal alignment** - upphafspunktur dálkanna, LEFT, CENTRE eða RIGHT
* **vertical alignment** - upphafspunktur raðanna, TOP, MIDDLE eða BOTTOM
* **delay** - bætir við sífellt lengri tímaseinkun á hvert afritað element. Athugaðu að efnið þarf að vera með einhvers konar hreyfingu til að þetta hafi sýnileg áhrif.
