# ✅ Gyors kezdési útmutató

## Bevezetés

Üdvözlünk a **Liberation** világában – a lézershow-szoftverek következő generációjában.

A Liberation egy nagy tudású, modern és összetett szoftver; a használhatóság és a megbízhatóság alapelveire épül, hogy szabadon kibontakoztathasd a kreativitásodat. Gyors, hatékony és gördülékeny; kövesd ezt a _Gyors kezdési útmutatót_, és rövid időn belül használatra kész leszel!

### Lézerek kezelése

A Liberation elég rugalmas ahhoz, hogy lézereket állíts be és vizualizálj úgy is, hogy egyetlen valódi lézer sincs csatlakoztatva. Amikor pedig készen állsz, zökkenőmentesen hozzárendelheted az egyes kimeneteket egy lézervezérlőhöz.

{% hint style="info" %}
A Liberationben tetszőleges számú lézert állíthatsz be és vizualizálhatsz; a licenccsomagok (Hobbyist, Pro stb.) csak azt korlátozzák, hogy hány lézert tudsz _élesíteni_. Ez azt jelenti, hogy akár ingyenes licenccel is tervezhetsz 100 lézeres show-t. Frissítésre csak akkor van szükség, amikor ténylegesen valódi lézereken szeretnéd futtatni.
{% endhint %}

