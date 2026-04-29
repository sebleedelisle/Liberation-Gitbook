---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Hullámoszcillátorok

## Ezen az oldalon:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Fűrészfog-hullám](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Háromszög-hullám](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Szinuszhullám](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Négyszöghullám](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Hullámoszcillátorok](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Egyéni oszcillátor](wave-oscillators.md#custom-oscillator-1)

## Wave oscillator beállításai

Minden Wave oszcillátor a következő beállításokkal rendelkezik:

* **range min / range max** - meghatározza annak a tulajdonságnak az értéktartományát, amelyet az oszcillátor vezérel. A tulajdonság értéke _range min_, amikor a hullámforma az alsó ponton van, és _range max_, amikor a hullámforma a felső ponton van.

{% hint style="info" %}
Például ha azt szeretnéd, hogy egy pont balra-jobbra mozogjon -100 és 100 között, kösd az oszcillátort az _x property socket_ csatlakozóhoz, állítsd a _min range_ értékét -100-ra, a _max range_ értékét pedig 100-ra.
{% endhint %}

* **duration** - az az időtartam, amíg egy teljes ciklus vagy _loop_ lefut. Ez a tempóhoz viszonyítva, ütemekben értendő. Tehát a ¼ egyetlen ütés. Az 1 egy teljes ütem, stb.
* **duration multiplier** - a kiválasztott szorzóval skálázza az alap időtartamot. Például ha a duration negyedhangra van állítva, a szorzó pedig 3, akkor az oszcillátor három negyedhangon át tart (pontozott félhang). Tört szorzók is használhatók — tartsd lenyomva a _SHIFT_ billentyűt a csúszka húzása közben, ha nem egész számokat szeretnél beállítani. Ez fáziseltolási effektekhez vagy finom időzítési eltolások létrehozásához hasznos.
* **offset** - a hullám kezdő eltolása a duration százalékában. Ha azt szeretnéd, hogy a hullám az út negyedénél induljon, állítsd 25%-ra.
* **repeat count** - megadja, hányszor fusson le a loop, mielőtt megáll. Az alapértelmezés _FOREVER_, de módosíthatod, ha nem szeretnéd, hogy az oszcillátor végtelen ideig fusson. Miután megáll, a tulajdonság a hullám végén lévő értékre áll.
* **delay count** - az oszcillátor indulása előtti késleltetés ütésekben. Amíg nem indul el, a tulajdonság a hullám elején lévő értékre áll.

{% hint style="info" %}
A _repeat count_ és a _delay count_ körültekintő használatával nagyon összetett animációkat hozhatsz létre — szinte olyan, mintha saját idővonalad lenne!
{% endhint %}

## Közös beállítások

* **steps** - a mozgást megadott számú diszkrét lépésre osztja. Akkor hasznos, ha azt szeretnéd, hogy a tulajdonságok sima mozgás helyett értékek között „ugorjanak”.

{% hint style="info" %}
Fontos, hogy a lépések idő szerint oszlanak el, nem érték szerint. Tehát ha egy hullámot 4 lépésre osztasz, és a duration 1 ütem, a tulajdonság minden ütésnél azonnal megváltozik.
{% endhint %}

* **clamp min / clamp max -** a hullám skáláját a minimális vagy maximális értékén túl növeli, majd levágja az eredményt.

{% hint style="info" %}
A _clamp_ fogalmát elég nehéz elmagyarázni, de képzeld el, hogy a hullámforma kifut a grafikon tetején vagy alján, majd a rendszer a szélekhez szorítja. Érdemes kísérletezni velük! Nagyon hasznosak például akkor, ha azt szeretnéd, hogy egy fűrészfog-hullám később induljon vagy korábban érjen véget.
{% endhint %}

* **ease function** - a Sawtooth és Triangle hullámoknál ease function is elérhető, amely finoman módosítja az animációs görbét, és sokkal kifejezőbbé teheti az animációkat.
  * **LINEAR** - az alapértelmezett beállítás, nincs easing; lineárisan mozog a min és max érték között.
  * **EASE OUT** - gyorsan indul, majd a vége felé lelassul. Nagyon jó fizikai hatások szimulálásához, például megállásig lassuló mozgáshoz.
  * **EASE IN** - lassan indul, majd fokozatosan gyorsul. Jól használható lendület felépülésének szimulálására.
  * **EASE IN/OUT** - a kettő kombinációja, nagyon természetes mozgást eredményez.

{% hint style="warning" %}
**Easing -** Ha teheted, kerüld az alapértelmezett lineáris animációt, kivéve, ha kifejezetten gépies hatást szeretnél. Az easing sokkal folyékonyabbá és természetesebbé teheti az animációkat.
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Fűrészfog-hullám

