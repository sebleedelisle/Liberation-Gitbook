# ✅ Laser output settings spjaldið

Opnaðu _Laser output_ stillingaspjaldið í valmyndinni _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Þá sérðu stillingar fyrir þann laser sem er valinn núna. Þú getur breytt vali á laser:

* með númerahnappnum hans á _Laser overview_ spjaldinu
* með tölutakka á lyklaborðinu; takkarnir 1 til 0 opna laser 1 - 10
* með `Tab` takkanum til að fletta í gegnum laserana (`Shift + Tab` fer til baka).

Efst á þessu spjaldi sérðu:

* númerahnapp - smelltu á hann til að vopna/afvopna þennan laser. Hann er rauður þegar laserinn er vopnaður.
* _Brightness_ sleða aðeins fyrir þennan laser. Athugaðu að þetta sameinast við heildarbirtustillinguna.
* _Test Pattern_ rofa og mynsturval. Þetta leyfir þér að velja tiltekið prófunarmynstur aðeins fyrir þennan laser. (Þessar stýringar eru speglaðar á tækjastikunni í Output sýninni).

### Úttaksstefna / leiðrétting speglunar

Næstu atriði eru til að leiðrétta uppsetningu lasersins þannig að hann hagi sér samræmt í Liberation.

* **Flip horizontal / vertical** - þessir valkostir leyfa þér að leiðrétta úttak lasersins

{% hint style="info" %}
Þú ættir ekki að þurfa að breyta stillingunum fyrir horizontal / vertical flip nema laserinn sé rangt tengdur eða hann sé með X/Y flip hnappa aftan á sem eru ekki rétt stilltir. Ef þú vilt spegla úttak fyrir tiltekinn Clip er hægt að gera það á Clip-inu sjálfu.
{% endhint %}

* **Orientation** - ef laserinn hefur verið riggaður á hlið eða á hvolfi geturðu leiðrétt snúninginn með þessari stillingu.
* **Fine position adjustments** - má nota til að leiðrétta mjög lítilsháttar hliðrun/snúning. Þetta er ætlað til að leiðrétta rek eða sig ef laser hefur verið skilinn eftir yfir nótt eða í langan tíma.

{% hint style="info" %}
Athugaðu að leiðréttingar fyrir orientation / mirroring breyta engu í 3D Visualiser. Þær á að nota til að leiðrétta úttak raunverulega lasersins svo það passi við það sem sést í 3D Visualiser!
{% endhint %}

### Afrita laserstillingar

Sjá [#copy-laser-settings](./#copy-laser-settings).

### Scanner settings

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed stillingin ákvarðar hversu hratt skannarnir hreyfast.

{% hint style="danger" %}
Þótt sjálfgefnu stillingarnar séu frekar varfærnar geturðu samt skemmt skannana ef þú keyrir þá of hratt. Farðu varlega, sérstaklega þegar þú hækkar hraðann.
{% endhint %}

{% hint style="info" %}
Þessi Speed stilling breytir ekki punktahraðanum; hún stillir í staðinn hversu dreifðir punktarnir eru. Nánari upplýsingar eru í [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Geislinn skiptir um lit og kveikir og slekkur á sér á meðan skannarnir færa hann til, og þessir tveir hlutir eru yfirleitt ekki fullkomlega samstilltir. Stilltu þetta til að koma þeim aftur í takt.

{% hint style="info" %}
Þetta er stundum kallað _blank shift_, en ég kýs persónulega heitið _scanner sync_ - það er aðeins nákvæmara þar sem þetta stillir tímasetningu allra litabreytinga miðað við hreyfingu skannans.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser „halar“ - Colour shift ekki rétt stillt</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Engir laser „halar“! Colour shift er gott!</p></figcaption></figure></div>

Ef þú sérð litla „hala“ í laserúttakinu er líklegt að það þurfi að stilla Scanner sync. Ef halarnir birtast samt sama hvað þú gerir ertu líklega að keyra skannana/laserdrifin hraðar en þau ráða við. Prófaðu að lækka skannahraðann.

#### Scanner presets

Notaðu þetta til að velja fyrirfram hannaða skannastillingu. Sjálfgefni valkosturinn er yfirleitt í lagi, svo þú ættir ekki að þurfa að breyta þessari stillingu nema þú sért með sérstaklega slæma (eða góða) skanna. Ef þú vilt skoða þetta nánar, sjá [scanner-presets.md](../../advanced/scanner-presets.md)

#### Colour calibration

Þú getur notað þetta kerfi til að leiðrétta birtukúrfu og hvítjöfnun lasersins. Sjá [colour-calibration.md](../../advanced/colour-calibration.md)

#### Advanced settings

Þú ættir ekki að þurfa að fikta í þessu, en ef þú ert forvitinn, sjá [advanced-laser-settings.md](../../advanced/advanced-laser-settings.md)
