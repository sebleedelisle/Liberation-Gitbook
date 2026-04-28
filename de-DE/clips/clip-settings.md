---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip-Einstellungen

### Clip-Einstellungen-Panel

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Das Clip-Einstellungen-Panel</p></figcaption></figure>

Ändere die Ausgabegröße des Clips mit _Scale X_ und _Scale Y_. Beide sind miteinander gekoppelt, außer du hältst die _SHIFT_-Taste gedrückt.

Ändere die horizontale und vertikale Position des Clips mit _Shift X_ und _Shift Y_.

_Zone Delay/Chase_ ist ein so praktisches Feature, dass es einen eigenen Abschnitt bekommt: [zone-delay-chase.md](zone-delay-chase.md "mention")

### Clips sperren

Wenn ein Clip gesperrt ist, kann er nicht verschoben oder gelöscht werden. Um einen Clip zu sperren, verwende die Checkbox _Locked_ im Rechtsklick-Menü. Im Clip-Einstellungen-Panel bekommst du noch ein paar weitere Optionen.

* _UNLOCK ALL -_ entsperrt jeden Clip im Clip Deck.
* _AUTO-LOCK_ - wenn _Auto-Lock_ aktiviert ist, wird jeder Clip, der automatisch abgespielt wird (entweder über die Timeline oder das MIDI-Aufnahme-/Wiedergabesystem), gesperrt. Das ist nützlich, wenn du eine Show in Logic Pro (oder etwas Ähnlichem) programmiert hast und die in der Show verwendeten Clips nicht versehentlich bearbeiten möchtest.
* _LOCKED CLIPS ZONES_ - wenn diese Option aktiviert ist, kannst du die Zonen für gesperrte Clips nicht ändern.
* _LOCKED CLIPS PARAMS_ - wenn diese Option aktiviert ist, kannst du die Parameter (Scale, Shift usw.) für gesperrte Clips nicht ändern.

### Rechtsklick-Menü

Wenn du mit der rechten Maustaste auf einen Clip klickst, erscheint ein Menü mit einigen Optionen für diesen Clip. Siehe [clip-editor-intro.md](../clip-editor/clip-editor-intro.md "mention"), [clip-settings.md](clip-settings.md "mention") und [groups.md](groups.md "mention") für mehr Informationen zu den ersten Einträgen in diesem Menü.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>Das Rechtsklick-Menü für Clip-Einstellungen</p></figcaption></figure>

### Retrigger

Clips sind standardmäßig auf _retrigger_ eingestellt. Das bedeutet: Egal, wann du den Clip startest, er beginnt ab genau diesem Moment zu laufen. Wenn du ihn also zu spät startest, ist die Animation des Clips leicht verspätet und nicht mehr exakt im Timing.

{% hint style="info" %}
Wenn du _Tap Tempo_ verwendest, während ein Clip mit Retrigger läuft, „quantisiert“ das System den Clip wieder ins Timing, auch wenn du ihn nicht exakt auf den Beat gestartet hast.
{% endhint %}

Wenn _Retrigger_ nicht aktiviert ist, bleibt der Clip immer im Timing – so, als wäre er ganz am Anfang der Clock gestartet worden. Das ist praktisch, wenn du über ein externes Clock-Signal perfekt mit der Musik synchronisiert bist.

{% hint style="info" %}
Clips sind oft so gestaltet, dass sie endlos loopen. Du kannst sie aber auch so bauen, dass sie nur einmal oder nur ein paar Durchläufe lang laufen. Achte darauf, solche Clips auf _retrigger_ zu lassen, sonst starten sie nicht neu!
{% endhint %}

### Transition in/out time (Fade)

Clips können so eingestellt werden, dass sie mit einer in Sekunden gemessenen Dauer ein- und ausblenden. Standardmäßig wird die Fade-Zeit von den Gruppeneinstellungen übernommen (und kann per Rechtsklick auf den Gruppen-Button geändert werden).

Wenn du eine andere Fade-Dauer als die der Clip-Gruppe verwenden möchtest, deaktiviere zuerst den Button _USE GROUP DEFAULT_ und passe dann die Slider _In time_ und _Out time_ des Clips an.
