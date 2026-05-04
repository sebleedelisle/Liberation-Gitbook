---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator-noder

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Lager ett enkelt punkt / én stråle.

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **Colour** - fargen på punktet. Se [Fargeinnstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- og **y**-posisjon - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Lager en linje / flate.

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **Size** - lengden på linjen
* **Colour** - fargen på linjen. Se [Fargeinnstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- og **y**-posisjon - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - vinkelen på linjen, i grader
* **resolution** - se [Oppløsning](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ bestemmer startpunktet og rotasjonssenteret for linjen
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Lager en sirkel / kjegle.

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **radius** - sirkelens radius
* **Colour** - fargen på sirkelen. Se [Fargeinnstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- og **y**-posisjon - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **resolution** - se [Oppløsning](fundamentals/resolution.md "mention")
* **Fill state** - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Lager et likesidet polygon, trekant, kvadrat, femkant osv.

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **size** - avstanden fra sentrum til hvert hjørne
* **Colour** - fargen på polygonet. Se [Fargeinnstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- og **y**-posisjon - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - figurens rotasjonsvinkel, i grader
* **resolution** - se [Oppløsning](fundamentals/resolution.md "mention")
* **Fill state** - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Laster inn en SVG-fil for egendefinerte figurer.

{% hint style="warning" %}
Liberation er kompatibel med _SVGTiny_-formatet. InkScape anbefales, men de fleste vektorgrafikkapper kan eksportere i dette formatet. Sørg for å konvertere all tekst til figurer før eksport. Liberation rendrer streker og kan valgfritt bruke fyll som masker. Pass på at linjene dine ikke er svarte, ellers vises de ikke uten en fargemodifikator!
{% endhint %}

* **Import SVG** - last inn en SVG-fil fra disk.

{% hint style="info" %}
Når en SVG er lastet inn, konverteres innholdet og lagres i klippet, så du trenger ikke å beholde en referanse til filen, med mindre du senere vil endre maskeinnstillingene.
{% endhint %}

* **Use fills as masks** - behandler alle fylte figurer som en maske, dvs. fylt med svart. Dette settes automatisk hvis SVG-en har fylte figurer. Hvis den ikke har fylte figurer, deaktiveres det. Se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - hvis figurene i SVG-en ikke har en kontur, kan vi ikke tegne dem! Dette alternativet legger til en kontur (eller _stroke_) på alle fylte figurer. Hvis SVG-en ikke har noen figurer med stroke, settes det automatisk. Hvis den ikke har fylte figurer, deaktiveres det.
* **Invert black lines** - hvis alle linjene i SVG-en er svarte, kan du ikke se dem! Dette alternativet gjør dem hvite. Det settes automatisk hvis SVG-en bare har svarte figurer, men deaktiveres hvis du ikke har noen.
* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **scale** - justerer størrelsen på SVG-en. Dette beregnes automatisk når SVG-en lastes inn (for å sikre at bildet er synlig), men kan redigeres manuelt etterpå.
* **x**- og **y**-posisjon - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - bildets rotasjonsvinkel, i grader
* **resolution** - se [Oppløsning](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Lager en animasjon fra en sekvens med SVG-filer.

* **Import SVG Sequence** - velg mappen som inneholder alle SVG-filene. Merk at de lastes inn i alfanumerisk rekkefølge.

{% hint style="info" %}
Når SVG-sekvensen er lastet inn, konverteres innholdet og lagres i klippet, så du trenger ikke å beholde en referanse til filene, med mindre du senere vil endre maskeinnstillingene.
{% endhint %}

* **Use fills as masks** - behandler alle fylte figurer som en maske, dvs. fylt med svart. Dette settes automatisk hvis noen av SVG-ene dine har fylte figurer. Hvis ingen har fylte figurer, deaktiveres det. Se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - hvis figurene i SVG-ene dine ikke har konturer, kan vi ikke tegne dem! Dette alternativet legger til en kontur (eller _stroke_) på alle fylte figurer. Hvis SVG-ene dine ikke har noen figurer med stroke, settes det automatisk. Hvis ingen har fylte figurer, deaktiveres det.
* **Invert black lines** - hvis alle linjene i SVG-ene dine er svarte, kan du ikke se dem! Dette alternativet gjør dem hvite. Det settes automatisk hvis SVG-ene dine bare har svarte figurer, men deaktiveres hvis du ikke har noen.
* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **scale** - justerer størrelsen på bildet.
* **x**- og **y**-posisjon - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - bildets rotasjonsvinkel, i grader
* **resolution** - se [Oppløsning](fundamentals/resolution.md "mention")
* **speed** - varigheten på hele animasjonen, i takter.
* **time per frame** - hvis dette er aktivert, gjelder varigheten per bilde i stedet for hele animasjonens lengde. Så hvis _speed_ er satt til ¼, varer hvert bilde 1 slag.
* **animation direction** -
  * _FORWARDS_ - animasjonen går forover og looper deretter tilbake til starten
  * _BACKWARDS_ - animasjonen går bakover og looper deretter tilbake til slutten
  * _PINGPONG_ - animasjonen går forover og deretter bakover i en loop
  * _MANUAL_ - gjeldende bilde settes med innstillingen _position manual_
* **position manual** - angi gjeldende bilde. 0 % er første bilde, 100 % er siste bilde. Dette kan settes manuelt eller med en ekstern oscillator.
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Lager tekst med en TrueType- eller OpenType-font.

* **Text** - skriv inn teksten du vil bruke her
* **Font** - velg fonten du vil bruke

{% hint style="info" %}
For å legge til flere fonter i Liberation kopierer du .ttf- eller .otf-filene til mappen `data/fonts` i arbeidsmappen til Liberation, og starter deretter Liberation på nytt.
{% endhint %}

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **horizontal alignment** - velg _LEFT_, _CENTRE_ eller _RIGHT_ for å velge tekstjustering.
* **Fill state** - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - tekststørrelsen
* **monospace** - tegner hvert tegn med samme bredde. Dette er nyttig for tidtakere og tellere fordi teksten ikke flytter seg sideveis når tallene endres.
* **character spacing** - justerer avstanden mellom tegn. Øk den for større tegnavstand, eller reduser den for å stramme inn teksten.
* **colour -** se [Fargeinnstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- og **y**-posisjon - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - bildets rotasjonsvinkel, i grader
* **resolution** - se [Oppløsning](fundamentals/resolution.md "mention")
* **reveal** - bruk dette til å gradvis vise teksten, ett tegn om gangen. Når dette er mellom 0 og 50 %, vises teksten gradvis fra venstre mot høyre. Når det er mellom 50 % og 100 %, forsvinner teksten fra venstre mot høyre. Du kan koble en oscillator til denne sokkelen for å lage animasjoner.
* **reveal by word** - når dette er aktivert, fungerer _reveal_ ord for ord i stedet for tegn for tegn.
* **countdown** - erstatter teksten du har skrevet inn, med en nedtelling. Når nedtellingen når null, vises den vanlige **Text**-verdien.
* **use seconds** - teller i faktiske sekunder. Når dette er av, er nedtellingen slagbasert: to slag teller som ett sekund, så 120 bpm tilsvarer faktiske sekunder.
* **show minutes/seconds** - viser gjenværende tid i minutter og sekunder. Hvis det er over en time, tas også timer med.
* **countdown to date/time** - teller ned til en bestemt UTC-dato og et bestemt UTC-klokkeslett i stedet for å telle ned fra et tall.
* **countdown datetime** - angir UTC-måldatoen og -klokkeslettet når **countdown to date/time** er på.
* **start number** - starttallet når **countdown to date/time** er av.
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyll, masker og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Hvis rullegardinmenyen for font er åpen, går pil opp- og pil ned-tastene gjennom de tilgjengelige fontene.
{% endhint %}
