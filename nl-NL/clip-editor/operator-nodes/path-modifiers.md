---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

Deze node vervangt de inhoud van lijnen en vormen door gelijkmatig verdeelde dots (bestaande dots blijven ongewijzigd).

* **Colour** – de kleur van de dots. Wordt genegeerd als _Inherit Colour_ is ingeschakeld; zie hieronder. _Zie ook_ [Kleurinstellingen en HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – de afstand tussen dots, gemeten in pixels. Kleinere waarden = meer dots, grotere waarden = minder.
* **Offset** – verschuift de startpositie van de dots als percentage van de spacing. Kan worden geanimeerd (bijv. met een sawtooth Oscillator Node) om “reizende” dot-effecten te maken.
* **Keep Original** – als dit is ingeschakeld, blijven de oorspronkelijke lijnen/vormen behouden en worden de dots eroverheen getekend.
* **Render Profile** – kiest de renderkwaliteit. _Zie_ [Render Profile](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – past de spacing automatisch aan zodat de padlengte er precies door deelbaar is.
* **Fade Out Ends** – vermindert geleidelijk de helderheid van dots richting het begin en einde van het pad. Handig wanneer je **Offset** animeert met een sawtooth Oscillator Node, zodat dots soepel in- en uitfaden terwijl ze naar het einde van de vorm bewegen.

## &#x20;Trimmer

Deze node trimt de zichtbare lengte van lijnen en vormen, zodat je ze in de tijd kunt onthullen, verbergen of animeren.

* **Offset** – bepaalt waar het zichtbare deel van de vorm begint. Zelfs met _Trim Size_ op 0% zorgt het animeren van Offset van 0% → 100% ervoor dat de vorm wordt ingetekeend, bij 50% volledig zichtbaar is en daarna weer verdwijnt.
* **Trim Size** – stelt in hoeveel van de vorm behouden blijft, als percentage van de totale lengte.
* **Loop** – behandelt de vorm als een doorlopende loop, zodat het einde weer aansluit op het begin in plaats van te verdwijnen.
* **All Shapes** – combineert alle invoervormen en trimt ze alsof ze één enkel pad zijn. Als dit uit staat, wordt elke vorm afzonderlijk getrimd.
* **Add Dot at Start / Add Dot at End** – voegt een dot in de gekozen kleur toe op de trimpunten. (Als er geen trim wordt toegepast, worden er geen dots toegevoegd.)
* **Colour** – de kleur van de trim-dots. _Zie ook_ [Kleurinstellingen en HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – kiest het renderprofiel voor de dots. _Zie_ [Render Profile](../fundamentals/render-profile.md "mention")
