---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Laste inn og lagre

Liberation lagrer kontinuerlig tilstanden sin til disk, slik at du kan være trygg på at programmet starter der det slapp hvis du får strømbrudd eller et systemproblem. Du skal ikke miste soner, tidslinjer eller annet innhold.

Du kan også eksportere oppsettet ditt for sikkerhetskopi eller for å overføre det til en annen datamaskin.

### Import/eksport av prosjekt

Prosjektfilen lagrer nesten alt i det gjeldende oppsettet, inkludert:

* Alt som er beskrevet i [Laste inn og lagre](loading-and-saving.md#laser-settings-import-export "mention") nedenfor
* Klipp, effekter og gruppeinnstillinger
* Alle tidslinjene dine (ikke inkludert lyd- og videomedier)
* Art-Net-oppsett
* Innstillinger for sending/mottak av MIDI
* Innstillinger for tempo/synkronisering

Den lagrer og laster for øyeblikket ikke:

* Lyd- og MIDI-inngangsinnstillinger slik de brukes i MIDI notes node og Sound Input Oscillator (den _lagrer_ også MIDI-innstillinger for sending/mottak, samt lydinngang for timecode)
* Grensesnittskalering
* Medier for Canvas guidebilder
* Lyd- og videomedier for tidslinjer
* Skrifter som brukes i Text node

{% hint style="danger" %}
Lyd- og videofiler i tidslinjen lagres ikke med prosjektfiler, så husk å lagre dem separat hvis du vil overføre til en annen datamaskin. Se [Laste inn og lagre](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Import/eksport av laserinnstillinger

* Laserinnstillinger for hver laser
* Beam-soner
* Målområder i Canvas
* DMX-soner
* Tilordning av laserkontroller (og aliaser for kontrollere du har gitt nytt navn)
* Innstillinger og forhåndsinnstillinger for laserskanner og fargekalibrering
* Innstillinger og forhåndsinnstillinger for 3D-visualisering

### Import/eksport av Clip Deck

* Alle klipp og deres sonetilordninger, innstillinger og parametere
* Alle gruppeinnstillinger, flash mode, fade in/out-tider osv.

Den lagrer og laster for øyeblikket ikke:

* Alle effekter og deres parametere og innstillinger

{% hint style="info" %}
**Last inn klipp fra en prosjektfil uten å laste inn hele prosjektet**

For å importere bare klippene fra et prosjekt velger du _**Clips->Import Clip Deck**_, og i stedet for å velge en Clip Deck-fil (.cpdk), velger du en prosjektfil.
{% endhint %}

### Append Clip Deck

Du kan legge til klipp fra en eksportert Clip Deck-fil i det gjeldende prosjektet med _Append Clip Deck_. Klipp legges til på slutten av din nåværende Clip Deck, men effektene og gruppeinnstillingene i filen importeres ikke.

### Export Selected Clips

Alle klipp som er valgt, eksporteres til en fil. Gruppeinnstillinger og effekter lagres ikke, bare klippene. Merk at aktive klipp som kjører, ikke eksporteres med mindre de også er valgt.

{% hint style="info" %}
Option/Alt - shift - klikk på klipp for å velge dem (eller bruk lassoen). Du ser hvilke klipp som er valgt, på den tykke hvite omrisset rundt dem. Se [Starte / stoppe clips](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Import/eksport av effekter

Laster inn og lagrer alle effekter sammen med gruppeinnstillinger og parametere.

{% hint style="info" %}
**Last inn effekter fra en prosjektfil uten å laste inn hele prosjektet**

For å importere bare effektene fra et prosjekt velger du _**Effects->Import Effects**_, og i stedet for å velge en effektfil (.efts), velger du en prosjektfil.
{% endhint %}

### Eksport av tidslinje

Eksporter en tidslinjefil med én eller flere tidslinjer. Merk at Clip Deck alltid inkluderes i eksporterte tidslinjefiler (selv om du kan velge hvilke Clips du vil importere tilbake, se [Laste inn og lagre](loading-and-saving.md#timeline-import "mention") nedenfor)

Hvis du har mer enn én tidslinje i prosjektfilen, åpnes et panel der du kan velge hvilke tidslinjer du vil eksportere.

{% hint style="danger" %}
Lyd- og videofiler i tidslinjen lagres ikke med tidslinjefiler, så husk å lagre dem separat hvis du vil overføre innholdet til en annen datamaskin. Se [Laste inn og lagre](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Import av tidslinje

Importer én eller flere tidslinjer fra én enkelt tidslinjefil. Når du har valgt tidslinjefilen, åpnes et panel med flere importvalg.

Hvis tidslinjefilen har mer enn én tidslinje, vises alle i listen. Huk av de du vil inkludere.

* Replace existing timelines\
  Sletter alle de gjeldende tidslinjene dine og erstatter dem med de importerte
* Import used clips only\
  Importerer bare klippene som brukes, og ordner klippene i grupper, én for hver tidslinje. Hvis dette valget ikke er aktivert, legges hele Clip Deck fra tidslinjefilen til de eksisterende klippene dine.
* Replace existing clip deck\
  Erstatter din nåværende Clip Deck med klippene i tidslinjefilen. Bare tilgjengelig hvis _Replace existing timelines_ er valgt.

{% hint style="info" %}
**Last inn tidslinjer fra en prosjektfil uten å laste inn hele prosjektet**

For å importere bare tidslinjene fra et prosjekt velger du _**Timeline->Import Timeline(s)**_, og i stedet for å velge en tidslinjefil (.ltml), velger du en prosjektfil.
{% endhint %}

### Import/eksport av DMX / Art-Net

Lagrer og laster Art-Net-nodene, sammen med IP-adressene deres. Inkluderer også DMX-sonene og alle DMX-forhåndsinnstillingene dine.

### Viktig merknad om mediefiler for tidslinjer

Lyd- og videofiler eksporteres for øyeblikket **ikke** med tidslinjefilen, så hvis du må flytte innhold til en annen datamaskin, må du passe på å ta med disse.

{% hint style="info" %}
**Hvordan en tidslinje ser etter mediefiler**

Når tidslinjen lastes inn, ser den i samme mappe som tidslinje- eller prosjektfilen og søker i den og eventuelle undermapper. Så lenge filene ligger i samme mappe eller en undermappe (for eksempel _/videos_ eller _/sound_), finner den dem når den lastes inn.
{% endhint %}
