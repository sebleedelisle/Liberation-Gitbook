---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Úvod do Clip Editor

Clip Editor je všestranný způsob, jak vytvářet laserový obsah, a tvoří jádro Liberation. Jednoduché věci v něm vytvoříte snadno, ale zároveň je dostatečně flexibilní i pro velmi propracované a komplexní efekty.

{% hint style="info" %}
Editor založený na nodes byl první částí Liberation, která vznikla. Zrodil se z rozhovoru s Robem Stanleym na setkání laserové komunity ve Velké Británii v roce 2018 o tom, jak by mohl vypadat „objektově orientovaný“ návrhář laserového obsahu.

I když působí jednoduše, jde o poměrně složitý systém. Na začátku roku 2019 jsem ale měl funkční demo, které koncept ověřilo – a tím začala celá tato cesta!
{% endhint %}

Jde o vizuální editor založený na nodes (nebo [architekturu grafu node](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)), který vám bude povědomý, pokud jste používali produkty jako TouchDesigner, MaxMSP nebo VVVV. Clip Editor je ale trochu jiný a o něco jednodušší, protože byl navržený speciálně pro vektorovou grafiku.

Clip Editor otevřete kliknutím pravým tlačítkem na tlačítko Clip a výběrem _EDIT CLIP_. Nebo klikněte pravým tlačítkem na prázdné tlačítko Clip a vyberte _CREATE AND EDIT CLIP_.

### Přehled

V Clip Editor uvidíte:

* tlačítka **Creator** a **Operator node** nahoře
* tlačítka **Oscillator node** vlevo
* náhled obsahu v panelu vpravo; když kliknete na node, zobrazí se druhý náhled, který ukazuje obsah přímo v daném node
* všechny nodes a propojení pro Clip, který upravujete (u nového Clip bude tato část prázdná)
* panel Clip Editor s různými možnostmi

Při úpravách zároveň uvidíte, jak Clip vypadá na pozadí ve 3D vizualizéru.

{% hint style="info" %}
Pokud ve 3D vizualizéru nevidíte žádný výstup, možná budete muset pomocí tlačítek pro zones zapnout požadované zones. Také zkontrolujte, že je zapnuté _Preview to lasers_; viz níže [Panel Clip Editor](clip-editor-intro.md#clip-editor-panel "mention").
{% endhint %}

### Sestavení Clip

Obvykle začnete jedním nebo více [Creator nodes](creator-nodes.md) a zleva doprava připojujete [Nodes typu Operator](operator-nodes/), které obsah zpracovávají. Když přesunete Creator a/nebo Operator blízko k sobě, všimnete si, že se automaticky propojí. Přetažením od sebe je zase odpojíte.

### Přidání nodes do Clip

Klikněte na jedno z tlačítek node nahoře nebo vlevo a přetáhněte je do prázdného místa v Clip Editor.

### Úprava nastavení pro node

Kliknutím na tlačítko s ikonou ozubeného kola (vpravo nahoře v node) otevřete panel vlastností pro daný node.

### Zapnutí a vypnutí node

Kliknutím na tlačítko s ikonou napájení (vlevo nahoře v node) node zapnete nebo vypnete. Node ztmavne, aby bylo vidět, že momentálně není aktivní. Pamatujte, že obsah přes Operator prochází i tehdy, když je vypnutý, ale daný node obsah nijak neovlivní.

### Propojení nodes

Obsah se vytváří pomocí Creator node a postupuje přes nodes zleva doprava. Každý Operator obsah nějakým způsobem ovlivní a předá ho dalšímu Operator. To, co zůstane na konci cesty, je obsah Clip. Creators a Operators se při přesunutí blízko k sobě automaticky propojí. Chcete-li je oddělit, přetáhněte je zase od sebe.

{% hint style="info" %}
Do vstupu dalšího node můžete připojit více než jeden node. To se hodí při kombinování více částí obsahu.
{% endhint %}

### Vlastnosti a sockets node

Každý node má dole řadu sockets a každý z nich představuje jednu vlastnost v daném node, například jas, pozici, měřítko, rotaci atd.

[Nodes typu Oscillator](oscillators/) lze k těmto sockets připojit zespodu a používat je k animaci těchto nastavení. Oscillator nodes mají nahoře výstup; kliknutím a tažením z něj vytáhnete propojení a pustíte ho do některého socket pro vlastnost u jiného node.

### Oscillator nodes

Oscillator nodes se používají ke změně vlastností v čase. Obvykle představují průběhy, jako je pilový nebo sinusový signál, ale některé Oscillator nodes používají jako zdroj externí vstupy, například úroveň vstupu z mikrofonu.

{% hint style="info" %}
Pokud jste někdy používali analogový syntezátor, koncept oscilátorů vám bude známý: běžně se používají k vytváření průběhů nebo ke změně zvuku v čase. Oscillators v Liberation dělají podobnou práci.

**Zajímavost:** název _Liberation_ byl inspirován syntezátorem Moog Liberation, „keytarem“ uvedeným v roce 1980, který proslavili Herbie Hancock, Jean-Michel Jarre a dokonce i James Brown!
{% endhint %}

Oscillators mají vždy nastavení _range_, která určují minimální a maximální hodnotu upravované vlastnosti. _Wave Oscillators_ mají vždy také nastavení _duration_, které určuje, jak rychle Oscillator mění hodnotu. Další informace najdete v části [Vlnové oscilátory](oscillators/wave-oscillators.md "mention").

### Panel Clip Editor

* Timer – nahoře v panelu uvidíte aktuální čas Clip během jeho přehrávání
* _RETRIGGER_ – spustí Clip znovu od začátku; zvlášť užitečné, pokud se Clip neopakuje ve smyčce
* _Preview to lasers_ – když je tato volba zaškrtnutá, uvidíte při úpravách tohoto Clip aktualizace ve 3D vizualizéru. Pokud ji vypnete, uvidíte Clips spuštěné mimo editor. Jde o globální nastavení, ne o nastavení pro jednotlivý Clip.
* _UNDO/REDO_ – pro samotný Clip Editor. Je také namapováno na `Cmd / Ctrl + Z` a `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ – uloží vaše úpravy, ale upozorní vás na přepsání
* _SAVE AS A COPY_ – uloží Clip do dalšího volného slotu v Clip Deck. Toto se stane novou pozicí pro váš Clip a všechna další uložení proběhnou na tomto novém místě.
* _EXIT EDITOR_ – zavře Clip Editor. Pokud máte neuložené změny, zobrazí se potvrzovací panel.
