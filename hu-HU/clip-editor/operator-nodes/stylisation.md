---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stylisation node-ok

## &#x20;Randomise

Szórt másolatokat hoz létre a bejövő elemekből egy koherens zajmező alapján. Más szóval szabályozott, „zajos” módon másolja és mozgatja az alakzatokat és pontokat. Ahelyett, hogy minden szépen egy helyen maradna, több változat jön létre, amelyek eltolódnak és szétterülnek, mint egy áramlásban mozgó részecskék.

* **count** – a másolatok száma bejövő elemenként (1–20). 1 esetén minden elemből egyetlen, enyhén elmozdított változat jön létre. Nagyobb értékek több szórt másolatot hoznak létre.
* **noise offset** – végiglépteti a zajmezőt (0–100%). Zökkenőmentesen ismétlődik, ezért Oscillator Node-dal animálva az összes másolat együtt, folyamatosan és simán mozog.
* **noise jitter** – a zaj textúraméretét szabályozza. Alacsonyabb értékek széles, sima eltérést adnak. Magasabb értékek sűrűbb, kiszámíthatatlanabb elhelyezést eredményeznek. Ez a mintázatot módosítja, nem az erősséget.
* **change between points** – azt szabályozza, mennyire különbözzön az egyes másolatok pozíciója az előzőtől. Alacsony értékeknél a másolatok csoportosak és hasonlók maradnak. Magas értékeknél nagyobb eltéréssel szétterülnek.
* **face direction** – minden másolatot úgy forgat el, hogy a zajmezőben való haladás irányába nézzen, így az áramlással egy irányba álló nyilak/részecskék jönnek létre.
* **amount** – az effekt teljes erőssége (0–100%). A displacement és a Face direction által létrehozott forgatás mértékét is skálázza.

{% hint style="info" %}
A randomise node a Randomise effekt alapja!
{% endhint %}

## &#x20;Trails

Visszhangokat hoz létre a tartalomból: az eredeti mögött elhalványuló vagy átméretezett másolatokat hagy, miközben az mozog.

* **change render profile for trail** – ha be van kapcsolva, minden trail másolat a kiválasztott **render profile** beállítást használja. _Lásd:_ [Render profile](../fundamentals/render-profile.md).
* **render profile** – az a profil, amelyet a trail másolatok használnak, ha a fenti kapcsoló be van kapcsolva. Gyakori használat, hogy a fő tartalom **DETAIL** módban van, a visszhangok pedig **FAST** módban renderelődnek. Így a fő alakzatok részletesek maradnak, a trail-ek renderelése pedig hatékonyabb.
* **delay** – a trail másolatok közti távolságot állítja be zenei időben, **1/64 hangjegyes lépésekben** mérve.\
  Tájékoztatásként:
  * 16 = 1/16 ütem (tizenhatod)
  * 32 = 1/8 ütem (nyolcad)
  * 64 = 1/4 ütem (negyed)
  * 128 = 1/2 ütem (fél)
  * 256 = 1 ütem
* **trail size** – hány trail másolat rajzolódjon ki az élő tartalom mögött.
* **freeze trails** – a folyamatosan áramló trail-eket rögzített pillanatképek sorozatává alakítja. Hasznos staccato jellegű, ütemhez szinkronizált trail effektekhez.
* **brightness start / brightness end** – a fényerőt a trail mentén alkalmazza a legfrissebb másolattól (**start**) a legrégebbi másolatig (**end**). Általában a **brightness start** 100%, a **brightness end** pedig 0%, így a visszhangok fokozatosan elhalványulnak.
* **scale start / scale end** – a méretezést a trail mentén alkalmazza a legfrissebb másolattól (start) a legrégebbi másolatig (end). Ha azt szeretné, hogy a trail-ek eltűnésig zsugorodjanak, állítsa a **scale start** értékét 100%-ra, a **scale end** értékét pedig 0%-ra.

## &#x20;Shimmer

Csillogó fényerőváltozást ad a tartalomhoz, az enyhe szikrázástól az intenzív stroboszkópos hatásig.

* **speed** – milyen gyorsan változik a shimmer az időben. Magasabb értékek gyorsabb villogást adnak; a 0 szünetelteti az effektet.
* **separation** – azt szabályozza, mennyire különbözzenek egymástól a szomszédos pontok/elemek.
  * 0: minden együtt shimmerel.
  * \>0: a közeli pontok fokozatosan eltérő fázist kapnak, így a shimmer az alakzaton belül változik.
  * <0: ugyanaz, mint fent, de a fázis előrehaladása ellentétes irányú.
* **threshold** – a pontok sima elhalványulás helyett a fényerejük alapján teljesen be- vagy kikapcsolnak. A fényesebb elemek gyakrabban világítanak, de vegye figyelembe, hogy a 100% fényerejű elemek mindig be vannak kapcsolva, a 0% fényerejű elemek pedig mindig ki vannak kapcsolva. Éles glitter vagy csillagfény jellegű effektekhez hasznos.

{% hint style="info" %}
A **threshold** bekapcsolása egy olyan remek rejtett funkció, amely igazán életre keltheti a részecskéket vagy a tartalmat. Elhalványulás helyett a pontok a fényerejük alapján gyorsan be- és kikapcsolnak. Mivel egy adott pillanatban kevesebb pont rajzolódik ki, az eredmény fényesebb kimenet és simább animáció.

Ne feledje azonban, hogy ha a tartalom már eleve 100% fényerejű, akkor ez nem fog változást okozni!
{% endhint %}

