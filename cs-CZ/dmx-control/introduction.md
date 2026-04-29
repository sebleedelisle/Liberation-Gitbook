---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Úvod

Liberation obsahuje flexibilní a výkonný systém DMX, který umožňuje vytvářet světelné efekty a ovládat lasery kompatibilní s DMX přes Art-Net. Je navržený tak, aby bylo snadné udržet světla synchronizovaná s laserovou show – bez potřeby samostatného světelného pultu.

{% hint style="info" %}
**Co je Art-Net a jak souvisí s DMX?**

**DMX** je systém, který se už mnoho let používá k ovládání světel, laserů, výrobníků kouře a dalších scénických efektů. Posílá řídicí signály po speciálních kabelech, obvykle s konektory XLR, a každé zařízení sleduje konkrétní sadu kanálů, podle kterých ví, co má dělat.

**Art-Net** je novější způsob přenosu stejných DMX dat přes běžnou počítačovou síť. Místo speciálních kabelů posílá vše přes Ethernet, stejně jako internetový nebo lokální síťový provoz.

V Liberation se veškerý DMX výstup posílá pomocí Art-Net. Můžete jím přímo ovládat zařízení kompatibilní s Art-Net, nebo připojit **Art-Net node** – malou krabičku, která převádí Art-Net zpět na standardní DMX. Díky tomu můžete dál ovládat tradiční DMX světla a efekty, i když samy Art-Net nepodporují.
{% endhint %}

Můžete ho také použít k ovládání různých typů scénické techniky, například výrobníků kouře, hazerů, CO₂ trysek, strojů na studené jiskry a dalších zařízení. Pokud podporují DMX, můžete je nastavit jako DMX zone a spouštět přímo z Liberation, společně s laserovým obsahem.

DMX zařízení se přidávají jako **DMX zones**, které se zobrazují v seznamu zones vedle laserových beam zones a cílových oblastí Canvas. Každá DMX zone používá **DMX preset**, který Liberation říká, jak mapovat vlastnosti z laserových Clips – například polohu, barvu a jas – na hodnoty DMX kanálů.

Když pošlete Clip do DMX zone, Liberation se podívá na první prvek v daném Clip a převede jeho vlastnosti podle zvoleného preset. Díky tomu můžete snadno řídit světla a DMX efekty přímo ze stejných Clips, které už používáte pro lasery.

#### Liberation na Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

První skutečnou zkouškou DMX systému v Liberation byl festival Glastonbury 2023, kde společnost Reach Lasers nainstalovala celkem 90 zdrojů paprsků jako součást pódia Arcadia „spider“.

18 laserů bylo řízeno pomocí interních Ether Dreams a dalších 12 beam barů se 6 hlavami bylo ovládáno přes Art-Net a DMX.