Az alapbeállítás 8, vízszintesen elrendezett lézert tartalmaz, de ezt bármire testre szabhatod. Amíg ismerkedsz a szoftverrel, valószínűleg érdemes megtartani ezt az alapértelmezést, később pedig hozzáigazíthatod a saját hardveres beállításodhoz. (Lásd: [setting-up-your-project.md](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Fontos: Mielőtt bármelyik lézert élesítenéd, győződj meg róla, hogy érted a kockázatokat, és alaposan olvasd el a [setting-up-lasers.md](../setting-up/setting-up-lasers.md) fejezetet.
{% endhint %}

## A szoftver áttekintése

### Biztonsági leállítás

Ha lézereket futtatsz, mindig legyen kéznél **hardveres vészleállító gomb** (lásd: [emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md)). Ha kevésbé sürgős esetben szeretnél mindent hatástalanítani, használd a _**DISARM ALL**_ gombot, az `Escape` billentyűt, vagy az APC40-en a _**SESSION**_ billentyűt. A globális fényerőt a képernyőn látható csúszkával vagy az APC40 fő faderével is csökkentheted.

### Csúszkaelemek

A Liberationben többféle csúszka és vezérlő található.

{% hint style="info" %}
Ha a csúszka pontosságánál nagyobb kontrollra van szükséged, `Cmd / Ctrl`-kattintással közvetlenül beírhatsz egy új értéket.
{% endhint %}

### Billentyűparancsok

A billentyűparancsok teljes listája itt található: [keyboard-shortcuts.md](../reference/keyboard-shortcuts.md)

### Képernyőelrendezés

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nem vagy biztos benne, mire való egy gomb? Vidd fölé az egeret, és megjelenik a leírása!
{% endhint %}

#### Menü

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

A menüben találod az összes fájlimportálási és -exportálási lehetőséget, valamint innen nyithatók meg a panelek. Itt találod azt az opciót is, amellyel a számítógépet a feliratkozásoddal engedélyezheted (_Liberation -> Authorise/Deauthorise this computer_).

#### Ikonsáv

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Itt találhatók a gyakori műveletek, például az összes lézer élesítése/hatástalanítása, a globális fényerő, a tesztminta, valamint a 3D, Canvas és Output nézetek közötti váltás.

### Nézetek

A képernyő bal felső részén lévő nagy terület a 3 fő nézet egyike lehet: **3D**, **CANVAS** és **OUTPUT.** Ezek között az ikonsáv gombjaival válthatsz (vagy a `Tab` billentyűvel válthatsz a 3D és OUTPUT nézetek között, majd tovább léptethetsz sorban az egyes lézerkimeneteken).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

A 3D nézet megmutatja, hogyan fognak kinézni a lézereid, és beállítható úgy, hogy illeszkedjen a saját lézeres elrendezésedhez. Kattints és húzd az egeret a kamera forgatásához, az egérgörgővel pedig előre-hátra mozgathatod a nézetet. Sok további beállítást találsz a _3D Visualiser settings_ panelen (_View -> 3D Visualiser Settings_). Lásd: [3d-visualiser.md](../setting-up/3d-visualiser.md).

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Az Output View az egyes lézerek zónáinak és maszkjainak beállítására szolgál. (Figyeld meg a hatalmas számot a bal felső sarokban, így könnyen látod, melyik lézeren dolgozol!)

Ez a nézet az adott lézer teljes kimenetét mutatja, valamint azt, hogy az egyes zónák hol helyezkednek el benne. Alapértelmezés szerint lézerenként csak egy zóna van, de ésszerű keretek között tetszőleges számú zónát hozzáadhatsz, és mindegyiket látni fogod ebben a nézetben.

{% hint style="info" %}
**Mi az a zóna?**

A zóna egy olyan terület a lézer kimenetén belül, amelybe lézeres tartalmat irányíthatsz. Egy lézerhez több zóna is tartozhat. A legegyszerűbb zónatípus a _beam_ zóna, de léteznek _canvas_ zónák és _DMX_ zónák is. Ebben az útmutatóban főként a beam zónákra koncentrálunk, amelyeket általában a levegőben megjelenő atmoszférikus sugáreffektek létrehozására használnak.
{% endhint %}

A szerkeszteni kívánt lézert az alábbi módokon választhatod ki:

* a felső sáv számozott gombjaival
* a kívánt lézer számának megfelelő számbillentyű megnyomásával _(1-9_ keys\_)\_
* a `Tab` billentyűvel, amellyel sorban végigléptethetsz rajtuk

Új lézert a _+_ gomb megnyomásával adhatsz hozzá a beállításhoz. (A _Laser Overview_ panelen is található egy _ADD LASER_ gomb.)

Lézert a _Laser Overview_ panel piros ⊖ gombjával törölhetsz a beállításból.

Az egérgörgővel nagyíthatsz és kicsinyíthetsz, a nézet mozgatásához pedig kattints és húzd az egeret bárhol, ahol nincs zóna.

Kattints egy zónára a kijelöléséhez, majd az egérrel állítsd a sarokpontjait. Ha egy sarok húzása közben lenyomva tartod az `Alt / Option` billentyűt, nem egyenletes módosítást végezhetsz. Kattints jobb gombbal a zónára további beállításokhoz, beleértve a zónatípus módosítását is.

Bal oldalt egy ikongombokból álló sáv található; vidd az egeret bármelyik gomb fölé, és megjelenik, mire való. Ezekkel a gombokkal beam zónákat, canvas zónákat és maszkokat adhatsz hozzá. Itt találhatók az adott lézerre vonatkozó tesztminta-beállítások, valamint a rács és az igazítási beállítások is.

További részletek: [output-view](../output-view/).

#### Canvas

A Canvas rendszer főként grafikákhoz és építészeti mappinghez használható. Összetett képeket oszthatsz szét több lézer között, és minden szakaszon perspektívakorrekciót alkalmazhatsz. Lásd: [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/).

### APC40 MIDI vezérlő

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Bár a Liberation egérrel és billentyűzettel is vezérelhető, sokkal jobb egy APC40 MIDI vezérlőfelületet használni (a Mark 2 a legjobb, de a Mark 1 is működik).

Lásd még: [apc40-reference.md](../reference/apc40-reference.md)

Már támogatjuk az APC Mini Mark 2-t és a MIDI Fighter Twistert is, és további vezérlők támogatása fejlesztés alatt áll. A legtöbb esetben azonban az APC40 Mark 2 a legjobb választás.&#x20;

### Clipek és effektek

{% hint style="info" %}
**Mi az a clip?**

A clip a Liberationön belüli bármilyen lézeres tartalom tárolója. A clipek tartalmazhatnak sugarakat vagy grafikus animációkat, és általában ismétlődő ciklusként működnek. Bármely zónába (vagy _Canvas target area_ területre) irányíthatók, és a Clip Deckben található clip gombokkal indíthatók.
{% endhint %}

#### Clip deck áttekintése

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Ezt a rácsot _clip decknek_ nevezzük, és itt tárolódnak az összes lézeres clipek. Úgy lett kialakítva, hogy közvetlenül megfeleljen az APC40 8 x 5 gombos rácsának.

**Navigálás a clip deckben.**

A clip decket balra és jobbra az alábbi módokon görgetheted:

* Bal és jobb nyílbillentyűk. A `Cmd / Ctrl` hozzáadásával egyszerre egy teljes oldalt görgethetsz.
* Trackpad: Swipe
* Egér: ha az egered rendelkezik oldalirányú görgetéssel, azt a clip deck fölött használhatod
* APC40 scroll knob
* APC40 _<- DEVICE ->_ gombok

A tájékozódást felül egy mini clip deck vizualizáló segíti. Lásd még: [clips](../clips/)

#### Clipek indítása és leállítása

Clip indításához nyomj meg egy clip gombot (egérrel vagy az APC40-en). Az újbóli megnyomás leállítja. Amikor elindítasz egy clipet, az azonos színű összes többi clip automatikusan leáll, kivéve, ha lenyomva tartod a _shift_ billentyűt.

Egyes clipek _Flash mode_ módban vannak (alapértelmezés szerint a pirosak); ezek azonnal leállnak, amint elengeded a clip gombot.

A _STOP_ gomb leállítja az összes éppen futó clipet.

#### Kimeneti zónák beállítása a cliphez

A clip gombok alatt találod a zónagombokat, alapértelmezés szerint a beam zónákat 1-től 8-ig (_BEAM 1_, _BEAM 2_ stb.). A zónagombok világítással jelzik, hogy mely zónák vannak hozzárendelve a jelenleg kijelölt cliphez.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Két sorral a zónagombok alatt találod az X/Y tükrözés gombjait; ezekkel vízszintesen és függőlegesen tükrözheted a clipet.

{% hint style="info" %}
Fontos, hogy ezek a zónahozzárendelések és X/Y tükrözési beállítások magához a cliphez tartoznak; a rendszer megőrzi őket a clip következő futtatásakor is. Ezek nem globális beállítások.
{% endhint %}

Kattints jobb gombbal egy clipre a további clipbeállítások szerkesztéséhez. Lásd még: [clip-settings.md](../clips/clip-settings.md)

### Csoportok

Észre fogod venni, hogy minden clipnek színes körvonala van; ez a szín jelzi, melyik _csoportba_ tartozik. Az APC40 clip gombjai is ezzel a színnel világítanak.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cián</td></tr><tr><td>Group 2</td><td>Narancs</td></tr><tr><td>Group 3</td><td>Piros</td></tr><tr><td>Group 4</td><td>Indigó</td></tr><tr><td>Group 5</td><td>Zöld</td></tr></tbody></table>

A csoport rendszer nagyon rugalmas, és lehetővé teszi, hogy:

* az egyik csoportban futó clipeket futva hagyd, miközben egy másik csoportban váltogatod a clipeket
* gyorsan hozzárendelj zónákat és X/Y tükrözéseket egy csoport összes clipjéhez
* _Flash mode_ módot állíts be egy cliphez (a Group 3 alapértelmezés szerint _Flash mode_ módban van)

A csoportoknak átmeneti be- és kifutási beállításai is vannak, amelyeket a clipek örökölhetnek vagy felülírhatnak.

A clip csoportját a jobb gombos menü gombjaival állíthatod be, vagy az APC40-en megnyomhatod a group gombot, és _amíg nyomva tartod_, megnyomhatod a clip gombokat.

Zónabeállítások módosítása egy csoport összes clipjére

Az APC40-en nyomd meg a group gombot, majd _amíg továbbra is nyomva tartod_, a zone és X/Y gombokkal kapcsolhatod a zónabeállításokat az adott csoport összes clipjére.

Lásd még: [groups.md](../clips/groups.md)

### Effektek

A Liberation effekt rendszere hatékony és sokoldalú módot ad a clip kimenetének valós idejű módosítására. Az alapértelmezett 1-8 effektgombok a zónagombok alatt találhatók.

#### Effekt alkalmazása

Nyomj meg egy effektgombot az effekt be- vagy kikapcsolásához, vagy még jobb, ha az APC40 1-8 csúszkáival úsztatod be és ki az effekteket.

#### Effektparaméterek

Az 1-8 forgóvezérlőkkel\* állíthatod az egyes effektek _paraméterét_. (Vagy jobb gombbal kattintva az egérrel is állíthatod a szintet és a paramétert.) A paraméter módosítása az effekt beállításától függően különböző dolgokat vezérel. Az alapértelmezett effektek listáját lent találod.

{% hint style="info" %}
Az effektgombokon látható kis számok az effekt _level_ és _parameter_ értékeire utalnak. A _level_ értéket az APC40 faderével vezérelheted, vagy kattintva-húzva a gombon. A paramétert az APC40 forgóvezérlőivel állíthatod, vagy jobb kattintással az egérrel.
{% endhint %}

_\*Az 1-8 forgóvezérlők az APC40 Mk2 tetején, az Mk1-en pedig jobb felül találhatók. Lásd még:_ [apc40-reference.md](../reference/apc40-reference.md)

#### Az alapértelmezett effektek

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Kaotikus mozgást alkalmaz a clip kimenetére. A paraméter a káosz mennyiségét/sebességét állítja.
2. **Sine wave** :\
   Az összes tartalmat egy mozgó szinuszhullám mentén torzítja. A paraméter a hullámhosszt állítja.
3. **Rotation** :\
   Mindent forgat. A paraméter a forgási sebességet állítja.
4. **Horizontal flip** :\
   Vízszintesen összenyomja és széthúzza a tartalmat. A paraméter a sebességet állítja.
5. **Scale** :\
   Ismételten teljes méretről nullára skáláz mindent. A paraméter a sebességet állítja.
6. **Hue** :\
   Módosítja minden tartalom árnyalatát, de a telítettséget nem változtatja meg (vagyis ami fehér, az fehér marad). A paraméter az árnyalatot állítja.
7. **Saturation and hue** :\
   Módosítja minden tartalom árnyalatát, és teljesen telíti a színt is (vagyis ami fehér, az is az adott színre vált). A paraméter az árnyalatot állítja.
8. **Flash** :\
   Ismételten teljes fényerőről nullára villogtat mindent. A paraméter a villogás sebességét állítja.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Az alsó sorban további 16 színeffekt található, amelyek előre beállított árnyalat- és telítettségértékeket alkalmaznak.

Fontos, hogy ezek az alapértelmezett effektek, de szerkeszthetők, és szinte bármire beállíthatók!

#### Mi az a _„jelenleg kijelölt clip”_?

Amikor elindítasz egy clipet, felvillan, jelezve, hogy aktív. Fehér körvonala is lesz, amely azt mutatja, hogy ez a jelenleg _kijelölt_ clip. Amikor zónagombokat kapcsolsz vagy a clip beállításait módosítod, ezek a _jelenleg kijelölt clipre_ lesznek alkalmazva.

{% hint style="info" %}
Ha egy clipet indítás nélkül szeretnél kijelölni, nyomd le az `Alt / Option` billentyűt, mielőtt megnyomod a clip gombot. Ez jó módszer a zónák és egyéb beállítások módosítására anélkül, hogy futtatnád a clipet.
{% endhint %}

### Clip settings panel

A _Clip Settings_ panelen szerkesztheted a méretezést, az X/Y pozíciót, és hozzáférhetsz a nagy tudású zone delay rendszerhez.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global settings panel

A _Global Settings_ panelen az összes zónára és kimenetre ható globális kimeneti beállításokat módosíthatod.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Kapcsold be az AUTO RESET opciót, hogy a rendszer automatikusan visszaállítsa az összes _Global settings_ értéket, amikor nem fut clip.&#x20;

### Időzítés

Szinte minden lézeres előadásnak van valamilyen zenei kísérete, ezért a Liberation időzítési rendszere percenkénti ütésekben megadott tempóra épül. A _Tempo Panel_ panelen láthatod az idő vizuális megjelenítését; minden négyzet egy ütemet jelöl, és időben villog.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Több szinkronizációs lehetőség is rendelkezésre áll, köztük a MIDI clock és az Ableton Link. Ha ismered a zene tempóját, manuálisan is beállíthatod a képernyőn látható csúszkával vagy az APC40 Tempo knob vezérlőjével, de a _Tap Tempo_ rendszerrel a zene üteméhez is igazíthatod\_.\_

#### Tap Tempo

A _Tap Tempo_ a zenei alkalmazásokban gyakran használt kifejezés; lehetővé teszi, hogy a zene lejátszása közben az ütemre koppintva állítsd be a tempót. Használhatod a képernyőn lévő gombot, de ajánlott inkább a _T_ billentyűt vagy az APC40 _Tap Tempo_ gombját használni (vagy akár lábkapcsolót, ha azt részesíted előnyben).

Nyomd meg az _R_ billentyűt vagy a _Metronome_ gombot (APC40), hogy a tempót a taktus elejére állítsd vissza.

Nyomd meg az _Y_ billentyűt, vagy fordítsd el a _Tempo_ knob(APC40) vezérlőt, hogy a tempót egész számra kerekítsd. Ez hasznos lehet elektronikus zenéknél, amelyek gyakran egész számú BPM-et használnak.

### A clip deck rendszerezése

Ha át szeretnél helyezni egy clipet a clip decken, kattints rá, és húzd az új pozícióba. Húzás közben a kurzorbillentyűkkel (vagy az APC40 görgőjével/gombjaival) balra és jobbra görgethetsz.

Másolat készítéséhez húzás közben tartsd lenyomva az `Alt / Option` billentyűt.

`Alt / Option`-kattintás egy clipen: kijelölés indítás nélkül.

`Alt / Option + Shift`-kattintás egy clipen: többes kijelölés; vagy kattints és húzz egy clipen kívüli területen a „lasszó” kijelöléshez.&#x20;

A kattintás és húzás az ÖSSZES kijelölt clipet mozgatja.

Egy vagy több clip törléséhez húzd le őket a clip deckről (megjelenik egy kuka ikon), vagy használd a DELETE gombot a clip jobb gombos menüjében.

### Laser overview panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

A _Laser overview panel_ gyors áttekintést ad a jelenleg futó lézerek állapotáról. A jobb oldali zöld négyzet azt jelzi, hogy a lézervezérlő rendben működik. Ha narancssárgára vált, időnként kiesések fordulnak elő, ha piros, megszakadt a kapcsolat. Ha szürke, akkor egyáltalán nincs vezérlőhöz csatlakoztatva.&#x20;

A középső grafikon a képkockahosszak előzményeit mutatja, a jobb oldali szám pedig az aktuális képfrissítési sebesség. Minél összetettebb a tartalom, annál alacsonyabb lesz a képfrissítési sebesség (vagyis annál villogósabbnak tűnhet). Körülbelül 25fps alatt már észrevehetően villogós lehet.&#x20;

### Csatlakozás lézerekhez – Controller Assignment panel

Kattints az _Assign Laser Controllers_ gombra a _Controller Assignment_ panel megnyitásához. (Ez a panel a menüsorban a _View -> Controller Assignment_ útvonalon is elérhető.)

Itt kiválaszthatod, hogy mely lézerkimenetek mely lézervezérlőkre kerüljenek. Húzd a vezérlőket a jobb oldali listából a bal oldali helyekre. A vezérlőket át is nevezheted annak megfelelően, hogy melyik lézerhez vannak párosítva (használd a toll ikon gombot).

További részletekért olvasd el a [controller-assignment.md](../setting-up/controller-assignment.md) fejezetet.

{% hint style="danger" %}
Mielőtt bármelyik lézert élesítenéd, mindenképpen olvasd el a [setting-up-lasers.md](../setting-up/setting-up-lasers.md) fejezetet.
{% endhint %}

### Laser output panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Ez a panel a _jelenleg kijelölt lézer_ beállításait mutatja (ezt a felül látható szám jelzi). A jelenleg kijelölt lézert a _tab_ billentyűvel, egy számbillentyű megnyomásával, a _Laser Overview_ panelen lévő lézerszámra kattintva vagy az _output view_ nézetben válthatod.

* **Number button** élesíti és hatástalanítja a lézert; ha piros, a lézer élesítve van.
* **Brightness** a lézer fényerejét a többi lézertől függetlenül állítja (és összeadódik a _global brightness_ beállítással – vagyis ha mindkettő 50%, a lézered 25%-on lesz).
* **Test Pattern** tesztmintát kapcsol be csak ehhez a lézerhez (felülírja a globális tesztminta-beállítást).
* **Orientation** korrigálja az oldalra vagy fejjel lefelé felszerelt lézereket.
* **Flip Horizontal and Flip Vertical** megfordítja a lézer kimenetét. Hasznos kimenetkorrekcióhoz eltérően bekötött lézereknél.
* **Copy Laser Settings** megnyit egy panelt, amellyel különféle beállításokat másolhatsz erről a lézerről másokra.

### Scanner beállítások

A show-lézerek úgy működnek, hogy egyetlen lézersugarat rendkívül gyorsan mozgatnak, miközben be- és kikapcsolják, hogy alakzatokat rajzoljanak a levegőbe. Amit vonalaknak, alakzatoknak és képeknek látsz, az valójában a sugár olyan gyors útvonalkövetése, amelyet a szemed már nem tud külön mozgásként követni.

A pontfolyam az az adat, amely megmondja a lézernek, hová mozduljon következőként, és mikor legyen a sugár be- vagy kikapcsolva. A Liberationben a clipek valós időben alakulnak át erre a pontfolyamra, miközben a lézerekhez kerülnek.

A Liberation részletes kontrollt ad afölött, hogyan jön létre ez a pontfolyam, így minden lézernél egyensúlyba hozhatod a simaságot, a fényerőt és a teljesítményt.

{% hint style="info" %}
Ha olyan régebbi lézerszoftverekhez vagy szokva, amelyek előre kiszámított pontfolyamokra támaszkodnak, ez a megközelítés eleinte eltérőnek tűnhet. A valós idejű pontgenerálás azonban lehetővé teszi, hogy ugyanaz a tartalom minden lézerhez eltérően legyen optimalizálva. Így könnyebb több, eltérő scanner sebességű vagy minőségű lézerrel dolgozni anélkül, hogy a tartalmat duplikálni vagy újraépíteni kellene. Emellett a clipfájlok mérete is nagyon kicsi marad, ezért a teljes alapértelmezett Liberation clip deck csak néhány megabájt, nem pedig gigabájt méretű.
{% endhint %}

Az alapvető scanner beállítások:

* **Speed** a scanner sebessége, vagyis hogy a lézer milyen gyorsan mozog az alakzatok rajzolásához. Ez a hagyományos lézerszoftverekben a pontsebesség állításának felel meg, de a Liberationben a lézer mozgási sebességét _a pontsebességtől függetlenül_ módosíthatod. Ezt általában nem kell állítanod.
* **Scanner sync** (néha _blank shift_ néven ismert, korábban Colour Shift) A scannerek nagyon gyorsan mozgatják a lézert, de a fényerő- és színváltozás általában nincs szinkronban a mozgással. Ez a sugarak és vonalak szélén kis villódzó fény-„farokként” jelenik meg. Ezzel a beállítással hozhatod szinkronba a mozgást és a színt. Lásd: [laser-settings](../setting-up/laser-settings/)

A többi haladó scanner beállítást az [advanced](../advanced/) fejezet tárgyalja.

### Zónázás

A lézerek beállításáról és zónázásáról szóló teljes útmutató: [setting-up-lasers.md](../setting-up/setting-up-lasers.md)
