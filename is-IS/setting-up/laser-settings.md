---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Stillingaspjald fyrir Laser Output

Opnaðu stillingaspjaldið _Laser output_ með valmyndinni _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Þá sérðu stillingar fyrir þann leysi sem er valinn. Þú getur skipt um valinn leysi:

* með númerahnappi hans á spjaldinu _Laser Overview_
* með talnatakka á lyklaborðinu; takkarnir 1 til 0 opna leysa 1 - 10
* með `Tab` til að fletta á milli leysa (`Shift + Tab` fer til baka).

Efst á þessu spjaldi sérðu:

* númerahnapp - smelltu á hann til að velja arm eða disarm fyrir þennan leysi. Hann er rauður þegar leysirinn er armed.
* _Brightness_ renna sem gildir aðeins fyrir þennan leysi. Athugaðu að hún er notuð ásamt Global Brightness.
* _Test Pattern_ rofa og val fyrir mynstur. Þetta gerir þér kleift að velja sérstakt test pattern aðeins fyrir þennan leysi. (Þessi stjórntæki sjást líka á tækjastikunni í Output view).

### Leiðrétting á stefnu úttaks / speglun

Næstu atriði eru til að leiðrétta uppsetningu leysisins þannig að hann hegði sér samræmt í Liberation.

* **Flip horizontal / vertical** - þessir valkostir gera þér kleift að leiðrétta úttak leysisins

{% hint style="info" %}
Þú ættir ekki að þurfa að breyta stillingunum Flip horizontal / vertical nema leysirinn sé rangt víraður eða hann sé með X/Y flip hnappa á bakhliðinni sem eru ekki rétt stilltir. Ef þú vilt spegla úttak fyrir tiltekinn Clip er hægt að gera það í viðkomandi Clip.
{% endhint %}

* **Orientation** - ef leysirinn hefur verið riggaður á hlið eða á hvolfi geturðu leiðrétt snúninginn með þessari stillingu.
* **Fine position adjustments** - má nota til að leiðrétta mjög smávægilega hliðrun/snúning. Þetta er ætlað til að leiðrétta rek eða sig ef leysir hefur verið skilinn eftir yfir nótt eða í langan tíma.

{% hint style="info" %}
Athugaðu að leiðréttingar á stefnu / speglun breyta engu í 3D Visualiser. Þær á að nota til að leiðrétta úttak raunverulega leysisins þannig að það passi við það sem sést í 3D Visualiser!
{% endhint %}

### Afrita Laser Settings

Sjá [Afrita Laser Settings](laser-settings.md#copy-laser-settings).

### Stillingar skanna

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Stillingin Speed ræður því hversu hratt skannarnir hreyfast.

{% hint style="danger" %}
Þótt sjálfgefnu stillingarnar séu frekar varfærnar geturðu samt skemmt skannana ef þú keyrir þá of hratt. Farðu varlega, sérstaklega þegar þú hækkar hraðann.
{% endhint %}

{% hint style="info" %}
Þessi Speed stilling breytir ekki punktatíðninni. Hún stillir í staðinn hversu dreifðir punktarnir eru. Nánari upplýsingar eru í [Hvernig Liberation býr til laserefni](../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Geislinn skiptir um lit og kveikir og slekkur á sér á meðan skannarnir færa hann til, og þessir tveir þættir eru yfirleitt ekki fullkomlega samstilltir. Stilltu þetta til að fá þá aftur í takt.

{% hint style="info" %}
Þetta er stundum kallað _blank shift_, en mér finnst hugtakið _scanner sync_ betra - það er aðeins nákvæmara, því stillingin breytir tímasetningu allra litabreytinga miðað við hreyfingu skannanna.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>„Halar“ í leysinum - Colour shift er ekki rétt stillt</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Engir „halar“ í leysinum! Colour shift er í lagi!</p></figcaption></figure></div>

Ef þú sérð litla „hala“ í úttaki leysisins þarf líklega að stilla Scanner sync. Ef halarnir sjást áfram sama hvað þú stillir, ertu líklega að keyra skannana eða drifbúnað leysisins hraðar en þeir ráða við. Prófaðu að lækka hraða skannanna.

#### Forstillingar skanna

Notaðu þetta til að velja fyrirfram hannaða stillingu fyrir skannana. Sjálfgefni valkosturinn er yfirleitt í lagi, þannig að þú ættir ekki að þurfa að breyta þessari stillingu nema þú sért með sérstaklega lélega (eða góða) skanna. Ef þú vilt skoða þetta nánar, sjá [Forstillingar skanna](../advanced/scanner-presets.md)

#### Litakvörðun

Þú getur notað þetta kerfi til að leiðrétta birtuferil og hvítjöfnun leysisins. Sjá [Litakvörðun](../advanced/colour-calibration.md)

#### Ítarlegar stillingar

Þú ættir ekki að þurfa að fikta í þessu, en ef þú ert forvitin/n, sjá [Ítarlegar Laser Settings](../advanced/advanced-laser-settings.md)
