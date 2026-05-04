---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Effecten

Het effects-systeem in Liberation is een leuke en veelzijdige manier om de clip-output in realtime aan te passen. Effecten zijn volledig flexibel en kunnen worden gebruikt om alles aan en uit te laten knipperen, te laten draaien, kleuren te veranderen of zelfs willekeurig rond te laten vliegen!

Alles wat je in de clip-editor kunt doen, kun je als effect gebruiken. Effecten worden zelfs bewerkt met exact dezelfde node-editor als clips! Zie [Effecten](effects.md#editing-effects "mention"). De creatieve mogelijkheden zijn vrijwel onbeperkt.

De standaard effectknoppen 1-8 staan onder de zoneknoppen, en effecten 9-24 zijn de kleine knoppen onderaan.

#### Een effect toepassen

Druk op een effectknop om het effect aan of uit te zetten, of nog beter: gebruik de APC40-sliders 1-8 om effecten in en uit te faden. Wil je een effect infaden zonder APC40, klik dan op de knop en sleep omhoog of omlaag. Of klik met de rechtermuisknop op de effectknop en pas de level-slider aan.

{% hint style="warning" %}
Als je op de effectknop drukt, wordt dat effect direct geactiveerd. Let er wel op dat er niets gebeurt als het level op nul staat! Klik op de knop en sleep om het level te wijzigen, klik met de rechtermuisknop en gebruik de _level_-slider, of gebruik de APC40-faders.
{% endhint %}

#### Effecten en de zone delay van de clip

Effecten nemen de zone delay-instelling over van elke clip die op dat moment draait. Dus als je clip een delay heeft die van links naar rechts beweegt en je voegt het flashing-effect toe, dan wordt de flash ook van links naar rechts vertraagd.

{% hint style="info" %}
Hoe de zone delay van de clip wordt overgenomen door effecten is zoiets dat extreem lastig uit te leggen is, maar meteen duidelijk wordt zodra je het probeert!

Ik zou zeggen dat dit een van de leukste en meest creatieve tools is die in Liberation zijn ingebouwd. Probeer het eens en je ziet wat ik bedoel!
{% endhint %}

#### Effectparameters

Voeg een parameter toe aan je effect met een _Parameter node._ Het Parameter-systeem is een manier om meerdere instellingen binnen je effect van buitenaf aan te passen. Zie [Parameter Control](clip-editor/oscillators/parameter-control.md "mention") voor meer informatie.

Gebruik de draaiknoppen 1-8 om de _parameter_ voor elk effect aan te passen. Of klik met de rechtermuisknop op de effectknop en pas de parameter-slider(s) aan. Wat de parameterwijziging doet, hangt af van hoe het effect is opgebouwd. Zie de lijst hieronder voor de standaardeffecten en wat hun parameters doen.

{% hint style="info" %}
Draaiknoppen 1-8 zitten langs de bovenrand van een APC40 Mk2 en rechtsboven op de Mk1. Zie ook: [APC40-referentie](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
De kleine getallen die je op de effectknoppen ziet, verwijzen naar het _level_ en de _parameter_ van het effect. Het _level_ wordt geregeld met de fader op de APC40, of je kunt op de knop klikken en slepen. De parameter wordt aangepast met de draaiknoppen op de APC40, of je kunt met de rechtermuisknop klikken om deze met de muis aan te passen.
{% endhint %}

#### De standaardeffecten

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Past een chaotische beweging toe op de clip-output. De parameter bepaalt de hoeveelheid/snelheid van de chaos.
2. **Sine wave** :\
   Vervormt alle content over een bewegende sinusgolf. De parameter bepaalt de golflengte.
3. **Rotation** :\
   Laat alles ronddraaien. De parameter bepaalt de draaisnelheid.
4. **Horizontal flip** :\
   Drukt alles horizontaal samen en rekt het uit. De parameter bepaalt de snelheid.
5. **Scale** :\
   Schaalt alles herhaaldelijk van volledig naar nul. De parameter bepaalt de snelheid.
6. **Hue** :\
Verandert de hue van alles, maar verandert de saturation niet (dus alles wat wit is blijft wit). De parameter bepaalt de hue.
7. **Saturation and hue** :\
Verandert de hue van alles en verzadigt de kleur ook volledig (dus alles wat wit is verandert naar de kleur). De parameter bepaalt de hue.
8. **Flash** :\
   Laat de helderheid van alles herhaaldelijk knipperen van volledig naar nul. De parameter bepaalt de knippersnelheid.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Er staan nog 16 extra kleureffecten op de onderste rij om vooraf ingestelde hue- en saturation-waarden toe te passen.

Let op: dit zijn de standaardeffecten, maar je kunt ze bewerken zodat ze bijna alles doen wat je wilt!

### Toepassen op groepen

Je kunt kiezen welke groepen door het effect worden beïnvloed. Klik met de rechtermuisknop en schakel de groepsselectievakjes met het label _Apply to groups_ in of uit.

Ik gebruik deze setup vooral wanneer ik canvas-graphics en laserstralen apart wil aansturen. Ik wijs alle canvas-clips toe aan groep 5 en sluit deze groep vervolgens uit van effecten waarvan ik niet wil dat ze deze grafische clips beïnvloeden.

Je kunt dit ook gebruiken om live twee verschillende kleurwijzigingen tegelijk toe te passen op twee groepen lasers. Maak twee effecten voor kleurwijziging en selecteer op welke clipgroepen elk effect wordt toegepast.

### MX group

Afkorting van _Mutually Exclusive_: dit is een manier om effecten zo te groeperen dat maar één effect in de groep tegelijk actief kan zijn. Let erop dat slechts één van de standaard kleurveranderingseffecten tegelijk actief kan zijn. Dit komt doordat ze allemaal in MX Group 1 zitten.

Deze functionaliteit is uitgeschakeld als de instelling _MX Group_ op 0 staat.

### Effecten bewerken

Klik met de rechtermuisknop op een effect en klik op de knop _EDIT EFFECT_ om de effect-editor te openen. Let op dat deze editor identiek is aan de Clip Editor!

Bewerk je effect op dezelfde manier als je een clip zou bewerken. Zie [De Clip Editor](clip-editor/ "mention").

Je hebt minstens één creator node nodig; dit kan van alles zijn (lijn, cirkel, vorm, zelfs tekst!), maar je kiest waarschijnlijk het best iets dat logisch is in de preview van de effectknop.

Wanneer effecten worden toegepast, worden alle creator nodes in het effect vervangen door de output van de clips die op dat moment draaien.

{% hint style="warning" %}
Om extreem vervelende technische redenen zijn de "trails"-nodes niet ingeschakeld binnen een effect. Hetzelfde geldt voor de instelling "delay" binnen pattern nodes (ze gebruiken hetzelfde systeem). Dit wordt opgelost in toekomstige versies.
{% endhint %}
