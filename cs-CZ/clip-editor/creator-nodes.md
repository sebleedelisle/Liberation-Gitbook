---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Vytvoří jeden bod / paprsek.

* **Render profile** – viz [Render profile](fundamentals/render-profile.md)
* **Colour** – barva bodu. Viz [Nastavení barev a HSB](fundamentals/colour-settings-and-hsb.md)
* pozice **x** a **y** – viz [Souřadnicový systém](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Vytvoří čáru / plochý paprsek.

* **Render profile** – viz [Render profile](fundamentals/render-profile.md)
* **Size** – délka čáry
* **Colour** – barva čáry. Viz [Nastavení barev a HSB](fundamentals/colour-settings-and-hsb.md)
* pozice **x** a **y** – viz [Souřadnicový systém](fundamentals/co-ordinate-system.md)
* **rotation** – úhel čáry ve stupních
* **resolution** – viz [Rozlišení](fundamentals/resolution.md)
* **alignment** – _LEFT / CENTRE / RIGHT –_ určuje počáteční bod a střed otáčení čáry
* _MOVE TO FRONT / MOVE TO BACK_ – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Vytvoří kružnici / kužel.

* **Render profile** – viz [Render profile](fundamentals/render-profile.md)
* **radius** – poloměr kružnice
* **Colour** – barva kružnice. Viz [Nastavení barev a HSB](fundamentals/colour-settings-and-hsb.md)
* pozice **x** a **y** – viz [Souřadnicový systém](fundamentals/co-ordinate-system.md)
* **resolution** – viz [Rozlišení](fundamentals/resolution.md)
* **Fill state** – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Vytvoří pravidelný mnohoúhelník, například trojúhelník, čtverec nebo pětiúhelník.

* **Render profile** – viz [Render profile](fundamentals/render-profile.md)
* **size** – vzdálenost od středu ke každému rohu
* **Colour** – barva mnohoúhelníku. Viz [Nastavení barev a HSB](fundamentals/colour-settings-and-hsb.md)
* pozice **x** a **y** – viz [Souřadnicový systém](fundamentals/co-ordinate-system.md)
* **rotation** – úhel natočení tvaru ve stupních
* **resolution** – viz [Rozlišení](fundamentals/resolution.md)
* **Fill state** – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Načte soubor SVG pro vlastní tvary.

{% hint style="warning" %}
Liberation je kompatibilní s formátem _SVGTiny_. Doporučujeme InkScape, ale většina aplikací pro vektorovou grafiku umí do tohoto formátu exportovat. Před exportem nezapomeňte převést veškerý text na tvary. Liberation vykreslí tahy a volitelně může použít výplně jako masks. Zkontrolujte, že čáry nejsou černé, jinak se bez modifikátoru barvy nezobrazí!
{% endhint %}

* **Import SVG** – načte soubor SVG z disku.

{% hint style="info" %}
Po načtení SVG se obsah převede a uloží jako součást Clip, takže nemusíte udržovat odkaz na původní soubor, pokud později nechcete měnit nastavení masks.
{% endhint %}

* **Use fills as masks** – zpracuje každý vyplněný tvar jako mask, tj. jako tvar vyplněný černou. Tato volba se nastaví automaticky, pokud SVG obsahuje jakékoli vyplněné tvary. Pokud žádné vyplněné tvary neobsahuje, bude vypnutá. Viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** – pokud tvary v SVG nemají obrys, nemůžeme je vykreslit! Tato volba přidá obrys (neboli _stroke_) ke každému vyplněnému tvaru. Pokud SVG neobsahuje žádné tvary s tahem, nastaví se automaticky. Pokud neobsahuje žádné vyplněné tvary, bude vypnutá.
* **Invert black lines** – pokud jsou všechny čáry v SVG černé, neuvidíte je! Tato volba je změní na bílé. Nastaví se automaticky, pokud SVG obsahuje pouze černé tvary, ale pokud žádné takové nemáte, bude vypnutá.
* **Render profile** – viz [Render profile](fundamentals/render-profile.md)
* **scale** – upravuje velikost SVG. Vypočítá se automaticky při načtení SVG (aby byl obraz viditelný), ale později ji můžete ručně změnit.
* pozice **x** a **y** – viz [Souřadnicový systém](fundamentals/co-ordinate-system.md)
* **rotation** – úhel natočení obrazu ve stupních
* **resolution** – viz [Rozlišení](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Vytvoří animaci ze sekvence souborů SVG.

* **Import SVG Sequence** – vyberte složku, která obsahuje všechny soubory SVG. Upozornění: načítají se v alfanumerickém pořadí.

{% hint style="info" %}
Po načtení sekvence SVG se obsah převede a uloží jako součást Clip, takže nemusíte udržovat odkazy na původní soubory, pokud později nechcete měnit nastavení masks.
{% endhint %}

* **Use fills as masks** – zpracuje každý vyplněný tvar jako mask, tj. jako tvar vyplněný černou. Tato volba se nastaví automaticky, pokud některé z vašich SVG obsahuje vyplněné tvary. Pokud žádné vyplněné tvary neobsahují, bude vypnutá. Viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** – pokud tvary ve vašich SVG nemají obrys, nemůžeme je vykreslit! Tato volba přidá obrys (neboli _stroke_) ke každému vyplněnému tvaru. Pokud SVG neobsahují žádné tvary s tahem, nastaví se automaticky. Pokud neobsahují žádné vyplněné tvary, bude vypnutá.
* **Invert black lines** – pokud jsou všechny čáry ve vašich SVG černé, neuvidíte je! Tato volba je změní na bílé. Nastaví se automaticky, pokud SVG obsahují pouze černé tvary, ale pokud žádné takové nemáte, bude vypnutá.
* **Render profile** – viz [Render profile](fundamentals/render-profile.md)
* **scale** – upravuje velikost obrazu.
* pozice **x** a **y** – viz [Souřadnicový systém](fundamentals/co-ordinate-system.md)
* **rotation** – úhel natočení obrazu ve stupních
* **resolution** – viz [Rozlišení](fundamentals/resolution.md)
* **speed** – délka celé animace v taktech.
* **time per frame** – pokud je tato volba nastavená, délka se počítá pro každý snímek, ne pro celou animaci. Když je tedy _speed_ nastaveno na ¼, každý snímek bude trvat 1 dobu.
* **animation direction** –
  * _FORWARDS_ – animace běží dopředu a potom se ve smyčce vrátí na začátek
  * _BACKWARDS_ – animace běží dozadu a potom se ve smyčce vrátí na konec
  * _PINGPONG_ – animace běží ve smyčce dopředu a potom dozadu
  * _MANUAL_ – aktuální snímek se nastavuje pomocí nastavení _position manual_
* **position manual** – nastavuje aktuální snímek; 0 % je první snímek, 100 % je poslední snímek. Lze ho nastavit ručně nebo pomocí externího oscilátoru.
* _MOVE TO FRONT / MOVE TO BACK_ – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Vytvoří text pomocí písma TrueType nebo OpenType.

* **Text** – sem napište požadovaný text
* **Font** – vyberte požadované písmo

{% hint style="info" %}
Chcete-li do Liberation přidat další písma, zkopírujte soubory .ttf nebo .otf do složky data/resources/fonts.
{% endhint %}

* **Render profile** – viz [Render profile](fundamentals/render-profile.md)
* **horizontal alignment** – vyberte _LEFT_, _CENTRE_ nebo _RIGHT_ a nastavte zarovnání textu.
* **Fill state** – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)
* **size** – velikost textu
* **colour -** viz [Nastavení barev a HSB](fundamentals/colour-settings-and-hsb.md)
* pozice **x** a **y** – viz [Souřadnicový systém](fundamentals/co-ordinate-system.md)
* **rotation** – úhel natočení obrazu ve stupních
* **resolution** – viz [Rozlišení](fundamentals/resolution.md)
* **reveal** – použijte pro postupné odhalování textu po jednotlivých znacích. Když je hodnota mezi 0 a 50 %, text se bude postupně objevovat zleva doprava. Když je mezi 50 % a 100 %, text bude zleva doprava mizet. Pro vytvoření animace můžete k tomuto vstupu připojit oscilátor.
* **reveal by word** – když je tato volba zapnutá, _reveal_ bude pracovat po jednotlivých slovech, ne po znacích.
* **countdown** – systém odpočtu (implementovaný narychlo!). Mění se každé 2 doby, takže pokud chcete sekundy, nastavte tempo na 120 bpm.
* **countdown start** – číslo, od kterého má odpočet začít
* _MOVE TO FRONT / MOVE TO BACK_ – viz [Výplně, masks a řazení podle hloubky](fundamentals/fills-masks-and-depth-sorting.md)
