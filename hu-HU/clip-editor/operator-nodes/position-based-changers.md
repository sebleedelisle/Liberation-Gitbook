---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Pozícióalapú módosítók

Ez a node-család a tartalmat a pozíció alapján módosítja. Alapértelmezés szerint a hatás vízszintes tengely mentén érvényesül (balról jobbra), de ezt a tengelyt tetszőleges szögbe elforgathatod. Mindegyik node tartalmaz egy _radial_ módot is, ahol a hatást az egyes pontok középponthoz viszonyított szöge vezérli.

* **Colour Changer by Position** – színátmenetet alkalmaz a választott tengely mentén vagy a radiális szög körül.\
  \&#xNAN;_Példa: hozz létre egy vonalon végigsöprő szivárvány színátmenetet, vagy használd a radial módot egy körön színkerékhatás készítéséhez._
* **Wave Shift by Position** – szinuszhullám-torzítást alkalmaz, és a tartalmat függőlegesen (vagy a választott tengelyre merőlegesen) tolja el.\
  \&#xNAN;_Példa: fodrozódjon egy vonal úgy, mint a víz, vagy radial módban pulzáljon kifelé egy kör a középpontból._
* **Noise Shift by Position** – simplex noise torzítást alkalmaz, és a tartalmat függőlegesen (vagy a választott tengelyre merőlegesen) tolja el.\
  \&#xNAN;_Példa: lásd a Wave Shift példát, de organikusabb és véletlenszerűbb karakterrel; ideális természetes változatosság hozzáadásához._

## &#x20;Színváltás pozíció alapján

Ez a node a pozíció alapján színváltozásokat alkalmaz a tartalmon. Alapértelmezés szerint a tengely vízszintes (0°), de elforgathatod, vagy radial módra válthatsz.

* **wavelength** – a ismétlődő színciklus méretét állítja be.
  * _Linear mode:_ 100%-nál egy teljes ciklus a tartalom teljes szélességét lefedi.
  * _Radial mode:_ 100%-nál egy teljes ciklus a teljes kört lefedi (360°). Az értékek a kör százalékai: pl. 50% = fél kör (180°).
* **offset** – a színciklus kezdőpontját tolja el a wavelength százalékában. Modulálhatod (pl. fűrészfog-oszcillátorral), hogy a színek folyamatosan körbefussanak.
* **repeat** – bekapcsolva a ciklus ismétlődik a tartalmon. Kikapcsolva a színátmenet csak egyszer kerül alkalmazásra: a kezdőpont előtti minden rész a kezdőszínt, a végpont utáni minden rész a végszínt kapja.
* **pingpong** – bekapcsolva minden ismétlés váltott irányú, tükrözött hatást hozva létre. Ha a _Repeat_ ki van kapcsolva, a színátmenet egyszer előre, majd visszafelé fut. _Megjegyzés: Pingpong módban a wavelength az előre- és visszafutást együtt fedi le._
* **linear angle** – elforgatja a hatás tengelyét. 0° = vízszintes.
* **radial** – radial módra vált, ahol a színek a középpontból mért szög alapján kerülnek alkalmazásra.
* **radial smooth loop** – automatikusan úgy állítja a wavelength értéket, hogy az egyenletesen osztható legyen a kör 100%-ával, így nem jelenik meg látható illesztés a ciklus körbefordulásánál.
* **legacy mode** – visszavált a régebbi kezdő/vég HSB csúszkákra. Hagyd kikapcsolva az újabb színátmenet-szerkesztő használatához.

**Colour Modes**

