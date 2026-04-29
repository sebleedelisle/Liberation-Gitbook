---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Gyors kezdési útmutató

## Bevezetés

Üdvözlünk a **Liberation** világában – ez a lézershow-szoftverek új generációja.

A Liberation nagy teljesítményű és összetett, modern szoftver; használhatóságra és megbízhatóságra épül, hogy szabadon kibontakoztathasd a kreativitásodat. Gyors, hatékony és gördülékeny; kövesd ezt a _Gyors kezdési útmutatót_, és pillanatok alatt elindulhatsz!

### Lézerek kezelése

A Liberation elég rugalmas ahhoz, hogy valódi, csatlakoztatott lézerek nélkül is beállíthasd és vizualizálhasd a lézereket. Amikor pedig készen állsz, minden kimenetet zökkenőmentesen hozzárendelhetsz egy lézervezérlőhöz.

{% hint style="info" %}
A Liberationben tetszőleges számú lézert állíthatsz be és jeleníthetsz meg; a licencszintek (Hobbyist, Pro stb.) csak azt korlátozzák, hány lézert tudsz _élesíteni_. Ez azt jelenti, hogy akár ingyenes licenccel is tervezhetsz 100 lézeres show-t. Frissítésre csak akkor van szükség, amikor ténylegesen valódi lézereken szeretnéd futtatni.
{% endhint %}

Az alapértelmezett beállítás 8, vízszintesen elrendezett lézert tartalmaz, de ezt tetszés szerint módosíthatod. Amíg ismerkedsz a szoftverrel, valószínűleg érdemes megtartani ezt az alapbeállítást, később pedig hozzáigazíthatod a saját hardveres összeállításodhoz. (Lásd: [A projekt beállítása](setting-up/setting-up-your-project.md))

{% hint style="warning" %}
Fontos: Mielőtt bármilyen lézert élesítenél, győződj meg róla, hogy érted a kapcsolódó kockázatokat, és alaposan olvasd végig a [A lézerbeállítási folyamat áttekintése](setting-up/setting-up-lasers.md) fejezetet.
{% endhint %}

## A szoftver áttekintése

### Biztonsági leállítás

Amikor lézereket használsz, mindig legyen kéznél **hardveres vészleállító gomb** (lásd: [Vészleállítás / reteszelések](hardware/emergency-stop-interlocks.md)). Ha viszont kevésbé sürgősen szeretnél mindent hatástalanítani, használhatod a _**DISARM ALL**_ gombot vagy az `Escape` billentyűt (illetve az APC40-en a _**SESSION**_ gombot). A globális fényerőt a képernyőn látható csúszkával vagy az APC40 fő faderével is csökkentheted.

### Csúszkaelemek

A Liberationben több helyen találsz különböző csúszkákat és vezérlőket.

{% hint style="info" %}
Ha nagyobb pontosságra van szükséged, mint amit a csúszka ad, `Cmd / Ctrl`-kattintással beírhatsz egy új értéket.
{% endhint %}

### Billentyűparancsok

A billentyűparancsok teljes listája itt található: [Billentyűparancsok](reference/keyboard-shortcuts.md)

### Képernyőelrendezés

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nem vagy biztos benne, mire való egy adott gomb? Vidd fölé az egeret, és megjelenik a leírása!
{% endhint %}

#### Menü

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

A menüben találod a fájlimportálási és -exportálási lehetőségeket, valamint innen nyithatod meg a paneleket. Itt találod azt az opciót is, amellyel a számítógépet a feliratkozásodhoz engedélyezheted (_Liberation -> Authorise/Deauthorise this computer_).

#### Ikonsáv

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Itt találod a gyakori feladatokat, például az összes lézer élesítését/hatástalanítását, a globális fényerőt, a tesztábrát, valamint a 3D, Canvas és Output nézetek közötti váltást.

### Nézetek

A képernyő bal felső részén lévő nagy területen három fő nézet egyike jelenhet meg: **3D**, **CANVAS** és **OUTPUT.** Ezek között az ikonsáv gombjaival válthatsz (vagy a `Tab` billentyűvel válthatsz a 3D és az OUTPUT nézet között, majd tovább lépkedhetsz sorban az egyes lézerkimeneteken).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D nézet

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

