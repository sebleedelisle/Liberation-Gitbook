---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Positiegebaseerde changers

Deze familie nodes past content aan op basis van positie. Standaard wordt het effect toegepast langs een horizontale as (van links naar rechts), maar je kunt deze as naar elke gewenste hoek draaien. Elke node heeft ook een _radial_ modus, waarbij het effect wordt bepaald door de hoek van elk punt ten opzichte van het midden.

* **Colour Changer by Position** – past een verloop toe over de gekozen as of rond de radiale hoek.\
  \&#xNAN;_Voorbeeld: maak een regenboogverloop dat over een lijn beweegt, of gebruik radial mode op een cirkel voor een kleurenwiel-effect._
* **Wave Shift by Position** – past een sinusgolfvervorming toe, waarbij de content verticaal wordt verschoven (of loodrecht op de gekozen as).\
  \&#xNAN;_Voorbeeld: laat een lijn rimpelen als water, of gebruik radial mode om een cirkel vanuit het midden naar buiten te laten pulseren._
* **Noise Shift by Position** – past een simplex-noisevervorming toe, waarbij de content verticaal wordt verschoven (of loodrecht op de gekozen as).\
  \&#xNAN;_Voorbeeld: zie het voorbeeld bij Wave Shift, maar dan met een organischer en willekeuriger karakter; ideaal om natuurlijke variatie toe te voegen._

## &#x20;Colour change by position

Deze node past kleurwijzigingen toe op je content op basis van positie. Standaard is de as horizontaal (0°), maar je kunt de as draaien of overschakelen naar radial mode.

* **wavelength** – bepaalt de grootte van de herhalende kleurcyclus.
  * _Linear mode:_ bij 100% beslaat één volledige cyclus de volledige breedte van de content.
  * _Radial mode:_ bij 100% beslaat één volledige cyclus de volledige cirkel (360°). Waarden zijn percentages van de cirkel: bijvoorbeeld 50% = een halve cirkel (180°).
* **offset** – verschuift het startpunt van de kleurcyclus, als percentage van de wavelength. Je kunt dit moduleren (bijvoorbeeld met een sawtooth oscillator) om vloeiend door kleuren te lopen.
* **repeat** – als dit is ingeschakeld, wordt de cyclus over de content herhaald. Als dit is uitgeschakeld, wordt het verloop maar één keer toegepast: alles vóór het begin krijgt de startkleur, alles na het einde krijgt de eindkleur.
* **pingpong** – als dit is ingeschakeld, wisselt elke herhaling van richting, waardoor een gespiegeld effect ontstaat. Als _Repeat_ is uitgeschakeld, loopt het verloop één keer vooruit en daarna terug. _Opmerking: in Pingpong mode omvat de wavelength zowel de heen- als de terugbeweging._
* **linear angle** – draait de as van het effect. 0° = horizontaal.
* **radial** – schakelt over naar radial mode, waarbij kleuren worden toegepast op basis van de hoek vanaf het midden.
* **radial smooth loop** – past de wavelength automatisch aan zodat deze gelijkmatig in 100% van de cirkel past. Zo voorkom je een zichtbare naad waar de cyclus rondloopt.
* **legacy mode** – schakelt terug naar de oudere HSB-sliders voor begin/einde. Laat dit uit om de nieuwere verloopeditor te gebruiken.

**Colour Modes**

