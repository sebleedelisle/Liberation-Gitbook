---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation støtter synkronisering med et eksternt SMPTE/LTC-timecode-signal, som ofte brukes i livemusikkshow for å holde lys, pyro, video og backing tracks synkronisert.

{% hint style="info" %}
Hva er SMPTE/LTC?

SMPTE er en standard for timecode, og LTC er denne timecode-informasjonen konvertert til et lydsignal. Hvis du lytter til denne lyden, høres det ut som en forferdelig høyfrekvent piping, men for datamaskiner er det tidsinformasjon med høy oppløsning.

**Nerdefakta!**

Historisk har SMPTE blitt brukt til å holde video og lyd synkronisert, eller ved synkronisering til analog tape kunne ett spor ha timecode-lyden innspilt på seg, noen ganger kalt å "stripe" tapen. Du kunne bruke dette timecode-sporet til å holde flere tape-maskiner synkronisert med hverandre, eller til å holde en MIDI-sequencer synkronisert med tapen. (Da slapp du å spille inn MIDI-instrumenter på tape; du kunne bare la sequenceren spille dem live mens du mikset!)

SMPTE står for Society of Motion Picture and Television Engineers, som definerte standarden. LTC står for _Linear TimeCode._
{% endhint %}

Du kan motta et LTC-timecode-signal via et hvilket som helst lydinterface på datamaskinen, men det anbefales å bruke et profesjonelt interface med minst én justerbar XLR-inngang og mulighet for monitorering.

Jeg har hatt gode erfaringer med [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), siden det har hodetelefonmonitorering, 2 XLR-innganger og ikke trenger noen spesielle drivere (i hvert fall på macOS). Hvis du bare skal bruke det til timecode, kan du velge den litt billigere [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (som bare har én inngang og ingen MIDI), men helt ærlig bør et hvilket som helst noenlunde bra lydinterface fungere.

{% hint style="info" %}
LTC-timecode-signaler distribueres vanligvis via balanserte XLR-kabler, siden de er robuste nok til å sende lydsignaler med lavt nivå over lange avstander. (XLR er den runde kontakten som vanligvis brukes med mikrofoner)
{% endhint %}

### Hardware connections

Koble XLR-kabelen med timecode-signalet til lydinterfacet, og kontroller at du får et godt signal. Juster nivået på lydinterfacet til signalet er sterkt, men ikke klipper. Hvis lydinterfacet har hodetelefonutgang, kan du lytte til timecode-signalet og kontrollere at det ikke hakker eller har for mye støy.

{% hint style="info" %}
Teoretisk er det mulig å motta signalet via jack-kontakten på MacBook-en, men dette krever en spesialkabel. Disse kontaktene er vanligvis 4-pols TRRS-minijacker, og jeg er ærlig talt ikke sikker på hvilke av disse lederne som kan brukes som lydinngang. Jeg er heller ikke sikker på hvilket spenningsnivå den tåler (jeg har lest et sted at det var +/-1V, men bruk dette på eget ansvar!)

Jeg tror du har det bedre med å skaffe et billig USB-lydinterface i stedet for å forsøke dette.
{% endhint %}

Hvis lydinterfacet ikke har noen form for input monitoring, kan du sjekke i macOS-systeminnstillingene (under _Sound_) for å kontrollere at du får et signal. (På Windows bruker du _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS viser inngangsnivået for alle lydinterface i systeminnstillingspanelet Sound</p></figcaption></figure>

### Setting up in Liberation

1. Velg lydinterfacet ditt og riktig inngangskanal i Timecode settings Window.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Merk at det finnes egne valg i nedtrekksmenyen for hver inngangskanal i lydinterfacet ditt

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Legg merke til firkanten til venstre. Hvis du mottar et gyldig timecode-signal, blir den grønn. Hvis ikke, er den rød.

2. Velg riktig framerate for innkommende timecode. Den som leverer timecode til deg, skal kunne fortelle deg hvilken framerate som brukes. (Hvis du velger feil, vil det fortsatt synkronisere, men du vil merke et lite "hopp" hvert sekund)
3. Åpne Timeline sine timecode settings med det lille klokkeikonet på tidslinjelinjen, og velg SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Juster start offset (i timer, minutter, sekunder, frames) slik at den stemmer med starten av låten. Hvis du har flere timelines, må du angi disse valgene separat for hver av dem.

{% hint style="info" %}
I turnéverdenen er det en vanlig konvensjon å la hver låt starte på en ny time, for eksempel 01:00:00:00 for første låt, 02:00:00:00 for andre låt, og så videre.

Liberation bytter automatisk til riktig timeline basert på timecode, så du trenger aldri å bytte timelines manuelt under et show.
{% endhint %}

Merk at i motsetning til MIDI Clock og Ableton Link er SMPTE et _absolutt_ tidssystem, målt i timer, minutter, sekunder og frames. Liberation sitt kjernetidssystem er basert på beats og bars, så når du mottar timecode, brukes tempoet som er satt opp i timeline. Du må sørge for at dette tempoet er synkronisert med musikken som også er synkronisert til timecode.
