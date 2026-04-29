---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Indlæsning og lagring

Liberation gemmer løbende sin tilstand på disken, så du kan være sikker på, at hvis der opstår strømafbrydelse eller et systemproblem, starter det op præcis dér, hvor det slap. Du bør aldrig miste dine zones, timeline eller andet indhold.

Du kan dog eksportere din opsætning som backup eller for at overføre den til en anden computer.

### Import/eksport af projekt

Project-filen gemmer næsten alt i din aktuelle opsætning, herunder:

* Alt det, der er beskrevet i [Indlæsning og lagring](loading-and-saving.md#laser-settings-import-export "mention") nedenfor
* Clips, effects og group settings
* Alle dine timelines (ikke inklusive audio- og videomedier)
* Art-Net-opsætning
* MIDI send/receive settings
* Tempo-/synkroniseringsindstillinger

Den gemmer og indlæser i øjeblikket ikke:

* Sound- og MIDI input-indstillinger, som bruges i MIDI notes-noden og Sound Input Oscillator (den gemmer _dog_ MIDI send/receive settings samt timecode sound input)
* Interface-skalering
* Medier til Canvas guide images
* Sound- og videomedier til timelines
* Skrifttyper, der bruges i Text-noden

{% hint style="danger" %}
Sound- og videofiler i timeline gemmes ikke sammen med project files, så sørg for at gemme dem separat, hvis du vil overføre til en anden computer. Se [Indlæsning og lagring](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Import/eksport af laserindstillinger

* Laser settings for hver laser
* Beam zones
* Canvas target areas
* DMX zones
* Tildeling af lasercontroller (og aliases for de controllere, du har omdøbt)
* Indstillinger og presets for laserscanner og farvekalibrering
* Indstillinger og presets for 3D Visualiser

### Import/eksport af Clip Deck

* Alle clips og deres zone-tildelinger, indstillinger og parametre
* Alle group settings, flash mode, fade in/out-tider osv.

Den gemmer og indlæser i øjeblikket ikke:

* Alle effects og deres parametre og indstillinger

{% hint style="info" %}
**Indlæs clips fra en project file uden at indlæse hele projektet**

Hvis du kun vil importere clips fra et projekt, skal du vælge _**Clips->Import Clip Deck**_ og vælge en project file i stedet for en clip deck-fil (.cpdk).
{% endhint %}

### Tilføj Clip Deck

Du kan tilføje clips fra en eksporteret Clip Deck-fil til dit aktuelle projekt med _Append Clip Deck_. Clips tilføjes i slutningen af dit aktuelle Clip Deck, men effects og group settings i filen importeres ikke.

### Eksportér valgte clips

Alle clips, der aktuelt er valgt, eksporteres til en fil. Group settings og effects gemmes ikke, kun clips. Bemærk, at aktive clips, der kører lige nu, ikke eksporteres, medmindre de også er valgt.

{% hint style="info" %}
Option/Alt - Shift - klik på clips for at vælge dem (eller brug lassoen). Du kan se, hvilke clips der er valgt, på den tykke hvide kontur omkring dem. Se [Start / stop af clips](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Import/eksport af Effects

Indlæser og gemmer alle effects sammen med deres group settings og parametre.

{% hint style="info" %}
**Indlæs effects fra en project file uden at indlæse hele projektet**

Hvis du kun vil importere effects fra et projekt, skal du vælge _**Effects->Import Effects**_ og vælge en project file i stedet for en effects-fil (.efts).
{% endhint %}

### Eksport af Timeline

Eksportér en timeline-fil med én eller flere timelines. Bemærk, at Clip Deck altid inkluderes i eksporterede timeline-filer (selvom du kan vælge præcist, hvilke clips du importerer igen, se [Indlæsning og lagring](loading-and-saving.md#timeline-import "mention") nedenfor).

Hvis du har mere end én timeline i din project file, åbnes et panel, hvor du kan vælge, hvilke timelines du vil eksportere.

{% hint style="danger" %}
Sound- og videofiler i timeline gemmes ikke sammen med timeline-filer, så sørg for at gemme dem separat, hvis du vil overføre dit indhold til en anden computer. Se [Indlæsning og lagring](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Import af Timeline

Importér én eller flere timelines fra en enkelt timeline-fil. Når du har valgt din timeline-fil, åbnes et panel med flere importindstillinger.

Hvis timeline-filen indeholder mere end én timeline, vises de alle på listen. Markér dem, du vil inkludere.

* Replace existing timelines\
  Sletter alle dine aktuelle timelines og erstatter dem med de importerede
* Import used clips only\
  Importerer kun de clips, der bruges, og arrangerer clips i groups, én for hver timeline. Hvis denne indstilling ikke er valgt, tilføjes hele timeline-filens Clip Deck til dine eksisterende clips.
* Replace existing clip deck\
  Erstatter dit aktuelle Clip Deck med clips i timeline-filen. Kun tilgængelig, hvis _Replace existing timelines_ er valgt.

{% hint style="info" %}
**Indlæs timelines fra en project file uden at indlæse hele projektet**

Hvis du kun vil importere timelines fra et projekt, skal du vælge _**Timeline->Import Timeline(s)**_ og vælge en project file i stedet for en timeline-fil (.ltml).
{% endhint %}

### Import/eksport af DMX / Art-Net

Gemmer og indlæser Art-Net-noderne sammen med deres IP-adresser. Inkluderer også DMX zones og alle dine DMX presets.

### Vigtig bemærkning om timeline-mediefiler

Sound- og videofiler eksporteres i øjeblikket **ikke** sammen med timeline-filen, så hvis du skal flytte indhold til en anden computer, skal du sørge for at inkludere dem.

{% hint style="info" %}
**Sådan finder en timeline mediefiler**

Når timeline indlæses, kigger den i samme mappe som timeline- eller project-filen og søger i den samt i eventuelle undermapper. Så længe filerne ligger i samme mappe eller i en undermappe (f.eks. _/videos_ eller _/sound_), finder den dem ved indlæsning.
{% endhint %}
