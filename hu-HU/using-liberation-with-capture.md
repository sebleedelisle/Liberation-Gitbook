---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 A Liberation használata Capture-rel

A Liberation külső visualiserként támogatja a [Capture](https://capture.se) alkalmazást (az 1.0.3-as verziótól). Ha már használod a Capture-t a munkafolyamatodban, akkor megjelenítheted vele a Liberation élő lézerkimenetét a 3D jelenetedben.

### Hogyan működik?

Nincs szükség külön csatlakoztatási folyamatra vagy kézi összekapcsolásra.

Ha:

* a Liberation és a Capture ugyanazon a hálózaton van
* a tűzfal engedélyezi a kapcsolatot

…akkor a Liberationben beállított lézerek automatikusan megjelennek a Capture-ben médiaforrásként. Nem kell IP-címeket konfigurálnod vagy külön funkciót engedélyezned – egyszerűen megjelenik.

### Lézerek megjelenítése Capture-ben

A Liberationben konfigurált összes lézer elérhető médiaforrásként jelenik meg a Capture-ben.

Ahhoz, hogy ténylegesen lásd a kimenetet:

* a lézert élesíteni kell a Liberationben
* a forrást hozzá kell rendelni egy lézer fixture-höz a Capture-ben

Élesítés után a Capture megjeleníti a Liberation élő kimeneti streamjét. Ha egy lézer nincs élesítve a Liberationben, továbbra is látható marad forrásként a Capture-ben, de nem ad ki jelet.

A lézerek Capture-ben történő beállításához további útmutatást és támogatást a [capture.se](https://www.capture.se/) dokumentációjában találsz. <br>

### Licencekorlátok és élesített lézerek

A Capture-kapcsolatok pontosan ugyanúgy számítanak, mint a fizikai lézerkimenetek.

Ez azt jelenti, hogy:

* csak annyi lézert élesíthetsz, amennyit a licencszinted engedélyez
* csak az élesített lézerek küldenek aktívan adatot a Capture felé

### Szükségem van Capture-re?

Egyáltalán nem.

A Liberation tartalmaz egy beépített 3D visualisert, amely mindig elérhető, és nem függ a licencszintedtől. A show-kat közvetlenül a Liberationben tervezheted meg és tekintheted meg előnézetben, külső szoftver nélkül.

A Capture egyszerűen egy további lehetőség, ha már használod világításhoz vagy show-tervezéshez.

### Hibaelhárítás

Ha a lézerek nem jelennek meg a Capture-ben:

* ellenőrizd, hogy mindkét alkalmazás ugyanazon a hálózaton van-e
* ellenőrizd a tűzfalbeállításokat
* győződj meg róla, hogy a lézer élesítve van a Liberationben
