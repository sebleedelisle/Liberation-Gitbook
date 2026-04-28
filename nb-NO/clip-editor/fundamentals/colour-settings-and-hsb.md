---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Fargeinnstillinger og HSB

Farger i Liberation defineres som HSB i stedet for RGB. Dette kan være uvant for deg, men jeg synes det er et mye mer intuitivt system når du først blir vant til det.

{% hint style="info" %}
Hvis du foretrekker å bruke RGB, kan du klikke på fargefeltet i en hvilken som helst fargeinnstilling. Dette åpner fargeredigeringspanelet, som gir deg valg for RGB og HSB.
{% endhint %}

### HSB - Hue, Saturation og Brightness

#### Hue

Fargetonen går fra 0 til 255. 0 er rødt, og når du øker verdien, går du gjennom alle fargetonene i regnbuen: oransje, gult, grønt, cyan, blått, lilla, magenta og deretter tilbake til rødt ved 255.

Siden dette er en løkke, kan du bruke en trekantbølge til å gå gjennom alle fargene.

#### Saturation

Denne innstillingen justerer metningen eller intensiteten i fargen. Med andre ord hvor _fargerik_ den er, og den går fra 0 til 255. Sett metningen til 0 for gråtoner, og 255 for fulle regnbuefarger. Et sted i midten gir deg pastellaktige, utvaskede farger.

{% hint style="info" %}
Beklager til mine amerikanske venner for den ekstra vokalen i ordet colour. Liberation er laget i England, så britisk engelsk er standard. I fremtiden håper jeg å tilby oversettelser til fransk, spansk, tysk, italiensk, forenklet kinesisk, og ja, til og med amerikansk engelsk. :innocent:
{% endhint %}

#### Brightness

Sannsynligvis den enkleste å forstå: 0 er helt svart, 255 er full lysstyrke.

### Eksempelbruk

#### Regnbuesyklus:

Sett _Brightness_ og _Saturation_ til 255. Koble en _Sawtooth_-oscillator til _Hue_-inngangen, og juster området fra 0 til 255.

#### Pulserende lysstyrke:

Koble en _Sawtooth_-oscillator til _Brightness_-inngangen, og juster området fra 255 til 0. Du kan justere clamp min og max ytterligere for å kontrollere varigheten på endringen. Bruk deretter easing-funksjonene til å finjustere animasjonen.

#### Hard flash / strobe:

Velg en farge med _Hue_ og _Saturation_, eller ved å klikke på fargevelgeren. Koble en _Square Wave_-oscillator til _Brightness_-inngangen, og juster området fra 255 til 0.

#### Syklus gjennom et egendefinert område med Hue-verdier:

Sett _Brightness_ og _Saturation_ til 255. Koble en _Triangle Wave_-oscillator til _Hue_-inngangen, og juster området:

* for blått til cyan bruker du et område fra 70 til 128
* for rødt til gult bruker du et område fra 0 til 40
* for rødt til magenta bruker du et område fra 255 til 220
