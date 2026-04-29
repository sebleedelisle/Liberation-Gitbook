---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Banemodifikatorer

## &#x20;Dotter

Denne noden erstatter innhold i linjer og former med jevnt fordelte punkter (eksisterende punkter endres ikke).

* **Colour** – fargen på punktene. Ignoreres hvis _Inherit Colour_ er aktivert, se nedenfor. _Se også_ [Fargeinnstillinger og HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – avstanden mellom punktene, målt i piksler. Mindre verdier = flere punkter, større verdier = færre.
* **Offset** – forskyver startposisjonen for punktene som en prosentandel av avstanden. Kan animeres (f.eks. med en sawtooth Oscillator Node) for å lage punkteffekter som «vandrer».
* **Keep Original** – hvis aktivert, beholdes de opprinnelige linjene/formene, og punktene tegnes oppå.
* **Render Profile** – velger gjengivelseskvalitet. _Se_ [Render profile](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – justerer automatisk avstanden slik at banelengden kan deles jevnt.
* **Fade Out Ends** – reduserer gradvis lysstyrken på punktene mot starten og slutten av banen. Nyttig når du animerer **Offset** med en sawtooth Oscillator Node, slik at punktene fader jevnt inn/ut når de beveger seg til slutten av formen.

## &#x20;Trimmer

Denne noden trimmer den synlige lengden på linjer og former, slik at du kan vise, skjule eller animere dem over tid.

* **Offset** – styrer hvor den synlige delen av formen starter. Selv med _Trim Size_ på 0 % vil animasjon av Offset fra 0 % → 100 % få formen til å tegnes inn, bli helt synlig ved 50 %, og deretter forsvinne igjen.
* **Trim Size** – angir hvor mye av formen som beholdes, som en prosentandel av den totale lengden.
* **Loop** – behandler formen som en sammenhengende løkke, slik at slutten kobles tilbake til begynnelsen i stedet for å forsvinne.
* **All Shapes** – kombinerer alle innkommende former og trimmer dem som om de var én enkelt bane. Hvis den er av, trimmes hver form individuelt.
* **Add Dot at Start / Add Dot at End** – legger til et punkt med valgt farge ved trimmepunktene. (Hvis ingen trimming er brukt, legges det ikke til punkter.)
* **Colour** – fargen på trimmepunktene. _Se også_ [Fargeinnstillinger og HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – velger renderprofilen for punktene. _Se_ [Render profile](../fundamentals/render-profile.md "mention")
