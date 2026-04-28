---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Scanner-Spezifikationen und Liberation

### Die unübersichtliche Realität von Scanner-Spezifikationen

Punktraten und Scanner-Spezifikationen können etwas verwirrend sein. Du siehst oft Angaben wie 30kpps @ 8º oder 50kpps @ 4º, aber was diese Zahlen tatsächlich bedeuten, ist nicht immer offensichtlich.

{% hint style="info" %}
Hinweis: Ich bin kein Spezialist für Scanner-Hardware, habe aber jahrelange praktische Erfahrung damit, Scanner unterschiedlichster Qualität über Software und Point-Stream-Erzeugung gut aussehen zu lassen, statt sie über Hardware-Tuning zu optimieren. Das hier basiert auf dieser Erfahrung.
{% endhint %}

#### **Woher diese Zahlen kommen**

Begriffe wie „30K“ und „50K“ sind Kurzformen dafür, wie Scanner mit dem ILDA-Testmuster bei diesen Punktraten unter bestimmten Bedingungen bewertet werden.

Wenn ein Scanner zum Beispiel mit _30Kpps @ 8°_ angegeben ist, bedeutet das eigentlich:

> „Dieser Scanner kann das ILDA-Testmuster bei 30.000 Punkten/Sek. und einem Scanwinkel von 8° korrekt wiedergeben, wenn er richtig eingestellt ist.“

Das ist keine umfassende oder vollständig standardisierte Messung der realen Leistung. Tatsächlich war es ursprünglich gar nicht als Benchmark gedacht, sondern wurde für einen **Abstimmvorgang** verwendet. Du gibst ein bekanntes Muster mit einer festen Punktrate aus (z. B. 30.000 Punkte/Sek.) und passt Dämpfung und Gain an, bis es korrekt aussieht.

Trotzdem ist es die am weitesten verbreitete Referenz, die wir haben, und sie kann dir eine gute Vorstellung von der Qualität der Scanner geben, zumindest bei seriösen Herstellern. Bei _weniger seriösen_ Herstellern allerdings ...

#### Wenn du die Scanner so testen willst, wie sie angegeben sind

{% hint style="danger" %}
**Das ist eine fortgeschrittene Technik, und du kannst deine Scanner beschädigen, wenn du nicht vorsichtig bist. Nicht empfohlen, außer du weißt genau, was du tust.**
{% endhint %}

Du brauchst Software, die das [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) ausgeben kann – ich glaube, LaserShowGen kann das eventuell – und musst die Ausgabegröße an den angegebenen Scanwinkel anpassen (z. B. 8°). Hinweise zur Analyse der Ausgabe findest du in der ILDA-Dokumentation.

#### Warum es möglicherweise kein guter Benchmark ist

Zunächst einmal kann dein Testmuster falsch aussehen, selbst wenn deine Scanner gut sind, weil sie nicht so eingestellt sind, dass sie dafür optimiert sind.

Es kann eine nützliche allgemeine Orientierung für „gute“ im Vergleich zu „schlechten“ Scannern sein, aber Hersteller nehmen es mit diesen Spezifikationen manchmal nicht ganz genau.

#### Wie wähle ich also einen guten Scanner aus?

Ich würde vor allem darauf achten, dass sie von einem seriösen Hersteller kommen. Teure High-End-Scanner-Hersteller wie Cambridge Technology (CT), Eye Magic (EMS) und ScannerMAX (eine Tochterfirma von Pangolin) sind immer gut, da kannst du kaum etwas falsch machen. Aber wenn ein Scannerpaar etwa 1000 $ kostet, ist das für viele von uns am Anfang teurer als unsere Laser!

Deshalb habe ich meistens chinesische Hersteller verwendet. Dragon Tiger (DT) Scanner sind ordentlich und bezahlbar, und ich glaube, LightSpace verwendet sie. Viele andere Hersteller (einschließlich OPT und Able in einigen Modellen) verwenden ebenfalls DT-basierte Systeme.

Phenix Technology (PT) ist im Allgemeinen eine niedrigere Klasse, aber ehrlich gesagt sind sie für die meisten Dinge wahrscheinlich völlig in Ordnung.

**Wenn deine Scanner unbranded sind, solltest du dir wahrscheinlich Gedanken über die Qualität machen!**

#### Wie Liberation hilft

Zunächst einmal brauchst du für die meisten Dinge keine wirklich teuren Scanner! Bezahlbare 30kpps DT oder sogar PT reichen aus. Die Standard-Scanner-Einstellungen sind bewusst konservativ, und in den meisten Fällen _solltest du sie nicht anpassen müssen_ (abgesehen von _Scanner sync_).

