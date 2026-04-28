---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Wave oscillators

## På denne side :

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Sawtooth wave](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Triangle wave](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sine wave](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Square wave](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Indstillinger for Wave oscillator

Alle Wave oscillators har følgende indstillinger :

* **range min / range max** - bestemmer værdiområdet for den egenskab, oscillatoren styrer. Egenskaben sættes til _range min_, når bølgeformen er nederst, og til _range max_, når bølgeformen er øverst.

{% hint style="info" %}
Hvis du for eksempel vil have en prik til at bevæge sig til venstre og højre mellem -100 og 100, skal du forbinde oscillatoren til _x property socket_, sætte _min range_ til -100 og _max range_ til 100.
{% endhint %}

* **duration** - hvor lang tid én fuld cyklus (eller _loop_) tager at gennemføre. Dette er relativt til tempoet i takter. Så ¼ er ét beat. 1 er en hel takt osv.
* **duration multiplier** - skalerer den grundlæggende varighed med en valgt faktor. Hvis duration for eksempel er sat til en fjerdedelsnode, og multiplier er 3, varer oscillatoren tre fjerdedelsnoder (en punkteret halvnode). Brøk-multiplikatorer understøttes også — hold _SHIFT_ nede, mens du trækker i slideren, for at angive ikke-hele tal. Det er nyttigt til phasing-effekter eller til at lave subtile timingforskydninger.
* **offset** - bølgens startforskydning som procentdel af varigheden. Hvis bølgen skal starte en fjerdedel inde i forløbet, skal du sætte dette til 25%.
* **repeat count** - antallet af gange loopet kører, før det stopper. Standardværdien er _FOREVER_, men du kan ændre den, hvis oscillatoren ikke skal køre uendeligt. Når den stopper, sættes egenskaben til værdien ved slutningen af bølgen.
* **delay count** - forsinkelsen i beats, før oscillatoren begynder at køre. Før den starter, sættes egenskaben til værdien ved starten af bølgen.

{% hint style="info" %}
Med omhyggelig brug af _repeat count_ og _delay count_ kan du lave meget komplekse animationer — nærmest som en lille tidslinje i sig selv!
{% endhint %}

## Fælles indstillinger

* **steps** - opdeler bevægelsen i et antal diskrete trin. Godt når du vil have egenskaber til at "hoppe" til værdier i stedet for at bevæge sig jævnt.

{% hint style="info" %}
Bemærk, at trinnene opdeles efter tid og ikke efter værdi. Så for en bølge opdelt i 4 trin med en duration på 1 takt skifter egenskaben øjeblikkeligt ved hvert beat.
{% endhint %}

* **clamp min / clamp max -** øger bølgens skala ud over dens minimums- eller maksimumsværdier og begrænser resultatet.

{% hint style="info" %}
_Clamp_-konceptet er lidt svært at forklare, men forestil dig, at bølgeformen går ud over toppen eller bunden af grafen og derefter bliver klemt fast til kanterne. Jeg anbefaler, at du eksperimenterer med dem! De er meget nyttige, hvis du vil have en sawtooth til at starte sent eller slutte tidligt.
{% endhint %}

* **ease function** - Sawtooth og Triangle waves har også en ease function, som ændrer animationskurven subtilt og kan gøre dine animationer virkelig udtryksfulde!
  * **LINEAR** - standarden, ingen easing; bevæger sig bare lineært mellem minimums- og maksimumsværdierne.
  * **EASE OUT** - starter hurtigt og sænker derefter farten, når den nærmer sig slutningen. Meget velegnet til at simulere fysik, f.eks. at bremse ned til stilstand.
  * **EASE IN** - starter langsomt og øger gradvist hastigheden. God til at simulere opbygning af momentum.
  * **EASE IN/OUT** - en kombination af begge og en meget organisk bevægelse.

{% hint style="warning" %}
**Easing -** Jeg ville undgå den lineære standardanimation, når du kan, medmindre du specifikt ønsker noget, der ser robotagtigt ud. Easing kan gøre dine animationer langt mere flydende og organiske!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sawtooth wave

Kaldes også nogle gange en _ramp waveform_, fordi den ramper opad og derefter falder brat ved slutningen af sin cyklus. Det er sandsynligvis den mest almindelige wave oscillator, fordi den laver et loop til cykliske egenskaber som _hue_ eller _rotation._

Se afsnittene ovenfor for :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Specifikt for Sawtooth :

* **cycle range compensation** - tilgængelig når **steps** er sat, og den er god til cykliske værdier, f.eks. en rotation fra 0 til 360. Når den ikke er slået til, er start- og slutværdierne ens, hvilket kan få bevægelsen til at hænge ved startpunktet (fordi 0 og 360 er samme vinkel). Slå den til, så reduceres maksimumområdet for at korrigere trinpositionerne.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Triangle wave

I modsætning til _sawtooth wave_, som hopper tilbage til begyndelsen i hver cyklus, bevæger _triangle wave_ sig lineært fremad og derefter tilbage.

Se afsnittene ovenfor for :

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

Den mest jævne bølgeform! Oscillerer blødt mellem to værdier som et pendul.

Se afsnittene ovenfor for :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Square wave

Den enkleste bølgeform - den skifter bare mellem to værdier frem og tilbage!

Se afsnittene ovenfor for :

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Specifikt for Square wave :

* **pulse width** - hvor lang tid bølgen er på sin maksimumsværdi i forhold til den samlede varighed. 50% er standarden, hvilket er præcis halvt af hver. Hvis den kun skal være "on" en fjerdedel af tiden, skal du sætte den til 25%. Du kan justere, hvornår denne puls sker, med _offset_-værdien.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

En af Liberations styrker er, at programmet kan generere tilfældige, men gentagelige effekter. _Noise_-oscillatoren kan bruges til at lave en organisk, loopende tilfældig bevægelse med så meget detalje/jitter, som du ønsker.

Se afsnittene ovenfor for :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Specifikt for Noise :

* **noise type** - algoritmen der bruges til at generere støjen.
  * **SIMPLEX** - standarden; en bølgende værdi, der ebber og flyder, og som gentages i et loop.
  * **RANDOM** - bruger en mere traditionel algoritme til tilfældige tal; helt støjende og kaotisk.

{% hint style="info" %}
**Simplex noise** blev designet af Ken Perlin i 2001 som en forbedring af hans "Perlin noise"-algoritme, som han udviklede i 1983 som en del af sit arbejde på filmen _Tron_ (som han vandt en Oscar for!)

Denne såkaldte "gradient"-støj opstod ud af hans frustration over tidligere "maskinagtige" computergenererede billeder. I CGI-verdenen er den særligt god til at rendere skyer, vandoverflader eller endda height-maps til realistisk terræn.

Men i Liberation er den god til bevægelse, der virker uforudsigelig, men stadig er jævn og organisk.
{% endhint %}

* **seed** - værdien der bruges til at skabe støjen. Hvis du ikke kan lide udseendet af den noise wave, du har, kan du prøve at ændre værdien.

{% hint style="info" %}
Sjov nørdefakta! For at få perfekt loopende simplex noise itererer jeg rundt om en cirkel på et 2D-støjplan. Og når seed-værdien ændres, flyttes dette plan gennem en 3. dimension!
{% endhint %}

* **simplex detail** - ændrer hvor detaljeret eller jittery støjen er. Hvis det gentagne mønster skal være mindre tydeligt, kan du øge duration og hæve denne værdi.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Opretter en helt brugerdefineret bølgeform. Det er meget nyttigt til at lave komplekse animationer.

Se afsnittene ovenfor for :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Nedenfor findes en liste over positioner og værdier. Varigheden opdeles i 64 trin, og du kan placere en værdi ved et hvilket som helst af disse punkter.

Hvert trin har følgende indstillinger :

* **Step** - tidstrinnet inden for varigheden. 0 er ved begyndelsen, og 64 er ved slutningen.
* **Level** - bølgens niveau ved det pågældende tidstrin. Niveauet går fra 0 til 1.
* **Animation type** - rullemenuen lader dig vælge, hvordan du vil bevæge dig mod dette niveau fra det forrige trin.
  * **None** - ingen overgang; hopper direkte til dette niveau på det angivne tidspunkt.
  * **Linear** - en helt lineær bevægelse fra det forrige niveau til dette.
  * **Ease in / Ease out / Ease in/out** - bruger easing mellem det forrige niveau og dette. Se _ease function_ ovenfor for en beskrivelse af animationstyperne.

***
