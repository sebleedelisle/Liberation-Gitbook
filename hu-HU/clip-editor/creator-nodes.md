---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator node-ok

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Egyetlen pontot / sugarat hoz létre.

* **Render profile** - lásd: [Render profile](fundamentals/render-profile.md "mention")
* **Colour** - a pont színe. Lásd: [Színbeállítások és HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** és **y** pozíció - lásd: [Koordináta-rendszer](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Vonalat / síkot hoz létre.

* **Render profile** - lásd: [Render profile](fundamentals/render-profile.md "mention")
* **Size** - a vonal hossza
* **Colour** - a vonal színe. Lásd: [Színbeállítások és HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** és **y** pozíció - lásd: [Koordináta-rendszer](fundamentals/co-ordinate-system.md "mention")
* **rotation** - a vonal szöge fokban
* **resolution** - lásd: [Felbontás](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ meghatározza a vonal kezdőpontját és forgásközéppontját
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Kört / kúpot hoz létre.

* **Render profile** - lásd: [Render profile](fundamentals/render-profile.md "mention")
* **radius** - a kör sugara
* **Colour** - a kör színe. Lásd: [Színbeállítások és HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** és **y** pozíció - lásd: [Koordináta-rendszer](fundamentals/co-ordinate-system.md "mention")
* **resolution** - lásd: [Felbontás](fundamentals/resolution.md "mention")
* **Fill state** - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Szabályos sokszöget hoz létre: háromszöget, négyzetet, ötszöget stb.

* **Render profile** - lásd: [Render profile](fundamentals/render-profile.md "mention")
* **size** - a középpont és az egyes csúcsok közötti távolság
* **Colour** - a sokszög színe. Lásd: [Színbeállítások és HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** és **y** pozíció - lásd: [Koordináta-rendszer](fundamentals/co-ordinate-system.md "mention")
* **rotation** - az alakzat elforgatási szöge fokban
* **resolution** - lásd: [Felbontás](fundamentals/resolution.md "mention")
* **Fill state** - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Egy SVG-fájlt tölt be egyéni alakzatokhoz.

{% hint style="warning" %}
A Liberation az _SVGTiny_ formátummal kompatibilis. Az InkScape használata ajánlott, de a legtöbb vektorgrafikus alkalmazás tud ebben a formátumban exportálni. Exportálás előtt minden szöveget alakzattá kell konvertálni. A Liberation kirajzolja a körvonalakat, és opcionálisan maszkként használhatja a kitöltéseket. Ügyelj arra, hogy a vonalak ne legyenek feketék, különben színmódosító nélkül nem fognak megjelenni!
{% endhint %}

* **Import SVG** - SVG-fájl betöltése lemezről.

{% hint style="info" %}
Miután betöltötted az SVG-t, a tartalom konvertálásra kerül és a clipen belül mentődik, ezért nem kell megtartanod a hivatkozást a fájlra, kivéve, ha később módosítani szeretnéd a maszkbeállításokat.
{% endhint %}

* **Use fills as masks** - minden kitöltött alakzatot maszkként dolgoz fel, azaz feketével kitöltve. Ez automatikusan be lesz kapcsolva, ha az SVG-ben vannak kitöltött alakzatok. Ha nincsenek benne kitöltött alakzatok, ki lesz kapcsolva. Lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - ha az SVG-ben lévő alakzatoknak nincs körvonala, akkor nem tudjuk kirajzolni őket! Ez az opció körvonalat (vagy _stroke_-ot) ad minden kitöltött alakzathoz. Ha az SVG-ben nincsenek körvonallal rendelkező alakzatok, automatikusan be lesz kapcsolva. Ha nincsenek benne kitöltött alakzatok, ki lesz kapcsolva.
* **Invert black lines** - ha az SVG-ben minden vonal fekete, akkor nem fogod látni őket! Ez az opció fehérre állítja őket. Automatikusan be lesz kapcsolva, ha az SVG-ben csak fekete alakzatok vannak, de ki lesz kapcsolva, ha nincsenek ilyenek.
* **Render profile** - lásd: [Render profile](fundamentals/render-profile.md "mention")
* **scale** - az SVG méretét állítja. Ez az SVG betöltésekor automatikusan kiszámításra kerül (hogy a kép biztosan látható legyen), de később manuálisan módosítható.
* **x** és **y** pozíció - lásd: [Koordináta-rendszer](fundamentals/co-ordinate-system.md "mention")
* **rotation** - a kép elforgatási szöge fokban
* **resolution** - lásd: [Felbontás](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Animációt hoz létre SVG-fájlok sorozatából.

* **Import SVG Sequence** - válaszd ki azt a mappát, amelyben az összes SVG-fájl található. Fontos, hogy a fájlok alfanumerikus sorrendben töltődnek be.

{% hint style="info" %}
Miután betöltötted az SVG-sorozatot, a tartalom konvertálásra kerül és a clipen belül mentődik, ezért nem kell megtartanod a hivatkozást a fájlokra, kivéve, ha később módosítani szeretnéd a maszkbeállításokat.
{% endhint %}

* **Use fills as masks** - minden kitöltött alakzatot maszkként dolgoz fel, azaz feketével kitöltve. Ez automatikusan be lesz kapcsolva, ha bármelyik SVG-ben vannak kitöltött alakzatok. Ha egyikben sincsenek kitöltött alakzatok, ki lesz kapcsolva. Lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - ha az SVG-kben lévő alakzatoknak nincs körvonala, akkor nem tudjuk kirajzolni őket! Ez az opció körvonalat (vagy _stroke_-ot) ad minden kitöltött alakzathoz. Ha az SVG-kben nincsenek körvonallal rendelkező alakzatok, automatikusan be lesz kapcsolva. Ha egyikben sincsenek kitöltött alakzatok, ki lesz kapcsolva.
* **Invert black lines** - ha az SVG-kben minden vonal fekete, akkor nem fogod látni őket! Ez az opció fehérre állítja őket. Automatikusan be lesz kapcsolva, ha az SVG-kben csak fekete alakzatok vannak, de ki lesz kapcsolva, ha nincsenek ilyenek.
* **Render profile** - lásd: [Render profile](fundamentals/render-profile.md "mention")
* **scale** - a kép méretét állítja.
* **x** és **y** pozíció - lásd: [Koordináta-rendszer](fundamentals/co-ordinate-system.md "mention")
* **rotation** - a kép elforgatási szöge fokban
* **resolution** - lásd: [Felbontás](fundamentals/resolution.md "mention")
* **speed** - a teljes animáció időtartama ütemekben.
* **time per frame** - ha ez be van állítva, akkor az időtartam képkockánként értendő, nem az animáció teljes hosszára. Tehát ha a _speed_ értéke ¼, akkor minden képkocka 1 beat hosszú lesz.
* **animation direction** -
  * _FORWARDS_ - az animáció előre fut, majd visszaugrik az elejére
  * _BACKWARDS_ - az animáció visszafelé fut, majd visszaugrik a végére
  * _PINGPONG_ - az animáció előre, majd visszafelé fut ciklusban
  * _MANUAL_ - az aktuális képkockát a _position manual_ beállítás határozza meg
* **position manual** - beállítja az aktuális képkockát; 0% az első képkocka, 100% az utolsó képkocka. Beállítható manuálisan vagy külső oszcillátorral.
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Szöveget hoz létre TrueType vagy OpenType betűtípussal.

* **Text** - ide írd be a kívánt szöveget
* **Font** - válaszd ki a kívánt betűtípust

{% hint style="info" %}
Ha további betűtípusokat szeretnél hozzáadni a Liberationhöz, másold a .ttf vagy .otf fájlokat a Liberation munkamappáján belüli `data/fonts` mappába, majd indítsd újra a Liberationt.
{% endhint %}

* **Render profile** - lásd: [Render profile](fundamentals/render-profile.md "mention")
* **horizontal alignment** - válaszd a _LEFT_, _CENTRE_ vagy _RIGHT_ lehetőséget a szöveg igazításának megadásához.
* **Fill state** - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - a szöveg mérete
* **monospace** - minden karaktert azonos szélességgel rajzol. Ez időzítőknél és számlálóknál hasznos, mert a szöveg nem ugrál oldalirányban, amikor a számok változnak.
* **character spacing** - a karakterek közötti távolságot állítja. Növeld, ha nagyobb betűközt szeretnél, vagy csökkentsd, ha szorosabb szöveget szeretnél.
* **colour -** lásd: [Színbeállítások és HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** és **y** pozíció - lásd: [Koordináta-rendszer](fundamentals/co-ordinate-system.md "mention")
* **rotation** - a kép elforgatási szöge fokban
* **resolution** - lásd: [Felbontás](fundamentals/resolution.md "mention")
* **reveal** - ezzel fokozatosan, karakterenként jelenítheted meg a szöveget. 0 és 50% között a szöveg fokozatosan jelenik meg balról jobbra. 50% és 100% között a szöveg balról jobbra tűnik el. Animációk készítéséhez oszcillátort csatlakoztathatsz ehhez a sockethez.
* **reveal by word** - ha be van kapcsolva, a _reveal_ szavanként működik, nem karakterenként.
* **countdown** - a beírt szöveget visszaszámlálásra cseréli. Amikor a visszaszámlálás eléri a nullát, a normál **Text** érték jelenik meg.
* **use seconds** - valós másodpercekben számol. Ha ez ki van kapcsolva, a visszaszámlálás ütemalapú: két ütem számít egy másodpercnek, így 120 bpm-nél egyezik a valós másodpercekkel.
* **show minutes/seconds** - percben és másodpercben mutatja a hátralévő időt. Ha több mint egy óra, az órákat is megjeleníti.
* **countdown to date/time** - számról indított visszaszámlálás helyett egy megadott UTC dátumig és időpontig számol vissza.
* **countdown datetime** - beállítja az UTC cél dátumot/időpontot, amikor a **countdown to date/time** be van kapcsolva.
* **start number** - a kezdő szám, amikor a **countdown to date/time** ki van kapcsolva.
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [Kitöltések, maszkok és mélységi rendezés](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Ha a betűtípus legördülő menü nyitva van, a fel és le nyílbillentyűkkel lépkedhetsz az elérhető betűtípusok között.
{% endhint %}
