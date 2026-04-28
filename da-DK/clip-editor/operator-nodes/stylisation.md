---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stylisation-noder

## &#x20;Randomise

Opretter spredte kopier af de indkommende elementer ved hjælp af et sammenhængende støjfelt. Med andre ord kopierer og flytter den dine former og punkter rundt på en kontrolleret, “støjende” måde. I stedet for at alt ligger pænt samlet ét sted, får du flere versioner, der forskyder sig og spreder sig ud, som partikler der bevæger sig i et flow.

* **count** – antal kopier pr. indkommende element (1–20). Med 1 får du én jitter-forskudt version af hvert element. Højere værdier opretter flere spredte kopier.
* **noise offset** – bevæger sig gennem støjfeltet (0–100%). Det looper sømløst, så hvis du animerer dette med en Oscillator Node, får du en jævn, kontinuerlig bevægelse af alle kopier samlet.
* **noise jitter** – styrer støjens teksturskala. Lavere værdier giver brede, bløde variationer. Højere værdier giver tættere og mere uregelmæssig placering. Dette ændrer mønsteret, ikke styrken.
* **change between points** – styrer hvor forskellig hver kopi er fra den forrige. Lave værdier holder kopierne samlet og ensartede. Høje værdier spreder dem mere ud med større variation.
* **face direction** – roterer hver kopi, så den vender i bevægelsesretningen i støjfeltet, hvilket giver pile/partikler, der følger flowet.
* **amount** – effektens samlede styrke (0–100%). Skalerer både forskydningen og rotationen fra Face direction.

{% hint style="info" %}
Randomise-noden er kernen i Randomise-effekten!
{% endhint %}

## &#x20;Trails

Opretter ekkoer af dit indhold, så der efterlades kopier bag originalen, som fader ud eller skaleres, mens den bevæger sig.

* **change render profile for trail** – hvis slået til, bruger alle trail-kopier den valgte **render profile**. _Se_ [render-profile.md](../fundamentals/render-profile.md "mention").
* **render profile** – profilen, der bruges til trail-kopier, når kontakten ovenfor er slået til. Bruges ofte, når hovedindholdet er sat til **DETAIL**, men ekkoerne renderes som **FAST**. Det giver tydelige detaljer på hovedformerne, mens trails renderes mere effektivt.
* **delay** – angiver afstanden mellem trail-kopier i musikalsk tid, målt i **1/64-node-trin**.\
  Som reference:
  * 16 = 1/16 takt (sekstendedelsnode)
  * 32 = 1/8 takt (ottendedelsnode)
  * 64 = 1/4 takt (fjerdedelsnode)
  * 128 = 1/2 takt (halvnode)
  * 256 = 1 takt
* **trail size** – hvor mange trail-kopier der tegnes bag det live indhold.
* **freeze trails** – omdanner jævnt flydende trails til en sekvens af frosne snapshots. Nyttigt til at skabe staccatoagtige, beat-synkroniserede trail-effekter.
* **brightness start / brightness end** – anvender lysstyrke hen over trailen fra den nyeste kopi (**start**) til den ældste kopi (**end**). Typisk sættes **brightness start** til 100% og **brightness end** til 0%, så ekkoerne fader ud.
* **scale start / scale end** – anvender skalering hen over trailen fra den nyeste kopi (start) til den ældste kopi (end). For trails, der skrumper helt væk, skal du sætte **scale start** til 100% og **scale end** til 0%.

## &#x20;Shimmer

Tilføjer en funklende variation i lysstyrke til dit indhold, fra diskret glimt til kraftig strobing.

* **speed** – hvor hurtigt shimmer ændrer sig over tid. Højere værdier flimrer hurtigere; 0 sætter effekten på pause.
* **separation** – hvor forskellige nabopunkter/-elementer er fra hinanden.
  * 0: alt shimmer samlet.
  * \>0: nærliggende punkter får gradvist forskellige faser, så shimmer varierer hen over formen.
  * <0: det samme som ovenfor, men faseforløbet går den modsatte vej.
* **threshold** – i stedet for at fade jævnt blinker punkterne nu enten helt til eller helt fra afhængigt af deres lysstyrke. Lysere elementer lyser op oftere, men bemærk, at elementer ved 100% lysstyrke altid er tændt, mens elementer ved 0% lysstyrke altid er slukket. Nyttigt til skarpe glitter- eller stjernelyseffekter.

{% hint style="info" %}
At slå **threshold** til er en af de gode skjulte funktioner, der virkelig kan give dine partikler eller dit indhold liv. I stedet for at fade bliver punkterne hurtigt slået til og fra baseret på deres lysstyrke. Fordi der tegnes færre punkter på et givent tidspunkt, giver det et kraftigere output og en mere jævn animation.

