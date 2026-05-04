---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation understøtter synkronisering med et eksternt SMPTE/LTC-timecodesignal, som ofte bruges i livemusikshows til at holde lys, pyro, video og backing tracks i takt.

{% hint style="info" %}
Hvad er SMPTE/LTC?

SMPTE er en standard for timecode, og LTC er denne timecode konverteret til et lydsignal. Hvis du lytter til lyden, lyder det som en forfærdelig, højfrekvent hylen, men for computere er det timinginformation i høj opløsning.

**Nørdefakta!**

Historisk er SMPTE blevet brugt til at holde video og lyd synkroniseret, eller ved synkronisering til analogt bånd kunne et spor have timecode-lyden optaget på sig, nogle gange kaldet at "stripe" båndet. Du kunne bruge dette timecode-spor til at holde flere båndmaskiner synkroniseret med hinanden, eller til at holde en MIDI-sequencer synkroniseret med båndet. (Så du behøvede ikke at optage MIDI-instrumenter på bånd; du kunne bare lade sequenceren spille dem live, mens du mixede!)

SMPTE står for Society of Motion Picture and Television Engineers, som definerede standarden. LTC står for _Linear TimeCode._
{% endhint %}

Du kan modtage et LTC-timecodesignal via ethvert lydinterface på din computer, men det anbefales at bruge et professionelt interface med mindst én justerbar XLR-indgang og mulighed for monitoring.

Jeg har haft gode erfaringer med [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), da det har hovedtelefonmonitoring, 2 XLR-indgange og ikke kræver særlige drivere (i hvert fald på macOS). Hvis du kun skal bruge det til timecode, kan du vælge den lidt billigere [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (som kun har én indgang og ingen MIDI), men helt ærligt burde ethvert nogenlunde godt lydinterface fungere.

{% hint style="info" %}
LTC-timecodesignaler distribueres typisk via balancerede XLR-kabler, da de er robuste nok til at transmittere lydsignaler med lavt niveau over lange afstande. (XLR er det runde stik, der normalt bruges til mikrofoner)
{% endhint %}

### Hardwareforbindelser

Sæt XLR-kablet med timecodesignalet i dit lydinterface, og sørg for, at du får et godt signal. Juster niveauet på lydinterfacet, indtil signalet er kraftigt, men ikke clipper. Hvis dit lydinterface har et hovedtelefonstik, kan du lytte til timecoden og sikre dig, at den ikke glitcher og ikke har for meget støj.

{% hint style="info" %}
Teoretisk er det muligt at modtage signalet via jackstikket på din MacBook, men det kræver et specialkabel. Disse stik er typisk 4-polede TRRS-minijacks, og jeg er ærligt talt ikke sikker på, hvilke af disse forbindelser der kan bruges som lydindgang, og jeg er heller ikke sikker på, hvilket spændingsniveau den kan håndtere (jeg har læst et sted, at det var +/-1V, men brug det på eget ansvar!)

Jeg tror, du er bedre stillet ved bare at skaffe et billigt USB-lydinterface i stedet for at forsøge dette.
{% endhint %}

Hvis dit lydinterface ikke har nogen form for input-monitoring, kan du tjekke i macOS-systemindstillingerne (under _Sound_) for at sikre dig, at du får et signal. (På Windows skal du bruge _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS viser inputniveauet for ethvert lydinterface i panelet Sound i systemindstillingerne</p></figcaption></figure>

### Opsætning i Liberation

1. Vælg dit lydinterface og den korrekte inputkanal i vinduet Timecode settings.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Bemærk, at der er separate valgmuligheder i rullemenuen for hver inputkanal i dit lydinterface

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Læg mærke til firkanten til venstre. Hvis du modtager et gyldigt timecodesignal, bliver den grøn. Hvis ikke, er den rød.

2. Vælg den korrekte framerate for den indgående timecode. Den, der leverer timecode til dig, bør kunne fortælle dig, hvad frameraten er. (Hvis du vælger forkert, synkroniserer den stadig, men du vil bemærke et lille "hop" hvert sekund)
3. Åbn Timeline's timecode settings ved hjælp af det lille ur-ikon på timeline-bjælken, og vælg indstillingen SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Juster start offset (i timer, minutter, sekunder, frames), så den passer til sangens start. Hvis du har flere timelines, skal du indstille disse muligheder separat for hver enkelt.

{% hint style="info" %}
Det er en almindelig konvention i touring-verdenen, at hver sang starter ved en ny time, dvs. 01:00:00:00 for den første sang, 02:00:00:00 for den anden sang osv.

Liberation skifter automatisk til den timeline, der passer til timecoden, så du behøver aldrig manuelt at skifte timelines under et show.
{% endhint %}

Bemærk, at SMPTE i modsætning til MIDI Clock og Ableton Link er et _absolut_ tidssystem, målt i timer, minutter, sekunder og frames. Liberations centrale tidssystem er baseret på beats og bars, så når du modtager timecode, bruger det det tempo, der er angivet i timeline. Du skal sikre dig, at dette tempo er synkroniseret med den musik, der også er synkroniseret til timecoden.
