---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Globális transzformációk

A clip-transzformációk (shift x/y, scale x/y) mellett léteznek Global Transformations is, amelyek minden futtatott clipre érvényesek. Megtekintésükhöz nyisd meg a _Global Transformations_ panelt. (Ez a panel általában a _Clip Settings_ melletti fülön található.)

Alapértelmezés szerint ezek a beállítások visszaállnak, amint már nincs lejátszás alatt álló clip. Ez a visszaállítási viselkedés kikapcsolható a _Global Transformations_ panel alján található _AUTO RESET_ gombbal.

{% hint style="info" %}
Fontos, hogy a Global Transformations nem érint semmit a Canvas területén, csak a Beam és DMX zónákra hat.
{% endhint %}

### Scale X/Y

Vízszintes és függőleges skálázás. Ezek az értékek össze vannak kapcsolva, kivéve, ha lenyomva tartod a `Shift` billentyűt. Alapértelmezés szerint ezek az APC40 Device Control 4-es és 8-as tekerőjére is hozzá vannak rendelve, és a Clip Deck jobb oldalán lévő kontextuális Parameters panelen jelennek meg.

### Shift X/Y

Vízszintes és függőleges eltolás. Mindent vízszintesen / függőlegesen mozgat el.

### Spin

Az összes tartalmat a középpont körül forgatja. A pozitív érték az óramutató járásával megegyező irányba, a negatív érték azzal ellentétes irányba forgat. Látható, hogy ez a beállítás hatással van a _Rotation_ transzformációra. Alapértelmezés szerint ez az APC40 Device Control 3-as tekerőjére van hozzárendelve, és a Clip Deck jobb oldalán lévő kontextuális Parameters panelen jelenik meg.

### Spin 3D

Az összes tartalmat az Y tengely körül forgatja (ez a középen lévő függőleges vonal). Látható, hogy ez a beállítás hatással van a _Rotation3D_ transzformációra. Alapértelmezés szerint ez az APC40 Device Control 7-es tekerőjére van hozzárendelve, és a Clip Deck jobb oldalán lévő kontextuális Parameters panelen jelenik meg.

### Rotation

Forgatás a középpont körül, fokban megadott értékkel.

### Rotation 3D

Forgatás az Y tengely körül (ez a középen lévő függőleges vonal), fokban megadott értékkel.

### Auto reset

Ha be van kapcsolva, az összes Global Transformations visszaáll, amint az összes jelenleg futó clip deaktiválódik. Így biztos lehetsz benne, hogy a következő clip indításakor nem ér meglepetés!
