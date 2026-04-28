---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator-nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Maakt één punt / beam.

* **Render profile** - zie [render-profile.md](fundamentals/render-profile.md "mention")
* **Colour** - de kleur van het punt. Zie [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- en **y**-positie - zie [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Maakt een lijn / sheet.

* **Render profile** - zie [render-profile.md](fundamentals/render-profile.md "mention")
* **Size** - de lengte van de lijn
* **Colour** - de kleur van de lijn. Zie [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- en **y**-positie - zie [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - de hoek van de lijn, in graden
* **resolution** - zie [resolution.md](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ bepaalt het startpunt en het rotatiecentrum van de lijn
* _MOVE TO FRONT / MOVE TO BACK_ - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Maakt een cirkel / cone.

* **Render profile** - zie [render-profile.md](fundamentals/render-profile.md "mention")
* **radius** - de straal van de cirkel
* **Colour** - de kleur van de cirkel. Zie [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- en **y**-positie - zie [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **resolution** - zie [resolution.md](fundamentals/resolution.md "mention")
* **Fill state** - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Maakt een gelijkzijdige veelhoek, zoals een driehoek, vierkant, vijfhoek enzovoort.

* **Render profile** - zie [render-profile.md](fundamentals/render-profile.md "mention")
* **size** - de afstand van het midden tot elk van de hoeken
* **Colour** - de kleur van de veelhoek. Zie [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- en **y**-positie - zie [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - de rotatiehoek van de vorm, in graden
* **resolution** - zie [resolution.md](fundamentals/resolution.md "mention")
* **Fill state** - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Laadt een SVG-bestand voor aangepaste vormen.

{% hint style="warning" %}
Liberation is compatibel met de _SVGTiny_-indeling. InkScape wordt aanbevolen, maar de meeste vectorprogramma's kunnen naar deze indeling exporteren. Zorg dat je tekst omzet naar vormen voordat je exporteert. Liberation rendert strokes en kan fills optioneel als masks gebruiken. Zorg dat je lijnen niet zwart zijn, anders worden ze zonder colour modifier niet weergegeven!
{% endhint %}

* **Import SVG** - laad een SVG-bestand vanaf schijf.

{% hint style="info" %}
Zodra een SVG is geladen, wordt de inhoud geconverteerd en in de clip opgeslagen. Je hoeft dus geen verwijzing naar het bestand te bewaren, tenzij je later de mask-instellingen wilt wijzigen.
{% endhint %}

* **Use fills as masks** - verwerkt elke gevulde vorm als een mask, oftewel gevuld met zwart. Dit wordt automatisch ingesteld als je SVG gevulde vormen bevat. Als er geen gevulde vormen zijn, wordt dit uitgeschakeld. Zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - als de vormen in je SVG geen outline hebben, kunnen we ze niet tekenen! Deze optie voegt een outline (of _stroke_) toe aan elke gevulde vorm. Als je SVG geen vormen met een stroke bevat, wordt dit automatisch ingesteld. Als er geen gevulde vormen zijn, wordt het uitgeschakeld.
* **Invert black lines** - als alle lijnen in je SVG zwart zijn, kun je ze niet zien! Deze optie maakt ze wit. Dit wordt automatisch ingesteld als je SVG alleen zwarte vormen bevat, maar wordt uitgeschakeld als je die niet hebt.
* **Render profile** - zie [render-profile.md](fundamentals/render-profile.md "mention")
* **scale** - past de grootte van de SVG aan. Dit wordt automatisch berekend wanneer de SVG wordt geladen (zodat de afbeelding zichtbaar is), maar kan daarna handmatig worden aangepast.
* **x**- en **y**-positie - zie [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - de rotatiehoek van de afbeelding, in graden
* **resolution** - zie [resolution.md](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Maakt een animatie van een reeks SVG-bestanden.

* **Import SVG Sequence** - kies de map waarin alle SVG-bestanden staan. Let op: ze worden in alfanumerieke volgorde geladen.

{% hint style="info" %}
Zodra de SVG-reeks is geladen, wordt de inhoud geconverteerd en in de clip opgeslagen. Je hoeft dus geen verwijzing naar de bestanden te bewaren, tenzij je later de mask-instellingen wilt wijzigen.
{% endhint %}

* **Use fills as masks** - verwerkt elke gevulde vorm als een mask, oftewel gevuld met zwart. Dit wordt automatisch ingesteld als een van je SVG's gevulde vormen bevat. Als geen enkele SVG gevulde vormen bevat, wordt dit uitgeschakeld. Zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - als de vormen in je SVG's geen outlines hebben, kunnen we ze niet tekenen! Deze optie voegt een outline (of _stroke_) toe aan elke gevulde vorm. Als je SVG's geen vormen met een stroke bevatten, wordt dit automatisch ingesteld. Als geen enkele SVG gevulde vormen bevat, wordt het uitgeschakeld.
* **Invert black lines** - als alle lijnen in je SVG's zwart zijn, kun je ze niet zien! Deze optie maakt ze wit. Dit wordt automatisch ingesteld als je SVG's alleen zwarte vormen bevatten, maar wordt uitgeschakeld als je die niet hebt.
* **Render profile** - zie [render-profile.md](fundamentals/render-profile.md "mention")
* **scale** - past de grootte van de afbeelding aan.
* **x**- en **y**-positie - zie [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - de rotatiehoek van de afbeelding, in graden
* **resolution** - zie [resolution.md](fundamentals/resolution.md "mention")
* **speed** - de duur van de volledige animatie, in maten.
* **time per frame** - als dit is ingesteld, geldt de duur per frame in plaats van voor de volledige lengte van de animatie. Dus als _speed_ is ingesteld op ¼, duurt elk frame 1 beat.
* **animation direction** -
  * _FORWARDS_ - de animatie loopt vooruit en herhaalt daarna vanaf het begin
  * _BACKWARDS_ - de animatie loopt achteruit en herhaalt daarna vanaf het einde
  * _PINGPONG_ - de animatie loopt vooruit en daarna achteruit in een lus
  * _MANUAL_ - het huidige frame wordt ingesteld met de instelling _position manual_
* **position manual** - stel het huidige frame in: 0% is het eerste frame, 100% is het laatste frame. Dit kan handmatig worden ingesteld of met een externe oscillator.
* _MOVE TO FRONT / MOVE TO BACK_ - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Maakt tekst met een TrueType- of OpenType-lettertype.

* **Text** - typ hier de gewenste tekst
* **Font** - kies het gewenste lettertype

{% hint style="info" %}
Als je meer lettertypen aan Liberation wilt toevoegen, kopieer je de .ttf- of .otf-bestanden naar de map data/resources/fonts.
{% endhint %}

* **Render profile** - zie [render-profile.md](fundamentals/render-profile.md "mention")
* **horizontal alignment** - kies _LEFT_, _CENTRE_ of _RIGHT_ om de tekstuitlijning te selecteren.
* **Fill state** - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - de tekstgrootte
* **colour -** zie [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- en **y**-positie - zie [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - de rotatiehoek van de afbeelding, in graden
* **resolution** - zie [resolution.md](fundamentals/resolution.md "mention")
* **reveal** - gebruik dit om de tekst geleidelijk te tonen, één teken per keer. Tussen 0 en 50% verschijnt de tekst geleidelijk van links naar rechts. Tussen 50% en 100% verdwijnt de tekst van links naar rechts. Je kunt een oscillator met deze socket verbinden om animaties te maken.
* **reveal by word** - wanneer dit is ingesteld, werkt _reveal_ per woord in plaats van per teken.
* **countdown** - een (haastig geïmplementeerd!) countdown-systeem. Verandert elke 2 beats, dus als je seconden wilt, zorg dan dat je op 120 bpm zit.
* **countdown start** - het getal waarmee je de countdown wilt laten beginnen
* _MOVE TO FRONT / MOVE TO BACK_ - zie [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
