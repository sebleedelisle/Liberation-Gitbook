---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Laser-Ausgabe-Einstellungen

Öffne das Einstellungs-Panel _Laser output_ über das Menü _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Hier werden die Einstellungen für den aktuell ausgewählten Laser angezeigt. Du kannst den Laser wechseln:

* über seine Nummerntaste im Panel _Laser overview_
* mit einer Zahlentaste auf deiner Tastatur; die Tasten 1 bis 0 öffnen die Laser 1 bis 10
* mit der Taste `Tab`, um durch die Laser zu wechseln (`Shift + Tab` geht rückwärts).

Oben in diesem Panel siehst du:

* eine Nummerntaste – klicke darauf, um diesen Laser zu aktivieren/deaktivieren. Sie ist rot, wenn der Laser aktiviert ist.
* einen _Brightness_-Schieberegler nur für diesen Laser. Beachte, dass dieser mit der globalen Helligkeit kombiniert wird.
* den _Test Pattern_-Schalter und eine Pattern-Auswahl. Damit kannst du nur für diesen Laser ein bestimmtes Test-Pattern auswählen. (Diese Bedienelemente werden in der Symbolleiste der Output-Ansicht gespiegelt.)

### Ausrichtung der Ausgabe / Spiegelungskorrektur

Die nächsten Elemente dienen dazu, die Einrichtung deines Lasers zu korrigieren, damit er sich in Liberation konsistent verhält.

* **Flip horizontal / vertical** – mit diesen Optionen kannst du die Ausgabe deines Lasers korrigieren

{% hint style="info" %}
Du solltest die Einstellungen für horizontalen/vertikalen Flip nicht ändern müssen, es sei denn, dein Laser wurde falsch verkabelt oder er hat X/Y-Flip-Tasten auf der Rückseite, die nicht korrekt eingestellt sind. Wenn die Ausgabe für einen bestimmten Clip gespiegelt werden soll, kannst du das direkt am Clip einstellen.
{% endhint %}

* **Orientation** – wenn dein Laser seitlich oder kopfüber montiert wurde, kannst du die Rotation mit dieser Einstellung korrigieren.
* **Fine position adjustments** – kann verwendet werden, um sehr kleine Verschiebungen/Rotationen zu korrigieren. Gedacht zum Ausgleichen von Drift/Setzen, wenn ein Laser über Nacht oder über längere Zeit stehen gelassen wurde.

{% hint style="info" %}
Beachte, dass die Korrekturen für Ausrichtung/Spiegelung nichts im 3D Visualiser ändern. Sie sollten verwendet werden, um die Ausgabe des tatsächlichen Lasers an das anzupassen, was im 3D Visualiser zu sehen ist!
{% endhint %}

### Laser-Einstellungen kopieren

Siehe [#copy-laser-settings](laser-settings.md#copy-laser-settings "mention").

### Scanner-Einstellungen

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Die Speed-Einstellung bestimmt, wie schnell sich die Scanner bewegen.

{% hint style="danger" %}
Auch wenn die Standardeinstellungen recht konservativ sind, kannst du deine Scanner trotzdem beschädigen, wenn du sie zu schnell ansteuerst. Sei vorsichtig, besonders wenn du die Geschwindigkeit erhöhst.
{% endhint %}

{% hint style="info" %}
Diese Speed-Einstellung ändert nicht die Punktfrequenz, sondern passt an, wie weit diese Punkte auseinanderliegen. Weitere Informationen findest du unter [how-liberation-generates-laser-content.md](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Der Strahl ändert die Farbe und wird ein- und ausgeschaltet, während die Scanner ihn bewegen. Diese beiden Dinge sind normalerweise nicht perfekt synchron. Passe diese Einstellung an, um sie wieder aufeinander abzustimmen.

{% hint style="info" %}
Das wird manchmal als _blank shift_ bezeichnet, aber ich persönlich bevorzuge den Begriff _scanner sync_ – er ist etwas genauer, weil damit das Timing aller Farbwechsel im Verhältnis zur Scannerbewegung angepasst wird.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser-„tails“ – Colour shift nicht richtig eingestellt</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Keine Laser-„tails“! Colour shift passt!</p></figcaption></figure></div>

Wenn du kleine „tails“ in deiner Laserausgabe siehst, muss wahrscheinlich die Scanner sync angepasst werden. Wenn die Tails unabhängig von der Einstellung weiterhin erscheinen, steuerst du deine Scanner/Lasertreiber vermutlich schneller an, als sie verarbeiten können. Versuche, die Scanner-Geschwindigkeit zu verringern.

#### Scanner-Presets

Verwende diese Einstellung, um ein vordefiniertes Scanner-Setting auszuwählen. Die Standardoption ist normalerweise in Ordnung, daher solltest du diese Einstellung nicht ändern müssen, es sei denn, du hast besonders schlechte (oder gute) Scanner. Wenn du tiefer einsteigen möchtest, siehe [scanner-presets.md](../advanced/scanner-presets.md "mention")

#### Farbkalibrierung

Mit diesem System kannst du die Helligkeitskurve und den Weißabgleich deines Lasers korrigieren. Siehe [colour-calibration.md](../advanced/colour-calibration.md "mention")

#### Erweiterte Einstellungen

Du solltest an diesen Einstellungen normalerweise nichts ändern müssen. Wenn du aber neugierig bist, siehe [advanced-laser-settings.md](../advanced/advanced-laser-settings.md "mention")
