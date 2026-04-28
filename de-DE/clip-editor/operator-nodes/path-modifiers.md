---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Pfadmodifikatoren

## &#x20;Dotter

Dieser Node ersetzt Linien- und Forminhalte durch gleichmäßig verteilte Punkte (vorhandene Punkte bleiben unverändert).

* **Colour** – die Farbe der Punkte. Wird ignoriert, wenn _Inherit Colour_ aktiviert ist, siehe unten. _Siehe auch_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – der Abstand zwischen den Punkten, gemessen in Pixeln. Kleinere Werte = mehr Punkte, größere Werte = weniger.
* **Offset** – verschiebt die Startposition der Punkte als Prozentsatz des Abstands. Kann animiert werden (z. B. mit einem Sägezahn-Oscillator Node), um „wandernde“ Punkteffekte zu erzeugen.
* **Keep Original** – wenn aktiviert, bleiben die ursprünglichen Linien/Formen erhalten und die Punkte werden darüber gezeichnet.
* **Render Profile** – wählt die Rendering-Qualität aus. _Siehe_ [render-profile.md](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – passt den Abstand automatisch so an, dass die Pfadlänge gleichmäßig teilbar ist.
* **Fade Out Ends** – reduziert die Helligkeit der Punkte zum Anfang und Ende des Pfads hin allmählich. Nützlich, wenn du **Offset** mit einem Sägezahn-Oscillator Node animierst, damit Punkte beim Bewegen zum Ende der Form weich ein- und ausgeblendet werden.

## &#x20;Trimmer

Dieser Node kürzt die sichtbare Länge von Linien und Formen, sodass du sie über die Zeit einblenden, ausblenden oder animieren kannst.

* **Offset** – steuert, wo der sichtbare Teil der Form beginnt. Selbst wenn _Trim Size_ auf 0 % steht, lässt eine Animation von Offset von 0 % → 100 % die Form entstehen, bei 50 % vollständig sichtbar werden und danach wieder verschwinden.
* **Trim Size** – legt fest, wie viel der Form erhalten bleibt, als Prozentsatz ihrer Gesamtlänge.
* **Loop** – behandelt die Form als durchgehende Schleife, sodass das Ende wieder mit dem Anfang verbunden wird, statt zu verschwinden.
* **All Shapes** – kombiniert alle Eingabeformen und trimmt sie, als wären sie ein einzelner Pfad. Wenn deaktiviert, wird jede Form einzeln getrimmt.
* **Add Dot at Start / Add Dot at End** – fügt an den Trimmpunkten einen Punkt in der gewählten Farbe hinzu. (Wenn kein Trim angewendet wird, werden keine Punkte hinzugefügt.)
* **Colour** – die Farbe der Trimmpunkte. _Siehe auch_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – wählt das Render Profile für die Punkte. _Siehe_ [render-profile.md](../fundamentals/render-profile.md "mention")
