---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / synkronisering

Musiksynkronisering är en grundläggande del av Liberation. När tempot och slagen matchar musiken kan du vara säker på att allt ligger i synk. Om du har turen att få MIDI clock (eller Ableton Link) behöver du inte tänka på manuell synkning alls. Men om inte, ingen fara – du kan matcha manuellt med _Live_-tempofunktionen.

Om du har erfarenhet av musik- eller ljusprogramvara kommer den här processen att kännas bekant. Om inte är det värt att lägga lite tid på att bekanta dig med systemet och öva hemma innan du kommer till en liveshow.

## Tempo panel

_Tempo_-panelen visas alltid på skärmen och innehåller alla synkroniseringsinställningar. Längst upp ser du den aktuella takt-/slagräknaren och en transportkontroll med knappar för play/pause samt rewind/fast-forward.

Under detta ser du taktslagsindikatorn: fyra rutor som ”pulserar” i takt med slaget. Den här _beat marker_ är en mycket användbar visualisering, och du kommer att titta på den ofta när du använder _Live_-temposystemet.

### Ställa in tempot

Du har flera sätt att ställa in tempot:

* Klicka och dra på _Tempo_-reglaget
* Shift-klicka och dra på _Tempo_-reglaget för att ändra tempot i steg om 0,1
* Dubbelklicka på _Tempo_-reglaget och skriv in numret manuellt
* Använd _Tempo_-ratten på APC40 (håll ned shift för steg om 0,1)
* Tap Tempo

{% hint style="info" %}
Tempo anges i ”beats per minute”, och standardvärdet är traditionellt oftast 120.
{% endhint %}

## Tap Tempo

Ställ in tempot automatiskt genom att klicka på _TAP_-knappen i takt med slaget. Ställ in början av takten med _RESET_-knappen.

{% hint style="info" %}
Tap Tempo-systemet är smart nog att förstå om du har tagit en paus från att tappa en stund, eller om du har missat ett par slag. Om du börjar tappa i dubbel hastighet förstår det att du vill dubbla tempot, och samma sak gäller om du tappar i halv hastighet.

Det är också smart nog att räkna ut om två personer tappar tempo samtidigt (t.ex. en på tangentbordet och en på APC40). Liberation jämnar ut de dubbla tryckningarna.
{% endhint %}

#### Tangentbordskommandon:

T - tap tempo\
R - återställ takten\
Y - avrunda tempot till närmaste beat per minute.

{% hint style="info" %}
Eftersom det mesta av dagens musik skapas digitalt är tempot sannolikt ett avrundat heltal. Så om ett tappat tempo verkar ligga nära, använd Y-tangenten (eller flytta APC40-temporeglaget ett ”tick”) för att avrunda till ett heltal
{% endhint %}

#### APC40-kontroller:

APC40 har en dedikerad _TAP TEMPO_-knapp, eller så kan du använda en ansluten fotpedal för att tappa med foten!

Använd _TEMPO_-ratten för att justera. Håll ned _SHIFT_ medan du använder _TEMPO_-ratten för finjusteringar.

Använd _METRONOME_-knappen för att **återställa takten**. (Observera att _METRONOME_-knappen också lyser i takt med slaget)

Vrid _TEMPO_-ratten ett ”tick” åt höger eller vänster för att **avrunda tempot** uppåt eller nedåt till ett helt BPM-tal.

Se även [APC40-referens](reference/apc40-reference.md "mention")

### Nudge tempo

Om du är säker på att du ligger tillräckligt nära det faktiska tempot men märker att du driver ur takt, använd _NUDGE_-knapparna för att korrigera.

Om Liberation-tempot hamnar före musiken, håll ned _NUDGE -_ för att tillfälligt sakta ned tills det ligger rätt igen.

Om Liberation-tempot hamnar efter musiken, håll ned _NUDGE +_ för att tillfälligt öka hastigheten tills det ligger rätt igen.

{% hint style="info" %}
Du kan använda antingen NUDGE-knapparna på skärmen eller de dedikerade knapparna på APC40.
{% endhint %}

### Half time / double time

Använd knapparna _÷2_ och _x2_ för att halvera respektive dubbla tempot permanent. Till skillnad från tempo multiplier är detta en permanent ändring av det aktuella tempot.

## Tempo Multiplier

_Tempo Multiplier_-systemet låter dig tillfälligt justera tempot innan du återgår till det tidigare värdet.

Slå på eller av _Tempo Multiplier_ genom att trycka på _TEMPO MULTIPLIER_-knappen eller _BANK_-knappen på APC40. Justera med reglaget på skärmen eller med APC40 A-B-reglaget. Du kan också använda preset-knapparna _25%, 50%, 100% 200%_.

## Externa tempokällor

### MIDI Clock

För att synka till en extern MIDI clock-signal väljer du radioknappen _MIDI CLOCK_ och väljer MIDI-enheten i rullgardinsmenyn. Observera den färgade statuslampan bredvid rullgardinsmenyerna:

* Grön - tar emot en MIDI clock-signal
* Orange - kan ansluta till MIDI-enheten, men det finns för närvarande ingen klocksignal
* Röd - kan inte ansluta till MIDI-enheten

{% hint style="info" %}
MIDI Clock skickar en serie frames (24 per fjärdedelsnot), men det finns ingen positionsdata i meddelandena. Det betyder att det hjälper till att hålla takten, men du kan fortfarande behöva återställa takten.

Liberations MIDI Clock-tempokälla svarar också på **MIDI Machine Control (MMC)**-meddelanden, så om din klockkälla skickar sådana behöver du inte återställa takten manuellt.
{% endhint %}



### Ableton Link

För att synka med Ableton Link väljer du _ABLETON LINK_ som tempokälla. Liberation ansluter till Link-sessionen på ditt lokala nätverk och följer det delade tempot och slagfasen från andra appar med Link-stöd.

Ableton Link använder ingen MIDI-port och överför ingen absolut song position. Använd kontrollerna för taktåterställning om du behöver att Liberations taktstart ska ligga i linje med ett visst ögonblick i showen.

### Timeline

Varje timeline har sitt eget tempo, som kan vara ett fast värde eller en _Tempo Map_. Med _Tempo Map_ kan du justera tempot vid specifika tidpunkter i timelinen.

Timeline-tempot används när _TIMELINE_ är valt som tempokälla.

{% hint style="info" %}
Du kan köra en timeline tillsammans med _vilken som helst_ av tempokällorna! Så om du har ett liveband som inte spelar till klick kan du starta timelinen manuellt och hålla den synkad med tempokällan _LIVE_. Eller om du har en MIDI clock-signal kan du använda den!
{% endhint %}
