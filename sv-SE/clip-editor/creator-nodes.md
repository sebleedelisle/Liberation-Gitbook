---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator-noder

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Skapar en enskild punkt/stråle.

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **Colour** - punktens färg. Se [Färginställningar och HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- och **y**-position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Skapar en linje/ljusplan.

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **Size** - linjens längd
* **Colour** - linjens färg. Se [Färginställningar och HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- och **y**-position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - linjens vinkel, i grader
* **resolution** - se [Upplösning](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ bestämmer linjens startpunkt och rotationscentrum
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Skapar en cirkel/kon.

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **radius** - cirkelns radie
* **Colour** - cirkelns färg. Se [Färginställningar och HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- och **y**-position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **resolution** - se [Upplösning](fundamentals/resolution.md "mention")
* **Fill state** - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Skapar en liksidig polygon, till exempel triangel, kvadrat eller pentagon.

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **size** - avståndet från mitten till varje hörn
* **Colour** - polygonens färg. Se [Färginställningar och HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- och **y**-position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - formens roterade vinkel, i grader
* **resolution** - se [Upplösning](fundamentals/resolution.md "mention")
* **Fill state** - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Läser in en SVG-fil för egna former.

{% hint style="warning" %}
Liberation är kompatibelt med formatet _SVGTiny_. InkScape rekommenderas, men de flesta program för vektorgrafik kan exportera i det här formatet. Se till att konvertera all text till former innan du exporterar. Liberation renderar linjer och kan även använda fyllningar som masker. Se till att dina linjer inte är svarta, annars syns de inte utan en färgmodifierare!
{% endhint %}

* **Import SVG** - läs in en SVG-fil från disk.

{% hint style="info" %}
När en SVG har lästs in konverteras innehållet och sparas i clipet, så du behöver inte behålla någon referens till filen, om du inte senare vill ändra maskinställningarna.
{% endhint %}

* **Use fills as masks** - behandlar alla fyllda former som masker, dvs fyllda med svart. Detta aktiveras automatiskt om din SVG innehåller fyllda former. Om den inte innehåller några fyllda former inaktiveras det. Se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - om formerna i din SVG inte har någon kontur kan vi inte rita dem! Det här alternativet lägger till en kontur (eller _stroke_) på varje fylld form. Om din SVG inte har några former med linje aktiveras det automatiskt. Om den inte har några fyllda former inaktiveras det.
* **Invert black lines** - om alla linjer i din SVG är svarta kan du inte se dem! Det här alternativet gör dem vita. Det aktiveras automatiskt om din SVG bara har svarta former, men inaktiveras om du inte har några.
* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **scale** - justerar SVG:ns storlek. Detta beräknas automatiskt när SVG:n läses in (för att säkerställa att bilden syns), men kan därefter ändras manuellt.
* **x**- och **y**-position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - bildens roterade vinkel, i grader
* **resolution** - se [Upplösning](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Skapar en animation från en sekvens av SVG-filer.

* **Import SVG Sequence** - välj mappen som innehåller alla SVG-filer. Observera att de läses in i alfanumerisk ordning.

{% hint style="info" %}
När SVG-sekvensen har lästs in konverteras innehållet och sparas i clipet, så du behöver inte behålla någon referens till filerna, om du inte senare vill ändra maskinställningarna.
{% endhint %}

* **Use fills as masks** - behandlar alla fyllda former som masker, dvs fyllda med svart. Detta aktiveras automatiskt om någon av dina SVG:er innehåller fyllda former. Om ingen innehåller fyllda former inaktiveras det. Se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - om formerna i dina SVG:er inte har några konturer kan vi inte rita dem! Det här alternativet lägger till en kontur (eller _stroke_) på varje fylld form. Om dina SVG:er inte har några former med linje aktiveras det automatiskt. Om ingen har några fyllda former inaktiveras det.
* **Invert black lines** - om alla linjer i dina SVG:er är svarta kan du inte se dem! Det här alternativet gör dem vita. Det aktiveras automatiskt om dina SVG:er bara har svarta former, men inaktiveras om du inte har några.
* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **scale** - justerar bildens storlek.
* **x**- och **y**-position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - bildens roterade vinkel, i grader
* **resolution** - se [Upplösning](fundamentals/resolution.md "mention")
* **speed** - hela animationens längd, i takter.
* **time per frame** - om detta är aktiverat gäller längden per bildruta i stället för animationens fulla längd. Om _speed_ till exempel är satt till ¼ blir varje bildruta 1 slag.
* **animation direction** -
  * _FORWARDS_ - animationen kör framåt och loopar sedan tillbaka till början
  * _BACKWARDS_ - animationen kör bakåt och loopar sedan tillbaka till slutet
  * _PINGPONG_ - animationen kör framåt och sedan bakåt i en loop
  * _MANUAL_ - aktuell bildruta anges med inställningen _position manual_
* **position manual** - anger aktuell bildruta; 0 % är första bildrutan och 100 % är sista bildrutan. Detta kan ställas in manuellt eller med en extern oscillator.
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Skapar text med ett TrueType- eller OpenType-typsnitt.

* **Text** - skriv texten du vill använda här
* **Font** - välj typsnittet du vill använda

{% hint style="info" %}
För att lägga till fler typsnitt i Liberation kopierar du .ttf- eller .otf-filerna till mappen data/resources/fonts.
{% endhint %}

* **Render profile** - se [Render profile](fundamentals/render-profile.md "mention")
* **horizontal alignment** - välj _LEFT_, _CENTRE_ eller _RIGHT_ för att ange textjustering.
* **Fill state** - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - textstorleken
* **colour -** se [Färginställningar och HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- och **y**-position - se [Koordinatsystem](fundamentals/co-ordinate-system.md "mention")
* **rotation** - bildens roterade vinkel, i grader
* **resolution** - se [Upplösning](fundamentals/resolution.md "mention")
* **reveal** - använd detta för att gradvis visa texten, ett tecken i taget. När värdet ligger mellan 0 och 50 % visas texten gradvis från vänster till höger. När det ligger mellan 50 % och 100 % försvinner texten från vänster till höger. Du kan ansluta en oscillator till den här sockeln för att skapa animationer.
* **reveal by word** - när detta är aktiverat arbetar _reveal_ ord för ord i stället för tecken för tecken.
* **countdown** - ett (snabbt implementerat!) nedräkningssystem. Det ändras varannan beat, så om du vill ha sekunder ska du se till att du ligger på 120 bpm.
* **countdown start** - numret som du vill att nedräkningen ska börja från
* _MOVE TO FRONT / MOVE TO BACK_ - se [Fyllningar, masker och djupsortering](fundamentals/fills-masks-and-depth-sorting.md "mention")
