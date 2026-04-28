---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube promóciós kép a Wicked Lasers jóvoltából</p></figcaption></figure>

A Wicked Lasers [LaserCube](https://www.laseros.com/lasercube/) egy rendkívül kompakt, akkumulátoros lézeregység, amely többféle teljesítménykonfigurációban érhető el. A hobbifelhasználók körében népszerű a könnyen használható okostelefonos alkalmazása miatt, de az újabb modellek már elég fejlettek ahhoz, hogy professzionális show-kban is használhatók legyenek.

A telefonos alkalmazás (LaserOS néven, asztali gépre is elérhető) ingyenesen letölthető, nagyon szórakoztató, és a legtöbb felhasználónak elegendő. Ha viszont nagyobb show-kat futtatsz több lézerrel, specializáltabb és nagyobb teljesítményű megoldásra lesz szükséged – itt jön képbe a Liberation.

### Csatlakozás LaserCube-hoz

A korai LaserCube modellek USB-n keresztül vezérelhetők, de a jelenlegi modellek mind beépített hálózati vezérlővel rendelkeznek. Ezeket a hálózaton vezérelhető kockákat „LaserCube Wifi” néven ismerik. A Liberation mindkét LaserCube-típust támogatja\*, akár USB-n, akár hálózaton keresztül csatlakoznak.

\*(A LaserCube hálózati protokoll támogatása a 0.7.3-as verzióban jelent meg)

### USB LaserCube

Csatlakoztasd a LaserCube-ot a számítógéphez micro USB kábellel, majd keresd meg a _Controller Assignment_ panelen (lásd: [controller-assignment.md](../setting-up/controller-assignment.md)). Ha nem jelenik meg automatikusan, kattints a _REFRESH_ gombra.

### Hálózati LaserCube „Wifi”

{% hint style="danger" %}
Bár a „Wifi” kockákat vezeték nélküli hálózaton való használatra tervezték, ez nem ajánlott, mert nagy eséllyel kimaradások és hibák jelentkeznek. Ehelyett használd az RJ45 aljzatot, és csatlakoztasd a LaserCube-ot vezetékes hálózathoz, ugyanúgy, ahogy az Ether Dream esetében tennéd.
{% endhint %}

Csatlakoztasd a LaserCube-ot a vezetékes hálózatodhoz.

Állítsd a LaserCube-ot „LAN Client” módba, és győződj meg róla, hogy van router a hálózaton. A LaserCube IP-címet kap a routertől, ezután meg kell jelennie a _Controller Assignment_ panelen. (Lásd: [controller-assignment.md](../setting-up/controller-assignment.md)).

{% hint style="info" %}
Router nélkül is létrehozható hálózat, ahol minden eszköz fix IP-címet kap, és ez nagyon gyakori a rendezvényiparban. Én személy szerint jobban szeretem, ha van router a hálózaton, és ezt ajánlom mindenkinek, akinek kevesebb tapasztalata van hálózatokkal.

A router dinamikusan oszt IP-címet mindennek; szerintem ez egyszerűbb és kevésbé hibalehetőséges.
{% endhint %}

{% hint style="danger" %}
Az Ether Dreammel ellentétben a _**LaserCube-ok NEM BLANKELIK A LÉZERT**_, ha buffer alulfutást, elveszett csomagot vagy más sérült / helytelen adatot észlelnek.

Ehelyett egyszerűen onnan folytatják, ahol abbahagyták, és ez bizonyos esetekben azt eredményezheti, hogy egy aktív nyaláb olyan területeken halad át, amelyek nincsenek zónákon belül, sőt rosszabb esetben a szoftveres maszkokon is átvág.

Egyeztetek a LaserCube tervezőivel/fejlesztőivel, és remélem, hogy ezt a jövőben firmware-frissítéssel kezelni fogják. Addig azonban gondoskodnod kell arról, hogy fizikailag kitakarj minden olyan területet, ahová nem szeretnéd, hogy a lézer eljusson.

Az igazsághoz hozzátartozik, hogy ezt valószínűleg amúgy is meg kellene tenned, de én magam szoftveres maszkokat használok kamerák és projektorok védelmére. Ezért fontos tudni, hogy LaserCube hálózati protokoll használatakor ez veszélyesebb, mint Ether Dreammel (amely azonnal biztonsági leállás módba lép, amint bármilyen hiba vagy hiányzó adat jelentkezik).

És bár már mondtam: **használj vezetékes kapcsolatot a LaserCube-hoz**. A Wifi erre nem lesz elég, és ezt a problémát még tovább rontja.
{% endhint %}
