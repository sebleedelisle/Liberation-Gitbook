---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator-noder

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Opretter en enkelt prik / stråle.

* **Render profile** - se [Renderprofil](fundamentals/render-profile.md "mention")
* **Colour** - prikkens farve. Se [Farveindstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Opretter en linje / flade.

* **Render profile** - se [Renderprofil](fundamentals/render-profile.md "mention")
* **Size** - linjens længde
* **Colour** - linjens farve. Se [Farveindstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - linjens vinkel i grader
* **resolution** - se [Resolution](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ bestemmer linjens startpunkt og rotationscentrum
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Opretter en cirkel / kegle.

* **Render profile** - se [Renderprofil](fundamentals/render-profile.md "mention")
* **radius** - cirklens radius
* **Colour** - cirklens farve. Se [Farveindstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **resolution** - se [Resolution](fundamentals/resolution.md "mention")
* **Fill state** - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Opretter en ligesidet polygon, trekant, firkant, femkant osv.

* **Render profile** - se [Renderprofil](fundamentals/render-profile.md "mention")
* **size** - afstanden fra centrum til hvert hjørne
* **Colour** - polygonens farve. Se [Farveindstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - formens roterede vinkel i grader
* **resolution** - se [Resolution](fundamentals/resolution.md "mention")
* **Fill state** - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Indlæser en SVG-fil til brugerdefinerede former.

{% hint style="warning" %}
Liberation er kompatibel med _SVGTiny_-formatet. InkScape anbefales, men de fleste vektorgrafik-apps kan eksportere i dette format. Sørg for at konvertere al tekst til former før eksport. Liberation renderer streger og kan valgfrit bruge udfyldninger som masker. Sørg for, at dine linjer ikke er sorte, ellers vises de ikke uden en farvemodifier!
{% endhint %}

* **Import SVG** - indlæs en SVG-fil fra disken.

{% hint style="info" %}
Når en SVG er indlæst, konverteres indholdet og gemmes i clippet, så du behøver ikke at bevare en reference til filen, medmindre du senere vil ændre maskeindstillingerne.
{% endhint %}

* **Use fills as masks** - behandler alle udfyldte former som en maske, dvs. udfyldt med sort. Dette aktiveres automatisk, hvis din SVG har udfyldte former. Hvis den ikke har udfyldte former, deaktiveres det. Se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - hvis formerne i din SVG ikke har en kontur, kan vi ikke tegne dem! Denne indstilling tilføjer en kontur (eller _stroke_) til alle udfyldte former. Hvis din SVG ikke har nogen former med stroke, aktiveres den automatisk. Hvis den ikke har udfyldte former, deaktiveres den.
* **Invert black lines** - hvis alle linjerne i din SVG er sorte, kan du ikke se dem! Denne indstilling gør dem hvide. Den aktiveres automatisk, hvis din SVG kun har sorte former, men den deaktiveres, hvis du ikke har nogen.
* **Render profile** - se [Renderprofil](fundamentals/render-profile.md "mention")
* **scale** - justerer SVG'ens størrelse. Dette beregnes automatisk, når SVG'en indlæses (for at sikre, at billedet er synligt), men kan efterfølgende redigeres manuelt.
* **x** og **y** position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - billedets roterede vinkel i grader
* **resolution** - se [Resolution](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Opretter en animation ud fra en sekvens af SVG-filer.

* **Import SVG Sequence** - vælg den mappe, der indeholder alle SVG-filerne. Bemærk, at de indlæses i alfanumerisk rækkefølge.

{% hint style="info" %}
Når SVG-sekvensen er indlæst, konverteres indholdet og gemmes i clippet, så du behøver ikke at bevare en reference til filerne, medmindre du senere vil ændre maskeindstillingerne.
{% endhint %}

* **Use fills as masks** - behandler alle udfyldte former som en maske, dvs. udfyldt med sort. Dette aktiveres automatisk, hvis nogen af dine SVG'er har udfyldte former. Hvis ingen har udfyldte former, deaktiveres det. Se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - hvis formerne i dine SVG'er ikke har nogen konturer, kan vi ikke tegne dem! Denne indstilling tilføjer en kontur (eller _stroke_) til alle udfyldte former. Hvis dine SVG'er ikke har nogen former med stroke, aktiveres den automatisk. Hvis ingen har udfyldte former, deaktiveres den.
* **Invert black lines** - hvis alle linjerne i dine SVG'er er sorte, kan du ikke se dem! Denne indstilling gør dem hvide. Den aktiveres automatisk, hvis dine SVG'er kun har sorte former, men den deaktiveres, hvis du ikke har nogen.
* **Render profile** - se [Renderprofil](fundamentals/render-profile.md "mention")
* **scale** - justerer billedets størrelse.
* **x** og **y** position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - billedets roterede vinkel i grader
* **resolution** - se [Resolution](fundamentals/resolution.md "mention")
* **speed** - varigheden af hele animationen i takter.
* **time per frame** - hvis denne er aktiveret, gælder varigheden pr. frame i stedet for hele animationens længde. Så hvis _speed_ er sat til ¼, varer hvert frame 1 beat.
* **animation direction** -
  * _FORWARDS_ - animationen kører fremad og looper derefter tilbage til begyndelsen
  * _BACKWARDS_ - animationen kører baglæns og looper derefter tilbage til slutningen
  * _PINGPONG_ - animationen kører fremad og derefter baglæns i et loop
  * _MANUAL_ - det aktuelle frame indstilles med indstillingen _position manual_
* **position manual** - indstil det aktuelle frame; 0 % er første frame, 100 % er sidste frame. Dette kan indstilles manuelt eller med en ekstern oscillator.
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Opretter tekst med en TrueType- eller OpenType-skrifttype.

* **Text** - skriv den tekst, du vil bruge, her
* **Font** - vælg den skrifttype, du vil bruge

{% hint style="info" %}
Hvis du vil tilføje flere skrifttyper til Liberation, skal du kopiere .ttf- eller .otf-filerne til mappen data/resources/fonts.
{% endhint %}

* **Render profile** - se [Renderprofil](fundamentals/render-profile.md "mention")
* **horizontal alignment** - vælg _LEFT_, _CENTRE_ eller _RIGHT_ for at vælge tekstjusteringen.
* **Fill state** - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - tekststørrelsen
* **colour -** se [Farveindstillinger og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - billedets roterede vinkel i grader
* **resolution** - se [Resolution](fundamentals/resolution.md "mention")
* **reveal** - brug denne til gradvist at vise teksten, ét tegn ad gangen. Når den er mellem 0 og 50 %, vises teksten gradvist fra venstre mod højre. Når den er mellem 50 % og 100 %, forsvinder teksten fra venstre mod højre. Du kan tilslutte en oscillator til denne socket for at lave animationer.
* **reveal by word** - når denne er aktiveret, arbejder _reveal_ ord for ord i stedet for tegn for tegn.
* **countdown** - et (hurtigt implementeret!) nedtællingssystem. Skifter hver 2. beat, så hvis du vil have sekunder, skal du sørge for at være på 120 bpm.
* **countdown start** - det tal, du vil starte nedtællingen fra
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fills, masks og dybdesortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
