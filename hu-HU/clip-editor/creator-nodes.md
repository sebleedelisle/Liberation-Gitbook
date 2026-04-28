---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator node-ok

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Egyetlen pontot / sugarat hoz létre.

* **Render profile** - lásd: [render-profile.md](fundamentals/render-profile.md)
* **Colour** - a pont színe. Lásd: [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** és **y** pozíció - lásd: [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Vonalat / síkot hoz létre.

* **Render profile** - lásd: [render-profile.md](fundamentals/render-profile.md)
* **Size** - a vonal hossza
* **Colour** - a vonal színe. Lásd: [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** és **y** pozíció - lásd: [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - a vonal szöge fokban
* **resolution** - lásd: [resolution.md](fundamentals/resolution.md)
* **alignment** - _LEFT / CENTRE / RIGHT -_ meghatározza a vonal kezdőpontját és forgásközéppontját
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Kört / kúpot hoz létre.

* **Render profile** - lásd: [render-profile.md](fundamentals/render-profile.md)
* **radius** - a kör sugara
* **Colour** - a kör színe. Lásd: [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** és **y** pozíció - lásd: [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **resolution** - lásd: [resolution.md](fundamentals/resolution.md)
* **Fill state** - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Szabályos sokszöget hoz létre: háromszöget, négyzetet, ötszöget stb.

* **Render profile** - lásd: [render-profile.md](fundamentals/render-profile.md)
* **size** - a középpont és az egyes csúcsok közötti távolság
* **Colour** - a sokszög színe. Lásd: [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** és **y** pozíció - lásd: [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - az alakzat elforgatási szöge fokban
* **resolution** - lásd: [resolution.md](fundamentals/resolution.md)
* **Fill state** - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Egy SVG-fájlt tölt be egyéni alakzatokhoz.

{% hint style="warning" %}
A Liberation az _SVGTiny_ formátummal kompatibilis. Az InkScape használata ajánlott, de a legtöbb vektorgrafikus alkalmazás tud ebben a formátumban exportálni. Exportálás előtt minden szöveget alakzattá kell konvertálni. A Liberation kirajzolja a körvonalakat, és opcionálisan maszkként használhatja a kitöltéseket. Ügyelj arra, hogy a vonalak ne legyenek feketék, különben színmódosító nélkül nem fognak megjelenni!
{% endhint %}

* **Import SVG** - SVG-fájl betöltése lemezről.

{% hint style="info" %}
Miután betöltötted az SVG-t, a tartalom konvertálásra kerül és a clipen belül mentődik, ezért nem kell megtartanod a hivatkozást a fájlra, kivéve, ha később módosítani szeretnéd a maszkbeállításokat.
{% endhint %}

* **Use fills as masks** - minden kitöltött alakzatot maszkként dolgoz fel, azaz feketével kitöltve. Ez automatikusan be lesz kapcsolva, ha az SVG-ben vannak kitöltött alakzatok. Ha nincsenek benne kitöltött alakzatok, ki lesz kapcsolva. Lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - ha az SVG-ben lévő alakzatoknak nincs körvonala, akkor nem tudjuk kirajzolni őket! Ez az opció körvonalat (vagy _stroke_-ot) ad minden kitöltött alakzathoz. Ha az SVG-ben nincsenek körvonallal rendelkező alakzatok, automatikusan be lesz kapcsolva. Ha nincsenek benne kitöltött alakzatok, ki lesz kapcsolva.
* **Invert black lines** - ha az SVG-ben minden vonal fekete, akkor nem fogod látni őket! Ez az opció fehérre állítja őket. Automatikusan be lesz kapcsolva, ha az SVG-ben csak fekete alakzatok vannak, de ki lesz kapcsolva, ha nincsenek ilyenek.
* **Render profile** - lásd: [render-profile.md](fundamentals/render-profile.md)
* **scale** - az SVG méretét állítja. Ez az SVG betöltésekor automatikusan kiszámításra kerül (hogy a kép biztosan látható legyen), de később manuálisan módosítható.
* **x** és **y** pozíció - lásd: [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - a kép elforgatási szöge fokban
* **resolution** - lásd: [resolution.md](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Animációt hoz létre SVG-fájlok sorozatából.

* **Import SVG Sequence** - válaszd ki azt a mappát, amelyben az összes SVG-fájl található. Fontos, hogy a fájlok alfanumerikus sorrendben töltődnek be.

{% hint style="info" %}
Miután betöltötted az SVG-sorozatot, a tartalom konvertálásra kerül és a clipen belül mentődik, ezért nem kell megtartanod a hivatkozást a fájlokra, kivéve, ha később módosítani szeretnéd a maszkbeállításokat.
{% endhint %}

* **Use fills as masks** - minden kitöltött alakzatot maszkként dolgoz fel, azaz feketével kitöltve. Ez automatikusan be lesz kapcsolva, ha bármelyik SVG-ben vannak kitöltött alakzatok. Ha egyikben sincsenek kitöltött alakzatok, ki lesz kapcsolva. Lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - ha az SVG-kben lévő alakzatoknak nincs körvonala, akkor nem tudjuk kirajzolni őket! Ez az opció körvonalat (vagy _stroke_-ot) ad minden kitöltött alakzathoz. Ha az SVG-kben nincsenek körvonallal rendelkező alakzatok, automatikusan be lesz kapcsolva. Ha egyikben sincsenek kitöltött alakzatok, ki lesz kapcsolva.
* **Invert black lines** - ha az SVG-kben minden vonal fekete, akkor nem fogod látni őket! Ez az opció fehérre állítja őket. Automatikusan be lesz kapcsolva, ha az SVG-kben csak fekete alakzatok vannak, de ki lesz kapcsolva, ha nincsenek ilyenek.
* **Render profile** - lásd: [render-profile.md](fundamentals/render-profile.md)
* **scale** - a kép méretét állítja.
* **x** és **y** pozíció - lásd: [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - a kép elforgatási szöge fokban
* **resolution** - lásd: [resolution.md](fundamentals/resolution.md)
* **speed** - a teljes animáció időtartama ütemekben.
* **time per frame** - ha ez be van állítva, akkor az időtartam képkockánként értendő, nem az animáció teljes hosszára. Tehát ha a _speed_ értéke ¼, akkor minden képkocka 1 beat hosszú lesz.
* **animation direction** -
  * _FORWARDS_ - az animáció előre fut, majd visszaugrik az elejére
  * _BACKWARDS_ - az animáció visszafelé fut, majd visszaugrik a végére
  * _PINGPONG_ - az animáció előre, majd visszafelé fut ciklusban
  * _MANUAL_ - az aktuális képkockát a _position manual_ beállítás határozza meg
* **position manual** - beállítja az aktuális képkockát; 0% az első képkocka, 100% az utolsó képkocka. Beállítható manuálisan vagy külső oszcillátorral.
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Szöveget hoz létre TrueType vagy OpenType betűtípussal.

* **Text** - ide írd be a kívánt szöveget
* **Font** - válaszd ki a kívánt betűtípust

{% hint style="info" %}
Ha további betűtípusokat szeretnél hozzáadni a Liberationhöz, másold a .ttf vagy .otf fájlokat a data/resources/fonts mappába.
{% endhint %}

* **Render profile** - lásd: [render-profile.md](fundamentals/render-profile.md)
* **horizontal alignment** - válaszd a _LEFT_, _CENTRE_ vagy _RIGHT_ lehetőséget a szöveg igazításának megadásához.
* **Fill state** - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* **size** - a szöveg mérete
* **colour -** lásd: [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** és **y** pozíció - lásd: [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - a kép elforgatási szöge fokban
* **resolution** - lásd: [resolution.md](fundamentals/resolution.md)
* **reveal** - ezzel fokozatosan, karakterenként jelenítheted meg a szöveget. 0 és 50% között a szöveg fokozatosan jelenik meg balról jobbra. 50% és 100% között a szöveg balról jobbra tűnik el. Animációk készítéséhez oszcillátort csatlakoztathatsz ehhez a sockethez.
* **reveal by word** - ha be van kapcsolva, a _reveal_ szavanként működik, nem karakterenként.
* **countdown** - egy (sietve megvalósított!) visszaszámláló rendszer. 2 ütemenként változik, ezért ha másodperceket szeretnél, ügyelj arra, hogy 120 bpm legyen beállítva.
* **countdown start** - az a szám, amelyről a visszaszámlálás induljon
* _MOVE TO FRONT / MOVE TO BACK_ - lásd: [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
