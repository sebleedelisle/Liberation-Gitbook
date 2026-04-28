---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Scanner-specifikációk és Liberation

### A scanner-specifikációk zavaros valósága

A pontsebességek és a scanner-specifikációk könnyen félreérthetők. Gyakran láthatsz olyan adatokat, mint 30kpps @ 8º vagy 50kpps @ 4º, de nem mindig egyértelmű, hogy ezek a számok valójában mit jelentenek.

{% hint style="info" %}
Nyilatkozat – nem vagyok scanner hardverspecialista, de sok év gyakorlati tapasztalatom van abban, hogyan lehet különböző minőségű scannerek képét szoftveresen és pontfolyam-generálással javítani, hardveres hangolás helyett. Az alábbiak ezen a tapasztalaton alapulnak.
{% endhint %}

#### **Honnan származnak ezek a számok**

A „30K” és „50K” kifejezések rövidítések, amelyek arra épülnek, hogy a scannereket az ILDA tesztábrával értékelik az adott pontsebességen, meghatározott feltételek mellett.

Amikor egy scannert például így adnak meg: _30Kpps @ 8°_, az valójában ezt jelenti:

> „Ez a scanner megfelelő hangolás mellett képes az ILDA tesztábrát 30 000 pont/mp sebességgel, 8°-os pásztázási szögön megjeleníteni.”

Ez nem átfogó vagy teljesen szabványosított mérőszáma a valós teljesítménynek. Valójában eredetileg nem is benchmarknak készült – egy **hangolási eljárás** részeként használták. Egy ismert mintát futtatsz fix pontsebességgel (pl. 30 000 pont/mp), majd addig állítod a csillapítást és az erősítést, amíg helyesen nem néz ki.

Ennek ellenére továbbra is ez a legelterjedtebb viszonyítási alap, és jó képet adhat a scannerek minőségéről, legalábbis megbízható gyártók esetén. A _kevésbé megbízható_ gyártóknál viszont...

#### Ha a scannereket a megadott értékelésük szerint szeretnéd tesztelni

{% hint style="danger" %}
**Ez haladó technika, és ha nem vagy óvatos, kárt tehetsz a scannerekben. Nem ajánlott, hacsak nem tudod pontosan, mit csinálsz.**
{% endhint %}

Olyan szoftverre lesz szükséged, amely képes kiadni az [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) ábrát – úgy tudom, a LaserShowGen talán képes erre –, majd a kimeneti méretet a megadott pásztázási szöghöz kell igazítanod (pl. 8°). A kimenet elemzéséhez lásd az ILDA dokumentációját.

#### Miért nem feltétlenül jó benchmark

Először is, a tesztábra akkor is hibásan jelenhet meg, ha a scannerek jók, egyszerűen azért, mert nincsenek kifejezetten erre optimalizálva hangolva.

Hasznos általános támpont lehet a „jó” és „rossz” scannerek megkülönböztetésére, de a gyártók néha meglehetősen lazán kezelik ezeket a specifikációkat.

#### Akkor hogyan válasszak jó scannert?

Szerintem a legfontosabb, hogy megbízható gyártótól származzanak. A drága, felső kategóriás scanner-gyártók, például a Cambridge Technology (CT), az Eye Magic (EMS) és a ScannerMAX (a Pangolin leányvállalata) mindig jó választások, ezekkel nem nagyon lehet mellényúlni. De amikor egy scannerpár ára körülbelül 1000 dollár, sok kezdő számára ez drágább, mint maga a lézer!

Ezért én többnyire kínai gyártókat használtam. A Dragon Tiger (DT) scannerek tisztességesek és megfizethetők, és úgy tudom, a LightSpace is ezeket használja. Sok más gyártó (köztük egyes OPT és Able modellek) szintén DT-alapú rendszereket használ.

A Phenix Technology (PT) általában alacsonyabb kategória, de őszintén szólva a legtöbb dologra valószínűleg megfelelnek.

**Ha a scannerek márkajelzés nélküliek, akkor érdemes igazán aggódni a minőség miatt!**

#### Hogyan segít a Liberation

Először is: a legtöbb feladathoz nincs szükséged igazán drága scannerekre! A megfizethető 30kpps DT, vagy akár PT scannerek is megfelelőek lesznek. Az alapértelmezett scanner-beállítások szándékosan óvatosak, és többnyire _nem kell módosítanod őket_ (a _Scanner sync_ kivételével).

