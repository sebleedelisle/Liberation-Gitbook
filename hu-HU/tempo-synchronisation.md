---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempó / szinkronizálás

A zenei szinkronizálás a Liberation egyik alapvető eleme; ha a tempó és az ütemek illeszkednek a zenéhez, biztos lehetsz benne, hogy minden szinkronban lesz. Ha van lehetőséged MIDI clock (vagy Ableton Link) használatára, akkor egyáltalán nem kell kézi szinkronizálással foglalkoznod. Ha nincs, az sem gond – a _Live_ tempó funkcióval kézzel is pontosan hozzáigazíthatod.

Ha van tapasztalatod zenei vagy világítástechnikai szoftverekkel, ez a folyamat ismerős lesz. Ha nincs, érdemes időt szánni a rendszer megismerésére, és otthon gyakorolni, mielőtt élő show-n használod.

## Tempo panel

A _Tempo_ panel mindig látható a képernyőn, és az összes szinkronizálási beállítást tartalmazza. Felül az aktuális ütem/ütés számláló, valamint a lejátszásvezérlő látható play/pause és rewind/fast-forward gombokkal.

Alatta található az ütemjelző: négy négyzet, amelyek az ütemre „pulzálnak”. Ez a _beat marker_ rendkívül hasznos vizuális visszajelzés, és a _Live_ tempó rendszer használata közben folyamatosan erre fogsz támaszkodni.

### A tempó beállítása

A tempó beállítására több lehetőség is van:

* Kattints és húzd a _Tempo_ csúszkát
* Shift-kattintással húzd a _Tempo_ csúszkát, ha 0,1-es lépésekben szeretnéd módosítani a tempót
* Kattints duplán a _Tempo_ csúszkára, és írd be kézzel az értéket
* Használd az APC40 _Tempo_ tekerőgombját (0,1-es lépésekhez tartsd lenyomva a Shiftet)
* Tap Tempo

{% hint style="info" %}
A tempó „beats per minute” értékben van megadva, a hagyományos alapértelmezett érték általában 120.
{% endhint %}

## Tap Tempo

A tempó automatikus beállításához kattints a _TAP_ gombra az ütemmel együtt. Az ütem elejét a _RESET_ gombbal állíthatod be.

{% hint style="info" %}
A Tap Tempo rendszer elég okos ahhoz, hogy felismerje, ha egy ideig nem kopogtál, vagy ha kihagytál néhány ütést. Ha dupla tempóban kezdesz kopogni, megérti, hogy duplázni szeretnéd a tempót; ugyanez igaz akkor is, ha felezett tempóban kopogsz.

Azt is képes felismerni, ha két ember egyszerre adja meg a tempót kopogással (például az egyik a billentyűzeten, a másik az APC40-en). A Liberation átlagolja a dupla koppintásokat.
{% endhint %}

#### Billentyűparancsok:

T - tap tempo\
R - az ütem visszaállítása\
Y - a tempó kerekítése a legközelebbi beats per minute értékre.

{% hint style="info" %}
Mivel manapság a legtöbb zene digitálisan készül, a tempó nagy valószínűséggel kerek egész szám. Ha tehát a bekopogott tempó közel jónak tűnik, használd az Y billentyűt (vagy mozdítsd el az APC40 tempó tekerőgombját egy „kattanással”), hogy egész számra kerekítsd.
{% endhint %}

#### APC40 vezérlők:

Az APC40-en külön _TAP TEMPO_ gomb található, de akár csatlakoztatott lábkapcsolóval is kopoghatod a tempót a lábaddal!

A beállításhoz használd a _TEMPO_ tekerőgombot. Finomhangoláshoz tartsd lenyomva a _SHIFT_ gombot a _TEMPO_ tekerőgomb használata közben.

A _METRONOME_ gombbal **visszaállíthatod az ütemet**. (A _METRONOME_ gomb az ütemmel együtt fel is villan.)

A _TEMPO_ tekerőgombot egy „kattanással” jobbra vagy balra elfordítva **kerekítheted a tempót** felfelé vagy lefelé egész BPM értékre.

