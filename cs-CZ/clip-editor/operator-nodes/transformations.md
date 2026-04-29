---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformations

## &#x20;Translate

Přesune veškerý obsah podél os x, y a/nebo z. Souřadnicový systém má střed uprostřed a na osách x a y sahá od -200 do +200. Viz [souřadnicový systém](../fundamentals/co-ordinate-system.md).

* **x** - vzdálenost posunu podél osy x (vlevo–vpravo).
* **y** - vzdálenost posunu podél osy y (nahoru–dolů).

#### Možnosti pro 3D (dostupné, když je vybráno 3D)

* **z** - vzdálenost posunu podél osy z (dozadu a dopředu ve směru do obrazovky).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Otočí veškerý obsah. Hodnoty jsou ve stupních. Viz [souřadnicový systém](../fundamentals/co-ordinate-system.md).

* **rotation** - velikost otočení obsahu po směru hodinových ručiček ve stupních. Vše se otáčí kolem počátku (0,0), tedy středu.
* **pivot point x / pivot point y** - těmito hodnotami posunete střed otáčení.

#### Možnosti pro 3D (dostupné, když je vybráno 3D)

* **rotation x** - otočení kolem osy x (pitch).
* **rotation y** - otočení kolem osy y (yaw).
* **pivot point z** - posun polohy středu otáčení na ose z.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Změní měřítko veškerého obsahu.

* **scale** - procento měřítka.
* **scale x / scale y** - pokud chcete měnit měřítko vodorovně a/nebo svisle, použijte tyto možnosti.

{% hint style="warning" %}
Kdykoli je něco na libovolné ose zmenšeno na 0 %, zmizí!
{% endhint %}
