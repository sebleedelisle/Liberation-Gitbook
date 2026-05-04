---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Kitöltések, maszkok és mélységi rendezés

### Körvonalak, kitöltések és maszkok

Észre fogod venni, hogy néhány Creator node rendelkezik _Fill state_ opcióval; ezeket megrajzolhatod körvonallal (_stroke_), maszkként (ami eltakarja az alatta lévő elemeket), vagy mindkettővel.

Amikor egy alakzatot maszkként renderelsz, az úgy viselkedik, mintha feketével lenne kitöltve, és bármit, ami alatta van, eltakar.

{% hint style="info" %}
Egy vonal (vagy _stroke_) lézerrel való megrajzolása viszonylag egyszerű: a lézert a vonal elejétől a vonal végéig pásztázod. Kész is a vonal!

A kitöltött alakzatok viszont nehezebbek. Ha egy alakzatot színnel szeretnél kitölteni, kézzel keresztirányú satírozást rajzolhatnál vonalakkal és kitöltéssel, de a Liberation ezt (egyelőre) nem tudja automatikusan megtenni. És még ha meg is tudná, az alatta lévő többi vonal akkor is átsejlene.

Amit viszont meg tudunk tenni, az az alakzatok _feketével_ való kitöltése. A háttérben a Liberation elvégzi az összes számítást, hogy eltávolítsa a feketével kitöltött alakzat alatt lévő tartalmat. És hidd el, ez elég aprólékos munka!

De nagyon jól működik, és egy feketével kitöltött alakzat illúzióját kelti.
{% endhint %}

### Mélységi rendezés

Mivel egyes alakzatok _eltakarhatnak_ más alakzatokat, a Liberationnek mélység szerint kell rendeznie őket. Alapértelmezés szerint az elemek a z pozíciójuk alapján vannak mélység szerint rendezve. Ha ugyanazon a z pozíción vannak, akkor a rétegpozíciójuk alapján rendeződnek, amelyet az egyes Creator elemen belül a _MOVE TO FRONT_ és _MOVE TO BACK_ gombokkal lehet módosítani.
