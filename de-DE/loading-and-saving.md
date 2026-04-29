---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Laden und Speichern

Liberation speichert seinen Zustand ständig auf der Festplatte. So kannst du sicher sein, dass es nach einem Stromausfall oder Systemproblem genau dort weiterläuft, wo es aufgehört hat. Deine Zonen, Timeline oder andere Inhalte solltest du nie verlieren.

Du kannst dein Setup aber auch exportieren, um es zu sichern oder auf einen anderen Computer zu übertragen.

### Projekt-Import/-Export

Die Projektdatei speichert fast alles aus deinem aktuellen Setup, einschließlich:

* Alles, was unten unter [#laser-settings-import-export](loading-and-saving.md#laser-settings-import-export "mention") beschrieben ist
* Clips, Effekte und Gruppeneinstellungen
* Alle deine Timelines (ohne Audio- und Videomedien)
* Art-Net-Setup
* MIDI-Sende-/Empfangseinstellungen
* Tempo- / Synchronisationseinstellungen

Derzeit werden nicht gespeichert und geladen:

* Sound- und MIDI-Eingangseinstellungen, wie sie im MIDI-Notes-Node und im Sound Input Oscillator verwendet werden (MIDI-Sende-/Empfangseinstellungen sowie der Timecode-Soundeingang werden _gespeichert_)
* Interface-Skalierung
* Medien für Canvas-Hilfsbilder
* Sound- und Videomedien für Timelines
* Schriftarten, die im Text-Node verwendet werden

{% hint style="danger" %}
Sound- und Videodateien in der Timeline werden nicht mit Projektdateien gespeichert. Speichere sie daher separat, wenn du sie auf einen anderen Computer übertragen möchtest. Siehe [Laden und Speichern](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Laser-Settings Import / Export

* Laser-Einstellungen für jeden Laser
* Beam-Zonen
* Canvas-Zielbereiche
* DMX-Zonen
* Zuweisung von Laser-Controllern (und Aliasse für Controller, die du umbenannt hast)
* Laser-Scanner- und Farbkalibrierungseinstellungen sowie Presets
* 3D Visualiser-Einstellungen und Presets

### Clip Deck Import / Export

* Alle Clips mit ihren Zonenzuweisungen, Einstellungen und Parametern
* Alle Gruppeneinstellungen, Flash Mode, Fade-In-/Fade-Out-Zeiten usw.

Derzeit werden nicht gespeichert und geladen:

* Alle Effekte mit ihren Parametern und Einstellungen

{% hint style="info" %}
**Clips aus einer Projektdatei laden, ohne das gesamte Projekt zu laden**

Um nur die Clips aus einem Projekt zu importieren, wähle _**Clips->Import Clip Deck**_ und wähle statt einer Clip-Deck-Datei (.cpdk) eine Projektdatei.
{% endhint %}

### Clip Deck anhängen

Du kannst Clips aus einer exportierten Clip-Deck-Datei mit _Append Clip Deck_ zu deinem aktuellen Projekt hinzufügen. Die Clips werden am Ende deines aktuellen Clip Deck hinzugefügt, die Effekte und Gruppeneinstellungen in der Datei werden jedoch nicht importiert.

### Ausgewählte Clips exportieren

Alle aktuell ausgewählten Clips werden in eine Datei exportiert. Gruppeneinstellungen und Effekte werden nicht gespeichert, nur die Clips. Beachte, dass aktuell laufende aktive Clips nicht exportiert werden, sofern sie nicht ebenfalls ausgewählt sind.

{% hint style="info" %}
Option/Alt - shift - click Clips, um sie auszuwählen (oder verwende das Lasso). Ausgewählte Clips erkennst du an der dicken weißen Umrandung. Siehe [Clips starten / stoppen](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Effects Import / Export

Lädt und speichert alle Effekte zusammen mit ihren Gruppeneinstellungen und Parametern.

{% hint style="info" %}
**Effekte aus einer Projektdatei laden, ohne das gesamte Projekt zu laden**

Um nur die Effekte aus einem Projekt zu importieren, wähle _**Effects->Import Effects**_ und wähle statt einer Effektdatei (.efts) eine Projektdatei.
{% endhint %}

### Timeline-Export

Exportiert eine Timeline-Datei mit einer oder mehreren Timelines. Beachte, dass das Clip Deck immer in exportierten Timeline-Dateien enthalten ist (du kannst jedoch auswählen, welche Clips du wieder importierst, siehe [#timeline-import](loading-and-saving.md#timeline-import "mention") unten).

Wenn dein Projekt mehr als eine Timeline enthält, öffnet sich ein Panel, in dem du auswählen kannst, welche Timelines exportiert werden sollen.

{% hint style="danger" %}
Sound- und Videodateien in der Timeline werden nicht mit Timeline-Dateien gespeichert. Speichere sie daher separat, wenn du deine Inhalte auf einen anderen Computer übertragen möchtest. Siehe [Laden und Speichern](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Timeline-Import

Importiert eine oder mehrere Timelines aus einer einzelnen Timeline-Datei. Nachdem du deine Timeline-Datei ausgewählt hast, öffnet sich ein Panel mit mehreren Importoptionen.

Wenn die Timeline-Datei mehr als eine Timeline enthält, werden alle aufgelistet. Aktiviere die Timelines, die du übernehmen möchtest.

* Replace existing timelines\
  Löscht alle deine aktuellen Timelines und ersetzt sie durch die importierten
* Import used clips only\
  Importiert nur die verwendeten Clips und ordnet sie in Gruppen an, eine Gruppe pro Timeline. Wenn diese Option nicht ausgewählt ist, wird das gesamte Clip Deck der Timeline-Datei an deine vorhandenen Clips angehängt.
* Replace existing clip deck\
  Ersetzt dein aktuelles Clip Deck durch die Clips in der Timeline-Datei. Nur verfügbar, wenn _Replace existing timelines_ ausgewählt ist.

{% hint style="info" %}
**Timelines aus einer Projektdatei laden, ohne das gesamte Projekt zu laden**

Um nur die Timelines aus einem Projekt zu importieren, wähle _**Timeline->Import Timeline(s)**_ und wähle statt einer Timeline-Datei (.ltml) eine Projektdatei.
{% endhint %}

### DMX- / Art-Net-Import/-Export

Speichert und lädt die Art-Net-Nodes zusammen mit ihren IP-Adressen. Enthält außerdem die DMX-Zonen und alle deine DMX-Presets.

### Wichtiger Hinweis zu Timeline-Mediendateien

Sound- und Videodateien werden derzeit **nicht** mit der Timeline-Datei exportiert. Wenn du Inhalte auf einen anderen Computer verschieben musst, stelle daher sicher, dass du diese Dateien mitnimmst.

{% hint style="info" %}
**Wie eine Timeline nach Mediendateien sucht**

Wenn die Timeline geladen wird, sucht sie im selben Ordner wie die Timeline- oder Projektdatei sowie in allen Unterordnern. Solange sich die Dateien also im selben Ordner oder in einem Unterordner befinden (z. B. _/videos_ oder _/sound_), werden sie beim Laden gefunden.
{% endhint %}