* **use whole shape** – egyetlen shimmer értéket alkalmaz egyenletesen a teljes alakzatra. Kikapcsolt állapotban a node felosztja az alakzatokat, így a különböző részek egymástól függetlenül csilloghatnak, szemcsés hatást keltve.

## &#x20;Particles

Ez egy kísérleti effekt, amely a tartalom alapján részecskéket hoz létre és animál. A bejövő pontalapú elemek emitter pozícióként működnek. Mivel a részecskepályák előre kiszámítottak, a bemeneti tartalom módosításakor szükség lehet frissítésre/újraszámításra a részecskék frissítéséhez (ehhez elég bármelyik beállítást módosítani).

**Általános**

* **keep original** – ha be van kapcsolva, az eredeti tartalom megmarad, és a részecskék arra kerülnek rá. Hasznos, ha azt szeretné, hogy az emitter pontok továbbra is láthatók legyenek.
* **number of particles** – hány részecske jöjjön létre egy kibocsátáskor. Magasabb értékek sűrűbb effekteket adnak, alacsonyabb értékek visszafogottabb eredményt.
* **emission period** – a loop azon tartománya (ütemben), amely alatt a részecskék kibocsátása történik. 100%-on egyenletesen oszlanak el a loopban; kisebb értékeknél összetorlódnak, így burst jellegű kibocsátás jön létre.
* **loop length** – a particle loop hossza, zenei ütemekben mérve.
* **loop count** – hányszor ismétlődjön a loop, mielőtt alaphelyzetbe áll. Ha az érték 1, a részecskék minden alkalommal pontosan ugyanazt a szimulációt követik, így teljesen megismételhető az eredmény. Magasabb értékek több változatosságot visznek be, mielőtt a ciklus újraindul.
* **delay** – a kibocsátás kezdőidejét tolja el adott számú 1/64 hangjeggyel, időzítési effektekhez.

**Mozgás**

* **speed** – milyen gyorsan távolodnak el a részecskék az emittertől.
* **speed variation** – véletlenszerűséget ad hozzá, hogy a részecskék ne mind azonos sebességgel mozogjanak. Természetesebb szóródást hoz létre.
* **direction** – beállítja az alapirányt, amerre a részecskék kilövődnek, **x, y, z angles** formájában megadva. Ezek a szögek 3D térben forgatják a kilövési vektort, így a részecskéket irányíthatja egyenesen felfelé, oldalra vagy bármilyen átlós irányba. **spread** beállítással kombinálva szélesebb kúpokat vagy kaotikusabb burstöket hozhat létre.

{% hint style="info" %}
**Euler angles**\
A Liberation **Euler angles** értékeket használ a 3D térbeli orientáció leírására. Ezek egyszerűen a három fő tengely körüli forgatások:

* **X** – előre/hátra billentés (mint amikor bólint)
* **Y** – balra/jobbra fordítás (mint amikor „nem”-et int a fejével)
* **Z** – görgetés az óramutató járásával megegyező/ellentétes irányba (mint amikor oldalra billenti a fejét)

E három érték módosításával a részecskéket bármilyen irányba állíthatja.
{% endhint %}

* **direction variation** – véletlenszerű szórást ad a megadott irány körül. Kúpok, permetek vagy robbanások létrehozásához hasznos.
* **drag** – idővel lelassítja a részecskéket. Magasabb értékeknél nehezebbnek és lomábbnak érződnek.
* **gravity** – lefelé húzza (pozitív) vagy felfelé nyomja (negatív) a részecskéket.
* **gravity variation** – részecskénként eltérő gravity értéket ad, így kaotikusabbá teszi a mozgást.

**Élettartam**

* **life duration** – mennyi ideig léteznek a részecskék (1/64 hangjegyes egységekben mérve). Rövidebb értékeknél a részecskék gyorsan eltűnnek, hosszabb értékeknél hosszabb ideig láthatók maradnak.
* **life variation** – véletlenszerűséget ad a részecskék élettartamához, hogy ne mind egyszerre tűnjenek el.
* **start delay / start delay variation** – késlelteti, hogy az egyes részecskék mikor váljanak láthatóvá (1/64 hangjegyes lépésekben). A részecske ez idő alatt már létrejött és mozog, de a fényereje 0, ezért láthatatlan marad, amíg a késleltetés le nem telik. Hasznos, ha késleltetett tűzijáték-szerű „sparkle” megjelenést szeretne.

**Szín és fényerő**

* **hue start** – a részecskék kezdeti színe.
* **hue variation** – véletlenszerűséget ad hozzá, hogy a részecskék ne mind ugyanazzal a színnel induljanak.
* **hue change** – a részecske élettartama során eltolja a hue értéket, színváltó trail-eket létrehozva.
* **brightness start / brightness end** – a fényerőt a részecske élettartama mentén alkalmazza. Általában érdemes a brightness start értékét magasra, a brightness end értékét alacsonyra állítani, hogy természetesen halványuljanak el.
* **brightness variation** – véletlenszerűsíti a kezdő fényerőt a dinamikusabb megjelenés érdekében.
* **saturation start / saturation end** – beállítja, mennyire élénk legyen a szín az elején és a végén.
* **saturation variation** – véletlenszerűsíti a saturation értéket, így változatosságot ad a részecskék között.

**Szimuláció**

* **time adjustment** – felgyorsítja vagy lelassítja a teljes részecskeszimulációt. Hasznos különböző tempókhoz való szinkronizáláshoz vagy a mozgás hangsúlyosabbá tételéhez.
