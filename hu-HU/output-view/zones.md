---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zónák

A legtöbb projektben a leggyakrabban használt zónatípus a _Beam zone_. Ez a zóna a levegőben látható atmoszferikus beam effektekhez készült. A másik zónatípus a _Canvas zone_ (lásd: [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/)).

{% hint style="danger" %}
**FIGYELMEZTETÉS – Különösen óvatosan mozgass zónákat, miközben a lézer működik**, és vedd le a fényerőt a lehető legalacsonyabbra. A lézerek biztonságos aktiválásáról és zónázásáról részletes útmutatót itt találsz: [setting-up-lasers.md](../setting-up/setting-up-lasers.md)
{% endhint %}

A zónákat egérrel kattintva és húzva mozgathatod. Kapcsolj be egy tesztmintát, hogy lásd, hová kerül a zóna.

{% hint style="info" %}
A nyílbillentyűkkel finoman **elmozdíthatod** az aktuálisan kijelölt zónát/pontot. A `Shift` billentyűvel nagyobb lépésekben mozgathatod.
{% endhint %}

{% hint style="info" %}
Gyors tipp: a zónabeállításokat gyorsan átmásolhatod több lézerre is! Lásd: [copy-laser-settings.md](../setting-up/copy-laser-settings.md)
{% endhint %}

### Új beam zóna hozzáadása

Kattints az eszköztár tetején található _Add a new beam zone_ gombra, és megjelenik egy új zóna. Vedd figyelembe, hogy a beam zónák a hozzáadásuk sorrendjében vannak rendezve, de átrendezhetők. Lásd: [re-ordering-beam-zones.md](re-ordering-beam-zones.md)

### Meglévő canvas zóna hozzáadása

Kattints az _Add existing canvas zone_ gombra. Megjelenik az elérhető canvas zónák listája, ahol be- és kikapcsolhatod őket az adott lézerhez. Lásd: [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/)

### Zónaforma-típusok

3 zónaforma-típus érhető el:

* **Quad** – az alapértelmezett téglalap alakú zónaforma, amely lehet szabályos (tengelyekhez igazított) vagy torzított. Nagyobb téglalap alakú zónákhoz, illetve perspektívakorrekciót igénylő canvas zónákhoz ideális.
* **Line/Curve** – 2 vagy több ponttal és vastagsággal definiált zóna. Ideális keskeny zónákhoz, illetve erkélyeken, hidakon vagy más ívelt formákon történő maszkoláshoz.
* **Segmented** – kisebb quadokra felosztható zóna. Építészeti mappinghez ideális.

Kattints jobb gombbal bármelyik zónára a beállításai megnyitásához. Ebben a jobb kattintásos menüben a következőket teheted:

* Átnevezheted a zónát (ez hasznos lehet a clip deckben való azonosításhoz, különösen sok zóna esetén)
* Engedélyezheted/letilthatod a zónát
* Zárolhatod a pozícióját
* Megváltoztathatod az alakzat típusát
* Visszaállíthatod az alapértelmezett pozícióra
* Elérheted az adott alakzattípushoz tartozó beállításokat
* Törölheted
* Hozzáadhatsz egy _Alt Zone_-t (lásd: [alt-zone-system.md](alt-zone-system.md))

{% hint style="danger" %}
**FIGYELMEZTETÉS –** légy nagyon óvatos, ha aktív lézer mellett módosítod a zóna típusát. A zóna az adott alakzathoz utoljára használt pozícióra/méretre áll vissza, így a kimenet hirtelen megváltozhat. A zónatípus módosítása előtt érdemes kikapcsolni a lézert.
{% endhint %}

### Quad zónaforma

A quad minden sarkát egérrel mozgathatod. `Alt / Option`-kattintással egy sarokra külön mozgathatod azt a többitől, és torzíthatod a quadot. Miután a quad torzítva lett, minden sarok szabadon mozgatható.

A torzítást eltávolíthatod, és visszaállíthatod tengelyekhez igazított téglalappá a jobb kattintásos menü _REMOVE DISTORTION_ gombjával.

#### Perspektívakorrekció

Ez az opció a jobb kattintásos menü kapcsológombjával állítható, és a torzítási módszert határozza meg. Beam zónák esetén általában érdemes kikapcsolva hagyni, de ha ez a zóna grafikát vetít egy sík felületre, kapcsold be, és a kimenet perspektívakorrekciót kap.

{% hint style="info" %}
Ha a _Perspective correction_ ki van kapcsolva, a tartalom _bilineáris interpolációval_ torzul. Más szóval a tartalom egyenletesen oszlik el a quad felületén. Ezért ideális beam zónákhoz.

Bekapcsolt perspektívakorrekció esetén a tartalom perspektivikus torzítással módosul, amely figyelembe veszi a rövidülést. Tehát ha grafikát vetítesz egy falra ferde szögből, ezzel korrigálhatod a kimenetet, és javíthatod a vetítési torzítást.
{% endhint %}

### Line / Curve zónaforma

A Line / Curve zónaforma az utóbbi show-kban az egyik leggyakrabban használt megoldásommá vált, és akár azt is mondhatnánk, hogy ennek kellene lennie az alapértelmezett beam zónaformának.

A zónáimnak gyakran nagyon keskenynek kell lenniük, hogy beférjenek a helyszínek szűk részeibe vagy épületeken az ablakok közé. Ilyenkor egy quad négy, egymáshoz nagyon közeli sarkának állítgatása rendkívül körülményes lehet. Így született meg a Line / Curve zóna!

Egyenes vonalakhoz mindössze két pontra van szükség, majd a jobb kattintásos menüben állítsd be a _Zone thickness_ értékét. Ez a legegyszerűbb zónák létrehozásának leggyorsabb módja.

`Alt / Option`-kattintással a vonalra további pontokat hozhatsz létre. Ezek a pontok automatikusan simítva lesznek, hogy folyamatos formát adjanak, a _Smooth level_ beállítással pedig kisimíthatod az esetleges töréseket.

`Alt / Option`-kattintással egy pontra törölheted azt.

Ha pedig van tapasztalatod vektorgrafikus alkalmazásokkal (Inkscape, Illustrator stb.), a _Manually adjust bezier curves_ opcióval finoman beállíthatod az összes vezérlőpontot.

### Segmented zónaforma

Ez a felosztott zóna nagyon részletes korrekciókat tesz lehetővé, és akkor hasznos, ha összetett formákra végzel mappinget. A jobb kattintásos menü + és - gombjaival adhatsz hozzá vagy távolíthatsz el felosztásokat.

### Teljesen másik zóna által fedett zóna szerkesztése

Kattints jobb gombbal a felül lévő zónára, majd kattints a lakat gombra a zárolásához. Ezután már szerkeszteni és állítani tudod az alatta lévő zónát.

<br>

{% hint style="info" %}
Miután hozzáadsz egy Beam zónát a kimenetedhez, az elérhető lesz cliphez való hozzáadásra a clip deckben.
{% endhint %}
