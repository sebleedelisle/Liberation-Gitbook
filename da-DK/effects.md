---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Effekter

Effektsystemet i Liberation er en sjov og fleksibel måde at ændre Clip-outputtet i realtid. Effekter er helt fleksible og kan bruges til at få alt til at blinke til og fra, rotere, skifte farver eller endda flyve tilfældigt rundt!

Alt, hvad du kan gøre i Clip-editoren, kan bruges som en effekt. Faktisk redigeres effekter med præcis den samme node-editor som clips! Se [Effekter](effects.md#editing-effects "mention"). De kreative muligheder er stort set uendelige.

Standard-effektknapperne 1-8 ligger under zoneknapperne, og effekterne 9-24 er de små knapper nederst.

#### Anvend en effekt

Tryk på en effektknap for at slå effekten til eller fra – eller endnu bedre: brug APC40-skyderne 1-8 til at fade effekter ind og ud. Hvis du vil fade en effekt ind uden en APC40, kan du klikke og trække op og ned på knappen. Du kan også højreklikke på effektknappen og justere _level_-skyderen.

{% hint style="warning" %}
Når du trykker på effektknappen, aktiveres effekten med det samme. Bemærk dog, at hvis level er sat til nul, sker der ingenting! Klik/træk på knappen for at ændre level, eller højreklik og brug _level_-skyderen, eller brug APC40-faderne.
{% endhint %}

#### Effekter og klippets zone delay

Effekter overtager zone delay-indstillingen for hvert clip, der kører i øjeblikket. Så hvis dit clip har en forsinkelse, der bevæger sig fra venstre mod højre, og du tilføjer blink-effekten, bliver blinket også forsinket fra venstre mod højre.

{% hint style="info" %}
Måden, et clips zone delay nedarves af effekter på, er en af de ting, der er ekstremt svær at beskrive, men indlysende, når du prøver det!

Jeg vil mene, at det er et af de sjoveste og mest kreative værktøjer, der er indbygget i Liberation. Prøv det, så kan du se, hvad jeg mener!
{% endhint %}

#### Effektparametre

Tilføj en parameter til din effekt med en _Parameter node._ Parameter-systemet er en måde at justere flere indstillinger inde i effekten udefra. Se [Parameter Control](clip-editor/oscillators/parameter-control.md "mention") for flere oplysninger.

Brug drejeknapperne 1-8 til at justere _parameter_ for hver effekt. Eller højreklik på effektknappen og juster parameter-skyderen eller -skyderne. Parameterændringen gør forskellige ting, afhængigt af hvordan effekten er sat op. Se listen nedenfor for standardeffekterne og hvad deres parametre gør.

{% hint style="info" %}
Rotary controllers 1-8 sidder langs toppen af en APC40 Mk2 og øverst til højre på Mk1. Se også: [APC40-reference](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
De små tal, du ser på effektknapperne, henviser til effektens _level_ og _parameter_. _level_ styres af faderen på APC40, eller du kan klikke og trække på knappen. Parameteren justeres med drejeknapperne på APC40, eller du kan højreklikke for at justere med musen.
{% endhint %}

#### Standardeffekterne

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Tilføjer en kaotisk bevægelse til Clip-outputtet. Parameteren justerer mængden/hastigheden af kaos.
2. **Sine wave** :\
   Forvrænger alt indhold hen over en bevægende sinusbølge. Parameteren justerer bølgelængden.
3. **Rotation** :\
   Roterer det hele. Parameteren justerer rotationshastigheden.
4. **Horizontal flip** :\
   Klemmer og strækker det hele vandret. Parameteren justerer hastigheden.
5. **Scale** :\
   Skalerer gentagne gange det hele fra fuld størrelse til nul. Parameteren justerer hastigheden.
6. **Hue** :\
   Ændrer farvetonen på det hele, men ændrer ikke mætningen (dvs. alt, der er hvidt, forbliver hvidt). Parameteren justerer farvetonen.
7. **Saturation and hue** :\
   Ændrer farvetonen på det hele og mætter også farven helt (dvs. alt, der er hvidt, skifter til farven). Parameteren justerer farvetonen.
8. **Flash** :\
   Blinker gentagne gange lysstyrken på det hele fra fuld til nul. Parameteren justerer blinkhastigheden.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Der er yderligere 16 farveeffekter langs den nederste række, som anvender forudindstillede hue- og saturation-værdier.

Bemærk, at dette er standardeffekterne, men de kan redigeres til at gøre næsten hvad som helst, du ønsker!

### Anvend på grupper

Du kan vælge, hvilke grupper der påvirkes af effekten. Højreklik, og slå gruppeafkrydsningsfelterne mærket _Apply to groups_ til eller fra.

Jeg bruger primært denne opsætning, når jeg arbejder med Canvas-grafik og laserstråler separat. Jeg tildeler alle Canvas-clips til gruppe 5 og udelukker derefter denne gruppe fra effekter, som jeg ikke vil have til at påvirke disse grafiske clips.

Du kan også bruge det til live at anvende 2 forskellige farveændringer på 2 grupper af lasere på én gang. Opret to farveændringseffekter, og vælg hvilke clip-grupper hver af dem skal anvendes på.

### MX group

Forkortelse for _Mutually Exclusive_. Dette er en måde at gruppere effekter på, så kun én effekt i gruppen kan være aktiv ad gangen. Læg mærke til, at kun én af standardeffekterne til farveskift kan være aktiv ad gangen. Det skyldes, at de alle er i MX Group 1.

Denne funktionalitet er deaktiveret, hvis _MX Group_-indstillingen er 0.

### Redigering af effekter

Højreklik på en effekt, og klik på knappen _EDIT EFFECT_ for at åbne effekt-editoren. Bemærk, at denne editor er identisk med Clip-editoren!

Rediger din effekt på samme måde, som du ville redigere et hvilket som helst clip. Se [Clip Editoren](clip-editor/ "mention").

Du skal have mindst én creator-node; det kan være hvad som helst (linje, cirkel, form, endda tekst!), men du bør nok vælge noget, der giver bedst mening i forhåndsvisningen på effektknappen.

Når effekter anvendes, erstattes alle creator-noder i effekten med outputtet fra de clips, der kører i øjeblikket.

{% hint style="warning" %}
Af ekstremt kedelige tekniske årsager er "trails"-noder ikke aktiveret inde i en effekt. Det samme gælder for "delay"-indstillingen inde i pattern-noder (de bruger det samme system). Dette bliver rettet i fremtidige revisioner.
{% endhint %}
