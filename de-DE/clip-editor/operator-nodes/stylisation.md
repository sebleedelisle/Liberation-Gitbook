---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stylisation-Nodes

## &#x20;Randomise

Erstellt verstreute Kopien der eingehenden Elemente mithilfe eines kohärenten Noise-Felds. Anders gesagt: Deine Formen und Punkte werden kontrolliert und „noisy“ kopiert und verschoben. Statt dass alles ordentlich an einer Stelle bleibt, erhältst du mehrere Versionen, die sich verschieben und verteilen – wie Partikel, die sich in einer Strömung bewegen.

* **count** – Anzahl der Kopien pro eingehendem Element (1–20). Bei 1 erhältst du eine einzelne, leicht versetzte Version jedes Elements. Höhere Werte erzeugen mehrere verstreute Kopien.
* **noise offset** – bewegt sich durch das Noise-Feld (0–100%). Die Bewegung loopt nahtlos. Wenn du diesen Wert mit einem Oscillator Node animierst, entsteht eine gleichmäßige, kontinuierliche Bewegung aller Kopien zusammen.
* **noise jitter** – steuert die Texturskalierung des Noise. Niedrigere Werte erzeugen breite, weiche Variationen. Höhere Werte erzeugen engere, unruhigere Platzierungen. Das verändert das Muster, nicht die Stärke.
* **change between points** – steuert, wie stark sich jede Kopie von der vorherigen unterscheidet. Niedrige Werte halten die Kopien nah beieinander und ähnlich. Hohe Werte verteilen sie stärker und erzeugen mehr Variation.
* **face direction** – rotiert jede Kopie so, dass sie in die Bewegungsrichtung im Noise-Feld zeigt. Dadurch richten sich Pfeile/Partikel am Flow aus.
* **amount** – Gesamtstärke des Effekts (0–100%). Skaliert sowohl die Verschiebung als auch die Rotation durch Face direction.

{% hint style="info" %}
Der Randomise-Node ist das Herzstück des Randomise-Effekts!
{% endhint %}

## &#x20;Trails

Erzeugt Echos deines Inhalts und lässt hinter dem Original beim Bewegen ausblendende oder skalierende Kopien zurück.

* **change render profile for trail** – wenn aktiviert, verwenden alle Trail-Kopien das ausgewählte **render profile**. _Siehe_ [Render profile](../fundamentals/render-profile.md "mention").
* **render profile** – das Profil, das für Trail-Kopien verwendet wird, wenn der Schalter oben aktiviert ist. Das wird häufig genutzt, wenn der Hauptinhalt auf **DETAIL** gesetzt ist, die Echos aber als **FAST** gerendert werden. So bleiben die Hauptformen klar und detailliert, während die Trails effizienter gerendert werden.
* **delay** – legt den Abstand zwischen Trail-Kopien in musikalischer Zeit fest, gemessen in **1/64-Noten-Schritten**.\
  Zur Orientierung:
  * 16 = 1/16 Takt (Sechzehntelnote)
  * 32 = 1/8 Takt (Achtelnote)
  * 64 = 1/4 Takt (Viertelnote)
  * 128 = 1/2 Takt (Halbe Note)
  * 256 = 1 Takt
* **trail size** – wie viele Trail-Kopien hinter dem Live-Inhalt gezeichnet werden.
* **freeze trails** – verwandelt weich fließende Trails in eine Folge eingefrorener Momentaufnahmen. Nützlich für stakkatoartige, beat-synchrone Trail-Effekte.
* **brightness start / brightness end** – wendet Helligkeit über den Trail hinweg an, von der neuesten Kopie (**start**) bis zur ältesten Kopie (**end**). Typischerweise setzt du **brightness start** auf 100% und **brightness end** auf 0%, damit die Echos ausblenden.
* **scale start / scale end** – wendet Skalierung über den Trail hinweg an, von der neuesten Kopie (start) bis zur ältesten Kopie (end). Für Trails, die bis auf nichts schrumpfen, setze **scale start** auf 100% und **scale end** auf 0%.

## &#x20;Shimmer

Fügt deinem Inhalt eine funkelnde Helligkeitsvariation hinzu – von leichtem Glitzern bis zu intensivem Strobing.

* **speed** – wie schnell sich der Shimmer über die Zeit verändert. Höhere Werte flackern schneller; 0 pausiert den Effekt.
* **separation** – wie stark sich benachbarte Punkte/Elemente voneinander unterscheiden.
  * 0: alles schimmert gemeinsam.
  * \>0: nahe Punkte erhalten zunehmend unterschiedliche Phasen, sodass der Shimmer über die Form variiert.
  * <0: wie oben, aber die Phasenprogression läuft in die entgegengesetzte Richtung.
* **threshold** – statt weich auszublenden, blinken Punkte nun abhängig von ihrer Helligkeit vollständig an oder aus. Hellere Elemente leuchten häufiger auf. Beachte aber, dass Elemente mit 100% Helligkeit immer an sind, während Elemente mit 0% Helligkeit immer aus sind. Nützlich für klare Glitter- oder Sternenlicht-Effekte.

{% hint style="info" %}
**threshold** zu aktivieren ist eines dieser großartigen versteckten Features, die deine Partikel oder Inhalte wirklich lebendig wirken lassen können. Statt auszublenden, werden Punkte basierend auf ihrer Helligkeit schnell ein- und ausgeschaltet. Da zu jedem Zeitpunkt weniger Punkte gezeichnet werden, ist das Ergebnis eine hellere Ausgabe und eine flüssigere Animation.

Beachte aber: Wenn dein Inhalt bereits auf 100% Helligkeit steht, passiert nichts!
{% endhint %}