Auch wenn du bessere Scanner hast, bringt es nichts, sie stärker zu belasten als nötig. Das verlängert ihre Lebensdauer deutlich.

#### Was ist ein „Point Stream“?

Du hast diesen Begriff wahrscheinlich schon gehört – so steuern wir den Pfad der Scanner.

Ein Point Stream ist eine Liste von X/Y-Positionen, jeweils mit einer Farbe. Um zum Beispiel eine weiße Linie zu zeichnen, sendest du eine Folge von Punkten entlang dieser Linie, alle auf Weiß gesetzt. Die Scanner bewegen sich dann mit einer festen Rate von Punkt zu Punkt – der Punkte-pro-Sekunde-Rate (PPS) – und der Strahl zeichnet die Form nach.

#### Wie das in traditioneller Laser-Software funktioniert

Traditionelle Laser-Software speichert für jeden Cue einen Point Stream. Bei animierten Cues bedeutet das normalerweise einen separaten Point Stream für jeden Frame. Der entscheidende Punkt ist: Alles ist vollständig vorgegeben. Dadurch bewegen sich die Scanner bei einer höheren Punktrate schneller durch dieselben vorab definierten Daten.

{% hint style="info" %}
Bei älterer Software war dieser Ansatz notwendig – Computer waren schlicht nicht schnell genug, um Point Streams in Echtzeit zu erzeugen. Deshalb gibt es normalerweise einen separaten Cue-Editor, mit dem die Daten für jeden Frame einer Animation vorab erzeugt werden.

Das erklärt auch, warum Content mehrere Gigabyte Speicherplatz belegen kann. Im Grunde speicherst du große, unkomprimierte Wellenformen mit ziemlich hohen Abtastraten.
{% endhint %}

#### Warum „Punktrate“ in Liberation weniger aussagekräftig ist

Liberation erzeugt den Point Stream in Echtzeit, was uns enorm viel Flexibilität gibt. Beachte die Einstellung "Scanner speed" im Laser Settings Panel. Damit können wir die Scanner schneller oder langsamer machen, aber wichtig ist: Sie ändert **nicht** die zugrunde liegende Punktrate (PPS).

#### Moment, was? Wie?

Ich weiß, am Anfang klingt das seltsam.

Da Liberation den Point Stream in Echtzeit erzeugt, kann es diesen Point Stream anpassen. Je weiter die Punkte auseinanderliegen, desto schneller bewegen sich die Scanner. Je näher sie beieinanderliegen, desto langsamer bewegen sich die Scanner.

{% hint style="info" %}
In aktuellen Versionen von Liberation beeinflusst die tatsächliche _Punktrate_ (in den erweiterten Einstellungen) die Scanner-Geschwindigkeit überhaupt nicht. Stattdessen passt der Renderer die Punktverteilung an die ausgewählte Punktrate an, während die Bewegung der Scanner unverändert bleibt.

Das wirkt sich zwar auf die „Auflösung“ des Punktpfads aus, macht aber hauptsächlich bei Grafiken einen Unterschied (und kann bei der feineren Einstellung von _Scanner sync_ helfen).
{% endhint %}

#### Super! Was bedeutet das alles nun konkret?

Gute Frage. Hier sind meine Tipps:

* Vermeide unbranded Scanner. Wenn du schnellere Scanner bekommen kannst, nimm sie – mindestens 30KPPS.
* Für die meisten Fälle sind DT30-Scanner in Ordnung, und PT30-Scanner sind in günstigeren Lasern wahrscheinlich OK.
* Wenn du Grafiken machst, sind in den meisten Fällen mehr Laser besser als schnellere Scanner.
* Sobald du bei höherwertigen Setups ankommst, sind alle etablierten High-End-Marken in Ordnung.
* Wenn du nur die billigsten unbranded Scanner bekommen kannst: Die Standardeinstellungen von Liberation sind recht konservativ, und du wirst für einfache Beam-Arbeit wahrscheinlich OK-Ergebnisse bekommen. Wenn es Probleme gibt, reduziere die Einstellung **Speed** (aber ändere nicht die Punktrate!).

#### Und das ILDA Test Pattern?

... ist weiterhin sehr nützlich als Kalibrierungs- und Referenzwerkzeug, wurde aber nie als umfassender Benchmark entwickelt und kann von Herstellern missbraucht oder großzügig interpretiert werden.
