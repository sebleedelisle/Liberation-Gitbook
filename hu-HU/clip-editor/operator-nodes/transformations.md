---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transzformációk

## &#x20;Translate

Az összes tartalmat elmozdítja az x, y és/vagy z tengely mentén. Fontos, hogy a koordináta-rendszer középpontja az origó, és az x, illetve y tengelyen +/-200-ig terjed. Lásd: [Koordináta-rendszer](../fundamentals/co-ordinate-system.md "mention").

* **x** - az x tengely mentén történő elmozdítás távolsága (balra - jobbra).
* **y** - az y tengely mentén történő elmozdítás távolsága (felül - alul).

#### 3D beállítások (akkor érhetők el, ha a 3D ki van választva)

* **z** - a z tengely mentén történő elmozdítás távolsága (hátra és előre, a képernyő mélysége felé).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Elforgatja az összes tartalmat. Az értékek fokban vannak megadva. Lásd: [Koordináta-rendszer](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - megadja fokban, hogy a tartalom mennyivel forduljon el az óramutató járásával megegyező irányban. Minden az origó (0,0), vagyis a középpont körül fordul el.
* **pivot point x / pivot point y** - ezekkel az értékekkel eltolható a forgatás origója.

#### 3D beállítások (akkor érhetők el, ha a 3D ki van választva)

* **rotation x** - forgatás az x tengely körül (pitch).
* **rotation y** - forgatás az y tengely körül (yaw).
* **pivot point z** - a forgatás eltolási pozíciója a z tengelyen.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Átméretezi az összes tartalmat.

* **scale** - a méretezés százalékos értéke.
* **scale x / scale y** - ezeket a beállításokat használd, ha vízszintesen és/vagy függőlegesen szeretnél méretezni.

{% hint style="warning" %}
Ha valami bármelyik tengelyen 0%-ra van méretezve, eltűnik!
{% endhint %}