A 3D nézet megmutatja, hogyan fognak kinézni a lézereid, és beállítható úgy, hogy a saját lézeres összeállításodnak feleljen meg. Kattints és húzd az egeret a kamera forgatásához, az egérgörgővel pedig előre-hátra mozgathatod a nézetet. Sok további opciót találsz a _3D Visualiser settings_ panelen (_View -> 3D Visualiser Settings_). Lásd: [3D Visualiser](setting-up/3d-visualiser.md).

#### Output nézet

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Az Output nézet az egyes lézerek zónáinak és maszkjainak beállítására szolgál. (Figyeld a bal felső sarokban lévő hatalmas számot, így könnyen látod, éppen melyik lézeren vagy!)

Ez a nézet az adott lézer teljes kimenetét mutatja, valamint azt, hogy az egyes zónák hol helyezkednek el benne. Alapértelmezetten lézerenként csak egy zóna van, de ésszerű keretek között tetszőleges számú zónát hozzáadhatsz, és mindegyiket látni fogod ebben a nézetben.

{% hint style="info" %}
**Mi az a zóna?**

A zóna a lézer kimenetén belüli olyan terület, amelybe lézertartalmat irányíthatsz. Egy lézerhez több zóna is tartozhat. A legegyszerűbb zónatípus a _beam_ zóna, de vannak _canvas_ zónák és _DMX_ zónák is. Ebben az útmutatóban főként a beam zónákra koncentrálunk, amelyeket általában a levegőben megjelenő atmoszférikus nyalábeffektek létrehozására használnak.
{% endhint %}

A szerkeszteni kívánt lézert az alábbi módokon választhatod ki:

* a felső sávban lévő számozott gombokkal
* a kívánt lézer számának billentyűjével _(1-9_ billentyűk\_)\_
* a `Tab` billentyűvel, amellyel sorban lépkedhetsz egyikről a másikra

Új lézert a _+_ gomb megnyomásával adhatsz hozzá az összeállításhoz. (A _Laser Overview_ panelen is van egy _ADD LASER_ gomb.)

Lézert az összeállításból a _Laser Overview_ panelen lévő piros ⊖ gombbal törölhetsz.

Az egérgörgővel nagyíthatsz és kicsinyíthetsz, a nézet mozgatásához pedig kattints és húzd bárhol, ahol nincs zóna.

Kattints egy zónára a kijelöléséhez, majd az egérrel állítsd a sarokpontjait. Ha húzás közben lenyomva tartod az `Alt / Option` billentyűt, a módosítás nem lesz egyenletes. Jobb kattintással további lehetőségeket láthatsz a zónához, például a zónatípus módosítását.

Bal oldalon egy ikongombokat tartalmazó sáv található; vidd az egeret bármelyik gomb fölé, hogy lásd, mire szolgál. Az itt lévő gombokkal beam zónákat, canvas zónákat és maszkokat adhatsz hozzá. Emellett beállíthatsz tesztábrát csak ehhez a lézerhez, valamint rács- és illesztési beállításokat is találsz.

További részletekért lásd: [Output nézet](output-view/).

#### Canvas

A Canvas rendszert főként grafikákhoz és építészeti mappinghez használják. Összetett képeket oszthatsz szét több lézer között, és minden szakaszt perspektívahelyesen korrigálhatsz. Lásd: [Grafika és a Canvas rendszer](graphics-and-the-canvas-system/).

### APC40 MIDI vezérlő

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Bár a Liberation egérrel és billentyűzettel is vezérelhető, sokkal jobb APC40 MIDI vezérlőfelületet használni (a Mark 2 a legjobb, de a Mark 1 is működik).

Lásd még: [APC40 referencia](reference/apc40-reference.md)

Mostanra az APC Mini Mark 2 és a MIDI Fighter Twister támogatását is megvalósítottuk, és további eszközök fejlesztése is folyamatban van. A legtöbb esetben azonban az APC40 Mark 2 a legjobb választás.

### Clipek és effektek

