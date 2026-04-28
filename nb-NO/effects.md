---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Effekter

Effektsystemet i Liberation er en morsom og fleksibel måte å endre klipputgangen i sanntid på. Effekter er helt fleksible og kan brukes til å få alt til å blinke av og på, rotere, endre farger eller til og med fly tilfeldig rundt!

Alt du kan gjøre i klippeditoren, kan brukes som en effekt. Faktisk redigeres effekter med nøyaktig samme nodeeditor som klipp! Se [#editing-effects](effects.md#editing-effects "mention"). De kreative mulighetene er praktisk talt uendelige.

Standard effektknapper 1–8 ligger under soneknappene, og effektene 9–24 er de små knappene nederst.

#### Bruke en effekt

Trykk på en effektknapp for å slå effekten av eller på, eller enda bedre: bruk APC40-sliderne 1–8 til å fade effekter inn og ut. For å fade inn en effekt uten APC40 klikker du og drar opp og ned på knappen. Du kan også høyreklikke på effektknappen og justere nivåslideren.

{% hint style="warning" %}
Når du trykker på effektknappen, aktiveres effekten umiddelbart. Men merk at hvis nivået er satt til null, skjer det ingenting! Klikk/dra på knappen for å endre nivået, eller høyreklikk og bruk _level_-slideren, eller bruk APC40-faderne.
{% endhint %}

#### Effekter og klippets zone delay

Effekter henter innstillingen for zone delay fra hvert klipp som kjører for øyeblikket. Så hvis klippet ditt har en forsinkelse som beveger seg fra venstre mot høyre, og du legger til blinkeeffekten, blir blinkingen også forsinket fra venstre mot høyre.

{% hint style="info" %}
Hvordan klippets zone delay arves av effekter, er en av de tingene som er ekstremt vanskelig å beskrive, men helt åpenbart når du prøver det!

Jeg vil påstå at det er et av de morsomste og mest kreative verktøyene som er innebygd i Liberation. Prøv det, så skjønner du hva jeg mener!
{% endhint %}

#### Effektparametere

Legg til en parameter i effekten din med en _Parameter node._ Parametersystemet er en måte å justere flere innstillinger inne i effekten utenfra. Se [parameter-control.md](clip-editor/oscillators/parameter-control.md "mention") for mer informasjon.

Bruk rotary-kontrollerne 1–8 til å justere _parameter_ for hver effekt. Eller høyreklikk på effektknappen og juster parameterslideren(e). Parameterendringen gjør ulike ting avhengig av hvordan effekten er satt opp. Se listen nedenfor for standardeffektene og hva parameterne deres gjør.

{% hint style="info" %}
Rotary-kontrollerne 1–8 ligger langs toppen av en APC40 Mk2 og øverst til høyre på Mk1. Se også: [apc40-reference.md](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
De små tallene du ser på effektknappene, viser til effektens _level_ og _parameter_. _level_ styres av faderen på APC40, eller du kan klikk-dra på knappen. Parameteren justeres med rotary-kontrollerne på APC40, eller du kan høyreklikke for å justere med musen.
{% endhint %}

#### Standardeffektene

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Legger til en kaotisk bevegelse på klipputgangen. Parameteren justerer mengden/hastigheten på kaoset.
2. **Sine wave** :\
   Forvrenger alt innholdet over en bevegelig sinusbølge. Parameteren justerer bølgelengden.
3. **Rotation** :\
   Roterer alt rundt. Parameteren justerer rotasjonshastigheten.
4. **Horizontal flip** :\
   Klemmer sammen og strekker alt horisontalt. Parameteren justerer hastigheten.
5. **Scale** :\
   Skalerer alt gjentatte ganger fra fullt til null. Parameteren justerer hastigheten.
6. **Hue** :\
   Endrer fargetonen på alt, men endrer ikke metningen (dvs. alt som er hvitt, forblir hvitt). Parameteren justerer fargetonen.
7. **Saturation and hue** :\
   Endrer fargetonen på alt og metter også fargen helt (dvs. alt som er hvitt, endres til fargen). Parameteren justerer fargetonen.
8. **Flash** :\
   Blinker gjentatte ganger lysstyrken på alt fra fullt til null. Parameteren justerer blinkehastigheten.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Det finnes ytterligere 16 fargeeffekter langs den nederste raden for å bruke forhåndsinnstilte verdier for fargetone og metning.

Merk at dette er standardeffektene, men de kan redigeres til å gjøre nesten hva du vil!

### Apply to groups

Du kan velge hvilke grupper som påvirkes av effekten. Høyreklikk og slå av eller på gruppeavmerkingsboksene merket _Apply to groups._

Jeg bruker først og fremst dette oppsettet når jeg jobber separat med canvas-grafikk og laserstråler. Jeg tilordner alle canvas-klipp til gruppe 5 og ekskluderer deretter denne gruppen fra effekter som jeg ikke vil skal påvirke disse grafiske klippene.

Du kan også bruke det til å legge på to forskjellige fargeendringer live på to grupper lasere samtidig. Opprett to fargeendringseffekter og velg hvilke klippgrupper hver av dem skal brukes på.

### MX group

Forkortelse for _Mutually Exclusive_. Dette er en måte å gruppere effekter på slik at bare én effekt i gruppen kan være aktiv om gangen. Legg merke til at bare én av standardeffektene for fargeendring kan være aktiv samtidig. Dette er fordi de alle ligger i MX Group 1.

Denne funksjonen er deaktivert hvis innstillingen _MX Group_ er 0.

### Redigere effekter

Høyreklikk på en effekt, og klikk på knappen _EDIT EFFECT_ for å åpne effekteditoren. Legg merke til at denne editoren er identisk med klippeditoren!

Rediger effekten på samme måte som du ville redigert et hvilket som helst klipp. Se [clip-editor](clip-editor/ "mention").

Du må ha minst én creator-node. Dette kan være hva som helst (linje, sirkel, form, til og med tekst!), men du bør sannsynligvis velge noe som gir mest mening i forhåndsvisningen på effektknappen.

Når effekter brukes, erstattes alle creator-noder i effekten med utgangen fra klippene som kjører for øyeblikket.

{% hint style="warning" %}
Av ekstremt kjedelige tekniske årsaker er "trails"-nodene ikke aktivert inne i en effekt. Det samme gjelder "delay"-innstillingen inne i pattern-noder (de bruker samme system). Dette blir rettet i fremtidige versjoner.
{% endhint %}
