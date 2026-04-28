---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Füllungen, Masken und Tiefensortierung

### Konturen, Füllungen und Masken

Du wirst feststellen, dass einige Creator-Nodes eine _Fill state_-Option haben. Du kannst sie mit einer Kontur (einem Umriss), als Maske (die darunterliegende Inhalte abdeckt) oder mit beidem zeichnen.

Wenn du eine Form als Maske renderst, ist es so, als wäre sie mit Schwarz gefüllt, und alles darunter wird verdeckt.

{% hint style="info" %}
Eine Linie (oder _Kontur_) mit einem Laser zu zeichnen, ist ziemlich einfach: Du scannst den Laser vom Anfang der Linie bis zum Ende der Linie. Schon hast du deine Linie!

Gefüllte Formen sind allerdings schwieriger. Wenn du eine Form mit Farbe füllen möchtest, könntest du manuell schraffieren, indem du Linien zeichnest und die Fläche damit füllst. Liberation kann das aber (noch) nicht automatisch. Und selbst wenn wir das könnten, würdest du darunterliegende Linien weiterhin durchscheinen sehen.

Was wir aber tun können: Formen mit _Schwarz_ füllen. Unter der Haube führt Liberation alle Berechnungen aus, um Inhalte zu entfernen, die unter der schwarz gefüllten Form liegen. Und glaub mir: Das ist ziemlich knifflig!

Es funktioniert aber sehr gut und erzeugt die Illusion einer schwarz gefüllten Form.
{% endhint %}

### Tiefensortierung

Da einige Formen andere Formen _überdecken_ können, muss Liberation sie nach ihrer Tiefe sortieren. Standardmäßig werden Elemente anhand ihrer z-Position tiefensortiert. Wenn sie sich an derselben z-Position befinden, werden sie anhand ihrer Ebenenposition sortiert. Diese kannst du mit den Buttons _MOVE TO FRONT_ und _MOVE TO BACK_ innerhalb jedes Creators ändern.
