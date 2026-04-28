---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Einführung

Der 3D Visualiser von Liberation ist eine unglaublich nützliche Funktion – du kannst deine Shows entwerfen und verfeinern, ohne überhaupt Laser zu benötigen! Für mich hat er sich als unverzichtbares Werkzeug erwiesen, besonders bei sehr komplexen Setups mit vielen Lasern.

### Navigation im 3D-Raum

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>Die Ansicht des 3D Visualiser</p></figcaption></figure>

* Klicke und ziehe, um die Ansicht um den Orbit-Punkt zu drehen
* Verwende das Mausrad, um dich zum Orbit-Punkt hin oder von ihm weg zu bewegen
* Klicke und ziehe bei gedrückter Umschalttaste, um die Kamera seitlich entlang der XY-Ebene zu bewegen (Strafe): nach links, rechts, oben und unten
* Doppelklicke irgendwo im Visualiser, um die Kameraposition zurückzusetzen

### Settings

Öffne das Panel _3D Visualiser Settings_ über das Menü _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Das Panel 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** - ändert die Größe des Visualiser im Verhältnis zum Rest der App
* **Brightness Adjustment** - ändert, wie hell die Laser dargestellt werden
* **Show laser numbers** - zeigt die entsprechende Nummer über jedem Laser an
* **Show zone names** - zeigt die entsprechenden Zonennamen unter jedem Laser an

### Camera settings

Diese Einstellungen beziehen sich hauptsächlich auf die virtuelle Kamera im 3D-Raum. Du siehst ein Dropdown-Menü mit Presets für diese Einstellungen, die du speichern und erneut laden kannst.

* **Camera distance -** Die Kamera ist immer auf ihren _Orbit-Punkt_ ausgerichtet. Der Kameraabstand gibt an, wie weit sie von diesem Punkt entfernt ist. Du kannst diese Einstellung auch mit dem Mausrad ändern.
* **FOV -** Field of view – bestimmt, wie weitwinklig bzw. wie stark hineingezoomt die Kamera ist.
* **Orbit position** - beschreibt die aktuelle Rotation um den Orbit-Punkt. Der erste Wert ist die Rotation um die X-Achse (Pitch), der zweite Wert ist die Rotation um die Y-Achse (Yaw).
* **Orbit centre point** - die Position des Orbit-Punkts im 3D-Raum: x, y, z.
* **Grid height** - die Höhe des Rasters über dem „Boden“ (also dort, wo y = 0 ist).

### Content settings

Diese Einstellungen legen fest, wo die Laser (und der Canvas) innerhalb der 3D-Umgebung platziert werden. Du siehst ein Dropdown-Menü mit Presets für diese Einstellungen, die du speichern und erneut laden kannst.

#### Lasers

Jeder Laser hat eine eigene Einstellungsgruppe, die du über das kleine weiße Dreieck aufklappen kannst.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Laser-Einstellungen im 3D Visualiser</p></figcaption></figure>

* **3D Position** - die x-, y- und z-Position des Lasers.
* **3D Orientation** - die Rotation des Lasers um die x-, y- und z-Achse.
* **Flip X / Flip Y** - spiegelt den virtuellen Output des Lasers. HINWEIS: Das sollte eigentlich nicht nötig sein – es ist besser, die Flip-/Orientation-Einstellungen des Lasers zu verwenden, um Abweichungen in deiner Hardware zu korrigieren.
* **Output Range horizontal / vertical** - bezieht sich auf den maximalen/minimalen Winkel der Scanner deines Lasers. 60º ist Standard, aber du kannst diesen Wert anpassen, wenn deine Laser anders sind.

#### Canvas

Wenn du das Canvas-System verwendest, kannst du auch auswählen, dass das Canvas-Bild in der 3D-Ansicht angezeigt wird. Aktiviere die Checkbox, um den Canvas darin zu rendern, und verwende die Einstellungen für Position, Orientierung und Skalierung, um festzulegen, wie er in deiner 3D-Ansicht aussieht.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Canvas-Einstellungen im 3D Visualiser</p></figcaption></figure>

{% hint style="info" %}
Siehst du „Geister“-Laser? Der 3D Visualiser ist bis zu einem gewissen Grad unabhängig vom Laser-Setup, und es ist möglich, im Visualiser mehr Laser zu haben als in Liberation. Wenn du deinem Projekt einen Laser hinzufügst, wird auch ein neues Laserobjekt im Visualiser hinzugefügt. Wenn du jedoch einen Laser löschst, bleibt im Visualiser weiterhin ein „Geister“-Laserobjekt zurück.

Um alle Geister-Laser zu entfernen, klicke auf den Button _Remove extra 3D laser objects_ (unten im Panel 3D Visualiser settings).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
