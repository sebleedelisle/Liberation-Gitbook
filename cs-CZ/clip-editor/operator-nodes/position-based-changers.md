---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Změny podle pozice

Tato skupina nodes upravuje obsah podle pozice. Ve výchozím nastavení se efekt aplikuje podél vodorovné osy zleva doprava, ale osu můžete natočit na libovolný úhel. Každý node obsahuje také režim _radial_, ve kterém je efekt řízen úhlem každého bodu vůči středu.

* **Colour Changer by Position** – posouvá barvy podél zvolené osy nebo kolem radiálního úhlu.\
  \&#xNAN;_Příklad: Vytvořte duhový gradient, který přechází přes čáru, nebo použijte režim radial na kruhu a vytvořte efekt barevného kola._
* **Wave Shift by Position** – aplikuje sinusové zkreslení a posouvá obsah svisle, případně kolmo ke zvolené ose.\
  \&#xNAN;_Příklad: Rozvlňte čáru jako vodní hladinu, nebo použijte režim radial a nechte kruh pulzovat směrem od středu._
* **Noise Shift by Position** – aplikuje zkreslení pomocí simplex noise a posouvá obsah svisle, případně kolmo ke zvolené ose.\
  \&#xNAN;_Příklad: viz příklad u Wave Shift, ale s organičtějším a náhodnějším charakterem, ideální pro přidání přirozené variability._

## &#x20;Změna barvy podle pozice

Tento node aplikuje barevné změny na obsah podle pozice. Ve výchozím nastavení je osa vodorovná (0°), ale můžete ji natočit nebo přepnout do režimu radial.

* **wavelength** – nastavuje velikost opakujícího se barevného cyklu.
  * _Lineární režim:_ při 100 % jeden celý cyklus pokryje celou šířku obsahu.
  * _Režim radial:_ při 100 % jeden celý cyklus pokryje celý kruh (360°). Hodnoty jsou procenta kruhu: např. 50 % = půl kruhu (180°).
* **offset** – posouvá počáteční bod barevného cyklu jako procento hodnoty wavelength. Můžete jej modulovat, například pomocí sawtooth oscillatoru, a plynule tak procházet barvami.
* **repeat** – když je zapnuto, cyklus se přes obsah opakuje. Když je vypnuto, gradient se aplikuje pouze jednou: vše před začátkem má počáteční barvu, vše za koncem má koncovou barvu.
* **pingpong** – když je zapnuto, každý opakovaný cyklus střídá směr a vytváří zrcadlový efekt. Pokud je _Repeat_ vypnuto, gradient proběhne jednou tam a zpět. _Poznámka: v režimu Pingpong pokrývá wavelength jak dopředný, tak návratový průběh._
* **linear angle** – natáčí osu efektu. 0° = vodorovně.
* **radial** – přepne do režimu radial, ve kterém se barvy aplikují podle úhlu od středu.
* **radial smooth loop** – automaticky upraví wavelength tak, aby se rovnoměrně vešla do 100 % kruhu, a zabrání tak viditelnému švu v místě, kde se cyklus uzavírá.

**Režimy barev**

Určují, které části barevných úprav se na obsah aplikují. Viz také: [Nastavení barev a HSB](../fundamentals/colour-settings-and-hsb.md).

* **hue mode**
  * _OFF_ – odstín se nemění.
  * _FIXED_ – odstín je vynucen na pevnou hodnotu.
  * _SHIFTED_ – odstín je posunut o zadanou hodnotu (prvky s různými barvami zůstanou odlišné, ale společně se posunou po barevném kole).
* **saturation mode**
  * _OFF_ – sytost se nemění.
  * _FIXED_ – sytost se nastaví na zadanou hodnotu.
* **brightness mode**
  * _OFF_ – jas se nemění.
  * _FIXED_ – jas se nastaví na zadanou hodnotu.
  * _MULTIPLY_ – jas se násobí zadanou hodnotou. Tím se zachová dynamika (např. blikající prvky stále blikají, ale v omezeném rozsahu jasu).

**Počáteční a koncové hodnoty**

Tyto slidery určují barevný rozsah aplikovaný podél zvolené osy nebo radiálního průběhu.

* **start hue** – odstín na začátku gradientu.
* **end hue** – odstín na konci gradientu.
* **start saturation** – sytost na začátku.
* **end saturation** – sytost na konci.
* **start brightness** – jas na začátku.
* **end brightness** – jas na konci.
* **blend** – míchá barevnou změnu s původními barvami. Při 100 % efekt plně nahradí původní barvy.

**Příklad 1: Posuvný duhový gradient**

Výchozí nastavení:

