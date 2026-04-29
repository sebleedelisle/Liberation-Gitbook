---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Hardver

#### **Fut a Liberation Windows alatt?**

Igen – a Liberation teljes mértékben támogatja a **Windows 10 és 11 (64 bites)** rendszereket, pontosan ugyanazokkal a funkciókkal, mint a Mac verzió. Minden kiadás egyszerre jelenik meg mindkét platformra.

#### **Fut a Liberation Macen?**

Igen – a Liberation teljes mértékben támogatja a **Mac rendszereket (macOS 12 Monterey és újabb)**, teljes funkcióegyezéssel a Windows verzióhoz képest. Minden frissítés egyszerre jelenik meg.

#### **Milyen minimális gépigény szükséges?**

Ez attól függ, hány lézert szeretnél vezérelni. Ha csak néhány lézert használsz, egy alacsonyabb teljesítményű gép is elegendő lesz. Bármelyik Apple Silicon Mac nagyon jól futtatja a szoftvert, és akár 100 lézer vezérlésére is képes lehet. Ha összetett, nagy jelentőségű show-kat futtatsz, akkor a lehető legjobb gépet javasoljuk, amit megengedhetsz magadnak.

#### **Hány lézert tudok vezérelni a Liberationnel?**

A Liberation sok lézert tud futtatni egyetlen számítógépről; több mint 100 lézervezérlővel is teszteltük, így a válasz az alábbiaktól függ:

* a számítógép CPU-ja
* a hálózat sebessége
* az előfizetés típusa

#### **Mely MIDI kontrollereket használhatom?**

A Liberationt a népszerű APC40 Mk2 MIDI kontrollerhez terveztük és optimalizáltuk. Az APC40 Mk1-gyel is működik. Lásd: [Élő vezérlés az APC40-nel](midi-control/live-control-with-the-apc40.md)

Fokozatosan adunk hozzá további MIDI kontrollereket, és jelenleg az APC Mini Mk2-t és a MIDI Fighter Twistert is támogatjuk.

Emellett elérhető a MIDI Send/Receive rendszer is, amely további MIDI vezérlést biztosít. Lásd: [MIDI Send/Receive](midi-control/midi-send-receive.md)

További információ: [MIDI-vezérlés](midi-control/).

#### **Használhatom bármilyen MIDI kontrollerrel?**

