---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Introductie tot de Clip Editor

De clipeditor is een veelzijdige manier om lasercontent te maken en vormt de kern van Liberation. Je kunt er eenvoudig simpele dingen mee maken, maar hij is ook flexibel genoeg voor bijzonder geavanceerde en complexe effecten.

{% hint style="info" %}
De node-gebaseerde editor was het eerste onderdeel van Liberation dat werd gemaakt! Het idee ontstond uit een gesprek met Rob Stanley tijdens een laserbijeenkomst in het VK in 2018, over hoe een "objectgeoriënteerde" ontwerper voor lasercontent eruit zou kunnen zien.

Hoewel het eenvoudig lijkt, is het een vrij complex systeem om te bouwen. Begin 2019 had ik echter een werkende demo die het concept bewees - en daarmee begon deze hele reis!
{% endhint %}

Het is een node-gebaseerde visuele editor (of [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) die vertrouwd zal aanvoelen als je producten zoals TouchDesigner, MaxMSP of VVVV hebt gebruikt. De clipeditor is wel iets anders en eenvoudiger, omdat hij specifiek is ontworpen voor vectorafbeeldingen.

Je kunt de Clip Editor openen door met de rechtermuisknop op de clipknop te klikken en _EDIT CLIP_ te selecteren. Of klik met de rechtermuisknop op een lege clipknop en selecteer _CREATE AND EDIT CLIP_.

### Overzicht

Wat je in de clipeditor ziet:

* De **Creator**- en **Operator node buttons** bovenaan
* De **Oscillator node buttons** aan de linkerkant
* Een preview van de content in een paneel aan de rechterkant. Als je op een node klikt, zie je een tweede preview die de content op die node zelf laat zien.
* Alle nodes en verbindingen voor de clip die je bewerkt (bij een nieuwe clip is dit leeg)
* Het Clip Editor-paneel met verschillende opties

Tijdens het bewerken zie je op de achtergrond ook hoe de clip eruitziet in de 3D visualiser.

{% hint style="info" %}
Als je geen output ziet in de 3D visualiser, moet je mogelijk de zone-knoppen gebruiken om de gewenste zones in te schakelen. Je moet er ook voor zorgen dat _Preview to lasers_ is ingeschakeld; zie [Introductie tot de Clip Editor](clip-editor-intro.md#clip-editor-panel "mention") hieronder.
{% endhint %}

### Een clip opbouwen

Meestal begin je met een of meer [creator nodes](creator-nodes.md) en verbind je van links naar rechts [Operator-nodes](operator-nodes/) die de content verwerken. Wanneer je creators en/of operators naar elkaar toe verplaatst, zul je merken dat ze automatisch met elkaar verbinden. Je kunt ze weer uit elkaar slepen om de verbinding te verbreken.

### Nodes toevoegen aan je clip

Klik en sleep vanaf een van de node-knoppen bovenaan of links naar een lege plek in de clipeditor.

### Instellingen van een node aanpassen

Klik op de knop met het tandwielpictogram (rechtsboven op de node) om het eigenschappenpaneel voor die node te openen.

### Een node in- en uitschakelen

Klik op de knop met het aan/uit-pictogram (linksboven op de node) om de node in of uit te schakelen. De node wordt gedimd om aan te geven dat hij momenteel niet actief is. Let op: content loopt nog steeds door een operator heen, ook als die is uitgeschakeld, maar de node beïnvloedt de content dan niet.

### Nodes met elkaar verbinden

Content wordt gemaakt met een creator node en wordt van links naar rechts door nodes doorgegeven; elke operator beïnvloedt de content op een bepaalde manier en geeft die door aan de volgende operator. Wat aan het einde van het pad overblijft, is de content van de clip. Creators en Operators worden automatisch met elkaar verbonden wanneer je ze dicht bij elkaar plaatst. Sleep ze weer uit elkaar om ze te scheiden.

{% hint style="info" %}
Je kunt meer dan één node verbinden met de input van de volgende node. Dit is handig om meerdere stukken content te combineren.
{% endhint %}

### Node-eigenschappen en sockets

Elke node heeft onderaan een reeks sockets. Elke socket staat voor een eigenschap binnen de node, zoals brightness, position, scale, rotation enzovoort.

[Oscillator nodes](oscillators/) kunnen van onderen met deze sockets worden verbonden en worden gebruikt om deze instellingen te animeren. Oscillator nodes hebben bovenaan een output; klik en sleep om de verbinding eruit te trekken en laat die los op een eigenschapssocket van een van de andere nodes.

### Oscillator nodes

Oscillator nodes worden gebruikt om eigenschappen in de loop van de tijd te veranderen. Meestal vertegenwoordigen ze golfvormen zoals een zaagtand- of sinusgolf, maar sommige oscillator nodes gebruiken externe inputs (zoals het inputniveau van de microfoon) als bron.

{% hint style="info" %}
Als je ooit een analoge synth hebt gebruikt, is het concept van oscillators waarschijnlijk bekend: ze worden vaak gebruikt om golfvormen te maken of het geluid in de loop van de tijd aan te passen. Oscillators in Liberation doen iets vergelijkbaars.

**Leuk weetje:** de naam _Liberation_ is geïnspireerd op de Moog Liberation, een "keytar"-synthesizer uit 1980 die bekend werd door Herbie Hancock, Jean-Michel Jarre en zelfs James Brown!
{% endhint %}

Oscillators hebben altijd _range_-instellingen die de minimale en maximale waarde bepalen van de eigenschap die wordt aangepast. _Wave Oscillators_ hebben daarnaast altijd een _duration_-instelling die bepaalt hoe snel de oscillator de waarde verandert. Zie [Golf-oscillatoren](oscillators/wave-oscillators.md "mention") voor meer informatie.

### Clip Editor-paneel

* Timer - bovenaan het paneel zie je de huidige tijd van de clip terwijl deze afspeelt
* _RETRIGGER_ - start de clip opnieuw vanaf het begin; extra handig als je clip niet loopt
* _Preview to lasers_ - als dit is aangevinkt, zie je de 3D visualiser bijwerken terwijl je deze clip bewerkt. Als je dit uitschakelt, zie je de clips die buiten de editor actief zijn. Dit is een globale instelling, niet per clip.
* _UNDO/REDO_ - voor de clipeditor zelf. Ook gekoppeld aan `Cmd / Ctrl + Z` en `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ - slaat je bewerkingen op, maar waarschuwt je voor overschrijven
* _SAVE AS A COPY_ - slaat je clip op in de eerstvolgende beschikbare slot in de Clip Deck. Dit wordt de nieuwe positie voor je clip en alle volgende saves worden op deze nieuwe plek opgeslagen.
* _EXIT EDITOR_ - sluit de clipeditor. Als je niet-opgeslagen wijzigingen hebt, krijg je een bevestigingspaneel.