Men husk, at hvis dit indhold allerede er ved 100% lysstyrke, sker der ingenting!
{% endhint %}

* **use whole shape** – anvender én shimmer-værdi ensartet på hele formen. Når den er slået fra, opdeler noden former, så forskellige dele kan glimte uafhængigt for et plettet udtryk.

## &#x20;Particles

Dette er en eksperimentel effekt, der genererer og animerer partikler baseret på dit indhold. Alle punktbaserede elementer, der går ind, behandles som emitter-positioner. Fordi partikelbaner forudberegnes, kan du være nødt til at opdatere/genberegne partiklerne, hvis dit inputindhold ændrer sig (du skal blot ændre en af indstillingerne).

**General**

* **keep original** – hvis slået til, bevares det oprindelige indhold, og partikler tilføjes ovenpå. Nyttigt når du vil have emitter-punkterne til at forblive synlige.
* **number of particles** – hvor mange partikler der oprettes pr. emission. Højere værdier giver tættere effekter, lavere værdier giver et mere minimalt udtryk.
* **emission period** – loopets spændvidde (i takter), som partiklerne udsendes over. Ved 100% fordeles de jævnt over loopet; mindre værdier samler dem i bursts.
* **loop length** – hvor længe partikelloopet varer, målt i musikalske takter.
* **loop count** – hvor mange gange loopet gentages, før det nulstilles. Hvis den er sat til 1, følger partiklerne altid præcis den samme simulation hver gang, så den kan gentages perfekt. Højere værdier giver mere variation, før cyklussen nulstilles.
* **delay** – forskyder emissionens starttid med et antal 1/64-noder for timing-effekter.

**Motion**

* **speed** – hvor hurtigt partiklerne bevæger sig væk fra emitteren.
* **speed variation** – tilføjer tilfældighed, så partiklerne ikke alle bevæger sig med samme hastighed. Skaber en mere naturlig spredning.
* **direction** – angiver basisretningen, som partikler affyres i, defineret af **x, y, z angles**. Disse vinkler roterer affyringsvektoren i 3D-rum, så du kan sigte partiklerne lige op, sidelæns eller i en diagonal retning. Kombinér med **spread** for bredere kegler eller mere kaotiske bursts.

{% hint style="info" %}
**Euler angles**\
Liberation bruger **Euler angles** til at beskrive orientering i 3D-rum. Det er ganske enkelt rotationer omkring de tre hovedakser:

* **X** – vip frem/tilbage (som når du nikker)
* **Y** – drej venstre/højre (som når du ryster på hovedet “nej”)
* **Z** – rul med/mod uret (som når du lægger hovedet på skrå)

Ved at justere disse tre værdier kan du pege partikler i enhver retning.
{% endhint %}

* **direction variation** – tilføjer tilfældig spredning omkring den retning. Nyttigt til at skabe kegler, sprays eller eksplosioner.
* **drag** – sænker partiklernes hastighed over tid. Højere værdier får dem til at føles tungere og mere træge.
* **gravity** – trækker partikler ned (positiv) eller skubber dem op (negativ).
* **gravity variation** – tilføjer variation i tyngdekraften pr. partikel, hvilket gør bevægelsen mere kaotisk.

**Life**

* **life duration** – hvor længe partikler eksisterer (målt i 1/64-node-enheder). Med kortere værdier forsvinder partikler hurtigt, mens de ved længere værdier forbliver synlige i længere tid.
* **life variation** – tilføjer tilfældighed til partiklernes levetid, så de ikke alle forsvinder på samme tid.
* **start delay / start delay variation** – forsinker, hvornår hver partikel bliver synlig (i 1/64-node-trin). Partiklen er allerede genereret og i bevægelse i denne periode, men dens lysstyrke holdes på 0, så den forbliver usynlig, indtil forsinkelsen er gået. Det er nyttigt, hvis du vil have forsinkede fyrværkeri-"glimt" til at dukke op.

**Colour & brightness**

* **hue start** – partiklernes startfarve.
* **hue variation** – tilføjer tilfældighed, så partiklerne ikke alle starter med samme farve.
* **hue change** – forskyder hue gennem partiklens levetid og skaber farveskiftende trails.
* **brightness start / brightness end** – anvender lysstyrke gennem partiklens levetid. Sæt typisk brightness start højt og brightness end lavt, så de fader naturligt ud.
* **brightness variation** – randomiserer startlysstyrken for et mere dynamisk udtryk.
* **saturation start / saturation end** – angiver hvor kraftig farven er i starten og slutningen.
* **saturation variation** – randomiserer mætningen for variation mellem partikler.

**Simulation**

* **time adjustment** – øger eller sænker hastigheden for hele partikelsimulationen. Nyttigt til at synkronisere til forskellige tempi eller overdrive bevægelse.
