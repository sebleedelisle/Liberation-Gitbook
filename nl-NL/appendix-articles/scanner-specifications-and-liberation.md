---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Scannerspecificaties en Liberation

### De rommelige werkelijkheid van scannerspecificaties

Puntfrequenties en scannerspecificaties kunnen best verwarrend zijn. Je ziet vaak specificaties zoals 30kpps @ 8º of 50kpps @ 4º, maar wat die getallen precies betekenen is niet altijd duidelijk.

{% hint style="info" %}
Disclaimer - ik ben geen specialist in scannerhardware, maar ik heb wel jaren praktische ervaring met het er goed uit laten zien van scanners van allerlei verschillende kwaliteitsniveaus via software en pointstream-generatie, in plaats van hardwareafstelling. Dit is gebaseerd op die ervaring.
{% endhint %}

#### **Waar deze getallen vandaan komen**

Termen zoals “30K” en “50K” zijn afkortingen die zijn gebaseerd op hoe scanners worden beoordeeld met het ILDA-testpatroon bij die puntfrequenties onder specifieke omstandigheden.

Wanneer een scanner wordt opgegeven als bijvoorbeeld: _30Kpps @ 8°_ betekent dat eigenlijk:

> “Deze scanner kan het ILDA-testpatroon weergeven op 30.000 punten/sec bij een scanhoek van 8°, mits goed afgesteld.”

Het is geen volledige of volledig gestandaardiseerde meting van prestaties in de praktijk. Sterker nog: het was oorspronkelijk helemaal niet bedoeld als benchmark, maar werd gebruikt voor een **afstelprocedure**. Je draait een bekend patroon op een vaste puntfrequentie (bijv. 30.000 punten/sec) en past damping en gain aan totdat het er correct uitziet.

Maar het is nog steeds de meestgebruikte referentie die we hebben, en het kan je een goed beeld geven van de kwaliteit van de scanners, in elk geval bij gerenommeerde fabrikanten. Bij _minder gerenommeerde_ fabrikanten daarentegen...

#### Scanners testen met Libera Lab

{% hint style="danger" %}
**Dit is een geavanceerde techniek en je kunt je scanners beschadigen als je niet voorzichtig bent. Niet aanbevolen tenzij je weet wat je doet.**
{% endhint %}

