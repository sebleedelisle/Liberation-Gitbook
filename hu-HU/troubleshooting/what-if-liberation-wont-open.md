---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Mi a teendő, ha a Liberation nem nyílik meg?

Ritkán fordul elő, de előfordulhat, hogy a Liberation nem indul el, vagy közvetlenül megnyitás után összeomlik. Ennek szinte mindig az az oka, hogy valamelyik helyi konfigurációs fájl megsérült — általában rendszerösszeomlás vagy valamilyen váratlan számítógépes hiba után.

Szerencsére ez könnyen javítható a helyi beállítások alaphelyzetbe állításával. Így teheted meg macOS és Windows alatt.

> **Fontos**
>
> * Zárd be a Liberation alkalmazást, mielőtt bármit csinálsz.
> * Ezek a lépések csak a helyi beállításokat, naplókat és gyorsítótárakat érintik. A licenced és a fiókod biztonságban van.

***

#### Hol találod a munkamappát?

A Liberation minden verziójához külön munkamappa tartozik. Ha például az 1.0.0 verziót használod, a mappa neve 1.0.0 lesz.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**A mappa gyors megnyitása**

**macOS**

1. Finderben nyomd meg a **Shift + Cmd + G** billentyűket.
2.  Illeszd be ezt az útvonalat, majd nyomd meg az **Enter** billentyűt:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Nyisd meg a verziószámodnak megfelelő mappát, például: `1.0.0`.

**Windows**

1.  Nyomd meg a **Win + R** billentyűket, illeszd be ezt, majd nyomd meg az **Enter** billentyűt:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Nyisd meg a verziószámodnak megfelelő mappát, például: `1.0.0`.

> **Tipp Windowshoz**: Ha inkább File Explorerben keresed meg, kapcsold be a rejtett elemek megjelenítését: **View > Show > Hidden items**.

***

#### 1. lépés – A beállításfájl biztonságos alaphelyzetbe állítása

A verziómappádon belül nyisd meg ezt:

```
data/liberation/
```

A liberation mappában találnod kell egy `settings.json` nevű fájlt. Töröld ezt a fájlt.

* **macOS példa**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows példa**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Most próbáld meg elindítani a Liberation alkalmazást. Ha megnyílik, kész vagy.

***

#### 2. lépés – Ellenőrizd, hogy nem egy problémás Clip okozza-e

Ha a Liberation akkor omlott össze, amikor egy Clip szerkesztése közben voltál, lehet, hogy az adott Clip fájlban van valami, ami a problémát okozza.

Ugyanabban a mappában, ahol a settings.json fájl található, találnod kell egy `clipEdit.json` nevű fájlt.

Készíts biztonsági másolatot erről a fájlról egy biztonságos helyre (például az Asztalra), majd töröld a Liberation munkamappájából.

Próbáld meg újra elindítani a Liberation alkalmazást. Ha most már rendben megnyílik, kérjük, küldd el e-mailben a biztonsági másolatot a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) címre, hogy kivizsgálhassuk, mi okozta a hibát.

***

#### 3. lépés - Készíts biztonsági másolatot, majd töröld a teljes munkamappát

Ha az 1. és 2. lépés nem segített:

1. Készíts **biztonsági másolatot** a teljes verziómappáról:
   * macOS: Kattints jobb gombbal a `1.0.0` mappára, és válaszd a **Compress** lehetőséget zip fájl készítéséhez, vagy másold át egy biztonságos helyre, például az Asztalra.
   * Windows: Kattints jobb gombbal a `1.0.0` mappára, és válaszd a **Send to > Compressed (zipped) folder** lehetőséget, vagy másold át egy biztonságos helyre, például az Asztalra.
2. A biztonsági mentés után **töröld** az eredeti `1.0.0` mappát a Liberation munkamappa helyéről.
3. Indítsd el újra a Liberation alkalmazást. Létre fog hozni egy friss munkamappát.

Ha a Liberation most megnyílik, folytasd a 4. lépéssel.

***

#### 4. lépés - Küldd el nekünk a biztonsági másolatot

Ez segít azonosítani, mi okozta a hibát, hogy a jövőbeli verziókban megelőzhessük.

Ha még nem tetted meg, tömörítsd zip fájlba a 3. lépésben készült **biztonsági másolatot**, majd küldd el e-mailben, hogy meg tudjuk állapítani az okot.

* **Címzett**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Tárgy**: Liberation start-up fix - working folder backup
* **Üzenet**: Kérjük, add meg:
  * Operációs rendszer és verzió (pl. macOS 14.6 vagy Windows 11 23H2)
  * Liberation verzió (pl. 1.0.0)
  * Melyik lépés oldotta meg, ha valamelyik (1., 2. vagy 3. lépés)
  * Rövid leírás arról, mi történt a probléma kezdete előtt
* **Melléklet**: a `1.0.0` munkamappa zip formátumú biztonsági másolata.

> Ha a zip túl nagy e-mailhez, töltsd fel egy felhőmeghajtóra, és ossz meg egy linket.

***

#### A 3. lépés után sem indul?

Ha a Liberation a munkamappa törlése után sem nyílik meg:

* Indítsd újra a számítógépet, és próbáld meg újra.
* Ideiglenesen kapcsold ki azokat a vírusirtókat vagy biztonsági eszközöket, amelyek blokkolhatják az új mappák létrehozását, majd próbáld meg elindítani.
* Telepítsd újra a legújabb Liberation buildet a meglévő telepítés fölé.
* Ha a fentiek egyike sem működik, vedd fel a kapcsolatot a támogatással a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) címen, és küldd el a részleteket, valamint az esetleges összeomlási naplókat a `logs` almappából, ha vannak ilyenek.

***

#### Összefoglaló

1. Töröld a `data/liberation/settings.json` fájlt a verziózott munkamappádból.
2. Ha Clip szerkesztése közben voltál, készíts biztonsági másolatot a `data/liberation/clipEdit.json` fájlról, majd töröld.
3. Ha továbbra sem nyílik meg, készíts biztonsági másolatot, majd töröld a teljes `1.0.0` mappát (vagy a saját verziód mappáját).
4. Ha a 3. lépés megoldja (vagy ha nem oldja meg), tömörítsd zip fájlba a biztonsági másolatot, és küldd el a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) címre az operációs rendszered és a Liberation verzió megadásával.
