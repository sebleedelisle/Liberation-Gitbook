---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Stillingaspjaldið Laser output

Opnaðu stillingaspjaldið _Laser output_ í valmyndinni _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Þá birtast stillingar fyrir þann laser sem er valinn hverju sinni og þú getur breytt honum:

* með númerahnappinum hans í spjaldinu _Laser overview_
* með númeralykli á lyklaborðinu; lyklar 1 til 0 opna laser 1 - 10
* með `Tab` lyklinum til að fletta á milli lasera (`Shift + Tab` fer til baka).

Efst á þessu spjaldi sérðu:

* númerahnapp - smelltu á hann til að virkja/afvirkja þennan laser. Hann er rauður þegar laserinn er virkjaður.
* _Brightness_ sleða eingöngu fyrir þennan laser. Athugaðu að þetta leggst saman við almenna birtustillingu.
* _Test Pattern_ rofa og mynsturval. Þetta gerir þér kleift að velja sérstakt prófunarmynstur eingöngu fyrir þennan laser. (Þessar stýringar eru einnig speglaðar á tækjastikunni í Output view).

### Leiðrétting á stefnu úttaks / speglun

Næstu atriði eru til að leiðrétta uppsetningu lasersins svo hann hegði sér á samræmdan hátt í Liberation.

* **Flip horizontal / vertical** - þessir valkostir gera þér kleift að leiðrétta úttak lasersins

{% hint style="info" %}
Þú ættir ekki að þurfa að breyta horizontal / vertical flip stillingunum nema laserinn sé rangt tengdur eða hann sé með X/Y flip hnappa aftan á sem eru ekki rétt stilltir. Ef þú vilt spegla úttak fyrir tiltekið clip er hægt að gera það á clip-inu sjálfu.
{% endhint %}

* **Orientation** - ef laserinn hefur verið festur á hlið eða á hvolfi geturðu leiðrétt snúninginn með þessari stillingu.
* **Fine position adjustments** - má nota til að leiðrétta mjög smávægilega tilfærslu/snúning. Þetta er hannað til að leiðrétta rek eða smávægilega hreyfingu ef laser hefur staðið yfir nótt eða í langan tíma.

{% hint style="info" %}
Athugaðu að leiðréttingar á stefnu / speglun breyta engu í 3D Visualiser. Þær á að nota til að leiðrétta úttak raunverulega lasersins þannig að það passi við það sem sést í 3D Visualiser!
{% endhint %}

### Afrita laserstillingar

Sjá [#copy-laser-settings](laser-settings.md#copy-laser-settings).

### Scanner stillingar

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed stillingin ákvarðar hversu hratt scanner-arnir hreyfast.

{% hint style="danger" %}
Þótt sjálfgefnu stillingarnar séu nokkuð varfærnar geturðu samt skemmt scanner-ana ef þú keyrir þá of hratt. Farðu varlega, sérstaklega þegar þú hækkar hraðann.
{% endhint %}

{% hint style="info" %}
Þessi Speed stilling breytir ekki punktahraðanum, heldur stillir hún hversu dreifðir punktarnir eru. Nánari upplýsingar eru í [how-liberation-generates-laser-content.md](../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Geislinn skiptir um lit og kveikir og slekkur á sér á meðan scanner-arnir færa hann til, og þessi tvö atriði eru yfirleitt ekki fullkomlega samstillt. Stilltu þetta til að koma þeim aftur í takt.

{% hint style="info" %}
Þetta er stundum kallað _blank shift_ en mér finnst heitið _scanner sync_ betra - það er aðeins nákvæmara þar sem það stillir tímasetningu allra litabreytinga miðað við hreyfingu scanner-anna.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser „halar“ - Colour shift er ekki rétt stillt</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Engir laser „halar“! Colour shift er gott!</p></figcaption></figure></div>

Ef þú sérð litla „hala“ í úttaki lasersins er líklegt að stilla þurfi scanner sync. Ef halarnir birtast áfram sama hvað þú stillir, ertu líklega að keyra scanner-ana/laser driver-ana hraðar en þeir ráða við. Prófaðu að lækka scanner speed.

#### Scanner forstillingar

Notaðu þetta til að velja fyrirfram hannaða scanner stillingu. Sjálfgefni valkosturinn er yfirleitt í lagi, þannig að þú ættir ekki að þurfa að breyta þessari stillingu nema þú sért með sérstaklega lélega (eða góða) scanner-a. Ef þú vilt kafa dýpra, sjá [scanner-presets.md](../advanced/scanner-presets.md)

#### Litakvörðun

Þú getur notað þetta kerfi til að leiðrétta birtuferil og hvítjafnvægi lasersins. Sjá [colour-calibration.md](../advanced/colour-calibration.md)

#### Ítarlegar stillingar

Þú ættir ekki að þurfa að fikta í þessu, en ef þú ert forvitinn, sjá [advanced-laser-settings.md](../advanced/advanced-laser-settings.md)
