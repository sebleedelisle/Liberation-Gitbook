---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / synkronisering

Musikksynkronisering er en grunnleggende del av Liberation. Når tempoet og taktslagene stemmer med musikken, kan du være trygg på at alt er synkronisert. Hvis du er så heldig å få MIDI clock (eller Ableton Link), trenger du ikke å tenke på manuell synkronisering i det hele tatt. Hvis ikke, er det ingen grunn til bekymring – du kan matche manuelt med _Live_-tempofunksjonen.

Hvis du har erfaring med musikk- eller lysprogramvare, vil denne prosessen være kjent for deg. Hvis ikke, bør du bruke litt tid på å bli kjent med systemet og øve hjemme før du går på en live-forestilling.

## Tempo-panel

_Tempo_-panelet vises alltid på skjermen og inneholder alle synkroniseringsinnstillingene. Øverst ser du gjeldende takt-/slagteller og en transport med knapper for play/pause og spol tilbake / spol fremover.

Under dette ser du beat-markøren: fire firkanter som «pulserer» i takt med slaget. Denne _beat marker_-visningen er svært nyttig, og du kommer til å bruke den hele tiden når du jobber med _Live_-temposystemet.

### Stille inn tempoet

Du har flere måter å stille inn tempoet på:

* Klikk og dra på _Tempo_-skyveknappen
* Shift-klikk og dra på _Tempo_-skyveknappen for å endre tempoet i trinn på 0,1
* Dobbeltklikk på _Tempo_-skyveknappen og skriv inn tallet manuelt
* Bruk _Tempo_-knotten på APC40 (trykk på shift for trinn på 0,1)
* Tap Tempo

{% hint style="info" %}
Tempo defineres i «beats per minute», og standardverdien er tradisjonelt vanligvis 120.
{% endhint %}

## Tap Tempo

Still inn tempoet automatisk ved å klikke på _TAP_-knappen i takt med musikken. Angi starten på takten med _RESET_-knappen.

{% hint style="info" %}
Tap Tempo-systemet er smart nok til å forstå om du har tatt en pause fra tappingen en stund, eller om du har hoppet over et par slag. Hvis du begynner å tappe i dobbelt tempo, forstår det at du vil doble tempoet. Det samme gjelder hvis du tapper i halvt tempo.

Det er også smart nok til å oppdage om to personer tapper tempo samtidig (for eksempel én på tastaturet og én på APC40). Liberation jevner ut de doble tappingene.
{% endhint %}

#### Tastaturkommandoer:

T - tap tempo\
R - reset the bar\
Y - round the tempo to the nearest beat per minute.

{% hint style="info" %}
Siden det meste av musikk i dag lages digitalt, er tempoet sannsynligvis et avrundet heltall. Så hvis et tappet tempo virker nært nok, kan du bruke Y-tasten (eller flytte APC40 tempo-knotten ett «hakk») for å runde av til et helt tall.
{% endhint %}

#### APC40-kontroller:

APC40 har en egen _TAP TEMPO_-knapp, eller du kan bruke en tilkoblet fotbryter til å tappe med foten!

Bruk _TEMPO_-knotten for å justere. Trykk på _SHIFT_ mens du bruker _TEMPO_-knotten for finjustering.

Bruk _METRONOME_-knappen til å **tilbakestille takten**. (Merk at _METRONOME_-knappen også lyser i takt med slaget)

Drei _TEMPO_-knotten ett «hakk» til høyre eller venstre for å **runde av tempoet** opp eller ned til et helt BPM-tall.

Se også [apc40-reference.md](reference/apc40-reference.md "mention")

### Nudge tempo

Hvis du er trygg på at du er nær nok det faktiske tempoet, men merker at du driver ut av takt, bruker du _NUDGE_-knappene for å korrigere.

Hvis Liberation-tempoet ligger foran musikken, holder du inne _NUDGE -_ for å senke tempoet midlertidig til det er justert inn igjen.

Hvis Liberation-tempoet sakker etter musikken, holder du inne _NUDGE +_ for å øke tempoet midlertidig til det er justert inn igjen.

{% hint style="info" %}
Du kan bruke enten NUDGE-knappene på skjermen eller de dedikerte knappene på APC40.
{% endhint %}

### Halvt tempo / dobbelt tempo

Bruk knappene _÷2_ og _x2_ til å halvere og doble tempoet permanent. I motsetning til tempo multiplier er dette en permanent endring av gjeldende tempo.

## Tempo Multiplier

_Tempo Multiplier_-systemet lar deg justere tempoet midlertidig før du går tilbake til slik det var før.

Slå _Tempo Multiplier_ av eller på ved å trykke på _TEMPO MULTIPLIER_-knappen eller _BANK_-knappen på APC40. Juster med skyveknappen på skjermen eller med APC40 A-B-skyveknappen. Du kan også bruke forhåndsinnstillingsknappene _25%, 50%, 100% 200%_.

## Eksterne tempokilder

### MIDI Clock

For å synkronisere til et eksternt MIDI clock-signal velger du radioknappen _MIDI CLOCK_ og velger MIDI-enheten fra rullegardinmenyen. Legg merke til det fargede statuslyset ved siden av rullegardinmenyene:

* Grønn – mottar et MIDI clock-signal
* Oransje – kan koble til MIDI-enheten, men det finnes ikke noe klokkesignal for øyeblikket
* Rød – kan ikke koble til MIDI-enheten

{% hint style="info" %}
MIDI Clock kringkaster en serie frames (24 per firedelsnote), men meldingene inneholder ingen posisjonsdata. Det betyr at det er nyttig for å holde tempoet, men du må kanskje fortsatt tilbakestille takten.

Liberation MIDI Clock-tempokilden reagerer også på **MIDI Machine Control (MMC)**-meldinger, så hvis klokkekilden din sender disse, trenger du ikke å tilbakestille takten manuelt.
{% endhint %}



### Timeline

Hver timeline har sitt eget tempo, som kan være en fast verdi eller et _Tempo Map_. Med _Tempo Map_ kan du justere tempoet på bestemte tidspunkter i timeline.

Timeline-tempoet brukes når _TIMELINE_ er valgt som tempokilde.

{% hint style="info" %}
Du kan kjøre en timeline sammen med _hvilken som helst_ av tempokildene! Så hvis du har et liveband som ikke spiller etter klikkspor, kan du starte timeline manuelt og holde den synkronisert med _LIVE_-tempokilden. Eller hvis du har et MIDI clock-signal, kan du bruke det!
{% endhint %}
