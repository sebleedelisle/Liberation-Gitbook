---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas célterületek

Már tudjuk, hogyan juttathatjuk a canvas egyes részeit az egyes lézerek zónáiba, de ahhoz, hogy a tartalom egyáltalán bekerüljön a canvasra, a kissé zavaró, de pontos nevű _Canvas target areas_ funkcióra lesz szükséged.

A _Canvas target areas_ a canvas olyan szakaszai, amelyekbe klipeket rajzolhatsz. A _CANVAS_ nézetben kék körvonalú téglalapokként jelennek meg.

Gyakran elég egyetlen canvas célterület, amelyet aztán több, különböző lézerekre küldött zónára osztasz fel.

Máskor több canvas célterületre lehet szükséged egy épület különböző részeihez, vagy azért, hogy kihasználd a köztük működő zónakésleltetést. (Igen! A zónakésleltetés a canvas célterületek között is működik!)

### Klipek küldése canvas célterületekre

Ha megnézed a Clip Decket, a beam zone gombok mellett látni fogod a canvas célterület gombjait. Előfordulhat, hogy görgetned kell az output gombokat, hogy látszódjanak: használd a `Shift + Left / Right Arrow` billentyűkombinációt, a képernyőn lévő ZONE PAGE gombokat, vagy az APC40 gombjait (lásd: [APC40 referencia](../reference/apc40-reference.md "mention")).

A klipeket pontosan ugyanúgy rendelheted canvas célterületekhez ezeknek a gomboknak a be- és kikapcsolásával, mint a beam zone gombok esetében.

### Canvas célterületek hozzáadása / szerkesztése

A felső menüsávban válaszd a _View -> Canvas Target Areas_ lehetőséget. Itt láthatod a projektedben található összes canvas célterület beállításait.

Felül található az _ADD CANVAS TARGET AREA_ gomb.

Canvas célterületet a piros, mínusz jeles gombbal törölhetsz.

A méretet és a pozíciót a csúszkákkal állíthatod. Érték beírásához kattints duplán egy csúszkára.

### Scale mode

* **FIT TO AREA** - lekicsinyíti a tartalmat úgy, hogy teljesen beleférjen a canvas célterületbe, miközben megtartja a képarányt. (Ez az alapértelmezett beállítás)
* **FILL AREA** - úgy méretezi a tartalmat, hogy kitöltse a canvas célterületet, miközben megtartja a képarányt. A tartalom a széleken levágódhat.
* **STRETCH TO FIT** - a tartalmat a teljes canvas célterület kitöltésére nyújtja, a képarány figyelmen kívül hagyásával.
