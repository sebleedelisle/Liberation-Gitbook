---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / Chase

Wir sind uns alle einig: Mehr Laser bedeuten mehr Spaß. Wenn sie aber alle exakt dasselbe machen, lässt du viele kreative Möglichkeiten ungenutzt.

Das Zone-delay-System ist eine einfache, aber wirkungsvolle Methode, um Abwechslung über mehrere Zonen hinweg zu erzeugen und ein Multi-Laser-Setup richtig auszunutzen. Du kannst es außerdem verwenden, um einen eher klassischen Chase-Effekt zu erzeugen.

#### So funktioniert es

_Zone delay_ verzögert das Timing des Clips pro Zone und erzeugt dadurch eine Art Wischbewegung über die Zonen.

Besonders wirkungsvoll ist es, _Zone delay_ bei einem bereits laufenden Clip hinzuzufügen. Verwende dazu den entsprechenden Regler auf der APC40, um Stärke und Pattern anzupassen. (Siehe [apc40-reference.md](../reference/apc40-reference.md "mention")). Alternativ kannst du das _Clip Settings_-Panel verwenden.

Zone-delay-Einstellungen:

* **Zone delay** – steuert die Verzögerungszeit, die auf jede Zone angewendet wird, gemessen in 64stel-Noten.
* **Pattern** – wählt die Reihenfolge der Zonen aus
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Das Pattern arbeitet mit den Zonennummern und geht davon aus, dass deine Zonen von links nach rechts sortiert sind. Beim Berechnen der Pattern behandelt Zone delay Canvas-Zonen und DMX-Zonen als separate Gruppen.
{% endhint %}

* **Delay mode**
  1. No delay – verwende dies im Chase-Modus
  2. Delay – der Standardmodus; verzögert das Timing jeder Zone
  3. Delay with re-trigger – setzt den Clip bei jedem Schritt durch das Pattern wieder an den Anfang zurück. Das funktioniert gut mit _Chase mode_.
* **Chase mode** – wenn Chase mode aktiviert ist, wird jede Zone wie bei einem klassischen Chase-Effekt ein- und ausgeschaltet. Passe das Erscheinungsbild des Chase mit den Einstellungen _Fade in, Hold,_ und _Fade out_ an. Diese Werte werden als Anteil des _Zone delay_-Werts festgelegt. Ein Wert von 1 entspricht also derselben Zeit, die im Wert _Zone delay_ angegeben ist. Das ist etwas schwer zu erklären, daher mein Tipp: Probier es am besten selbst aus.

{% hint style="info" %}
Zone delay wird auch auf alle aktiven Effekte angewendet. Ein Flashing-Effekt wird zum Beispiel ebenso über die Zonen verzögert wie die Animation im Clip selbst.
{% endhint %}

Wenn ein Clip irgendeine Art von _Zone delay_ verwendet, siehst du oben rechts im Clip ein Drei-Punkte-Symbol. Diese Punkte sind animiert und zeigen dir den _Zone delay_-Stil dieses Clips. Weitere Details findest du unter [what-are-the-small-icons-on-the-clip-buttons.md](what-are-the-small-icons-on-the-clip-buttons.md "mention").

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Das Drei-Punkte-Symbol zeigt an, dass ein Clip einen Zone delay hat, und zeigt dessen Modus</p></figcaption></figure>

{% hint style="info" %}
Zone delay ist eine Einstellung, die zu jedem einzelnen Clip gehört. Sie ist nicht global, sondern Teil der kreativen Gestaltung eines Clips.
{% endhint %}
