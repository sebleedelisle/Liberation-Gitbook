---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Laser output beállítási panel

Nyisd meg a _Laser output_ beállítási panelt a _View -> Laser Output Settings_ menüből.

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Itt az aktuálisan kiválasztott lézer beállításait látod, amelyeket így válthatsz:

* a _Laser overview_ panelen lévő számozott gombbal
* a billentyűzet számbillentyűivel; az 1–0 billentyűk az 1–10. lézert nyitják meg
* a `Tab` billentyűvel lépkedhetsz a lézerek között (`Shift + Tab` visszafelé lép).

A panel tetején ezeket találod:

* egy számozott gomb – erre kattintva élesítheted vagy hatástalaníthatod ezt a lézert. Piros, amikor a lézer élesítve van.
* egy _Brightness_ csúszka csak ehhez a lézerhez. Fontos, hogy ez a globális fényerővel együtt érvényesül.
* _Test Pattern_ kapcsoló és mintaválasztó. Ezzel csak ehhez a lézerhez választhatsz külön tesztmintát. (Ezek a vezérlők az Output nézet eszköztárában is megjelennek).

### Kimeneti tájolás / tükrözés korrekciója

A következő elemekkel a lézer beállítását korrigálhatod, hogy következetesen viselkedjen a Liberationben.

* **Flip horizontal / vertical** – ezekkel az opciókkal korrigálhatod a lézer kimenetét

{% hint style="info" %}
A horizontal / vertical flip beállításokat általában nem kell módosítanod, kivéve, ha a lézer hibásan van bekötve, vagy a hátoldalán lévő X/Y flip gombok nincsenek megfelelően beállítva. Ha egy adott clip kimenetét szeretnéd megfordítani, azt magán a clipen lehet beállítani.
{% endhint %}

* **Orientation** – ha a lézer az oldalára fordítva vagy fejjel lefelé van felszerelve, ezzel a beállítással korrigálhatod az elforgatást.
* **Fine position adjustments** – nagyon kis eltolódások/elfordulások korrigálására használható. Arra készült, hogy javítsa az elcsúszást vagy beállási változást, ha a lézer éjszakára vagy hosszabb időre bekapcsolva maradt.

{% hint style="info" %}
Fontos, hogy az orientation / mirroring korrekciók semmit nem változtatnak a 3D Visualiserben. Ezeket arra kell használni, hogy a tényleges lézer kimenete megegyezzen azzal, ami a 3D Visualiserben látható!
{% endhint %}

### Lézerbeállítások másolása

Lásd: [Laser output beállítási panel](laser-settings.md#copy-laser-settings "mention").

### Scanner settings

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

A speed beállítás határozza meg, milyen gyorsan mozognak a szkennerek.

{% hint style="danger" %}
Bár az alapértelmezett beállítások elég óvatosak, a szkennereket így is károsíthatod, ha túl gyorsan hajtod őket. Légy körültekintő, különösen a sebesség növelésekor.
{% endhint %}

{% hint style="info" %}
Ez a speed beállítás nem a pontsebességet módosítja, hanem azt, mennyire legyenek szétterítve a pontok. További információért lásd: [◼️ Hogyan generál a Liberation lézeres tartalmat](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

A sugár színt vált, illetve be- és kikapcsol, miközben a szkennerek mozgatják, és ez a két dolog általában nincs tökéletesen szinkronban egymással. Ezzel a beállítással hozhatod őket újra összhangba.

{% hint style="info" %}
Ezt néha _blank shift_ néven említik, de én személy szerint jobban szeretem a _scanner sync_ kifejezést – valamivel pontosabb, mert az összes színváltás időzítését állítja a szkenner mozgásához képest.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Lézer „csóvák” – a Colour shift nincs megfelelően beállítva</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Nincsenek lézer „csóvák”! A Colour shift jó!</p></figcaption></figure></div>

Ha kis „csóvákat” látsz a lézer kimenetén, valószínűleg a scanner sync beállítást kell korrigálni. Ha a csóvák bármit állítasz is továbbra is megjelennek, akkor valószínűleg gyorsabban hajtod a szkennereket/lézermeghajtókat, mint amit kezelni tudnak. Próbáld csökkenteni a szkenner sebességét.

#### Scanner presets

Ezzel előre elkészített szkennerbeállítást választhatsz. Az alapértelmezett opció általában megfelelő, ezért ezt a beállítást nem kell módosítanod, kivéve, ha különösen rossz (vagy jó) szkennereid vannak. Ha mélyebben is bele szeretnél nézni, lásd: [◼️ Scanner presets és renderprofilok](../advanced/scanner-presets.md "mention")

#### Colour calibration

Ezzel a rendszerrel korrigálhatod a lézer fényerőgörbéjét és fehéregyensúlyát. Lásd: [Színkalibrálás](../advanced/colour-calibration.md "mention")

#### Advanced settings

Ezekkel általában nem kell foglalkoznod, de ha kíváncsi vagy, lásd: [◼️ Speciális lézerbeállítások](../advanced/advanced-laser-settings.md "mention")
