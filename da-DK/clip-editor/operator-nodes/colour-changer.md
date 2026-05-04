---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Ændrer farverne på alt indgående indhold. Du kan enten angive faste HSB-værdier eller skifte til gradientsystemet og hente farver fra en brugerdefineret gradient.

* **hue, saturation, brightness** - farveværdierne, se [Farveindstillinger og HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - farvetonen ændres ikke
  * FIXED - elementernes farvetone sættes til værdien for hue
  * SHIFT - elementernes farvetone forskydes med værdien, så elementer med forskellige farver fortsat er forskellige, men blot forskydes langs farvetonen.
* **saturation mode** -
  * OFF - mætningen ændres ikke
  * FIXED - mætningen fastsættes til den angivne værdi.
* **brightness mode** -
  * OFF - lysstyrken ændres ikke
  * FIXED - elementernes lysstyrke sættes til værdien for brightness
  * MULTIPLY - elementernes lysstyrke kombineres med værdien for brightness, så hvis de blinker, bliver de ved med at blinke, men kun op til den lysstyrke, der er angivet her.
* **gradient mode** - skifter fra de faste HSB-skydere til gradienteditoren. Denne node henter én farve fra gradienten og anvender den derefter med hue-, saturation- og brightness-tilstandene ovenfor.
* **gradient position** - vælger, hvilket punkt i gradienten der hentes farve fra. Animér dette fra 0 % til 100 % med en Sawtooth Oscillator for at bevæge dig gennem gradienten over tid.
* **blend** - hvor kraftigt Colour change anvendes. 0% er slet ikke, 100% er fuldt, og 50% er en kombination af den eksisterende farve og de nye værdier.

{% hint style="info" %}
Colour Change-node henter én farve fra gradienten til hele inputtet. Hvis gradienten skal løbe hen over formen efter position, skal du i stedet bruge [positionsbaserede ændringer](position-based-changers.md "mention").
{% endhint %}

### Gradienteditor

Når **gradient mode** er slået til, vises gradienteditoren under hovedkontrollerne.

* Klik på gradientbjælken for at tilføje et farvestop.
* Venstreklik på et stop for at vælge det, og træk det derefter sidelæns for at flytte det.
* Træk et valgt stop ned væk fra bjælken, eller tryk på Delete/Backspace, for at fjerne det. En gradient beholder altid mindst to stop.
* Højreklik på et stop for at redigere det med farvevælgeren.
* Brug **Position**, **Hue**, **Saturation** og **Brightness** til at finjustere det valgte stop.
* **interpolation** vælger, hvordan farver blandes mellem stop:
* **HSB** - blander hue, saturation og brightness. Det er bedst til jævne regnbueagtige bevægelser rundt på farvehjulet.
* **RGB** - blander røde, grønne og blå værdier direkte. Det føles ofte mere som en farvefade på en skærm eller en lyspult.
* **NONE** - springer fra ét stop til det næste uden blanding.
* **hue direction** er tilgængelig ved HSB-interpolation:
* **AUTO** - tager den korteste vej rundt på hue-hjulet.
* **FORWARDS** - bevæger sig altid fremad gennem hue-værdierne.
* **BACKWARDS** - bevæger sig altid baglæns gennem hue-værdierne.
