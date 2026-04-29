---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Posisjonsbaserte endringer

Denne nodefamilien endrer innhold ut fra posisjon. Som standard brukes effekten langs en horisontal akse (fra venstre mot høyre), men du kan rotere denne aksen til hvilken som helst vinkel. Hver node har også en _radial_ modus, der effekten styres av vinkelen til hvert punkt i forhold til sentrum.

* **Colour Changer by Position** – forskyver farger langs den valgte aksen eller rundt den radiale vinkelen.\
  \&#xNAN;_Eksempel: Lag en regnbuegradient som beveger seg over en linje, eller bruk radial modus på en sirkel for å lage en fargehjuleffekt._
* **Wave Shift by Position** – legger på en sinusbølgeforvrengning som forskyver innholdet vertikalt (eller vinkelrett på den valgte aksen).\
  \&#xNAN;_Eksempel: Få en linje til å bølge som vann, eller bruk radial modus for å få en sirkel til å pulsere utover fra sentrum._
* **Noise Shift by Position** – legger på en simplex noise-forvrengning som forskyver innholdet vertikalt (eller vinkelrett på den valgte aksen).\
  \&#xNAN;_Eksempel: se eksempelet for Wave Shift, men med et mer organisk og tilfeldig uttrykk, perfekt for å legge til naturlig variasjon._

## &#x20;Fargeendring etter posisjon

Denne noden legger på fargeendringer over innholdet basert på posisjon. Som standard er aksen horisontal (0°), men du kan rotere den eller bytte til radial modus.

* **wavelength** – angir størrelsen på den repeterende fargesyklusen.
  * _Linear mode:_ ved 100% strekker én full syklus seg over hele bredden av innholdet.
  * _Radial mode:_ ved 100% strekker én full syklus seg rundt hele sirkelen (360°). Verdiene er prosent av sirkelen: f.eks. 50% = en halv sirkel (180°).
* **offset** – forskyver startpunktet for fargesyklusen, som prosent av wavelength. Du kan modulere dette (f.eks. med en sawtooth oscillator) for å bla jevnt gjennom fargene.
* **repeat** – når dette er aktivert, repeteres syklusen over innholdet. Hvis det er deaktivert, brukes gradienten bare én gang: alt før starten får startfargen, og alt etter slutten får sluttfargen.
* **pingpong** – når dette er aktivert, veksler hver repetisjon retning og lager en speilet effekt. Hvis _Repeat_ er deaktivert, går gradienten frem og deretter tilbake én gang. _Merk: i Pingpong-modus dekker wavelength både frem- og retursveipet._
* **linear angle** – roterer aksen for effekten. 0° = horisontal.
* **radial** – bytter til radial modus, der farger legges på basert på vinkelen fra sentrum.
* **radial smooth loop** – justerer automatisk wavelength slik at den går jevnt opp i 100% av sirkelen, og hindrer en synlig skjøt der syklusen går rundt.

**Colour Modes**

