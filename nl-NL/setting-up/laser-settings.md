---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Paneel Laser output settings

Open het instellingenpaneel _Laser output_ via het menu _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Hier zie je de instellingen voor de momenteel geselecteerde laser. Je kunt een andere laser selecteren:

* via de nummerknop in het paneel _Laser overview_
* met een cijfertoets op je toetsenbord; de toetsen 1 t/m 0 openen lasers 1 t/m 10
* met de `Tab`-toets om door de lasers te bladeren (`Shift + Tab` gaat terug).

Bovenaan dit paneel zie je:

* een nummerknop - klik hierop om deze laser te armen/disarmen. De knop is rood wanneer de laser armed is.
* een _Brightness_-schuifregelaar, alleen voor deze laser. Let op: deze wordt gecombineerd met de globale brightness.
* een _Test Pattern_-schakelaar en patroonselectie. Hiermee kies je een specifiek testpatroon voor alleen deze laser. (Deze bedieningselementen worden gespiegeld in de werkbalk van de Output-weergave).

### Output-oriëntatie / correctie van spiegeling

De volgende opties zijn bedoeld om de set-up van je laser te corrigeren, zodat deze zich consistent gedraagt in Liberation.

* **Flip horizontal / vertical** - met deze opties kun je de output van je laser corrigeren

{% hint style="info" %}
Je hoeft de instellingen voor horizontal / vertical flip normaal gesproken niet te wijzigen, tenzij je laser verkeerd is bekabeld of X/Y-flipknoppen aan de achterkant heeft die niet goed staan ingesteld. Als je de output voor een specifieke clip wilt spiegelen, kun je dat op de clip zelf doen.
{% endhint %}

* **Orientation** - als je laser op zijn kant of ondersteboven is opgehangen, kun je met deze instelling de rotatie corrigeren.
* **Fine position adjustments** - hiermee kun je heel kleine verschuivingen/rotaties corrigeren. Bedoeld om drift/zakken te corrigeren als een laser een nacht of langere tijd heeft gestaan.

{% hint style="info" %}
Let op: de correcties voor orientation / mirroring veranderen niets in de 3D Visualiser. Gebruik ze om de output van de echte laser te laten overeenkomen met wat je in de 3D Visualiser ziet!
{% endhint %}

### Laserinstellingen kopiëren

Zie [#copy-laser-settings](laser-settings.md#copy-laser-settings "mention").

### Scanner settings

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

De instelling Speed bepaalt hoe snel de scanners bewegen.

{% hint style="danger" %}
Hoewel de standaardinstellingen vrij behoudend zijn, kun je je scanners nog steeds beschadigen als je ze te snel aanstuurt. Wees voorzichtig, vooral wanneer je de snelheid verhoogt.
{% endhint %}

{% hint style="info" %}
Deze Speed-instelling verandert de point rate niet, maar past aan hoe ver die punten uit elkaar liggen. Zie voor meer informatie [how-liberation-generates-laser-content.md](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

De beam verandert van kleur en gaat aan en uit terwijl de scanners hem rondbewegen. Deze twee dingen lopen meestal niet perfect synchroon. Pas deze instelling aan om ze weer op één lijn te krijgen.

{% hint style="info" %}
Dit wordt soms _blank shift_ genoemd, maar persoonlijk geef ik de voorkeur aan de term _scanner sync_ - die is iets nauwkeuriger, omdat hiermee de timing van alle kleurveranderingen ten opzichte van de scannerbeweging wordt aangepast.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser-"tails" - Colour shift niet goed ingesteld</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Geen laser-"tails"! Colour shift goed!</p></figcaption></figure></div>

Als je kleine "tails" in je laseroutput ziet, moet de scanner sync waarschijnlijk worden bijgesteld. Als de tails blijven verschijnen, wat je ook instelt, stuur je je scanners/laserdrivers waarschijnlijk sneller aan dan ze aankunnen. Probeer de scannersnelheid te verlagen.

#### Scanner presets

Gebruik dit om een vooraf ontworpen scannerinstelling te kiezen. De standaardoptie is meestal prima, dus je hoeft deze instelling normaal gesproken niet te wijzigen, tenzij je bijzonder slechte (of juist goede) scanners hebt. Als je dieper wilt ingaan op de details, zie [scanner-presets.md](../advanced/scanner-presets.md "mention")

#### Colour calibration

Met dit systeem kun je de helderheidscurve en witbalans van je laser corrigeren. Zie [colour-calibration.md](../advanced/colour-calibration.md "mention")

#### Advanced settings

Je hoeft hier normaal gesproken niet aan te zitten, maar als je nieuwsgierig bent, zie [advanced-laser-settings.md](../advanced/advanced-laser-settings.md "mention")
