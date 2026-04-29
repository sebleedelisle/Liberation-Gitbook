---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Effektek

A Liberation effekt rendszere szórakoztató és sokoldalú módot ad arra, hogy valós időben módosítsd a klipek kimenetét. Az effektek teljesen rugalmasak: villogtathatsz velük mindent, ki-be kapcsolhatod, forgathatod, megváltoztathatod a színeket, vagy akár véletlenszerűen mozgatva „röptetheted” is a tartalmat.

Bármi, amit a klipszerkesztőben meg tudsz csinálni, effektként is használható. Sőt, az effektek pontosan ugyanazzal a nodeszerkesztővel szerkeszthetők, mint a klipek. Lásd: [Effektek](effects.md#editing-effects). A kreatív lehetőségek gyakorlatilag végtelenek.

Az alapértelmezett 1–8-as effektgombok a zónagombok alatt találhatók, a 9–24-es effektek pedig az alsó sorban lévő kis gombok.

#### Effekt alkalmazása

Nyomj meg egy effektgombot az effekt ki- vagy bekapcsolásához, de még jobb, ha az APC40 1–8-as csúszkáival úsztatod be és ki az effekteket. Ha APC40 nélkül szeretnél beúsztatni egy effektet, kattints a gombra, és húzd fel-le. Vagy kattints jobb gombbal az effektgombra, és állítsd a szintcsúszkát.

{% hint style="warning" %}
Az effektgomb megnyomása azonnal aktiválja az adott effektet. Fontos azonban, hogy ha a szint nullára van állítva, semmi sem fog történni. Kattints és húzd a gombot a szint módosításához, vagy kattints jobb gombbal, és használd a _level_ csúszkát, illetve használd az APC40 fadereit.
{% endhint %}

#### Effektek és a klip zónakésleltetése

Az effektek átveszik az éppen futó klipek zónakésleltetési beállítását. Tehát ha a klipedben van egy balról jobbra haladó késleltetés, és hozzáadod a villogó effektet, akkor a villogás is balról jobbra késleltetve jelenik meg.

{% hint style="info" %}
Azt, hogy a klip zónakésleltetését hogyan öröklik az effektek, nagyon nehéz leírni, de teljesen egyértelművé válik, amint kipróbálod.

Szerintem ez a Liberation egyik legszórakoztatóbb és legkreatívabb beépített eszköze. Próbáld ki, és látni fogod, mire gondolok.
{% endhint %}

#### Effektparaméterek

Adj paramétert az effektedhez egy _Parameter node_ segítségével. A Parameter rendszerrel az effekten belüli több beállítást kívülről is módosíthatsz. További információ: [Parameter Control](clip-editor/oscillators/parameter-control.md).

Az 1–8-as forgóvezérlőkkel állíthatod az egyes effektek _parameter_ értékét. Vagy kattints jobb gombbal az effektgombra, és állítsd a paramétercsúszkákat. A paraméter módosítása attól függően más-más dolgot csinál, hogyan van felépítve az effekt. Az alábbi listában láthatod az alapértelmezett effekteket és azt, hogy mit csinálnak a paramétereik.

{% hint style="info" %}
Az 1–8-as forgóvezérlők az APC40 Mk2 felső részén, az Mk1 esetén pedig jobb felül találhatók. Lásd még: [APC40 referencia](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
Az effektgombokon látható kis számok az effekt _level_ és _parameter_ értékére utalnak. A _level_ értéket az APC40 faderével vezérelheted, vagy kattintással és húzással állíthatod a gombon. A paramétert az APC40 forgóvezérlőivel módosíthatod, vagy jobb kattintással egérrel is beállíthatod.
{% endhint %}

#### Az alapértelmezett effektek

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Kaotikus mozgást alkalmaz a klip kimenetére. A paraméter a káosz mértékét/sebességét állítja.
2. **Sine wave** :\
   Az összes tartalmat egy mozgó szinuszhullám mentén torzítja. A paraméter a hullámhosszt állítja.
3. **Rotation** :\
   Mindent körbeforgat. A paraméter a forgási sebességet állítja.
4. **Horizontal flip** :\
   Vízszintesen összenyomja és széthúzza a tartalmat. A paraméter a sebességet állítja.
5. **Scale** :\
   Ismételten teljes méretről nullára skáláz mindent. A paraméter a sebességet állítja.
6. **Hue** :\
   Megváltoztatja minden elem színárnyalatát, de a telítettséget nem módosítja (azaz ami fehér, az fehér marad). A paraméter a színárnyalatot állítja.
7. **Saturation and hue** :\
   Megváltoztatja minden elem színárnyalatát, és teljesen telítetté teszi a színt (azaz ami fehér, az is az adott színre változik). A paraméter a színárnyalatot állítja.
8. **Flash** :\
   Ismételten teljes fényerőről nullára villogtatja az összes tartalom fényerejét. A paraméter a villogás sebességét állítja.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Az alsó sorban további 16 színeffekt található, amelyek előre beállított színárnyalat- és telítettségértékeket alkalmaznak.

Fontos, hogy ezek az alapértelmezett effektek, de szerkeszthetők, így szinte bármit csinálhatnak, amit szeretnél.

### Alkalmazás csoportokra

Kiválaszthatod, mely csoportokra hasson az effekt. Kattints jobb gombbal, és kapcsold be vagy ki az _Apply to groups_ feliratú csoportjelölőnégyzeteket.

Ezt a beállítást főleg akkor használom, amikor a canvas grafikákkal és a lézersugarakkal külön dolgozom. Az összes canvas klipet az 5-ös csoporthoz rendelem, majd ezt a csoportot kizárom azokból az effektekből, amelyekkel nem szeretném módosítani ezeket a grafikus klipeket.

Arra is használhatod, hogy élőben egyszerre 2 különböző színváltást alkalmazz 2 lézercsoportra. Hozz létre két színváltó effektet, majd válaszd ki, hogy mely klipcsoportokra legyenek alkalmazva.

### MX csoport

A _Mutually Exclusive_ rövidítése: ezzel úgy csoportosíthatod az effekteket, hogy a csoporton belül egyszerre csak egy effekt lehessen aktív. Figyeld meg, hogy az alapértelmezett színváltó effektek közül egyszerre csak egy lehet aktív. Ez azért van, mert mindegyik az MX Group 1 része.

Ez a funkció le van tiltva, ha az _MX Group_ beállítás értéke 0.

### Effektek szerkesztése

Kattints jobb gombbal bármelyik effektre, majd kattints az _EDIT EFFECT_ gombra az effektszerkesztő megnyitásához. Láthatod, hogy ez a szerkesztő megegyezik a klipszerkesztővel.

Az effektet ugyanúgy szerkesztheted, mint bármelyik klipet. Lásd: [A Clip Editor](clip-editor/).

Legalább egy creator node szükséges; ez bármi lehet (vonal, kör, alakzat, akár szöveg is), de érdemes olyat választani, ami az effektgomb előnézetében a legérthetőbb.

Az effektek alkalmazásakor az effektben lévő összes creator node helyére az éppen futó klipek kimenete kerül.

{% hint style="warning" %}
Kifejezetten unalmas technikai okokból a "trails" node-ok nem engedélyezettek effekten belül. Ugyanez vonatkozik a pattern node-okban lévő "delay" beállításra is (ugyanazt a rendszert használják). Ezt a későbbi verziókban javítjuk.
{% endhint %}
