---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Výchozí mapování odesílání a příjmu MIDI

**Zapnutí a vypnutí položky Clip se spouští pomocí MIDI note on / off na kanálech 1 až 14**

Clips mají vodorovnou (x) a svislou (y) pozici. Klikněte pravým tlačítkem na Clip a uvidíte jeho pozici. MIDI může spouštět Clips od pozice 0,0.

{% hint style="info" %}
Ovládání Clips tímto systémem je absolutní a pozice Clips se při posouvání v Clip Deck nemění.
{% endhint %}

MIDI kanál 1, nota 1 odpovídá Clip 0,0, nota 2 odpovídá Clip 0,1, nota 3 odpovídá Clip 0,2 — postupuje se dolů po řádcích a dále po sloupcích. Po dosažení 128 se přejde na další kanál a začne se znovu. Celkem tedy máte k dispozici 128 × 14 = 1792 Clips dostupných přes MIDI.

MIDI nota pro souřadnice Clip:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nota : 1</td><td>Nota : 6</td><td>Nota : 11</td><td>Nota : 16</td><td>Nota : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nota : 2</td><td>Nota : 7</td><td>Nota : 12</td><td>Nota : 17</td><td>...atd.</td></tr><tr><td><strong>y : 2</strong></td><td>Nota : 3</td><td>Nota : 8</td><td>Nota : 13</td><td>Nota : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nota : 4</td><td>Nota : 9</td><td>Nota : 14</td><td>Nota : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nota : 5</td><td>Nota : 10</td><td>Nota : 15</td><td>Nota : 20</td><td></td></tr></tbody></table>

Událost MIDI note on spustí Clip a odpovídající událost note off jej zastaví. Platí to bez ohledu na režim spouštění skupiny. Systém byl původně navržen pro přehrávání a záznam, takže přepínání Clip pomocí not by bylo nežádoucí.

### **Efekty**

Zprávy MIDI control change (CC) na **kanálu 15** upravují efekty.\
Efekt 1 používá CC 0–3, hodnota 0–127\
Efekt 2 používá CC 4–7, hodnota 0–127\
Efekt 3 používá CC 8–11, hodnota 0–127\
… a tak dále.

Každá skupina čtyř ovladačů řídí úroveň a 3 parametry daného efektu:

<table><thead><tr><th width="164">Efekt :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Úroveň</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parametr 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...atd.</td></tr><tr><td><strong>Parametr 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parametr 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Globální nastavení**

Zprávy MIDI control change na **kanálu 16** mění globální nastavení:\
CC 1 : Shift X (vodorovně) 0–127, 64 je uprostřed\
CC 2 : Shift Y (svisle) 0–127, 64 je uprostřed\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

A důležité:\
CC 15 : Global Brightness

Upozorňujeme, že tento systém byl původně navržen pro záznam a přehrávání, aby bylo možné používat Logic, Ableton nebo jiné DAW k vytváření animací na časové ose. I když jej můžete použít pro živé ovládání, není pro tento účel optimalizovaný a oproti nastavení APC40 mu některé funkce pro živé ovládání chybí.
