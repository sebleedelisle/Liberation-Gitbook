# ✅ Gyors kezdési útmutató

## Bevezetés

Üdvözlünk a **Liberation** világában – ez a lézershow-szoftverek következő generációja.

A Liberation erős és összetett modern szoftver. A használhatóságra és a megbízhatóságra épül, hogy szabadon kibontakoztathasd a kreativitásodat. Gyors, hatékony és gördülékeny; kövesd ezt a _gyors kezdési útmutatót_, és hamar használatra kész leszel!

### Lézerek kezelése

A Liberation elég rugalmas ahhoz, hogy lézereket állíts be és jeleníts meg akkor is, ha egyetlen valódi lézer sincs csatlakoztatva. Amikor pedig készen állsz, minden kimenetet zökkenőmentesen hozzárendelhetsz egy laser controller eszközhöz.

{% hint style="info" %}
A Liberationben annyi lézert állíthatsz be és jeleníthetsz meg, amennyit szeretnél. A licenccsomagok (Hobbyist, Pro stb.) csak azt korlátozzák, hány lézert tudsz _armed_ állapotba tenni. Ez azt jelenti, hogy akár ingyenes licenccel is tervezhetsz 100 lézeres show-t. Csak akkor kell frissítened, amikor valódi lézereken szeretnéd futtatni.
{% endhint %}

