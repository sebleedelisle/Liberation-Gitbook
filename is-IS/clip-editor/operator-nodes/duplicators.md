---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Býr til speglað afrit af öllu efninu. Sjálfgefið er speglunarásinn lóðrétt lína í miðjunni.

* **angle** - horn speglunarásarinnar.
* **offset position** - hliðrar speglunarásnum til (færir hann hornrétt á ásinn).
* **delay** - tímaseinkun speglaða efnisins. Athugaðu að þetta hefur aðeins áhrif ef efnið er með einhvers konar hreyfingu.

#### 3D valkostir (í boði þegar 3D er valið)

* **angle X / angle Y** - speglunarásinn verður að fleti og þú getur notað þessar stillingar til að snúa fletinum í 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Afritar efni í hringlaga mynstri.

* **radius** - fjarlægðin frá miðpunktinum sem efnið er hliðrað um áður en því er snúið.
* **count** - fjöldi afrita sem á að búa til af hlutnum.
* **use each objects pivot point** - þegar þetta er valið er hverju elementi hliðrað og það snúið um eigin miðpunkt. (Hefur aðeins áhrif þegar verið er að afrita fleiri en eitt element)
* **delay** - bætir við sífellt lengri tímaseinkun fyrir hvert afritað element. Athugaðu að efnið þarf að vera með einhvers konar hreyfingu til að þetta hafi sjáanleg áhrif.
* **rotation** - viðbótarsnúningur sem bætist við elementin.

#### 3D valkostir (í boði þegar 3D er valið)

* **rotation x / rotation y** - snýr öllu hringlaga mynstrinu um x- og y-ásana.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Afritar efni í rúðumynstri með röðum og dálkum.

* **spacing** - fjarlægðin milli elementa.
* **count X**- fjöldi afrita lárétt (dálkar).
* **count Y**- fjöldi afrita lóðrétt (raðir).
* **horizontal alignment** - upphafspunktur dálkanna, LEFT, CENTRE eða RIGHT.
* **vertical alignment** - upphafspunktur raðanna, TOP, MIDDLE eða BOTTOM.
* **delay** - bætir við sífellt lengri tímaseinkun fyrir hvert afritað element. Athugaðu að efnið þarf að vera með einhvers konar hreyfingu til að þetta hafi sjáanleg áhrif.
