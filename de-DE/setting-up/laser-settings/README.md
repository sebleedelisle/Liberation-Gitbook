# ✅ Panel „Laser output“-Einstellungen

Öffne das Einstellungs-Panel _Laser output_ über das Menü _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Damit werden dir die Einstellungen für den aktuell ausgewählten Laser angezeigt. Du kannst den Laser auswählen:

* über die Nummern-Schaltfläche im Panel _Laser overview_
* mit einer Zifferntaste auf deiner Tastatur; die Tasten 1 bis 0 öffnen die Laser 1–10
* mit der Taste `Tab`, um durch die Laser zu wechseln (`Shift + Tab` geht rückwärts).

Oben in diesem Panel siehst du:

* eine Nummern-Schaltfläche – klicke darauf, um diesen Laser zu aktivieren/deaktivieren. Sie ist rot, wenn der Laser aktiviert ist.
* einen _Brightness_-Regler nur für diesen Laser. Beachte, dass dieser mit der globalen Helligkeit kombiniert wird.
* einen _Test Pattern_-Schalter und eine Pattern-Auswahl. Damit kannst du ein bestimmtes Test-Pattern nur für diesen Laser auswählen. (Diese Bedienelemente werden in der Toolbar der Output-Ansicht gespiegelt.)

### Ausgabeausrichtung / Spiegelung korrigieren

Die nächsten Elemente dienen dazu, das Setup deines Lasers zu korrigieren, damit er sich in Liberation konsistent verhält.

* **Flip horizontal / vertical** – mit diesen Optionen kannst du die Ausgabe deines Lasers korrigieren

{% hint style="info" %}
Du solltest die Einstellungen für horizontalen/vertikalen Flip nicht ändern müssen, außer dein Laser wurde falsch verkabelt oder er hat X/Y-Flip-Schalter auf der Rückseite, die nicht richtig eingestellt sind. Wenn die Ausgabe für einen bestimmten Clip gespiegelt werden soll, kannst du das direkt am Clip einstellen.
{% endhint %}

* **Orientation** – wenn dein Laser seitlich oder kopfüber montiert wurde, kannst du die Rotation mit dieser Einstellung korrigieren.
* **Fine position adjustments** – kann verwendet werden, um sehr kleine Verschiebungen/Rotationen zu korrigieren. Gedacht zum Ausgleichen von Drift/Setzen, wenn ein Laser über Nacht oder längere Zeit stehen gelassen wurde.

{% hint style="info" %}
Beachte, dass die Korrekturen für Ausrichtung/Spiegelung im 3D Visualiser nichts verändern. Sie sollten verwendet werden, um die Ausgabe des echten Lasers an das anzupassen, was im 3D Visualiser zu sehen ist!
{% endhint %}

### Laser-Einstellungen kopieren

Siehe [Panel „Laser output“-Einstellungen](./#copy-laser-settings "mention").

### Scanner-Einstellungen

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Die Einstellung Speed bestimmt, wie schnell sich die Scanner bewegen.

{% hint style="danger" %}
Auch wenn die Standardeinstellungen recht konservativ sind, kannst du deine Scanner trotzdem beschädigen, wenn du sie zu schnell betreibst. Sei vorsichtig, besonders wenn du die Geschwindigkeit erhöhst.
{% endhint %}

{% hint style="info" %}
Diese Speed-Einstellung ändert nicht die Point-Rate, sondern passt an, wie weit die Punkte auseinanderliegen. Weitere Informationen findest du unter [◼️ Wie Liberation Laserinhalte erzeugt](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Der Strahl ändert seine Farbe und wird ein- und ausgeschaltet, während die Scanner ihn bewegen. Diese beiden Dinge sind normalerweise nicht perfekt miteinander synchron. Passe diese Einstellung an, um sie wieder aufeinander abzustimmen.

{% hint style="info" %}
Das wird manchmal als _blank shift_ bezeichnet, aber ich persönlich bevorzuge den Begriff _scanner sync_ – er ist etwas genauer, da hier das Timing aller Farbwechsel im Verhältnis zur Scannerbewegung angepasst wird.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser-„Tails“ – Colour shift ist nicht richtig eingestellt</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Keine Laser-„Tails“! Colour shift passt!</p></figcaption></figure></div>

Wenn du kleine „Tails“ in deiner Laserausgabe siehst, muss wahrscheinlich Scanner sync angepasst werden. Wenn die Tails trotzdem immer erscheinen, betreibst du deine Scanner/Lasertreiber vermutlich schneller, als sie verarbeiten können. Versuche, die Scanner-Geschwindigkeit zu reduzieren.

#### Scanner presets

Verwende dies, um eine vordefinierte Scanner-Einstellung auszuwählen. Die Standardoption ist normalerweise in Ordnung, du solltest diese Einstellung also nicht ändern müssen, außer du hast besonders schlechte (oder gute) Scanner. Wenn du tiefer einsteigen möchtest, siehe [◼️ Scanner-Presets & Render-Profile](../../advanced/scanner-presets.md "mention")

#### Colour calibration

Mit diesem System kannst du die Helligkeitskurve und den Weißabgleich deines Lasers korrigieren. Siehe [Farbkalibrierung](../../advanced/colour-calibration.md "mention")

#### Advanced settings

Du solltest an diesen Einstellungen normalerweise nichts ändern müssen. Wenn du aber neugierig bist, siehe [◼️ Erweiterte Lasereinstellungen](../../advanced/advanced-laser-settings.md "mention")