Még ha jobb scannereid is vannak, nincs értelme jobban terhelni őket, mint amennyire szükséges. Ez jelentősen meghosszabbítja az élettartamukat.

#### Mi az a „pontfolyam”?

Valószínűleg hallottad már ezt a kifejezést – így vezéreljük a scannerek útvonalát.

A pontfolyam X/Y pozíciók listája, ahol minden ponthoz szín is tartozik. Ha például egy fehér vonalat szeretnél rajzolni, pontok sorozatát küldöd a vonal mentén, mindegyiket fehérre állítva. A scannerek ezután pontról pontra mozognak fix sebességgel – ez a pont/mp sebesség (PPS) –, és a nyaláb kirajzolja az alakzatot.

#### Hogyan működik ez a hagyományos lézerszoftverekben

A hagyományos lézerszoftverek minden cue-hoz eltárolnak egy pontfolyamot. Animált cue-k esetén ez általában minden képkockához külön pontfolyamot jelent. A lényeg, hogy minden teljesen előre meghatározott. Ennek következtében a pontsebesség növelése azt eredményezi, hogy a scannerek gyorsabban haladnak végig ugyanazon az előre meghatározott adaton.

{% hint style="info" %}
Régebbi szoftvereknél ez a megközelítés szükséges volt – a számítógépek egyszerűen nem voltak elég gyorsak ahhoz, hogy valós időben generáljanak pontfolyamokat. Ezért van általában külön cue-szerkesztő, amellyel előre legenerálható az animáció minden képkockájának adata.

Ez azt is megmagyarázza, miért foglalhatnak a tartalmak gigabájtnyi helyet. Lényegében nagy, tömörítetlen hullámformákat tárolsz meglehetősen magas mintavételi frekvencián.
{% endhint %}

#### Miért kevésbé jelentős a „pontsebesség” a Liberationben

A Liberation valós időben generálja a pontfolyamot, ami rengeteg rugalmasságot ad. Figyeld meg a "Scanner speed" beállítást a Laser Settings panelen. Ezzel gyorsíthatjuk és lassíthatjuk a scannereket, de fontos, hogy **nem** változtatja meg az alapul szolgáló pontsebességet (PPS).

#### Várj, mi? Hogyan?

Tudom, elsőre furcsán hangzik.

Mivel a Liberation valós időben generálja a pontfolyamot, ezt a pontfolyamot menet közben tudja módosítani. Minél távolabb vannak egymástól a pontok, annál gyorsabban mozognak a scannerek. Minél közelebb vannak egymáshoz, annál lassabban mozognak.

{% hint style="info" %}
A Liberation újabb verzióiban a tényleges _pontsebesség_ (a haladó beállításokban) egyáltalán nem befolyásolja a scanner sebességét. Ehelyett a renderelő a ponteloszlást igazítja a kiválasztott pontsebességhez, miközben a scannerek mozgása változatlan marad.

Ez hatással van a pontútvonal „felbontására”, de ennek főként grafikáknál van jelentősége (és segíthet a _scanner sync_ beállítás finomabb igazításában).
{% endhint %}

#### Remek! Akkor mit jelent mindez a gyakorlatban?

Jó kérdés. Íme a tippjeim:

* Kerüld a márkajelzés nélküli scannereket. Ha tudsz gyorsabb scannereket venni, tedd meg – legalább 30KPPS legyen.
* A legtöbb esetben a DT30 scannerek megfelelőek, az olcsóbb lézerekben pedig a PT30 scannerek is valószínűleg rendben lesznek.
* Ha grafikákkal dolgozol, a legtöbb esetben több lézer többet számít, mint a gyorsabb scannerek.
* Ha már felsőbb kategóriás rendszerekről van szó, bármelyik elismert prémium márka megfelelő lesz.
* Ha csak a legolcsóbb, márkajelzés nélküli scannereket tudod beszerezni, a Liberation alapértelmezett beállításai elég óvatosak, és alap beam munkákhoz valószínűleg elfogadható eredményt kapsz. Ha nehezen boldogul, csökkentsd a **Speed** beállítást (de ne változtasd meg a pontsebességet!).

#### És az ILDA Test Pattern?

…továbbra is nagyon hasznos kalibrációs és viszonyítási eszköz, de soha nem átfogó benchmarknak tervezték, és a gyártók könnyen félrehasználhatják vagy lazán értelmezhetik.
