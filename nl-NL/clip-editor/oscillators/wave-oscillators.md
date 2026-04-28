---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Golf-oscillatoren

## Op deze pagina :

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Zaagtandgolf](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Driehoeksgolf](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sinusgolf](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Blokgolf](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Instellingen voor golf-oscillatoren

Alle golf-oscillatoren hebben de volgende instellingen :

* **range min / range max** - bepaalt het waardebereik voor de eigenschap die de oscillator aanstuurt. De eigenschap wordt ingesteld op _range min_ wanneer de golfvorm onderaan staat, en op _range max_ wanneer de golfvorm bovenaan staat.

{% hint style="info" %}
Als je bijvoorbeeld een punt naar links en rechts wilt laten bewegen tussen -100 en 100, verbind je de oscillator met de _x property socket_, stel je _range min_ in op -100 en _range max_ op 100.
{% endhint %}

* **duration** - de tijd die één volledige cyclus (of _loop_) nodig heeft om te voltooien. Dit is relatief aan het tempo in maten. Dus ¼ is één tel. 1 is een volledige maat, enzovoort.
* **duration multiplier** - schaalt de basisduur met een gekozen factor. Als **duration** bijvoorbeeld is ingesteld op een kwartnoot en de multiplier op 3 staat, duurt de oscillator drie kwartnoten (een gepunte halve noot). Fractionele multipliers worden ook ondersteund — houd _SHIFT_ ingedrukt terwijl je de slider sleept om niet-gehele getallen in te stellen. Dit is handig voor faserings-effecten of subtiele timingverschuivingen.
* **offset** - de startverschuiving van de golf als percentage van de duur. Als je wilt dat de golf op een kwart van de cyclus begint, stel je dit in op 25%.
* **repeat count** - het aantal keren dat de loop wordt afgespeeld voordat hij stopt. De standaardwaarde is _FOREVER_, maar je kunt dit aanpassen als je niet wilt dat de oscillator oneindig blijft lopen. Nadat hij stopt, wordt de eigenschap ingesteld op de waarde aan het einde van de golf.
* **delay count** - de vertraging in tellen voordat de oscillator begint te lopen. Voordat hij begint, wordt de eigenschap ingesteld op de waarde aan het begin van de golf.

{% hint style="info" %}
Met slim gebruik van _repeat count_ en _delay count_ kun je zeer complexe animaties maken, bijna alsof het een eigen tijdlijn is!
{% endhint %}

## Algemene instellingen

* **steps** - verdeelt de beweging in een aantal discrete stappen. Handig wanneer je eigenschappen wilt laten "springen" naar waarden in plaats van vloeiend te bewegen.

{% hint style="info" %}
Let op: de stappen worden verdeeld over de tijd, niet over de waarde. Dus bij een golf die is verdeeld in 4 stappen met een duration van 1 maat, verandert de eigenschap direct op elke tel.
{% endhint %}

* **clamp min / clamp max -** vergroot de schaal van de golf voorbij de minimale of maximale waarden en begrenst het resultaat.

{% hint style="info" %}
Het _clamp_-concept is best lastig uit te leggen, maar stel je voor dat de golfvorm boven of onder de grafiek uitkomt en vervolgens tegen de randen wordt vastgezet. Ik raad je aan ermee te experimenteren! Ze zijn erg handig als je wilt dat een zaagtand later begint of eerder eindigt.
{% endhint %}

* **ease function** - de Sawtooth- en Triangle-golven hebben ook een ease function die de animatiecurve subtiel verandert en je animaties veel expressiever kan maken!
  * **LINEAR** - de standaardinstelling, zonder easing; beweegt gewoon lineair tussen de min- en max-waarden.
  * **EASE OUT** - begint snel en vertraagt daarna richting het einde. Erg geschikt om fysica te simuleren, bijvoorbeeld afremmen tot stilstand.
  * **EASE IN** - begint langzaam en versnelt geleidelijk. Goed om opbouwend momentum te simuleren.
  * **EASE IN/OUT** - een combinatie van beide, voor een heel organische beweging.

{% hint style="warning" %}
**Easing -** Vermijd waar mogelijk de standaard lineaire animatie, tenzij je specifiek iets wilt dat robotachtig oogt. Easing kan je animaties veel vloeiender en organischer maken!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Zaagtandgolf

Wordt soms ook een _ramp waveform_ genoemd, omdat hij omhoog oploopt en aan het einde van de cyclus abrupt terugvalt. Dit is waarschijnlijk de meest gebruikte golf-oscillator, omdat hij een loop maakt voor cyclische eigenschappen zoals _hue_ of _rotation._

Zie de secties hierboven voor :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Specifiek voor Sawtooth :

* **cycle range compensation** - beschikbaar wanneer **steps** is ingesteld, en handig voor cyclische waarden, bijvoorbeeld een rotatie van 0 tot 360. Wanneer dit niet is ingeschakeld, zijn de begin- en eindwaarden hetzelfde, wat kan zorgen dat de animatie blijft hangen op het startpunt (omdat 0 en 360 dezelfde hoek zijn). Schakel dit in en het maximale bereik wordt verkleind om de stap-posities te corrigeren.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Driehoeksgolf

In tegenstelling tot de _zaagtandgolf_, die elke cyclus terugspringt naar het begin, beweegt de _driehoeksgolf_ lineair vooruit en daarna weer terug.

Zie de secties hierboven voor :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sinusgolf

De soepelste golfvorm! Oscilleert zacht tussen twee waarden, als een slinger.

Zie de secties hierboven voor :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Blokgolf

De eenvoudigste golfvorm: hij schakelt gewoon heen en weer tussen twee waarden!

Zie de secties hierboven voor :

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Specifiek voor Square wave :

* **pulse width** - de tijd dat de golf op de maximale waarde staat, relatief aan de totale duration. 50% is de standaardwaarde: precies half om half. Als je wilt dat hij maar een kwart van de tijd "aan" is, stel je dit in op 25%. Met de _offset_-waarde kun je aanpassen wanneer deze puls plaatsvindt.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

Een van de sterke punten van Liberation is dat het willekeurige, maar herhaalbare effecten kan genereren. De _noise_-oscillator kan worden gebruikt om een organische, loopende willekeurige beweging te maken, met zoveel detail/jitter als je wilt.

Zie de secties hierboven voor :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Specifiek voor Noise :

* **noise type** - het algoritme dat wordt gebruikt om de noise te genereren.
  * **SIMPLEX** - de standaardinstelling: een golvende waarde die op en neer beweegt en in een loop herhaalt.
  * **RANDOM** - gebruikt een traditioneler algoritme voor willekeurige getallen; volledig ruisachtig en chaotisch.

{% hint style="info" %}
**Simplex noise** is in 2001 ontworpen door Ken Perlin als verbetering van zijn "Perlin noise"-algoritme, dat hij in 1983 ontwikkelde als onderdeel van zijn werk aan de film _Tron_ (waarvoor hij een Oscar won!)

Deze zogenaamde "gradient" noise kwam voort uit zijn frustratie over eerdere, "machineachtige" computergegenereerde beelden. In de CGI-wereld is het bijzonder geschikt voor het renderen van wolken, wateroppervlakken of zelfs height-maps voor realistisch terrein.

Maar in Liberation is het goed voor schijnbaar onvoorspelbare beweging die toch soepel en organisch blijft.
{% endhint %}

* **seed** - de waarde die wordt gebruikt om de noise te maken. Als je het uiterlijk van de noise wave niet mooi vindt, probeer dan deze waarde te veranderen.

{% hint style="info" %}
Leuk nerdy feitje! Om een perfect loopende simplex noise te krijgen, itereer ik rond een cirkel op een 2D-noisevlak. En door de seed-waarde te veranderen, verplaats je dit vlak door een 3e dimensie!
{% endhint %}

* **simplex detail** - bepaalt hoe gedetailleerd of jittery de noise is. Als je wilt dat het herhalende patroon minder opvalt, verhoog dan de duration en verhoog deze waarde.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Maakt een volledig aangepaste golfvorm. Dit is erg handig voor het maken van complexe animaties.

Zie de secties hierboven voor :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Hieronder staat een lijst met posities en waarden. De duration wordt verdeeld in 64 stappen en je kunt op elk van deze punten een waarde plaatsen.

Elke stap heeft de volgende instellingen :

* **Step** - de tijdstap binnen de duration. 0 is aan het begin en 64 is aan het einde.
* **Level** - het niveau van de golf op die tijdstap. Het level loopt van 0 tot 1.
* **Animation type** - in het dropdown-menu kies je hoe je vanaf de vorige stap naar dit level wilt bewegen.
  * **None** - geen overgang; springt op het opgegeven moment direct naar dit level.
  * **Linear** - een volledig lineaire beweging van het vorige level naar dit level.
  * **Ease in / Ease out / Ease in/out** - eased tussen het vorige level en dit level. Zie _ease function_ hierboven voor een beschrijving van de animatietypen.

***
