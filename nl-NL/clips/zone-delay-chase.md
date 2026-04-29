---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

We zijn het er allemaal over eens dat meer lasers meer plezier betekent. Maar als ze allemaal precies hetzelfde doen, mis je creatieve mogelijkheden.

Het zone-delay-systeem is een eenvoudige maar effectieve manier om variatie tussen zones aan te brengen en zo echt het meeste uit een opstelling met meerdere lasers te halen. Je kunt het ook gebruiken om een traditioneler chase-effect te maken.

#### Hoe het werkt

_Zone delay_ voegt een vertraging toe aan de timing van de clip per zone, waardoor een soort sweep over de zones ontstaat.

Het is erg effectief om zone delay toe te voegen aan een clip die al loopt. Gebruik de bijbehorende bediening op de APC40 om het niveau en het patroon aan te passen. (Zie [APC40-referentie](../reference/apc40-reference.md "mention")). Je kunt ook het paneel _Clip Settings_ gebruiken.

Zone delay-instellingen:

* **Zone delay** - bepaalt hoeveel vertraging op elke zone wordt toegepast, gemeten in 64e noten.
* **Pattern** - kies de volgorde van de zones
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Het patroon werkt op basis van de zonenummers en gaat ervan uit dat je zones van links naar rechts op volgorde staan. Bij het berekenen van patronen behandelt Zone delay canvas-zones en DMX-zones als aparte groepen.
{% endhint %}

* **Delay mode**
  1. No delay - gebruik dit in chase mode
  2. Delay - de standaardmodus; vertraagt de timing van elke zone
  3. Delay with re-trigger - zet de clip bij elke stap door het patroon terug naar het begin. Dit werkt goed met _Chase mode_.
* **Chase mode** - wanneer chase mode aan staat, wordt elke zone aan- en uitgezet zoals bij een traditioneel chase-effect. Pas het uiterlijk van de chase aan met de instellingen _Fade in, Hold,_ en _Fade out_. Deze instellingen worden ingesteld als verhouding van de zone-delay-waarde, dus een waarde van 1 is dezelfde tijd als opgegeven bij _Zone delay_. Het is wat lastig uit te leggen, dus mijn advies is: probeer het vooral zelf uit.

{% hint style="info" %}
Zone delay wordt ook toegepast op actieve effecten. Een knippereffect wordt bijvoorbeeld ook over de zones vertraagd, net als de animatie binnen de clip zelf.
{% endhint %}

Wanneer een clip een vorm van _Zone delay_ heeft, zie je rechtsboven in de clip een pictogram met drie puntjes. Deze puntjes zijn geanimeerd om de stijl van _Zone delay_ voor die clip te tonen. Zie [Wat betekenen de kleine pictogrammen op de clipknoppen?](what-are-the-small-icons-on-the-clip-buttons.md "mention") voor meer informatie.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Het symbool met drie puntjes dat aangeeft dat een clip een zone delay heeft, inclusief de bijbehorende modus</p></figcaption></figure>

{% hint style="info" %}
Zone delay is een instelling die bij elke clip hoort. Het is niet globaal; het maakt deel uit van het creatieve ontwerp van een clip.
{% endhint %}
