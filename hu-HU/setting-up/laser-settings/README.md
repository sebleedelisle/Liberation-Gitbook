# ✅ Laser output settings panel

A _Laser output_ beállítási panelt a _View -> Laser Output Settings_ menüből nyithatod meg.

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Itt az aktuálisan kiválasztott lézer beállításai jelennek meg, amelyeket így válthatsz:

* a _Laser overview_ panelen található számgombbal
* a billentyűzet számgombjaival; az 1–0 billentyűk az 1–10. lézert nyitják meg
* a `Tab` billentyűvel, amellyel végiglépkedhetsz a lézereken (`Shift + Tab` visszafelé lép).

A panel tetején a következőket látod:

* egy számgombot – erre kattintva élesítheted vagy kikapcsolhatod az adott lézer élesítését. A gomb piros, amikor a lézer élesítve van.
* egy _Brightness_ csúszkát csak ehhez a lézerhez. Fontos, hogy ez a globális fényerővel együtt érvényesül.
* _Test Pattern_ kapcsolót és mintaválasztót. Ezzel csak ehhez a lézerhez választhatsz konkrét tesztmintát. (Ezek a vezérlők az Output nézet eszköztárában is megtalálhatók.)

### Kimeneti tájolás / tükrözés korrekciója

A következő elemekkel a lézer beállítását korrigálhatod, hogy az következetesen működjön a Liberationben.

* **Flip horizontal / vertical** – ezekkel az opciókkal korrigálhatod a lézer kimenetét

{% hint style="info" %}
A vízszintes / függőleges tükrözési beállításokat általában nem kell módosítanod, kivéve ha a lézer hibásan van bekötve, vagy a hátulján található X/Y tükröző gombok nincsenek megfelelően beállítva. Ha egy adott Clip kimenetét szeretnéd tükrözni, azt magán a Clipen állíthatod be.
{% endhint %}

* **Orientation** – ha a lézer az oldalára fordítva vagy fejjel lefelé van felszerelve, ezzel a beállítással korrigálhatod az elforgatást.
* **Fine position adjustments** – nagyon kis eltolások vagy elfordulások korrigálására használható. Arra készült, hogy javítsa az elmozdulást vagy beállást, ha a lézer egy éjszakán át vagy hosszabb ideig állt.

{% hint style="info" %}
Fontos, hogy az orientation / mirroring korrekciók semmit nem változtatnak a 3D Visualiserben. Ezeket arra kell használni, hogy a tényleges lézer kimenete megfeleljen annak, amit a 3D Visualiserben látsz.
{% endhint %}

### Lézerbeállítások másolása

Lásd: [Laser output settings panel](./#copy-laser-settings).

### Scanner beállítások

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

A sebességbeállítás határozza meg, milyen gyorsan mozognak a scannerek.

{% hint style="danger" %}
Bár az alapértelmezett beállítások meglehetősen óvatosak, a scannerek akkor is megsérülhetnek, ha túl gyorsan hajtod őket. Légy körültekintő, különösen a sebesség növelésekor.
{% endhint %}

{% hint style="info" %}
Ez a sebességbeállítás nem a pontsebességet módosítja, hanem azt, hogy a pontok mennyire legyenek szétterítve. További információ: [◼️ Hogyan generál a Liberation lézeres tartalmat](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

A nyaláb színt vált, illetve be- és kikapcsol, miközben a scannerek mozgatják. Ez a két folyamat általában nincs tökéletes szinkronban egymással. Ezzel a beállítással hozhatod őket újra összhangba.

{% hint style="info" %}
Ezt néha _blank shift_ néven is említik, de én jobban szeretem a _scanner sync_ kifejezést – valamivel pontosabb, mert az összes színváltás időzítését igazítja a scanner mozgásához képest.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Lézeres „csóvák” – a Colour shift nincs megfelelően beállítva</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Nincsenek lézeres „csóvák”! A Colour shift jó!</p></figcaption></figure></div>

Ha kis „csóvákat” látsz a lézerkimeneten, valószínűleg a scanner sync beállítását kell módosítani. Ha a csóvák bárhogy állítod is megmaradnak, valószínűleg gyorsabban hajtod a scannereket vagy a lézermeghajtókat, mint amit kezelni tudnak. Próbáld csökkenteni a scanner sebességét.

#### Scanner presetek

Ezzel előre elkészített scanner beállítást választhatsz. Az alapértelmezett opció általában megfelelő, ezért ezt a beállítást nem kell módosítanod, kivéve ha különösen gyenge (vagy jó) scannereid vannak. Ha mélyebben is érdekel, lásd: [◼️ Scanner presets és renderprofilok](../../advanced/scanner-presets.md)

#### Színkalibráció

Ezzel a rendszerrel korrigálhatod a lézer fényerőgörbéjét és fehéregyensúlyát. Lásd: [Színkalibrálás](../../advanced/colour-calibration.md)

#### Advanced settings

Ezekhez általában nem kell hozzányúlnod, de ha kíváncsi vagy, lásd: [◼️ Speciális lézerbeállítások](../../advanced/advanced-laser-settings.md)
