---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Soneforsinkelse / chase

Vi er alle enige om at flere lasere betyr mer moro, men hvis alle gjør nøyaktig det samme, går du glipp av kreative muligheter.

Systemet for soneforsinkelse er en enkel, men effektiv måte å skape variasjon på tvers av zones, og kan virkelig utnytte et oppsett med flere lasere. Det kan også brukes til å lage en mer tradisjonell chase-effekt.

#### Slik fungerer det

_Zone delay_ legger til en forsinkelse i timingen til klippet på tvers av hver sone, og skaper en slags sveip gjennom sonene.

Det er veldig effektivt å legge _Zone delay_ til et klipp som allerede kjører. Bruk den relevante kontrollen på APC40 for å justere nivå og mønster. (Se [APC40-referanse](../reference/apc40-reference.md "mention")). Du kan også bruke _Clip Settings_-panelet.

Innstillinger for Zone delay:

* **Zone delay** – styrer hvor mye forsinkelse som legges på hver sone, målt i 64-delsnoter.
* **Pattern** – velg sonerekkefølge
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Mønsteret bruker sonenumrene og forutsetter at sonene dine er ordnet fra venstre mot høyre. Zone delay behandler canvas-soner og DMX-soner som separate grupper når mønstrene beregnes.
{% endhint %}

* **Delay mode**
  1. No delay – bruk dette i chase-modus
  2. Delay – standardmodusen, forsinker timingen for hver sone
  3. Delay with re-trigger – tilbakestiller klippet til starten hver gang gjennom mønsteret. Dette fungerer godt med _Chase mode_.
* **Chase mode** – når chase-modus er på, slås hver sone av og på som i en tradisjonell chase-effekt. Juster hvordan chasen ser ut med innstillingene _Fade in, Hold,_ og _Fade out_. Disse innstillingene angis som en andel av Zone delay-verdien, så en verdi på 1 vil gi samme tid som er angitt i _Zone delay_-verdien. Det er litt vanskelig å forklare, så mitt råd er å prøve selv.

{% hint style="info" %}
Zone delay brukes også på alle aktive effekter. For eksempel vil en blinkende effekt bli forsinket på tvers av sonene, i tillegg til animasjonen i selve klippet.
{% endhint %}

Når et klipp har en form for _Zone delay_, ser du et ikon med tre prikker øverst til høyre på klippet. Disse prikkene er animert for å vise hvilken type _Zone delay_ klippet har. Se [Hva er de små ikonene på clip-knappene?](what-are-the-small-icons-on-the-clip-buttons.md "mention") for mer informasjon.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Symbolet med tre prikker som viser at et klipp har soneforsinkelse og hvilken modus det bruker</p></figcaption></figure>

{% hint style="info" %}
Zone delay er en innstilling som tilhører hvert enkelt klipp. Den er ikke global, men en del av den kreative utformingen av et klipp.
{% endhint %}