Néha _ramp waveform_ néven is ismert, mert a ciklus során felfelé fut, majd a végén hirtelen leesik. Valószínűleg ez a leggyakrabban használt hullámoszcillátor, mert jól használható olyan tulajdonságok ciklikus mozgatására, mint a _hue_ vagy a _rotation._

A fenti szakaszokban találod ezeket:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Sawtooth-specifikus beállítás:

* **cycle range compensation** - akkor érhető el, ha a **steps** be van állítva, és ciklikusan változó értékekhez hasznos, például 0 és 360 közötti forgatáshoz. Ha nincs bekapcsolva, a kezdő- és végérték azonos lesz, ami megtapadást okozhat a kezdőponton (mert a 0 és a 360 ugyanaz a szög). Kapcsold be, és a maximális tartomány csökkenni fog a lépéspozíciók korrekciójához.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Háromszög-hullám

A _sawtooth wave_ hullámmal ellentétben, amely minden ciklusban visszaugrik az elejére, a _triangle wave_ lineárisan előre, majd visszafelé mozog.

A fenti szakaszokban találod ezeket:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Szinuszhullám

A legsimább hullámforma. Finoman oszcillál két érték között, mint egy inga.

A fenti szakaszokban találod ezeket:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Négyszöghullám

A legegyszerűbb hullámforma: egyszerűen két érték között vált oda-vissza.

A fenti szakaszokban találod ezeket:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Square wave-specifikus beállítás:

* **pulse width** - az az időtartam, ameddig a hullám a teljes duration-höz képest a maximális értékén marad. Az alapértelmezett érték 50%, ami pontosan fele-fele arányt jelent. Ha azt szeretnéd, hogy csak az idő negyedében legyen „bekapcsolva”, állítsd 25%-ra. A pulzus időzítését az _offset_ értékkel módosíthatod.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Zaj

A Liberation egyik erőssége, hogy véletlenszerű, de megismételhető effekteket tud generálni. A _noise_ oszcillátorral organikus, loopolt véletlen mozgás hozható létre, tetszőleges részletességgel vagy remegéssel.

A fenti szakaszokban találod ezeket:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Noise-specifikus beállítás:

* **noise type** - a zaj generálásához használt algoritmus.
  * **SIMPLEX** - az alapértelmezett; hullámzó érték, amely finoman emelkedik és süllyed, majd loopként ismétlődik.
  * **RANDOM** - hagyományosabb véletlenszám-algoritmust használ, teljesen zajos és kaotikus.

{% hint style="info" %}
A **Simplex noise** algoritmust Ken Perlin tervezte 2001-ben a „Perlin noise” algoritmusának továbbfejlesztéseként, amelyet 1983-ban fejlesztett ki a _Tron_ filmen végzett munkája során (amiért Oscar-díjat kapott).

Ez az úgynevezett „gradient” zaj abból a frusztrációból született, hogy a korábbi számítógéppel generált képek túlságosan „gépszerűek” voltak. A CGI világában különösen jól használható felhők, vízfelszínek vagy akár valósághű terephez készült magasságtérképek renderelésére.

A Liberationben pedig látszólag kiszámíthatatlan, mégis sima és organikus mozgások létrehozására hasznos.
{% endhint %}

* **seed** - a zaj létrehozásához használt érték. Ha nem tetszik az aktuális zajhullám kinézete, próbáld meg módosítani ezt az értéket.

{% hint style="info" %}
Egy kis geek érdekesség: a tökéletesen loopoló simplex zajhoz egy 2D zajsíkban kör mentén iterálok. A seed érték módosítása pedig ezt a síkot mozgatja egy 3. dimenzión keresztül.
{% endhint %}

* **simplex detail** - azt módosítja, mennyire részletes vagy remegő a zaj. Ha azt szeretnéd, hogy az ismétlődő minta kevésbé legyen feltűnő, növeld a duration értékét, és emeld meg ezt az értéket.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Egyéni oszcillátor

Teljesen egyéni hullámformákat hoz létre. Nagyon hasznos összetett animációk készítéséhez.

A fenti szakaszokban találod ezeket:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Ez alatt pozíciók és értékek listája található. A duration 64 lépésre oszlik, és ezek bármelyik pontjára elhelyezhetsz egy értéket.

Minden lépés a következő beállításokkal rendelkezik:

* **Step** - az időlépés a duration időtartamán belül. A 0 az elejét, a 64 a végét jelenti.
* **Level** - a hullám szintje az adott időlépésnél. A szint 0 és 1 között lehet.
* **Animation type** - a legördülő menüben kiválaszthatod, hogyan mozogjon az előző lépéstől ehhez a szinthez.
  * **None** - nincs átmenet, az adott időpontban közvetlenül erre a szintre ugrik.
  * **Linear** - teljesen lineáris mozgás az előző szintről erre a szintre.
  * **Ease in / Ease out / Ease in/out** - easing átmenetet használ az előző szintről erre a szintre. Az animációtípusok leírását lásd fent, az _ease function_ résznél.

***
