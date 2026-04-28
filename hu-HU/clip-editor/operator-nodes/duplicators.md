---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Az összes tartalom tükrözött másolatát hozza létre. Alapértelmezés szerint a tükörtengely egy függőleges vonal középen.

* **angle** - a tükörtengely vonalának szöge.
* **offset position** - eltolja a tükörtengelyt (a tengelyre merőlegesen mozgatja)
* **delay** - a tükrözött tartalom időkésleltetése. Ez csak akkor lesz hatással, ha a tartalom valamilyen animációt tartalmaz.

#### 3D beállítások (akkor érhetők el, ha a 3D ki van választva)

* **angle X / angle Y** - a tükörtengely síkká alakul, és ezekkel a beállításokkal 3D-ben forgathatod a síkot.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Körkörös mintában duplikálja a tartalmat.

* **radius** - az a távolság a középponttól, amennyivel a tartalom eltolódik a forgatás előtt.
* **count** - az objektum létrehozandó másolatainak száma.
* **use each objects pivot point** - ha be van kapcsolva, minden elem a saját középpontja körül lesz eltolva és elforgatva. (Csak akkor van hatása, ha több elem duplikálása történik)
* **delay** - fokozatosan növekvő időkésleltetést ad minden duplikált elemhez. A látható hatáshoz a tartalomnak valamilyen animációt kell tartalmaznia.
* **rotation** - az elemekhez hozzáadott elforgatási eltolás.

#### 3D beállítások (akkor érhetők el, ha a 3D ki van választva)

* **rotation x / rotation y** - a teljes körkörös mintát az x és y tengely körül forgatja.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Sorokból és oszlopokból álló rácsmintában duplikálja a tartalmat.

* **spacing** - az elemek közötti távolság
* **count X**- a vízszintes másolatok száma (oszlopok)
* **count Y**- a függőleges másolatok száma (sorok)
* **horizontal alignment** - az oszlopok kezdőpontja: LEFT, CENTRE vagy RIGHT
* **vertical alignment** - a sorok kezdőpontja: TOP, MIDDLE vagy BOTTOM
* **delay** - fokozatosan növekvő időkésleltetést ad minden duplikált elemhez. A látható hatáshoz a tartalomnak valamilyen animációt kell tartalmaznia.
