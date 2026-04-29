---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Vezérlő-hozzárendelés

Miután beállítottad a lézereket a Liberationben, mindegyiket hozzárendelheted egy valós lézervezérlőhöz. (A használható hardverek ellenőrzéséhez lásd: [Kompatibilis lézerek és vezérlők (DAC-ok)](../hardware/compatible-lasers-and-controllers-dacs.md).) A vezérlők USB-n vagy hálózaton keresztül csatlakozhatnak.

* Nyisd meg a _Controller Assignment_ panelt a _View -> Controller Assignment_ menüponttal. (Vagy használhatod a _Laser Overview_ panelen található _ASSIGN LASER CONTROLLERS_ gombot is.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment panel"><figcaption></figcaption></figure>

* A panel két részre van osztva: bal oldalon a lézerek listája, jobb oldalon az elérhető vezérlők listája látható. Ha nem látod a lézervezérlőt a listában, nyomd meg a _REFRESH_ gombot. Ha továbbra is problémád van, lásd: [Hibaelhárítás](../troubleshooting/).
* Egy vezérlő lézerhez rendeléséhez kattints rá jobb oldalon, majd húzd át egy szabad lézerhelyre bal oldalon. Ezzel megadod a Liberationnek, hogy melyik vezérlőt melyik lézerhez használja. (Ha meggondolod magad, a vezérlőket szabadon áthúzhatod egyik lézerről a másikra.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Vezérlők listája" width="375"><figcaption></figcaption></figure>

* Ha zöld négyzetet látsz a vezérlő mellett, az azt jelenti, hogy a Liberation sikeresen csatlakozott hozzá.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Egy Ether Dream és egy Helios DAC hozzárendelve a 2-es, illetve 3-as lézerhez</p></figcaption></figure>

{% hint style="info" %}
Fontos: amikor csatlakozol egy vezérlőhöz, a lézer automatikusan hatástalanított állapotba kerül.
{% endhint %}

* A narancssárga négyzet 🟧 azt jelenti, hogy a vezérlőnél időszakos kapcsolati problémák jelentkeznek. Ezt általában hálózati probléma okozza; lásd: [Hibaelhárítás](../troubleshooting/).
* A piros négyzet 🟥 azt jelenti, hogy a vezérlő nem érhető el; lásd: [Hibaelhárítás](../troubleshooting/).
* A _disconnect button_ (X) bontja a kapcsolatot a vezérlővel, de nem törli a lézerhez tartozó hozzárendelést. Ezután a _reconnect button_ (frissítés nyíl ikon) használatával újracsatlakoztathatod, vagy ismét a _disconnect button_ gombra kattintva törölheted a hozzárendelést.
* _Haladó funkció:_ A diagramra hasonlító gombra kattintva nyisd meg a vezérlő analitikai paneljét. Ez egy haladó funkció, amely részletes információkat ad az adatfolyamról, és segíthet a problémák elhárításában. (Ez az opció egyes vezérlőtípusoknál nem feltétlenül érhető el.)
* A _rename button_ (ceruza) használatával tetszőleges névre átnevezheted a vezérlőt. Érdemes olyan nevet adni neki, amely alapján könnyen társítható az adott hardverhez. Ha a vezérlő egy lézerbe van beépítve, ennek megfelelően is elnevezheted, például _LaserCube Ultra #1_ vagy _Triton T5 #3._ Ezeket a neveket a Liberation telepítése elmenti, és ezentúl megjelennek; ez nagyon hasznos lehet a lézerek gyors azonosításához.

{% hint style="info" %}
Tipp: **kattints duplán** egy jobb oldali vezérlőre, hogy automatikusan hozzárendeld a bal oldali következő szabad lézerhez. Ez sok időt megtakaríthat, ha sok lézert kell hozzárendelned!
{% endhint %}

A _DISCONNECT ALL_ és _RECONNECT ALL_ gombokkal gyorsan alaphelyzetbe állíthatod az összes kapcsolatot. Ez hasznos, ha hálózati problémákat tapasztalsz.
