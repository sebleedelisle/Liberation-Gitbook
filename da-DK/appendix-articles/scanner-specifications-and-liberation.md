---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Scannerspecifikationer og Liberation

### Den lidt rodede virkelighed bag scannerspecifikationer

Punktrater og scannerspecifikationer kan være lidt forvirrende. Du ser ofte specifikationer som 30kpps @ 8º eller 50kpps @ 4º, men det er ikke altid tydeligt, hvad tallene faktisk betyder.

{% hint style="info" %}
Ansvarsfraskrivelse - jeg er ikke specialist i scannerhardware, men jeg har mange års praktisk erfaring med at få scannere af meget forskellig kvalitet til at se gode ud via software og generering af point streams i stedet for hardware-tuning. Dette er baseret på den erfaring.
{% endhint %}

#### **Hvor disse tal kommer fra**

Begreber som “30K” og “50K” er forkortelser baseret på, hvordan scannere vurderes med ILDA-testmønstret ved disse punktrater under bestemte forhold.

Når en scanner angives som for eksempel: _30Kpps @ 8°_ betyder det i praksis:

> “Denne scanner kan gengive ILDA-testmønstret ved 30.000 punkter/sek. ved en scanningsvinkel på 8°, når den er korrekt tunet.”

Det er ikke en fuldstændig eller fuldt standardiseret måling af ydeevne i praksis. Faktisk blev det oprindeligt slet ikke designet som en benchmark - det blev brugt til en **tuningprocedure**. Du kører et kendt mønster ved en fast punktrate (f.eks. 30.000 punkter/sek.) og justerer damping og gain, indtil det ser korrekt ud.

Men det er stadig den mest udbredte reference, vi har, og den kan give dig en god idé om scannernes kvalitet, i hvert fald hos anerkendte producenter. Med _mindre anerkendte_ producenter derimod...

#### Hvis du vil teste scannerne ud fra deres angivne specifikationer

{% hint style="danger" %}
**Dette er en avanceret teknik, og du kan beskadige dine scannere, hvis du ikke er forsigtig. Anbefales ikke, medmindre du ved, hvad du laver.**
{% endhint %}

Du skal finde software, der kan outputte [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) - jeg tror, LaserShowGen muligvis kan gøre det - og justere outputstørrelsen, så den matcher den angivne scanningsvinkel (f.eks. 8°). Se ILDA-dokumentationen for råd om, hvordan du analyserer outputtet.

#### Hvorfor det måske ikke er en god benchmark

Først og fremmest kan dit testmønster blive vist forkert, selvom dine scannere er gode, fordi de ikke er tunet på en måde, der er optimeret til netop det.

Det kan være en nyttig generel rettesnor for “gode” kontra “dårlige” scannere, men producenter kan nogle gange tage sig ret store friheder med disse specifikationer.

#### Så hvordan vælger jeg en god scanner?

Jeg vil sige: sørg for, at de er lavet af en anerkendt producent. Dyre high-end scannerproducenter som Cambridge Technology (CT), Eye Magic (EMS) og ScannerMAX (et datterselskab af Pangolin) er altid gode valg, og dem går du ikke galt i byen med. Men når et sæt scannere koster omkring $1000, er det for mange af os, der er i gang, dyrere end selve laserne!

Så jeg har for det meste brugt kinesiske producenter. Dragon Tiger (DT)-scannere er fornuftige og til at betale, og jeg mener, LightSpace bruger dem. Mange andre producenter (herunder OPT og Able i nogle modeller) bruger også DT-baserede systemer.

Phenix Technology (PT) ligger generelt i et lavere niveau, men helt ærligt er de sandsynligvis fine til det meste.

**Hvis dine scannere ikke har noget mærke, er det nok dér, du skal begynde at bekymre dig om kvaliteten!**

#### Hvordan Liberation hjælper

