---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Vi er vist alle enige om, at flere lasere giver mere sjov, men hvis de alle gør præcis det samme, går du glip af kreative muligheder.

Zone delay-systemet er en enkel, men effektiv måde at skabe variation på tværs af zoner og kan virkelig udnytte et setup med flere lasere. Det kan også bruges til at lave en mere traditionel chase-effekt.

#### Sådan fungerer det

_Zone delay_ tilføjer en forsinkelse til clip’ens timing på tværs af hver zone, så der opstår en slags sweep gennem zonerne.

Det er meget effektivt at tilføje zone delay til en clip, der allerede kører. Brug den relevante kontrol på APC40 til at justere niveau og mønster. (Se [APC40-reference](../reference/apc40-reference.md "mention")). Du kan også bruge panelet _Clip Settings_.

Zone delay-indstillinger:

* **Zone delay** - styrer mængden af forsinkelse, der anvendes på hver zone, målt i 64.-delsnoder.
* **Pattern** - vælg zonerækkefølgen
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Mønsteret bruger zonenumrene og antager, at dine zoner er ordnet fra venstre mod højre. Zone delay behandler canvas-zoner og DMX-zoner som separate grupper, når mønstrene beregnes.
{% endhint %}

* **Delay mode**
  1. No delay - brug denne i chase mode
  2. Delay - standardtilstanden, som forsinker timingen for hver zone
  3. Delay with re-trigger - nulstiller clip’en tilbage til starten hver gang gennem mønsteret. Det fungerer godt med _Chase mode_.
* **Chase mode** - når chase mode er slået til, tændes og slukkes hver zone som en traditionel chase-effekt. Juster chase-udseendet med indstillingerne _Fade in, Hold,_ og _Fade out_. Disse indstillinger angives som en andel af zone delay-værdien, så en værdi på 1 svarer til den samme tid som angivet i _Zone delay_-værdien. Det er lidt svært at forklare, så mit råd er at prøve det selv.

{% hint style="info" %}
Zone delay anvendes også på alle aktive effekter. For eksempel bliver en blinkende effekt forsinket på tværs af zonerne, ligesom animationen i selve clip’en.
{% endhint %}

Når en clip har en eller anden form for _Zone delay_, vises et ikon med tre prikker øverst til højre på clip’en. Prikkerne er animerede for at vise typen af _Zone delay_ for den pågældende clip. Se [Hvad betyder de små ikoner på clip-knapperne?](what-are-the-small-icons-on-the-clip-buttons.md "mention") for flere detaljer.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Symbolet med tre prikker, som viser, at en clip har zone delay og hvilken tilstand den bruger</p></figcaption></figure>

{% hint style="info" %}
Zone delay er en indstilling, der hører til den enkelte clip. Den er ikke global; den er en del af clip’ens kreative design.
{% endhint %}
