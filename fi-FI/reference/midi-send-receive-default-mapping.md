---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ MIDI-lähetyksen ja -vastaanoton oletusmääritys

**Clipien käynnistys ja pysäytys laukaistaan MIDI note on / off -viesteillä kanavilla 1–14**

Clipeillä on vaaka- (x) ja pystysijainti (y). Napsauta Clipiä hiiren oikealla painikkeella, niin näet sen sijainnin. MIDI voi laukaista Clipejä alkaen kohdasta 0,0.

{% hint style="info" %}
Huomaa, että tällä järjestelmällä Clipien ohjaus on absoluuttista, eivätkä Clipien sijainnit muutu, kun vierität Clip Deckiä.
{% endhint %}

MIDI-kanava 1, nuotti 1 on Clip 0,0, nuotti 2 on Clip 0,1 ja nuotti 3 on Clip 0,2, edeten riveillä alaspäin ja sarakkeissa eteenpäin. Kun arvo saavuttaa 128, se siirtyy seuraavalle kanavalle ja alkaa alusta. Käytettävissä on siis yhteensä 128 x 14 = 1792 Clipiä MIDI:n kautta.

MIDI-nuotti Clipin koordinaateille:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nuotti : 1</td><td>Nuotti : 6</td><td>Nuotti : 11</td><td>Nuotti : 16</td><td>Nuotti : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nuotti : 2</td><td>Nuotti : 7</td><td>Nuotti : 12</td><td>Nuotti : 17</td><td>...jne</td></tr><tr><td><strong>y : 2</strong></td><td>Nuotti : 3</td><td>Nuotti : 8</td><td>Nuotti : 13</td><td>Nuotti : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nuotti : 4</td><td>Nuotti : 9</td><td>Nuotti : 14</td><td>Nuotti : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nuotti : 5</td><td>Nuotti : 10</td><td>Nuotti : 15</td><td>Nuotti : 20</td><td></td></tr></tbody></table>

Huomaa, että MIDI note on -tapahtuma käynnistää Clipin ja vastaava note off -tapahtuma pysäyttää sen. Tämä ei riipu ryhmän trigger-tilasta. Järjestelmä suunniteltiin alun perin toistoa ja tallennusta varten, joten nuottien käyttäminen Clipin päälle/pois-vaihtona ei olisi ollut toivottavaa.

### **Tehosteet**

MIDI control change (CC) -viestit **kanavalla 15** säätävät tehosteita.\
Tehoste 1 käyttää CC 0-3, arvo 0-127\
Tehoste 2 käyttää CC 4-7, arvo 0-127\
Tehoste 3 käyttää CC 8-11, arvo 0-127\
… ja niin edelleen.

Jokainen neljän ohjaimen ryhmä säätää kyseisen tehosteen tasoa ja kolmea parametria:

<table><thead><tr><th width="164">Tehoste :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Taso</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parametri 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...jne</td></tr><tr><td><strong>Parametri 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parametri 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Yleiset asetukset**

MIDI control change -viestit **kanavalla 16** muuttavat yleisiä asetuksia:\
CC 1 : Shift X (vaaka) 0 -127, 64 on keskellä\
CC 2 : Shift Y (pysty) 0 -127, 64 on keskellä\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Ja tärkeänä asetuksena:\
CC 15 : Global brightness

Huomaa, että tämä järjestelmä suunniteltiin alun perin tallennusta ja toistoa varten. Sen avulla voit luoda aikajanapohjaisia animaatioita Logicilla, Abletonilla tai muulla DAW-ohjelmistolla. Vaikka voit käyttää sitä live-ohjaukseen, sitä ei ole optimoitu siihen käyttöön, ja siitä puuttuu joitakin live-ohjauksen toimintoja verrattuna APC40-määritykseen.
