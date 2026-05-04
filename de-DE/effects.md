---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Effekte

Das Effektsystem in Liberation ist eine spaßige und vielseitige Möglichkeit, die Clip-Ausgabe in Echtzeit zu verändern. Effekte sind komplett flexibel und können alles blinken lassen, ein- und ausschalten, drehen, Farben ändern oder sogar zufällig herumfliegen lassen!

Alles, was du im Clip-Editor machen kannst, kann auch als Effekt verwendet werden. Tatsächlich werden Effekte mit genau demselben Node-Editor bearbeitet wie Clips! Siehe [Effekte](effects.md#editing-effects "mention"). Die kreativen Möglichkeiten sind praktisch unbegrenzt.

Die Standard-Effekttasten 1–8 befinden sich unter den Zonentasten, und die Effekte 9–24 sind die kleinen Tasten unten.

#### Einen Effekt anwenden

Drücke eine Effekttaste, um den Effekt ein- oder auszuschalten. Noch besser: Verwende die APC40-Slider 1–8, um Effekte ein- und auszublenden. Um einen Effekt ohne APC40 einzublenden, klicke auf die Taste und ziehe nach oben oder unten. Oder klicke mit der rechten Maustaste auf die Effekttaste und passe den Level-Slider an.

{% hint style="warning" %}
Wenn du die Effekttaste drückst, wird dieser Effekt sofort aktiviert. Beachte jedoch: Wenn der Level auf null steht, passiert nichts! Klicke auf die Taste und ziehe, um den Level zu ändern, oder klicke mit der rechten Maustaste und verwende den _level_-Slider, oder nutze die APC40-Fader.
{% endhint %}

#### Effekte und die Zonenverzögerung des Clips

Effekte übernehmen die Zone-Delay-Einstellung jedes aktuell laufenden Clips. Wenn dein Clip also eine Verzögerung hat, die von links nach rechts läuft, und du den Flash-Effekt hinzufügst, wird auch der Flash von links nach rechts verzögert.

{% hint style="info" %}
Wie die Zonenverzögerung des Clips von Effekten übernommen wird, gehört zu den Dingen, die extrem schwer zu beschreiben sind, aber sofort klar werden, wenn du es ausprobierst!

Ich würde sagen, dass es eines der spaßigsten und kreativsten Werkzeuge ist, die in Liberation eingebaut sind. Probier es aus, dann siehst du, was ich meine!
{% endhint %}

#### Effektparameter

Füge deinem Effekt mit einem _Parameter node_ einen Parameter hinzu. Das Parameter-System ist eine Möglichkeit, mehrere Einstellungen innerhalb deines Effekts von außen anzupassen. Weitere Informationen findest du unter [Parameter Control](clip-editor/oscillators/parameter-control.md "mention").

Verwende die Drehregler 1–8, um den _parameter_ für jeden Effekt anzupassen. Oder klicke mit der rechten Maustaste auf die Effekttaste und passe die Parameter-Slider an. Die Parameteränderung bewirkt unterschiedliche Dinge, je nachdem, wie der Effekt aufgebaut ist. In der Liste unten findest du die Standard-Effekte und was ihre Parameter tun.

{% hint style="info" %}
Die Drehregler 1–8 befinden sich beim APC40 Mk2 oben und beim Mk1 oben rechts. Siehe auch: [APC40-Referenz](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
Die kleinen Zahlen auf den Effekttasten beziehen sich auf _level_ und _parameter_ des Effekts. Der _level_ wird über den Fader am APC40 gesteuert, oder du klickst auf die Taste und ziehst. Der Parameter wird über die Drehregler am APC40 angepasst, oder du klickst mit der rechten Maustaste, um ihn mit der Maus einzustellen.
{% endhint %}

#### Die Standard-Effekte

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Wendet eine chaotische Bewegung auf die Clip-Ausgabe an. Der Parameter passt Stärke und Geschwindigkeit des Chaos an.
2. **Sine wave** :\
   Verformt den gesamten Inhalt entlang einer bewegten Sinuswelle. Der Parameter passt die Wellenlänge an.
3. **Rotation** :\
   Dreht alles. Der Parameter passt die Drehgeschwindigkeit an.
4. **Horizontal flip** :\
   Staucht und streckt alles horizontal. Der Parameter passt die Geschwindigkeit an.
5. **Scale** :\
   Skaliert alles wiederholt von voll auf null. Der Parameter passt die Geschwindigkeit an.
6. **Hue** :\
Ändert den Farbton von allem, verändert aber nicht die Sättigung (d. h. alles Weiße bleibt weiß). Der Parameter passt den Farbton an.
7. **Saturation and hue** :\
Ändert den Farbton von allem und sättigt die Farbe außerdem vollständig (d. h. alles Weiße wird zur jeweiligen Farbe). Der Parameter passt den Farbton an.
8. **Flash** :\
   Lässt die Helligkeit von allem wiederholt von voll auf null blinken. Der Parameter passt die Blinkgeschwindigkeit an.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

In der unteren Reihe gibt es weitere 16 Farbeffekte, mit denen du voreingestellte Farbton- und Sättigungswerte anwenden kannst.

Beachte, dass dies die Standard-Effekte sind, sie aber so bearbeitet werden können, dass sie fast alles tun, was du möchtest!

### Auf Gruppen anwenden

Du kannst auswählen, welche Gruppen vom Effekt beeinflusst werden. Klicke mit der rechten Maustaste und schalte die Gruppen-Checkboxes mit der Beschriftung _Apply to groups_ um.

Ich verwende dieses Setup hauptsächlich, wenn ich separat mit Canvas-Grafiken und Laserbeams arbeite. Ich weise alle Canvas-Clips Gruppe 5 zu und schließe diese Gruppe dann von Effekten aus, die diese grafischen Clips nicht beeinflussen sollen.

Du kannst es auch verwenden, um live zwei unterschiedliche Farbänderungen gleichzeitig auf zwei Gruppen von Lasern anzuwenden. Erstelle zwei Farbänderungs-Effekte und wähle aus, auf welche Clip-Gruppen jeder davon angewendet wird.

### MX-Gruppe

Kurz für _Mutually Exclusive_: Damit kannst du Effekte so gruppieren, dass immer nur ein Effekt in der Gruppe gleichzeitig aktiv sein kann. Beachte, dass immer nur einer der Standard-Farbwechseleffekte gleichzeitig aktiv sein kann. Das liegt daran, dass sie alle in MX Group 1 sind.

Diese Funktion ist deaktiviert, wenn die Einstellung _MX Group_ auf 0 steht.

### Effekte bearbeiten

Klicke mit der rechten Maustaste auf einen beliebigen Effekt und dann auf die Schaltfläche _EDIT EFFECT_, um den Effekt-Editor zu öffnen. Du wirst sehen, dass dieser Editor identisch mit dem Clip-Editor ist!

Bearbeite deinen Effekt genauso, wie du jeden anderen Clip bearbeiten würdest. Siehe [Der Clip Editor](clip-editor/ "mention").

Du brauchst mindestens einen Creator-Node; das kann alles Mögliche sein (Linie, Kreis, Form, sogar Text!), aber du solltest wahrscheinlich etwas wählen, das in der Vorschau der Effekttaste am meisten Sinn ergibt.

Wenn Effekte angewendet werden, werden alle Creator-Nodes im Effekt durch die Ausgabe der aktuell laufenden Clips ersetzt.

{% hint style="warning" %}
Aus extrem mühsamen technischen Gründen sind die „trails“-Nodes innerhalb eines Effekts nicht aktiviert. Dasselbe gilt für die Einstellung „delay“ innerhalb von Pattern-Nodes (sie verwenden dasselbe System). Das wird in zukünftigen Versionen behoben.
{% endhint %}