Ezek határozzák meg, hogy a színmódosítások mely részei kerülnek alkalmazásra a tartalomra. Lásd még: [Színbeállítások és HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – a hue változatlan marad.
  * _FIXED_ – a hue rögzített értékre áll.
  * _SHIFTED_ – a hue a megadott értékkel eltolódik (a különböző színű elemek továbbra is elkülönülnek, de együtt mozdulnak el a színkörön).
* **saturation mode**
  * _OFF_ – a saturation változatlan marad.
  * _FIXED_ – a saturation a megadott értékre áll.
* **brightness mode**
  * _OFF_ – a brightness változatlan marad.
  * _FIXED_ – a brightness a megadott értékre áll.
  * _MULTIPLY_ – a brightness a megadott értékkel skálázódik. Ez megőrzi a dinamikát (pl. a villogó elemek továbbra is villognak, de a korlátozott fényerőtartományon belül).

**Gradient editor**

Ugyanazt a színátmenet-szerkesztőt használja, mint a [Colour Changer](colour-changer.md "mention"), de a színátmenetet pozíció alapján képezi le a tartalomra.

* Kattints a színátmenetsávra egy színpont hozzáadásához.
* Bal kattintással jelölj ki egy pontot, majd húzd oldalra az áthelyezéséhez.
* Egy kijelölt pont eltávolításához húzd lefelé, el a sávtól, vagy nyomd meg a Delete/Backspace billentyűt. A színátmenetben mindig legalább két pont marad.
* Jobb kattintással szerkeszthetsz egy pontot a színválasztóval.
* A **Position**, **Hue**, **Saturation** és **Brightness** használatával pontosan szerkesztheted a kijelölt pontot.
* Az **interpolation** határozza meg, hogyan keverednek a színek a pontok között:
* **HSB** – a hue, saturation és brightness értékeket keveri. Ez a legjobb a színkörön körbefutó, sima szivárványszerű mozgáshoz.
* **RGB** – közvetlenül a vörös, zöld és kék értékeket keveri. Ez gyakran inkább képernyős vagy világítópultos színátmenet érzetét adja.
* **NONE** – keverés nélkül ugrik az egyik pontról a következőre.
* A **hue direction** HSB interpoláció esetén érhető el:
* **AUTO** – a legrövidebb útvonalat választja a hue színkörön.
* **FORWARDS** – mindig előrefelé halad a hue értékeken.
* **BACKWARDS** – mindig visszafelé halad a hue értékeken.
* **blend** – összekeveri a színváltozást az eredeti színekkel. 100%-nál a hatás teljesen lecseréli az eredeti színeket.

**Régi kezdő-/végértékek**

Ha a **legacy mode** be van kapcsolva, a színátmenet-szerkesztőt a régebbi vezérlők váltják fel:

* **start hue / end hue** – a tartomány elején és végén használt hue.
* **start saturation / end saturation** – saturation a tartomány elején és végén.
* **start brightness / end brightness** – brightness a tartomány elején és végén.

**1. példa: Csúszó szivárvány színátmenet**

Alapértelmezett beállításokból indulva:

1. Hagyd a node-ot **Linear** módban (0° angle = vízszintes).
2. Hagyd a **wavelength** értékét 100%-on (a teljes szélességet lefedi, és ez legyen az alapértelmezett).
3. Hagyd meg az alapértelmezett színátmenetet.
4. Kapcsold be a **repeat** beállítást.
5. Adj egy **Sawtooth Oscillator**-t az **offset** beállításhoz, amely 0%-ról 100%-ra fut.

***

**2. példa: Fekete–fehér–fekete színátmenet (Pingpong)**

Alapértelmezett beállításokból indulva:

1. Hagyd a node-ot **Linear** módban (0° angle = vízszintes).
2. Hagyd a **wavelength** értékét 100%-on (a teljes szélességet lefedi, és ez legyen az alapértelmezett).
3. Kapcsold ki a **repeat** beállítást.
4. Állítsd az első színátmenet-pontot feketére.
5. Állítsd az utolsó színátmenet-pontot fehérre.
6. Kapcsold ki a **hue mode** beállítást.
7. Állítsd a **saturation mode** beállítást FIXED értékre, ha szürkeárnyalatos eredményt szeretnél kényszeríteni.
8. Állítsd a **brightness mode** beállítást FIXED értékre.
9. Kapcsold be a **pingpong** beállítást.

_Eredmény: a színátmenet a szélesség mentén feketéről fehérre, majd vissza feketére halványul._\
Ha azt szeretnéd, hogy a tartalom megtartsa a hue és saturation értékét, kapcsold OFF állásba a Saturation mode beállítást. \\

***

**3. példa: Forgó szivárványkerék (Radial)**

1. Kapcsold be a **radial** módot.
2. Állítsd a **wavelength** értékét 100%-ra (teljes 360°-os söprés).
3. Kapcsold be a **repeat** beállítást.
4. Adj egy **Sawtooth Oscillator**-t az **offset** beállításhoz, amely 0%-ról 100%-ra fut.

_Eredmény: varratmentes színkerék, amely folyamatosan körbeforog a kör mentén._

## &#x20;Hullámeltolás pozíció alapján

Ez a node hullámtorzítást alkalmaz a tartalmon, és a pontokat a választott tengelyre merőlegesen (vagy radiálisan, a középpontból kifelé) tolja el.

* **Wavelength** – a hullámciklus hosszát állítja be.
  * _Linear mode:_ 100%-nál egy teljes ciklus a tartalom teljes szélességét lefedi.
  * _Radial mode:_ 100%-nál egy teljes ciklus a teljes 360°-ot lefedi. (Az értékek a kör százalékai: 50% = fél fordulat, 25% = negyed fordulat stb.)
* **Size** – a hullám amplitúdóját szabályozza (milyen messzire mozdul el a tartalom).
* **Offset** – eltolja a hullámot a tengely mentén (vagy radial módban a kör körül). Ez a wavelength százaléka, ezért **Oscillator Node** segítségével animálhatod, hogy a hullám haladjon.
* **Radial** – linear módról radial módra vált, így az elmozdulás a középpontból mért szögön alapul.
* **Radial Smooth Loop** – úgy állítja a wavelength értéket, hogy az egyenletesen osztható legyen a kör 100%-ával, megelőzve a látható illesztéseket a körbefordulásnál.
* **Triangle** – a hullámformát szinuszról háromszögre váltja.
* **Absolute** – a hullám abszolút értékét veszi, így csak felfelé irányuló elmozdulásokat hoz létre (a negatív oldalt áthajtja a pozitív oldalra).
* **Angle** – elforgatja a hullám tengelyét. 0° = vízszintes.

## &#x20;Noise eltolás pozíció alapján

Ez a node zajmezővel (turbulenciához hasonlóan) torzítja a tartalmat, és a pontokat a választott tengelyre merőlegesen (vagy radiálisan, a középpontból kifelé) tolja el. A _Wave Shift_ node-hoz képest az eredmény organikusabb és véletlenszerűbb.

* **Detail** – a noise finomságát szabályozza. Magasabb érték = élesebb, részletesebb változás. Alacsonyabb érték = simább változás.
* **Wavelength** – a noise minta léptékét állítja be.
  * _Linear mode:_ 100%-nál a noise egy teljes ciklusa a tartalom szélességét lefedi.
  * _Radial mode:_ 100%-nál egy teljes ciklus a teljes 360°-ot lefedi.
* **Size** – az elmozdítás mértékét szabályozza (a noise torzítás amplitúdója).
* **Offset** – eltolja a noise mintát a tengely mentén (vagy a kör körül). Ez a wavelength százaléka, ezért **Oscillator Node** segítségével animálhatod, hogy a noise „áramoljon”.
* **Depth Offset** – a 3D noise mezőn belül mozgat, időbeli változatosságot létrehozva. Különösen hatékony, ha Oscillator Node-dal animálod.
* **Depth Detail** – azt szabályozza, mennyire részletes a változás a mélységi dimenzió mentén.
* **Absolute** – a noise abszolút értékét veszi, a negatív értékeket pozitívba hajtva (csak egyoldalú elmozdulást hoz létre).
* **Angle** – lineáris módban elforgatja a zaj tengelyét. 0° = vízszintes.
* **Radial** – linear módról radial módra vált, így az elmozdulás a középpontból mért szögön alapul.
* **Radial Smooth Loop** – úgy állítja a wavelength értéket, hogy az egyenletesen osztható legyen a kör 100%-ával, megelőzve a látható illesztéseket radial módban.
