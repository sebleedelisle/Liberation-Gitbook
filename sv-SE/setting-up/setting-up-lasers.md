---
description: >-
  Lasrar kan vara farliga, så det är viktigt att följa bästa praxis och
  säkerhetsriktlinjer. Den här sidan ger en praktisk översikt som hjälper dig
  genom processen att konfigurera lasrar på ett säkert sätt.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/setting-up-lasers
---

# ✅ Översikt över hur du konfigurerar lasrar

### Översikt över processen för att slå på lasrar säkert

Den här manualen ersätter inte formell utbildning i lasersäkerhet, vilket du definitivt behöver innan du använder lasrar offentligt. Vissa områden har ytterligare lagkrav, men oavsett detta ska du alltid följa bästa praxis för säkerhet och arbeta professionellt.

PLASA har en kostnadsfri lasersäkerhetsguide som kan laddas ned och som allmänt har accepterats som bästa praxis: [https://www.plasa.org/guidance-for-display-lasers/](https://www.plasa.org/guidance-for-display-lasers/)

Se till att du förstår säkerhetsriskerna med lasrar innan du använder dem!

#### Introduktion

Den här sidan är avsedd att ge dig en översikt över processen för att starta lasrar på ett säkert sätt. Exakt hur du utför varje steg beskrivs längre fram i det här avsnittet, men den här sidan hjälper dig att förstå helheten. Du kan också återkomma hit som referens varje gång du konfigurerar lasrar.

<figure><img src="../.gitbook/assets/laser-aperture.jpg" alt=""><figcaption><p>En typisk lucka över laseröppningen</p></figcaption></figure>

### Konfigurera hårdvaran:

1. **Stäng aperturluckan** på lasern
2. **Rigga lasern säkert** och rikta den åt rätt håll
3. **Anslut stoppknappen** till lasern
4. **Anslut laser controller** till datorn
5. **Slå på strömmen** till lasern

### Konfigurera Liberation:

1. **Sätt alla lasrar i läget disarmed** och hitta och anslut controller i Liberation
2. **Sänk inställningen&#x20;**_**Global Brightness**_**&#x20;till 0** (använd reglaget i ikonraden eller _Master Fader_ på APC40)
3. **Sätt lasern i läget armed** – med aperturluckan fortfarande stängd, kontrollera att inga Clips är aktiva och sätt lasern i läget armed (använd knappen _Arm_ i panelen _Laser Overview_)
4. **Slå på test pattern** (använd knappen ☒ i ikonraden, välj mönster 1: den gröna kvadraten med ett kryss genom)
5. **Justera Output zone** – gör en uppskattning av den säkraste storleken och positionen för zone (till exempel kan den ligga högt upp mot taket, men det beror på din specifika miljö)
6. **Kontrollera att lasern fungerar** – höj ljusstyrkan långsamt tills du kan se ljus bakom aperturfönstret. Sänk sedan ljusstyrkan tillbaka till noll.
7. **Testa stoppknappen** för att säkerställa att all laserutgång släcks när den trycks in

### Starta laserutgång

1. **Utrym exponeringsområdet** – se till att ingen kan exponeras för lasern och informera all personal om att de ska hålla sig utanför exponeringsområdet medan lasrarna konfigureras. (Du bör också se till att kameror och projektorer är täckta eller har linsskydden på!)
2. **Öppna aperturluckan** – stå vid sidan av och utanför output, och skjut ned aperturluckan. Om dina zones är högt placerade kan du vilja lämna den delvis stängd.
3. **Höj ljusstyrkan tills lasern knappt syns** – gör lasern bara så ljus som behövs för att se zone
4. **Justera zone eller zones** – ställ in storlek, form och position för zone så att den ligger 3 m över golvet från alla offentligt tillgängliga områden, och så att lasern inte når några andra offentligt tillgängliga områden
5. **Lägg till fysisk maskning** – använd aperturluckan och/eller svart folietejp för att fysiskt maska allt utanför önskad zone. Detta är kritiskt viktigt eftersom både laserhårdvara och mjukvara kan fallera.
6. **Lägg till masks i programvaran** – masks i Liberation kan användas för att skydda kameror och projektorer, men ska **aldrig** användas i stället för fysisk maskning för att skydda människor. Observera att ingen mjukvara eller hårdvara är ofelbar, så se till att du förstår riskerna innan du använder masks i programvaran.

{% hint style="warning" %}
Observera att den här guiden förutsätter en installation inomhus. Om du arbetar utomhus måste ytterligare steg vidtas för att säkerställa flygsäkerheten, inklusive men inte begränsat till:

* Skaffa nödvändiga tillstånd från luftfartsmyndigheter som FAA eller CAA
* Samordna med närliggande flygplatser och flygfält
* Kontrollera offentlig flygradar och även utse en observatör som håller uppsikt efter flygplan

Även lasrar som ligger långt under säkerhetsgränsen kan orsaka katastrofala distraktioner för piloter.

Se till att du har nödvändiga kvalifikationer, licenser och tillstånd innan du riktar någon laser upp i luftrummet.
{% endhint %}
