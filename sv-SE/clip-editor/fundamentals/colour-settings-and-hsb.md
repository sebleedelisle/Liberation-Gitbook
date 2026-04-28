---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Färginställningar och HSB

Färg i Liberation definieras som HSB i stället för RGB. Det kan kännas ovant, men när du väl har vant dig tycker jag att det är ett mycket mer intuitivt system.

{% hint style="info" %}
Om du föredrar att använda RGB kan du klicka på färgrutan i valfri färginställning. Då öppnas färgredigeringspanelen, där du får alternativ för både RGB och HSB.
{% endhint %}

### HSB - Hue, Saturation och Brightness

#### Hue

Färgnyansen går från 0 till 255. 0 är rött, och när du ökar värdet passerar du genom alla nyanser i regnbågen: orange, gult, grönt, cyan, blått, lila, magenta och sedan tillbaka till rött vid 255.

Eftersom detta är en loop kan du använda en triangelvåg för att gå igenom alla färger.

#### Saturation

Den här inställningen justerar färgens mättnad eller intensitet. Med andra ord hur _färgstark_ den är, och värdet går från 0 till 255. Ställ in mättnaden på 0 för gråskalor och 255 för fulla regnbågsfärger. Någonstans i mitten får du pastelliga, urblekta färger.

{% hint style="info" %}
Ursäkta till mina amerikanska vänner för den extra vokalen i ordet colour. Liberation är gjort i England, så brittisk engelska är standard. I framtiden hoppas jag kunna erbjuda översättningar till franska, spanska, tyska, italienska, förenklad kinesiska och ja, till och med amerikansk engelska. :innocent:
{% endhint %}

#### Brightness

Förmodligen enklast att förstå: 0 är helt svart, 255 är full ljusstyrka.

### Exempel på användning

#### Regnbågscykel :

Ställ in _Brightness_ och _Saturation_ på 255. Anslut en _Sawtooth_-oscillator till din _Hue_-socket och justera dess intervall från 0 till 255.

#### Pulserande ljusstyrka :

Anslut en _Sawtooth_-oscillator till din _Brightness_-socket och justera dess intervall från 255 till 0. Du kan även justera clamp min och max för att styra ändringens varaktighet. Använd sedan easing-funktionerna för att finjustera animationen ytterligare.

#### Hård blixt / strobe :

Välj en färg med _Hue_ och _Saturation_ eller genom att klicka på färgväljaren. Anslut en _Square Wave_-oscillator till din _Brightness_-socket och justera dess intervall från 255 till 0.

#### Cykla genom ett eget nyansintervall :

Ställ in _Brightness_ och _Saturation_ på 255. Anslut en _Triangle Wave_-oscillator till din _Hue_-socket och justera dess intervall :

* för blått till cyan använder du intervallet 70 till 128
* för rött till gult använder du intervallet 0 till 40
* för rött till magenta använder du intervallet 255 till 220
