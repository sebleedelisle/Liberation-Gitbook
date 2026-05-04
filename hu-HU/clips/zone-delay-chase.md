---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Abban mindannyian egyetértünk, hogy több lézerrel több a lehetőség, de ha mind pontosan ugyanazt csinálja, sok kreatív lehetőségről lemaradsz.

A Zone delay rendszer egyszerű, mégis hatékony módszer arra, hogy változatosságot vigyél a zones között, és igazán kihasználd a több lézeres összeállítást. Hagyományosabb chase effekt létrehozására is használható.

#### Hogyan működik

A _Zone delay_ késleltetést ad a clip időzítéséhez zónánként, így egyfajta söprő mozgást hoz létre a zónák között.

Különösen hatásos, ha a Zone delay-t egy már futó cliphez adod hozzá: az APC40 megfelelő vezérlőjével állíthatod a mértékét és a mintát. (Lásd: [APC40 referencia](../reference/apc40-reference.md "mention")). Használhatod a _Clip Settings_ panelt is.

Zone delay beállítások:

* **Zone delay** - az egyes zónákra alkalmazott késleltetés idejét szabályozza, hatvannegyed hangértékekben mérve.
* **Pattern** - a zónák sorrendjének kiválasztása
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
A pattern a zónaszámok alapján működik, és feltételezi, hogy a zónák balról jobbra sorrendben vannak. A minták számításakor a Zone delay a Canvas-zónákat és a DMX-zónákat külön csoportként kezeli.
{% endhint %}

* **Delay mode**
  1. No delay - chase módban ezt használd
  2. Delay - az alapértelmezett mód; késlelteti az egyes zónák időzítését
  3. Delay with re-trigger - a pattern mentén minden alkalommal visszaállítja a clipet az elejére. Ez jól működik _Chase mode_ használatával.
* **Chase mode** - bekapcsolt chase módnál minden zóna a hagyományos chase effekthez hasonlóan kapcsol be és ki. A chase megjelenését a _Fade in, Hold,_ és _Fade out_ beállításokkal szabályozhatod. Ezek a beállítások a zone delay érték arányaként vannak megadva, tehát az 1 érték ugyanannyi időt jelent, mint amit a _Zone delay_ értéknél megadtál. Ezt kicsit nehéz elmagyarázni, ezért azt javaslom, próbáld ki magad.

{% hint style="info" %}
A Zone delay az aktív effektekre is érvényes. Például egy villogó effekt ugyanúgy késleltetve jelenik meg a zónák között, mint maga a clipen belüli animáció.
{% endhint %}

Ha egy clip bármilyen _Zone delay_ beállítást használ, a clip jobb felső sarkában egy hárompontos ikon jelenik meg. Ezek a pontok animálva mutatják az adott clip _Zone delay_ stílusát. További részletekért lásd: [Mik azok a kis ikonok a Clip gombokon?](what-are-the-small-icons-on-the-clip-buttons.md "mention").

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>A hárompontos szimbólum jelzi, hogy a clip Zone delay beállítást használ, valamint annak módját</p></figcaption></figure>

{% hint style="info" %}
A Zone delay clipenkénti beállítás, nem globális; a clip kreatív kialakításának része.
{% endhint %}
