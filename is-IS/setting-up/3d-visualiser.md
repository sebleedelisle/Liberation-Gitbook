---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Inngangur

3D Visualiser í Liberation er einstaklega gagnlegt verkfæri — þú getur hannað og fínstillt sýningarnar þínar án þess að þurfa neina leysigeisla! Þetta hefur reynst mér ómetanlegt, sérstaklega í flóknum uppsetningum með mörgum leysum.

### Að rata um 3D rýmið

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>3D Visualiser view</p></figcaption></figure>

* Smelltu og dragðu til að snúa sýninni í kringum orbit punktinn
* Notaðu músarhjólið til að færa þig aftur á bak og áfram í átt að orbit punktinum
* Smelltu og dragðu á meðan þú heldur Shift inni til að færa myndavélina til hliðar (strafe) til vinstri, hægri, upp og niður eftir XY planinu
* Tvísmelltu hvar sem er í visualiser til að endurstilla staðsetningu myndavélarinnar

### Settings

Opnaðu _3D Visualiser Settings_ panel í gegnum _Window_ valmyndina.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings panel</p></figcaption></figure>

* **Visualiser size** - breytir stærð visualiser miðað við afganginn af appinu
* **Brightness Adjustment** - breytir því hversu bjartir leysarnir birtast
* **Show laser numbers** - birtir viðeigandi númer fyrir ofan hvern leysi
* **Show zone names** - birtir viðeigandi nöfn fyrir zone fyrir neðan hvern leysi

### Stillingar myndavélar

Þessar stillingar tengjast að mestu sýndarmyndavélinni í 3D rýminu. Þú sérð fellilista með forstillingum fyrir þessar stillingar sem þú getur vistað og hlaðið inn aftur.

* **Camera distance -** Myndavélin beinist alltaf að sínum _Orbit point_. Camera distance segir til um hversu langt hún er frá þessum punkti. Þú getur líka stillt þetta með músarhjólinu.
* **FOV -** Field of view — ákvarðar hversu vítt sjónarhorn myndavélin hefur eða hversu mikið er aðdráttað.
* **Orbit position** - lýsir núverandi snúningi í kringum orbit punktinn. Fyrra gildið er snúningur um X-ásinn (pitch) og seinna gildið er snúningur um Y-ásinn (yaw).
* **Orbit centre point** - staðsetning orbit punktsins í 3D rýminu, x, y, z.
* **Grid height** - hæð grindarinnar frá „jörðinni“ (þ.e. þar sem y = 0).

### Content settings

Þessar stillingar ákvarða hvar leysarnir (og Canvas) eru staðsett í 3D umhverfinu. Þú sérð fellilista með forstillingum fyrir þessar stillingar sem þú getur vistað og hlaðið inn aftur.

#### Leysar

Hver leysir hefur sinn eigin stillingahóp sem þú getur opnað með litla hvíta þríhyrningnum.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Stillingar fyrir leysa í 3D visualiser</p></figcaption></figure>

* **3D Position** - x-, y- og z-staðsetning leysisins.
* **3D Orientation** - snúningur leysisins um x-, y- og z-ásana.
* **Flip X / Flip Y** - speglar sýndar Output leysisins — ATHUGAÐU að þetta ætti ekki að vera nauðsynlegt. Betra er að nota flip / orientation stillingarnar fyrir leysinn til að leiðrétta ósamræmi í vélbúnaðinum.
* **Output Range horizontal / vertical** - tengist hámarks- og lágmarkshorni skanna leysisins. 60º er staðlað, en þú getur breytt þessu ef leysarnir þínir eru öðruvísi.

#### Canvas

Ef þú notar Canvas kerfið geturðu líka valið að hafa myndina úr Canvas með í 3D view. Virkjaðu gátreitinn til að birta Canvas þar og notaðu stillingar fyrir staðsetningu, stefnu og skala til að ákvarða hvernig það birtist í 3D view hjá þér.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Stillingar fyrir Canvas í 3D visualiser</p></figcaption></figure>

{% hint style="info" %}
Sérðu „drauga“-leysa? 3D Visualiser er að nokkru leyti óháður leysauppsetningunni og það er hægt að hafa fleiri leysa í visualiser en þú ert með í Liberation. Þegar þú bætir leysi við verkefnið þitt er nýjum leysihlut inni í visualiser líka bætt við. En ef þú eyðir leysi verður eftir „drauga“-leysihlutur í visualiser.

Til að losna við alla drauga-leysana skaltu smella á _Remove extra 3D laser objects_ hnappinn (neðst í 3D Visualiser settings panel).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
