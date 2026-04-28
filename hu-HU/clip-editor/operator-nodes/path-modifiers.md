---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

Ez a node a vonalakat és alakzatokat egyenletesen elosztott pontokra cseréli (a meglévő pontok változatlanok maradnak).

* **Colour** – a pontok színe. A rendszer figyelmen kívül hagyja, ha az _Inherit Colour_ be van kapcsolva, lásd lent. _Lásd még_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – a pontok közötti távolság, pixelben mérve. Kisebb érték = több pont, nagyobb érték = kevesebb pont.
* **Offset** – a pontok kezdőpozícióját tolja el a térköz százalékában. Animálható (például fűrészfog Oscillator Node-dal), így „vándorló” pont effektusok hozhatók létre.
* **Keep Original** – ha be van kapcsolva, az eredeti vonalak/alakzatok megmaradnak, és a pontok ezek fölé rajzolódnak.
* **Render Profile** – a renderelési minőséget választja ki. _Lásd_ [render-profile.md](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – automatikusan úgy igazítja a térközt, hogy az útvonal hossza egyenletesen osztható legyen vele.
* **Fade Out Ends** – fokozatosan csökkenti a pontok fényerejét az útvonal eleje és vége felé. Hasznos, ha az **Offset** értékét fűrészfog Oscillator Node-dal animálod, mert így a pontok simán halványodnak be és ki, amikor az alakzat végéhez érnek.

## &#x20;Trimmer

Ez a node levágja a vonalak és alakzatok látható hosszát, így időben felfedheted, elrejtheted vagy animálhatod őket.

* **Offset** – azt szabályozza, hol kezdődjön az alakzat látható része. Ha a _Trim Size_ 0%, az Offset 0% → 100% közötti animálása akkor is berajzoltatja az alakzatot, 50%-nál teljesen láthatóvá teszi, majd újra eltünteti.
* **Trim Size** – megadja, hogy az alakzat teljes hosszának hány százaléka maradjon meg.
* **Loop** – az alakzatot folyamatos hurokként kezeli, így a vége eltűnés helyett visszakapcsolódik az elejéhez.
* **All Shapes** – az összes bemeneti alakzatot egyesíti, és úgy vágja őket, mintha egyetlen útvonalat alkotnának. Ha ki van kapcsolva, minden alakzat külön-külön lesz levágva.
* **Add Dot at Start / Add Dot at End** – a választott színű pontot ad hozzá a vágási pontokhoz. (Ha nincs alkalmazva vágás, nem kerülnek hozzáadásra pontok.)
* **Colour** – a vágási pontok színe. _Lásd még_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – kiválasztja a pontok renderelési profilját. _Lásd_ [render-profile.md](../fundamentals/render-profile.md)
