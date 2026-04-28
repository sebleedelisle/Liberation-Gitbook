---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Standardtilordning for MIDI-sending/-mottak

**Clip av og på utløses av MIDI note on / off på kanal 1 til 14**

Clips har en horisontal (x) og vertikal (y) posisjon. Høyreklikk på en clip for å se posisjonen. MIDI kan utløse clips fra og med 0,0.

{% hint style="info" %}
Merk at clip-kontroll med dette systemet er absolutt, og clip-posisjonene endres ikke når du blar i Clip Deck.
{% endhint %}

MIDI-kanal 1, note 1 er clip 0,0, note 2 er clip 0,1, note 3 er clip 0,2, nedover i rader og bortover i kolonner. Når den kommer til 128, går den videre til neste kanal og starter på nytt. Du har altså totalt 128 x 14 = 1792 clips som er tilgjengelige via MIDI.

MIDI-note for clip-koordinater:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Note : 1</td><td>Note : 6</td><td>Note : 11</td><td>Note : 16</td><td>Note : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Note : 2</td><td>Note : 7</td><td>Note : 12</td><td>Note : 17</td><td>...osv.</td></tr><tr><td><strong>y : 2</strong></td><td>Note : 3</td><td>Note : 8</td><td>Note : 13</td><td>Note : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Note : 4</td><td>Note : 9</td><td>Note : 14</td><td>Note : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Note : 5</td><td>Note : 10</td><td>Note : 15</td><td>Note : 20</td><td></td></tr></tbody></table>

Merk at en MIDI note on-hendelse starter clipen, og den tilsvarende note off-hendelsen stopper clipen. Dette gjelder uavhengig av utløsermodus for gruppen. Systemet ble opprinnelig laget for avspilling og opptak, så det ville vært uønsket om notene slo en clip av/på.

### **Effekter**

MIDI control change-meldinger (CC) på **kanal 15** justerer effektene.\
Effekt 1 bruker CC 0–3, verdi 0–127\
Effekt 2 bruker CC 4–7, verdi 0–127\
Effekt 3 bruker CC 8–11, verdi 0–127\
… og så videre.

Hver gruppe på fire kontrollerer nivået og 3 parametere for den effekten:

<table><thead><tr><th width="164">Effekt:</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Nivå</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...osv.</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Globale innstillinger**

MIDI control change-meldinger på **kanal 16** endrer de globale innstillingene:\
CC 1 : Shift X (horisontal) 0–127, 64 er i midten\
CC 2 : Shift Y (vertikal) 0–127, 64 er i midten\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Og viktigst:\
CC 15 : Global brightness

Merk at dette systemet opprinnelig ble laget for opptak og avspilling, slik at du kan bruke Logic, Ableton eller en annen DAW til å lage tidslinjeanimasjoner. Selv om du kan bruke det til live-kontroll, er det ikke optimalisert for den bruken, og noen funksjoner for live-kontroll mangler sammenlignet med APC40-oppsettet.
