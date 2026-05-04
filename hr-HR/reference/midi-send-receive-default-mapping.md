---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Zadano mapiranje za MIDI slanje/primanje

**Clip se uključuje i isključuje MIDI note on / off porukama na kanalima 1 do 14**

Svaki Clip ima vodoravni (x) i okomiti (y) položaj. Kliknite desnom tipkom miša na Clip i vidjet ćete njegov položaj. MIDI može pokretati Clip počevši od 0,0.

{% hint style="info" %}
Imajte na umu da je upravljanje za Clip ovim sustavom apsolutno i da se položaji ne mijenjaju dok se pomičete kroz Clip Deck.
{% endhint %}

MIDI kanal 1, nota 1 odgovara položaju Clip 0,0; nota 2 položaju Clip 0,1; nota 3 položaju Clip 0,2, krećući se prema dolje po redovima i zatim kroz stupce. Kada dođe do 128, prelazi na sljedeći kanal i počinje ponovno. Tako ukupno imate 128 x 14 = 1792 Clip stavki dostupnih putem MIDI-ja.

MIDI nota za koordinate Clip:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nota : 1</td><td>Nota : 6</td><td>Nota : 11</td><td>Nota : 16</td><td>Nota : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nota : 2</td><td>Nota : 7</td><td>Nota : 12</td><td>Nota : 17</td><td>...itd.</td></tr><tr><td><strong>y : 2</strong></td><td>Nota : 3</td><td>Nota : 8</td><td>Nota : 13</td><td>Nota : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nota : 4</td><td>Nota : 9</td><td>Nota : 14</td><td>Nota : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nota : 5</td><td>Nota : 10</td><td>Nota : 15</td><td>Nota : 20</td><td></td></tr></tbody></table>

Imajte na umu da MIDI note on događaj pokreće Clip, a odgovarajući note off događaj ga zaustavlja. To vrijedi neovisno o načinu okidanja za grupu. Sustav je izvorno osmišljen za reprodukciju i snimanje, pa bi prebacivanje Clip između uključenog i isključenog stanja pomoću nota bilo nepoželjno.

### **Efekti**

MIDI control change (CC) poruke na **kanalu 15** podešavaju efekte.\
Efekt 1 koristi CC 0-3, vrijednost 0-127\
Efekt 2 koristi CC 4-7, vrijednost 0-127\
Efekt 3 koristi CC 8-11, vrijednost 0-127\
… i tako dalje.

Svaka grupa od četiri kontrole upravlja razinom i 3 parametra tog efekta:

<table><thead><tr><th width="164">Efekt :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Razina</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parametar 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...itd.</td></tr><tr><td><strong>Parametar 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parametar 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Globalne postavke**

MIDI control change poruke na **kanalu 16** mijenjaju globalne postavke:\
CC 1 : Shift X (vodoravno) 0 -127, 64 je sredina\
CC 2 : Shift Y (okomito) 0 -127, 64 je sredina\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

I, što je važno:\
CC 15 : Global Brightness

Imajte na umu da je ovaj sustav izvorno osmišljen za snimanje i reprodukciju, što vam omogućuje da u Logic, Ableton ili drugom DAW programu stvarate animacije na vremenskoj crti. Iako ga možete koristiti za upravljanje uživo, nije optimiziran za tu namjenu, a u usporedbi s APC40 setup nedostaju neke funkcije za upravljanje uživo.
