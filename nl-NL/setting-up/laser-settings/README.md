# ✅ Paneel Laser output settings

Open het instellingenpaneel _Laser output_ via het menu _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Je ziet nu de instellingen voor de momenteel geselecteerde laser. Je kunt deze laser wijzigen:

* via de nummerknop in het paneel _Laser overview_
* met een cijfertoets op je toetsenbord; toetsen 1 t/m 0 openen lasers 1 - 10
* met de `Tab`-toets om door de lasers te bladeren (`Shift + Tab` gaat terug).

Bovenaan dit paneel zie je:

* een nummerknop - klik hierop om deze laser te activeren/deactiveren. De knop is rood wanneer de laser actief is.
* een _Brightness_-schuifregelaar alleen voor deze laser. Let op: deze wordt gecombineerd met de globale brightness.
* _Test Pattern_-schakelaar en patroonselector. Hiermee kies je een specifiek testpatroon alleen voor deze laser. (Deze bedieningselementen worden ook weergegeven in de werkbalk van de Output-weergave).

### Uitvoeroriëntatie / spiegelcorrectie

De volgende elementen zijn bedoeld om de setup van je laser te corrigeren, zodat deze zich consistent gedraagt in Liberation.

* **Flip horizontal / vertical** - met deze opties kun je de uitvoer van je laser corrigeren

{% hint style="info" %}
Je zou de instellingen voor horizontal / vertical flip niet hoeven te wijzigen, tenzij je laser verkeerd is bekabeld of X/Y-flipknoppen aan de achterkant heeft die niet goed staan. Als je de uitvoer voor een specifieke clip wilt spiegelen, kun je dat op de clip zelf doen.
{% endhint %}

* **Orientation** - als je laser op zijn kant of ondersteboven is gemonteerd, kun je de rotatie met deze instelling corrigeren.
* **Fine position adjustments** - kun je gebruiken om zeer kleine verschuivingen/rotaties te corrigeren. Bedoeld om drift/verzakking te corrigeren als een laser een nacht of langere tijd heeft gestaan.

{% hint style="info" %}
Let op: de oriëntatie- en spiegelcorrecties veranderen niets in de 3D Visualiser. Ze zijn bedoeld om de uitvoer van de echte laser te laten overeenkomen met wat je in de 3D Visualiser ziet!
{% endhint %}

### Laserinstellingen kopiëren

Zie [Paneel Laser output settings](./#copy-laser-settings "mention").

### Scannerinstellingen

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

De speed-instelling bepaalt hoe snel de scanners bewegen.

{% hint style="danger" %}
Hoewel de standaardinstellingen vrij voorzichtig zijn, kun je je scanners nog steeds beschadigen als je ze te snel aanstuurt. Wees voorzichtig, vooral wanneer je de snelheid verhoogt.
{% endhint %}

{% hint style="info" %}
Deze speed-instelling verandert de point rate niet, maar past aan hoe ver die punten uit elkaar liggen. Zie voor meer informatie [◼️ Hoe Liberation lasercontent genereert](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

De straal verandert van kleur en gaat aan en uit terwijl de scanners hem rondsturen. Deze twee dingen lopen meestal niet perfect synchroon. Pas deze instelling aan om ze weer op één lijn te krijgen.

{% hint style="info" %}
Dit wordt soms _blank shift_ genoemd, maar persoonlijk geef ik de voorkeur aan _scanner sync_ - dat is iets nauwkeuriger, omdat hiermee de timing van alle kleurveranderingen ten opzichte van de scannerbeweging wordt aangepast.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser-"staarten" - Colour shift niet goed ingesteld</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Geen laser-"staarten"! Colour shift goed!</p></figcaption></figure></div>

Als je kleine "staarten" in je laseruitvoer ziet, moet de scanner sync waarschijnlijk worden aangepast. Als de staarten blijven verschijnen, ongeacht de instelling, stuur je je scanners/laserdrivers waarschijnlijk sneller aan dan ze aankunnen. Probeer de scannersnelheid te verlagen.

#### Scanner presets

Gebruik dit om een vooraf ontworpen scannerinstelling te kiezen. De standaardoptie is meestal prima, dus je hoeft deze instelling normaal niet te wijzigen, tenzij je bijzonder slechte (of goede) scanners hebt. Als je dieper wilt duiken, zie [◼️ Scannerpresets & renderprofielen](../../advanced/scanner-presets.md "mention")

#### Colour calibration

Je kunt dit systeem gebruiken om de helderheidscurve en witbalans van je laser te corrigeren. Zie [Kleurkalibratie](../../advanced/colour-calibration.md "mention")

#### Advanced settings

Je zou hier niet aan hoeven te zitten, maar als je nieuwsgierig bent, zie [◼️ Geavanceerde laserinstellingen](../../advanced/advanced-laser-settings.md "mention")