Jelenleg egy konfigurálható MIDI rendszeren dolgozunk, amely ezt a jövőben lehetővé teszi. Addig is néhány felhasználónak sikerült MIDI interpreterrel megoldania a vezérlést, amely bármilyen MIDI üzenetet át tud alakítani a MIDI Send/Receive rendszer számára, de ez körülményes és haladó beállítás. Tanácsért keress rá a [fórumon](https://forum.liberationlaser.com), de reálisan nézve az APC40 a legjobb választás.

## Lézervezérlők

#### **Mely lézervezérlők kompatibilisek a Liberationnel?**

* [Ether Dream (ajánlott)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (előfordulhat, hogy frissítened kell a firmware-t)
* LaserCube USB (és LaserDock)
* LaserCube hálózati protokoll (vezetékes kapcsolattal)
* AVB, ahogy a [LASollinger lézerek](https://laseranimation.com/en/) használják (jelenleg csak macOS alatt, tesztelés alatt)

További információ: [Kompatibilis lézerek és vezérlők (DAC-ok)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Miért nem támogatjátok a \[más márkájú] lézervezérlőt?**

A szoftverek és hardverek közötti jobb együttműködés érdekében a Liberation csak olyan DAC-okat támogat, amelyeknek közzétett kommunikációs protokolljuk van. Úgy gondolom, hogy ez a legjobb út előre a lézeripar számára.

#### **Honnan tudhatom, hogy a lézerem használható-e a Liberationnel?**

Ha a lézered rendelkezik az alábbiak egyikével, használhatod a Liberationnel:

* Külső **ILDA input** – egy 25 tűs D-csatlakozó, kompatibilis külső vezérlővel használva.
* Beépített **Ether Dream**.
* Bármely **LaserCube** (USB-s és Wi-Fi-s LaserCube-bal is működik).
* **Beépített Mercury rendszerrel rendelkező X-Laser egység** (Ether Dream módban).
* **Beépített AVB-vel rendelkező LaserAnimation Sollinger projektor** (csak macOS, AVB-kompatibilis hálózati eszközök szükségesek, jelenleg tesztelés alatt).

További információ: [Kompatibilis lézerek és vezérlők (DAC-ok)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Használhatom a Liberationt a LaserCube-ommal?**

Igen, a Liberation közvetlenül működik bármelyik LaserCube-bal. Lásd: [LaserCube](hardware/lasercube.md)

## Licencek

#### **Mennyibe kerül egy licenc?**

Az aktuális árakat a [shop](https://liberationlaser.com/shop) oldalon találod.

#### **Milyen korlátozások vannak a licenccsomagok között?**

Az aktuális licencopciókat a [shop](https://liberationlaser.com/shop) oldalon találod.

Fontos, hogy **minden** csomagban – még az ingyenesben is – tetszőleges számú lézerrel állíthatsz be, előnézhetsz és tervezhetsz show-kat. Más korlátozás nincs, csak az, hogy hány lézert tudsz _arm_ állapotba helyezni. A Liberation minden egyéb funkciója mindenki számára elérhető.

#### **Frissíthetek magasabb csomagra?**

Bármikor válthatsz magasabb csomagra. A jelenlegi licencedből hátralévő időre részleges visszatérítést kapsz, és az új csomagod azonnal elindul. Lásd: [Licenc frissítése / visszaminősítése](installation/upgrade-downgrade-your-license.md)

#### **Visszaválthatok alacsonyabb licencre?**

Bármikor válthatsz alacsonyabb csomagra, de a módosítás csak az aktuális licencidőszak végén lép életbe. Lásd: [Licenc frissítése / visszaminősítése](installation/upgrade-downgrade-your-license.md)

#### **Hogyan engedélyezem a számítógépemet a licencemmel?**

Miután megvásároltad a licencet, a számítógépet magában a Liberation szoftverben engedélyezheted. Az _About_ képernyőn megjelenik egy _Authorise_ gomb, amely arra kér, hogy jelentkezz be a weboldalra. Az engedélyezési folyamat befejezéséhez kövesd a képernyőn megjelenő utasításokat. Lásd: [Engedélyezés és az engedély visszavonása](installation/authorising-and-de-authorising.md)

#### **Milyen gyakran kell csatlakoztatnom a számítógépet az internethez?**

Minden licencmegújításkor csatlakoztatnod kell a Liberationt az internethez, hogy frissítse a belső licencét. Havi ismétlődő fizetés esetén havonta kell csatlakoznod.

#### **Mi történik, ha a megújítás után nem tudom csatlakoztatni a számítógépet az internethez?**

A Liberation a licenc megújulása után 7 nap türelmi időt ad arra, hogy csatlakozz az internethez és frissítsd a belső licencet. Ezt követően a Liberation visszaáll _Free_ módba.

#### **Mi történik, ha lejár a bankkártyám?**

E-mail értesítést kapsz a fizetési szolgáltatónktól, és frissítened kell a fizetési adataidat. Jelentkezz be a weboldalra, és az előfizetések oldalán használd az _Update payment details_ hivatkozást.

#### **Hogyan mondhatom le az ismétlődő licencemet?**

Jelentkezz be a weboldalra, nyisd meg a _Your subscriptions_ oldalt, válaszd ki a lemondani kívánt előfizetést, majd kattints a _Cancel Subscription_ hivatkozásra. A licencidőszak végéig továbbra is használhatod a Liberationt.

#### **Hány számítógépre telepíthetem a Liberationt?**

A Liberationt tetszőleges számú számítógépre telepítheted. Licencengedélyezés csak a lézer / DMX kimenet engedélyezéséhez szükséges, és a licenccsomagod határozza meg, hány számítógép lehet egyszerre kimenetre engedélyezve. Lásd: [Hogyan működik a licencelés](installation/how-licensing-works.md)

#### **Hogyan helyezhetem át a licencemet egyik számítógépről a másikra?**

* Nyisd meg a Liberationt azon a számítógépen, amelyet már nem szeretnél használni
* Győződj meg róla, hogy csatlakozol az internethez, majd kattints az _About_ képernyőn a _De-authorise this computer_ gombra
* Ezután nyisd meg a Liberationt az új számítógépen
* Kattints az _About_ képernyőn az _Authorise this computer_ gombra.
* Megnyílik a weboldal; jelentkezz be, és az engedélyezés befejezéséhez kövesd a képernyőn megjelenő utasításokat

Távolról is visszavonhatod egy olyan számítógép engedélyezését, amelyhez már nincs hozzáférésed (bizonyos korlátozásokkal). Lásd: [Engedélyezés és az engedély visszavonása](installation/authorising-and-de-authorising.md)

#### **Visszavonhatom a Liberation engedélyezését egy elveszett vagy ellopott számítógépen?**

A számítógép engedélyezését a weboldalon keresztül vonhatod vissza. Ha a Liberation telepítése a legutóbbi megújítás óta nem volt online, ez azonnal elvégezhető.

Ha nem, az engedélyezés visszavonása az előfizetés megújulásakor vagy akkor lép életbe, amikor a számítógép csatlakozik az internethez – amelyik előbb történik. Ha sürgősen új számítógépet kell engedélyezned, vedd fel a kapcsolatot a támogatással.

### A Liberation használata

#### Az alapértelmezett beállításban 8 lézer van – hogyan módosíthatom ezt?

Lásd: [A projekt beállítása](setting-up/setting-up-your-project.md) és [Lézerek hozzáadása / eltávolítása](setting-up/adding-removing-lasers.md)

#### Átmásolhatom a zónabeállításokat egyik lézerről a többire?

Igen! Lásd: [Zónák másolása lézerek között](output-view/copy-zones-between-lasers.md)

#### Beírhatok egy számot a csúszka használata helyett?

Igen. `Cmd / Ctrl`-kattintás a csúszkán, és beírhatod az értéket a billentyűzettel.

#### **Hogyan szinkronizálhatom a Liberationt zenéhez?**

Van egy intelligens „tap tempo” rendszere, amely a megszokott módon működik, de használhatsz külső MIDI clockot vagy Ableton Linket is. Lásd: [Tempó / szinkronizálás](tempo-synchronisation.md). A timeline szinkronizálható bármely audiointerfészen beérkező LTC/SMPTE timecode-dal. Lásd: [Timecode](timecode.md).

#### Milyen beállításokat kell módosítanom, hogy a legjobb kimenetet kapjam a lézerből?

A fő beállítás a _Colour Shift_, amely kompenzálja a tükrök mozgása és a lézerek fényerejének változása közötti kis késleltetést. Ha a lézerpontoknak/-nyaláboknak kis „farkuk” van, ezt kell beállítanod. (A „farkakra” példát a [Laser output beállítási panel](setting-up/laser-settings.md) oldalon található fotókon láthatsz.)

Megpróbálhatod módosítani a scanner sebességét is: lassabbra, ha a scannereid egyszerűbbek, vagy gyorsabbra, ha jó minőségűek. De **használd óvatosan, mert ha túl erősen hajtod őket, károsíthatod a scannereket.**

Vannak előre beállított scanner-beállítások is. Az alapértelmezett opció konzervatív, és a legtöbb lézernyalábos feladathoz megfelelő. Vannak azonban más presetek jobb scannerekhez, valamint kifejezetten grafikához hangolt presetek is.

További információ: [Laser output beállítási panel](setting-up/laser-settings.md). Saját presetek létrehozásáról lásd: [◼️ Scanner presets és renderprofilok](advanced/scanner-presets.md) (haladó, folyamatban)

A színegyensúlyt a _Colour calibration_ beállításokkal is korrigálhatod. Lásd: [Színkalibrálás](advanced/colour-calibration.md) (haladó technika)

#### Mire való a _Latency(ms)_ beállítás?

Ez a frame-késleltetés, vagyis a maximális idő aközött, hogy egy frame létrejön, majd elküldésre kerül egy lézernek. Általában nem kell módosítanod, de ha hálózati problémáid vannak, megpróbálhatod növelni. További részletek: [Késleltetés beállítása](setting-up/latency-setting.md).

### Clipek

#### Hogyan módosíthatom egy clip zónáit és beállításait anélkül, hogy elindítanám?

`Alt / Option`-kattintással teheted _aktuálisan kijelölt Clip_ állapotba anélkül, hogy aktiválnád. Lásd még: [Clipek indítása / leállítása](clips/starting-stopping-clips.md)

#### Hogyan másolhatok clipecet?

Kattints és húzz a `Alt / Option` billentyű nyomva tartása közben. Lásd még: [A Clip Deck rendszerezése](clips/organising-your-clip-deck.md)

#### Hogyan törölhetek clipecet?

Kattints rájuk, majd húzd le őket a clip deckről. Lásd még: [A Clip Deck rendszerezése](clips/organising-your-clip-deck.md)

#### Hogyan jelölhetek ki többet egyszerre, törölhetek, egyesíthetek clip deckeket stb.?

Lásd: [A Clip Deck rendszerezése](clips/organising-your-clip-deck.md)

#### Mit jelentenek a clipen látható kis mikrofon szimbólum és más ikonok?

Ezek azt jelzik, hogy a clip hang- vagy MIDI-bemenetet használ, a 3 pont pedig azt mutatja, hogy zónakésleltetés van beállítva. Lásd: [Mik azok a kis ikonok a Clip gombokon?](clips/what-are-the-small-icons-on-the-clip-buttons.md)
