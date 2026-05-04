---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Introduksjon til Clip Editor

Clip Editor er en allsidig måte å lage laserinnhold på, og den er en sentral del av Liberation. Det er enkelt å lage enkle ting, men samtidig fleksibelt nok til å lage svært avanserte og komplekse effekter.

{% hint style="info" %}
Den nodebaserte editoren var den første delen av Liberation som ble laget! Den oppsto etter en samtale med Rob Stanley på et britisk lasertreff i 2018 om hvordan en «objektorientert» designer for laserinnhold kunne se ut.

Selv om den virker enkel, er det et ganske komplekst system å bygge, men ved starten av 2019 hadde jeg en fungerende demo som beviste konseptet – og det startet hele denne reisen!
{% endhint %}

Dette er en nodebasert visuell editor (eller [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) som vil virke kjent hvis du har brukt produkter som TouchDesigner, MaxMSP eller VVVV. Clip Editor er likevel litt annerledes og noe enklere, siden den er laget spesielt for vektorgrafikk.

Du kan åpne Clip Editor ved å høyreklikke på Clip-knappen og velge _EDIT CLIP_. Eller høyreklikk på en tom Clip-knapp og velg _CREATE AND EDIT CLIP_.

### Oversikt

Dette ser du i Clip Editor:

* **Creator**- og **Operator node buttons** langs toppen
* **Oscillator node buttons** langs venstre side
* En forhåndsvisning av innholdet i et panel til høyre. Hvis du klikker på en node, ser du også en ekstra forhåndsvisning som viser innholdet ved selve noden.
* Alle nodene og koblingene for klippet du redigerer (hvis det er et nytt klipp, er dette tomt)
* Clip Editor-panelet med ulike alternativer

Mens du redigerer, ser du også hvordan klippet ser ut i 3D Visualiser i bakgrunnen.

{% hint style="info" %}
Hvis du ikke ser noe output i 3D Visualiser, må du kanskje bruke zone-knappene til å slå på sonene du vil bruke. Du må også kontrollere at _Preview to lasers_ er aktivert. Se [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel "mention") nedenfor.
{% endhint %}

### Bygge et klipp

Du starter vanligvis med én eller flere [creator-noder](creator-nodes.md), og kobler [Operator-noder](operator-nodes/) fra venstre mot høyre for å behandle innholdet. Når du flytter creators og/eller operators sammen, vil du se at de automatisk kobles til hverandre. Du kan dra dem fra hverandre igjen for å koble dem fra.

### Legge til noder i klippet

Klikk og dra fra en av node-knappene langs toppen eller venstre side til et tomt område i Clip Editor.

### Justere innstillinger for en node

Klikk på tannhjulikonet (øverst til høyre på noden) for å åpne egenskapspanelet for den noden.

### Aktivere og deaktivere en node

Klikk på strømikonet (øverst til venstre på noden) for å aktivere og deaktivere noden. Noden blir nedtonet for å vise at den ikke er aktiv for øyeblikket. Merk at innhold fortsatt går gjennom en operator selv om den er deaktivert, men noden påvirker ikke innholdet.

### Koble noder sammen

Innhold lages med en creator-node og sendes videre gjennom noder fra venstre mot høyre. Hver operator påvirker innholdet på en eller annen måte og sender det videre til neste operator. Det som er igjen ved enden av banen, er klippets innhold. Creators og Operators kobles automatisk til hverandre når du flytter dem nær hverandre. Dra dem fra hverandre igjen for å skille dem.

{% hint style="info" %}
Du kan koble mer enn én node inn i inngangen på neste node. Dette er nyttig for å kombinere flere deler med innhold.
{% endhint %}

### Nodeegenskaper og sockets

Hver node har en rekke sockets langs bunnen, og hver av dem representerer en egenskap i noden, for eksempel brightness, position, scale, rotation osv.

[Oscillator-noder](oscillators/) kan kobles til disse socketene nedenfra og brukes til å animere disse innstillingene. Oscillator-noder har en output øverst. Klikk og dra for å trekke ut koblingen, og slipp den i en av egenskapssocketene på de andre nodene.

### Oscillator-noder

Oscillator-noder brukes til å endre egenskaper over tid. De representerer vanligvis bølgeformer, for eksempel sagtann- eller sinusbølger, men noen oscillator-noder bruker eksterne innganger (for eksempel nivået på mikrofoninngangen) som kilde.

{% hint style="info" %}
Hvis du noen gang har brukt en analog synth, kjenner du til konseptet oscillatorer, som ofte brukes til å lage bølgeformer eller justere lyden over tid. Oscillatorer i Liberation gjør en lignende jobb.

**Fun fact:** navnet _Liberation_ var inspirert av Moog Liberation, en «keytar»-synthesizer som ble lansert i 1980 og gjort kjent av Herbie Hancock, Jean-Michel Jarre og til og med James Brown!
{% endhint %}

Oscillatorer har alltid _range_-innstillinger som styrer minimums- og maksimumsverdien for egenskapen som skal justeres. _Wave Oscillators_ har alltid en _duration_-innstilling som bestemmer hvor raskt oscillatoren endrer verdien. Se [Bølgeoscillatorer](oscillators/wave-oscillators.md "mention") for mer informasjon.

### Clip Editor-panel

* Timer – øverst i panelet ser du gjeldende tid for klippet mens det går
* _RETRIGGER_ – starter klippet på nytt fra begynnelsen; ekstra nyttig hvis klippet ikke looper
* _Preview to lasers_ – når dette er avkrysset, ser du at 3D Visualiser oppdateres mens du redigerer dette klippet. Hvis du slår det av, ser du klippene som kjører utenfor editoren. Dette er en global innstilling, ikke per klipp.
* _UNDO/REDO_ – for selve Clip Editor. Er også tilordnet `Cmd / Ctrl + Z` og `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ – lagrer endringene dine, men advarer deg om overskriving
* _SAVE AS A COPY_ – lagrer klippet ditt på neste ledige plass i Clip Deck. Dette blir den nye plasseringen for klippet, og alle senere lagringer skjer på dette nye stedet.
* _EXIT EDITOR_ – lukker Clip Editor. Hvis du har ulagrede endringer, får du opp et bekreftelsespanel.
