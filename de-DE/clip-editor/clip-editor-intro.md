---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Einführung in den Clip Editor

Der Clip Editor ist eine vielseitige Möglichkeit, Laser-Content zu erstellen, und bildet das Herzstück von Liberation. Einfache Dinge lassen sich schnell bauen, gleichzeitig ist er flexibel genug für erstaunlich anspruchsvolle und komplexe Effekte.

{% hint style="info" %}
Der nodebasierte Editor war der erste Teil von Liberation, der entwickelt wurde! Er entstand aus einem Gespräch mit Rob Stanley bei einem Laser-Meet-up in Großbritannien im Jahr 2018 darüber, wie ein „objektorientierter“ Designer für Laser-Content aussehen könnte.

Auch wenn er einfach wirkt, ist es ein ziemlich komplexes System. Anfang 2019 hatte ich aber eine funktionierende Demo, die das Konzept bewiesen hat – und damit begann diese ganze Reise!
{% endhint %}

Es ist ein nodebasierter visueller Editor (oder eine [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)), der dir bekannt vorkommen wird, wenn du Produkte wie TouchDesigner, MaxMSP oder VVVV verwendet hast. Der Clip Editor ist allerdings etwas anders und auch etwas einfacher, da er speziell für Vektorgrafiken entwickelt wurde.

Du kannst den Clip Editor öffnen, indem du mit der rechten Maustaste auf den Clip-Button klickst und _EDIT CLIP_ auswählst. Oder klicke mit der rechten Maustaste auf einen leeren Clip-Button und wähle _CREATE AND EDIT CLIP_.

### Überblick

Im Clip Editor siehst du:

* die **Creator**- und **Operator**-Node-Buttons oben
* die **Oscillator**-Node-Buttons links
* eine Vorschau des Contents in einem Panel rechts; wenn du auf eine Node klickst, siehst du eine zweite Vorschau, die dir den Content direkt an dieser Node zeigt
* alle Nodes und Verbindungen für den Clip, den du gerade bearbeitest (bei einem neuen Clip ist dieser Bereich leer)
* das Clip Editor panel mit verschiedenen Optionen

Während der Bearbeitung siehst du im Hintergrund außerdem, wie der Clip im 3D Visualiser aussieht.

{% hint style="info" %}
Wenn du im 3D Visualiser keine Ausgabe siehst, musst du eventuell die Zone-Buttons verwenden, um die gewünschten Zonen einzuschalten. Außerdem muss _Preview to lasers_ aktiviert sein, siehe [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel "mention") weiter unten.
{% endhint %}

### Einen Clip bauen

Normalerweise beginnst du mit einer oder mehreren [Creator Nodes](creator-nodes.md) und verbindest dann von links nach rechts [Operatoren](operator-nodes/), die den Content verarbeiten. Wenn du Creator und/oder Operatoren zusammenschiebst, wirst du feststellen, dass sie sich automatisch miteinander verbinden. Du kannst sie wieder auseinanderziehen, um die Verbindung erneut zu trennen.

### Nodes zu deinem Clip hinzufügen

Klicke auf einen der Node-Buttons oben oder links und ziehe ihn in einen leeren Bereich im Clip Editor.

### Einstellungen für eine Node anpassen

Klicke auf den Button mit dem Zahnrad-Symbol (oben rechts an der Node), um das Eigenschaften-Panel für diese Node zu öffnen.

### Eine Node aktivieren und deaktivieren

Klicke auf den Button mit dem Power-Symbol (oben links an der Node), um die Node zu aktivieren oder zu deaktivieren. Die Node wird abgedunkelt, um zu zeigen, dass sie aktuell nicht aktiv ist. Beachte, dass Content weiterhin durch einen Operator geleitet wird, auch wenn er deaktiviert ist; die Node beeinflusst den Content dann aber nicht.

### Nodes miteinander verbinden

