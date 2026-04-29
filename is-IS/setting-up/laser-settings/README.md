# ✅ Stillingaspjaldið Laser output

Opnaðu stillingaspjaldið _Laser output_ í valmyndinni _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Þá birtast stillingar fyrir leysinn sem er valinn hverju sinni. Þú getur skipt um valinn leysi:

* með númerahnappinum hans í _Laser overview_ spjaldinu
* með númeralykli á lyklaborðinu; takkarnir 1 til 0 opna leysi 1–10
* með `Tab` lyklinum til að fletta í gegnum leysana (`Shift + Tab` fer afturábak).

Efst á þessu spjaldi sérðu:

* númerahnapp — smelltu á hann til að skipta þessum leysi á milli armed og disarmed. Hann er rauður þegar leysirinn er armed.
* _Brightness_ sleða sem gildir aðeins fyrir þennan leysi. Athugaðu að þetta sameinast Global Brightness.
* _Test Pattern_ rofa og mynsturval. Þetta gerir þér kleift að velja tiltekið test pattern aðeins fyrir þennan leysi. (Þessar stýringar eru einnig í tækjastikunni í Output view.)

### Stefna Output / leiðrétting á speglun

Næstu atriði eru til að leiðrétta uppsetningu leysisins svo hann hegði sér samræmt í Liberation.

* **Flip horizontal / vertical** — þessir valkostir gera þér kleift að leiðrétta Output frá leysinum

{% hint style="info" %}
Þú ættir ekki að þurfa að breyta stillingunum fyrir lárétta/lóðrétta speglun nema leysirinn sé rangt tengdur eða hann sé með X/Y flip-hnappa aftan á sem eru ekki rétt stilltir. Ef þú vilt spegla Output fyrir tiltekið Clip er það gert á Clip sjálfu.
{% endhint %}

* **Orientation** — ef leysirinn hefur verið riggaður á hlið eða á hvolf geturðu leiðrétt snúninginn með þessari stillingu.
* **Fine position adjustments** — má nota til að leiðrétta mjög litlar hliðranir eða snúning. Þetta er ætlað til að leiðrétta rek eða sig ef leysir hefur verið skilinn eftir yfir nótt eða í langan tíma.

{% hint style="info" %}
Athugaðu að leiðréttingar á stefnu/speglun breyta engu í 3D Visualiser. Þær á að nota til að láta raunverulegt Output leysisins passa við það sem sést í 3D Visualiser!
{% endhint %}

### Afrita laser settings

Sjá [Afrita laser settings](./#copy-laser-settings).

### Skannastillingar

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed stillingin ræður því hversu hratt skannarnir hreyfast.

{% hint style="danger" %}
Þótt sjálfgefnu stillingarnar séu nokkuð varfærnar geturðu samt skemmt skannana ef þú keyrir þá of hratt. Farðu varlega, sérstaklega þegar þú hækkar Speed.
{% endhint %}

{% hint style="info" %}
Þessi Speed stilling breytir ekki punktahraðanum; hún stillir í staðinn hversu dreifðir punktarnir eru. Nánari upplýsingar eru í [Hvernig Liberation býr til leysiefni](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Geislinn skiptir um lit og kveikir og slekkur á sér á meðan skannarnir hreyfa hann um svæðið, og þessi tvö atriði eru yfirleitt ekki fullkomlega samstillt. Stilltu þetta til að koma þeim aftur í takt.

{% hint style="info" %}
Þetta er stundum kallað _blank shift_, en mér finnst persónulega _scanner sync_ betra heiti — það er aðeins nákvæmara þar sem stillingin breytir tímasetningu allra litabreytinga miðað við hreyfingu skannans.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>„Halar“ í leysinum — Colour shift er ekki rétt stillt</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Engir „halar“ í leysinum! Colour shift er í lagi!</p></figcaption></figure></div>

Ef þú sérð litla „hala“ í Output frá leysinum þarf líklega að stilla Scanner sync. Ef halarnir sjást samt sama hvað þú gerir ertu líklega að keyra skannana eða leysidrifin hraðar en þau ráða við. Prófaðu að lækka Speed fyrir skannana.

#### Scanner presets

Notaðu þetta til að velja fyrirfram hannaða skannastillingu. Sjálfgefni valkosturinn er yfirleitt í lagi, þannig að þú ættir ekki að þurfa að breyta þessari stillingu nema skannarnir þínir séu sérstaklega slæmir (eða góðir). Ef þú vilt skoða þetta nánar, sjá [Scanner presets](../../advanced/scanner-presets.md)

#### Colour calibration

Þú getur notað þetta kerfi til að leiðrétta birtukúrfu og hvítjöfnun leysisins. Sjá [Colour calibration](../../advanced/colour-calibration.md)

#### Advanced settings

Þú ættir ekki að þurfa að fikta í þessum stillingum, en ef þú ert forvitin(n), sjá [Advanced laser settings](../../advanced/advanced-laser-settings.md)