Az alapértelmezett beállítás 8, vízszintesen elrendezett lézert tartalmaz, de ezt tetszés szerint módosíthatod. Amíg ismerkedsz a szoftverrel, érdemes megtartani ezt az alapbeállítást, később pedig igazíthatod a saját hardveres felépítésedhez. (Lásd: [A projekt beállítása](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Fontos: mielőtt bármelyik lézert armed állapotba tennéd, győződj meg róla, hogy érted a kockázatokat, és alaposan menj végig a [Lézerek beállítása](../setting-up/setting-up-lasers.md) fejezeten.
{% endhint %}

## A szoftver áttekintése

### Biztonsági leállítás

Amikor lézereket működtetsz, mindig legyen kéznél egy **hardveres vészleállító gomb** (lásd: [Vészleállítás / reteszelések](../hardware/emergency-stop-interlocks.md)). Ha kevésbé sürgős helyzetben szeretnél mindent _disarmed_ állapotba kapcsolni, használhatod a _**DISARM ALL**_ gombot, az `Escape` billentyűt, vagy az APC40 _**SESSION**_ gombját. A Global Brightness értékét is csökkentheted a képernyőn látható csúszkával vagy az APC40 fő faderével.

### Csúszkaelemek

A Liberation több helyén találsz különféle csúszkákat és vezérlőket.

{% hint style="info" %}
Ha a csúszka pontosságánál nagyobb kontrollra van szükséged, `Cmd / Ctrl`-kattintással közvetlenül beírhatsz egy új értéket.
{% endhint %}

### Billentyűparancsok

A billentyűparancsok teljes listája itt található: [Billentyűparancsok](../reference/keyboard-shortcuts.md)

### Képernyőelrendezés

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nem vagy biztos benne, mire való egy gomb? Vidd fölé az egeret, és megjelenik a leírása!
{% endhint %}

#### Menü

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

A menüben találod az összes fájlimportálási és -exportálási lehetőséget, valamint innen nyithatod meg a paneleket. Itt találod azt a lehetőséget is, amellyel a számítógépet a feliratkozásodhoz engedélyezheted (_Liberation -> Authorise/Deauthorise this computer_).

#### Ikonsáv

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Itt találod a gyakori műveleteket, például az összes lézer arm/disarm vezérlését, a Global Brightness beállítást, a test pattern kapcsolót, valamint a 3D, Canvas és Output view közötti váltást.

### Nézetek

A képernyő bal felső részén lévő nagy terület a három fő nézet egyike lehet: **3D**, **CANVAS** vagy **OUTPUT.** Az ikonsáv gombjaival válthatsz közöttük. A `Tab` billentyűvel a 3D és az OUTPUT view között válthatsz, majd tovább lépkedhetsz sorban az egyes lézerkimenetek között.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

A 3D view megmutatja, hogyan fognak kinézni a lézereid, és beállítható úgy, hogy megfeleljen a saját lézeres elrendezésednek. Kattintással és húzással forgathatod a kamerát, az egérgörgővel pedig előre-hátra mozgathatod. Sok további opciót találsz a _3D Visualiser settings_ panelen (_View -> 3D Visualiser Settings_). Lásd: [3D megjelenítő](../setting-up/3d-visualiser.md).

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Az Output view a zones és masks beállítására szolgál minden lézerhez. (Figyeld a bal felső sarokban lévő hatalmas számot, így könnyen látod, melyik lézeren dolgozol!)

Ez a nézet az adott lézer teljes kimenetét mutatja, és azt, hogy az egyes zone elemek hol helyezkednek el benne. Alapértelmezés szerint lézerenként csak egy zone van, de ésszerű keretek között bármennyit hozzáadhatsz, és mind megjelenik ebben a nézetben.

{% hint style="info" %}
**Mi az a zone?**

A zone a lézer kimenetén belüli terület, ahová lézeres tartalmat irányíthatsz. Egy lézeren több zone is lehet. A legegyszerűbb típus a _beam_ zone, de léteznek _canvas_ zones és _DMX_ zones is. Ebben az útmutatóban főként a beam zones használatára koncentrálunk, amelyeket általában levegőben látható atmoszférikus beam effektekhez használnak.
{% endhint %}

A szerkeszteni kívánt lézert többféleképpen választhatod ki:

* a felső sáv számozott gombjaival
* a kívánt lézer számának megfelelő billentyű megnyomásával _(1-9_ billentyűk\_)\_
* a `Tab` billentyűvel, amellyel sorban végiglépkedhetsz rajtuk

Új lézert a _+_ gomb megnyomásával adhatsz a beállításhoz. (A _Laser Overview_ panelen is van egy _ADD LASER_ gomb.)

Lézert a _Laser Overview_ panel piros ⊖ gombjával törölhetsz a beállításból.

Az egér görgőjével nagyíthatsz és kicsinyíthetsz, és bárhol kattintva-húzva mozgathatod a nézetet, ahol nincs zone.

Kattints egy zone elemre a kijelöléséhez, majd az egérrel igazítsd a sarokpontjait. Ha sarok húzása közben lenyomva tartod az `Alt / Option` billentyűt, nem egyenletesen módosíthatod. Jobb kattintással további opciókat nyithatsz meg, például a zone típusának módosítását.

Bal oldalt egy ikongombokból álló sávot találsz. Vidd az egeret bármelyik gomb fölé, és megjelenik, mire való. Ezekkel a gombokkal beam zones, canvas zones és masks adhatók hozzá. Itt találod az adott lézerre vonatkozó test pattern, rács- és igazítási beállításokat is.

További részletek: [Output nézet](../output-view/).

#### Canvas

A Canvas rendszer főként grafikákhoz és építészeti mappinghez használható. Összetett képeket oszthatsz szét több lézer között, és minden szakaszon perspektívakorrekciót alkalmazhatsz. Lásd: [Grafika és a Canvas rendszer](../graphics-and-the-canvas-system/).

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Bár a Liberation egérrel és billentyűzettel is vezérelhető, sokkal jobb APC40 MIDI vezérlőfelületet használni. A Mark 2 a legjobb választás, de a Mark 1 is működik.

Lásd még: [APC40 referencia](../reference/apc40-reference.md)

Már az APC Mini Mark 2 és a MIDI Fighter Twister támogatását is megvalósítottuk, és további eszközök fejlesztés alatt állnak. A legtöbb esetben azonban az APC40 Mark 2 a legjobb választás.&#x20;

### Clips és effektek

{% hint style="info" %}
**Mi az a Clip?**

A Clip egy tároló bármilyen lézeres tartalom számára a Liberationben. A Clips tartalmazhatnak beams elemeket vagy grafikus animációkat, és általában ismétlődő ciklusként működnek. Bármelyik zone területre (vagy _Canvas target area_ célterületre) irányíthatók, és a Clip Deckben lévő Clip gombokkal indíthatók.
{% endhint %}

#### Clip Deck áttekintése

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Ezt a rácsot _Clip Deck_ néven használjuk; itt tárolódik az összes lézeres Clip. Úgy készült, hogy közvetlenül megfeleljen az APC40 8 x 5 gombos rácsának.

**Navigálás a Clip Deck területén.**

A Clip Deck balra és jobbra görgethető:

* Bal és jobb nyílbillentyűvel. `Cmd / Ctrl` hozzáadásával egyszerre egy teljes oldalt görgethetsz.
* Trackpaddel: legyintéssel
* Egérrel: ha az egered támogatja az oldalirányú görgetést, használd, miközben a mutató a Clip Deck fölött van
* APC40 görgetőgombbal
* APC40 _<- DEVICE ->_ gombokkal

A tájékozódást felül egy mini Clip Deck megjelenítő segíti. Lásd még: [Clipek és Clip Deck](../clips/)

#### Clips indítása és leállítása

Clip indításához nyomj meg egy Clip gombot egérrel vagy az APC40 eszközön. Újbóli megnyomással leállítod. Amikor elindítasz egy Clip elemet, az azonos színű összes többi Clip automatikusan leáll, kivéve, ha lenyomva tartod a _shift_ billentyűt.

Egyes Clips _Flash mode_ módban vannak (alapértelmezés szerint a pirosak). Ilyenkor azonnal leállnak, amint felengeded a Clip gombot.

A _STOP_ gomb leállítja az összes éppen futó Clip elemet.

#### Output zones beállítása a Clip számára

A Clip gombok alatt látod a zone gombokat, alapértelmezés szerint a beam zones 1-től 8-ig (_BEAM 1_, _BEAM 2_ stb.). A zone gombok világítása jelzi, mely zones vannak hozzárendelve az aktuálisan kijelölt Clip elemhez.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Két sorral a zone gombok alatt találod az X/Y tükrözőgombokat. Ezekkel vízszintesen és függőlegesen tükrözheted a Clip tartalmát.

{% hint style="info" %}
Fontos, hogy ezek a zone hozzárendelések és X/Y tükrözési beállítások magához a Clip elemhez tartoznak; a következő futtatáskor is megmaradnak. Nem globális beállítások.
{% endhint %}

Jobb kattintással további beállításokat szerkeszthetsz az adott Clip elemhez. Lásd még: [Clip beállításai](../clips/clip-settings.md)

### Csoportok

Észre fogod venni, hogy minden Clip színes körvonalat kap, és ez a szín jelzi, melyik _csoportba_ tartozik. Az APC40 Clip gombjai is ezzel a színnel világítanak.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>1. csoport</td><td>Cián</td></tr><tr><td>2. csoport</td><td>Narancs</td></tr><tr><td>3. csoport</td><td>Piros</td></tr><tr><td>4. csoport</td><td>Indigó</td></tr><tr><td>5. csoport</td><td>Zöld</td></tr></tbody></table>

A csoportos rendszer nagyon rugalmas, és lehetővé teszi, hogy:

* egy csoport Clips elemei tovább fussanak, miközben egy másik csoport elemeit kapcsolgatod
* gyorsan hozzárendelj zones és X/Y tükrözési beállításokat egy csoport összes Clip eleméhez
* _Flash mode_ módot állíts be egy Clip elemhez (a 3. csoport alapértelmezés szerint _Flash mode_ módban van)

A csoportokhoz be- és kimeneti átmenetbeállítások is tartoznak, amelyeket a Clips örökölhetnek, vagy felülírhatnak.

A Clip csoportját a jobb kattintásos menü gombjaival állíthatod be, vagy APC40 használata esetén nyomd le a csoport gombját, és _amíg lenyomva tartod_, nyomd meg a Clip gombokat.

Zone beállítások módosítása egy csoport összes Clip eleméhez

APC40 használatakor nyomd meg a csoport gombját, majd _amíg lenyomva tartod_, a zone és X/Y gombokkal kapcsolhatod az adott csoport összes Clip elemének zone beállításait.

Lásd még: [Clipcsoportok](../clips/groups.md)

### Effektek

A Liberation effektrendszere erős és sokoldalú módja annak, hogy valós időben módosítsd a Clip kimenetét. Az alapértelmezett 1–8 effektgombok a zone gombok alatt találhatók.

#### Effekt alkalmazása

Nyomj meg egy effektgombot az effekt be- vagy kikapcsolásához, vagy még jobb, ha az APC40 1–8 csúszkáival fokozatosan hozod be és ki az effekteket.

#### Effektparaméterek

Az 1–8 rotary controller\* segítségével állíthatod az egyes effektek _parameter_ értékét. (Egérrel jobb kattintással is állíthatod a level és parameter értéket.) A parameter módosítása az effekt beállításától függően különböző dolgokat csinál. Az alapértelmezett effekteket az alábbi lista mutatja.

{% hint style="info" %}
Az effektgombokon látható kis számok az effekt _level_ és _parameter_ értékére utalnak. A _level_ értékét az APC40 faderével vezérelheted, vagy kattintással-húzással a gombon. A parameter az APC40 rotary vezérlőivel állítható, vagy jobb kattintással egérrel is módosítható.
{% endhint %}

_\*Az 1–8 rotary controller az APC40 Mk2 felső részén, az Mk1 esetén pedig jobb felül található. Lásd még:_ [APC40 referencia](../reference/apc40-reference.md)

#### Az alapértelmezett effektek

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Kaotikus mozgást alkalmaz a Clip kimenetére. A parameter a káosz mértékét/sebességét állítja.
2. **Sine wave** :\
   Az összes tartalmat mozgó szinuszhullám mentén torzítja. A parameter a hullámhosszt állítja.
3. **Rotation** :\
   Mindent körbeforgat. A parameter a forgási sebességet állítja.
4. **Horizontal flip** :\
   Vízszintesen összenyomja és széthúzza a tartalmat. A paraméter a sebességet állítja.
5. **Scale** :\
   Ismételten teljes méretről nullára méretez mindent. A parameter a sebességet állítja.
6. **Hue** :\
   Mindennek megváltoztatja a színárnyalatát, de a telítettséget nem módosítja (vagyis ami fehér, az fehér marad). A parameter a színárnyalatot állítja.
7. **Saturation and hue** :\
   Mindennek megváltoztatja a színárnyalatát, és teljesen telíti a színt is (vagyis ami fehér, az az adott színre változik). A parameter a színárnyalatot állítja.
8. **Flash** :\
   Ismételten teljes fényerőről nullára villogtat mindent. A parameter a villogás sebességét állítja.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Az alsó sorban további 16 színeffekt található előre beállított hue és saturation értékek alkalmazásához.

Fontos, hogy ezek csak az alapértelmezett effektek; szinte bármire átszerkeszthetők!

#### Mi az az _„aktuálisan kijelölt Clip”_?

Amikor elindítasz egy Clip elemet, világítani kezd, jelezve, hogy aktív. Emellett fehér körvonalat is kap, amely azt mutatja, hogy jelenleg ez a _kijelölt_ Clip. Amikor zone gombokat kapcsolsz vagy Clip beállításokat módosítasz, ezek az _aktuálisan kijelölt Clip_ elemre vonatkoznak.

{% hint style="info" %}
Ha úgy szeretnél kijelölni egy Clip elemet, hogy nem indítod el, nyomd le az `Alt / Option` billentyűt a Clip gomb megnyomása előtt. Ez jó módszer a zones és más beállítások módosítására anélkül, hogy futtatnád.
{% endhint %}

### Clip Settings panel

A _Clip Settings_ panelen szerkesztheted a méretezést, az X/Y pozíciót, és hozzáférhetsz a nagy teljesítményű zone delay rendszerhez.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings panel

A _Global Settings_ panelen olyan globális kimeneti beállításokat módosíthatsz, amelyek az összes zone teljes kimenetére hatnak.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Kapcsold be az AUTO RESET opciót, hogy az összes _Global settings_ automatikusan visszaálljon, amikor nincs lejátszás alatt Clip.&#x20;

### Időzítés

Szinte minden lézeres megjelenítéshez tartozik valamilyen zenei hangsáv, ezért a Liberation időzítési rendszere percenkénti ütésszámon alapuló tempóra épül. A _Tempo Panel_ területén az idő vizuális ábrázolását látod; minden négyzet egy ütemet jelöl, és ütemre villog.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Több szinkronizálási lehetőség is elérhető, köztük a MIDI clock és az Ableton Link. Ha ismered a zene tempóját, kézzel is beállíthatod a képernyőn látható csúszkával vagy az APC40 Tempo gombjával, de a _Tap Tempo_ rendszerrel is tarthatod az ütemet a zenével\_.\_

#### Tap Tempo

A _Tap Tempo_ a zenei alkalmazásokban gyakran használt kifejezés: lehetővé teszi, hogy a zene lejátszása közben az ütemre koppintva állítsd be a tempót. Használhatod a képernyőn lévő gombot, de ajánlott inkább a _T_ billentyűt vagy az APC40 _Tap Tempo_ gombját használni (vagy akár lábkapcsolót, ha azt szeretnéd).

A tempó ütem elejére állításához nyomd meg az _R_ billentyűt vagy az APC40 _Metronome_ gombját.

A tempó egész számra kerekítéséhez nyomd meg a _Y_ billentyűt, vagy fordítsd el az APC40 _Tempo_ gombját. Ez elektronikus zenénél lehet hasznos, ahol a percenkénti ütésszám általában egész szám.

### A Clip Deck rendszerezése

Ha át szeretnél helyezni egy Clip elemet a Clip Deck területén, kattints rá, és húzd az új helyére. Húzás közben a kurzorbillentyűkkel vagy az APC40 görgőjével/gombjaival balra és jobbra görgethetsz.

Másolat készítéséhez húzás közben tartsd lenyomva az `Alt / Option` billentyűt.

`Alt / Option`-kattintással egy Clip kijelölhető anélkül, hogy elindulna.

`Alt / Option + Shift`-kattintással több Clip is kijelölhető, vagy kattints és húzz egy Clip-en kívüli területen a „lasszó” kijelöléshez.&#x20;

Kattintással és húzással az ÖSSZES kijelölt Clip együtt mozgatható.

Egy vagy több Clip törléséhez húzd le őket a Clip Deck területéről (megjelenik egy kuka ikon), vagy használd a Clip jobb kattintásos menüjének DELETE gombját.

### Laser Overview panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

A _Laser Overview panel_ gyors áttekintést ad az éppen futó lézereid állapotáról. A jobb oldali zöld négyzet azt jelzi, hogy a laser controller rendben működik. Ha narancssárgára vált, időnkénti kimaradások vannak; ha piros, megszakadt a kapcsolat. Ha szürke, akkor egyáltalán nincs controller csatlakoztatva.&#x20;

A középső grafikon a képkockahosszok előzményeit mutatja, a jobb oldali szám pedig az aktuális képkockasebesség. Minél összetettebb a tartalom, annál alacsonyabb lesz a képkockasebesség (vagyis annál vibrálóbbnak tűnhet). Körülbelül 25 fps alatt már kissé vibrálónak látszik.&#x20;

### Csatlakozás lézerekhez – Controller Assignment panel

Kattints az _Assign Laser Controllers_ gombra a _Controller Assignment_ panel megnyitásához. (Ez a panel a menüsáv _View -> Controller Assignment_ útvonalán is elérhető.)

Itt választhatod ki, mely lézerkimenetek mely laser controller eszközökhöz tartozzanak. Húzd át a controller elemeket a jobb oldali listából a bal oldali helyekre. A controller eszközöket át is nevezheted, hogy illeszkedjenek ahhoz a lézerhez, amellyel párosítva vannak (használd a toll ikonú gombot).

További részletekért olvasd el a [Vezérlő-hozzárendelés](../setting-up/controller-assignment.md) fejezetet.

{% hint style="danger" %}
Mielőtt bármelyik lézert armed állapotba tennéd, mindenképp menj végig a [Lézerek beállítása](../setting-up/setting-up-lasers.md) fejezeten.
{% endhint %}

### Laser Settings panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Ez a panel az _aktuálisan kijelölt lézer_ beállításait mutatja (ezt a felső szám jelzi). Az aktuálisan kijelölt lézert a _tab_ billentyűvel, egy számbillentyű megnyomásával, a _Laser Overview_ panelen lévő lézerszámra kattintva vagy az _output view_ területen válthatod.

* **Number button** _armed_ vagy _disarmed_ állapotba kapcsolja a lézert; ha piros, a lézer _armed_ állapotban van.
* **Brightness** a többi lézertől függetlenül állítja a lézer fényerejét (és összeadódik a _global brightness_ beállítással – vagyis ha mindkettő 50%, a lézered 25%-on lesz).
* **Test Pattern** csak ehhez a lézerhez kapcsol be test pattern mintát (felülírja a globális test pattern beállítást).
* **Orientation** korrigálja az oldalra vagy fejjel lefelé felszerelt lézereket.
* **Flip Horizontal and Flip Vertical** megfordítja a lézer kimenetét. Hasznos kimeneti korrekcióhoz, ha a lézerek bekötése nem egységes.
* **Copy Laser Settings** megnyit egy panelt, amellyel különféle beállításokat másolhatsz erről a lézerről másokra.

### Scanner beállítások

A megjelenítő lézerek úgy működnek, hogy egyetlen lézersugarat rendkívül gyorsan mozgatnak, miközben be- és kikapcsolják, hogy alakzatokat rajzoljanak a levegőbe. Amit vonalaknak, alakzatoknak és képeknek látsz, valójában a sugár útvonala, amelyet olyan gyorsan követ, hogy a szemed már nem tudja külön mozgásként érzékelni.

A point stream az az adatfolyam, amely megmondja a lézernek, hová mozduljon tovább, és mikor legyen be- vagy kikapcsolva a sugár. A Liberation a Clips tartalmát valós időben alakítja át erre a point stream formára, miközben elküldi a lézereknek.

A Liberation részletes kontrollt ad afelett, hogyan jön létre ez a point stream, így minden lézernél egyensúlyba hozhatod a simaságot, a fényerőt és a teljesítményt.

{% hint style="info" %}
Ha olyan régebbi lézerszoftverhez vagy szokva, amely előre kiszámított point stream adatokra épít, ez a megközelítés elsőre eltérőnek tűnhet. A valós idejű pontgenerálás azonban lehetővé teszi, hogy ugyanaz a tartalom minden lézerhez külön optimalizálható legyen. Így könnyebb több, eltérő scanner sebességű vagy minőségű lézerrel dolgozni anélkül, hogy a tartalmat duplikálni vagy újraépíteni kellene. Emellett a Clip fájlok nagyon kicsik maradnak, ezért a teljes alapértelmezett Liberation Clip Deck csak néhány megabájt, nem pedig gigabájt méretű.
{% endhint %}

Az alapvető scanner beállítások:

* **Speed** a scanner sebessége, vagyis az, milyen gyorsan mozog a lézer az alakzatok rajzolásához. Ez a hagyományos lézerszoftverek point rate állításának felel meg, de a Liberation lehetővé teszi, hogy a lézer mozgási sebességét _a point rate értékétől függetlenül_ módosítsd. Ezt általában nem kell állítanod.
* **Scanner sync** (más néven _blank shift, korábban Colour Shift_) A scanners nagyon gyorsan mozgatják a lézert, de a fényerő- és színváltozás általában nincs szinkronban a mozgással. Ez apró, vibráló fény-„farokként” jelenik meg a beams és vonalak szélén. Ezzel a beállítással hozhatod szinkronba a mozgást és a színt. Lásd: [Laser Settings](../setting-up/laser-settings/)

A többi haladó scanner beállítást a [Haladó beállítások](../advanced/) fejezet tárgyalja.

### Zoning

A lézerek beállításának és zoning folyamatának teljes útmutatójához lásd: [Lézerek beállítása](../setting-up/setting-up-lasers.md)
