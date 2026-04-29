---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplikátory

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Vytvoří zrcadlenou kopii veškerého obsahu. Ve výchozím nastavení je osa zrcadlení svislá čára uprostřed.

* **angle** - úhel osy zrcadlení.
* **offset position** - posune osu zrcadlení (kolmo k ose)
* **delay** - časové zpoždění zrcadleného obsahu. Pozor, projeví se pouze tehdy, pokud obsah obsahuje nějaký druh animace.

#### Možnosti 3D (dostupné, když je vybráno 3D)

* **angle X / angle Y** - osa zrcadlení se změní na rovinu a pomocí těchto nastavení můžete rovinu otáčet ve 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Duplikuje obsah do kruhového vzoru.

* **radius** - vzdálenost od středového bodu, o kterou se obsah posune před otočením.
* **count** - počet kopií objektu, které se mají vytvořit.
* **use each objects pivot point** - když je tato volba vybraná, každý prvek se posune a otočí kolem vlastního středového bodu. (Má vliv pouze při duplikování více prvků)
* **delay** - přidá každému duplikovanému prvku postupně delší časové zpoždění. Aby byl efekt patrný, obsah musí obsahovat nějaký druh animace.
* **rotation** - dodatečné otočení přidané k prvkům.

#### Možnosti 3D (dostupné, když je vybráno 3D)

* **rotation x / rotation y** - otočí celý kruhový vzor kolem os x a y.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Duplikuje obsah do mřížky tvořené řádky a sloupci.

* **spacing** - vzdálenost mezi prvky
* **count X**- počet kopií vodorovně (sloupce)
* **count Y**- počet kopií svisle (řádky)
* **horizontal alignment** - počáteční bod sloupců, LEFT, CENTRE nebo RIGHT
* **vertical alignment** - počáteční bod řádků, TOP, MIDDLE nebo BOTTOM
* **delay** - přidá každému duplikovanému prvku postupně delší časové zpoždění. Aby byl efekt patrný, obsah musí obsahovat nějaký druh animace.
