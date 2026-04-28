---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ MIDI küldés/fogadás alapértelmezett leképezése

**A Clip be- és kikapcsolását az 1–14. csatornákon érkező MIDI note on / off üzenetek indítják**

A Clip-eknek van vízszintes (x) és függőleges (y) pozíciójuk. Kattints jobb gombbal egy Clip-re, és látni fogod a pozícióját. A MIDI a Clip-eket a 0,0 pozíciótól kezdve tudja indítani.

{% hint style="info" %}
Fontos, hogy a Clip-ek vezérlése ebben a rendszerben abszolút, vagyis a Clip-pozíciók nem változnak, amikor görgeted a Clip Deck-et.
{% endhint %}

Az 1-es MIDI-csatorna 1-es note-ja a 0,0 pozíciójú Clip, a 2-es note a 0,1 pozíciójú Clip, a 3-as note a 0,2 pozíciójú Clip; soronként lefelé, majd oszloponként halad. Amikor eléri a 128-at, a következő csatornára vált, és újrakezdi. Így összesen 128 x 14 = 1792 Clip érhető el MIDI-n keresztül.

MIDI note a Clip-koordinátákhoz:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Note : 1</td><td>Note : 6</td><td>Note : 11</td><td>Note : 16</td><td>Note : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Note : 2</td><td>Note : 7</td><td>Note : 12</td><td>Note : 17</td><td>...stb.</td></tr><tr><td><strong>y : 2</strong></td><td>Note : 3</td><td>Note : 8</td><td>Note : 13</td><td>Note : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Note : 4</td><td>Note : 9</td><td>Note : 14</td><td>Note : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Note : 5</td><td>Note : 10</td><td>Note : 15</td><td>Note : 20</td><td></td></tr></tbody></table>

Fontos, hogy egy MIDI note on esemény elindítja a Clip-et, a hozzá tartozó note off esemény pedig leállítja. Ez független a csoport trigger módjától. A rendszert eredetileg lejátszáshoz és felvételhez tervezték, ezért nem lett volna kívánatos, hogy a note-ok kapcsolóként váltsák a Clip állapotát.

### **Effektek**

A **15-ös csatornán** érkező MIDI control change (CC) üzenetek az effekteket állítják.\
Az 1. effekt a CC 0-3 értékeket használja, 0-127 értéktartománnyal\
A 2. effekt a CC 4-7 értékeket használja, 0-127 értéktartománnyal\
A 3. effekt a CC 8-11 értékeket használja, 0-127 értéktartománnyal\
… és így tovább.

Minden négyes csoport az adott effekt szintjét és 3 paraméterét vezérli:

<table><thead><tr><th width="164">Effekt:</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Level</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...stb.</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Globális beállítások**

A **16-os csatornán** érkező MIDI control change üzenetek a globális beállításokat módosítják:\
CC 1 : Shift X (vízszintes) 0 -127, 64 van középen\
CC 2 : Shift Y (függőleges) 0 -127, 64 van középen\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

És ami különösen fontos:\
CC 15 : Global brightness

Vedd figyelembe, hogy ezt a rendszert eredetileg felvételhez és lejátszáshoz tervezték, hogy Logic, Ableton vagy más DAW segítségével idővonalas animációkat hozhass létre. Bár élő vezérlésre is használható, erre a felhasználásra nincs optimalizálva, és az APC40 beállításhoz képest néhány élő vezérlési funkció hiányzik.
