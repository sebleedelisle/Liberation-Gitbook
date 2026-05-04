---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Wave oscillators

## På den här sidan :

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Sawtooth wave](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Triangle wave](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sine wave](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Square wave](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Inställningar för Wave oscillator

Alla Wave oscillators har följande inställningar :

* **range min / range max** - bestämmer värdeintervallet för egenskapen som oscillatorn styr. Egenskapen sätts till _range min_ när vågformen är längst ned, och till _range max_ när vågformen är längst upp.

{% hint style="info" %}
Om du till exempel vill att en punkt ska röra sig åt vänster och höger mellan -100 och 100 ansluter du oscillatorn till _x property socket_, ställer in _min range_ på -100 och _max range_ på 100.
{% endhint %}

* **duration** - tiden det tar för en hel cykel (eller _loop_) att slutföras. Detta är relativt till tempot i takter. ¼ är alltså ett slag. 1 är en hel takt, osv.
* **duration multiplier** - skalar grundlängden med en vald faktor. Om duration till exempel är inställd på en fjärdedelsnot och multiplier är 3, varar oscillatorn i tre fjärdedelsnoter (en punkterad halvnot). Decimala multiplikatorer stöds också — håll ned _SHIFT_ medan du drar reglaget för att ställa in tal som inte är heltal, vilket är användbart för fasningseffekter eller subtila timingförskjutningar.
* **offset** - startförskjutningen för vågen som en procentandel av duration. Om du vill att vågen ska börja en fjärdedel in ställer du in detta på 25%.
* **repeat count** - antalet gånger loopen körs innan den stannar. Standardvärdet är _FOREVER_, men du kan ändra det om du inte vill att oscillatorn ska köras utan slut. När den har stannat sätts egenskapen till värdet vid slutet av vågen.
* **delay count** - fördröjningen i slag innan oscillatorn börjar köras. Innan den börjar köras sätts egenskapen till värdet vid början av vågen.

{% hint style="info" %}
Med genomtänkt användning av _repeat count_ och _delay count_ kan du skapa mycket komplexa animationer, nästan som en egen tidslinje!
{% endhint %}

## Gemensamma inställningar

* **steps** - delar upp rörelsen i ett antal diskreta steg. Bra när du vill att egenskaper ska "hoppa" till värden i stället för att röra sig mjukt.

{% hint style="info" %}
Observera att stegen delas upp efter tid, inte efter värde. För en våg som delas i 4 steg med duration på 1 takt ändras egenskapen alltså direkt varje slag.
{% endhint %}

* **clamp min / clamp max -** ökar vågens skala bortom dess lägsta eller högsta värden och klampar resultatet.

{% hint style="info" %}
Begreppet _clamp_ är ganska svårt att förklara, men tänk dig att vågformen går utanför grafens över- eller nederkant och sedan kläms fast mot kanterna. Jag rekommenderar att du experimenterar med dem! De är mycket användbara om du vill att en sawtooth ska börja sent eller sluta tidigt.
{% endhint %}

* **ease function** - Sawtooth- och Triangle-vågorna har också en ease function som subtilt ändrar animationskurvan och kan göra dina animationer riktigt uttrycksfulla!
  * **LINEAR** - standardläget, ingen easing, rör sig bara linjärt mellan min- och maxvärdena.
* **EASE OUT** - börjar snabbt och saktar sedan ned när den närmar sig slutet. Mycket bra för att simulera fysik, till exempel att bromsa in till stillastående.
  * **EASE IN** - börjar långsamt och ökar gradvis hastigheten. Bra för att simulera att momentum byggs upp.
  * **EASE IN/OUT** - en kombination av båda, med en mycket organisk rörelse.

{% hint style="warning" %}
**Easing -** Jag skulle undvika den linjära standardanimationen när du kan, om du inte uttryckligen vill ha något som ser robotaktigt ut. Easing kan göra dina animationer mycket mer flytande och organiska!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sawtooth wave

Kallas ibland även en _ramp waveform_, eftersom den rampar uppåt och sedan faller skarpt i slutet av sin cykel. Det är förmodligen den vanligaste vågoscillatorn eftersom den skapar en loop för cykliska egenskaper som _hue_ eller _rotation._

Se avsnitten ovan för :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Specifikt för Sawtooth :

* **cycle range compensation** - tillgänglig när **steps** är inställt, och är bra för cykliska värden, till exempel en rotation från 0 till 360. När detta inte är inställt blir start- och slutvärdet samma, vilket kan orsaka att värdet fastnar vid startpunkten (eftersom 0 och 360 är samma vinkel). Slå på detta så minskas maxintervallet för att korrigera stegpositionerna.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Triangle wave

Till skillnad från _sawtooth wave_, som hoppar tillbaka till början vid varje cykel, rör sig _triangle wave_ linjärt framåt och sedan bakåt.

Se avsnitten ovan för :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sine wave

Den mjukaste vågformen! Oscillerar försiktigt mellan två värden, som en pendel.

Se avsnitten ovan för :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Square wave

Den enklaste vågformen - den växlar bara mellan två värden, fram och tillbaka!

Se avsnitten ovan för :

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Specifikt för Square wave :

* **pulse width** - hur länge vågen ligger på sitt maxvärde i förhållande till den totala duration. 50% är standardvärdet, vilket är exakt hälften var. Om du bara vill att den ska vara "på" en fjärdedel av tiden ställer du in den på 25%. Du kan justera när denna puls sker med värdet _offset_.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

En av Liberations styrkor är att det kan generera slumpmässiga men upprepningsbara effekter. _noise_-oscillatorn kan användas för att skapa en organisk loopande slumpmässig rörelse med så mycket detalj/jitter du vill.

Se avsnitten ovan för :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Specifikt för Noise :

* **noise type** - algoritmen som används för att generera bruset.
  * **SIMPLEX** - standardläget, ett böljande värde som stiger och faller och upprepas i en loop.
  * **RANDOM** - använder en mer traditionell slumptalsalgoritm, helt brusig och kaotisk.

{% hint style="info" %}
**Simplex noise** designades av Ken Perlin 2001 som en förbättring av hans "Perlin noise"-algoritm, som han utvecklade 1983 som en del av sitt arbete med filmen _Tron_ (som han vann en Oscar för!)

Detta så kallade "gradient"-brus föddes ur hans frustration över tidigare "maskinliknande" datorgenererade bilder. I CGI-världen är det särskilt bra för att rendera moln, vattenytor eller till och med höjdkartor för realistisk terräng.

Men i Liberation är det bra för rörelse som verkar oförutsägbar men ändå är mjuk och organisk.
{% endhint %}

* **seed** - värdet som används för att skapa bruset. Om du inte gillar hur brusvågen ser ut kan du prova att ändra detta värde.

{% hint style="info" %}
Roligt nördfaktum! För att få perfekt loopande simplex noise itererar jag runt en cirkel på ett 2D-brusplan. Och när seed-värdet ändras flyttas detta plan genom en tredje dimension!
{% endhint %}

* **simplex detail** - ändrar hur detaljerat eller jitterigt bruset är. Om du vill att det upprepande mönstret ska vara mindre tydligt, öka duration och höj detta värde.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Skapar helt anpassade vågformer. Detta är mycket användbart för att skapa komplexa animationer.

Se avsnitten ovan för :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Nedanför detta finns en lista med positioner och värden. Duration delas upp i 64 steg och du kan placera ett värde vid vilken som helst av dessa punkter.

Varje steg har följande inställningar :

* **Step** - tidssteget inom duration. 0 är i början och 64 är i slutet.
* **Level** - vågens nivå vid det tidssteget. Nivån sträcker sig mellan 0 och 1.
* **Animation type** - rullgardinsmenyn låter dig välja hur du vill röra dig mot denna nivå från föregående steg.
  * **None** - ingen övergång, hoppar direkt till denna nivå vid den angivna tiden.
  * **Linear** - en helt linjär rörelse från föregående nivå till denna.
  * **Ease in / Ease out / Ease in/out** - easar mellan föregående nivå och denna. Se _ease function_ ovan för en beskrivning av animationstyperna.

***
