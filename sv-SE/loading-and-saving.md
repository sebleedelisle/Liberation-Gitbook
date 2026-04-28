---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Läsa in och spara

Liberation sparar hela tiden sitt tillstånd till disk, så du kan vara säker på att programmet startar precis där det slutade om du skulle få strömavbrott eller ett systemproblem. Du ska aldrig behöva förlora dina zoner, din timeline eller annat innehåll.

Du kan däremot exportera din konfiguration för säkerhetskopiering och för att flytta den till en annan dator.

### Projektimport/-export

Projektfilen sparar nästan allt i din aktuella konfiguration, inklusive:

* Allt som beskrivs i [#laser-settings-import-export](loading-and-saving.md#laser-settings-import-export "mention") nedan
* Clips, effekter och gruppinställningar
* Alla dina timelines (inte ljud- och videomedia)
* Artnet-konfiguration
* Inställningar för MIDI-sändning/-mottagning
* Tempo-/synkroniseringsinställningar

Den sparar och läser för närvarande inte in:

* Inställningar för ljud- och MIDI-ingång som används i MIDI notes-noden och Sound Input Oscillator (den sparar _däremot_ inställningar för MIDI-sändning/-mottagning samt timecode-ljudingången)
* Gränssnittsskalning
* Media för Canvas guide images
* Ljud- och videomedia för timelines
* Typsnitt som används i Text-noden

{% hint style="danger" %}
Ljud- och videofiler i timeline sparas inte med projektfiler, så se till att spara dem separat om du vill flytta dem till en annan dator. Se [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Import/export av laserinställningar

* Laserinställningar för varje laser
* Beam zones
* Canvas target areas
* DMX zones
* Tilldelning av laserkontroller (och alias för eventuella kontroller som du har bytt namn på)
* Inställningar och presets för laserscanner- och färgkalibrering
* Inställningar och presets för 3D visualiser

### Clip Deck-import/-export

* Alla clips och deras zontilldelningar, inställningar och parametrar
* Alla gruppinställningar, flash mode, fade in/out-tider osv.

Den sparar och läser för närvarande inte in:

* Alla effekter och deras parametrar och inställningar

{% hint style="info" %}
**Läs in clips från en projektfil utan att läsa in hela projektet**

Om du bara vill importera clips från ett projekt väljer du _**Clips->Import Clip Deck**_ och väljer en projektfil i stället för en clip deck-fil (.cpdk).
{% endhint %}

### Append Clip Deck

Du kan lägga till clips från en exporterad clip deck-fil i ditt aktuella projekt med _Append Clip Deck_. Clips läggs till i slutet av ditt aktuella Clip Deck, men effekterna och gruppinställningarna i filen importeras inte.

### Export Selected Clips

Alla clips som är markerade just nu exporteras till en fil. Gruppinställningar och effekter sparas inte, bara clips. Observera att aktiva clips som körs för närvarande inte exporteras om de inte också är markerade.

{% hint style="info" %}
Option/Alt - shift - klicka på clips för att markera dem (eller använd lassot). Du ser vilka clips som är markerade på den tjocka vita konturen runt dem. Se [starting-stopping-clips.md](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Effektimport/-export

Läser in och sparar alla effekter tillsammans med deras gruppinställningar och parametrar.

{% hint style="info" %}
**Läs in effekter från en projektfil utan att läsa in hela projektet**

Om du bara vill importera effekterna från ett projekt väljer du _**Effects->Import Effects**_ och väljer en projektfil i stället för en effektfil (.efts).
{% endhint %}

### Timeline-export

Exportera en timeline-fil med en eller flera timelines. Observera att Clip Deck alltid inkluderas i exporterade timeline-filer (även om du kan välja vilka clips du vill importera tillbaka, se [#timeline-import](loading-and-saving.md#timeline-import "mention") nedan).

Om du har fler än en timeline i projektfilen öppnas en panel där du kan välja vilka timelines du vill exportera.

{% hint style="danger" %}
Ljud- och videofiler i timeline sparas inte med timeline-filer, så se till att spara dem separat om du vill flytta ditt innehåll till en annan dator. Se [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Timeline-import

Importera en eller flera timelines från en enda timeline-fil. När du har valt din timeline-fil öppnas en panel med flera importalternativ.

Om timeline-filen innehåller fler än en timeline listas alla. Markera de som du vill inkludera.

* Replace existing timelines\
  Tar bort alla dina aktuella timelines och ersätter dem med de importerade
* Import used clips only\
  Importerar bara de clips som används och ordnar dem i grupper, en för varje timeline. Om det här alternativet inte är valt läggs hela timeline-filens Clip Deck till efter dina befintliga clips.
* Replace existing clip deck\
  Ersätter ditt aktuella Clip Deck med clips i timeline-filen. Endast tillgängligt om _Replace existing timelines_ är valt.

{% hint style="info" %}
**Läs in timelines från en projektfil utan att läsa in hela projektet**

Om du bara vill importera timelines från ett projekt väljer du _**Timeline->Import Timeline(s)**_ och väljer en projektfil i stället för en timeline-fil (.ltml).
{% endhint %}

### DMX-/Artnet-import/-export

Sparar och läser in Artnet-noderna tillsammans med deras IP-adresser. Inkluderar även DMX zones och alla dina DMX-presets.

### Viktigt om mediafiler i timeline

Ljud- och videofiler exporteras för närvarande **inte** med timeline-filen, så om du behöver flytta innehåll till en annan dator måste du se till att ta med dem.

{% hint style="info" %}
**Så hittar en timeline mediafiler**

När timeline läses in letar den i samma mapp som timeline- eller projektfilen och söker i den och i eventuella undermappar. Så länge filerna ligger i samma mapp eller i en undermapp (till exempel _/videos_ eller _/sound_) hittar programmet dem när det läser in.
{% endhint %}
