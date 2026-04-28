---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Standard-mapping for MIDI send/receive

**Clip til og fra udløses af MIDI note on/off på kanal 1 til 14**

Clips har en vandret (x) og lodret (y) position. Højreklik på en Clip, så kan du se dens position. MIDI kan udløse Clips med start ved 0,0.

{% hint style="info" %}
Bemærk, at Clip-styring med dette system er absolut, og at Clip-positionerne ikke ændrer sig, når du ruller i Clip Deck.
{% endhint %}

MIDI-kanal 1, note 1 er Clip 0,0, note 2 er Clip 0,1, og note 3 er Clip 0,2. Det fortsætter ned gennem rækkerne og videre langs kolonnerne. Når den når til 128, går den videre til næste kanal og starter forfra. Du har altså i alt 128 x 14 = 1792 Clips, som kan tilgås via MIDI.

MIDI-note for Clip-koordinater:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Note : 1</td><td>Note : 6</td><td>Note : 11</td><td>Note : 16</td><td>Note : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Note : 2</td><td>Note : 7</td><td>Note : 12</td><td>Note : 17</td><td>...osv.</td></tr><tr><td><strong>y : 2</strong></td><td>Note : 3</td><td>Note : 8</td><td>Note : 13</td><td>Note : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Note : 4</td><td>Note : 9</td><td>Note : 14</td><td>Note : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Note : 5</td><td>Note : 10</td><td>Note : 15</td><td>Note : 20</td><td></td></tr></tbody></table>

Bemærk, at en MIDI note on-hændelse starter Clippen, og den tilsvarende note off-hændelse stopper Clippen. Dette gælder uanset trigger mode på gruppen. Systemet blev oprindeligt designet til afspilning og optagelse, så det ville have været uhensigtsmæssigt, hvis noderne skiftede en Clip til og fra.

### **Effekter**

MIDI control change-meddelelser (CC) på **kanal 15** justerer effekterne.\
Effekt 1 bruger CC 0-3, værdi 0-127\
Effekt 2 bruger CC 4-7, værdi 0-127\
Effekt 3 bruger CC 8-11, værdi 0-127\
… og så videre.

Hver gruppe på fire styrer niveauet og 3 parametre for den pågældende effekt:

<table><thead><tr><th width="164">Effekt :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Niveau</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...osv.</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Globale indstillinger**

MIDI control change-meddelelser på **kanal 16** ændrer de globale indstillinger:\
CC 1 : Shift X (vandret) 0 -127, 64 er i midten\
CC 2 : Shift Y (lodret) 0 -127, 64 er i midten\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Og vigtigt:\
CC 15 : Global brightness

Bemærk, at dette system oprindeligt blev designet til optagelse og afspilning, så du kan bruge Logic, Ableton eller en anden DAW til at oprette timeline-animationer. Selvom du kan bruge det til live-styring, er det ikke optimeret til den brug, og nogle funktioner til live-styring mangler sammenlignet med APC40-opsætningen.
