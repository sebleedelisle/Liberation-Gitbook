---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Skannerspesifikasjoner og Liberation

### Den rotete virkeligheten bak skannerspesifikasjoner

Punktrater og skannerspesifikasjoner kan være litt forvirrende. Du ser ofte spesifikasjoner som 30kpps @ 8º eller 50kpps @ 4º, men det er ikke alltid åpenbart hva disse tallene faktisk betyr.

{% hint style="info" %}
Ansvarsfraskrivelse – jeg er ikke spesialist på skannermaskinvare, men jeg har mange års praktisk erfaring med å få skannere av svært ulik kvalitet til å se bra ut ved hjelp av programvare og generering av punktstrømmer, i stedet for maskinvarejustering. Dette er basert på den erfaringen.
{% endhint %}

#### **Hvor disse tallene kommer fra**

Begreper som “30K” og “50K” er kortformer basert på hvordan skannere vurderes med ILDA-testmønsteret ved disse punktratene under bestemte forhold.

Når en skanner oppgis som for eksempel: _30Kpps @ 8°_ betyr det egentlig:

> “Denne skanneren kan gjengi ILDA-testmønsteret ved 30 000 punkter/sek ved en skannevinkel på 8°, når den er riktig justert.”

Det er ikke en komplett eller fullt standardisert måling av ytelse i praksis. Faktisk ble det opprinnelig ikke laget som en ytelsestest i det hele tatt – det ble brukt som en **justeringsprosedyre**. Du kjører et kjent mønster med en fast punktrate (f.eks. 30 000 punkter/sek), og justerer demping og gain til det ser riktig ut.

Men det er fortsatt den mest brukte referansen vi har, og den kan gi deg en god pekepinn på kvaliteten på skannerne, i hvert fall fra seriøse produsenter. Med _mindre seriøse_ produsenter derimot ...

#### Hvis du vil teste skannerne slik de er spesifisert

{% hint style="danger" %}
**Dette er en avansert teknikk, og du kan skade skannerne dine hvis du ikke er forsiktig. Anbefales ikke med mindre du vet hva du gjør.**
{% endhint %}

Du må finne programvare som kan sende ut [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) – jeg tror LaserShowGen kanskje kan gjøre det – og justere utgangsstørrelsen slik at den samsvarer med den angitte skannevinkelen (f.eks. 8°). Se ILDA-dokumentasjonen for råd om hvordan du analyserer utdataene.

#### Hvorfor det kanskje ikke er en god ytelsestest

Først og fremst kan testmønsteret ditt vises feil selv om skannerne dine er gode, fordi de ikke er justert på en måte som er optimalisert for akkurat det mønsteret.

Det kan være en nyttig generell pekepinn for “gode” kontra “dårlige” skannere, men produsenter kan noen ganger tøye disse spesifikasjonene ganske langt.

#### Så hvordan velger jeg en god skanner?

Jeg vil si: sørg for at de er laget av en seriøs produsent. Dyre skannere i toppklassen fra produsenter som Cambridge Technology (CT), Eye Magic (EMS) og ScannerMAX (et datterselskap av Pangolin) er alltid gode valg, og du går ikke feil der. Men når et par skannere koster rundt $1000, er det for mange av oss som starter opp dyrere enn selve laserne!

Så jeg har for det meste brukt kinesiske produsenter. Dragon Tiger (DT)-skannere er brukbare og rimelige, og jeg tror LightSpace bruker dem. Mange andre produsenter (inkludert OPT og Able i noen modeller) bruker også DT-baserte systemer.

Phenix Technology (PT) er generelt et lavere nivå, men helt ærlig er de sannsynligvis helt greie til det meste.

**Hvis skannerne dine er uten merke, er det sannsynligvis da du bør bekymre deg for kvaliteten!**

#### Hvordan Liberation hjelper

Først og fremst: til det meste trenger du ikke veldig dyre skannere! Rimelige 30kpps DT, eller til og med PT, vil fungere fint. Standardinnstillingene for skannere er bevisst konservative, og for det meste _skal du ikke trenge å justere dem_ (bortsett fra _Scanner sync_).

