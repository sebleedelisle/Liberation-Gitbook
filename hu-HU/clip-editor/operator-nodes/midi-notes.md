---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

„Lézerhárfa” jellegű effekteket hoz létre, ahol a beérkező MIDI-hangok nyalábokat vagy alakzatokat indítanak el egy tartományon belül. A node minden hanghoz azt a tartalmat használja _forrásként_, amelyet bemenetként adsz neki: ha egy pontot küldesz be, pontok sorát kapod. Ha egy alakzatot, például egy kört, akkor körök sorát kapod, és az összetettebb alakzatokat is ugyanígy sokszorosítja.

Azt, hogy a Liberation melyik MIDI-interfészre figyeljen, itt választhatod ki: **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – melyik MIDI-csatornára figyeljen (0 = összes csatorna, 1–16 = adott csatorna)
* **width** – a hangok teljes szélessége, amelyen belül eloszlanak.
* **MIDI note min / max** – a tartomány legalacsonyabb és legmagasabb MIDI-hangértéke.
* **ignore out of range notes** – kiszűri a beállított tartományon kívüli hangokat. Ha ki van kapcsolva, a tartományon kívüli hangokat a legközelebbi elérhető hangra „szorítja” (a magas hangok a tartomány tetejét, az alacsony hangok az alját indítják).
* **auto extend range** – automatikusan bővíti a tartományt, ha azon kívüli hangokat játszol le.

{% hint style="info" %}
Nem tudod, milyen hangtartomány érkezik be? Kapcsold be az **auto extend range** beállítást, állítsd a **MIDI note min** értékét nagyon magasra, a **MIDI note max** értékét pedig nagyon alacsonyra, majd játszd végig a hangokat. A rendszer mindet felismeri, és kibővíti neked a tartományt. Ha minden megvan, egyszerűen kapcsold ki az **auto extend range** beállítást a rögzítéshez.
{% endhint %}

* **leave all notes visible** – a tartomány összes hangjához létrehozza a nyalábokat vagy alakzatokat, függetlenül attól, hogy éppen szólnak-e; így „lézerhárfa” hatást kapsz.
* **hit colour** – az a szín, amely egy hang indításakor megjelenik.
* **hit colour hold time** – mennyi ideig marad a hit colour teljes fényerőn, mielőtt halványulni kezd. Az érték másodpercben értendő (0–1). _100% = 1 másodperc._
* **hit colour decay time** – mennyi idő alatt halványul vissza a hit colour a kitartási idő után. Az érték másodpercben értendő (0–1). _100% = 1 másodperc._

{% hint style="info" %}
Ha a tartalmad már eleve tiszta fehér, a hit colour fehérre állítása nem fog látható változást okozni. A legjobb eredményhez használj telített színt a tartalomhoz, a hit colour értékét pedig állítsd fehérre – így a hangok indításakor nagyon szép villanás effektet kapsz.
{% endhint %}

* **note off fade out time** – mennyi idő alatt halványul el a hang a felengedése után. Az érték másodpercben értendő (0–1). _100% = 1 másodperc._
* **hit scale factor** – mennyivel nagyítódik fel a hang indításkor (pl. 2 = kétszeres méret).
* **hit scale hold time** – mennyi ideig marad a hang felnagyítva, mielőtt visszazsugorodik. Az érték másodpercben értendő (0–1). _100% = 1 másodperc._
* **hit scale decay time** – mennyi idő alatt tér vissza a hang az eredeti méretéhez. Az érték másodpercben értendő (0–1). _100% = 1 másodperc._
* **note off shrink time** – mennyi idő alatt zsugorodik vissza az eredeti méretre a hang felengedése után. Az érték másodpercben értendő (0–1). _100% = 1 másodperc._ (Nincs hatása, ha a **leave all notes visible** be van kapcsolva.)

{% hint style="info" %}
Méretezés – Fontos, hogy ha a tartalmad egyetlen pont, akkor a méretezésnek nem lesz hatása!
{% endhint %}
