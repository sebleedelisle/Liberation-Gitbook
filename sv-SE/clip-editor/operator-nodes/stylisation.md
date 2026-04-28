---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stylisation-noder

## &#x20;Randomise

Skapar utspridda kopior av inkommande element med hjälp av ett sammanhängande brusfält. Med andra ord kopierar och flyttar den dina former och punkter på ett kontrollerat, ”brusigt” sätt. I stället för att allt ligger prydligt på ett ställe får du flera versioner som förskjuts och sprids ut, som partiklar som rör sig i ett flöde.

* **count** – antal kopior per inkommande element (1–20). Med 1 får du en enda jittrad version av varje element. Högre värden skapar flera utspridda kopior.
* **noise offset** – går igenom brusfältet cykliskt (0–100%). Det loopar sömlöst, så om du animerar detta med en Oscillator Node får du en mjuk, kontinuerlig rörelse för alla kopior tillsammans.
* **noise jitter** – styr texturskalan för bruset. Lägre värden ger bred, mjuk variation. Högre värden ger tätare och mer oberäknelig placering. Detta ändrar mönstret, inte styrkan.
* **change between points** – styr hur mycket varje kopia skiljer sig från den föregående. Låga värden håller kopiorna samlade och lika. Höga värden sprider ut dem med större variation.
* **face direction** – roterar varje kopia så att den pekar i rörelseriktningen i brusfältet, vilket ger pilar/partiklar som följer flödet.
* **amount** – effektens totala styrka (0–100%). Skalar både förskjutningen och rotationen från Face direction.

{% hint style="info" %}
Randomise-noden är själva kärnan i Randomise-effekten!
{% endhint %}

## &#x20;Trails

Skapar ekon av ditt innehåll, med kopior som tonar ut eller skalas bakom originalet när det rör sig.

* **change render profile for trail** – om detta är på använder alla trail-kopior vald **render profile**. _Se_ [render-profile.md](../fundamentals/render-profile.md "mention").
* **render profile** – profilen som används för trail-kopior när växeln ovan är på. Används ofta när huvudinnehållet är inställt på **DETAIL** men ekona renderas som **FAST**, vilket ger tydliga detaljer i huvudformerna samtidigt som trails renderas mer effektivt.
* **delay** – anger avståndet mellan trail-kopior i musikalisk tid, mätt i **1/64-notsteg**.\
  Som referens:
  * 16 = 1/16 takt (sextondel)
  * 32 = 1/8 takt (åttondel)
  * 64 = 1/4 takt (fjärdedel)
  * 128 = 1/2 takt (halvnot)
  * 256 = 1 takt
* **trail size** – hur många trail-kopior som ritas bakom det aktiva innehållet.
* **freeze trails** – gör mjukt flytande trails till en sekvens av frysta ögonblicksbilder. Praktiskt för att skapa staccato-liknande, beat-synkade trail-effekter.
* **brightness start / brightness end** – applicerar ljusstyrka över trailen från den nyaste kopian (**start**) till den äldsta kopian (**end**). Vanligtvis ställer du **brightness start** på 100% och **brightness end** på 0% så tonar ekona ut.
* **scale start / scale end** – applicerar skalning över trailen från den nyaste kopian (start) till den äldsta kopian (end). För trails som krymper till ingenting ställer du **scale start** på 100% och **scale end** på 0%.

## &#x20;Shimmer

Lägger till en glittrande variation i ljusstyrka i ditt innehåll, från diskret skimmer till intensiv strobning.

* **speed** – hur snabbt shimmer ändras över tid. Högre värden flimrar snabbare; 0 pausar effekten.
* **separation** – hur mycket närliggande punkter/element skiljer sig från varandra.
  * 0: allt skimrar tillsammans.
  * \>0: närliggande punkter får gradvis olika faser, så skimret varierar över formen.
  * <0: samma som ovan, men fasförskjutningen går åt motsatt håll.
* **threshold** – i stället för att tona mjukt blinkar punkter nu helt på eller av beroende på sin ljusstyrka. Ljusare element tänds oftare, men tänk på att element med 100% ljusstyrka alltid är på, medan element med 0% ljusstyrka alltid är av. Användbart för skarpa glitter- eller stjärnljuseffekter.

{% hint style="info" %}
Att slå på **threshold** är en av de där riktigt bra dolda funktionerna som verkligen kan ge liv åt dina partiklar eller ditt innehåll. I stället för att tona växlas punkter snabbt på och av baserat på sin ljusstyrka. Eftersom färre punkter ritas vid varje givet ögonblick blir resultatet ljusare output och mjukare animation.

Men kom ihåg att om ditt innehåll redan har 100% ljusstyrka händer ingenting!
{% endhint %}

