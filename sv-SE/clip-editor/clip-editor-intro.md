---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Introduktion till Clip Editor

Clip Editor är ett mångsidigt sätt att skapa laserinnehåll och är en central del av Liberation. Det är enkelt att skapa enkla saker, men samtidigt tillräckligt flexibelt för att skapa mycket avancerade och komplexa effekter.

{% hint style="info" %}
Den nodbaserade editorn var den första delen av Liberation som byggdes! Den föddes ur ett samtal med Rob Stanley på en laserträff i Storbritannien 2018 om hur en ”objektorienterad” designer för laserinnehåll skulle kunna se ut.

Även om den verkar enkel är det ett ganska komplext system att bygga, men i början av 2019 hade jag en fungerande demo som bevisade konceptet – och det var starten på hela den här resan!
{% endhint %}

Det är en nodbaserad visuell editor (eller [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) som känns bekant om du har använt produkter som TouchDesigner, MaxMSP eller VVVV. Clip Editor är dock lite annorlunda och något enklare, eftersom den är särskilt utformad för vektorgrafik.

Du kan öppna Clip Editor genom att högerklicka på Clip-knappen och välja _EDIT CLIP_. Eller högerklicka på en tom Clip-knapp och välj _CREATE AND EDIT CLIP_.

### Översikt

Det du ser i Clip Editor:

* Knapparna för **Creator**- och **Operator-noder** längst upp
* Knapparna för **Oscillator-noder** längs vänster sida
* En förhandsvisning av innehållet i en panel till höger, och om du klickar på en nod visas en andra förhandsvisning som visar innehållet vid själva noden.
* Alla noder och anslutningar för den Clip du redigerar (om det är en ny Clip är detta tomt)
* Clip Editor-panelen med olika alternativ

Medan du redigerar ser du också hur Clip ser ut i 3D Visualiser i bakgrunden.

{% hint style="info" %}
Om du inte ser någon output i 3D Visualiser kan du behöva använda zone-knapparna för att slå på de zoner du vill använda. Du behöver också se till att _Preview to lasers_ är aktiverat, se [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel "mention") nedan.
{% endhint %}

### Bygga en Clip

Du börjar vanligtvis med en eller flera [creator nodes](creator-nodes.md) och ansluter [operators](operator-nodes/) från vänster till höger som bearbetar innehållet. När du flyttar creators och/eller operators tillsammans märker du att de automatiskt ansluts till varandra. Du kan dra isär dem för att koppla från dem igen.

### Lägga till noder i din Clip

Klicka och dra från en av nodknapparna längst upp eller till vänster till en tom yta i Clip Editor.

### Justera inställningar för en nod

Klicka på kugghjulsikonen (uppe till höger på noden) för att öppna egenskapspanelen för den noden.

### Aktivera och inaktivera en nod

Klicka på strömikonen (uppe till vänster på noden) för att aktivera och inaktivera noden. Noden tonas ned för att visa att den inte är aktiv just nu. Observera att innehåll fortfarande passerar genom en operator även om den är inaktiverad, men noden påverkar inte innehållet.

### Ansluta noder till varandra

Innehåll skapas med en creator node och skickas vidare genom noder från vänster till höger. Varje operator påverkar innehållet på något sätt och skickar det vidare till nästa operator. Det som finns kvar i slutet av kedjan är innehållet i Clip. Creators och Operators ansluts automatiskt till varandra när du flyttar dem nära varandra. Dra isär dem igen för att separera dem.

{% hint style="info" %}
Du kan ansluta mer än en nod till nästa nods input. Det är användbart när du vill kombinera flera delar av innehåll
{% endhint %}

### Nodegenskaper och sockets

Varje nod har en rad sockets längs nederkanten, och var och en representerar en egenskap i noden, till exempel brightness, position, scale, rotation osv.

[Oscillator nodes](oscillators/) kan anslutas till dessa sockets underifrån och användas för att animera inställningarna. Oscillator nodes har en output upptill. Klicka och dra för att dra ut anslutningen och släpp den i en av de andra nodernas egenskapssockets.

### Oscillator nodes

Oscillator nodes används för att ändra egenskaper över tid. De representerar vanligtvis vågformer, till exempel sågtandsvåg eller sinusvåg, men vissa oscillator nodes använder externa inputs (till exempel nivån från mikrofoningången) som källa.

{% hint style="info" %}
Om du någon gång har använt en analog synth känner du igen begreppet oscillatorer, som ofta används för att skapa vågformer eller justera ljudet över tid. Oscillatorer i Liberation gör ungefär samma sak.

**Kul fakta:** namnet _Liberation_ inspirerades av Moog Liberation, en ”keytar”-synthesizer som släpptes 1980 och blev känd genom Herbie Hancock, Jean-Michel Jarre och till och med James Brown!
{% endhint %}

Oscillatorer har alltid _range_-inställningar som styr det minsta och största värdet för egenskapen som ska justeras. Och _Wave Oscillators_ har alltid en _duration_-inställning som avgör hur snabbt oscillatorn ändrar värdet. Se [wave-oscillators.md](oscillators/wave-oscillators.md "mention") för mer information.

### Clip Editor-panelen

* Timer – längst upp i panelen ser du den aktuella tiden för Clip medan den spelas upp
* _RETRIGGER_ – startar om Clip från början; extra användbart om din Clip inte loopar
* _Preview to lasers_ – när detta är markerat ser du 3D Visualiser uppdateras medan du redigerar denna Clip. Om du stänger av det ser du de Clips som körs utanför editorn. Detta är en global inställning, inte en inställning per Clip.
* _UNDO/REDO_ – för Clip Editor själv. Är också mappat till `Cmd / Ctrl + Z` och `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ – sparar dina ändringar men varnar dig innan något skrivs över
* _SAVE AS A COPY_ – sparar din Clip på nästa lediga plats i Clip Deck. Detta blir den nya positionen för din Clip och alla efterföljande sparningar görs på den nya platsen.
* _EXIT EDITOR_ – stänger Clip Editor. Om du har osparade ändringar visas en bekräftelsepanel.
