---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Megváltoztatja az összes bejövő tartalom színeit. Beállíthatsz fix HSB-értékeket, vagy átválthatsz a gradiensrendszerre, és egy egyéni gradiensből mintavételezhetsz színeket.

* **hue, saturation, brightness** - a színértékek, lásd: [Színbeállítások és HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - a hue nem módosul
  * FIXED - az elemek hue értéke a megadott hue értékre áll
  * SHIFT - az elemek hue értéke a megadott értékkel eltolódik, így a különböző színű elemek továbbra is különbözőek maradnak, csak a hue érték mentén eltolva.
* **saturation mode** -
  * OFF - a saturation nem módosul
  * FIXED - a saturation a megadott értékre rögzül.
* **brightness mode** -
  * OFF - a brightness nem módosul
  * FIXED - az elemek brightness értéke a megadott brightness értékre áll
  * MULTIPLY - az elemek brightness értéke a brightness értékkel kombinálódik, így ha villognak, továbbra is villogni fognak, de legfeljebb az itt megadott brightness értékig.
* **gradient mode** - a fix HSB csúszkákról a gradiensszerkesztőre vált. A node egy színt mintavételez a gradiensből, majd a fenti hue, saturation és brightness módokkal alkalmazza.
* **gradient position** - kiválasztja, hogy a gradiens melyik pontjából történjen a mintavételezés. Animáld 0%-tól 100%-ig egy Sawtooth Oscillator segítségével, hogy időben végighaladj a gradiensen.
* **blend** - meghatározza, milyen erősen érvényesül a színváltó: 0% esetén egyáltalán nem, 100% esetén teljes mértékben, 50% esetén pedig a meglévő szín és az új értékek keveréke.

{% hint style="info" %}
A Colour Change node a teljes bemenethez egyetlen színt mintavételez a gradiensből. Ha azt szeretnéd, hogy a gradiens pozíció alapján fusson végig az alakzaton, használd inkább ezt: [pozícióalapú módosítók](position-based-changers.md "mention").
{% endhint %}

### Gradiensszerkesztő

Ha a **gradient mode** be van kapcsolva, a gradiensszerkesztő a fő vezérlők alatt jelenik meg.

* Kattints a gradienssávra egy színmegálló hozzáadásához.
* Bal kattintással jelölj ki egy megállót, majd húzd oldalra az áthelyezéséhez.
* Egy kijelölt megálló eltávolításához húzd lefelé, el a sávtól, vagy nyomd meg a Delete/Backspace billentyűt. Egy gradiens mindig legalább két megállót megtart.
* Jobb kattintással szerkesztheted a megállót a színválasztóval.
* A kijelölt megálló pontos szerkesztéséhez használd a **Position**, **Hue**, **Saturation** és **Brightness** vezérlőket.
* Az **interpolation** határozza meg, hogyan keveredjenek a színek a megállók között:
* **HSB** - a hue, saturation és brightness értékeket keveri. Ez a legjobb a színkörön körbefutó, sima szivárványszerű mozgáshoz.
* **RGB** - közvetlenül a vörös, zöld és kék értékeket keveri. Ez gyakran inkább képernyős vagy világítási pultos színátmenet érzetét kelti.
* **NONE** - keverés nélkül ugrik egyik megállóról a következőre.
* A **hue direction** HSB interpolációnál érhető el:
* **AUTO** - a legrövidebb útvonalat választja a hue színkörön.
* **FORWARDS** - mindig előre halad a hue értékeken keresztül.
* **BACKWARDS** - mindig visszafelé halad a hue értékeken keresztül.