Content wird mit einer Creator Node erstellt und von links nach rechts durch Nodes weitergegeben; jeder Operator beeinflusst den Content auf irgendeine Weise und gibt ihn an den nächsten Operator weiter. Was am Ende des Pfads übrig bleibt, ist der Content des Clips. Creator und Operatoren werden automatisch miteinander verbunden, wenn du sie nah genug zusammenschiebst. Um sie zu trennen, ziehe sie wieder auseinander.

{% hint style="info" %}
Du kannst mehr als eine Node mit dem Eingang der nächsten Node verbinden. Das ist hilfreich, um mehrere Content-Elemente zu kombinieren.
{% endhint %}

### Node-Eigenschaften und Sockets

Jede Node hat unten eine Reihe von Sockets. Jeder Socket steht für eine Eigenschaft innerhalb der Node, zum Beispiel Helligkeit, Position, Skalierung, Rotation usw.

[Oscillator Nodes](oscillators/) können von unten mit diesen Sockets verbunden und verwendet werden, um diese Einstellungen zu animieren. Oscillator Nodes haben oben einen Ausgang. Klicke darauf und ziehe, um die Verbindung herauszuziehen, und lege sie dann auf einem Eigenschafts-Socket einer anderen Node ab.

### Oscillator Nodes

Oscillator Nodes werden verwendet, um Eigenschaften über die Zeit zu verändern. Sie stellen typischerweise Wellenformen wie eine Sägezahn- oder Sinuswelle dar, manche Oscillator Nodes nutzen aber externe Eingänge (z. B. den Mikrofon-Eingangspegel) als Quelle.

{% hint style="info" %}
Wenn du schon einmal einen analogen Synthesizer verwendet hast, kennst du vermutlich das Konzept von Oszillatoren. Sie werden häufig verwendet, um Wellenformen zu erzeugen oder den Klang über die Zeit zu verändern. Oscillators in Liberation erfüllen eine ähnliche Aufgabe.

**Fun fact:** Der Name _Liberation_ wurde vom Moog Liberation inspiriert, einem 1980 erschienenen Synthesizer-„Keytar“, der durch Herbie Hancock, Jean-Michel Jarre und sogar James Brown bekannt wurde!
{% endhint %}

Oscillators haben immer _range_-Einstellungen, mit denen der minimale und maximale Wert der anzupassenden Eigenschaft gesteuert wird. _Wave Oscillators_ haben außerdem immer eine _duration_-Einstellung, die festlegt, wie schnell der Oscillator den Wert verändert. Weitere Informationen findest du unter [wave-oscillators.md](oscillators/wave-oscillators.md "mention").

### Clip Editor panel

* Timer – oben im Panel siehst du die aktuelle Zeit des Clips während der Wiedergabe
* _RETRIGGER_ – startet den Clip wieder von vorn; besonders nützlich, wenn dein Clip nicht loopt
* _Preview to lasers_ – wenn diese Option aktiviert ist, wird der 3D Visualiser während der Bearbeitung dieses Clips aktualisiert. Wenn du sie deaktivierst, siehst du die Clips, die außerhalb des Editors laufen. Dies ist eine globale Einstellung, nicht pro Clip.
* _UNDO/REDO_ – für den Clip Editor selbst. Ist außerdem auf `Cmd / Ctrl + Z` und `Cmd / Ctrl + Shift + Z` gelegt.
* _SAVE CLIP_ – speichert deine Änderungen, warnt dich aber vor dem Überschreiben
* _SAVE AS A COPY_ – speichert deinen Clip im nächsten verfügbaren Slot im Clip Deck. Dies wird zur neuen Position deines Clips, und alle weiteren Speichervorgänge werden an diesem neuen Ort ausgeführt.
* _EXIT EDITOR_ – schließt den Clip Editor. Wenn du ungespeicherte Änderungen hast, wird ein Bestätigungs-Panel angezeigt.