Als je buiten een showproject wilt experimenteren met het gedrag van scanners, gebruik dan [Libera Lab](https://github.com/sebleedelisle/libera-lab/releases). Dit is een desktoptool voor Libera-compatibele lasercontrollers, bedoeld om laseroutput te ontdekken, te testen, te previewen en te inspecteren.

<figure><img src="../.gitbook/assets/libera-lab-screenshot.png" alt="Libera Lab showing the ILDA test pattern, point-rate controls, controller list and scanner-load meter"><figcaption><p>Libera Lab can output known patterns, stream ILDA files and show a scanner-load estimate for the current point stream.</p></figcaption></figure>

Libera Lab is handig omdat je hiermee:

* bekende testpatronen kunt uitvoeren, waaronder het ILDA-testpatroon
* ILDA-bestanden kunt laden en streamen
* de puntenstream kunt previewen vóór of tijdens de output
* de output kunt inspecteren met tools voor scope en scannerbelasting
* kunt vergelijken hoe verschillende patronen, puntsnelheden en outputgroottes de scanners beïnvloeden

Als je scanners wilt testen aan de hand van een gepubliceerde specificatie, stel Libera Lab dan in op het [ILDA-testpatroon](https://ilda.com/technical.htm?r=7950), kies de gespecificeerde puntsnelheid en pas de outputgrootte aan aan de opgegeven scanhoek (bijv. 8°). Raadpleeg de ILDA-documentatie voor advies over hoe je de output analyseert.

#### Waarom het misschien geen goede benchmark is

Om te beginnen kan je testpatroon er verkeerd uitzien, zelfs als je scanners goed zijn, omdat ze niet zijn afgesteld op een manier die daarvoor is geoptimaliseerd.

Het kan een nuttige algemene richtlijn zijn voor “goede” versus “slechte” scanners, maar fabrikanten gaan soms vrij losjes om met deze specificaties.

#### Hoe kies ik dan een goede scanner?

Ik zou vooral zorgen dat ze van een gerenommeerde fabrikant komen. Dure high-end scannerfabrikanten zoals Cambridge Technology (CT), Eye Magic (EMS) en ScannerMAX (een dochterbedrijf van Pangolin) zijn altijd goed en daar kun je eigenlijk niet mis mee gaan. Maar als een scannerset rond de $1000 kost, is dat voor veel van ons in het begin duurder dan onze lasers!

Daarom heb ik vooral Chinese fabrikanten gebruikt. Dragon Tiger (DT)-scanners zijn degelijk en betaalbaar, en ik denk dat LightSpace ze gebruikt. Veel andere fabrikanten (waaronder OPT en Able in sommige modellen) gebruiken ook systemen op basis van DT.

Phenix Technology (PT) zit over het algemeen in een lagere klasse, maar eerlijk gezegd zijn ze waarschijnlijk prima voor de meeste toepassingen.

**Als je scanners merkloos zijn, is dat waarschijnlijk het moment waarop je je zorgen moet maken over de kwaliteit!**

#### Hoe Liberation helpt

Allereerst heb je voor de meeste dingen echt geen extreem dure scanners nodig! Betaalbare 30kpps DT, of zelfs PT, is prima. De standaard scannerinstellingen zijn bewust conservatief en meestal _hoef je ze niet aan te passen_ (behalve _Scanner sync_).

Als je wilt begrijpen wat de scannerinstellingen werkelijk doen, is Libera Lab een betere plek om te experimenteren dan je showproject. Je kunt de puntsnelheid, outputhoek en het testpatroon wijzigen terwijl je de preview, scope en informatie over scannerbelasting bekijkt.

Zelfs als je betere scanners hebt, heeft het geen zin om ze harder aan te sturen dan nodig is. Dit verlengt hun levensduur aanzienlijk.

#### Wat is een "point stream"?

Je hebt deze term waarschijnlijk al eerder gehoord - dit is hoe we het pad van de scanners aansturen.

Een point stream is een lijst met X/Y-posities, elk met een kleur. Om bijvoorbeeld een witte lijn te tekenen, stuur je een reeks punten langs die lijn, allemaal ingesteld op wit. De scanners bewegen vervolgens van punt naar punt met een vaste snelheid - de points per second rate (PPS) - en de straal tekent zo de vorm.

#### Hoe dit werkt in traditionele lasersoftware

Traditionele lasersoftware slaat voor elke cue een point stream op. Bij geanimeerde cues betekent dat meestal een aparte point stream voor elk frame. Het belangrijkste punt is dat alles volledig vooraf is bepaald. Daardoor zorgt het verhogen van de puntfrequentie ervoor dat de scanners sneller door dezelfde vooraf gedefinieerde data bewegen.

{% hint style="info" %}
Voor oudere software was deze aanpak noodzakelijk - computers waren simpelweg niet snel genoeg om point streams in realtime te genereren. Daarom is er meestal een aparte cue-editor, die wordt gebruikt om de data voor elk animatieframe vooraf te genereren.

Dit verklaart ook waarom content gigabytes aan ruimte kan innemen. Je slaat in feite grote, ongecomprimeerde golfvormen op met behoorlijk hoge samplerates.
{% endhint %}

#### Waarom "point rate" minder betekenis heeft in Liberation

Liberation genereert de point stream in realtime, wat ons enorm veel flexibiliteit geeft. Let op de instelling "Scanner speed" in het paneel Laser Settings. Hiermee kunnen we de scanners versnellen en vertragen, maar belangrijk is dat dit **niet** de onderliggende puntfrequentie (PPS) verandert.

#### Wacht, wat? Hoe dan?

Ik weet het, het klinkt in het begin vreemd.

Omdat Liberation de point stream in realtime genereert, kan het die point stream aanpassen. Hoe verder de punten uit elkaar liggen, hoe sneller de scanners bewegen. Hoe dichter ze bij elkaar liggen, hoe langzamer de scanners bewegen.

{% hint style="info" %}
In recente versies van Liberation heeft de daadwerkelijke _point rate_ (in de geavanceerde instellingen) helemaal geen invloed op de scannersnelheid. In plaats daarvan past de renderer de puntverdeling aan de geselecteerde puntfrequentie aan, terwijl de beweging van de scanners hetzelfde blijft.

Dit heeft wel invloed op de "resolutie" van het puntpad, maar dat maakt vooral verschil bij graphics (en kan helpen bij het fijner afstellen van de instelling _scanner sync_).
{% endhint %}

#### Mooi! Dus wat betekent dit nu eigenlijk allemaal?

Goede vraag. Dit zijn mijn tips:

* Vermijd merkloze scanners. Als je snellere scanners kunt krijgen, doe dat dan - minimaal 30KPPS.
* In de meeste gevallen zijn DT30-scanners prima, en PT30-scanners zijn waarschijnlijk OK in goedkopere lasers.
* Als je graphics doet, zijn meer lasers in de meeste gevallen beter dan snellere scanners.
* Zodra je bij high-end setups komt, zijn alle gevestigde high-end merken prima.
* Als je alleen de goedkoopste merkloze scanners kunt krijgen, zijn de standaardinstellingen van Liberation vrij conservatief en krijg je waarschijnlijk acceptabele resultaten voor basis-beamwerk. Als het moeizaam gaat, verlaag dan de instelling **Speed** (maar verander de puntfrequentie niet!).
* Als je instellingen wilt testen of vergelijken, doe dat dan eerst in Libera Lab in plaats van te experimenteren in een showbestand.

#### En het ILDA Test Pattern?

…is nog steeds erg nuttig als kalibratie- en referentietool, en Libera Lab maakt het gemakkelijker om het uit te voeren en te inspecteren. Maar het was nooit bedoeld als volledige benchmark en kan door fabrikanten verkeerd worden gebruikt of ruim worden geïnterpreteerd.
