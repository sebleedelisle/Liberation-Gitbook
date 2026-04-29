---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Színkalibrálás

A színkalibrálás biztosítja, hogy a projektor vörös, zöld és kék lézerei minden fényerőszinten egyenletesen és kiszámíthatóan adjanak fényt. A különböző projektorok fényerőgörbéje nem feltétlenül lineáris, vagyis az 50% vörös sokkal világosabbnak vagy sötétebbnek tűnhet, mint a 100% vörös fényerejének fele. A kalibrálás ezt korrigálja, így a színek tisztán keverednek, az átmenetek simák lesznek, a fehér pedig kiegyensúlyozott marad.

#### A projektor bemelegítése

A lézerdiódák működése változik, ahogy bemelegszenek. Kalibrálás előtt mindig hagyd stabilizálódni a projektort:

* Vetíts ki egy világos képet, például a **White rectangle test pattern (11)** mintát legalább **15–20 percig**.
* Így a beállított színegyensúly az előadás közben is következetes marad.

#### Hogyan működik a kalibrációs teszt

A kalibráláshoz használd a tesztmintákat (lásd: [Tesztábrák](../output-view/test-patterns.md))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Mindegyik minta négy mozgó vonalat jelenít meg:

* **Felső vonal** – 100% fényerő teljes sebességen
* **Második vonal** – 75% fényerő 75% sebességen
* **Harmadik vonal** – 50% fényerő 50% sebességen
* **Negyedik vonal** – 25% fényerő 25% sebességen

Mivel a fényerő _és a sebesség_ együtt skálázódik, a vonalaknak azonos fényerejűnek kell látszaniuk. Ha valamelyik világosabbnak vagy sötétebbnek tűnik, állítsd a megfelelő csúszkát, amíg egyezni nem fognak.

Minden tesztmintában van egy ötödik vonal is **0% fényerőn**, amelynek nem szabad látszania. Ez azoknak a lézereknek a korrigálására szolgál, amelyek nagyon alacsony szinteken még nem adnak ki fényt. Ha a lézer alacsony fényerőn továbbra sem látható, fokozatosan növeld a **0% setting** értékét, amíg a vonal éppen meg nem jelenik, majd vedd vissza kissé, amíg újra eltűnik. A cél annak a küszöbnek a megtalálása, ahol a lézer elkezd világítani, majd éppen ez alatt maradni – így az elhalványulások természetesen indulnak, anélkül hogy az alsó tartomány levágódna.

#### A Colour Calibration panel használata

A panel külön vezérlést ad minden csatornához (vörös, zöld, kék) a 100, 75, 50, 25 és 0%-os szinteken.

1. **Válassz ki egy tesztmintát** (kezdd a vörössel).
2. **Állítsd a csúszkákat** úgy, hogy a 100, 75, 50 és 25%-os vonalak azonos fényerejűnek látszódjanak.
3. **Finomhangold a 0%-os csúszkát**, ha a „kikapcsolt” vonal még halványan látható.
4. **Ismételd meg zölddel és kékkel.**
5. Válts a **White test pattern (8)** mintára. Mind a négy vonalnak egyformának kell látszania, a fehérnek pedig semlegesnek kell tűnnie, elszíneződés nélkül.

#### A fehéregyensúly beállítása

Ezzel a rendszerrel a **fehéregyensúlyt** is beállíthatod. Miután az egyes csatornákat külön kalibráltad, válts a **White test pattern (8)** mintára. Ha a kimenet elszínezettnek tűnik (például túl zöld vagy túl kék), állítsd a vörös, zöld és kék csatornák egymáshoz viszonyított szintjeit, amíg a vonalak semleges fehérnek nem látszanak. Még akkor is, ha a lézereid teljesítménye jelentősen eltér, a kalibrálás segít közelebb hozni őket egymáshoz, és tisztább, kiegyensúlyozottabb színkeverést eredményez.

#### A kalibrálás mentése

* A **Store** felülírja az aktuális presetet.
* A **Store As** új presetet hoz létre; ez hasznos, ha több lézerrel dolgozol.
