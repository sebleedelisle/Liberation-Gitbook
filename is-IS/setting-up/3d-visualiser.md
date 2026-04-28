---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Inngangur

3D Visualiser í Liberation er afar gagnlegur eiginleiki — þú getur hannað og fínstillt sýningarnar þínar án þess að þurfa nokkra leysigeisla! Þetta hefur reynst mér ómetanlegt verkfæri, sérstaklega í flóknum uppsetningum með mörgum leysum.

### Að fara um 3D-rýmið

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>3D Visualiser-skjárinn</p></figcaption></figure>

* Smelltu og dragðu til að snúa sýninni í kringum orbit-punktinn
* Notaðu músarhjólið til að færa þig aftur og fram í átt að orbit-punktinum
* Smelltu og dragðu á meðan þú heldur shift-lyklinum niðri til að færa myndavélina til hliðar (strafe), til vinstri, hægri, upp og niður eftir XY-planinu
* Tvísmelltu hvar sem er í visualiser til að endurstilla staðsetningu myndavélarinnar

### Settings

Opnaðu _3D Visualiser Settings_ spjaldið í _Window_ valmyndinni.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings spjaldið</p></figcaption></figure>

* **Visualiser size** - breytir stærð visualiser miðað við restina af forritinu
* **Brightness Adjustment** - breytir því hversu bjartir leysarnir birtast
* **Show laser numbers** - birtir viðeigandi númer fyrir ofan hvern leysi
* **Show zone names** - birtir viðeigandi zone-nöfn fyrir neðan hvern leysi

### Stillingar myndavélar

Þessar stillingar tengjast aðallega sýndarmyndavélinni í 3D-rýminu. Þú sérð fellilista með forstillingum fyrir þessar stillingar sem þú getur vistað og hlaðið aftur inn.

* **Camera distance -** Myndavélin vísar alltaf á _Orbit point_. Fjarlægð myndavélarinnar segir til um hversu langt hún er frá þessum punkti. Þú getur líka stillt þetta með skrunhjóli músarinnar.
* **FOV -** Field of view - ákvarðar hversu vítt sjónarhorn myndavélarinnar er eða hversu mikið hún er aðdrægð.
* **Orbit position** - lýsir núverandi snúningi í kringum orbit-punktinn. Fyrra gildið er snúningur um X-ásinn (pitch) og seinna gildið er snúningur um Y-ásinn (yaw).
* **Orbit centre point** - staðsetning orbit-punktsins í 3D-rýminu, x, y, z.
* **Grid height** - hæð hnitanetsins frá „jörðinni“ (þ.e. þar sem y = 0).

### Content settings

Þessar stillingar ákvarða hvar leysarnir (og canvas) eru staðsett innan 3D-umhverfisins. Þú sérð fellilista með forstillingum fyrir þessar stillingar sem þú getur vistað og hlaðið aftur inn.

#### Lasers

Hver leysir hefur sinn eigin stillingahóp sem þú getur stækkað með litla hvíta þríhyrningnum.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Stillingar leysis í 3D visualiser</p></figcaption></figure>

* **3D Position** - x-, y- og z-staðsetning leysisins.
* **3D Orientation** - snúningur leysisins um hvern x-, y- og z-ás.
* **Flip X / Flip Y** - speglar sýndarúttak leysisins - ATHUGAÐU að þetta ætti ekki að vera nauðsynlegt - betra er að nota flip / orientation stillingar leysisins til að leiðrétta ósamræmi í vélbúnaðinum þínum.
* **Output Range horizontal / vertical** - tengist hámarks-/lágmarkshorni skanna leysisins. 60º er staðlað, en þú getur breytt þessu ef leysarnir þínir eru öðruvísi.

#### Canvas

Ef þú notar canvas-kerfið geturðu einnig valið að hafa canvas-myndina með í 3D-sýninni. Virkjaðu gátreitinn til að birta canvas inni í henni og notaðu staðsetningar-, stefnu- og kvarðastillingarnar til að ákvarða hvernig hún lítur út í 3D-sýninni þinni.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Canvas-stillingar í 3D visualiser</p></figcaption></figure>

{% hint style="info" %}
Sérðu „drauga“-leysa? 3D Visualiser er að nokkru leyti óháður leysiuppsetningunni og það er mögulegt að hafa fleiri leysa í visualiser en þú ert með í Liberation. Þegar þú bætir leysi við verkefnið þitt verður einnig bætt við nýjum leysi-hlut inni í visualiser. En ef þú eyðir leysi verður „drauga“-leysihlutur áfram í visualiser.

Til að losna við alla drauga-leysana skaltu smella á _Remove extra 3D laser objects_ hnappinn (neðst í 3D Visualiser settings spjaldinu).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