{% hint style="info" %}
**Mi az a clip?**

A clip a Liberationben bármilyen lézertartalom tárolója. A clipek tartalmazhatnak nyalábokat vagy grafikus animációkat, és általában ismétlődő ciklusként működnek. Bármely zónába (vagy _Canvas target area_ területre) irányíthatók, és a Clip Deck clip gombjaival indíthatók.
{% endhint %}

#### Clip Deck áttekintése

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Ezt a rácsot _Clip Decknek_ nevezzük, és itt tárolódik az összes lézerclip. Úgy készült, hogy közvetlenül megfeleljen az APC40 8 x 5 gombos rácsának.

**Navigálás a Clip Deckben.**

A Clip Decket balra és jobbra görgetheted az alábbi módokon:

* Bal és jobb nyílbillentyűk. A `Cmd / Ctrl` hozzáadásával egyszerre egy teljes oldalt görgethetsz.
* Trackpad: húzás
* Egér: ha az egered támogatja az oldalirányú görgetést, használhatod, amikor a Clip Deck fölött van az egérmutató
* APC40 scroll knob
* APC40 _<- DEVICE ->_ gombok

A tájékozódást a felül látható, kisméretű Clip Deck-vizualizáció segíti. Lásd még: [Clipek és Clip Deck](clips/)

#### Clipek indítása és leállítása

Egy clip elindításához nyomd meg a clip gombját (egérrel vagy az APC40-en). A leállításhoz nyomd meg újra. Amikor elindítasz egy clipet, az azonos színű összes többi clip automatikusan leáll, kivéve, ha lenyomva tartod a _shift_ billentyűt.

Egyes clipek _Flash mode_ módban lesznek (alapértelmezetten a pirosak); ezek azonnal leállnak, amint felengeded a clip gombját.

A _STOP_ gomb leállítja az összes éppen futó clipet.

#### A clip kimeneti zónáinak beállítása

A clip gombok alatt láthatók a zónagombok, alapértelmezetten az 1–8 beam zónák (_BEAM 1_, _BEAM 2_ stb.). A zónagombok világítással jelzik, mely zónák vannak hozzárendelve az aktuálisan kijelölt cliphez.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Két sorral a zónagombok alatt találod az X/Y tükröző gombokat; ezekkel vízszintesen és függőlegesen tükrözheted a clipet.

{% hint style="info" %}
Fontos, hogy ezek a zónahozzárendelések és X/Y tükrözési beállítások magához a cliphez tartoznak; a következő futtatáskor is megmaradnak. Nem globális beállítások.
{% endhint %}

Jobb kattintással további beállításokat szerkeszthetsz a cliphez. Lásd még: [Clip beállításai](clips/clip-settings.md)

### Csoportok

Észreveheted, hogy minden clipnek színes körvonala van, és ez a szín jelzi, melyik _csoportba_ tartozik. Az APC40 clip gombjai is ezzel a színnel világítanak.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cián</td></tr><tr><td>Group 2</td><td>Narancs</td></tr><tr><td>Group 3</td><td>Piros</td></tr><tr><td>Group 4</td><td>Indigó</td></tr><tr><td>Group 5</td><td>Zöld</td></tr></tbody></table>

A csoportrendszer nagyon rugalmas, és lehetővé teszi, hogy:

* az egyik csoport clipjei tovább fussanak, miközben egy másik csoportot kapcsolgatsz
* gyorsan zónákat és X/Y tükrözéseket rendelj egy csoport összes clipjéhez
* _Flash mode_ módot állíts be egy cliphez (a Group 3 alapértelmezetten _Flash mode_ módban van)

A csoportoknak be- és kifutási átmenetbeállításaik is vannak, amelyeket a clipek örökölhetnek, vagy felülírhatnak.

A clip csoportját a jobb kattintásos menü gombjaival állíthatod be, illetve APC40 használatakor megnyomhatod a group gombot, és _miközben továbbra is lenyomva tartod_, megnyomhatod a clip gombjait.

Zónabeállítások módosítása egy csoport összes clipjéhez

