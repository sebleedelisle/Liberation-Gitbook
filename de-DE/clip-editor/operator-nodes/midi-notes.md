---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Erzeugt Effekte im Stil einer „Laserharfe“, bei denen eingehende MIDI-Noten Beams oder Formen über einen Bereich hinweg auslösen. Der Node verwendet den Content, den du ihm übergibst, als _Quelle_ für jede Note: Gibst du ihm einen Punkt, erhältst du eine Reihe von Punkten. Gibst du ihm eine Form wie einen Kreis, erhältst du eine Reihe von Kreisen, und komplexere Formen werden genauso repliziert.

Du kannst in **Liberation → Settings** (`Cmd / Ctrl + ,`) auswählen, auf welches MIDI-Interface Liberation hört.

* **midi channel** – welcher MIDI-Kanal abgehört wird (0 = alle Kanäle, 1–16 = bestimmter Kanal)
* **width** – die Gesamtbreite, über die die Noten verteilt werden.
* **midi note min / max** – die niedrigsten und höchsten MIDI-Notenwerte im Bereich.
* **ignore out of range notes** – filtert alle Noten außerhalb des festgelegten Bereichs heraus. Wenn deaktiviert, werden Noten außerhalb des Bereichs auf die nächstverfügbare Note „geklemmt“: Hohe Noten lösen das obere Ende des Bereichs aus, niedrige Noten das untere Ende.
* **auto extend range** – erweitert den Bereich automatisch, wenn Noten außerhalb davon gespielt werden.

{% hint style="info" %}
Nicht sicher, welchen Notenbereich du bekommst? Aktiviere **auto extend range**, setze **midi note min** sehr hoch und **midi note max** sehr niedrig, und spiele dann deine Noten durch. Das System erfasst sie alle und erweitert den Bereich für dich. Sobald du alles hast, schaltest du **auto extend range** einfach wieder aus, um den Bereich zu fixieren.
{% endhint %}

* **leave all notes visible** – erzeugt Beams oder Formen für alle Noten im Bereich, unabhängig davon, ob sie gerade gespielt werden. Dadurch entsteht ein „Laserharfen“-Effekt.
* **hit colour** – die Farbe, die erscheint, wenn eine Note ausgelöst wird.
* **hit colour hold time** – wie lange die Hit-Farbe mit voller Helligkeit gehalten wird, bevor sie ausblendet. Der Wert ist in Sekunden (0–1). _100% = 1 Sekunde._
* **hit colour decay time** – wie lange es dauert, bis die Hit-Farbe nach der Haltezeit wieder zurückfadet. Der Wert ist in Sekunden (0–1). _100% = 1 Sekunde._

{% hint style="info" %}
Wenn dein Content bereits reinweiß ist, macht es keinen Unterschied, **hit colour** auf Weiß zu setzen. Für die besten Ergebnisse verwendest du eine gesättigte Farbe für deinen Content und setzt **hit colour** auf Weiß – das erzeugt einen sehr schönen Flash-Effekt, wenn Noten ausgelöst werden.
{% endhint %}

* **note off fade out time** – wie lange die Note nach dem Loslassen ausblendet. Der Wert ist in Sekunden (0–1). _100% = 1 Sekunde._
* **hit scale factor** – wie stark die Note beim Auslösen vergrößert wird (z. B. 2 = doppelte Größe).
* **hit scale hold time** – wie lange die Note vergrößert bleibt, bevor sie wieder zurückschrumpft. Der Wert ist in Sekunden (0–1). _100% = 1 Sekunde._
* **hit scale decay time** – wie lange es dauert, bis die Note wieder zu ihrer ursprünglichen Größe zurückkehrt. Der Wert ist in Sekunden (0–1). _100% = 1 Sekunde._
* **note off shrink time** – wie lange es dauert, nach dem Loslassen der Note wieder auf die ursprüngliche Größe zurückzuschrumpfen. Der Wert ist in Sekunden (0–1). _100% = 1 Sekunde._ (Hat keine Wirkung, wenn **leave all notes visible** aktiviert ist.)

{% hint style="info" %}
Skalierung – Beachte: Wenn dein Content nur aus einem einzelnen Punkt besteht, hat die Skalierung keine Wirkung!
{% endhint %}
