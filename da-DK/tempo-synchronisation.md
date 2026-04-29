---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / synkronisering

Musiksynkronisering er et grundlæggende element i Liberation. Når tempo og beats passer til musikken, kan du være sikker på, at alt kører synkront. Hvis du er så heldig at have MIDI clock (eller Ableton Link), behøver du slet ikke bekymre dig om manuel synkronisering. Hvis ikke, er der ingen grund til bekymring – du kan matche manuelt med _Live_-tempofunktionen.

Hvis du har erfaring med musik- eller lyssoftware, vil processen være velkendt. Hvis ikke, er det en god idé at bruge lidt tid på at lære systemet at kende og øve dig derhjemme, før du står til et liveshow.

## Tempo-panel

_Tempo_-panelet vises altid på skærmen og indeholder alle synkroniseringsindstillinger. Øverst ser du den aktuelle takt-/beat-tæller og en transportsektion med knapper til play/pause og rewind/fastforward.

Nedenunder ser du beatmarkøren: fire firkanter, der “pulserer” i takt med beatet. Denne _beat marker_ er en meget nyttig visualisering, som du hele tiden vil bruge som reference, når du arbejder med _Live_-temposystemet.

### Indstilling af tempo

Du har flere muligheder for at indstille tempoet:

* Klik og træk på _Tempo_-skyderen
* Shift-klik og træk på _Tempo_-skyderen for at ændre tempoet i trin på 0,1
* Dobbeltklik på _Tempo_-skyderen, og skriv tallet manuelt
* Brug _Tempo_-knappen på APC40 (tryk på shift for trin på 0,1)
* Tap Tempo

{% hint style="info" %}
Tempo angives i “beats per minute”, og den traditionelle standardværdi er normalt 120.
{% endhint %}

## Tap Tempo

Indstil tempoet automatisk ved at klikke på _TAP_-knappen i takt med beatet. Indstil starten af takten med _RESET_-knappen.

{% hint style="info" %}
Tap Tempo-systemet er intelligent nok til at registrere, hvis du har holdt en pause fra at tappe i et stykke tid, eller hvis du har misset et par beats. Hvis du begynder at tappe i dobbelt tempo, forstår det, at du vil fordoble tempoet. Det samme gælder, hvis du tapper i halvt tempo.

Det er også intelligent nok til at finde ud af, hvis to personer tapper tempo på samme tid (fx én på tastaturet og én på APC40). Liberation udjævner de dobbelte taps.
{% endhint %}

#### Tastaturkommandoer:

T - tap tempo\
R - reset takten\
Y - afrund tempoet til nærmeste beat per minute.

{% hint style="info" %}
Da det meste musik i dag skabes digitalt, vil tempoet sandsynligvis være et afrundet heltal. Så hvis et tappet tempo virker til at være tæt på, kan du bruge Y-tasten (eller flytte APC40-tempo-knappen ét “tick”) for at afrunde det til et helt tal.
{% endhint %}

#### APC40-kontroller:

APC40 har en dedikeret _TAP TEMPO_-knap, og du kan også bruge en tilsluttet fodkontakt til at tappe med foden!

Brug _TEMPO_-knappen til at justere. Tryk på _SHIFT_, mens du bruger _TEMPO_-knappen, for finjustering.

Brug _METRONOME_-knappen til at **resette takten**. (Bemærk, at _METRONOME_-knappen også lyser i takt med beatet)

Drej _TEMPO_-knappen ét “tick” til højre eller venstre for at **runde tempoet** op eller ned til et helt BPM-tal.

Se også [APC40-reference](reference/apc40-reference.md "mention")

### Nudge tempo

Hvis du er sikker på, at du er tæt nok på det faktiske tempo, men oplever, at du driver ud af takt, kan du bruge _NUDGE_-knapperne til at korrigere.

Hvis Liberation-tempoet kommer foran musikken, skal du trykke og holde _NUDGE -_ nede for midlertidigt at sænke tempoet, indtil det passer igen.

Hvis Liberation-tempoet falder bagud i forhold til musikken, skal du trykke og holde _NUDGE +_ nede for midlertidigt at øge tempoet, indtil det passer igen.

{% hint style="info" %}
Du kan bruge enten NUDGE-knapperne på skærmen eller de dedikerede knapper på APC40.
{% endhint %}

### Halvt tempo / dobbelt tempo

Brug knapperne _÷2_ og _x2_ til permanent at halvere eller fordoble tempoet. I modsætning til tempo multiplier er dette en permanent ændring af det aktuelle tempo.

## Tempo Multiplier

_Tempo Multiplier_-systemet lader dig midlertidigt justere tempoet og derefter vende tilbage til den tidligere værdi.

Slå _Tempo Multiplier_ til eller fra ved at trykke på _TEMPO MULTIPLIER_-knappen eller _BANK_-knappen på APC40. Justér med skyderen på skærmen eller med APC40 A-B-skyderen. Du kan også bruge preset-knapperne _25%, 50%, 100% 200%_.

## Eksterne tempokilder

### MIDI Clock

For at synkronisere til et eksternt MIDI clock-signal skal du vælge _MIDI CLOCK_-radioknappen og vælge MIDI-enheden i rullemenuen. Bemærk den farvede statuslampe ved siden af rullemenuerne:

* Grøn - modtager et MIDI clock-signal
* Orange - kan oprette forbindelse til MIDI-enheden, men der er i øjeblikket intet clock-signal
* Rød - kan ikke oprette forbindelse til MIDI-enheden

{% hint style="info" %}
MIDI Clock udsender en serie frames (24 per fjerdedelsnode), men der er ingen positionsdata i beskederne. Det betyder, at det er nyttigt til at holde tempo, men du kan stadig få brug for at resette takten.

Liberations MIDI Clock-tempokilde reagerer også på **MIDI Machine Control (MMC)**-beskeder, så hvis din clock-kilde sender disse, behøver du ikke resette takten manuelt.
{% endhint %}



### Timeline

Hver timeline har sit eget tempo, som kan være en fast værdi eller en _Tempo Map_. _Tempo Map_ giver dig mulighed for at justere tempoet på bestemte tidspunkter i timelinen.

Timeline-tempoet bruges, når _TIMELINE_ er valgt som tempokilde.

{% hint style="info" %}
Du kan køre en timeline sammen med _any_ af tempokilderne! Så hvis du har et liveband, der ikke spiller efter click, kan du starte timelinen manuelt og holde den synkroniseret med _LIVE_-tempokilden. Eller hvis du har et MIDI clock-signal, kan du bruge det!
{% endhint %}
