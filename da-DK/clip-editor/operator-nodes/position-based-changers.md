---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Positionsbaserede ændringer

Denne node-familie ændrer indhold ud fra position. Som standard anvendes effekten langs en vandret akse (fra venstre mod højre), men du kan rotere aksen til en hvilken som helst vinkel. Hver node har også en _radial_ mode, hvor effekten styres af vinklen for hvert punkt i forhold til centrum.

* **Colour Changer by Position** – forskyder farver hen over den valgte akse eller rundt om den radiale vinkel.\
  \&#xNAN;_Eksempel: Lav en regnbuegradient, der bevæger sig hen over en linje, eller brug radial mode på en cirkel for at skabe en farvehjul-effekt._
* **Wave Shift by Position** – anvender en sinusbølge-forvrængning, som forskyder indholdet lodret (eller vinkelret på den valgte akse).\
  \&#xNAN;_Eksempel: Få en linje til at bølge som vand, eller brug radial mode til at få en cirkel til at pulsere udad fra centrum._
* **Noise Shift by Position** – anvender en simplex noise-forvrængning, som forskyder indholdet lodret (eller vinkelret på den valgte akse).\
  \&#xNAN;_Eksempel: Se eksemplet for Wave Shift, men med et mere organisk og tilfældigt udtryk, perfekt til at tilføje naturlig variation._

## &#x20;Farveændring efter position

Denne node anvender farveændringer på dit indhold baseret på position. Som standard er aksen vandret (0°), men du kan rotere den eller skifte til radial mode.

* **wavelength** – angiver størrelsen på den gentagne farvecyklus.
  * _Linear mode:_ ved 100% spænder én fuld cyklus over hele indholdets bredde.
  * _Radial mode:_ ved 100% spænder én fuld cyklus over hele cirklen (360°). Værdierne er procenter af cirklen: f.eks. 50% = en halv cirkel (180°).
* **offset** – forskyder farvecyklussens startpunkt som en procentdel af wavelength. Du kan modulere dette (f.eks. med en sawtooth oscillator) for at cykle jævnt gennem farverne.
* **repeat** – når den er aktiveret, gentages cyklussen hen over indholdet. Hvis den er deaktiveret, anvendes gradienten kun én gang: Alt før starten får startfarven, og alt efter slutningen får slutfarven.
* **pingpong** – når den er aktiveret, skifter hver gentagelse retning, hvilket skaber en spejlet effekt. Hvis _Repeat_ er deaktiveret, går gradienten først frem og derefter tilbage én gang. _Bemærk: I Pingpong mode dækker wavelength både fremadgående og tilbagegående sweep._
* **linear angle** – roterer effektens akse. 0° = vandret.
* **radial** – skifter til radial mode, hvor farver anvendes ud fra vinklen fra centrum.
* **radial smooth loop** – justerer automatisk wavelength, så den går op i 100% af cirklen, hvilket forhindrer en synlig samling dér, hvor cyklussen looper.

**Farvetilstande**

