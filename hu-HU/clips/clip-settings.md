---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip beállításai

### Clip settings panel

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>A clip beállítási panelje</p></figcaption></figure>

A clip kimeneti méretét a _Scale X_ és _Scale Y_ segítségével módosíthatod. Ezek együtt vannak zárolva, kivéve, ha lenyomva tartod a _SHIFT_ billentyűt.

A clip vízszintes és függőleges pozícióját a _Shift X_ és _Shift Y_ segítségével módosíthatod.

A _Zone Delay/Chase_ annyira szórakoztató funkció, hogy külön szakaszt kapott. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Parameters panel

A Clip Deck jobb oldalán lévő panel nyolc környezetfüggő paramétert jelenít meg. Ha ki van választva egy Clip, az első vezérlők a kiválasztott Clip _Shift X_, _Shift Y_ és _Zone Delay_ beállításai, ezeket pedig a globális _Spin_ és _Scale_ vezérlők követik.

Ugyanezek a paraméterek a támogatott MIDI vezérlőkön is megjelennek. Ha nincs kiválasztva Clip, a Cliphez tartozó mezők üresek. Ha lenyomva tartasz egy csoportgombot, az első két vezérlő az adott csoport fade in és fade out idejére vált.

### Clip zárolása

Ha egy clip zárolva van, nem lehet áthelyezni vagy törölni. Egy clip zárolásához használd a jobb kattintásos menü _Locked_ jelölőnégyzetét. A Clip settings panel további beállításokat is kínál.

* _UNLOCK ALL -_ feloldja a Clip Deck összes clipjét.
* _AUTO-LOCK_ - ha az _Auto-Lock_ be van kapcsolva, minden automatikusan lejátszott clip — akár a timeline, akár a MIDI felvétel/lejátszás rendszer indítja — zárolva lesz. Ez akkor hasznos, ha Logic Próban (vagy hasonló szoftverben) programoztál egy show-t, és nem szeretnéd véletlenül módosítani a show-ban használt clipeket.
* _LOCKED CLIPS ZONES_ - ha ez be van kapcsolva, nem módosíthatod a zónákat egyetlen zárolt clipnél sem.
* _LOCKED CLIPS PARAMS_ - ha ez be van kapcsolva, nem módosíthatod a paramétereket (scale, shift stb.) egyetlen zárolt clipnél sem.

### Jobb kattintásos menü

Ha jobb gombbal kattintasz egy Clipre, megjelenik egy menü a Cliphez tartozó néhány beállítással. A menü első elemeiről bővebben lásd: [Bevezetés a Clip Editor használatába](../clip-editor/clip-editor-intro.md "mention"), [Clip beállításai](clip-settings.md "mention") és [Clipcsoportok](groups.md "mention").

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

A clipek alapértelmezés szerint _retrigger_ módra vannak állítva. Ez azt jelenti, hogy amikor megnyomod, a clip onnantól kezd el futni. Ha tehát későn indítod el, a clip animációja kissé késni fog, és nem lesz pontosan ütemben.

{% hint style="info" %}
Ha egy retriggerelt clip futása közben _Tap Tempo_-t használsz, a rendszer „kvantálja” a clipet, hogy ütemben legyen, még akkor is, ha nem pontosan az ütésre indítottad.
{% endhint %}

Ha a _Retrigger_ nincs engedélyezve, a clip mindig ütemben lesz — úgy viselkedik, mintha a clip az óra legelején indult volna el. Ez akkor jó, ha külső órajel segítségével tökéletesen szinkronban vagy a zenével.

{% hint style="info" %}
A clipeket gyakran úgy tervezik, hogy végtelenül ismétlődjenek, de készítheted őket úgy is, hogy csak egyszer vagy néhányszor fussanak le. Ezeknél mindenképpen hagyd bekapcsolva a _retrigger_ beállítást, különben nem indulnak újra!
{% endhint %}

### Be-/kimeneti átmeneti idő (fade)

A Clips esetén beállítható, hogy másodpercben megadott időtartam alatt fade in és fade out történjen. Alapértelmezés szerint a fade időt a csoport beállításaiból öröklik (ez a csoport gombjára jobb gombbal kattintva módosítható).

Ha a clip csoportjától eltérő fade időt szeretnél, először kapcsold ki a _USE GROUP DEFAULT_ gombot, majd állítsd be a clip _In time_ és _Out time_ csúszkáit.
