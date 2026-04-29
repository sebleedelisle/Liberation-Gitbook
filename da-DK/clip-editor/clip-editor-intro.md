---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Introduktion til Clip Editor

Clip Editor er en alsidig måde at skabe laserindhold på, og den er kernen i Liberation. Det er nemt at lave enkle ting, men samtidig fleksibelt nok til at lave utroligt avancerede og komplekse effekter.

{% hint style="info" %}
Den nodebaserede editor var den første del af Liberation, der blev lavet! Den udsprang af en samtale med Rob Stanley ved et britisk lasertræf i 2018 om, hvordan en "objektorienteret" designer til laserindhold kunne se ud.

Selvom den virker enkel, er det et ret komplekst system at bygge, men i starten af 2019 havde jeg en fungerende demo, der beviste konceptet – og det satte hele denne rejse i gang!
{% endhint %}

Det er en nodebaseret visuel editor (eller [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)), som vil føles bekendt, hvis du har brugt produkter som TouchDesigner, MaxMSP eller VVVV. Clip Editor er dog lidt anderledes og noget enklere, fordi den er designet specifikt til vektorgrafik.

Du kan åbne Clip Editor ved at højreklikke på clip-knappen og vælge _EDIT CLIP_. Eller højreklik på en tom clip-knap, og vælg _CREATE AND EDIT CLIP_.

### Oversigt

Det, du ser i Clip Editor:

* Knapperne til **Creator**- og **Operator-noder** langs toppen
* Knapperne til **Oscillator-noder** langs venstre side
* En forhåndsvisning af indholdet i et panel til højre, og hvis du klikker på en node, ser du en ekstra forhåndsvisning, der viser indholdet ved selve noden.
* Alle noder og forbindelser for det clip, du redigerer (hvis det er et nyt clip, er området tomt)
* Clip Editor-panelet med forskellige indstillinger

Mens du redigerer, kan du også se, hvordan clippet ser ud i 3D Visualiser i baggrunden.

{% hint style="info" %}
Hvis du ikke ser noget output i 3D Visualiser, skal du muligvis bruge zoneknapperne til at aktivere de zoner, du vil bruge. Du skal også sikre dig, at _Preview to lasers_ er slået til. Se [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel "mention") nedenfor.
{% endhint %}

### Opbygning af et clip

Du starter typisk med en eller flere [creator-noder](creator-nodes.md) og forbinder [Operatornoder](operator-nodes/) fra venstre mod højre, som behandler indholdet. Når du flytter creators og/eller operators tæt på hinanden, vil du bemærke, at de automatisk forbindes. Du kan trække dem fra hinanden igen for at afbryde forbindelsen.

### Tilføjelse af noder til dit clip

Klik og træk fra en af nodeknapperne langs toppen eller venstre side ind i et tomt område i Clip Editor.

### Justering af indstillinger for en node

Klik på tandhjulsikonet (øverst til højre på noden) for at åbne egenskabspanelet for den node.

### Aktivering og deaktivering af en node

Klik på tænd/sluk-ikonet (øverst til venstre på noden) for at aktivere og deaktivere noden. Noden bliver nedtonet for at vise, at den ikke er aktiv i øjeblikket. Bemærk, at indhold stadig passerer gennem en operator, selvom den er deaktiveret, men noden påvirker ikke indholdet.

### Forbindelse af noder

Indhold laves med en creator-node og sendes videre gennem noder fra venstre mod højre; hver operator påvirker indholdet på en eller anden måde og sender det videre til den næste operator. Det, der er tilbage ved slutningen af kæden, er clippets indhold. Creators og Operators forbindes automatisk med hinanden, når du flytter dem tæt på hinanden. For at adskille dem skal du trække dem fra hinanden igen.

{% hint style="info" %}
Du kan forbinde mere end én node til den næste nodes input. Det er nyttigt, når du vil kombinere flere stykker indhold.
{% endhint %}

### Nodeegenskaber og sockets

Hver node har en række sockets langs bunden, og hver af dem repræsenterer en egenskab i noden, f.eks. lysstyrke, position, skalering, rotation osv.

[Oscillator-noder](oscillators/) kan forbindes til disse sockets nedefra og bruges til at animere disse indstillinger. Oscillator-noder har et output øverst. Klik og træk for at trække forbindelsen ud, og slip den i en af de andre noders property sockets.

### Oscillator-noder

Oscillator-noder bruges til at ændre egenskaber over tid. De repræsenterer typisk bølgeformer som f.eks. en savtaks- eller sinusbølge, men nogle oscillator-noder bruger eksterne input (f.eks. mikrofonens inputniveau) som kilde.

{% hint style="info" %}
Hvis du nogensinde har brugt en analog synth, kender du sikkert konceptet med oscillatorer, som ofte bruges til at skabe bølgeformer eller justere lyden over tid. Oscillatorer i Liberation gør noget tilsvarende.

**Sjov detalje:** navnet _Liberation_ er inspireret af Moog Liberation, en "keytar"-synthesizer udgivet i 1980 og gjort berømt af Herbie Hancock, Jean-Michel Jarre og endda James Brown!
{% endhint %}

Oscillatorer har altid _range_-indstillinger, der styrer minimums- og maksimumsværdien for den egenskab, der skal justeres. Og _Wave Oscillators_ har altid en _duration_-indstilling, der bestemmer, hvor hurtigt oscillatoren ændrer værdien. Se [Wave oscillators](oscillators/wave-oscillators.md "mention") for flere oplysninger.

### Clip Editor-panel

* Timer – øverst i panelet ser du den aktuelle tid for clippet, efterhånden som det afspilles
* _RETRIGGER_ – starter clippet forfra; ekstra nyttigt, hvis dit clip ikke looper
* _Preview to lasers_ – når denne er markeret, ser du 3D Visualiser blive opdateret, mens du redigerer dette clip. Hvis du slår den fra, ser du de clips, der kører uden for editoren. Dette er en global indstilling, ikke en indstilling pr. clip.
* _UNDO/REDO_ – for selve Clip Editor. Er også knyttet til `Cmd / Ctrl + Z` og `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ – gemmer dine ændringer, men advarer dig om overskrivning
* _SAVE AS A COPY_ – gemmer dit clip i den næste ledige plads i Clip Deck. Dette bliver den nye placering for dit clip, og alle efterfølgende gemninger sker på denne nye placering.
* _EXIT EDITOR_ – lukker Clip Editor. Hvis du har ugemte ændringer, får du vist et bekræftelsespanel.
