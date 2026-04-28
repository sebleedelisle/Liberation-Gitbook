---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Positionsbaserade ändrare

Den här familjen av noder ändrar innehåll utifrån position. Som standard appliceras effekten längs en horisontell axel (från vänster till höger), men du kan rotera axeln till valfri vinkel. Varje nod har också ett _radial_-läge, där effekten styrs av vinkeln för varje punkt i förhållande till centrum.

* **Colour Changer by Position** – skiftar färger längs den valda axeln eller runt den radiella vinkeln.\
  \&#xNAN;_Exempel: Skapa en regnbågsgradient som sveper över en linje, eller använd radial-läge på en cirkel för att skapa en färghjul-effekt._
* **Wave Shift by Position** – applicerar en sinusvågsdistorsion och förskjuter innehållet vertikalt (eller vinkelrätt mot den valda axeln).\
  \&#xNAN;_Exempel: Få en linje att bölja som vatten, eller använd radial-läge för att få en cirkel att pulsera utåt från centrum._
* **Noise Shift by Position** – applicerar simplexbrusdistorsion och förskjuter innehållet vertikalt (eller vinkelrätt mot den valda axeln).\
  \&#xNAN;_Exempel: se exemplet för Wave Shift, men med en mer organisk och slumpmässig karaktär, perfekt för att lägga till naturlig variation._

## &#x20;Färgändring efter position

Den här noden applicerar färgändringar över ditt innehåll baserat på position. Som standard är axeln horisontell (0°), men du kan rotera den eller växla till radial-läge.

* **wavelength** – anger storleken på den upprepande färgcykeln.
  * _Linear mode:_ vid 100% sträcker sig en hel cykel över innehållets fulla bredd.
  * _Radial mode:_ vid 100% sträcker sig en hel cykel runt hela cirkeln (360°). Värdena är procent av cirkeln: t.ex. 50% = en halv cirkel (180°).
* **offset** – flyttar färgcykelns startpunkt, som en procentandel av våglängden. Du kan modulera detta (t.ex. med en sawtooth oscillator) för att cykla jämnt genom färgerna.
* **repeat** – när detta är aktiverat upprepas cykeln över innehållet. Om det är avstängt appliceras gradienten bara en gång: allt före starten får startfärgen och allt efter slutet får slutfärgen.
* **pingpong** – när detta är aktiverat växlar varje upprepning riktning och skapar en speglad effekt. Om _Repeat_ är avstängt går gradienten först framåt och sedan tillbaka en gång. _Obs: i Pingpong-läge täcker wavelength både framåt- och retursvepet._
* **linear angle** – roterar effektens axel. 0° = horisontellt.
* **radial** – växlar till radial-läge och applicerar färger baserat på vinkeln från centrum.
* **radial smooth loop** – justerar automatiskt wavelength så att den delar upp 100% av cirkeln jämnt, vilket förhindrar en synlig skarv där cykeln går runt.

**Colour Modes**