* **use whole shape** – applicerar ett enda shimmer-värde jämnt över hela formen. När detta är av delar noden upp former så att olika delar kan glittra oberoende av varandra, för ett spräckligt utseende.

## &#x20;Particles

Detta är en experimentell effekt som skapar och animerar partiklar baserat på ditt innehåll. Alla punktbaserade element som går in behandlas som emitterpositioner. Eftersom partikelbanor förberäknas kan du behöva uppdatera/beräkna om partiklarna om ditt indatainnehåll ändras (ändra bara någon av inställningarna)

**General**

* **keep original** – om detta är på behålls originalinnehållet och partiklar läggs ovanpå. Praktiskt när du vill att emitterpunkterna ska fortsätta vara synliga.
* **number of particles** – hur många partiklar som skapas per emission. Högre värden ger tätare effekter, lägre värden ger ett mer minimalistiskt resultat.
* **emission period** – loopens spann (i takter) under vilket partiklar emitteras. Vid 100% sprids de jämnt över loopen; mindre värden samlar dem tätare för burst-effekter.
* **loop length** – hur länge partikelloopen varar, mätt i musikaliska takter.
* **loop count** – hur många gånger loopen upprepas innan den återställs. Om detta är inställt på 1 följer partiklarna alltid exakt samma simulering varje gång, vilket gör den helt repeterbar. Högre värden introducerar mer variation innan cykeln återställs.
* **delay** – förskjuter emissionens starttid med ett antal 1/64-noter, för timingeffekter.

**Motion**

* **speed** – hur snabbt partiklarna rör sig bort från emittern.
* **speed variation** – lägger till slumpmässighet så att partiklarna inte alla rör sig med samma hastighet. Skapar en mer naturlig spridning.
* **direction** – anger grundriktningen som partiklarna skjuts i, definierad av **x, y, z angles**. Dessa vinklar roterar skjutvektorn i 3D-rymden, så att du kan rikta partiklarna rakt upp, åt sidan eller diagonalt. Kombinera med **spread** för bredare koner eller mer kaotiska bursts.

{% hint style="info" %}
**Euler angles**\
Liberation använder **Euler angles** för att beskriva orientering i 3D-rymden. Det är helt enkelt rotationer runt de tre huvudaxlarna:

* **X** – luta framåt/bakåt (som när du nickar)
* **Y** – vrid vänster/höger (som när du skakar på huvudet för ”nej”)
* **Z** – rulla medurs/moturs (som när du lutar huvudet åt sidan)

Genom att justera dessa tre värden kan du rikta partiklar åt vilket håll som helst.
{% endhint %}

* **direction variation** – lägger till slumpmässig spridning runt den riktningen. Användbart för att skapa koner, sprayer eller explosioner.
* **drag** – saktar ner partiklar över tid. Högre värden gör att de känns tyngre och trögare.
* **gravity** – drar partiklar nedåt (positivt) eller trycker dem uppåt (negativt).
* **gravity variation** – lägger till variation i gravitation per partikel, vilket gör rörelsen mer kaotisk.

**Life**

* **life duration** – hur länge partiklar existerar (mätt i 1/64-notenheter). Med kortare värden försvinner partiklar snabbt, medan längre värden gör att de förblir synliga under längre tid.
* **life variation** – lägger till slumpmässighet i partiklarnas livslängd så att de inte alla försvinner samtidigt.
* **start delay / start delay variation** – fördröjer när varje partikel blir synlig (i 1/64-notsteg). Partikeln har redan skapats och rör sig under den här perioden, men dess ljusstyrka hålls på 0, så den förblir osynlig tills fördröjningen har passerat. Det är användbart om du vill att fördröjda fyrverkeri-”gnistor” ska dyka upp.

**Colour & brightness**

* **hue start** – partiklarnas ursprungliga färg.
* **hue variation** – lägger till slumpmässighet så att partiklarna inte alla börjar med samma färg.
* **hue change** – skiftar nyansen över partikelns livslängd och skapar färgskiftande trails.
* **brightness start / brightness end** – applicerar ljusstyrka över partikelns livslängd. Vanligtvis ställer du brightness start högt och brightness end lågt så att de tonar ut naturligt.
* **brightness variation** – slumpvarierar startljusstyrkan för ett mer dynamiskt utseende.
* **saturation start / saturation end** – anger hur intensiv färgen är i början och slutet.
* **saturation variation** – slumpvarierar mättnaden för variation mellan partiklar.

**Simulation**

* **time adjustment** – snabbar upp eller saktar ner hela partikelsimuleringen. Användbart för att synka till olika tempon eller förstärka rörelse.
