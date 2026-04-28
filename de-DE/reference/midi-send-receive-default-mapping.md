---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Standardzuordnung für MIDI-Senden/-Empfangen

**Clip-Start und -Stopp werden durch MIDI Note On / Off auf den Kanälen 1 bis 14 ausgelöst**

Clips haben eine horizontale (x) und vertikale (y) Position. Klicke mit der rechten Maustaste auf einen Clip, dann siehst du seine Position. MIDI kann Clips ab 0,0 auslösen.

{% hint style="info" %}
Beachte, dass die Clip-Steuerung mit diesem System absolut ist und sich die Clip-Positionen nicht ändern, wenn du im Clip Deck scrollst.
{% endhint %}

MIDI-Kanal 1, Note 1 ist Clip 0,0, Note 2 ist Clip 0,1, Note 3 ist Clip 0,2; die Zuordnung läuft nach unten durch die Zeilen und dann weiter über die Spalten. Sobald 128 erreicht ist, wechselt sie zum nächsten Kanal und beginnt erneut. Damit hast du insgesamt 128 x 14 = 1792 Clips, die über MIDI erreichbar sind.

MIDI-Note für Clip-Koordinaten:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Note : 1</td><td>Note : 6</td><td>Note : 11</td><td>Note : 16</td><td>Note : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Note : 2</td><td>Note : 7</td><td>Note : 12</td><td>Note : 17</td><td>...etc</td></tr><tr><td><strong>y : 2</strong></td><td>Note : 3</td><td>Note : 8</td><td>Note : 13</td><td>Note : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Note : 4</td><td>Note : 9</td><td>Note : 14</td><td>Note : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Note : 5</td><td>Note : 10</td><td>Note : 15</td><td>Note : 20</td><td></td></tr></tbody></table>

Beachte, dass ein MIDI-Note-On-Event den Clip startet und das entsprechende Note-Off-Event den Clip stoppt. Das gilt unabhängig vom Trigger Mode der Gruppe. Das System wurde ursprünglich für Wiedergabe und Aufnahme entwickelt; daher wäre es unerwünscht gewesen, wenn Noten einen Clip umschalten würden.

### **Effekte**

MIDI-Control-Change-Nachrichten (CC) auf **Kanal 15** steuern die Effekte.\
Effekt 1 verwendet CC 0-3, Wert 0-127\
Effekt 2 verwendet CC 4-7, Wert 0-127\
Effekt 3 verwendet CC 8-11, Wert 0-127\
… und so weiter.

Jede Vierergruppe steuert den Level und 3 Parameter dieses Effekts:

<table><thead><tr><th width="164">Effekt :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Level</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...etc</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Globale Einstellungen**

MIDI-Control-Change-Nachrichten auf **Kanal 16** ändern die globalen Einstellungen:\
CC 1 : Shift X (horizontal) 0 -127, 64 liegt in der Mitte\
CC 2 : Shift Y (vertikal) 0 -127, 64 liegt in der Mitte\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Und besonders wichtig:\
CC 15 : Global brightness

Bitte beachte, dass dieses System ursprünglich für Aufnahme und Wiedergabe entwickelt wurde, damit du mit Logic, Ableton oder einer anderen DAW Timeline-Animationen erstellen kannst. Du kannst es zwar für die Live-Steuerung verwenden, es wurde aber nicht für diesen Einsatz optimiert. Im Vergleich zum APC40-Setup fehlen einige Funktionen für die Live-Steuerung.