Disse bestemmer, hvilke dele af farvejusteringerne der anvendes på indholdet. Se også: [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – hue ændres ikke.
  * _FIXED_ – hue tvinges til en fast værdi.
  * _SHIFTED_ – hue forskydes med den angivne mængde (elementer med forskellige farver forbliver adskilte, men forskydes samlet rundt på farvehjulet).
* **saturation mode**
  * _OFF_ – saturation ændres ikke.
  * _FIXED_ – saturation sættes til den angivne værdi.
* **brightness mode**
  * _OFF_ – brightness ændres ikke.
  * _FIXED_ – brightness sættes til den angivne værdi.
  * _MULTIPLY_ – brightness skaleres med den angivne værdi. Det bevarer dynamikken (f.eks. blinker blinkende elementer stadig, men inden for det begrænsede lysstyrkeområde).

**Start-/slutværdier**

Disse skydere definerer det farveområde, der anvendes hen over den valgte akse (eller det radiale sweep).

* **start hue** – hue ved gradientens begyndelse.
* **end hue** – hue ved gradientens slutning.
* **start saturation** – saturation ved begyndelsen.
* **end saturation** – saturation ved slutningen.
* **start brightness** – brightness ved begyndelsen.
* **end brightness** – brightness ved slutningen.
* **blend** – blander farveændringen med de oprindelige farver. Ved 100% erstatter effekten de oprindelige farver fuldt ud.

**Eksempel 1: Glidende regnbuegradient**

Med udgangspunkt i standardindstillingerne:

1. Lad noden være i **Linear** mode (0° vinkel = vandret).
2. Lad **wavelength** stå på 100% (spænder over hele bredden og bør være standard).
3. Lad start- og slutværdierne være som standard.
4. Aktivér **repeat**.
5. Tilføj en **Sawtooth Oscillator** til indstillingen **offset**, som går fra 0% til 100%.

***

**Eksempel 2: Sort-hvid-sort-gradient (Pingpong)**

Med udgangspunkt i standardindstillingerne:

1. Lad noden være i **Linear** mode (0° vinkel = vandret).
2. Lad **wavelength** stå på 100% (spænder over hele bredden og bør være standard).
3. Slå **repeat** fra.
4. Sæt **start brightness** til 0 (sort).
5. Sæt **end brightness** til 100 (hvid).
6. Sæt **start saturation** og **end saturation** til 0 (konverterer til gråtoner).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Aktivér **pingpong**.

_Resultat: Gradientens lysstyrke går fra sort til hvid og derefter tilbage til sort hen over bredden._\
Bemærk, at hvis indholdet skal bevare sin hue og saturation, skal du slå Saturation mode OFF. \\

***

**Eksempel 3: Roterende regnbuehjul (Radial)**

1. Aktivér **radial** mode.
2. Sæt **wavelength** til 100% (et fuldt 360° sweep).
3. Slå **repeat** til.
4. Tilføj en **Sawtooth Oscillator** til indstillingen **offset**, som går fra 0% til 100%.

_Resultat: Et sømløst farvehjul, der roterer kontinuerligt rundt om cirklen._

## &#x20;Wave shift efter position

Denne node anvender en bølgeforvrængning hen over dit indhold og forskyder punkter vinkelret på den valgte akse (eller radialt fra centrum).

* **Wavelength** – angiver længden på bølgecyklussen.
  * _Linear mode:_ ved 100% spænder én fuld cyklus over hele indholdets bredde.
  * _Radial mode:_ ved 100% spænder én fuld cyklus over hele 360°. (Værdierne er procenter af cirklen: 50% = en halv omgang, 25% = en kvart omgang osv.)
* **Size** – styrer bølgens amplitude (hvor langt indholdet forskydes).
* **Offset** – forskyder bølgen langs aksen (eller rundt om cirklen i radial mode). Dette er en procentdel af wavelength, så du kan animere den med en **Oscillator Node** for at få bølgen til at bevæge sig.
* **Radial** – skifter fra linear til radial mode, så forskydningen baseres på vinklen fra centrum.
* **Radial Smooth Loop** – justerer wavelength, så den går op i 100% af cirklen, hvilket forhindrer synlige samlinger ved loopet.
* **Triangle** – ændrer bølgeformen fra sinus til trekant.
* **Absolute** – tager bølgens absolutte værdi, så der kun opstår opadgående forskydninger (den negative side foldes over på den positive).
* **Angle** – roterer bølgens akse. 0° = vandret.

## &#x20;Noise shift efter position

Denne node forvrænger indhold ved hjælp af et noise-felt (som turbulens), hvor punkter forskydes vinkelret på den valgte akse (eller radialt fra centrum). Sammenlignet med _Wave Shift_ er resultatet mere organisk og tilfældigt.

* **Detail** – styrer, hvor fint noise er. Højere værdier = skarpere og mere detaljeret variation. Lavere værdier = blødere variation.
* **Wavelength** – angiver skalaen på noise-mønsteret.
  * _Linear mode:_ ved 100% spænder én fuld noise-cyklus over indholdets bredde.
  * _Radial mode:_ ved 100% spænder én fuld cyklus over hele 360°.
* **Size** – styrer forskydningsmængden (amplituden af noise-forvrængningen).
* **Offset** – forskyder noise-mønsteret langs aksen (eller rundt om cirklen). Dette er en procentdel af wavelength, så du kan animere den med en **Oscillator Node** for at få noise til at “flyde.”
* **Depth Offset** – bevæger sig gennem 3D noise-feltet og skaber variation over tid. Dette er især effektivt, når det animeres med en Oscillator Node.
* **Depth Detail** – styrer, hvor detaljeret variationen er på tværs af dybdedimensionen.
* **Absolute** – tager den absolutte værdi af noise og folder negative værdier over i positive (så der kun opstår ensidig forskydning).
* **Radial** – skifter fra linear til radial mode, så forskydningen baseres på vinklen fra centrum.
* **Radial Smooth Loop** – justerer wavelength, så den går op i 100% af cirklen, hvilket forhindrer synlige samlinger i radial mode.
