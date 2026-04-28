---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Farveindstillinger og HSB

Farver i Liberation defineres som HSB i stedet for RGB. Det er måske uvant for dig, men når du først vænner dig til det, synes jeg, det er et langt mere intuitivt system.

{% hint style="info" %}
Hvis du foretrækker at bruge RGB, kan du klikke på farvefeltet i en hvilken som helst farveindstilling. Det åbner farveredigeringspanelet, hvor du får valgmuligheder for RGB og HSB.
{% endhint %}

### HSB - Hue, Saturation og Brightness

#### Hue

Farvetonen går fra 0 til 255. 0 er rød, og efterhånden som du øger værdien, bevæger du dig gennem alle regnbuens farvetoner: orange, gul, grøn, cyan, blå, lilla, magenta og derefter tilbage til rød ved 255.

Da dette er en løkke, kan du bruge en triangle wave til at cykle gennem alle farver.

#### Saturation

Denne indstilling justerer farvens mætning eller intensitet. Med andre ord, hvor _farverig_ den er, og værdien går fra 0 til 255. Sæt din saturation til 0 for gråtoner og til 255 for fulde regnbuefarver. Et sted midt imellem giver dig pastelfarver med et mere afdæmpet udtryk.

{% hint style="info" %}
Beklager til mine amerikanske venner for den ekstra vokal i ordet colour. Liberation er lavet i England, så britisk engelsk er standarden. I fremtiden håber jeg at kunne tilbyde oversættelser til fransk, spansk, tysk, italiensk, forenklet kinesisk og ja, endda amerikansk engelsk. :innocent:
{% endhint %}

#### Brightness

Nok den nemmeste at forstå: 0 er helt sort, og 255 er fuld lysstyrke.

### Eksempel på brug

#### Regnbuecyklus :

Sæt _Brightness_ og _Saturation_ til 255. Forbind en _Sawtooth_-oscillator til din _Hue_-socket, og juster dens område fra 0 til 255.

#### Pulserende lysstyrke :

Forbind en _Sawtooth_-oscillator til din _Brightness_-socket, og juster dens område fra 255 til 0. Du kan derefter justere clamp min og max yderligere for at styre ændringens varighed. Brug derefter easing-funktionerne til at finjustere animationen yderligere.

#### Hårdt flash / strobe :

Vælg en farve med _Hue_ og _Saturation_ eller ved at klikke på farvevælgeren. Forbind en _Square Wave_-oscillator til din _Brightness_-socket, og juster dens område fra 255 til 0.

#### Cykl gennem et brugerdefineret område af farvetoner :

Sæt _Brightness_ og _Saturation_ til 255. Forbind en _Triangle Wave_-oscillator til din _Hue_-socket, og juster dens område :

* for blå til cyan skal du bruge et område fra 70 til 128
* for rød til gul skal du bruge et område fra 0 til 40
* for rød til magenta skal du bruge et område fra 255 til 220