Lásd még: [APC40 referencia](reference/apc40-reference.md "mention")

### Tempó igazítása

Ha biztos vagy benne, hogy elég közel vagy a tényleges tempóhoz, de azt tapasztalod, hogy idővel elcsúszik a szinkron, használd a _NUDGE_ gombokat a korrekcióhoz.

Ha a Liberation tempója a zene elé siet, tartsd lenyomva a _NUDGE -_ gombot, hogy ideiglenesen lassítson, amíg újra össze nem igazodik.

Ha a Liberation tempója lemarad a zenétől, tartsd lenyomva a _NUDGE +_ gombot, hogy ideiglenesen gyorsítson, amíg újra össze nem igazodik.

{% hint style="info" %}
Használhatod a képernyőn látható NUDGE gombokat vagy az APC40 dedikált gombjait is.
{% endhint %}

### Half time / double time

A _÷2_ és _x2_ gombokkal véglegesen felezheted vagy duplázhatod a tempót. A tempo multiplier funkcióval ellentétben ez tartós módosítás az aktuális tempón.

## Tempo Multiplier

A _Tempo Multiplier_ rendszerrel ideiglenesen módosíthatod a tempót, majd visszatérhetsz az eredeti értékre.

A _Tempo Multiplier_ be- és kikapcsolásához nyomd meg a _TEMPO MULTIPLIER_ gombot vagy az APC40 _BANK_ gombját. Az értéket a képernyőn látható csúszkával vagy az APC40 A-B csúszkájával állíthatod. Használhatod a _25%, 50%, 100% 200%_ preset gombokat is.

## Külső tempóforrások

### MIDI Clock

Külső MIDI clock jelhez való szinkronizáláshoz válaszd ki a _MIDI CLOCK_ rádiógombot, majd a legördülő menüből a MIDI eszközt. Figyeld a legördülő menük melletti színes állapotjelző fényt:

* Zöld - MIDI clock jel érkezik
* Narancssárga - csatlakozni tud a MIDI eszközhöz, de jelenleg nincs clock jel
* Piros - nem tud csatlakozni a MIDI eszközhöz

{% hint style="info" %}
A MIDI Clock képkockák sorozatát sugározza (negyedhangonként 24-et), de az üzenetek nem tartalmaznak pozícióadatot. Ez azt jelenti, hogy hasznos a tempó tartásához, de előfordulhat, hogy az ütemet továbbra is vissza kell állítanod.

A Liberation MIDI Clock tempóforrás a **MIDI Machine Control (MMC)** üzenetekre is reagál, így ha a clock forrásod továbbít ilyeneket, nem kell kézzel visszaállítanod az ütemet.
{% endhint %}



### Ableton Link

Az Ableton Linkkel való szinkronizáláshoz válaszd az _ABLETON LINK_ tempóforrást. A Liberation csatlakozik a helyi hálózaton futó Link munkamenethez, és követi a többi Link-kompatibilis alkalmazás közös tempóját és ütésfázisát.

Az Ableton Link nem használ MIDI portot, és nem továbbít abszolút dalpozíciót. Ha azt szeretnéd, hogy a Liberation ütemkezdete a show egy adott pillanatához igazodjon, használd az ütem-visszaállítási vezérlőket.

### Timeline

Minden timeline saját tempóval rendelkezik, amely lehet fix érték vagy _Tempo Map_. A _Tempo Map_ lehetővé teszi, hogy a timeline adott időpontjainál módosítsd a tempót.

A timeline tempója akkor lesz használatban, ha a tempóforrásként a _TIMELINE_ van kiválasztva.

{% hint style="info" %}
A timeline-t _bármelyik_ tempóforrással együtt futtathatod! Ha például élő zenekarod van, amely nem clickre játszik, kézzel elindíthatod a timeline-t, és a _LIVE_ tempóforrással szinkronban tarthatod. Vagy ha van MIDI clock jeled, azt is használhatod!
{% endhint %}