APC40 használatakor nyomd meg a group gombot, majd _miközben továbbra is lenyomva tartod_, a zóna- és X/Y gombokkal kapcsolhatod a csoport összes clipjének zónabeállításait.

Lásd még: [Clipcsoportok](clips/groups.md)

### Effektek

A Liberation effektrendszere nagy teljesítményű és sokoldalú módja annak, hogy valós időben módosítsd a clip kimenetét. Az alapértelmezett 1–8 effektgombok a zónagombok alatt találhatók.

#### Effekt alkalmazása

Nyomj meg egy effektgombot az effekt ki- vagy bekapcsolásához, de még jobb, ha az APC40 1–8 csúszkáival úsztatod be és ki az effekteket.

#### Effektparaméterek

Az 1–8 forgóvezérlővel\* állíthatod az egyes effektek _paraméterét_. (Vagy jobb kattintással egérrel is állíthatod a szintet és a paramétert.) A paraméter módosítása attól függően mást és mást csinál, hogyan van beállítva az effekt. Az alapértelmezett effekteket az alábbi lista tartalmazza.

{% hint style="info" %}
Az effektgombokon látható kis számok az effekt _level_ és _parameter_ értékeire utalnak. A _level_ értéket az APC40 faderével szabályozhatod, vagy kattintás-húzással a gombon. A paramétert az APC40 forgóvezérlőivel állíthatod, vagy jobb kattintással egérrel módosíthatod.
{% endhint %}

_\*Az 1–8 forgóvezérlő az APC40 Mk2 tetején, az Mk1-en pedig jobb felül található. Lásd még:_ [APC40 referencia](reference/apc40-reference.md)

#### Az alapértelmezett effektek

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Kaotikus mozgást alkalmaz a clip kimenetére. A paraméter a káosz mértékét/sebességét állítja.
2. **Sine wave** :\
   Az összes tartalmat egy mozgó szinuszhullám mentén torzítja. A paraméter a hullámhosszt állítja.
3. **Rotation** :\
   Mindent körbeforgat. A paraméter a forgási sebességet állítja.
4. **Horizontal flip** :\
   Vízszintesen összenyomja és széthúzza az összes tartalmat. A paraméter a sebességet állítja.
5. **Scale** :\
   Ismételten teljes méretről nullára méretezi az összes tartalmat. A paraméter a sebességet állítja.
6. **Hue** :\
   Megváltoztatja minden tartalom árnyalatát, de a telítettséget nem módosítja (vagyis ami fehér, fehér marad). A paraméter az árnyalatot állítja.
7. **Saturation and hue** :\
   Megváltoztatja minden tartalom árnyalatát, és teljesen telíti a színt is (vagyis ami fehér, az is színessé válik). A paraméter az árnyalatot állítja.
8. **Flash** :\
   Ismételten teljes értékről nullára villogtatja minden tartalom fényerejét. A paraméter a villogás sebességét állítja.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Az alsó sorban további 16 színeffekt található, amelyek előre beállított árnyalat- és telítettségértékeket alkalmaznak.

Fontos, hogy ezek az alapértelmezett effektek, de szinte bármire átszerkeszthetők, amire szükséged van!

#### Mi az _„aktuálisan kijelölt clip”_?

Amikor elindítasz egy clipet, világítani kezd, jelezve, hogy aktív. Emellett fehér körvonala is lesz, ami azt mutatja, hogy ez az aktuálisan _kijelölt_ clip. Amikor zónagombokat kapcsolsz vagy a clip beállításait módosítod, ezek az _aktuálisan kijelölt clipre_ érvényesek.

{% hint style="info" %}
Ha egy clipet az elindítása nélkül szeretnél kijelölni, nyomd le az `Alt / Option` billentyűt, mielőtt megnyomod a clip gombját. Ez jó módszer a zónák és egyéb beállítások módosítására anélkül, hogy a clip futna.
{% endhint %}

### Clip Settings panel

A _Clip Settings_ panelen szerkesztheted a méretezést, az X/Y pozíciót, és innen érheted el a hatékony zónakésleltetési rendszert.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings panel

