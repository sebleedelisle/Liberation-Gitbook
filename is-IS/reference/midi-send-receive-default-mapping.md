---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Sjálfgefin MIDI-vörpun fyrir sendingu/móttöku

**Kveikt og slökkt er á Clips með MIDI note on / off á rásum 1 til 14**

Clips hafa lárétta (x) og lóðrétta (y) staðsetningu. Hægrismelltu á Clip til að sjá staðsetninguna. MIDI getur ræst Clips frá 0,0.

{% hint style="info" %}
Athugaðu að stjórnun Clips með þessu kerfi er algild og staðsetningar Clips breytast ekki þegar þú flettir í Clip Deck.
{% endhint %}

MIDI-rás 1, nóta 1 er Clip 0,0, nóta 2 er Clip 0,1 og nóta 3 er Clip 0,2, niður eftir röðum og áfram eftir dálkum. Þegar komið er að 128 færist kerfið yfir á næstu rás og byrjar aftur. Þannig hefurðu samtals 128 x 14 = 1792 Clips sem hægt er að nálgast með MIDI.

MIDI-nótur fyrir hnit Clips:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nóta : 1</td><td>Nóta : 6</td><td>Nóta : 11</td><td>Nóta : 16</td><td>Nóta : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nóta : 2</td><td>Nóta : 7</td><td>Nóta : 12</td><td>Nóta : 17</td><td>...o.s.frv.</td></tr><tr><td><strong>y : 2</strong></td><td>Nóta : 3</td><td>Nóta : 8</td><td>Nóta : 13</td><td>Nóta : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nóta : 4</td><td>Nóta : 9</td><td>Nóta : 14</td><td>Nóta : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nóta : 5</td><td>Nóta : 10</td><td>Nóta : 15</td><td>Nóta : 20</td><td></td></tr></tbody></table>

Athugaðu að MIDI note on-atburður ræsir Clip og samsvarandi note off-atburður stöðvar það. Þetta gildir óháð ræsingarham hópsins. Kerfið var upphaflega hannað fyrir afspilun og upptöku, þannig að það hefði ekki hentað að láta nóturnar víxla Clip af og á.

### **Áhrif**

MIDI Control Change (CC)-skilaboð á **rás 15** stilla áhrifin.\
Áhrif 1 nota CC 0-3, gildi 0-127\
Áhrif 2 nota CC 4-7, gildi 0-127\
Áhrif 3 nota CC 8-11, gildi 0-127\
… og svo framvegis.

Hver hópur með fjórum stjórningum stýrir styrknum og 3 færibreytum fyrir viðkomandi áhrif:

<table><thead><tr><th width="164">Áhrif :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Styrkur</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Færibreyta 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...o.s.frv.</td></tr><tr><td><strong>Færibreyta 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Færibreyta 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Almennar stillingar**

MIDI Control Change-skilaboð á **rás 16** breyta almennum stillingum:\
CC 1 : Shift X (lárétt) 0 -127, 64 er í miðjunni\
CC 2 : Shift Y (lóðrétt) 0 -127, 64 er í miðjunni\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Og mikilvægast:\
CC 15 : Global Brightness

Athugaðu að þetta kerfi var upphaflega hannað fyrir upptöku og afspilun, svo þú gætir notað Logic, Ableton eða annað DAW til að búa til tímalínuhreyfingar. Þó að hægt sé að nota það fyrir lifandi stjórnun hefur það ekki verið fínstillt fyrir þá notkun og nokkrar aðgerðir fyrir lifandi stjórnun vantar miðað við APC40-uppsetninguna.
