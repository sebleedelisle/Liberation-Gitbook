# ✅ Rychlý úvod

## Úvod

Vítejte v **Liberation** – nové generaci softwaru pro laserové show.

Liberation je výkonný a komplexní moderní software. Je postavený na základech použitelnosti a spolehlivosti, aby vám dal svobodu vyjádřit kreativitu. Je rychlý, efektivní a plynulý. Postupujte podle tohoto _Rychlého úvodu_ a za chvíli budete připraveni pracovat!

### Správa laserů

Liberation je dostatečně flexibilní na to, abyste mohli nastavovat lasery a vizualizovat je i bez jakýchkoli skutečných připojených laserů. Až budete připraveni, můžete pak každý výstup plynule přiřadit k laserovému kontroléru.

{% hint style="info" %}
V Liberation můžete nastavit a vizualizovat libovolný počet laserů. Licenční úrovně (Hobbyist, Pro atd.) omezují pouze počet laserů, které můžete _aktivovat pro výstup._ To znamená, že i s bezplatnou licencí můžete navrhovat laserové show se 100 lasery. Upgrade potřebujete až ve chvíli, kdy je chcete skutečně spustit na reálných laserech.
{% endhint %}

Výchozí nastavení obsahuje 8 laserů rozložených vodorovně, ale můžete si ho upravit podle potřeby. Než se se softwarem seznámíte, bude pravděpodobně nejlepší ponechat toto výchozí nastavení. Později ho můžete upravit tak, aby odpovídalo vaší hardwarové sestavě. (Viz [Nastavení projektu](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Důležité: Než aktivujete jakékoli lasery pro výstup, ujistěte se, že rozumíte souvisejícím rizikům, a pečlivě si projděte kapitolu [Nastavení laserů](../setting-up/setting-up-lasers.md).
{% endhint %}

## Přehled softwaru

### Bezpečnostní vypnutí

Kdykoli používáte lasery, musíte mít po ruce **hardwarové tlačítko nouzového zastavení** (viz [Nouzové zastavení a bezpečnostní blokování](../hardware/emergency-stop-interlocks.md)). Pokud ale chcete deaktivovat vše méně naléhavě, můžete použít tlačítko _**DISARM ALL**_, klávesu `Escape` nebo klávesu _**SESSION**_ na APC40. Globální jas můžete také snížit pomocí posuvníku na obrazovce nebo hlavního faderu na APC40.

### Posuvníky

V Liberation najdete různé posuvníky a ovládací prvky.

{% hint style="info" %}
Pokud potřebujete přesnější ovládání, než umožňuje posuvník, klikněte na něj se stisknutou klávesou `Cmd / Ctrl` a zadejte novou hodnotu.
{% endhint %}

### Klávesové zkratky

Úplný seznam klávesových zkratek najdete zde: [Klávesové zkratky](../reference/keyboard-shortcuts.md)

### Rozložení obrazovky

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nejste si jistí, co některé tlačítko dělá? Najeďte na něj myší a zobrazí se popis.
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

V menu najdete všechny možnosti importu a exportu souborů a také zde otevíráte panely. Najdete tu i možnost autorizovat počítač pomocí vašeho předplatného (_Liberation -> Authorise/Deauthorise this computer_).

#### Lišta ikon

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Najdete zde běžné úlohy, například aktivaci a deaktivaci všech laserů, Global Brightness, Test Pattern a přepínání mezi zobrazeními 3D, Canvas a Output.

### Zobrazení

Velká oblast vlevo nahoře na obrazovce může zobrazovat jedno ze 3 hlavních zobrazení: **3D**, **CANVAS** a **OUTPUT.** Přepínáte mezi nimi pomocí tlačítek na liště ikon. Můžete také použít klávesu `Tab` pro přepínání mezi zobrazeními 3D a OUTPUT a potom pokračovat v postupném procházení jednotlivých laserových výstupů.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view ukazuje, jak budou vaše lasery vypadat, a lze ho nastavit tak, aby odpovídal vaší vlastní laserové sestavě. Kliknutím a tažením otáčíte kameru, kolečkem myši se posouváte dopředu a dozadu. Mnoho dalších možností najdete v panelu _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Viz [3D Visualiser](../setting-up/3d-visualiser.md).

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view slouží k nastavení zones a masks pro každý laser. Všimněte si velkého čísla v levém horním rohu, abyste snadno viděli, se kterým laserem právě pracujete.

Toto zobrazení představuje celý výstup daného laseru a ukazuje, kde se v něm nachází jednotlivé zones. Ve výchozím nastavení je pro každý laser jen jedna zone, ale můžete přidat tolik zones, kolik je rozumně praktické. V tomto zobrazení je uvidíte všechny.

{% hint style="info" %}
**Co je zone?**

Zone je prostor v rámci výstupu laseru, do kterého můžete směrovat laserový obsah. Jeden laser může mít více než jednu zone. Nejjednodušším typem je beam zone, ale existují také canvas zone a DMX zone. V tomto průvodci se budeme soustředit hlavně na beam zones, které se obvykle používají k vytváření atmosférických paprskových efektů ve vzduchu.
{% endhint %}

Laser, který chcete upravovat, můžete vybrat jedním z těchto způsobů:

* číselnými tlačítky v liště nahoře
* stisknutím číselné klávesy požadovaného laseru _(klávesy 1–9)_
* klávesou `Tab`, která postupně přechází z jednoho laseru na další

Nový laser do sestavy přidáte stisknutím tlačítka _+_. (V panelu _Laser Overview_ je také tlačítko _ADD LASER_.)

Laser ze sestavy odstraníte stisknutím červeného tlačítka ⊖ v panelu _Laser Overview_.

Přibližovat a oddalovat můžete kolečkem myši. Kliknutím a tažením kdekoli mimo zone posunete zobrazení.

Kliknutím na zone ji vyberete a potom můžete myší upravit její rohové body. Pokud při tažení rohu podržíte klávesu `Alt / Option`, úprava nebude rovnoměrná. Kliknutím pravým tlačítkem na zone zobrazíte další možnosti včetně změny typu zone.

Vlevo je lišta s řadou ikonových tlačítek. Když na libovolné tlačítko najedete myší, zobrazí se popis jeho funkce. Tlačítka zde umožňují přidávat beam zones, canvas zones a masks. Najdete tu také možnosti nastavit Test Pattern pouze pro tento laser a nastavení mřížky a přichytávání.

Další podrobnosti najdete v části [Output view](../output-view/).

#### Canvas

Systém Canvas se používá hlavně pro grafiku a architektonický mapping. Složité obrazy můžete rozdělit mezi více laserů a u každé části korigovat perspektivu. Viz [Grafika a systém Canvas](../graphics-and-the-canvas-system/).

### MIDI kontrolér APC40

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Liberation je sice možné ovládat myší a klávesnicí, ale mnohem lepší je použít MIDI ovládací rozhraní APC40. Nejvhodnější je Mark 2, ale funguje i Mark 1.

Viz také: [Referenční příručka APC40](../reference/apc40-reference.md)

Nově jsme implementovali také podporu pro APC Mini Mark 2 a MIDI Fighter Twister a další zařízení jsou ve vývoji. Pro většinu případů je ale nejlepší volbou APC40 Mark 2.&#x20;

### Clips a efekty

{% hint style="info" %}
**Co je Clip?**

Clip je kontejner pro libovolný laserový obsah v Liberation. Clips mohou obsahovat paprsky nebo grafické animace a obvykle jde o smyčku. Lze je směrovat do libovolné zone nebo _cílové oblasti Canvas_ a spouští se pomocí tlačítek Clip v rámci Clip Deck.
{% endhint %}

#### Přehled Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Tato mřížka se nazývá _Clip Deck_ a ukládají se do ní všechny laserové Clips. Je navržena tak, aby přímo odpovídala mřížce tlačítek 8 × 5 na APC40.

**Navigace v Clip Deck.**

V Clip Deck se můžete posouvat doleva a doprava pomocí:

* Šipky doleva a doprava. Přidáním `Cmd / Ctrl` se posunete vždy o celou stránku.
* Trackpad: přejetí prstem
* Myš: pokud má vaše myš boční posun, můžete ho použít, když je kurzor nad Clip Deck
* otočný ovladač posunu na APC40
* tlačítka APC40 _<- DEVICE ->_

Pro lepší orientaci je nahoře miniaturní vizualizace Clip Deck. Viz také [Clips a Clip Deck](../clips/)

#### Spouštění a zastavování Clips

Stisknutím tlačítka Clip (myší nebo na APC40) spustíte Clip. Dalším stisknutím ho zastavíte. Když spustíte Clip, všechny ostatní Clips stejné barvy se automaticky zastaví, pokud nedržíte _shift_.

Některé Clips budou v režimu _Flash mode_ (ve výchozím nastavení červené). V takovém případě se zastaví hned, jak tlačítko Clip pustíte.

Tlačítko _STOP_ zastaví všechny aktuálně spuštěné Clips.

#### Nastavení výstupních zones pro Clip

Pod tlačítky Clip uvidíte tlačítka zones, ve výchozím nastavení beam zones 1 až 8 (_BEAM 1_, _BEAM 2_ atd.). Tlačítka zones svítí podle toho, které zones jsou přiřazené k aktuálně vybranému Clip.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

O dva řádky níže pod tlačítky zones najdete tlačítka X/Y flip. Těmi můžete Clip převrátit vodorovně a svisle.

{% hint style="info" %}
Tato přiřazení zones a nastavení X/Y flip jsou svázaná se samotným Clip. Při příštím spuštění tohoto Clip zůstanou zachovaná. Nejde o globální nastavení.
{% endhint %}

Kliknutím pravým tlačítkem na Clip upravíte další nastavení tohoto Clip. Viz také [Nastavení Clip](../clips/clip-settings.md)

### Skupiny

Všimněte si, že každý Clip má barevný obrys. Tato barva určuje, do které _skupiny_ patří. Tlačítka Clip na APC40 se také rozsvítí touto barvou.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Skupina 1</td><td>Azurová</td></tr><tr><td>Skupina 2</td><td>Oranžová</td></tr><tr><td>Skupina 3</td><td>Červená</td></tr><tr><td>Skupina 4</td><td>Indigo</td></tr><tr><td>Skupina 5</td><td>Zelená</td></tr></tbody></table>

Systém skupin je velmi flexibilní a umožňuje:

* ponechat spuštěné Clips v jedné skupině, zatímco přepínáte skupiny v jiné
* rychle přiřadit zones a X/Y flips všem Clips ve skupině
* nastavit _Flash mode_ pro Clip (Skupina 3 je ve výchozím nastavení nastavena na _Flash mode_)

Skupiny mají také nastavení přechodu dovnitř/ven, která mohou jejich Clips zdědit nebo přepsat.

Skupinu Clip můžete přiřadit pomocí tlačítek v menu po kliknutí pravým tlačítkem. Na APC40 můžete také stisknout tlačítko skupiny a _zatímco ho stále držíte,_ stisknout tlačítka Clip.

Změna nastavení zones pro všechny Clips ve skupině

Na APC40 stiskněte tlačítko skupiny a _zatímco ho stále držíte,_ použijte tlačítka zones a X/Y pro přepnutí nastavení zones u všech Clips v této skupině.

Viz také [Skupiny Clips](../clips/groups.md)

### Efekty

Systém efektů v Liberation je výkonný a univerzální způsob, jak v reálném čase měnit výstup Clip. Výchozí tlačítka efektů 1–8 jsou pod tlačítky zones.

#### Použití efektu

Stisknutím tlačítka efektu efekt zapnete nebo vypnete. Ještě lepší je používat fadery 1–8 na APC40 a efekty plynule přidávat nebo ubírat.

#### Parametry efektů

Otočnými ovladači 1–8\* nastavujete _parameter_ jednotlivých efektů. (Případně můžete kliknout pravým tlačítkem myši a upravit úroveň a parametr.) Změna parametru dělá různé věci podle toho, jak je efekt nastavený. Výchozí efekty najdete v seznamu níže.

{% hint style="info" %}
Malá čísla na tlačítkách efektů označují _level_ a _parameter_ efektu. _Level_ se ovládá faderem na APC40 nebo kliknutím a tažením na tlačítku. Parametr se nastavuje otočnými ovladači na APC40 nebo kliknutím pravým tlačítkem a úpravou myší.
{% endhint %}

_\*Otočné ovladače 1–8 jsou u APC40 Mk2 nahoře a u Mk1 vpravo nahoře. Viz také:_ [Referenční příručka APC40](../reference/apc40-reference.md)

#### Výchozí efekty

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**:\
   Aplikuje na výstup Clip chaotický pohyb. Parametr upravuje množství/rychlost chaosu.
2. **Sine wave**:\
   Deformuje veškerý obsah podél pohybující se sinusové vlny. Parametr upravuje vlnovou délku.
3. **Rotation**:\
   Roztočí vše kolem dokola. Parametr upravuje rychlost otáčení.
4. **Horizontal flip**:\
   Vodorovně stlačuje a roztahuje všechen obsah. Parametr upravuje rychlost.
5. **Scale**:\
   Opakovaně mění měřítko všeho od plné velikosti po nulu. Parametr upravuje rychlost.
6. **Hue**:\
   Mění odstín všeho, ale nemění sytost (tedy vše, co je bílé, zůstane bílé). Parametr upravuje odstín.
7. **Saturation and hue**:\
   Mění odstín všeho a zároveň barvu plně nasytí (tedy vše, co je bílé, se změní na danou barvu). Parametr upravuje odstín.
8. **Flash**:\
   Opakovaně bliká jasem všeho od plné hodnoty po nulu. Parametr upravuje rychlost blikání.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Ve spodním řádku je dalších 16 barevných efektů pro použití přednastavených hodnot odstínu a sytosti.

Toto jsou výchozí efekty, ale můžete je upravit tak, aby dělaly téměř cokoli chcete.

#### Co je _„aktuálně vybraný Clip“_?

Když spustíte Clip, rozsvítí se, aby bylo vidět, že je aktivní. Zároveň má kolem sebe bílý obrys, který označuje, že jde o aktuálně _vybraný_ Clip. Kdykoli přepnete tlačítka zones nebo upravíte nastavení Clip, změny se použijí na _aktuálně vybraný Clip._

{% hint style="info" %}
Chcete-li vybrat Clip bez jeho spuštění, před stisknutím tlačítka Clip podržte klávesu `Alt / Option`. Je to dobrý způsob, jak upravit jeho zones a další nastavení, aniž by se spustil.
{% endhint %}

### Panel Clip Settings

Pomocí panelu _Clip Settings_ můžete upravovat měřítko, pozici X/Y a získat přístup k výkonnému systému zpoždění pro zones.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

V panelu _Global Settings_ můžete upravit globální nastavení výstupu, která ovlivňují veškerý výstup ve všech zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Zapnutím AUTO RESET se automaticky resetují všechna nastavení _Global settings_, kdykoli se nepřehrávají žádné Clips.&#x20;

### Časování

Téměř všechny laserové show mají nějaký hudební doprovod, takže systém časování v Liberation je založený na tempu v úderech za minutu. V panelu _Tempo Panel_ vidíte znázornění času: každý čtverec představuje jeden beat a čtverce blikají v rytmu.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

K dispozici je více možností synchronizace, včetně MIDI clock a Ableton Link. Pokud znáte tempo hudby, můžete ho ručně upravit pomocí posuvníku na obrazovce nebo ovladače Tempo na APC40. S hudbou ale můžete držet krok také pomocí systému _Tap Tempo_\_.\_

#### Tap Tempo

_Tap Tempo_ je termín běžně používaný v hudebních aplikacích. Umožňuje nastavovat tempo klepáním do rytmu během přehrávání hudby. Můžete použít tlačítko na obrazovce, ale doporučuje se použít klávesu _T_ nebo tlačítko _Tap Tempo_ na APC40, případně i nožní spínač, pokud vám to vyhovuje.

Stisknutím klávesy _R_ nebo tlačítka _Metronome_ (APC40) resetujete tempo na začátek taktu.

Stisknutím klávesy _Y_ nebo otočením ovladače _Tempo_ (APC40) zaokrouhlíte tempo na celé číslo. To může být užitečné u elektronické hudby, která mívá tempo v celých úderech za minutu.

### Organizace Clip Deck

Chcete-li přesunout Clip v Clip Deck, klikněte na něj a přetáhněte ho na nové místo. Během tažení můžete pomocí kurzorových kláves nebo kolečka/tlačítek posunu na APC40 posouvat zobrazení doleva a doprava.

Při tažení podržte klávesu `Alt / Option`, chcete-li vytvořit kopii.

Kliknutím na Clip se stisknutou klávesou `Alt / Option` ho vyberete bez spuštění.

Kliknutím na Clip se stisknutými klávesami `Alt / Option + Shift` provedete vícenásobný výběr. Případně klikněte a táhněte mimo Clip a vyberte oblast „lasem“.&#x20;

Kliknutí a tažení přesune VŠECHNY vybrané Clips.

Chcete-li odstranit jeden nebo více Clips, buď je přetáhněte mimo Clip Deck (zobrazí se ikona koše), nebo použijte tlačítko DELETE z menu Clip po kliknutí pravým tlačítkem.

### Panel Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panel _Laser Overview_ vám poskytuje rychlý přehled o stavu aktuálně spuštěných laserů. Zelený čtverec vpravo znamená, že laserový kontrolér funguje správně. Pokud se změní na oranžový, dochází k občasným výpadkům. Pokud je červený, kontrolér je odpojený. Pokud je šedý, není k žádnému kontroléru připojený vůbec.&#x20;

Graf uprostřed zobrazuje historii délek snímků a číslo vpravo ukazuje aktuální snímkovou frekvenci. Čím složitější obsah, tím nižší snímková frekvence bude, tedy tím víc bude obraz blikat. Hodnoty pod přibližně 25 fps už začnou působit poněkud blikavě.&#x20;

### Připojení k laserům – panel Controller Assignment

Kliknutím na tlačítko _Assign Laser Controllers_ otevřete panel _Controller Assignment_. (K tomuto panelu se dostanete také přes _View -> Controller Assignment_ v liště menu.)

Zde můžete zvolit, které laserové výstupy půjdou do kterých laserových kontrolérů. Přetáhněte kontroléry ze seznamu vpravo do slotů vlevo. Kontroléry si můžete přejmenovat podle toho, se kterým laserem jsou spárované (použijte tlačítko s ikonou pera).

Další podrobnosti najdete v kapitole [Controller Assignment](../setting-up/controller-assignment.md).

{% hint style="danger" %}
Než aktivujete jakékoli lasery pro výstup, projděte si kapitolu [Nastavení laserů](../setting-up/setting-up-lasers.md).
{% endhint %}

### Panel Laser Settings

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Tento panel zobrazuje nastavení _aktuálně vybraného laseru_ (označeného číslem nahoře). Aktuálně vybraný laser změníte klávesou _tab_, stisknutím číselné klávesy, kliknutím na číslo laseru v panelu _Laser Overview_ nebo v _Output view._

* **Number button** aktivuje a deaktivuje laser pro výstup. Pokud je červené, laser je aktivovaný.
* **Brightness** upravuje jas laseru nezávisle na ostatních laserech. Kombinuje se s nastavením _Global Brightness_ – tedy pokud jsou obě hodnoty na 50 %, váš laser bude na 25 %.
* **Test Pattern** zapne testovací obrazec pouze pro tento laser (přepíše globální nastavení Test Pattern).
* **Orientation** koriguje lasery zavěšené na bok nebo vzhůru nohama.
* **Flip Horizontal and Flip Vertical** obrací výstup laseru. Hodí se pro korekci výstupu u laserů s nejednotným zapojením.
* **Copy Laser Settings** otevře panel, který umožňuje zkopírovat různá nastavení z tohoto laseru do ostatních.

### Nastavení skenerů

Zobrazovací lasery fungují tak, že extrémně rychle pohybují jedním laserovým paprskem a zapínají a vypínají ho, aby ve vzduchu kreslily tvary. To, co vidíte jako čáry, tvary a obrazy, je ve skutečnosti paprsek sledující dráhy rychleji, než je vaše oko stihne sledovat.

Point stream je datový proud, který laseru říká, kam se má přesunout dál a kdy má být paprsek zapnutý nebo vypnutý. V Liberation se Clips převádějí do tohoto point stream v reálném čase při odesílání do laserů.

Liberation vám dává podrobnou kontrolu nad tím, jak se tento point stream generuje, abyste mohli u každého laseru vyvážit plynulost, jas a výkon.

{% hint style="info" %}
Pokud jste zvyklí na starší laserový software, který spoléhá na předem vypočítané point stream, může tento přístup zpočátku působit jinak. Generování bodů v reálném čase ale umožňuje optimalizovat stejný obsah pro každý laser odlišně. Díky tomu se snáze pracuje s více lasery, které mají různé rychlosti nebo kvalitu skenerů, aniž by bylo nutné obsah duplikovat nebo znovu vytvářet. Zároveň jsou soubory Clip velmi malé, a proto má celý výchozí Clip Deck v Liberation jen několik megabajtů místo gigabajtů.
{% endhint %}

Základní nastavení skenerů jsou:

* **Speed** je rychlost skenerů, tedy jak rychle se laser pohybuje při kreslení tvarů. Odpovídá to úpravě point rate v tradičním laserovém softwaru, ale v Liberation můžete měnit rychlost pohybu laseru _nezávisle na point rate._ Toto nastavení byste neměli potřebovat měnit.
* **Scanner sync** (někdy označované jako _blank shift, dříve Colour Shift_) Skener pohybuje laserem opravdu rychle, ale změna jasu a barvy obvykle není synchronizovaná s pohybem. Projevuje se to jako malé blikající „ocásky“ světla na okrajích paprsků a čar. Tímto nastavením sladíte pohyb a barvu. Viz [Laser Settings](../setting-up/laser-settings/)

Další pokročilá nastavení skenerů jsou popsána v kapitole [Pokročilé](../advanced/).

### Zoning

Úplného průvodce nastavením laserů a zoning najdete zde: [Nastavení laserů](../setting-up/setting-up-lasers.md)
