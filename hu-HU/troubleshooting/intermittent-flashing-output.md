---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Szakadozó / villogó kimenet

Nyisd meg a _Laser Overview_ panelt, és nézd meg a problémás lézer melletti csatlakozási jelzőfényt.

**Ha a csatlakozási jelzőfény NEM folyamatosan zöld:**\
Akkor valószínűleg hálózati vagy CPU-teljesítményproblémáról van szó:

**Hálózati teljesítmény -**

* Győződj meg róla, hogy nem Wi-Fi hálózathoz csatlakozol. Mindig vezetékes kapcsolatot használj. Ellenőrizd, hogy az operációs rendszer a vezetékes hálózatot részesíti-e előnyben a Wi-Fi-vel szemben, vagy kapcsold ki a Wi-Fi-t, ha nem vagy biztos benne.
* Ellenőrizd a hálózati adaptert, és próbálj ki egy másik USB-C adaptert.
* Windows-felhasználók: ellenőrizzétek / frissítsétek a hálózati illesztőprogramokat, és futtassátok a megfelelő hálózati teszteszközöket.
* Ellenőrizd az összes kábelt, switchet és routert. Módszeresen cseréld ki és teszteld végig az összes kábelt.
* Indítsd újra az összes hálózati eszközt, beleértve a switcheket, routereket és minden Ether Dream eszközt.

**CPU-teljesítmény**

Ha régi vagy alacsony teljesítményű gépet használsz, előfordulhat, hogy túl lassú a Liberation futtatásához. Ellenőrizd a képkockasebesség-jelzőt az ikonsáv jobb oldalán.

Két szám látható ott: a tényleges képkockasebesség és a cél képkockasebesség. Ha a tényleges képkockasebesség 30 alá esik, problémák jelentkezhetnek.

A következő lépések segíthetnek:

* Távolítsd el a nem használt lézereket; például ha csak egy lézer van csatlakoztatva, töröld a többit.
* Válts az Output vagy Canvas nézetre.
* Zárj be minden más programot, ellenőrizd a hálózati tűzfalbeállításokat, zárd be a vírusirtót, a Dropboxot stb.
* Csökkentsd a kijelző felbontását, és tedd kisebbre a Liberation ablakát.

Ha ezek egyike sem segít, érdemes megfontolni a számítógép fejlesztését vagy cseréjét.

***

**Ha a csatlakozási jelzőfény folyamatosan zöld:**

Akkor valószínűleg hardverproblémáról van szó. Ez kívül esik a kézikönyv hatókörén, de a következőket megpróbálhatod:

* Tiltsd le az SFS (Scan Fail Safety) rendszert. Egyes lézereknél van olyan funkció, amely letiltja a kimenetet, ha a szkennerek leállnak, vagyis erős statikus nyalábot hoznának létre. Ezek néha túl óvatosak / megbízhatatlanok lehetnek.

{% hint style="danger" %}
A scan fail safety rendszer letiltásakor rendkívül óvatosan járj el. Az erős statikus nyalábok égést okozhatnak! Legyen kéznél vészleállító gomb és tűzoltó készülék.
{% endhint %}

* Ellenőrizd az interlock kábeleket és rendszereket.
* Ellenőrizd a vezérlő és a lézer közötti összes kábelezést.

Egy [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) felbecsülhetetlen segítség lehet a lézerproblémák hibakereséséhez.
