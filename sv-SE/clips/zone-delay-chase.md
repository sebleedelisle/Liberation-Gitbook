---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Vi är nog alla överens om att fler lasrar betyder roligare shower, men om alla gör exakt samma sak går du miste om kreativa möjligheter.

Systemet för Zone delay är ett enkelt men effektivt sätt att skapa variation mellan zones och kan verkligen utnyttja en uppsättning med flera lasrar. Det kan också användas för att skapa en mer traditionell chase-effekt.

#### Så fungerar det

_Zone delay_ lägger till en fördröjning i klippets timing för varje zon, vilket skapar en slags svepning över zonerna.

Det är väldigt effektivt att lägga till Zone delay i ett klipp som redan spelas. Använd motsvarande kontroll på APC40 för att justera nivå och mönster. (Se [APC40-referens](../reference/apc40-reference.md "mention")). Du kan också använda panelen _Clip Settings_.

Inställningar för Zone delay:

* **Zone delay** - styr hur mycket fördröjning som läggs på varje zon, mätt i 64-delar.
* **Pattern** - välj zonordning
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Mönstret baseras på zonnumren och förutsätter att dina zoner ligger i ordning från vänster till höger. Zone delay behandlar canvas-zoner och DMX-zoner som separata grupper när mönstren beräknas.
{% endhint %}

* **Delay mode**
  1. No delay - använd detta i chase-läge
  2. Delay - standardläget, fördröjer timingen för varje zon
  3. Delay with re-trigger - återställer klippet till början varje gång genom mönstret. Detta fungerar bra med _Chase mode_.
* **Chase mode** - när chase-läget är på slås varje zon på och av som i en traditionell chase-effekt. Justera chase-utseendet med inställningarna _Fade in, Hold,_ och _Fade out_. Dessa inställningar anges som en andel av värdet för Zone delay, så ett värde på 1 motsvarar samma tid som anges i _Zone delay_. Det är lite svårt att förklara, så mitt råd är att prova själv.

{% hint style="info" %}
Zone delay tillämpas även på alla aktiva effekter. Till exempel kommer en blinkande effekt att fördröjas över zonerna, precis som animationen i själva klippet.
{% endhint %}

När ett klipp har någon form av _Zone delay_ visas en ikon med tre punkter längst upp till höger på klippet. Punkterna är animerade för att visa vilken typ av _Zone delay_ klippet använder. Se [Vad betyder de små ikonerna på clip-knapparna?](what-are-the-small-icons-on-the-clip-buttons.md "mention") för mer information.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Symbolen med tre punkter som visar att ett klipp har Zone delay och vilket läge det använder</p></figcaption></figure>

{% hint style="info" %}
Zone delay är en inställning som hör till varje enskilt klipp. Den är inte global, utan är en del av klippets kreativa utformning.
{% endhint %}
