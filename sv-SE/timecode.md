---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Tidskod

Liberation har stöd för synkronisering med en extern SMPTE/LTC-tidskodsignal, som ofta används i livemusikshower för att hålla ljus, pyro, video och backing tracks i takt.

{% hint style="info" %}
Vad är SMPTE/LTC?

SMPTE är en standard för tidskod, och LTC är denna tidskod omvandlad till en ljudsignal. Om du lyssnar på ljudet låter det som ett fruktansvärt högfrekvent tjut, men för datorer är det tidsinformation med hög upplösning.

**Nördfakta!**

Historiskt har SMPTE använts för att hålla video och ljud synkade, eller vid synk till analogt band kunde ett spår ha tidskodsljudet inspelat på sig, ibland kallat att ”stripa” bandet. Du kunde använda detta tidskodsspår för att hålla flera bandspelare synkade med varandra, eller för att hålla en MIDI-sequencer synkad med bandet. (Då behövde du inte spela in MIDI-instrument på band, utan kunde låta sequencern spela dem live medan du mixade!)

SMPTE står för Society of Motion Picture and Television Engineers, som definierade standarden. LTC står för _Linear TimeCode._
{% endhint %}

Du kan ta emot en LTC-tidskodsignal via vilket ljudinterface som helst på datorn, men det rekommenderas att använda ett professionellt interface med minst en justerbar XLR-ingång och möjlighet till medhörning.

Jag har haft bra erfarenhet av [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), eftersom det har hörlursmedhörning, 2 XLR-ingångar och inte kräver några särskilda drivrutiner (åtminstone på macOS). Om du bara ska använda det för tidskod kan du välja den något billigare [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (som bara har en ingång och ingen MIDI), men ärligt talat bör vilket någorlunda bra ljudinterface som helst fungera.

{% hint style="info" %}
LTC-tidskodsignaler distribueras vanligtvis via balanserade XLR-kablar, eftersom de är tillräckligt robusta för att överföra ljudsignaler med låg nivå över långa avstånd. (XLR är den runda kontakt som vanligtvis används med mikrofoner)
{% endhint %}

### Hårdvaruanslutningar

Anslut XLR-kabeln med tidskodssignalen till ditt ljudinterface och se till att du får en bra signal. Justera nivån på ljudinterfacet tills signalen är stark men inte klipper. Om ditt ljudinterface har ett hörlursuttag kan du lyssna på tidskoden och kontrollera att den inte glitchar och inte har för mycket brus.

{% hint style="info" %}
Teoretiskt är det möjligt att ta emot signalen via jackuttaget på din MacBook, men det kräver en specialkabel. Dessa uttag är vanligtvis 4-poliga TRRS-minijack, och jag är ärligt talat inte säker på vilken av kontakterna som kan användas som ljudingång. Jag är inte heller säker på vilken spänningsnivå den klarar (jag har läst någonstans att det var +/-1V, men använd detta på egen risk!)

Jag tror att du har det bättre om du bara skaffar ett billigt USB-ljudinterface i stället för att försöka med detta.
{% endhint %}

Om ditt ljudinterface inte har någon form av ingångsmedhörning kan du kontrollera i macOS systeminställningar (under _Sound_) att du får in en signal. (På Windows använder du _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS visar ingångsnivån för vilket ljudinterface som helst i systeminställningspanelen Sound</p></figcaption></figure>

### Ställa in i Liberation

1. Välj ditt ljudinterface och rätt ingångskanal i fönstret Timecode settings.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Observera att det finns separata alternativ i rullgardinsmenyn för varje ingångskanal i ditt ljudinterface

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Lägg märke till rutan till vänster. Om du tar emot en giltig tidskodsignal blir den grön. Om inte blir den röd.

2. Välj rätt bildfrekvens för den inkommande tidskoden. Den som levererar tidskoden till dig bör kunna tala om vilken bildfrekvens som används. (Om du väljer fel kommer den fortfarande att synka, men du märker ett litet ”hopp” varje sekund)
3. Öppna Timeline:s timecode-inställningar med den lilla klockikonen i timeline-raden och välj alternativet SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Justera start-offset (i timmar, minuter, sekunder, frames) så att den matchar låtens start. Om du har flera timelines behöver du ställa in dessa alternativ separat för var och en.

{% hint style="info" %}
En vanlig konvention i turnévärlden är att låta varje låt börja på en annan timme, t.ex. 01:00:00:00 för första låten, 02:00:00:00 för andra låten och så vidare.

Liberation växlar automatiskt till rätt timeline beroende på tidskoden, så du behöver aldrig byta timeline manuellt under en show.
{% endhint %}

Observera att SMPTE, till skillnad från MIDI Clock och Ableton Link, är ett _absolut_ tidssystem som mäts i timmar, minuter, sekunder och frames. Liberation:s grundläggande tidssystem bygger på beats och bars, så när du tar emot tidskod används det tempo som är inställt i timeline. Du behöver se till att detta tempo är synkat med den musik som också är synkad till tidskoden.