Selv om du har bedre skannere, er det ingen grunn til å drive dem hardere enn nødvendig. Det vil forlenge levetiden deres betydelig.

#### Hva er en “point stream”?

Du har sikkert hørt dette begrepet før – det er måten vi styrer banen til skannerne på.

En punktstrøm er en liste med X/Y-posisjoner, hver med en farge. For å tegne noe som en hvit linje, sender du en sekvens med punkter langs den linjen, alle satt til hvitt. Skannerne beveger seg deretter fra punkt til punkt med en fast hastighet – punkter per sekund (PPS) – og strålen tegner opp formen.

#### Hvordan dette fungerer i tradisjonell laserprogramvare

Tradisjonell laserprogramvare lagrer en punktstrøm for hver cue. For animerte cues betyr det vanligvis en separat punktstrøm for hvert bilde. Hovedpoenget er at alt er fullstendig forhåndsbestemt. Resultatet er at en høyere punktrate får skannerne til å bevege seg raskere gjennom de samme forhåndsdefinerte dataene.

{% hint style="info" %}
For eldre programvare var denne tilnærmingen nødvendig – datamaskiner var rett og slett ikke raske nok til å generere punktstrømmer i sanntid. Derfor finnes det vanligvis en separat cue-editor, som brukes til å forhåndsgenerere dataene for hvert bilde i animasjonen.

Det forklarer også hvorfor innhold kan ta opp gigabyte med plass. Du lagrer i praksis store, ukomprimerte bølgeformer med ganske høye samplingsrater.
{% endhint %}

#### Hvorfor “point rate” er mindre meningsfullt i Liberation

Liberation genererer punktstrømmen i sanntid, noe som gir oss svært stor fleksibilitet. Legg merke til innstillingen "Scanner speed" i Laser Settings-panelet. Den lar oss øke og redusere hastigheten på skannerne, men det viktige er at den **ikke** endrer den underliggende punktraten (PPS).

#### Vent, hva? Hvordan?

Jeg vet, det høres rart ut i starten.

Fordi Liberation genererer punktstrømmen i sanntid, kan den justere denne punktstrømmen. Jo mer spredt punktene er, desto raskere beveger skannerne seg. Jo tettere de ligger, desto saktere beveger skannerne seg.

{% hint style="info" %}
I nyere versjoner av Liberation påvirker ikke den faktiske _punktraten_ (i avanserte innstillinger) skannerhastigheten i det hele tatt. I stedet justerer rendereren punktfordelingen slik at den samsvarer med valgt punktrate, samtidig som bevegelsen til skannerne holdes uendret.

Dette påvirker “oppløsningen” til punktbanen, men det har først og fremst betydning for grafikk (og kan hjelpe med finere justering av _scanner sync_-innstillingen).
{% endhint %}

#### Flott! Så hva betyr alt dette egentlig?

Godt spørsmål. Her er mine tips:

* Unngå skannere uten merke. Hvis du kan få raskere skannere, gjør det – minimum 30KPPS.
* I de fleste tilfeller er DT30-skannere helt fine, og PT30-skannere er sannsynligvis OK i billigere lasere.
* Hvis du jobber med grafikk, vil flere lasere i de fleste tilfeller være bedre enn raskere skannere.
* Når du kommer opp på mer avanserte oppsett, vil alle de etablerte high-end-merkene fungere fint.
* Hvis du bare får tak i de billigste skannerne uten merke, er Liberation sine standardinnstillinger ganske konservative, og du vil sannsynligvis få OK resultater for grunnleggende beam-arbeid. Hvis det sliter, reduser **Speed**-innstillingen (men ikke endre punktraten!).

#### Og ILDA Test Pattern?

… er fortsatt svært nyttig som kalibrerings- og referanseverktøy, men det ble aldri laget som en komplett ytelsestest og kan misbrukes eller tolkes løst av produsenter.