Disse bestemmer hvilke deler av fargejusteringene som brukes på innholdet. Se også: [Fargeinnstillinger og HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – hue endres ikke.
  * _FIXED_ – hue låses til en fast verdi.
  * _SHIFTED_ – hue forskyves med den angitte mengden (elementer med ulike farger forblir forskjellige, men forskyves samlet rundt fargehjulet).
* **saturation mode**
  * _OFF_ – saturation endres ikke.
  * _FIXED_ – saturation settes til den angitte verdien.
* **brightness mode**
  * _OFF_ – brightness endres ikke.
  * _FIXED_ – brightness settes til den angitte verdien.
  * _MULTIPLY_ – brightness skaleres med den angitte verdien. Dette bevarer dynamikk (f.eks. vil blinkende elementer fortsatt blinke, men innenfor det begrensede lysstyrkeområdet).

**Start / End Values**

Disse glidebryterne definerer fargeområdet som brukes langs den valgte aksen (eller det radiale sveipet).

* **start hue** – hue ved starten av gradienten.
* **end hue** – hue ved slutten av gradienten.
* **start saturation** – saturation ved starten.
* **end saturation** – saturation ved slutten.
* **start brightness** – brightness ved starten.
* **end brightness** – brightness ved slutten.
* **blend** – blander fargeendringen med originalfargene. Ved 100% erstatter effekten originalfargene helt.

**Eksempel 1: Glidende regnbuegradient**

Med standardinnstillinger:

1. La noden stå i **Linear** mode (0° angle = horizontal).
2. La **wavelength** stå på 100% (dekker hele bredden, og bør være standard).
3. La start- og sluttverdiene stå som standard.
4. Aktiver **repeat**.
5. Legg til en **Sawtooth Oscillator** på innstillingen **offset** som går fra 0% til 100%.

***

**Eksempel 2: Svart–hvit–svart-gradient (Pingpong)**

Med standardinnstillinger:

1. La noden stå i **Linear** mode (0° angle = horizontal).
2. La **wavelength** stå på 100% (dekker hele bredden, og bør være standard).
3. Slå av **repeat**.
4. Sett **start brightness** til 0 (svart).
5. Sett **end brightness** til 100 (hvit).
6. Sett **start saturation** og **end saturation** til 0 (konverterer til gråtoner).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Aktiver **pingpong**.

_Resultat: gradienten toner fra svart til hvitt, og deretter tilbake til svart over bredden._\
Merk at hvis du vil at innholdet skal beholde hue og saturation, slår du av Saturation mode. \\

***

**Eksempel 3: Roterende regnbuehjul (Radial)**

1. Aktiver **radial** mode.
2. Sett **wavelength** til 100% (et fullt 360°-sveip).
3. Slå på **repeat**.
4. Legg til en **Sawtooth Oscillator** på innstillingen **offset** som går fra 0% til 100%.

_Resultat: et sømløst fargehjul som roterer kontinuerlig rundt sirkelen._

## &#x20;Wave shift etter posisjon

Denne noden legger på en bølgeforvrengning over innholdet og forskyver punkter vinkelrett på den valgte aksen (eller radialt fra sentrum).

* **Wavelength** – angir lengden på bølgesyklusen.
  * _Linear mode:_ ved 100% strekker én full syklus seg over hele bredden av innholdet.
  * _Radial mode:_ ved 100% strekker én full syklus seg over hele 360°. (Verdiene er prosent av sirkelen: 50% = en halv omdreining, 25% = en kvart omdreining osv.)
* **Size** – styrer amplituden til bølgen (hvor langt innholdet forskyves).
* **Offset** – forskyver bølgen langs aksen (eller rundt sirkelen i radial modus). Dette er en prosent av wavelength, slik at du kan animere den med en **Oscillator Node** for å få bølgen til å bevege seg.
* **Radial** – bytter fra lineær til radial modus, slik at forskyvningen baseres på vinkelen fra sentrum.
* **Radial Smooth Loop** – justerer wavelength slik at den går jevnt opp i 100% av sirkelen, og hindrer synlige skjøter der den går rundt.
* **Triangle** – endrer bølgeformen fra sinus til trekant.
* **Absolute** – bruker absoluttverdien av bølgen, slik at forskyvninger bare går oppover (den negative siden brettes over på den positive).
* **Angle** – roterer aksen for bølgen. 0° = horisontal.

## &#x20;Noise shift etter posisjon

Denne noden forvrenger innhold ved hjelp av et noise-felt (som turbulens), og forskyver punkter vinkelrett på den valgte aksen (eller radialt fra sentrum). Sammenlignet med _Wave Shift_ blir resultatet mer organisk og tilfeldig.

* **Detail** – styrer hvor finmasket noise-mønsteret er. Høyere verdier = skarpere og mer detaljert variasjon. Lavere verdier = jevnere variasjon.
* **Wavelength** – angir skalaen på noise-mønsteret.
  * _Linear mode:_ ved 100% strekker én full noise-syklus seg over bredden av innholdet.
  * _Radial mode:_ ved 100% strekker én full syklus seg over hele 360°.
* **Size** – styrer forskyvningsmengden (amplituden til noise-forvrengningen).
* **Offset** – forskyver noise-mønsteret langs aksen (eller rundt sirkelen). Dette er en prosent av wavelength, slik at du kan animere den med en **Oscillator Node** for å få noise til å “flyte.”
* **Depth Offset** – beveger seg gjennom 3D noise-feltet og skaper variasjon over tid. Dette er spesielt effektivt når det animeres med en Oscillator Node.
* **Depth Detail** – styrer hvor detaljert variasjonen er langs dybdedimensjonen.
* **Absolute** – bruker absoluttverdien av noise, slik at negative verdier brettes over til positive (gir bare ensidig forskyvning).
* **Radial** – bytter fra lineær til radial modus, slik at forskyvningen baseres på vinkelen fra sentrum.
* **Radial Smooth Loop** – justerer wavelength slik at den går jevnt opp i 100% av sirkelen, og hindrer synlige skjøter i radial modus.
