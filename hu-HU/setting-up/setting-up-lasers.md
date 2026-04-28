---
description: >-
  A lézerek veszélyesek lehetnek, ezért fontos betartani a bevált gyakorlatokat
  és a biztonsági irányelveket. Ez az oldal hasznos áttekintést ad, amely
  segít a lézerek biztonságos beállításának folyamatában.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/setting-up-lasers
---

# ✅ Lézerek beállítási folyamatának áttekintése

### A lézerek biztonságos bekapcsolási folyamatának áttekintése

Ez a kézikönyv nem helyettesíti a hivatalos lézerbiztonsági képzést, amelyre mindenképpen szükséged lesz, mielőtt nyilvános környezetben lézereket használsz. Egyes területeken további jogi követelmények is érvényesek, de ettől függetlenül mindig tartsd be a biztonságos és professzionális munkavégzés bevált gyakorlatait.

A PLASA ingyenesen letölthető lézerbiztonsági útmutatót kínál, amelyet általánosan bevált gyakorlatként fogadnak el: [https://www.plasa.org/guidance-for-display-lasers/](https://www.plasa.org/guidance-for-display-lasers/)

Használat előtt mindenképpen győződj meg róla, hogy érted a lézerekhez kapcsolódó biztonsági kockázatokat!

#### Bevezetés

Ez az oldal áttekintést ad arról, hogyan lehet biztonságosan bekapcsolni a lézereket. Az egyes lépések pontos végrehajtásának részleteit a fejezet későbbi részei tárgyalják, de ez az oldal segít átlátni a teljes folyamatot, és később referenciaként is visszatérhetsz hozzá minden lézerbeállítás előtt.

<figure><img src="../.gitbook/assets/laser-aperture.jpg" alt=""><figcaption><p>Egy tipikus lézer apertúrafedele</p></figcaption></figure>

### A hardver beállítása:

1. **Zárd le az apertúrafedelet** a lézeren
2. **Rögzítsd biztonságosan a lézert**, és irányítsd a megfelelő irányba
3. **Csatlakoztasd a leállítógombot** a lézerhez
4. **Csatlakoztasd a lézervezérlőt** a számítógéphez
5. **Kapcsold be** a lézert

### A Liberation beállítása:

1. **Hatástalaníts minden lézert**, majd keresd meg és csatlakoztasd a vezérlőt a Liberation alkalmazásban
2. **Állítsd a&#x20;**_**Global Brightness**_**&#x20;beállítást 0-ra** (használd az ikonsáv csúszkáját vagy az APC40 _Master Fader_ vezérlőjét)
3. **Élesítsd a lézert** - miközben az apertúrafedél még zárva van, győződj meg róla, hogy jelenleg nincs aktív Clip, majd élesítsd a lézert (használd a _Laser Overview_ panel _Arm_ gombját)
4. **Kapcsold be a tesztmintát** (használd az ikonsáv ☒ gombját, válaszd az 1-es mintát: a zöld négyzetet kereszttel)
5. **Állítsd be a kimeneti zónát** - becsüld meg a legbiztonságosabb zónaméretet és pozíciót (például ez lehet magasan, a mennyezet felé irányítva, de ez az adott környezettől függ)
6. **Ellenőrizd, hogy a lézer működik-e** - lassan növeld a fényerőt, amíg fényt nem látsz az apertúraablak mögött. Ezután csökkentsd vissza a fényerőt nullára.
7. **Teszteld a leállítógombot**, hogy megnyomásakor minden lézerkimenet megszűnik-e

### A lézerkimenet indítása

1. **Ürítsd ki az expozíciós területet** - győződj meg róla, hogy senki sem kerülhet a lézersugár útjába, és tájékoztasd a személyzetet, hogy a lézerek beállítása közben maradjanak távol az expozíciós területtől. (Arra is ügyelj, hogy minden kamera és projektor le legyen takarva, vagy rajta legyen az objektívsapka!)
2. **Nyisd ki az apertúrafedelet** - állj oldalra, a kimeneti iránytól távol, majd csúsztasd le az apertúrafedelet. Ha a zónáid magasan vannak, érdemes lehet részben zárva hagyni.
3. **Növeld a fényerőt addig, amíg a lézer éppen csak láthatóvá válik** - csak annyira legyen fényes, amennyire a zóna ellenőrzéséhez szükséges
4. **Állítsd be a zóná(ka)t** - állítsd be a zóna méretét, alakját és pozícióját úgy, hogy a közönség által hozzáférhető területeken a padlótól legalább 3 m-re legyen, és a lézer ne érjen el más, közönség által hozzáférhető területeket
5. **Adj hozzá fizikai maszkolást** - az apertúrafedél és/vagy fekete fóliaszalag segítségével fizikailag takard ki a kívánt zónán kívüli területeket. Ez kiemelten fontos, mert bármely lézeres hardver vagy szoftver meghibásodhat.
6. **Adj hozzá szoftveres maszkokat** - a Liberation szoftveres maszkjai használhatók kamerák és projektorok védelmére, de emberek védelmére **soha** nem helyettesíthetik a fizikai maszkolást. Ne feledd, hogy semmilyen szoftver vagy hardver nem tévedhetetlen, ezért szoftveres maszkok használata előtt győződj meg róla, hogy érted a kockázatokat.

{% hint style="warning" %}
Ez az útmutató beltéri beállítást feltételez. Ha kültéren dolgozol, további lépéseket kell tenni a repülésbiztonság érdekében, többek között:

* A szükséges engedélyek beszerzése a légügyi hatóságoktól, például az FAA-tól vagy a CAA-tól
* Egyeztetés a közeli repülőterekkel és repülőterek üzemeltetőivel
* Nyilvános repüléskövető radar ellenőrzése, valamint megfigyelő kijelölése a repülőgépek figyelésére

A biztonsági határérték alatt jóval működő lézerek is katasztrofális figyelemelterelést okozhatnak a pilóták számára.

Győződj meg róla, hogy rendelkezel a szükséges képesítésekkel, licencekkel és engedélyekkel, mielőtt bármilyen lézert a légtérbe irányítasz.
{% endhint %}
