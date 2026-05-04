---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Endrer fargene på alt innkommende innhold. Du kan enten angi faste HSB-verdier, eller bytte til gradientsystemet og hente farger fra en egendefinert gradient.

* **hue, saturation, brightness** – fargeverdiene, se [Fargeinnstillinger og HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** –
  * OFF – hue endres ikke
  * FIXED – hue for elementer settes til hue-verdien
  * SHIFT – hue for elementer forskyves med verdien, slik at elementer med ulike farger fortsatt er ulike, men bare forskyves langs hue-verdien.
* **saturation mode** –
  * OFF – saturation endres ikke
  * FIXED – saturation låses til den angitte verdien.
* **brightness mode** –
  * OFF – brightness endres ikke
  * FIXED – brightness for elementer settes til brightness-verdien
  * MULTIPLY – brightness for elementer kombineres med brightness-verdien, slik at hvis de blinker, vil de fortsatt blinke, men bare opp til brightness som er angitt her.
* **gradient mode** – bytter fra de faste HSB-glidebryterne til gradientredigereren. Denne node henter én farge fra gradienten og bruker den deretter med modusene for hue, saturation og brightness ovenfor.
* **gradient position** – velger hvilket punkt i gradienten som skal samples. Animer dette fra 0 % til 100 % med en Sawtooth Oscillator for å gå gjennom gradienten over tid.
* **blend** – hvor sterkt colour changer brukes. 0 % er ikke i det hele tatt, 100 % er fullt, og 50 % er en kombinasjon av den eksisterende fargen og de nye verdiene.

{% hint style="info" %}
Colour Change node henter én farge fra gradienten for hele inndataen. Hvis du vil at gradienten skal gå over formen basert på posisjon, bruker du [posisjonsbaserte endrere](position-based-changers.md "mention") i stedet.
{% endhint %}

### Gradientredigerer

Når **gradient mode** er på, vises gradientredigereren under hovedkontrollene.

* Klikk på gradientlinjen for å legge til et fargestopp.
* Venstreklikk på et stopp for å velge det, og dra det deretter sidelengs for å flytte det.
* Dra et valgt stopp ned og bort fra linjen, eller trykk på Delete/Backspace, for å fjerne det. En gradient beholder alltid minst to stopp.
* Høyreklikk på et stopp for å redigere det med fargevelgeren.
* Bruk **Position**, **Hue**, **Saturation** og **Brightness** for å redigere det valgte stoppet nøyaktig.
* **interpolation** velger hvordan farger blandes mellom stopp:
* **HSB** – blander hue, saturation og brightness. Dette er best for jevne regnbuelignende bevegelser rundt fargehjulet.
* **RGB** – blander røde, grønne og blå verdier direkte. Dette oppleves ofte mer som en fargeovergang på en skjerm eller lysmikser.
* **NONE** – hopper fra ett stopp til det neste uten blanding.
* **hue direction** er tilgjengelig ved HSB-interpolering:
* **AUTO** – tar korteste vei rundt hue-hjulet.
* **FORWARDS** – går alltid forover gjennom hue-verdiene.
* **BACKWARDS** – går alltid bakover gjennom hue-verdiene.
