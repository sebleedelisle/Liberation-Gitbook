---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Stručný úvod

## Úvod

Vítejte v **Liberation** – nové generaci softwaru pro laserové show.

Liberation je výkonný a komplexní moderní software. Je postavený na použitelnosti a spolehlivosti, aby vám dal svobodu vyjádřit vlastní kreativitu. Je rychlý, efektivní a plynulý. Podle tohoto _Stručného úvodu_ budete připraveni během chvilky.

### Správa laserů

Liberation je dostatečně flexibilní na to, abyste si mohli nastavit lasery a vizualizovat je i bez skutečně připojených laserů. Až budete připraveni, můžete každý výstup plynule přiřadit k laserovému kontroléru.

{% hint style="info" %}
V Liberation můžete nastavit a vizualizovat libovolný počet laserů. Licenční úrovně (Hobbyist, Pro atd.) omezují pouze počet laserů, které můžete _aktivovat pro výstup_. To znamená, že i s bezplatnou licencí můžete navrhovat laserové show se 100 lasery. Upgrade potřebujete až ve chvíli, kdy show chcete skutečně spustit na reálných laserech.
{% endhint %}

Výchozí nastavení obsahuje 8 laserů rozmístěných vodorovně, ale můžete si ho upravit podle potřeby. Než se se softwarem seznámíte, bude nejspíš nejlepší ponechat toto výchozí nastavení. Později ho můžete přizpůsobit své hardwarové sestavě. (Viz [Nastavení projektu](setting-up/setting-up-your-project.md "mention"))

