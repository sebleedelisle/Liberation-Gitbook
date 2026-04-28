---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Tempo mit einer Audiospur synchronisieren

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Tempo mit einer Audiospur synchronisieren" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

Die Timeline von Liberation ist für feste und wechselnde Tempi ausgelegt. Eine zuverlässige Synchronisation beginnt aber immer damit, das Tempo zu finden und das Audio korrekt auszurichten. Dieser Abschnitt beschreibt den empfohlenen Workflow.

#### 1. Den ersten Downbeat ausrichten

Füge deine Audiospur zur Timeline hinzu und stelle sicher, dass sie auf einen Beat einrastet, sodass der **erste musikalische Downbeat** der Spur exakt am Anfang eines Takts liegt.

Dieser Schritt ist entscheidend.

Wenn das Audio nicht von selbst auf einem Downbeat beginnt, hast du zwei Möglichkeiten:

* **Clip-Verzögerung anpassen**\
  Klicke mit der rechten Maustaste auf den Audio-Clip und passe den Wert für Delay an, bis der erste Downbeat mit einem Beat- oder Taktmarker übereinstimmt.
* **Audio extern zuschneiden**\
  Bearbeite die Audiodatei in einem externen Editor wie Audacity, sodass die Datei exakt auf dem ersten Downbeat beginnt, und importiere sie anschließend erneut.

{% hint style="info" %}
**Wichtig:**\
Wenn der Anfang des Audios nicht auf einen Beat oder Takt ausgerichtet ist, verschiebt sich die wahrgenommene Startposition der Musik vor und zurück, sobald du das Tempo änderst. Dadurch wird eine genaue Tempoanpassung extrem schwierig.
{% endhint %}

#### 2. Ein Starttempo festlegen

Wenn du eine ungefähre BPM-Zahl kennst, gib sie in die Tempo-Steuerung der Timeline ein und starte die Wiedergabe von Anfang an.

Beobachte die Beat- und Taktmarker genau, während die Spur abgespielt wird.

* Wenn die Marker der Musik vorauslaufen, reduziere das Tempo leicht.
* Wenn sie hinterherlaufen, erhöhe das Tempo leicht.
* Stoppe die Wiedergabe, passe das Tempo an und versuche es erneut.

Bei den meisten modernen Musikstücken ist das Tempo ein fester ganzzahliger BPM-Wert. Sobald du den richtigen Wert gefunden hast, sollte er für die gesamte Spur synchron bleiben.

#### 3. Die Wellenform als visuelle Hilfe nutzen

Die Audio-Wellenform ist eine hilfreiche Referenz beim Anpassen des Tempos.

* Transienten und Peaks sollten mit den vertikalen Taktmarkern übereinstimmen.
* Zoome nah heran, um die Ausrichtung über mehrere Takte hinweg zu prüfen.

**Tipp:**\
Verwende das Mausrad oder eine Trackpad-Geste, um die Timeline zu zoomen. Verwende das horizontale Scrollrad oder die entsprechende Geste, um nach links und rechts zu navigieren. Herangezoomt zu arbeiten macht kleine Anpassungen deutlich einfacher.

#### 4. Spuren mit nicht-ganzzahligem BPM-Wert

Wenn die Spur keinen ganzzahligen BPM-Wert verwendet, driftet die Synchronisation langsamer auseinander.

* Zoome weiter hinein.
* Verwende kleinere Tempoanpassungen.
* Prüfe die Ausrichtung über längere Abschnitte der Spur hinweg, nicht nur über die ersten paar Takte.

#### 5. Musik mit Tempowechseln

Wenn die Musik schneller oder langsamer wird, verwende die Tempo Map:

* Spiele die Spur ab und beobachte die Beat-Marker.
* Wenn eine Abweichung sichtbar wird, füge an dieser Stelle einen Tempowechsel hinzu.
* Passe das Tempo für den neuen Abschnitt an, bis er wieder synchron läuft.

Wiederhole diesen Vorgang für jeden Tempowechsel in der Musik.

#### 6. Externe Tempoanalyse (optional)

Als letzte Möglichkeit kannst du die Spur in einer DAW wie Logic Pro analysieren und automatisch eine Tempo Map erzeugen. Beachte, dass dabei häufig sehr viele Tempowechsel entstehen, manchmal einer pro Takt. Das kann für die meisten Shows detaillierter sein als nötig.
