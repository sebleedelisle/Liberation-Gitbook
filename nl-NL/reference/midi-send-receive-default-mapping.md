---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Standaard MIDI-mapping voor verzenden/ontvangen

**Clips in- en uitschakelen wordt getriggerd door MIDI note on / off op kanalen 1 tot en met 14**

Clips hebben een horizontale (x) en verticale (y) positie. Klik met de rechtermuisknop op een clip om de positie te zien. MIDI kan clips triggeren vanaf 0,0.

{% hint style="info" %}
Let op: clipbesturing met dit systeem is absoluut. De clipposities veranderen dus niet wanneer je door de clip deck scrolt.
{% endhint %}

MIDI-kanaal 1, noot 1 is clip 0,0, noot 2 is clip 0,1, noot 3 is clip 0,2, waarbij de mapping omlaag door de rijen en verder langs de kolommen loopt. Zodra 128 is bereikt, gaat de mapping naar het volgende kanaal en begint opnieuw. In totaal zijn er dus 128 x 14 = 1792 clips via MIDI bereikbaar.

MIDI-noot voor clipcoördinaten:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Noot : 1</td><td>Noot : 6</td><td>Noot : 11</td><td>Noot : 16</td><td>Noot : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Noot : 2</td><td>Noot : 7</td><td>Noot : 12</td><td>Noot : 17</td><td>...enz.</td></tr><tr><td><strong>y : 2</strong></td><td>Noot : 3</td><td>Noot : 8</td><td>Noot : 13</td><td>Noot : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Noot : 4</td><td>Noot : 9</td><td>Noot : 14</td><td>Noot : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Noot : 5</td><td>Noot : 10</td><td>Noot : 15</td><td>Noot : 20</td><td></td></tr></tbody></table>

Let op: een MIDI note on-event start de clip, en het bijbehorende note off-event stopt de clip. Dit staat los van de trigger mode van de groep. Het systeem is oorspronkelijk ontworpen voor afspelen en opnemen, dus het zou ongewenst zijn geweest als noten een clip zouden toggelen.

### **Effecten**

MIDI control change-berichten (CC) op **kanaal 15** passen de effecten aan.\
Effect 1 gebruikt CC 0-3, waarde 0-127\
Effect 2 gebruikt CC 4-7, waarde 0-127\
Effect 3 gebruikt CC 8-11, waarde 0-127\
… enzovoort.

Elke groep van vier regelt het level en 3 parameters voor dat effect:

<table><thead><tr><th width="164">Effect :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Level</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...enz.</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Globale instellingen**

MIDI control change-berichten op **kanaal 16** wijzigen de globale instellingen:\
CC 1 : Shift X (horizontaal) 0 -127, 64 is het midden\
CC 2 : Shift Y (verticaal) 0 -127, 64 is het midden\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

En belangrijk:\
CC 15 : Global brightness

Let op: dit systeem is oorspronkelijk ontworpen voor opnemen en afspelen, zodat je Logic, Ableton of een andere DAW kunt gebruiken om tijdlijnanimaties te maken. Je kunt het wel gebruiken voor live-besturing, maar het is daar niet voor geoptimaliseerd. Bovendien ontbreken sommige functies voor live-besturing in vergelijking met de APC40-configuratie.