Dessa avgör vilka delar av färgjusteringarna som appliceras på innehållet. Se även: [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – hue ändras inte.
  * _FIXED_ – hue tvingas till ett fast värde.
  * _SHIFTED_ – hue förskjuts med det angivna värdet (element med olika färger förblir åtskilda, men flyttas tillsammans runt färghjulet).
* **saturation mode**
  * _OFF_ – saturation ändras inte.
  * _FIXED_ – saturation sätts till det angivna värdet.
* **brightness mode**
  * _OFF_ – brightness ändras inte.
  * _FIXED_ – brightness sätts till det angivna värdet.
  * _MULTIPLY_ – brightness skalas med det angivna värdet. Detta bevarar dynamiken (t.ex. blinkande element fortsätter att blinka, men inom det begränsade brightness-området).

**Start / End Values**

Dessa reglage definierar färgområdet som appliceras längs den valda axeln (eller det radiella svepet).

* **start hue** – hue i början av gradienten.
* **end hue** – hue i slutet av gradienten.
* **start saturation** – saturation i början.
* **end saturation** – saturation i slutet.
* **start brightness** – brightness i början.
* **end brightness** – brightness i slutet.
* **blend** – blandar färgändringen med originalfärgerna. Vid 100% ersätter effekten originalfärgerna helt.

**Exempel 1: Glidande regnbågsgradient**

Utgå från standardinställningarna :

1. Lämna noden i **Linear**-läge (0° angle = horisontellt).
2. Lämna **wavelength** på 100% (sträcker sig över hela bredden och bör vara standardvärdet).
3. Lämna start- och slutvärdena som standard.
4. Aktivera **repeat**.
5. Lägg till en **Sawtooth Oscillator** på inställningen **offset** som går från 0% till 100%.

***

**Exempel 2: Svart–vit–svart-gradient (Pingpong)**

Utgå från standardinställningarna :

1. Lämna noden i **Linear**-läge (0° angle = horisontellt).
2. Lämna **wavelength** på 100% (sträcker sig över hela bredden och bör vara standardvärdet).
3. Stäng av **repeat**.
4. Sätt **start brightness** till 0 (svart).
5. Sätt **end brightness** till 100 (vitt).
6. Sätt **start saturation** och **end saturation** till 0 (konverterar till gråskala).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Aktivera **pingpong**.

_Resultat: gradienten tonar från svart till vitt och sedan tillbaka till svart över bredden._\
Observera att om du vill att innehållet ska behålla sin hue och saturation ska du stänga av Saturation mode. \\

***

**Exempel 3: Roterande regnbågshjul (Radial)**

1. Aktivera **radial**-läge.
2. Sätt **wavelength** till 100% (ett helt 360°-svep).
3. Slå på **repeat**.
4. Lägg till en **Sawtooth Oscillator** på inställningen **offset** som går från 0% till 100%.

_Resultat: ett sömlöst färghjul som roterar kontinuerligt runt cirkeln._

## &#x20;Vågförskjutning efter position

Den här noden applicerar en vågdistorsion över ditt innehåll och förskjuter punkter vinkelrätt mot den valda axeln (eller radiellt från centrum).

* **Wavelength** – anger längden på vågcykeln.
  * _Linear mode:_ vid 100% sträcker sig en hel cykel över innehållets fulla bredd.
  * _Radial mode:_ vid 100% sträcker sig en hel cykel över hela 360°. (Värdena är procent av cirkeln: 50% = ett halvt varv, 25% = ett kvarts varv osv.)
* **Size** – styr vågens amplitud (hur långt innehållet förskjuts).
* **Offset** – flyttar vågen längs axeln (eller runt cirkeln i radial-läge). Detta är en procentandel av wavelength, så du kan animera det med en **Oscillator Node** för att få vågen att röra sig.
* **Radial** – växlar från linear till radial-läge, så att förskjutningen baseras på vinkeln från centrum.
* **Radial Smooth Loop** – justerar wavelength så att den delar upp 100% av cirkeln jämnt, vilket förhindrar synliga skarvar vid övergången.
* **Triangle** – ändrar vågformen från sinus till triangel.
* **Absolute** – tar vågens absolutvärde och skapar endast uppåtriktade förskjutningar (viker den negativa sidan över den positiva).
* **Angle** – roterar vågens axel. 0° = horisontellt.

## &#x20;Brusförskjutning efter position

Den här noden förvränger innehåll med ett brusfält (som turbulens) och förskjuter punkter vinkelrätt mot den valda axeln (eller radiellt från centrum). Jämfört med _Wave Shift_ blir resultatet mer organiskt och slumpmässigt.

* **Detail** – styr hur fint bruset är. Högre värden = skarpare och mer detaljerad variation. Lägre värden = mjukare variation.
* **Wavelength** – anger skalan för brusmönstret.
  * _Linear mode:_ vid 100% sträcker sig en hel bruscykel över innehållets bredd.
  * _Radial mode:_ vid 100% sträcker sig en hel cykel över hela 360°.
* **Size** – styr förskjutningens storlek (amplituden för brusdistorsionen).
* **Offset** – flyttar brusmönstret längs axeln (eller runt cirkeln). Detta är en procentandel av wavelength, så du kan animera det med en **Oscillator Node** för att få bruset att “flöda.”
* **Depth Offset** – förflyttar sig genom 3D-brusfältet och skapar variation över tid. Detta är särskilt effektivt när det animeras med en Oscillator Node.
* **Depth Detail** – styr hur detaljerad variationen är längs djupdimensionen.
* **Absolute** – tar brusets absolutvärde och viker negativa värden till positiva (vilket ger endast ensidig förskjutning).
* **Radial** – växlar från linear till radial-läge, så att förskjutningen baseras på vinkeln från centrum.
* **Radial Smooth Loop** – justerar wavelength så att den delar upp 100% av cirkeln jämnt, vilket förhindrar synliga skarvar i radial-läge.
