---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Standardmappning för MIDI-sändning/-mottagning

**Clip startas och stoppas av MIDI note on / off på kanalerna 1 till 14**

Clips har en horisontell (x) och vertikal (y) position. Högerklicka på ett Clip så ser du dess position. MIDI kan trigga Clips med början vid 0,0.

{% hint style="info" %}
Observera att Clip-styrning med det här systemet är absolut, och att Clip-positionerna inte ändras när du skrollar i Clip Deck.
{% endhint %}

MIDI-kanal 1, not 1 är Clip 0,0, not 2 är Clip 0,1 och not 3 är Clip 0,2. Det fortsätter nedåt i rader och sedan vidare i kolumner. När det når 128 går det vidare till nästa kanal och börjar om. Totalt har du alltså 128 x 14 = 1792 Clips som kan nås via MIDI.

MIDI-not för Clip-koordinater:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Not : 1</td><td>Not : 6</td><td>Not : 11</td><td>Not : 16</td><td>Not : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Not : 2</td><td>Not : 7</td><td>Not : 12</td><td>Not : 17</td><td>...osv.</td></tr><tr><td><strong>y : 2</strong></td><td>Not : 3</td><td>Not : 8</td><td>Not : 13</td><td>Not : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Not : 4</td><td>Not : 9</td><td>Not : 14</td><td>Not : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Not : 5</td><td>Not : 10</td><td>Not : 15</td><td>Not : 20</td><td></td></tr></tbody></table>

Observera att en MIDI note on-händelse startar Clip, och motsvarande note off-händelse stoppar Clip. Detta gäller oavsett vilket triggerläge som är valt för gruppen. Systemet utformades ursprungligen för uppspelning och inspelning, så det hade inte varit önskvärt att låta noter växla ett Clip av/på.

### **Effekter**

MIDI control change-meddelanden (CC) på **kanal 15** justerar effekterna.\
Effekt 1 använder CC 0-3, värde 0-127\
Effekt 2 använder CC 4-7, värde 0-127\
Effekt 3 använder CC 8-11, värde 0-127\
… och så vidare.

Varje grupp om fyra styr nivån och 3 parametrar för den effekten:

<table><thead><tr><th width="164">Effekt:</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Nivå</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...osv.</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Globala inställningar**

MIDI control change-meddelanden på **kanal 16** ändrar de globala inställningarna:\
CC 1 : Shift X (horisontellt) 0 -127, 64 är i mitten\
CC 2 : Shift Y (vertikalt) 0 -127, 64 är i mitten\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Och viktigt:\
CC 15 : Global brightness

Observera att det här systemet ursprungligen utformades för inspelning och uppspelning, så att du kan använda Logic, Ableton eller en annan DAW för att skapa tidslinjebaserade animationer. Även om du kan använda det för live-styrning är det inte optimerat för det användningsområdet, och vissa funktioner för live-styrning saknas jämfört med APC40-konfigurationen.