A _Global Settings_ panelen módosíthatod azokat a globális kimeneti beállításokat, amelyek minden zónában az összes kimenetre hatással vannak.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Kapcsold be az AUTO RESET opciót, hogy amikor nem fut clip, az összes _Global settings_ automatikusan visszaálljon.

### Időzítés

Szinte minden lézeres megjelenítéshez tartozik valamilyen zenei kíséret, ezért a Liberation időzítési rendszere percenkénti ütésszámon alapuló tempót használ. A _Tempo Panel_ panelen az idő megjelenítését látod; minden négyzet egy ütemet jelöl, és időben villog.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Több szinkronizálási lehetőség is elérhető, például MIDI clock és Ableton Link. Ha ismered a zene tempóját, manuálisan is beállíthatod a képernyőn lévő csúszkával vagy az APC40 Tempo knob vezérlőjével, de a _Tap Tempo_ rendszerrel a zenéhez is igazíthatod\_.\_

#### Tap Tempo

A _Tap Tempo_ gyakori kifejezés a zenei alkalmazásokban; segítségével a zene lejátszása közben az ütemre koppintva állíthatod be a tempót. Használhatod a képernyőn lévő gombot, de ajánlott inkább a _T_ billentyűt vagy az APC40 _Tap Tempo_ gombját használni (vagy akár lábkapcsolót, ha azt részesíted előnyben).

A tempó ütem elejére állításához nyomd meg az _R_ billentyűt vagy az APC40 _Metronome_ gombját.

A tempó egész számra kerekítéséhez nyomd meg az _Y_ billentyűt, vagy fordítsd el az APC40 _Tempo_ knob vezérlőjét. Ez hasznos lehet elektronikus zenénél, ahol a percenkénti ütésszám gyakran egész szám.

### A Clip Deck rendszerezése

Egy clip áthelyezéséhez a Clip Decken kattints rá, és húzd az új pozícióba. Húzás közben a kurzorbillentyűkkel (vagy az APC40 görgőjével/gombjaival) balra és jobbra görgethetsz.

Másolat készítéséhez húzás közben tartsd lenyomva az `Alt / Option` billentyűt.

`Alt / Option`-kattintással elindítás nélkül kijelölhetsz egy clipet.

`Alt / Option + Shift`-kattintással több clipet jelölhetsz ki, vagy kattints és húzz egy clipen kívül, hogy „lasszóval” jelölj ki.

A kattintás és húzás az ÖSSZES kijelölt clipet húzza.

Egy vagy több clip törléséhez húzd őket le a Clip Deckről (megjelenik egy kuka ikon), vagy használd a DELETE gombot a clip jobb kattintásos menüjében.

### Laser Overview panel

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

A _Laser Overview panel_ gyors áttekintést ad az aktuálisan futó lézereid állapotáról. A jobb oldali zöld négyzet azt jelzi, hogy a lézervezérlő rendben működik. Ha narancssárgára vált, időnkénti adatkimaradások vannak, ha pirosra, akkor megszakadt a kapcsolat. Ha szürke, akkor egyáltalán nincs vezérlőhöz csatlakoztatva.

A középső grafikon a képkockahosszak előzményeit mutatja, a jobb oldali szám pedig az aktuális képfrissítési sebesség. Minél összetettebb a tartalom, annál lassabb lesz a képfrissítés (vagyis annál villódzóbbnak tűnhet). Körülbelül 25 fps alatt már kissé villódzónak fog látszani.

### Csatlakozás lézerekhez – Controller Assignment panel

Kattints az _Assign Laser Controllers_ gombra a _Controller Assignment_ panel megnyitásához. (Ez a panel a menüsávban a _View -> Controller Assignment_ útvonalon is elérhető.)

Itt választhatod ki, mely lézerkimenetek mely lézervezérlőkre menjenek. Húzd át a vezérlőket a jobb oldali listából a bal oldali helyekre. A vezérlőket át is nevezheted annak megfelelően, melyik lézerhez vannak párosítva (használd a toll ikon gombot).

További részletekért olvasd el a [Vezérlő-hozzárendelés](setting-up/controller-assignment.md) fejezetet.

