---
description: >-
  A lézerek veszélyesek lehetnek, ezért fontos betartani a bevált gyakorlatokat
  és a biztonsági irányelveket. Ez az oldal hasznos áttekintést ad, amely segít
  a lézerek biztonságos beállításának folyamatában.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/setting-up-lasers
---

# ✅ A lézerbeállítási folyamat áttekintése

### A lézerek biztonságos bekapcsolásának folyamata

Ez a kézikönyv nem helyettesíti a hivatalos lézerbiztonsági képzést, amelyre mindenképpen szükséged lesz, mielőtt nyilvános helyen lézereket használnál. Egyes területeken további jogszabályi követelmények is érvényesek, de ettől függetlenül mindig tartsd be a biztonság és a professzionális működés bevált gyakorlatait.

A PLASA ingyenesen letölthető lézerbiztonsági útmutatót kínál, amelyet általában bevált gyakorlatként fogadnak el: [https://www.plasa.org/guidance-for-display-lasers/](https://www.plasa.org/guidance-for-display-lasers/)

Használat előtt győződj meg róla, hogy érted a lézerekkel kapcsolatos biztonsági kockázatokat!

#### Bevezetés

Ez az oldal áttekintést ad a lézerek biztonságos bekapcsolásának folyamatáról. Az egyes lépések pontos végrehajtását a szakasz későbbi részei részletesen ismertetik, de ez az oldal segít átlátni a teljes folyamatot, és később referenciaként is visszatérhetsz hozzá minden lézerbeállításkor.

<figure><img src="../.gitbook/assets/laser-aperture.jpg" alt=""><figcaption><p>Egy tipikus lézer kimeneti nyílásának fedele</p></figcaption></figure>

### A hardver beállítása:

1. **Zárd le a kimeneti nyílás fedelét** a lézeren
2. **Rögzítsd biztonságosan a lézert**, és irányítsd a megfelelő irányba
3. **Csatlakoztasd a stop gombot** a lézerhez
4. **Csatlakoztasd a laser controller eszközt** a számítógépedhez
5. **Kapcsold be** a lézert

### A Liberation beállítása:

1. **Tedd disarmed állapotba az összes lézert**, majd keresd meg és csatlakoztasd a controller eszközt a Liberation alkalmazásban
2. **Állítsd a&#x20;**_**Global Brightness**_**&#x20;beállítást 0-ra** (Használd az ikonsáv csúszkáját vagy az APC40 _Master Fader_ vezérlőjét)
3. **Tedd _armed_ állapotba a lézert** – miközben a kimeneti nyílás fedele továbbra is zárva van, ellenőrizd, hogy jelenleg egyetlen Clip sem aktív, majd tedd _armed_ állapotba a lézert (használd a _Laser Overview_ panel _Arm_ gombját)
4. **Kapcsold be a test pattern elemet** (használd az ikonsáv ☒ gombját, válaszd az 1-es mintát, a kereszttel áthúzott zöld négyzetet)
5. **Állítsd be az Output zone-t** – becsüld meg a legbiztonságosabb zone méretet és pozíciót (például lehet magasan, a mennyezet irányában, de ez az adott környezettől függ)
6. **Ellenőrizd, hogy működik-e a lézer** – lassan emeld a fényerőt, amíg fényt nem látsz a kimeneti nyílás ablaka mögött. Ezután csökkentsd vissza a fényerőt nullára.
7. **Teszteld a stop gombot**, hogy megbizonyosodj róla: megnyomásakor minden lézerkimenet megszűnik

### A lézerkimenet indítása

1. **Ürítsd ki a besugárzási területet** – győződj meg róla, hogy senkit nem érhet lézersugár, és tájékoztasd az összes személyzetet, hogy a lézerek beállítása közben maradjanak a besugárzási területen kívül. (Arról is győződj meg, hogy minden kamera és projektor le van takarva, vagy rajta van az objektívsapka!)
2. **Nyisd ki a kimeneti nyílás fedelét** – állj oldalra, a kimeneti sugár útjától távol, majd csúsztasd le a fedelet. Ha a zone-ok magasan vannak, érdemes lehet részben zárva hagyni.
3. **Emeld a fényerőt addig, amíg a lézer éppen csak láthatóvá válik** – csak annyira legyen fényes a lézer, amennyire a zone láthatóságához szükséges
4. **Állítsd be a zone elemeket** – állítsd be a zone méretét, alakját és pozícióját úgy, hogy bármely közönség számára hozzáférhető területtől számítva legalább 3 m-rel a padló felett legyen, és a lézer ne érjen el más, közönség számára hozzáférhető területeket
5. **Adj hozzá fizikai kitakarást** – használd a kimeneti nyílás fedelét és/vagy fekete fóliaszalagot minden olyan terület fizikai kitakarására, amely a kívánt zone területen kívül esik. Ez rendkívül fontos, mert bármely lézerhardver vagy szoftver meghibásodhat.
6. **Adj hozzá szoftveres masks elemeket** – a Liberation szoftveres masks funkciói használhatók kamerák és projektorok védelmére, de emberek védelmére **soha** nem helyettesíthetik a fizikai kitakarást. Vedd figyelembe, hogy semmilyen szoftver vagy hardver nem tévedhetetlen, ezért győződj meg róla, hogy érted a kockázatokat, mielőtt szoftveres masks elemeket használsz.

{% hint style="warning" %}
Ez az útmutató beltéri beállítást feltételez. Ha kültéren dolgozol, további lépéseket kell tenned a légi közlekedés biztonsága érdekében, többek között:

* A szükséges engedélyek beszerzése légügyi hatóságoktól, például az FAA-tól vagy a CAA-tól
* Egyeztetés a közeli repülőterekkel és repülőterek üzemeltetőivel
* Nyilvános repüléskövető radar ellenőrzése, valamint egy megfigyelő kijelölése, aki figyeli a légi járműveket

A biztonsági küszöbérték alatt jóval működő lézerek is katasztrofális figyelemelterelést okozhatnak a pilótáknak.

Győződj meg róla, hogy rendelkezel a szükséges képesítésekkel, licencekkel és engedélyekkel, mielőtt bármilyen lézert a légtér felé irányítanál.
{% endhint %}
