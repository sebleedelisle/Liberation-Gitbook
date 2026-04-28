---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Mi a teendő, ha a Liberation nem nyílik meg?

Ritkán fordul elő, de előfordulhat, hogy a Liberation nem indul el, vagy közvetlenül megnyitás után összeomlik. Ezt szinte mindig az okozza, hogy az egyik helyi konfigurációs fájl megsérült – általában egy rendszerösszeomlás vagy valamilyen váratlan számítógépes esemény után.

Szerencsére a helyi beállítások visszaállításával ez könnyen javítható. Az alábbiakban macOS és Windows rendszeren is bemutatjuk a lépéseket.

> **Fontos**
>
> * Mielőtt bármit tenne, zárja be a Liberation alkalmazást.
> * Ezek a lépések csak a helyi beállításokat, naplókat és gyorsítótárakat érintik. A licence és a fiókja biztonságban marad.

***

#### Hol található a munkamappa?

A Liberation minden verziójának saját munkamappája van. Ha például az 1.0.0 verziót használja, a mappa neve 1.0.0 lesz.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**A mappa gyors megnyitása**

**macOS**

1. A Finderben nyomja meg a **Shift + Cmd + G** billentyűkombinációt.
2.  Illessze be ezt az elérési utat, majd nyomja meg az **Enter** billentyűt:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Nyissa meg a verziószámának megfelelő mappát, például: `1.0.0`.

**Windows**

1.  Nyomja meg a **Win + R** billentyűkombinációt, illessze be ezt, majd nyomja meg az **Enter** billentyűt:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Nyissa meg a verziószámának megfelelő mappát, például: `1.0.0`.

> **Tipp Windowshoz**: Ha a File Explorerben böngészi a mappákat, kapcsolja be a rejtett elemek megjelenítését: **View > Show > Hidden items**.

***

#### 1. lépés – A beállításfájl biztonságos visszaállítása

A verziómappán belül nyissa meg ezt:

```
data/liberation/
```

A liberation mappában egy se`ttings.json` nevű fájlt kell találnia. Törölje ezt a fájlt.

* **macOS példa**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows példa**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Most próbálja meg elindítani a Liberation alkalmazást. Ha megnyílik, ezzel készen is van.

***

#### 2. lépés – Ellenőrizze, nincs-e problémás clip

Ha a Liberation egy clip szerkesztése közben omlott össze, lehetséges, hogy magával a clip fájllal van probléma.

Ugyanabban a mappában, ahol a settings.json fájl található, egy clipEdit`.json` nevű fájlt kell találnia.

Készítsen biztonsági mentést erről a fájlról egy biztonságos helyre (például a Desktopra), majd törölje a Liberation munkamappájából.

Próbálja meg újra elindítani a Liberation alkalmazást. Ha most már rendben megnyílik, kérjük, küldje el e-mailben a biztonsági mentést a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) címre, hogy meg tudjuk vizsgálni, mi okozta a problémát.

***

#### 3. lépés - Készítsen biztonsági mentést, majd törölje a teljes munkamappát

Ha az 1. és a 2. lépés nem segített:

1. **Készítsen biztonsági mentést** a teljes verziómappáról:
   * macOS: Kattintson jobb gombbal az `1.0.0` mappára, és válassza a **Compress** lehetőséget egy zip fájl készítéséhez, vagy másolja át egy biztonságos helyre, például a Desktopra.
   * Windows: Kattintson jobb gombbal az `1.0.0` mappára, és válassza a **Send to > Compressed (zipped) folder** lehetőséget, vagy másolja át egy biztonságos helyre, például a Desktopra.
2. A biztonsági mentés elkészítése után **törölje** az eredeti `1.0.0` mappát a Liberation munkamappa-helyéről.
3. Indítsa el újra a Liberation alkalmazást. Ez létrehoz egy új, tiszta munkamappát.

Ha a Liberation most megnyílik, folytassa a 4. lépéssel.

***

#### 4. lépés - Küldje el nekünk a biztonsági mentést

Ez segít azonosítani, mi okozta a problémát, hogy a jövőbeli verziókban megelőzhessük.

Ha még nem tette meg, tömörítse zip fájlba a 3. lépésben készített **biztonsági mentést**, majd küldje el e-mailben, hogy diagnosztizálni tudjuk az okot.

* **Címzett**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Tárgy**: Liberation indítási javítás - munkamappa biztonsági mentése
* **Szöveg**: Kérjük, adja meg:
  * Operációs rendszer és verzió (pl. macOS 14.6 vagy Windows 11 23H2)
  * Liberation verzió (pl. 1.0.0)
  * Melyik lépés oldotta meg a problémát, ha valamelyik (1., 2. vagy 3. lépés)
  * Rövid leírás arról, mi történt a probléma kezdete előtt
* **Melléklet**: az `1.0.0` munkamappa zip fájlba tömörített biztonsági mentése.

> Ha a zip túl nagy e-mailhez, töltse fel egy felhőalapú tárhelyre, és osszon meg egy linket.

***

#### A 3. lépés után sem indul el?

Ha a Liberation a munkamappa törlése után sem nyílik meg:

* Indítsa újra a számítógépet, majd próbálja meg újra.
* Ideiglenesen kapcsolja ki azokat a vírusirtó vagy biztonsági eszközöket, amelyek blokkolhatják az új mappák létrehozását, majd próbálja meg elindítani.
* Telepítse újra a Liberation legújabb buildjét a meglévő telepítésre.
* Ha a fentiek egyike sem segít, vegye fel a kapcsolatot a támogatással a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) címen, és küldje el a részleteket, valamint a `logs` almappában található esetleges összeomlási naplókat.

***

#### Összefoglalás

1. Törölje a `data/liberation/settings.json` fájlt a verziószámozott munkamappából.
2. Ha clipet szerkesztett, készítsen biztonsági mentést, majd törölje a `data/liberation/clipEdit.json` fájlt.
3. Ha továbbra sem nyílik meg, készítsen biztonsági mentést, majd törölje a teljes `1.0.0` (vagy az Ön verziójának megfelelő) mappát.
4. Ha a 3. lépés megoldja a problémát (vagy ha nem), tömörítse zip fájlba a biztonsági mentést, és küldje el a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) címre az operációs rendszer és a Liberation verzió megadásával.