Først og fremmest: til det meste har du ikke brug for virkelig dyre scannere! Prisvenlige 30kpps DT eller endda PT er fine. Standardindstillingerne for scannerne er bevidst konservative, og for det meste _bør du ikke have brug for at justere dem_ (bortset fra _Scanner sync_).

Selv hvis du har bedre scannere, er der ingen grund til at drive dem hårdere end nødvendigt. Det forlænger deres levetid markant.

#### Hvad er en "point stream"?

Du har sikkert hørt udtrykket før - det er sådan, vi styrer scannernes bane.

En point stream er en liste over X/Y-positioner, hver med en farve. For at tegne noget som en hvid linje sender du en sekvens af punkter langs linjen, alle sat til hvid. Scannerne bevæger sig derefter fra punkt til punkt med en fast hastighed - punkter pr. sekund-raten (PPS) - og strålen tegner formen.

#### Hvordan det fungerer i traditionel lasersoftware

Traditionel lasersoftware gemmer en point stream for hver cue. For animerede cues betyder det som regel en separat point stream for hvert frame. Det centrale er, at alt er helt forudbestemt. Derfor får en højere punktrate scannerne til at bevæge sig hurtigere gennem de samme foruddefinerede data.

{% hint style="info" %}
For ældre software var denne tilgang nødvendig - computere var simpelthen ikke hurtige nok til at generere point streams i realtid. Derfor findes der normalt en separat cue editor, som bruges til at forhåndsgenerere dataene for hvert animationsframe.

Det forklarer også, hvorfor indhold kan fylde flere gigabyte. Du gemmer reelt store, ukomprimerede bølgeformer ved ret høje sample rates.
{% endhint %}

#### Hvorfor "point rate" er mindre meningsfuldt i Liberation

Liberation genererer point streamen i realtid, hvilket giver os en enorm fleksibilitet. Bemærk indstillingen "Scanner speed" i Laser Settings-panelet. Den gør det muligt at sætte scannerne op og ned i hastighed, men vigtigt: den ændrer **ikke** den underliggende punktrate (PPS).

#### Vent, hvad? Hvordan?

Jeg ved det - det lyder mærkeligt i starten.

Fordi Liberation genererer point streamen i realtid, kan den justere denne point stream. Jo mere spredt punkterne er, desto hurtigere bevæger scannerne sig. Jo tættere de ligger, desto langsommere bevæger scannerne sig.

{% hint style="info" %}
I nyere versioner af Liberation påvirker den faktiske _point rate_ (i avancerede indstillinger) slet ikke scannerhastigheden. I stedet justerer rendereren punktfordelingen, så den matcher den valgte punktrate, samtidig med at scannernes bevægelse forbliver uændret.

Det har en effekt på punktbanens “opløsning”, men det gør primært en forskel for grafik (og kan hjælpe med finere justering af _scanner sync_-indstillingen).
{% endhint %}

#### Fint! Så hvad betyder det egentlig i praksis?

Godt spørgsmål. Her er mine tips:

* Undgå scannere uden mærke. Hvis du kan få hurtigere scannere, så gør det - minimum 30KPPS.
* I de fleste tilfælde er DT30-scannere fine, og PT30-scannere er sandsynligvis OK i billigere lasere.
* Hvis du laver grafik, vil flere lasere i de fleste tilfælde være bedre end hurtigere scannere.
* Når du når op i high-end setups, vil alle de etablerede high-end mærker være fine.
* Hvis du kun kan få de billigste scannere uden mærke, er Liberations standardindstillinger ret konservative, og du får sandsynligvis OK resultater til grundlæggende beam-arbejde. Hvis det har svært ved at følge med, så reducer indstillingen **Speed** (men lad være med at ændre punktraten!).

#### Og ILDA Test Pattern?

…er stadig meget nyttigt som kalibrerings- og referenceværktøj, men det blev aldrig designet som en komplet benchmark og kan misbruges eller fortolkes løst af producenter.
