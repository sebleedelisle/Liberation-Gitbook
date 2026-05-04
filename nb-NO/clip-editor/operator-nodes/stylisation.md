---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stylisation-noder

## &#x20;Randomise

Lager spredte kopier av de innkommende elementene ved hjelp av et sammenhengende støyfelt. Med andre ord kopierer og flytter den former og punkter på en kontrollert, «støyende» måte. I stedet for at alt ligger pent på ett sted, får du flere versjoner som forskyves og sprer seg, som partikler som beveger seg i en strøm.

* **count** – antall kopier per innkommende element (1–20). Med 1 får du én enkelt forskjøvet versjon av hvert element. Høyere verdier lager flere spredte kopier.
* **noise offset** – går gjennom støyfeltet (0–100 %). Den looper sømløst, så hvis du animerer dette med en Oscillator Node, får du jevn, kontinuerlig bevegelse av alle kopiene samlet.
* **noise jitter** – styrer teksturskalaen i støyen. Lavere verdier gir brede, myke variasjoner. Høyere verdier gir tettere og mer uforutsigbar plassering. Dette endrer mønsteret, ikke styrken.
* **change between points** – styrer hvor forskjellig hver kopi er fra den forrige. Lave verdier holder kopiene samlet og like. Høye verdier sprer dem mer og gir større variasjon.
* **face direction** – roterer hver kopi slik at den vender i bevegelsesretningen i støyfeltet, noe som gir piler/partikler som følger strømmen.
* **amount** – samlet styrke på effekten (0–100 %). Skalerer både forskyvningen og rotasjonen fra Face direction.

{% hint style="info" %}
Randomise-noden er kjernen i Randomise-effekten!
{% endhint %}

## &#x20;Trails

Lager ekkoer av innholdet ditt, med kopier som toner ut eller skaleres bak originalen mens den beveger seg.

* **change render profile for trail** – hvis på, bruker alle trail-kopier valgt **render profile**. _Se_ [Render profile](../fundamentals/render-profile.md "mention").
* **render profile** – profilen som brukes for trail-kopier når bryteren over er på. Brukes ofte når hovedinnholdet er satt til **DETAIL**, mens ekkoene rendres som **FAST**. Da får du tydelige detaljer i hovedformene, samtidig som trails rendres mer effektivt.
* **delay** – angir avstanden mellom trail-kopier i musikalsk tid, målt i **1/64-note-trinn**.\
  Til referanse:
  * 16 = 1/16 takt (sekstendedelsnote)
  * 32 = 1/8 takt (åttendedelsnote)
  * 64 = 1/4 takt (fjerdedelsnote)
  * 128 = 1/2 takt (halvnote)
  * 256 = 1 takt
* **trail size** – hvor mange trail-kopier som tegnes bak det aktive innholdet.
* **prefill trails** – fyller sporhistorikken med én gang når Clip starter, i stedet for å vente på at ekkoene bygges opp over de første taktene.
* **freeze trails** – gjør jevnt flytende trails om til en serie frosne øyeblikksbilder. Nyttig for å lage stakkato, taktsynkroniserte trail-effekter.
* **brightness start / brightness end** – legger lysstyrke over trailen fra den nyeste kopien (**start**) til den eldste kopien (**end**). Vanligvis setter du **brightness start** til 100 % og **brightness end** til 0 %, slik at ekkoene toner ut.
* **scale start / scale end** – legger skalering over trailen fra den nyeste kopien (start) til den eldste kopien (end). For trails som krymper helt bort, setter du **scale start** til 100 % og **scale end** til 0 %.

## &#x20;Shimmer

Legger til en blinkende variasjon i lysstyrken på innholdet ditt, fra forsiktig glitring til intens strobing.

* **speed** – hvor raskt shimmer endrer seg over tid. Høyere verdier blinker raskere; 0 pauser effekten.
* **separation** – hvor forskjellige nabopunkter/-elementer er fra hverandre.
  * 0: alt skimrer sammen.
  * \>0: nærliggende punkter får gradvis forskjellige faser, slik at shimmer varierer over formen.
  * <0: samme som over, men faseprogresjonen går motsatt vei.
* **threshold** – i stedet for å tone jevnt, blinker punktene nå helt på eller av avhengig av lysstyrken. Lysere elementer lyser opp oftere, men merk at elementer med 100 % lysstyrke alltid er på, mens elementer med 0 % lysstyrke alltid er av. Nyttig for skarpe glitter- eller stjernelyseffekter.

{% hint style="info" %}
Å slå på **threshold** er en av de gode skjulte funksjonene som virkelig kan gi liv til partiklene eller innholdet ditt. I stedet for å tone ut og inn, slås punktene raskt av og på basert på lysstyrken. Fordi færre punkter tegnes til enhver tid, blir resultatet lysere output og jevnere animasjon.

