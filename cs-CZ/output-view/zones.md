---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

Hlavní typ zone, který budete používat ve většině projektů, je _Beam zone_. Je určená pro atmosférické paprskové efekty ve vzduchu. Druhým typem je _Canvas zone_ (viz [Grafika a systém Canvas](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**VAROVÁNÍ – Při přesouvání zones za běhu laseru buďte mimořádně opatrní** a stáhněte jas na co nejnižší hodnotu. Podrobný návod, jak lasery bezpečně aktivovat a nastavit jejich zones, najdete v části [Nastavení laserů](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

Zones můžete myší uchopit a přetáhnout. Zapněte test pattern, abyste viděli, kam daná zone směřuje.

{% hint style="info" %}
Pomocí kláves se šipkami můžete aktuálně vybranou zone nebo bod jemně **posouvat**. Podržením klávesy `Shift` posouváte ve větších krocích.
{% endhint %}

{% hint style="info" %}
Tip: nastavení zone můžete rychle zkopírovat mezi více lasery. Viz [Kopírování nastavení laseru](../setting-up/copy-laser-settings.md "mention").
{% endhint %}

### Přidání nové Beam zone

Klikněte na tlačítko _Add a new beam zone_ v horní části panelu nástrojů a objeví se nová zone. Beam zones jsou seřazené v pořadí, ve kterém je přidáte, ale jejich pořadí můžete změnit. Viz [Změna pořadí Beam zones](re-ordering-beam-zones.md "mention").

### Přidání existující Canvas zone

Klikněte na tlačítko _Add existing canvas zone_. Zobrazí se seznam dostupných Canvas zones a pro tento laser je můžete zapínat a vypínat. Viz [Grafika a systém Canvas](../graphics-and-the-canvas-system/ "mention").

### Typy tvarů pro zone

K dispozici jsou 3 typy tvaru zone:

* **Quad** – výchozí obdélníkový tvar zone, který může být pravidelný (zarovnaný podle os) nebo deformovaný. Nejlépe se hodí pro větší obdélníkové zones nebo Canvas zones, které vyžadují korekci perspektivy.
* **Line/Curve** – zone definovaná 2 nebo více body a tloušťkou. Ideální pro úzké zones nebo pro ukončení paprsků na balkonech, mostech či jiných zakřivených tvarech.
* **Segmented** – zone, kterou lze rozdělit na menší čtyřúhelníky. Ideální pro architektonický mapping.

Kliknutím pravým tlačítkem na libovolnou zone otevřete její nastavení. V této nabídce po kliknutí pravým tlačítkem můžete:

* Přejmenovat zone (to se hodí pro její identifikaci v Clip Deck, zejména pokud máte hodně zones)
* Povolit nebo zakázat zone
* Zamknout její pozici
* Změnit typ jejího tvaru
* Vrátit ji do výchozí pozice
* Otevřít nastavení specifická pro daný typ tvaru
* Smazat ji
* Přidat _Alt Zone_ (viz [Systém Alt Zone](alt-zone-system.md "mention"))

{% hint style="danger" %}
**VAROVÁNÍ –** při změně typu zone v době, kdy je laser aktivní, buďte velmi opatrní. Zone se vrátí na poslední pozici a velikost pro daný tvar, takže se výstup může náhle změnit. Před změnou typu zone je nejlepší laser vypnout.
{% endhint %}

### Tvar zone: Quad

Každý roh tvaru Quad můžete posouvat myší. Kliknutím na roh se stisknutou klávesou `Alt / Option` ho přesunete nezávisle na ostatních a Quad deformujete. Jakmile je Quad deformovaný, všechny rohy lze volně posouvat.

Deformaci můžete odstranit a vrátit tvar na obdélník zarovnaný podle os pomocí tlačítka _REMOVE DISTORTION_ v nabídce po kliknutí pravým tlačítkem.

#### Korekce perspektivy

Tuto volbu nastavíte přepínačem v nabídce po kliknutí pravým tlačítkem a určuje metodu deformace. Pro paprsky je nejlepší nechat ji vypnutou. Pokud ale tato zone promítá grafiku na rovnou plochu, zapněte ji a výstup bude perspektivně korigovaný.

{% hint style="info" %}
Pokud je _Perspective correction_ vypnutá, obsah se deformuje pomocí _bilineární interpolace_. Jinými slovy, obsah je v rámci Quad rozložen rovnoměrně. Proto se tato metoda nejlépe hodí pro paprsky.

Když je korekce perspektivy zapnutá, obsah se deformuje pomocí perspektivního zkreslení, které vyrovnává perspektivní zkrácení. Pokud tedy promítáte grafiku na stěnu pod šikmým úhlem, můžete tím výstup narovnat a opravit zkreslení projekce.
{% endhint %}

### Tvar zone: Line / Curve

Tvar Line / Curve se v posledních show stal mojí nejpoužívanější volbou a dalo by se říct, že by měl být výchozí pro Beam zones.

Moje zones musí být velmi často úzké, aby se vešly do problematických úzkých prostor v místech konání nebo mezi okna na budovách. Zjistil jsem, že nastavovat čtyři rohy Quad, když jsou tak blízko u sebe, může být dost piplačka. A tak vznikl tvar Line / Curve!

Pro rovné čáry stačí dva body a pak už jen upravíte _Zone thickness_ v nabídce po kliknutí pravým tlačítkem. Je to nejrychlejší způsob, jak vytvořit jednoduché zones.

Kliknutím na čáru se stisknutou klávesou `Alt / Option` vytvoříte další body. Tyto body se automaticky vyhlazují, aby vznikl plynulý tvar, a případné zlomy můžete doladit pomocí _Smooth level_.

Kliknutím na bod se stisknutou klávesou `Alt / Option` ho smažete.

Pokud máte zkušenosti s aplikacemi pro vektorovou grafiku (Inkscape, Illustrator atd.), můžete použít volbu _Manually adjust bezier curves_ a získat jemnou kontrolu nad všemi řídicími body.

### Tvar zone: Segmented

Tato rozdělená zone umožňuje provádět velmi detailní korekce a hodí se při mappingu na složité tvary. Rozdělení můžete přidávat nebo odebírat pomocí tlačítek + a - v nabídce po kliknutí pravým tlačítkem.

### Jak upravit zone, která je celá překrytá jinou zone

Klikněte pravým tlačítkem na horní zone a kliknutím na tlačítko se zámkem ji zamkněte. Potom by mělo být možné upravovat a nastavovat zone pod ní.

<br>

{% hint style="info" %}
Jakmile do výstupu přidáte Beam zone, bude dostupná pro přidání do Clip v Clip Deck.
{% endhint %}
