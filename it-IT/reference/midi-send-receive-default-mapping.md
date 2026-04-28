---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Mappatura predefinita MIDI di invio/ricezione

**Le Clip vengono attivate e disattivate dai messaggi MIDI note on / off sui canali da 1 a 14**

Le Clip hanno una posizione orizzontale (x) e verticale (y): fai clic con il tasto destro su una Clip per vederne la posizione. Il MIDI può attivare le Clip a partire da 0,0.

{% hint style="info" %}
Tieni presente che il controllo delle Clip con questo sistema è assoluto: le posizioni delle Clip non cambiano quando scorri il Clip Deck.
{% endhint %}

Il canale MIDI 1, nota 1 corrisponde alla Clip 0,0; la nota 2 alla Clip 0,1; la nota 3 alla Clip 0,2, procedendo verso il basso per righe e poi lungo le colonne. Quando arriva a 128, passa al canale successivo e ricomincia. In totale hai quindi 128 x 14 = 1792 Clip accessibili via MIDI.

Nota MIDI per le coordinate delle Clip:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nota : 1</td><td>Nota : 6</td><td>Nota : 11</td><td>Nota : 16</td><td>Nota : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nota : 2</td><td>Nota : 7</td><td>Nota : 12</td><td>Nota : 17</td><td>...ecc.</td></tr><tr><td><strong>y : 2</strong></td><td>Nota : 3</td><td>Nota : 8</td><td>Nota : 13</td><td>Nota : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nota : 4</td><td>Nota : 9</td><td>Nota : 14</td><td>Nota : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nota : 5</td><td>Nota : 10</td><td>Nota : 15</td><td>Nota : 20</td><td></td></tr></tbody></table>

Tieni presente che un evento MIDI note on avvia la Clip, mentre l’evento note off equivalente la interrompe. Questo vale indipendentemente dalla modalità di trigger impostata sul gruppo. Il sistema è stato progettato originariamente per la riproduzione e la registrazione, quindi far sì che le note attivassero/disattivassero una Clip in modalità toggle sarebbe stato indesiderato.

### **Effetti**

I messaggi MIDI control change (CC) sul **canale 15** regolano gli effetti.\
L’effetto 1 usa i CC 0-3, valore 0-127\
L’effetto 2 usa i CC 4-7, valore 0-127\
L’effetto 3 usa i CC 8-11, valore 0-127\
… e così via.

Ogni gruppo di quattro controlla il livello e 3 parametri dell’effetto:

<table><thead><tr><th width="164">Effetto :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Livello</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parametro 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...ecc.</td></tr><tr><td><strong>Parametro 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parametro 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Impostazioni globali**

I messaggi MIDI control change sul **canale 16** modificano le impostazioni globali:\
CC 1 : Shift X (orizzontale) 0 -127, 64 è al centro\
CC 2 : Shift Y (verticale) 0 -127, 64 è al centro\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

E, cosa importante:\
CC 15 : Luminosità globale

Tieni presente che questo sistema è stato progettato originariamente per la registrazione e la riproduzione, permettendoti di usare Logic, Ableton o altre DAW per creare animazioni su timeline. Anche se puoi usarlo per il controllo live, non è stato ottimizzato per questo uso e mancano alcune funzioni per il controllo live rispetto alla configurazione APC40.