{% hint style="warning" %}
Důležité: Než aktivujete jakékoli lasery pro výstup, ujistěte se, že rozumíte souvisejícím rizikům, a pečlivě projděte kapitolu [Nastavení laserů](setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Přehled softwaru

### Bezpečnostní vypnutí

Kdykoli používáte lasery, musíte mít po ruce **hardwarové tlačítko nouzového zastavení** (viz [Nouzové vypínače a bezpečnostní blokování](hardware/emergency-stop-interlocks.md "mention")). Pokud ale chcete vše vypnout méně urgentně, můžete použít tlačítko _**DISARM ALL**_, klávesu `Escape` nebo klávesu _**SESSION**_ na APC40. Globální jas můžete také snížit pomocí posuvníku na obrazovce nebo hlavního faderu na APC40.

### Posuvníky

V Liberation najdete různé posuvníky a ovládací prvky.

{% hint style="info" %}
Pokud potřebujete přesnější nastavení, než umožňuje posuvník, klikněte na něj se stisknutou klávesou `Cmd / Ctrl` a zadejte novou hodnotu ručně.
{% endhint %}

### Klávesové zkratky

Úplný seznam klávesových zkratek najdete zde: [Klávesové zkratky](reference/keyboard-shortcuts.md "mention")

### Rozvržení obrazovky

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nejste si jistí, co konkrétní tlačítko dělá? Najeďte na něj myší a zobrazí se popis.
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

V menu najdete všechny možnosti importu a exportu souborů a také otevírání panelů. Najdete zde také možnost autorizovat počítač pomocí svého předplatného (_Liberation -> Authorise/Deauthorise this computer_).

#### Lišta ikon

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Najdete zde běžné úlohy, například aktivaci a vypnutí výstupu všech laserů, Global Brightness, Test Pattern a přepínání mezi 3D view, Canvas view a Output view.

### Views

Velká oblast v levé horní části obrazovky může zobrazovat jeden ze 3 hlavních režimů: **3D**, **CANVAS** a **OUTPUT**. Přepínáte mezi nimi pomocí tlačítek v liště ikon. Můžete také použít klávesu `Tab` pro přepnutí mezi 3D view a Output view a poté postupně procházet jednotlivé laserové výstupy.

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view ukazuje, jak budou vaše lasery vypadat, a lze ji nakonfigurovat podle vaší vlastní laserové sestavy. Kliknutím a tažením otáčíte kameru, kolečkem myši se posouváte dopředu a dozadu. Mnoho dalších možností najdete v panelu _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Viz [3D vizualizér](setting-up/3d-visualiser.md "mention").

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view slouží ke konfiguraci zone a mask pro každý laser. Všimněte si velkého čísla v levém horním rohu, díky kterému snadno poznáte, který laser právě upravujete.

Tento pohled představuje celý výstup daného laseru a ukazuje, kde se v něm jednotlivé zone nacházejí. Ve výchozím nastavení má každý laser pouze jednu zone, ale můžete jich přidat tolik, kolik je rozumně praktické. Všechny je uvidíte právě v tomto pohledu.

{% hint style="info" %}
**Co je zone?**

Zone je prostor v laserovém výstupu, do kterého můžete směrovat laserový obsah. Jeden laser může mít více než jednu zone. Nejjednodušším typem je _beam_ zone, ale existují také _canvas_ zones a _DMX_ zones. V této příručce se zaměříme hlavně na beam zones, které se obvykle používají k vytváření atmosférických paprskových efektů ve vzduchu.
{% endhint %}

Laser, který chcete upravit, můžete vybrat několika způsoby:

* číslovanými tlačítky v horní liště,
* stisknutím číselné klávesy požadovaného laseru (_klávesy 1–9_)
* klávesou `Tab`, která cyklicky přechází z jednoho laseru na další.

Nový laser přidáte do sestavy stisknutím tlačítka _+_. V panelu _Laser Overview_ je také tlačítko _ADD LASER_.

Laser ze sestavy odstraníte stisknutím červeného tlačítka ⊖ v panelu _Laser Overview_.

Přibližovat a oddalovat můžete kolečkem myši. Kliknutím a tažením v místě, kde není žádná zone, posunete zobrazení.

Kliknutím na zone ji vyberete a poté můžete myší upravit její rohové body. Pokud při tažení rohu podržíte klávesu `Alt / Option`, úprava nebude rovnoměrná. Kliknutím pravým tlačítkem na zone zobrazíte další možnosti včetně změny typu zone.

Vlevo je lišta s řadou ikonových tlačítek. Když na libovolné tlačítko najedete myší, zobrazí se popis jeho funkce. Tlačítka zde umožňují přidávat beam zones, canvas zones a masks. Najdete zde také možnosti nastavení testovacího obrazce pouze pro tento laser a nastavení mřížky a přichytávání.

Podrobnosti najdete v části [Output view](output-view/ "mention").

#### Canvas

Systém Canvas se používá hlavně pro grafiku a architektonické mapování. Složité obrazy můžete rozložit přes více laserů a u každé části upravit perspektivu. Viz [Grafika a systém Canvas](graphics-and-the-canvas-system/ "mention").

### MIDI kontrolér APC40

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Liberation lze ovládat myší a klávesnicí, ale výrazně lepší je použít MIDI ovládací rozhraní APC40. Nejvhodnější je Mark 2, ale funguje i Mark 1.

Viz také: [Referenční příručka APC40](reference/apc40-reference.md "mention")

Liberation podporuje také APC Mini a MIDI Fighter Twister. Pro většinu případů je ale stále nejlepší volbou APC40 Mark 2.

### Clips a efekty

{% hint style="info" %}
**Co je Clip?**

Clip je kontejner pro libovolný laserový obsah v Liberation. Clips mohou obsahovat paprsky nebo grafické animace a obvykle jde o smyčku. Lze je směrovat do libovolné zone nebo do cílové oblasti _Canvas_ a spouští se pomocí tlačítek Clip v Clip Deck.
{% endhint %}

#### Přehled Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Tato mřížka se nazývá _Clip Deck_ a ukládají se do ní všechny laserové Clips. Je navržena tak, aby přímo odpovídala mřížce tlačítek 8 × 5 na APC40.

**Pohyb v Clip Deck.**

Clip Deck můžete posouvat doleva a doprava pomocí:

* šipek vlevo a vpravo. Přidáním `Cmd / Ctrl` se posunete vždy o celou stránku,
* trackpadu: přejetím prstem,
* myši: pokud má vaše myš vodorovné rolování, můžete ho použít při najetí nad Clip Deck,
* otočného ovladače pro posun na APC40,
* tlačítek APC40 _<- DEVICE ->_.

Pro lepší orientaci je nahoře malý vizualizér Clip Deck. Viz také [Clips a Clip Deck](clips/ "mention")

#### Spouštění a zastavování Clips

Clip spustíte stisknutím tlačítka Clip, buď myší, nebo na APC40. Dalším stisknutím ho zastavíte. Když spustíte Clip, všechny ostatní Clips stejné barvy se automaticky zastaví, pokud nedržíte _shift_.

Některé Clips budou v režimu _Flash mode_ (ve výchozím nastavení červené). V takovém případě se zastaví, jakmile tlačítko Clip pustíte.

Tlačítko _STOP_ zastaví všechny právě běžící Clips.

#### Nastavení výstupních zone pro Clip

Pod tlačítky Clip uvidíte tlačítka zone, ve výchozím nastavení beam zones 1 až 8 (_BEAM 1_, _BEAM 2_ atd.). Tlačítka zone svítí podle toho, které zone jsou přiřazené k aktuálně vybranému Clip.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

O dva řádky níže pod tlačítky zone najdete tlačítka pro převrácení X/Y. Přepnutím těchto tlačítek převrátíte Clip vodorovně nebo svisle.

{% hint style="info" %}
Pamatujte, že tato přiřazení zone a nastavení převrácení X/Y jsou svázaná se samotným Clip. Při příštím spuštění daného Clip zůstanou zachovaná. Nejde o globální nastavení.
{% endhint %}

Kliknutím pravým tlačítkem na Clip můžete upravit další nastavení. Viz také [Nastavení Clip](clips/clip-settings.md "mention")

### Skupiny

Všimnete si, že každý Clip má barevný obrys. Tato barva určuje, do které _skupiny_ patří. Tlačítka Clip na APC40 se rozsvítí stejnou barvou.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Azurová</td></tr><tr><td>Group 2</td><td>Oranžová</td></tr><tr><td>Group 3</td><td>Červená</td></tr><tr><td>Group 4</td><td>Indigová</td></tr><tr><td>Group 5</td><td>Zelená</td></tr></tbody></table>

Systém skupin je velmi flexibilní a umožňuje:

* ponechat Clips v jedné skupině běžet, zatímco přepínáte Clips v jiné skupině,
* rychle přiřadit zone a převrácení X/Y všem Clips ve skupině,
* nastavit _Flash mode_ pro Clip (Group 3 je ve výchozím nastavení v režimu _Flash mode_).

Skupiny mají také nastavení přechodu při spuštění a zastavení, která mohou jejich Clips zdědit nebo přepsat.

Skupinu pro Clip můžete přiřadit pomocí tlačítek v menu po kliknutí pravým tlačítkem. Na APC40 můžete stisknout tlačítko skupiny a _dokud ho stále držíte_, stisknout tlačítka Clip.

Změna nastavení zone pro všechny Clips ve skupině

Na APC40 stiskněte tlačítko skupiny a _dokud ho stále držíte_, pomocí tlačítek zone a X/Y přepínejte nastavení zone pro všechny Clips v dané skupině.

Viz také [Skupiny Clips](clips/groups.md "mention")

### Efekty

Systém efektů v Liberation je výkonný a všestranný způsob, jak v reálném čase měnit výstup Clip. Výchozí tlačítka efektů 1–8 jsou pod tlačítky zone.

#### Použití efektu

Efekt zapnete nebo vypnete stisknutím tlačítka efektu. Ještě lepší je ale použít fadery 1–8 na APC40 a efekty plynule přidávat nebo ubírat.

#### Parametry efektů

Pomocí otočných ovladačů 1–8\* upravíte _parameter_ každého efektu. Případně můžete kliknout pravým tlačítkem myši a upravit level a parameter. Změna parametru dělá různé věci podle toho, jak je efekt nastavený. Výchozí efekty jsou popsány níže.

{% hint style="info" %}
Malá čísla na tlačítkách efektů označují _level_ a _parameter_ efektu. _Level_ se ovládá faderem na APC40, případně kliknutím a tažením na tlačítku. Parameter se upravuje otočnými ovladači na APC40 nebo kliknutím pravým tlačítkem a úpravou myší.
{% endhint %}

_\*Otočné ovladače 1–8 jsou u APC40 Mk2 v horní části a u Mk1 vpravo nahoře. Viz také:_ [Referenční příručka APC40](reference/apc40-reference.md "mention")

#### Výchozí efekty

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**:\
   Aplikuje na výstup Clip chaotický pohyb. Parameter upravuje míru nebo rychlost chaosu.
2. **Sine wave**:\
   Deformuje veškerý obsah podle pohybující se sinusové vlny. Parameter upravuje vlnovou délku.
3. **Rotation**:\
   Otáčí vše kolem středu. Parameter upravuje rychlost otáčení.
4. **Horizontal flip**:\
   Vodorovně stlačuje a roztahuje veškerý obsah. Parameter upravuje rychlost.
5. **Scale**:\
   Opakovaně mění měřítko všeho od plné velikosti po nulu. Parameter upravuje rychlost.
6. **Hue**:\
Mění odstín všeho, ale nemění sytost (tedy vše bílé zůstane bílé). Parameter upravuje odstín.
7. **Saturation and hue**:\
Mění odstín všeho a zároveň barvu plně nasytí (tedy vše bílé se změní na danou barvu). Parameter upravuje odstín.
8. **Flash**:\
   Opakovaně mění jas všeho od plné hodnoty po nulu. Parameter upravuje rychlost blikání.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Ve spodním řádku je dalších 16 barevných efektů, které aplikují přednastavené hodnoty odstínu a sytosti.

Pamatujte, že jde o výchozí efekty, ale lze je upravit tak, aby dělaly téměř cokoli chcete.

#### Co je _„aktuálně vybraný Clip“_?

Když spustíte Clip, rozsvítí se, aby bylo vidět, že je aktivní. Zároveň má kolem sebe bílý obrys, který označuje, že jde o aktuálně _vybraný_ Clip. Kdykoli přepínáte tlačítka zone nebo upravujete nastavení Clip, změny se použijí na _aktuálně vybraný Clip_.

{% hint style="info" %}
Pokud chcete Clip vybrat bez spuštění, před stisknutím tlačítka Clip podržte klávesu `Alt / Option`. Je to dobrý způsob, jak upravit jeho zone a další nastavení bez spuštění výstupu.
{% endhint %}

### Panel Clip Settings

Panel _Clip Settings_ použijte k úpravě měřítka, polohy X/Y a k přístupu k výkonnému systému zpoždění zone.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

V panelu _Global Settings_ můžete upravovat globální nastavení výstupu, která ovlivňují veškerý výstup napříč všemi zone.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Zapnutím AUTO RESET se automaticky resetují všechna _Global settings_ vždy, když nehrají žádné Clips.

### Časování

Téměř všechny laserové show mají nějaký hudební doprovod, takže systém časování v Liberation je založený na tempu v úderech za minutu. V panelu _Tempo Panel_ vidíte znázornění času. Každý čtverec představuje jeden beat a uvidíte, jak blikají do rytmu.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

K dispozici je více možností synchronizace včetně MIDI clock a Ableton Link. Pokud znáte tempo hudby, můžete ho ručně upravit pomocí posuvníku na obrazovce nebo ovladače Tempo na APC40. Tempo ale můžete s hudbou udržovat také pomocí systému _Tap Tempo_.

#### Tap Tempo

_Tap Tempo_ je termín běžně používaný v hudebních aplikacích. Umožňuje vyťukat rytmus podle právě hrající hudby a nastavit tak tempo. Můžete použít tlačítko na obrazovce, ale doporučuje se klávesa _T_ nebo tlačítko _Tap Tempo_ na APC40, případně i nožní spínač, pokud vám vyhovuje.

Stisknutím klávesy _R_ nebo tlačítka _Metronome_ na APC40 resetujete tempo na začátek taktu.

Stisknutím klávesy _Y_ nebo otočením ovladače _Tempo_ na APC40 zaokrouhlíte tempo na celé číslo. To může být užitečné u elektronické hudby, která mívá tempo s celým počtem úderů za minutu.

### Organizace Clip Deck

Chcete-li přesunout Clip v Clip Deck, klikněte na něj a přetáhněte ho na novou pozici. Během tažení můžete pomocí kurzorových kláves nebo kolečka/tlačítek pro posun na APC40 posouvat zobrazení doleva a doprava.

Při tažení podržte klávesu `Alt / Option`, chcete-li vytvořit kopii.

Kliknutím na Clip se stisknutou klávesou `Alt / Option` ho vyberete bez spuštění.

Kliknutím na Clip se stisknutými klávesami `Alt / Option + Shift` provedete vícenásobný výběr. Případně klikněte a táhněte mimo Clip pro výběr „lasem“.

Kliknutí a tažení přesune VŠECHNY vybrané Clips.

Jeden nebo více Clips odstraníte buď přetažením mimo Clip Deck (zobrazí se ikona koše), nebo pomocí tlačítka DELETE v menu Clip po kliknutí pravým tlačítkem.

### Panel Laser Overview

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panel _Laser Overview_ vám rychle ukáže stav právě používaných laserů. Zelený čtverec vpravo znamená, že laserový kontrolér pracuje správně. Pokud zoranžoví, dochází k občasným výpadkům, a pokud je červený, kontrolér se odpojil. Pokud je šedý, není vůbec připojený ke kontroléru.

Graf uprostřed zobrazuje historii délek snímků a číslo vpravo je aktuální snímková frekvence. Čím složitější je obsah, tím nižší bude snímková frekvence (tedy tím více může obraz působit blikavě). Cokoli pod zhruba 25 fps začne vypadat trochu roztřeseně nebo blikavě.

### Připojení k laserům – panel Controller Assignment

Kliknutím na tlačítko _Assign Laser Controllers_ otevřete panel _Controller Assignment_. Tento panel je dostupný také z menu _View -> Controller Assignment_.

Zde můžete zvolit, které laserové výstupy půjdou do kterých laserových kontrolérů. Přetáhněte kontroléry ze seznamu vpravo do slotů vlevo. Kontroléry můžete přejmenovat podle toho, s jakým laserem jsou spárované (použijte tlačítko s ikonou tužky).

Další podrobnosti najdete v kapitole [Controller Assignment](setting-up/controller-assignment.md "mention").

{% hint style="danger" %}
Než aktivujete jakékoli lasery pro výstup, projděte si kapitolu [Nastavení laserů](setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Panel Laser Settings

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Tento panel zobrazuje nastavení pro _aktuálně vybraný laser_ (znázorněný číslem nahoře). Aktuálně vybraný laser změníte klávesou _tab_, stisknutím číselné klávesy, kliknutím na číslo laseru v panelu _Laser Overview_ nebo v _Output view_.

* **Number button** aktivuje nebo vypíná výstup laseru. Pokud je červené, laser je aktivovaný pro výstup.
* **Brightness** upravuje jas laseru nezávisle na ostatních laserech. Kombinuje se s nastavením _global brightness_ – například pokud jsou oba jasy na 50 %, laser bude na 25 %.
* **Test Pattern** zapne testovací obrazec pouze pro tento laser a přepíše globální nastavení testovacího obrazce.
* **Orientation** opravuje orientaci laserů zavěšených bokem nebo vzhůru nohama.
* **Flip Horizontal and Flip Vertical** obrací výstup laseru. Hodí se ke korekci výstupu u laserů s nekonzistentním zapojením.
* **Copy Laser Settings** otevře panel, ve kterém můžete zkopírovat různá nastavení z tohoto laseru do ostatních.

### Nastavení skenerů

Zobrazovací lasery fungují tak, že extrémně rychle pohybují jedním laserovým paprskem a zapínáním a vypínáním paprsku kreslí tvary ve vzduchu. To, co vidíte jako čáry, tvary a obrazy, je ve skutečnosti paprsek, který opisuje dráhy rychleji, než je vaše oko dokáže sledovat.

Proud bodů je datový tok, který laseru říká, kam se má dál přesunout a kdy má být paprsek zapnutý nebo vypnutý. V Liberation se Clips převádějí na tento proud bodů v reálném čase při odesílání do laserů.

Liberation vám dává podrobnou kontrolu nad tím, jak se tento proud bodů generuje, takže můžete u každého laseru vyvážit plynulost, jas a výkon.

{% hint style="info" %}
Pokud jste zvyklí na starší laserový software, který spoléhá na předem vypočítané proudy bodů, může tento přístup zpočátku působit jinak. Generování bodů v reálném čase ale umožňuje stejný obsah optimalizovat pro každý laser odlišně. Díky tomu se snáze pracuje s více lasery, které mají různé rychlosti nebo kvalitu skenerů, aniž byste museli obsah duplikovat nebo znovu vytvářet. Zároveň to udržuje soubory Clip velmi malé, takže celý výchozí Clip Deck v Liberation má jen několik megabajtů místo gigabajtů.
{% endhint %}

Základní nastavení skenerů jsou:

* **Speed** je rychlost skeneru, tedy jak rychle se laser pohybuje při kreslení tvarů. Odpovídá to úpravě point rate v tradičním laserovém softwaru, ale v Liberation můžete měnit rychlost pohybu laseru _nezávisle na point rate_. Toto nastavení byste neměli potřebovat měnit.
* **Scanner sync** (někdy označované jako _blank shift_, dříve Colour Shift) Skener pohybuje laserem velmi rychle, ale změna jasu a barvy obvykle není synchronní s pohybem. Projevuje se to jako malé blikající „ocásky“ světla na okrajích paprsků a čar. Tímto nastavením sladíte pohyb a barvu. Viz [Laser Settings](setting-up/laser-settings.md "mention")

Další pokročilá nastavení skenerů jsou popsána v kapitole [Pokročilé](advanced/ "mention").

### Zoning

Úplný návod k nastavení a zoning laserů najdete zde: [Nastavení laserů](setting-up/setting-up-lasers.md "mention")
