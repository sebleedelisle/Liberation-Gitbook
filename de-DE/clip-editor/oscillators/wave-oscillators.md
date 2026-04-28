---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Wave oscillators

## Auf dieser Seite:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Sawtooth wave](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Triangle wave](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sine wave](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Square wave](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Einstellungen für Wave-Oszillatoren

Alle Wave-Oszillatoren haben die folgenden Einstellungen:

* **range min / range max** - legt den Wertebereich für die Eigenschaft fest, die der Oszillator steuert. Die Eigenschaft wird auf _range min_ gesetzt, wenn die Wellenform ganz unten ist, und auf _range max_, wenn die Wellenform ganz oben ist.

{% hint style="info" %}
Wenn du zum Beispiel möchtest, dass sich ein Punkt zwischen -100 und 100 nach links und rechts bewegt, verbindest du den Oszillator mit dem _x property socket_, setzt _min range_ auf -100 und _max range_ auf 100.
{% endhint %}

* **duration** - die Zeit, die ein vollständiger Zyklus (oder _Loop_) braucht. Sie ist relativ zum Tempo in Takten. ¼ ist also ein einzelner Beat. 1 ist ein vollständiger Takt usw.
* **duration multiplier** - skaliert die Basisdauer mit einem ausgewählten Faktor. Wenn **duration** zum Beispiel auf eine Viertelnote gesetzt ist und der Multiplikator 3 beträgt, läuft der Oszillator über drei Viertelnoten (eine punktierte halbe Note). Bruchwerte werden ebenfalls unterstützt — halte _SHIFT_ gedrückt, während du den Slider ziehst, um nicht-ganzzahlige Werte einzustellen. Das ist nützlich für Phasing-Effekte oder subtile Timing-Verschiebungen.
* **offset** - der Startversatz der Welle als Prozentsatz der Dauer. Wenn die Welle nach einem Viertel der Dauer starten soll, setzt du diesen Wert auf 25%.
* **repeat count** - die Anzahl der Wiederholungen, bevor der Loop stoppt. Standardmäßig ist der Wert _FOREVER_, du kannst ihn aber ändern, wenn der Oszillator nicht unbegrenzt laufen soll. Nach dem Stoppen wird die Eigenschaft auf den Wert am Ende der Welle gesetzt.
* **delay count** - die Verzögerung in Beats, bevor der Oszillator startet. Bevor er startet, wird die Eigenschaft auf den Wert am Anfang der Welle gesetzt.

{% hint style="info" %}
Mit einer sorgfältigen Kombination aus _repeat count_ und _delay count_ kannst du sehr komplexe Animationen erstellen — fast wie eine eigene Timeline!
{% endhint %}

## Gemeinsame Einstellungen

* **steps** - teilt die Bewegung in eine Anzahl diskreter Schritte auf. Nützlich, wenn Eigenschaften zu Werten „springen“ sollen, statt sich weich zu bewegen.

{% hint style="info" %}
Beachte, dass die Schritte nach Zeit und nicht nach Wert aufgeteilt werden. Bei einer Welle mit 4 Schritten und einer Dauer von 1 Takt ändert sich die Eigenschaft also sofort bei jedem Beat.
{% endhint %}

* **clamp min / clamp max -** vergrößert die Skalierung der Welle über ihre Minimal- oder Maximalwerte hinaus und begrenzt das Ergebnis.

{% hint style="info" %}
Das _clamp_-Konzept ist etwas schwer zu erklären. Stell dir vor, die Wellenform läuft oben oder unten aus dem Diagramm heraus und wird dann an den Kanten abgeschnitten. Am besten experimentierst du damit! Die Werte sind sehr nützlich, wenn eine Sawtooth wave später beginnen oder früher enden soll.
{% endhint %}

* **ease function** - die Sawtooth- und Triangle-Wellen haben außerdem eine Ease-Funktion, die die Animationskurve subtil verändert und deine Animationen deutlich ausdrucksstärker machen kann.
  * **LINEAR** - Standardwert, kein Easing; bewegt sich einfach linear zwischen Minimal- und Maximalwert.
  * **EASE OUT** - startet schnell und wird zum Ende hin langsamer. Sehr gut, um Physik zu simulieren, z. B. ein Abbremsen bis zum Stillstand.
  * **EASE IN** - startet langsam und wird allmählich schneller. Gut, um zunehmenden Schwung zu simulieren.
  * **EASE IN/OUT** - eine Kombination aus beidem, mit sehr organischer Bewegung.

{% hint style="warning" %}
**Easing -** Ich würde die standardmäßige lineare Animation nach Möglichkeit vermeiden, außer du möchtest ganz bewusst etwas Roboterhaftes. Easing kann deine Animationen viel fließender und organischer wirken lassen!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sawtooth wave

Auch als _Ramp Waveform_ bekannt, weil sie nach oben ansteigt und am Ende ihres Zyklus abrupt abfällt. Das ist wahrscheinlich der am häufigsten verwendete Wave-Oszillator, weil er einen Loop für zyklische Eigenschaften wie _hue_ oder _rotation_ erzeugt.