Men husk at hvis innholdet ditt allerede har 100 % lysstyrke, vil det ikke gjøre noe!
{% endhint %}

* **use whole shape** – bruker én shimmer-verdi jevnt på hele formen. Når den er av, deler noden opp formene slik at ulike deler kan glitre uavhengig for et prikkete uttrykk.

## &#x20;Particles

Dette er en eksperimentell effekt som genererer og animerer partikler basert på innholdet ditt. Alle punktbaserte elementer som går inn, behandles som emitterposisjoner. Siden partikkelbaner forhåndsberegnes, kan det hende du må oppdatere/beregne på nytt hvis input-innholdet endres, for å oppdatere partiklene (bare endre en av innstillingene).

**General**

* **keep original** – hvis på, beholdes det opprinnelige innholdet, og partiklene legges oppå. Nyttig når du vil at emitterpunktene fortsatt skal være synlige.
* **number of particles** – hvor mange partikler som opprettes per utslipp. Høyere verdier gir tettere effekter, lavere verdier gir et mer minimalt uttrykk.
* **emission period** – lengden på loopen (i takter) som partiklene sendes ut over. Ved 100 % spres de jevnt utover loopen; mindre verdier samler dem tettere for utbrudd.
* **loop length** – hvor lenge partikkelloopen varer, målt i musikalske takter.
* **loop count** – hvor mange ganger loopen gjentas før den tilbakestilles. Hvis den er satt til 1, følger partiklene alltid nøyaktig samme simulering hver gang, slik at den blir helt repeterbar. Høyere verdier gir mer variasjon før syklusen tilbakestilles.
* **delay** – forskyver starttidspunktet for utslippet med et antall 1/64-noter, for timingeffekter.

**Motion**

* **speed** – hvor raskt partiklene beveger seg bort fra emitteren.
* **speed variation** – legger til tilfeldighet slik at partiklene ikke alle beveger seg med samme hastighet. Gir en mer naturlig spredning.
* **direction** – angir basisretningen partiklene skytes i, definert av **x, y, z angles**. Disse vinklene roterer skytevektoren i 3D-rom, slik at du kan sikte partiklene rett opp, sidelengs eller i en hvilken som helst diagonal. Kombiner med **spread** for bredere kjegler eller mer kaotiske utbrudd.

{% hint style="info" %}
**Euler angles**\
Liberation bruker **Euler angles** til å beskrive orientering i 3D-rom. Dette er ganske enkelt rotasjoner rundt de tre hovedaksene:

* **X** – vipp fremover/bakover (som å nikke)
* **Y** – drei venstre/høyre (som å riste på hodet «nei»)
* **Z** – rull med/mot klokken (som å legge hodet på skakke)

Ved å justere disse tre verdiene kan du peke partikler i hvilken som helst retning.
{% endhint %}

* **direction variation** – legger til tilfeldig spredning rundt den retningen. Nyttig for å lage kjegler, sprayer eller eksplosjoner.
* **drag** – bremser partiklene over tid. Høyere verdier gjør at de føles tyngre og tregere.
* **gravity** – trekker partiklene ned (positiv) eller skyver dem opp (negativ).
* **gravity variation** – legger til variasjon i gravitasjonen per partikkel, noe som gjør bevegelsen mer kaotisk.

**Life**

* **life duration** – hvor lenge partiklene eksisterer (målt i 1/64-note-enheter). Med kortere verdier forsvinner partiklene raskt, mens de med lengre verdier forblir synlige over lengre tid.
* **life variation** – legger til tilfeldighet i partiklenes levetid, slik at de ikke alle forsvinner samtidig.
* **start delay / start delay variation** – forsinker når hver partikkel blir synlig (i 1/64-note-trinn). Partikkelen er allerede generert og i bevegelse i denne perioden, men lysstyrken holdes på 0, så den forblir usynlig til forsinkelsen er over. Dette er nyttig hvis du vil at forsinkede fyrverkeri-«glitter» skal dukke opp.

**Colour & brightness**

* **hue start** – startfargen på partiklene.
* **hue variation** – legger til tilfeldighet slik at partiklene ikke alle starter med samme farge.
* **hue change** – forskyver hue gjennom partikkelens levetid og lager trails som skifter farge.
* **brightness start / brightness end** – legger lysstyrke over partikkelens levetid. Vanligvis setter du brightness start høyt og brightness end lavt, slik at de toner naturlig ut.
* **brightness variation** – randomiserer startlysstyrken for et mer dynamisk uttrykk.
* **saturation start / saturation end** – angir hvor mettet fargen er ved start og slutt.
* **saturation variation** – randomiserer metningen for variasjon mellom partikler.

**Simulation**

* **time adjustment** – øker eller senker hastigheten på hele partikkelsimuleringen. Nyttig for å synkronisere til ulike tempoer eller overdrive bevegelsen.
