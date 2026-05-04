---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas áttekintés

A Liberation Canvas rendszer viszonylag egyszerű, de elsőre zavaró lehet. Íme egy átfogó, koncepcionális áttekintés a kezdéshez.

{% hint style="info" %}
**Várj, szükségem van a canvas rendszerre?**

Lehet, hogy nem! Ha csak egyetlen grafikát vetítesz egyetlen lézerre, ezt könnyen megteheted egy beam zone segítségével is (bár alapértelmezés szerint a beam zone tartalma vízszintesen tükrözve jelenik meg, ezért a clipet X irányban tükröznöd kell).

Ha viszont grafikus tartalmat szeretnél több lézer között elosztani, vagy külön szakaszokra bontani építészeti mappinghez, akkor a canvas rendszer pontosan erre való.
{% endhint %}

### Canvas

Először is ott van maga a canvas. Ezt látod a _CANVAS_ nézetben: egy nagy „vásznat” jelképez, amelynek a területén bárhová rajzolhatsz tartalmat.

### Canvas célterületek

Ezek kék körvonalú téglalapokként jelennek meg a canvas nézetben, és olyan területek, amelyekre tartalmat küldhetsz. Egy clip tartalmát ugyanúgy küldöd egy canvas célterületre, ahogyan egy clipet egy beam zone-ra küldenél. A canvas célterületek gombjai a Clip Deckben, a beam zone gomboktól jobbra láthatók.

{% hint style="info" %}
Ha nem látod a canvas gombokat a Clip Deckben, próbáld meg görgetni a beam zone gombokat a `Shift + Left / Right Arrow` billentyűkombinációval. Minden canvas célterülethez látnod kell egy gombot _CANVAS 1, CANVAS 2_ stb. felirattal.
{% endhint %}

### Canvas zónák

A Canvas zónák a canvason belüli olyan területek, amelyeket egy lézerre szeretnél küldeni. A canvas nézetben rózsaszín körvonalú téglalapok jelölik őket. Minden zónára jobb gombbal kattintva kiválaszthatod, mely lézerekhez legyen hozzárendelve. Ha ezután átváltasz az adott lézer _OUTPUT_ nézetére, látni fogod, hogy megjelent egy új zóna.

{% hint style="danger" %}
FIGYELMEZTETÉS – ha a lézer élesítve van, előfordulhat, hogy hirtelen tartalmat kezdesz vetíteni egy alapértelmezett canvas zónában. A canvas zónák hozzárendelése előtt érdemes hatástalanítani a lézert.
{% endhint %}

{% hint style="info" %}
Canvas zónát úgy is hozzárendelhetsz egy lézerhez, hogy az _OUTPUT_ nézetben az _add canvas zone_ gombra kattintasz. Lásd: [Zónák](../output-view/zones.md "mention").
{% endhint %}

### Segédképek

Hozzáadhatsz egy segédképet a canvashoz, és ezt sablonként használhatod a grafikáidhoz. Érdemes módosítani a segédkép színárnyalatát (jobb gombos menü), és sötétíteni rajta, hogy a rákerülő tartalom könnyebben látható legyen.

{% hint style="info" %}
Építészeti mappingnél hasznosnak találtam egy „kiterített” épületnézet elkészítését, amely az épület összes felületét sík, torzításmentes képként ábrázolja. A különböző szakaszok perspektívakorrekcióját ezután az _OUTPUT_ nézetben, a canvas zóna segítségével lehet elvégezni.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Egy „kilapított” segédkép a brit Gatesheadben található Saltwell Hallhoz</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>A canvas zónák a Liberation egy korai verziójában (c2017!) Figyeld meg, hogy a rózsaszín téglalapok választják ki, a canvas melyik része jelenjen meg, az alul látható output nézetek pedig azt mutatják, hogy az egyes lézereken belül hová kerülnek ezek a zónák.</p></figcaption></figure>

### Canvas a 3D visualiserben

Elég körülményes lenne – finoman szólva – újra felépíteni egy bonyolult, több lézerből álló vetítési rendszert a 3D visualiserben. Ehelyett lehetőséged van elhelyezni a canvast a 3D térben. Kapcsold be a _Show canvas_ jelölőnégyzetet a _3D visualiser settings_ panelen. (A canvason lévő segédképek is megjelennek a visualiserben.)

{% hint style="info" %}
Fontos, hogy a visualiser továbbra is a lézerekből kiinduló atmoszférikus hatásként jeleníti meg a canvas vetítéseit. Egyszerűen kimozgathatod őket a nézetből, vagy – ha precízen szeretnéd – össze is igazíthatod őket a canvasszal.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Rendkívül elégedettséget adhat, amikor a lézer nyalábjait sikerül összeigazítani a canvas képével a 3D visualiserben.</p></figcaption></figure>