{% hint style="danger" %}
Mielőtt bármilyen lézert élesítenél, mindenképpen menj végig a [A lézerbeállítási folyamat áttekintése](setting-up/setting-up-lasers.md) fejezeten.
{% endhint %}

### Laser Output panel

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Ez a panel az _aktuálisan kijelölt lézer_ beállításait mutatja (felül a szám jelzi). Az aktuálisan kijelölt lézert a _tab_ billentyűvel, egy számbillentyű megnyomásával, a _Laser Overview_ panelen lévő lézerszámra kattintva, vagy az _output view_ nézetben válthatod.

* **Number button** élesíti és hatástalanítja a lézert; ha piros, a lézer élesítve van.
* **Brightness** a többi lézertől függetlenül állítja a lézer fényerejét (és összeadódik a _global brightness_ beállítással – vagyis ha mindkettő 50%, a lézered 25%-on lesz).
* **Test Pattern** bekapcsol egy tesztábrát csak ehhez a lézerhez (felülírja a globális tesztábra-beállítást).
* **Orientation** korrigálja az oldalra vagy fejjel lefelé szerelt lézereket.
* **Flip Horizontal and Flip Vertical** megfordítja a lézer kimenetét. Hasznos a nem egységesen bekötött lézerek kimeneti korrekciójához.
* **Copy Laser Settings** megnyit egy panelt, amelyen különböző beállításokat másolhatsz erről a lézerről más lézerekre.

### Scanner beállítások

A display lézerek úgy működnek, hogy egyetlen lézernyalábot rendkívül gyorsan mozgatnak, miközben ki- és bekapcsolják, így rajzolnak alakzatokat a levegőbe. Amit vonalakként, formákként és képekként látsz, valójában az a nyaláb útvonala, amelyet gyorsabban rajzol végig, mint ahogy a szemed követni tudná.

A pontfolyam az az adat, amely megmondja a lézernek, hová mozduljon legközelebb, és mikor legyen a nyaláb be- vagy kikapcsolva. A Liberationben a clipek valós időben alakulnak át ezzé a pontfolyammá, miközben a lézerek felé küldésre kerülnek.

A Liberation részletes vezérlést ad afölött, hogyan jön létre ez a pontfolyam, így minden lézernél egyensúlyba hozhatod a simaságot, a fényerőt és a teljesítményt.

{% hint style="info" %}
Ha olyan régebbi lézerszoftverhez vagy szokva, amely előre kiszámított pontfolyamokra támaszkodik, ez a megközelítés elsőre eltérőnek tűnhet. A valós idejű pontgenerálás azonban lehetővé teszi, hogy ugyanazt a tartalmat minden lézerhez másképp optimalizáld. Így könnyebb több, eltérő scannersebességű vagy minőségű lézerrel dolgozni anélkül, hogy duplikálnod vagy újraépítened kellene a tartalmat. Emellett a clipfájlok is nagyon kicsik maradnak, ezért a teljes alapértelmezett Liberation Clip Deck csak néhány megabájt, nem pedig gigabájtok.
{% endhint %}

Az alapvető scanner beállítások:

* **Speed** a scanner sebessége, vagyis hogy milyen gyorsan mozog a lézer az alakzatok kirajzolásához. Ez a hagyományos lézerszoftverekben a pontsebesség állításának felel meg, de a Liberationben a lézer mozgási sebességét _a pontsebességtől függetlenül_ módosíthatod. Ezt általában nem szükséges állítanod.
* **Scanner sync** (néha _blank shift_, korábban Colour Shift néven ismert) A scannerek nagyon gyorsan mozgatják a lézert, de a fényerő- és színváltozás általában nincs szinkronban a mozgással. Ez kis villódzó fény-„farokként” jelenik meg a nyalábok és vonalak szélén. Ezzel a beállítással hozhatod szinkronba a mozgást és a színt. Lásd: [Laser output beállítási panel](setting-up/laser-settings.md)

A többi haladó scanner beállítást az [Haladó](advanced/) fejezet ismerteti.

### Zónázás

A lézerek beállításának és zónázásának teljes útmutatójáért lásd: [A lézerbeállítási folyamat áttekintése](setting-up/setting-up-lasers.md)
