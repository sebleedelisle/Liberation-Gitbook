---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Domyślne mapowanie wysyłania/odbioru MIDI

**Włączanie i wyłączanie elementów Clip jest wyzwalane przez komunikaty MIDI note on / off na kanałach od 1 do 14**

Elementy Clip mają pozycję poziomą (x) i pionową (y). Kliknij element Clip prawym przyciskiem myszy, aby zobaczyć jego pozycję. MIDI może wyzwalać elementy Clip, zaczynając od 0,0.

{% hint style="info" %}
Sterowanie elementami Clip w tym systemie jest bezwzględne, a pozycje elementów Clip nie zmieniają się podczas przewijania Clip Deck.
{% endhint %}

Kanał MIDI 1, nuta 1 to Clip 0,0; nuta 2 to Clip 0,1; nuta 3 to Clip 0,2 — kolejno w dół wierszami i dalej kolumnami. Po osiągnięciu 128 system przechodzi do następnego kanału i zaczyna od początku. Łącznie daje to 128 x 14 = 1792 elementy Clip dostępne przez MIDI.

Nuta MIDI dla współrzędnych elementu Clip:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nuta : 1</td><td>Nuta : 6</td><td>Nuta : 11</td><td>Nuta : 16</td><td>Nuta : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nuta : 2</td><td>Nuta : 7</td><td>Nuta : 12</td><td>Nuta : 17</td><td>...itd.</td></tr><tr><td><strong>y : 2</strong></td><td>Nuta : 3</td><td>Nuta : 8</td><td>Nuta : 13</td><td>Nuta : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nuta : 4</td><td>Nuta : 9</td><td>Nuta : 14</td><td>Nuta : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nuta : 5</td><td>Nuta : 10</td><td>Nuta : 15</td><td>Nuta : 20</td><td></td></tr></tbody></table>

Zdarzenie MIDI note on uruchamia element Clip, a odpowiadające mu zdarzenie note off zatrzymuje element Clip. Działa to niezależnie od trybu wyzwalania ustawionego w grupie. System został pierwotnie zaprojektowany do odtwarzania i nagrywania, więc przełączanie elementu Clip tymi samymi nutami byłoby niepożądane.

### **Efekty**

Komunikaty MIDI control change (CC) na **kanale 15** regulują efekty.\
Efekt 1 używa CC 0-3, wartość 0-127\
Efekt 2 używa CC 4-7, wartość 0-127\
Efekt 3 używa CC 8-11, wartość 0-127\
… i tak dalej.

Każda grupa czterech kontrolerów steruje poziomem i 3 parametrami danego efektu:

<table><thead><tr><th width="164">Efekt :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Level</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...itd.</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Ustawienia globalne**

Komunikaty MIDI control change na **kanale 16** zmieniają ustawienia globalne:\
CC 1 : Shift X (poziomo) 0 -127, 64 znajduje się pośrodku\
CC 2 : Shift Y (pionowo) 0 -127, 64 znajduje się pośrodku\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

I co ważne:\
CC 15 : Global brightness

Pamiętaj, że ten system został pierwotnie zaprojektowany do nagrywania i odtwarzania, aby umożliwić używanie Logic, Ableton lub innego programu DAW do tworzenia animacji na osi czasu. Można go używać do sterowania na żywo, ale nie został zoptymalizowany pod tym kątem, a w porównaniu z konfiguracją APC40 brakuje niektórych funkcji sterowania na żywo.
