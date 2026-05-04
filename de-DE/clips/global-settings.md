---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Globale Transformationen

Zusätzlich zu Clip-Transformationen (shift x/y, scale x/y) gibt es Global Transformations, die auf jeden Clip angewendet werden, den du startest. Öffne das Panel _Global Transformations_, um sie zu sehen. (Dieses Panel befindet sich normalerweise in einem Tab neben _Clip Settings_.)

Standardmäßig werden alle diese Einstellungen zurückgesetzt, sobald keine Clips mehr laufen. Dieses Reset-Verhalten kann mit dem Button _AUTO RESET_ unten im Panel _Global Transformations_ deaktiviert werden.

{% hint style="info" %}
Beachte, dass Global Transformations nichts im Canvas beeinflussen, sondern nur Beam- und DMX-Zonen.
{% endhint %}

### Scale X/Y

Horizontale und vertikale Skalierung. Diese Werte sind miteinander gekoppelt, außer du drückst `Shift`. Standardmäßig sind sie außerdem den APC40 Device Control-Reglern 4 und 8 zugewiesen und erscheinen im kontextbezogenen Parameters-Panel rechts neben dem Clip Deck.

### Shift X/Y

Horizontale und vertikale Verschiebung. Verschiebt alles horizontal bzw. vertikal.

### Spin

Dreht alle Inhalte um die Mitte. Ein positiver Wert dreht im Uhrzeigersinn, ein negativer Wert gegen den Uhrzeigersinn. Du wirst sehen, dass diese Einstellung die Transformation _Rotation_ beeinflusst. Standardmäßig ist sie dem APC40 Device Control-Regler 3 zugewiesen und erscheint im kontextbezogenen Parameters-Panel rechts neben dem Clip Deck.

### Spin 3D

Dreht alle Inhalte um die Y-Achse (eine vertikale Linie in der Mitte). Du wirst sehen, dass diese Einstellung die Transformation _Rotation3D_ beeinflusst. Standardmäßig ist sie dem APC40 Device Control-Regler 7 zugewiesen und erscheint im kontextbezogenen Parameters-Panel rechts neben dem Clip Deck.

### Rotation

Eine Drehung um die Mitte, Wert in Grad.

### Rotation 3D

Eine Drehung um die Y-Achse (eine vertikale Linie in der Mitte), Wert in Grad.

### Auto reset

Wenn diese Option aktiviert ist, werden alle Global Transformations zurückgesetzt, sobald alle aktuell laufenden Clips deaktiviert wurden. So kannst du sicher sein, dass dich beim nächsten Starten eines Clips keine Überraschungen erwarten!