Siehe die Abschnitte oben für:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Spezifisch für Sawtooth:

* **cycle range compensation** - verfügbar, wenn **steps** gesetzt ist, und nützlich für zyklische Werte, zum Beispiel eine Rotation von 0 bis 360. Wenn diese Option nicht gesetzt ist, sind Anfangs- und Endwert gleich, was am Startpunkt zu einem Hängenbleiben führen kann (weil 0 und 360 derselbe Winkel sind). Wenn du diese Option aktivierst, wird der Maximalbereich reduziert, um die Schrittpositionen zu korrigieren.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Triangle wave

Anders als die _sawtooth wave_, die in jedem Zyklus zurück zum Anfang springt, bewegt sich die _triangle wave_ linear vorwärts und dann rückwärts.

Siehe die Abschnitte oben für:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sine wave

Die weichste Wellenform! Sie oszilliert sanft zwischen zwei Werten, wie ein Pendel.

Siehe die Abschnitte oben für:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Square wave

Die einfachste Wellenform - sie kippt einfach zwischen zwei Werten hin und her!

Siehe die Abschnitte oben für:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Spezifisch für Square:

* **pulse width** - die Zeitspanne, in der die Welle relativ zur Gesamtdauer auf ihrem Maximalwert ist. 50% ist der Standardwert, also genau halb und halb. Wenn sie nur ein Viertel der Zeit „an“ sein soll, setze den Wert auf 25%. Mit dem _offset_-Wert kannst du anpassen, wann dieser Puls stattfindet.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

Eine Stärke von Liberation ist, dass es zufällige, aber wiederholbare Effekte erzeugen kann. Der _noise_-Oszillator kann verwendet werden, um eine organische, loopende Zufallsbewegung mit so viel Detail/Jitter zu erzeugen, wie du möchtest.

Siehe die Abschnitte oben für:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Spezifisch für Noise:

* **noise type** - der Algorithmus, mit dem das Rauschen erzeugt wird.
  * **SIMPLEX** - Standardwert; ein wellenförmiger Wert, der an- und abschwillt und sich in einem Loop wiederholt.
  * **RANDOM** - verwendet einen traditionelleren Zufallszahlen-Algorithmus, komplett verrauscht und chaotisch.

{% hint style="info" %}
**Simplex noise** wurde 2001 von Ken Perlin als Verbesserung seines „Perlin noise“-Algorithmus entwickelt, den er 1983 im Rahmen seiner Arbeit am Film _Tron_ entwickelte (wofür er einen Oscar gewann!).

Dieses sogenannte „Gradient“-Rauschen entstand aus seiner Frustration über zuvor sehr „maschinenhaft“ wirkende computergenerierte Bilder. In der CGI-Welt eignet es sich besonders gut zum Rendern von Wolken, Wasseroberflächen oder sogar Höhenkarten für realistisches Terrain.

In Liberation ist es aber vor allem gut für scheinbar unvorhersehbare Bewegungen, die trotzdem weich und organisch bleiben.
{% endhint %}

* **seed** - der Wert, mit dem das Rauschen erzeugt wird. Wenn dir das Aussehen der Noise-Welle nicht gefällt, probiere einen anderen Wert aus.

{% hint style="info" %}
Nerd-Fact! Um perfekt loopendes Simplex Noise zu bekommen, iteriere ich auf einer 2D-Noise-Ebene entlang eines Kreises. Wenn du den Seed-Wert änderst, verschiebst du diese Ebene durch eine 3. Dimension!
{% endhint %}

* **simplex detail** - ändert, wie detailliert oder jitterig das Rauschen ist. Wenn das sich wiederholende Muster weniger offensichtlich sein soll, erhöhe die Dauer und diesen Wert.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Erzeugt komplett benutzerdefinierte Wellenformen. Das ist sehr nützlich, um komplexe Animationen zu erstellen.

Siehe die Abschnitte oben für:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Darunter befindet sich eine Liste mit Positionen und Werten. Die Dauer ist in 64 Schritte unterteilt, und du kannst an jedem dieser Punkte einen Wert platzieren.

Jeder Schritt hat die folgenden Einstellungen:

* **Step** - der Zeitschritt innerhalb der Dauer. 0 ist am Anfang und 64 am Ende.
* **Level** - der Pegel der Welle an diesem Zeitschritt. Der Pegel liegt zwischen 0 und 1.
* **Animation type** - im Drop-down-Menü kannst du auswählen, wie du dich vom vorherigen Schritt zu diesem Level bewegen möchtest.
  * **None** - keine Übergangsanimation; springt zur angegebenen Zeit direkt auf dieses Level.
  * **Linear** - eine vollständig lineare Bewegung vom vorherigen Level zu diesem.
  * **Ease in / Ease out / Ease in/out** - eased vom vorherigen Level zu diesem. Eine Beschreibung der Animationstypen findest du oben unter _ease function_.

***