Deze bepalen welke onderdelen van de kleuraanpassingen op de content worden toegepast. Zie ook: [Kleurinstellingen en HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – hue blijft ongewijzigd.
  * _FIXED_ – hue wordt vastgezet op een vaste waarde.
  * _SHIFTED_ – hue wordt verschoven met de opgegeven hoeveelheid (elementen met verschillende kleuren blijven onderscheidbaar, maar worden samen rond het kleurenwiel verschoven).
* **saturation mode**
  * _OFF_ – saturation blijft ongewijzigd.
  * _FIXED_ – saturation wordt ingesteld op de opgegeven waarde.
* **brightness mode**
  * _OFF_ – brightness blijft ongewijzigd.
  * _FIXED_ – brightness wordt ingesteld op de opgegeven waarde.
  * _MULTIPLY_ – brightness wordt geschaald met de opgegeven waarde. Dit behoudt dynamiek (bijvoorbeeld: knipperende elementen blijven knipperen, maar binnen het beperkte helderheidsbereik).

**Verloopeditor**

Gebruikt dezelfde verloopeditor als [Colour Changer](colour-changer.md "mention"), maar koppelt het verloop op basis van positie aan de inhoud.

* Klik op de verloopbalk om een kleurstop toe te voegen.
* Klik met de linkermuisknop op een stop om deze te selecteren en sleep deze daarna zijwaarts om hem te verplaatsen.
* Sleep een geselecteerde stop omlaag, weg van de balk, of druk op Delete/Backspace om deze te verwijderen. Een verloop behoudt altijd minstens twee stops.
* Klik met de rechtermuisknop op een stop om deze met de kleurkiezer te bewerken.
* Gebruik **Position**, **Hue**, **Saturation** en **Brightness** om de geselecteerde stop nauwkeurig te bewerken.
* **interpolation** bepaalt hoe kleuren tussen stops worden gemengd:
* **HSB** – mengt hue, saturation en brightness. Dit is het meest geschikt voor vloeiende regenboogachtige bewegingen rond het kleurenwiel.
* **RGB** – mengt waarden voor rood, groen en blauw rechtstreeks. Dit voelt vaak meer als een kleurovergang op een scherm of lichttafel.
* **NONE** – springt zonder overgang van de ene stop naar de volgende.
* **hue direction** is beschikbaar bij HSB-interpolatie:
* **AUTO** – neemt de kortste route rond het hue-wiel.
* **FORWARDS** – loopt altijd vooruit door de hue-waarden.
* **BACKWARDS** – loopt altijd achteruit door de hue-waarden.
* **blend** – mengt de kleurwijziging met de oorspronkelijke kleuren. Bij 100% vervangt het effect de oorspronkelijke kleuren volledig.

**Verouderde start-/eindwaarden**

Als **legacy mode** aan staat, wordt de verloopeditor vervangen door de oudere bedieningselementen:

* **start hue / end hue** – hue aan het begin en einde van het bereik.
* **start saturation / end saturation** – saturation aan het begin en einde van het bereik.
* **start brightness / end brightness** – brightness aan het begin en einde van het bereik.

**Voorbeeld 1: verschuivend regenboogverloop**

Begin met de standaardinstellingen:

1. Laat de node in **Linear** mode staan (hoek van 0° = horizontaal).
2. Laat **wavelength** op 100% staan (beslaat de volledige breedte en zou de standaardwaarde moeten zijn).
3. Laat het standaardverloop staan.
4. Schakel **repeat** in.
5. Voeg een **Sawtooth Oscillator** toe aan de instelling **offset**, die van 0% naar 100% loopt.

***

**Voorbeeld 2: zwart-wit-zwart-verloop (Pingpong)**

Begin met de standaardinstellingen:

1. Laat de node in **Linear** mode staan (hoek van 0° = horizontaal).
2. Laat **wavelength** op 100% staan (beslaat de volledige breedte en zou de standaardwaarde moeten zijn).
3. Schakel **repeat** uit.
4. Zet de eerste verloopstop op zwart.
5. Zet de laatste verloopstop op wit.
6. Zet **hue mode** OFF.
7. Zet **saturation mode** op FIXED als je het resultaat naar grijswaarden wilt forceren.
8. Zet **brightness mode** op FIXED.
9. Schakel **pingpong** in.

_Resultaat: het verloop gaat over de breedte van zwart naar wit en daarna terug naar zwart._\
Let op: als je wilt dat de content zijn hue en saturation behoudt, zet Saturation mode dan op OFF. \\

***

**Voorbeeld 3: roterend regenboogwiel (Radial)**

1. Schakel **radial** mode in.
2. Zet **wavelength** op 100% (een volledige sweep van 360°).
3. Schakel **repeat** in.
4. Voeg een **Sawtooth Oscillator** toe aan de instelling **offset**, die van 0% naar 100% loopt.

_Resultaat: een naadloos kleurenwiel dat continu rond de cirkel draait._

## &#x20;Wave shift by position

Deze node past een golfvervorming toe over je content, waarbij punten loodrecht op de gekozen as worden verschoven (of radiaal vanaf het midden).

* **Wavelength** – bepaalt de lengte van de golfcyclus.
  * _Linear mode:_ bij 100% beslaat één volledige cyclus de volledige breedte van de content.
  * _Radial mode:_ bij 100% beslaat één volledige cyclus de volledige 360°. (Waarden zijn percentages van de cirkel: 50% = een halve draai, 25% = een kwart draai, enzovoort.)
* **Size** – bepaalt de amplitude van de golf (hoe ver de content wordt verplaatst).
* **Offset** – verschuift de golf langs de as (of rond de cirkel in radial mode). Dit is een percentage van de wavelength, zodat je dit met een **Oscillator Node** kunt animeren om de golf te laten bewegen.
* **Radial** – schakelt van linear naar radial mode, zodat de verplaatsing wordt gebaseerd op de hoek vanaf het midden.
* **Radial Smooth Loop** – past de wavelength aan zodat deze gelijkmatig in 100% van de cirkel past. Zo voorkom je zichtbare naden bij het rondlopen.
* **Triangle** – verandert de golfvorm van sinus naar driehoek.
* **Absolute** – neemt de absolute waarde van de golf, waardoor alleen opwaartse verplaatsingen ontstaan (de negatieve kant wordt over de positieve gevouwen).
* **Angle** – draait de as van de golf. 0° = horizontaal.

## &#x20;Noise shift by position

Deze node vervormt content met een noise field (zoals turbulentie), waarbij punten loodrecht op de gekozen as worden verschoven (of radiaal vanaf het midden). Vergeleken met _Wave Shift_ is het resultaat organischer en willekeuriger.

* **Detail** – bepaalt hoe fijn de noise is. Hogere waarden = scherpere, gedetailleerdere variatie. Lagere waarden = vloeiendere variatie.
* **Wavelength** – bepaalt de schaal van het noisepatroon.
  * _Linear mode:_ bij 100% beslaat één volledige noisecyclus de breedte van de content.
  * _Radial mode:_ bij 100% beslaat één volledige cyclus de volledige 360°.
* **Size** – bepaalt de hoeveelheid verplaatsing (de amplitude van de noisevervorming).
* **Offset** – verschuift het noisepatroon langs de as (of rond de cirkel). Dit is een percentage van de wavelength, zodat je dit met een **Oscillator Node** kunt animeren om de noise te laten “stromen”.
* **Depth Offset** – beweegt door het 3D-noiseveld en creëert variatie in de tijd. Dit is vooral effectief wanneer je het animeert met een Oscillator Node.
* **Depth Detail** – bepaalt hoe gedetailleerd de variatie is over de dieptedimensie.
* **Absolute** – neemt de absolute waarde van de noise, waardoor negatieve waarden naar positieve waarden worden gevouwen (dit geeft alleen eenzijdige verplaatsing).
* **Angle** – roteert de as van de noise in lineaire modus. 0° = horizontaal.
* **Radial** – schakelt van linear naar radial mode, zodat de verplaatsing wordt gebaseerd op de hoek vanaf het midden.
* **Radial Smooth Loop** – past de wavelength aan zodat deze gelijkmatig in 100% van de cirkel past. Zo voorkom je zichtbare naden in radial mode.
