---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / Synchronisation

Musiksynchronisation ist ein grundlegender Bestandteil von Liberation. Sobald Tempo und Beats zur Musik passen, kannst du sicher sein, dass alles synchron läuft. Wenn du MIDI Clock (oder Ableton Link) nutzen kannst, musst du dich um manuelle Synchronisation gar nicht kümmern. Falls nicht, kein Problem: Mit der _Live_-Tempo-Funktion kannst du das Tempo manuell angleichen.

Wenn du Erfahrung mit Musik- oder Lichtsoftware hast, wird dir dieser Ablauf vertraut vorkommen. Wenn nicht, lohnt es sich, das System in Ruhe kennenzulernen und zu Hause zu üben, bevor du damit in eine Live-Show gehst.

## Tempo-Panel

Das _Tempo_-Panel ist immer auf dem Bildschirm sichtbar und enthält alle Synchronisationseinstellungen. Oben siehst du den aktuellen Takt/Beat-Zähler sowie eine Transportsteuerung mit Play/Pause- und Zurückspulen/Vorspulen-Buttons.

Darunter siehst du den Beat-Marker: vier Quadrate, die zum Beat „pulsieren“. Dieser _Beat-Marker_ ist eine extrem hilfreiche Visualisierung, auf die du beim Arbeiten mit dem _Live_-Tempo-System ständig zurückgreifen wirst.

### Tempo einstellen

Du hast mehrere Möglichkeiten, das Tempo einzustellen:

* Klicke auf den _Tempo_-Slider und ziehe ihn
* Shift-klicke auf den _Tempo_-Slider und ziehe ihn, um das Tempo in 0,1-Schritten zu ändern
* Doppelklicke auf den _Tempo_-Slider und gib den Wert manuell ein
* Verwende den _Tempo_-Knob am APC40 (drücke Shift für 0,1-Schritte)
* Tap Tempo

{% hint style="info" %}
Tempo wird in „beats per minute“ angegeben. Der klassische Standardwert ist meist 120.
{% endhint %}

## Tap Tempo

Stelle das Tempo automatisch ein, indem du den _TAP_-Button im Takt des Beats klickst. Setze den Anfang des Takts mit dem _RESET_-Button.

{% hint style="info" %}
Das Tap-Tempo-System ist intelligent genug, um zu erkennen, wenn du eine Weile mit dem Tippen pausiert oder ein paar Beats ausgelassen hast. Wenn du in Double Time zu tippen beginnst, versteht es, dass du das Tempo verdoppeln möchtest. Dasselbe gilt, wenn du in Half Time tippst.

Es erkennt außerdem, wenn zwei Personen gleichzeitig das Tempo tippen (z. B. eine über die Tastatur und eine am APC40). Liberation mittelt die doppelten Taps.
{% endhint %}

#### Tastaturbefehle:

T - Tap Tempo\
R - Takt zurücksetzen\
Y - Tempo auf den nächsten ganzen Beat pro Minute runden.

{% hint style="info" %}
Da die meiste Musik heute digital erstellt wird, ist das Tempo wahrscheinlich eine gerundete ganze Zahl. Wenn ein getapptes Tempo also schon nahe dran ist, verwende die Y-Taste (oder bewege den APC40-Tempo-Knob um einen „Tick“), um es auf eine ganze Zahl zu runden.
{% endhint %}

#### APC40-Steuerung:

Der APC40 hat einen eigenen _TAP TEMPO_-Button. Alternativ kannst du auch einen angeschlossenen Fußschalter verwenden und mit dem Fuß tappen!

Verwende den _TEMPO_-Knob zum Anpassen. Drücke _SHIFT_, während du den _TEMPO_-Knob verwendest, um Feineinstellungen vorzunehmen.

Verwende den _METRONOME_-Button, um **den Takt zurückzusetzen**. (Beachte, dass der _METRONOME_-Button auch im Takt des Beats aufleuchtet.)

Drehe den _TEMPO_-Knob um einen „Tick“ nach rechts oder links, um **das Tempo** auf eine ganze BPM-Zahl auf- oder abzurunden.

Siehe auch [apc40-reference.md](reference/apc40-reference.md "mention")

### Tempo per Nudge korrigieren

Wenn du sicher bist, dass du nah genug am tatsächlichen Tempo bist, aber merkst, dass du aus dem Timing driftest, verwende die _NUDGE_-Buttons zur Korrektur.

Wenn das Liberation-Tempo der Musik vorausläuft, halte _NUDGE -_ gedrückt, um es vorübergehend zu verlangsamen, bis es wieder ausgerichtet ist.

Wenn das Liberation-Tempo hinter der Musik zurückbleibt, halte _NUDGE +_ gedrückt, um es vorübergehend zu beschleunigen, bis es wieder ausgerichtet ist.

{% hint style="info" %}
Du kannst entweder die NUDGE-Buttons auf dem Bildschirm oder die entsprechenden Buttons am APC40 verwenden.
{% endhint %}

### Half Time / Double Time

Verwende die _÷2_- und _x2_-Buttons, um das Tempo dauerhaft zu halbieren oder zu verdoppeln. Anders als beim Tempo Multiplier ist dies eine dauerhafte Änderung des aktuellen Tempos.

## Tempo Multiplier

Mit dem _Tempo Multiplier_-System kannst du das Tempo vorübergehend anpassen und anschließend zum vorherigen Wert zurückkehren.

Schalte den _Tempo Multiplier_ mit dem _TEMPO MULTIPLIER_-Button oder dem _BANK_-Button am APC40 ein bzw. aus. Passe ihn über den Bildschirm-Slider oder den APC40 A-B slider an. Oder verwende die Preset-Buttons _25%, 50%, 100% 200%_.

## Externe Tempoquellen

### MIDI Clock

Um zu einem externen MIDI-Clock-Signal zu synchronisieren, wähle den _MIDI CLOCK_-Radiobutton und wähle das MIDI-Gerät im Dropdown-Menü aus. Beachte die farbige Statusanzeige neben den Dropdown-Menüs:

* Grün - empfängt ein MIDI-Clock-Signal
* Orange - kann eine Verbindung zum MIDI-Gerät herstellen, empfängt aktuell aber kein Clock-Signal
* Rot - kann keine Verbindung zum MIDI-Gerät herstellen

{% hint style="info" %}
MIDI Clock sendet eine Reihe von Frames (24 pro Viertelnote), aber die Nachrichten enthalten keine Positionsdaten. Das bedeutet, dass es hilfreich ist, um im Timing zu bleiben, du den Takt aber möglicherweise trotzdem zurücksetzen musst.

Die Liberation-MIDI-Clock-Tempoquelle reagiert außerdem auf **MIDI Machine Control (MMC)**-Nachrichten. Wenn deine Clock-Quelle diese sendet, musst du den Takt nicht manuell zurücksetzen.
{% endhint %}



### Timeline

Jede Timeline hat ihr eigenes Tempo. Dieses kann ein fester Wert oder eine _Tempo Map_ sein. Mit der _Tempo Map_ kannst du das Tempo zu bestimmten Zeitpunkten innerhalb der Timeline anpassen.

Das Timeline-Tempo wird verwendet, wenn _TIMELINE_ als Tempoquelle ausgewählt ist.

{% hint style="info" %}
Du kannst eine Timeline mit _jeder_ Tempoquelle laufen lassen! Wenn du also eine Live-Band hast, die nicht zu einem Klick spielt, kannst du die Timeline manuell starten und sie mit der _LIVE_-Tempoquelle synchron halten. Oder wenn du ein MIDI-Clock-Signal hast, kannst du dieses verwenden!
{% endhint %}