* **use whole shape** – wendet einen Shimmer-Wert gleichmäßig auf die gesamte Form an. Wenn deaktiviert, unterteilt der Node Formen, sodass verschiedene Bereiche unabhängig voneinander funkeln können und ein gesprenkelter Look entsteht.

## &#x20;Particles

Dies ist ein experimenteller Effekt, der auf Basis deines Inhalts Partikel erzeugt und animiert. Alle punktbasierten eingehenden Elemente werden als Emitter-Positionen behandelt. Da Partikelpfade vorab berechnet werden, musst du die Partikel eventuell aktualisieren/neu berechnen, wenn sich dein Eingangsinhalt ändert (ändere dazu einfach eine der Einstellungen).

**General**

* **keep original** – wenn aktiviert, bleibt der ursprüngliche Inhalt erhalten und Partikel werden darüber hinzugefügt. Nützlich, wenn die Emitter-Punkte sichtbar bleiben sollen.
* **number of particles** – wie viele Partikel pro Emission erstellt werden. Höhere Werte erzeugen dichtere Effekte, niedrigere Werte wirken minimalistischer.
* **emission period** – die Spanne des Loops (in Takten), über die Partikel emittiert werden. Bei 100% werden sie gleichmäßig über den Loop verteilt; kleinere Werte bündeln sie zu Bursts.
* **loop length** – wie lange der Partikel-Loop dauert, gemessen in musikalischen Takten.
* **loop count** – wie oft der Loop wiederholt wird, bevor er zurückgesetzt wird. Bei 1 folgen die Partikel jedes Mal exakt derselben Simulation, wodurch der Ablauf perfekt wiederholbar ist. Höhere Werte erzeugen mehr Variation, bevor der Zyklus zurückgesetzt wird.
* **delay** – verschiebt die Startzeit der Emission um eine Anzahl von 1/64-Noten, für Timing-Effekte.

**Motion**

* **speed** – wie schnell sich die Partikel vom Emitter wegbewegen.
* **speed variation** – fügt Zufälligkeit hinzu, damit sich nicht alle Partikel mit derselben Geschwindigkeit bewegen. Erzeugt eine natürlichere Streuung.
* **direction** – legt die Grundrichtung fest, in die Partikel abgefeuert werden, definiert durch **x, y, z angles**. Diese Winkel rotieren den Abschussvektor im 3D-Raum, sodass du die Partikel gerade nach oben, seitlich oder in jede diagonale Richtung ausrichten kannst. Kombiniere dies mit **spread** für breitere Kegel oder chaotischere Bursts.

{% hint style="info" %}
**Euler-Winkel**\
Liberation verwendet **Euler-Winkel**, um Orientierung im 3D-Raum zu beschreiben. Das sind einfache Rotationen um die drei Hauptachsen:

* **X** – nach vorn/hinten neigen (wie beim Nicken)
* **Y** – nach links/rechts drehen (wie beim Kopfschütteln für „Nein“)
* **Z** – im/gegen den Uhrzeigersinn rollen (wie beim seitlichen Neigen des Kopfes)

Durch Anpassen dieser drei Werte kannst du Partikel in jede Richtung ausrichten.
{% endhint %}

* **direction variation** – fügt eine zufällige Streuung um diese Richtung hinzu. Nützlich, um Kegel, Sprays oder Explosionen zu erzeugen.
* **drag** – bremst Partikel mit der Zeit ab. Höhere Werte lassen sie schwerer und träger wirken.
* **gravity** – zieht Partikel nach unten (positiv) oder drückt sie nach oben (negativ).
* **gravity variation** – fügt pro Partikel Variation zur Schwerkraft hinzu, wodurch die Bewegung chaotischer wird.

**Life**

* **life duration** – wie lange Partikel existieren (gemessen in 1/64-Noten-Einheiten). Bei kürzeren Werten verschwinden Partikel schnell, bei längeren Werten bleiben sie länger sichtbar.
* **life variation** – fügt der Lebensdauer der Partikel Zufälligkeit hinzu, damit sie nicht alle gleichzeitig verschwinden.
* **start delay / start delay variation** – verzögert, wann jedes Partikel sichtbar wird (in 1/64-Noten-Schritten). Das Partikel ist während dieser Zeit bereits erzeugt und in Bewegung, seine Helligkeit bleibt aber bei 0, sodass es unsichtbar bleibt, bis die Verzögerung abgelaufen ist. Das ist nützlich, wenn du verzögerte Feuerwerks-„Sparkles“ erscheinen lassen möchtest.

**Colour & brightness**

* **hue start** – Anfangsfarbe der Partikel.
* **hue variation** – fügt Zufälligkeit hinzu, damit nicht alle Partikel mit derselben Farbe starten.
* **hue change** – verschiebt den Farbton über die Lebensdauer des Partikels und erzeugt farbwechselnde Trails.
* **brightness start / brightness end** – wendet Helligkeit über die Lebensdauer des Partikels an. Typischerweise setzt du brightness start hoch und brightness end niedrig, damit sie natürlich ausblenden.
* **brightness variation** – randomisiert die Anfangshelligkeit für einen dynamischeren Look.
* **saturation start / saturation end** – legt fest, wie kräftig die Farbe am Anfang und Ende ist.
* **saturation variation** – randomisiert die Sättigung für Variation zwischen den Partikeln.

**Simulation**

* **time adjustment** – beschleunigt oder verlangsamt die gesamte Partikelsimulation. Nützlich, um sie an verschiedene Tempi anzupassen oder Bewegungen stärker zu betonen.
