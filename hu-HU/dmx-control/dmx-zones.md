---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ DMX zónák

A DMX zone a Liberation olyan kimeneti zone típusa, amely lézerpontok helyett Art-Net/DMX adatot küld. A beam zone és canvas zone mellett jelennek meg, így a Clips ugyanabban a zone-választási munkafolyamatban rendelhetők hozzájuk.

A kezelésükhöz nyisd meg a menüből a **DMX Zones** elemet, vagy használd a Laser Overview DMX szakaszát.

* **ADD DMX ZONE** - új DMX zone létrehozása.
* **ARM** - engedélyezi a DMX-kimenetet az adott zone számára. Ha egy DMX zone nincs élesítve, a hozzárendelt csatornáit nullára állítja.
* **Node** - kiválasztja az Art-Net node számát.
* **Universe** - kiválasztja az Art-Net universe értékét. A megjelenített érték 1-től számozott, tehát a Universe 1 az első universe.
* **Address** - beállítja a lámpatest kezdőcímét. A megjelenített érték szintén 1-től számozott.
* **Preset** - kiválasztja azt a DMX presetet, amely a Clip tartalmát DMX-csatornákra képezi le.
* **Edit DMX zone settings** (ceruza ikon) - megnyitja a zone beállításait, például a kézi zone-továbbítást és a lámpatest tájolását.
* **Edit DMX profile/channel mapping** (csúszkák ikon) - megnyitja a DMX preset-/csatornaszerkesztőt.
* **Delete** - eltávolítja a DMX zone-t.

### Élesítési korlátok

Az egyszerre élesíthető DMX zone-ok száma a licencszintedtől függ. Ha a licencszinted nem engedélyezi a DMX-kimenetet, vagy már élesítetted a maximális számú DMX zone-t, a további zone-ok **ARM** gombja le van tiltva, és rámutatáskor behajtani tilos ikont jelenít meg.

Mielőtt további zone-okat élesítenél, kapcsold ki az élesítést egy másik DMX zone-nál, vagy használj magasabb DMX-korláttal rendelkező licencszintet.
