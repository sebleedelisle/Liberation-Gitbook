---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ MIDI gönderme/alma varsayılan eşlemesi

**Clip öğelerini açma ve kapatma, 1 ile 14 arasındaki kanallarda MIDI note on / off ile tetiklenir**

Clips yatay (x) ve dikey (y) konuma sahiptir. Bir Clip üzerinde sağ tıklarsanız konumunu görebilirsiniz. MIDI, 0,0 konumundan başlayarak Clips tetikleyebilir.

{% hint style="info" %}
Bu sistemde Clip kontrolünün mutlak olduğunu ve Clip Deck içinde kaydırma yaptığınızda Clip konumlarının değişmediğini unutmayın.
{% endhint %}

MIDI kanal 1, nota 1; Clip 0,0’dır. Nota 2; Clip 0,1, nota 3; Clip 0,2 şeklinde satırlar boyunca aşağı ve sütunlar boyunca ilerler. 128’e ulaştığında bir sonraki kanala geçer ve yeniden başlar. Böylece MIDI üzerinden erişilebilen toplam 128 x 14 = 1792 Clip olur.

Clip koordinatları için MIDI notası:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nota : 1</td><td>Nota : 6</td><td>Nota : 11</td><td>Nota : 16</td><td>Nota : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nota : 2</td><td>Nota : 7</td><td>Nota : 12</td><td>Nota : 17</td><td>...vb.</td></tr><tr><td><strong>y : 2</strong></td><td>Nota : 3</td><td>Nota : 8</td><td>Nota : 13</td><td>Nota : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nota : 4</td><td>Nota : 9</td><td>Nota : 14</td><td>Nota : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nota : 5</td><td>Nota : 10</td><td>Nota : 15</td><td>Nota : 20</td><td></td></tr></tbody></table>

MIDI note on olayı Clip öğesini başlatır, karşılık gelen note off olayı ise Clip öğesini durdurur. Bu, gruptaki trigger mode ayarından bağımsızdır. Sistem başlangıçta oynatma ve kayıt için tasarlandığından, notaların bir Clip öğesini toggle etmesi istenmeyen bir davranış olurdu.

### **Efektler**

**Kanal 15** üzerindeki MIDI control change (CC) mesajları efektleri ayarlar.\
Efekt 1, CC 0-3 ve 0-127 değer aralığını kullanır\
Efekt 2, CC 4-7 ve 0-127 değer aralığını kullanır\
Efekt 3, CC 8-11 ve 0-127 değer aralığını kullanır\
… ve bu şekilde devam eder.

Her dört kontrol grubu, ilgili efektin seviyesini ve 3 parametresini kontrol eder:

<table><thead><tr><th width="164">Efekt :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Seviye</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parametre 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...vb.</td></tr><tr><td><strong>Parametre 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parametre 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Genel ayarlar**

**Kanal 16** üzerindeki MIDI control change mesajları genel ayarları değiştirir:\
CC 1 : Shift X (yatay) 0 -127, 64 orta noktadır\
CC 2 : Shift Y (dikey) 0 -127, 64 orta noktadır\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Ve önemli olarak:\
CC 15 : Global Brightness

Bu sistemin başlangıçta kayıt ve oynatma için tasarlandığını unutmayın; Logic, Ableton veya başka bir DAW kullanarak zaman çizelgesi animasyonları oluşturmanıza olanak sağlar. Canlı kontrol için kullanabilirsiniz, ancak bu kullanım için optimize edilmemiştir ve APC40 ile yapılan kuruluma kıyasla bazı canlı kontrol işlevleri eksiktir.
