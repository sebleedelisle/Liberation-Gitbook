---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Sjálfgefin MIDI send/receive-vörpun

**Kveikt og slökkt er á Clip með MIDI note on / off á rásum 1 til 14**

Clip hafa lárétta (x) og lóðrétta (y) staðsetningu. Hægrismelltu á Clip til að sjá staðsetninguna. MIDI getur ræst Clip frá 0,0.

{% hint style="info" %}
Athugaðu að Clip-stýring með þessu kerfi er algild og staðsetningar Clip breytast ekki þegar þú flettir í Clip Deck.
{% endhint %}

MIDI-rás 1, nóta 1 er Clip 0,0, nóta 2 er Clip 0,1 og nóta 3 er Clip 0,2, áfram niður eftir röðum og til hliðar eftir dálkum. Þegar talan nær 128 færist hún yfir á næstu rás og byrjar aftur. Þú hefur því samtals 128 x 14 = 1792 Clip sem hægt er að nálgast með MIDI.

MIDI-nóta fyrir Clip-hnit:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nóta : 1</td><td>Nóta : 6</td><td>Nóta : 11</td><td>Nóta : 16</td><td>Nóta : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nóta : 2</td><td>Nóta : 7</td><td>Nóta : 12</td><td>Nóta : 17</td><td>...o.s.frv.</td></tr><tr><td><strong>y : 2</strong></td><td>Nóta : 3</td><td>Nóta : 8</td><td>Nóta : 13</td><td>Nóta : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nóta : 4</td><td>Nóta : 9</td><td>Nóta : 14</td><td>Nóta : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nóta : 5</td><td>Nóta : 10</td><td>Nóta : 15</td><td>Nóta : 20</td><td></td></tr></tbody></table>

Athugaðu að MIDI note on-atvik ræsir Clip og samsvarandi note off-atvik stöðvar það. Þetta gildir óháð trigger mode í hópnum. Kerfið var upphaflega hannað fyrir afspilun og upptöku, þannig að ekki hefði hentað að láta nóturnar víxla kveikt/slökkt á Clip.

### **Áhrif**

MIDI control change (CC)-skilaboð á **rás 15** stilla áhrifin.\
Áhrif 1 notar CC 0-3, gildi 0-127\
Áhrif 2 notar CC 4-7, gildi 0-127\
Áhrif 3 notar CC 8-11, gildi 0-127\
… og svo framvegis.

Hver fjögurra stýringa hópur stýrir styrknum og 3 breytum fyrir viðkomandi áhrif:

<table><thead><tr><th width="164">Áhrif :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Styrkur</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Breyta 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...o.s.frv.</td></tr><tr><td><strong>Breyta 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Breyta 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Almennar stillingar**

MIDI control change-skilaboð á **rás 16** breyta almennu stillingunum:\
CC 1 : Shift X (lárétt) 0 -127, 64 er í miðjunni\
CC 2 : Shift Y (lóðrétt) 0 -127, 64 er í miðjunni\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Og mikilvægt:\
CC 15 : Global brightness

Athugaðu að þetta kerfi var upphaflega hannað fyrir upptöku og afspilun, svo þú getir notað Logic, Ableton eða annan DAW-hugbúnað til að búa til hreyfimyndir á tímalínu. Þótt þú getir notað það fyrir beina stýringu hefur það ekki verið fínstillt fyrir slíka notkun og sumar aðgerðir fyrir beina stýringu vantar miðað við APC40-uppsetninguna.