1. Nechte node v režimu **Linear** (úhel 0° = vodorovně).
2. Nechte **wavelength** na 100 % (pokryje celou šířku a měla by to být výchozí hodnota).
3. Nechte počáteční a koncové hodnoty ve výchozím stavu.
4. Zapněte **repeat**.
5. Přidejte **Sawtooth Oscillator** k nastavení **offset**, který přechází od 0 % do 100 %.

***

**Příklad 2: Gradient černá–bílá–černá (Pingpong)**

Výchozí nastavení:

1. Nechte node v režimu **Linear** (úhel 0° = vodorovně).
2. Nechte **wavelength** na 100 % (pokryje celou šířku a měla by to být výchozí hodnota).
3. Vypněte **repeat**.
4. Nastavte **start brightness** na 0 (černá).
5. Nastavte **end brightness** na 100 (bílá).
6. Nastavte **start saturation** a **end saturation** na 0 (převede na stupně šedi).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Zapněte **pingpong**.

_Výsledek: gradient přechází přes šířku z černé do bílé a potom zpět do černé._\
Pokud chcete, aby si obsah zachoval svůj odstín a sytost, vypněte Saturation mode. \\

***

**Příklad 3: Rotující duhové kolo (Radial)**

1. Zapněte režim **radial**.
2. Nastavte **wavelength** na 100 % (celý průběh 360°).
3. Zapněte **repeat**.
4. Přidejte **Sawtooth Oscillator** k nastavení **offset**, který přechází od 0 % do 100 %.

_Výsledek: plynulé barevné kolo, které se nepřetržitě otáčí kolem kruhu._

## &#x20;Vlnový posun podle pozice

Tento node aplikuje na obsah vlnové zkreslení a posouvá body kolmo ke zvolené ose, případně radiálně od středu.

* **Wavelength** – nastavuje délku cyklu vlny.
  * _Lineární režim:_ při 100 % jeden celý cyklus pokryje celou šířku obsahu.
  * _Režim radial:_ při 100 % jeden celý cyklus pokryje plných 360°. (Hodnoty jsou procenta kruhu: 50 % = půl otáčky, 25 % = čtvrt otáčky atd.)
* **Size** – řídí amplitudu vlny, tedy jak daleko se obsah posune.
* **Offset** – posouvá vlnu podél osy, případně kolem kruhu v režimu radial. Jde o procento hodnoty wavelength, takže jej můžete animovat pomocí **Oscillator Node** a nechat vlnu cestovat.
* **Radial** – přepne z lineárního režimu do režimu radial, takže posun vychází z úhlu od středu.
* **Radial Smooth Loop** – upraví wavelength tak, aby se rovnoměrně vešla do 100 % kruhu, a zabrání viditelným švům v místě uzavření.
* **Triangle** – změní tvar vlny ze sinusového na trojúhelníkový.
* **Absolute** – použije absolutní hodnotu vlny, takže vznikají pouze posuny směrem nahoru (záporná strana se překlopí do kladné).
* **Angle** – natáčí osu vlny. 0° = vodorovně.

## &#x20;Šumový posun podle pozice

Tento node zkresluje obsah pomocí šumového pole podobného turbulenci a posouvá body kolmo ke zvolené ose, případně radiálně od středu. Ve srovnání s _Wave Shift_ je výsledek organičtější a náhodnější.

* **Detail** – určuje jemnost šumu. Vyšší hodnoty = ostřejší a detailnější variace. Nižší hodnoty = plynulejší variace.
* **Wavelength** – nastavuje měřítko šumového vzoru.
  * _Lineární režim:_ při 100 % jeden celý cyklus šumu pokryje šířku obsahu.
  * _Režim radial:_ při 100 % jeden celý cyklus pokryje plných 360°.
* **Size** – určuje velikost posunu, tedy amplitudu šumového zkreslení.
* **Offset** – posouvá šumový vzor podél osy nebo kolem kruhu. Jde o procento hodnoty wavelength, takže jej můžete animovat pomocí **Oscillator Node** a nechat šum „téct“.
* **Depth Offset** – posouvá se 3D šumovým polem a vytváří změny v čase. Je obzvlášť účinné při animaci pomocí Oscillator Node.
* **Depth Detail** – určuje detailnost změn v hloubkové dimenzi.
* **Absolute** – použije absolutní hodnotu šumu a překlopí záporné hodnoty do kladných, takže vzniká pouze jednostranný posun.
* **Radial** – přepne z lineárního režimu do režimu radial, takže posun vychází z úhlu od středu.
* **Radial Smooth Loop** – upraví wavelength tak, aby se rovnoměrně vešla do 100 % kruhu, a zabrání viditelným švům v režimu radial.
