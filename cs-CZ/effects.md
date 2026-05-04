---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Efekty

Systém efektů v Liberation je zábavný a všestranný způsob, jak v reálném čase měnit výstup z Clip. Efekty jsou plně flexibilní a můžete je použít k tomu, aby vše blikalo, otáčelo se, měnilo barvy, nebo se dokonce náhodně pohybovalo v prostoru.

Jako efekt můžete použít cokoli, co lze vytvořit v Clip Editor. Efekty se ve skutečnosti upravují ve stejném editoru nodes jako Clips! Viz [Úprava efektů](effects.md#editing-effects "mention"). Tvůrčí možnosti jsou prakticky neomezené.

Výchozí tlačítka efektů 1–8 jsou pod tlačítky zone a efekty 9–24 jsou malá tlačítka dole.

#### Použití efektu

Stisknutím tlačítka efekt efekt zapnete nebo vypnete. Ještě lepší je použít fadery 1–8 na APC40 a efekty plynule přidávat nebo ubírat. Chcete-li efekt plynule přidat bez APC40, klikněte na tlačítko a táhněte nahoru nebo dolů. Případně klikněte na tlačítko efektu pravým tlačítkem a upravte posuvník úrovně.

{% hint style="warning" %}
Stisknutí tlačítka efektu tento efekt okamžitě aktivuje. Pokud je ale úroveň nastavena na nulu, nic se nestane! Kliknutím a tažením na tlačítku změňte úroveň, případně klikněte pravým tlačítkem a použijte posuvník _level_, nebo použijte fadery na APC40.
{% endhint %}

#### Efekty a zpoždění zone v Clip

Efekty přebírají nastavení zpoždění zone pro každý právě spuštěný Clip. Pokud tedy má váš Clip zpoždění, které postupuje zleva doprava, a přidáte blikající efekt, bude se i blikání zpožďovat zleva doprava.

{% hint style="info" %}
To, jak efekty dědí zpoždění zone z Clip, se velmi těžko popisuje, ale jakmile to vyzkoušíte, je to okamžitě jasné!

Podle mě je to jeden z nejzábavnějších a nejkreativnějších nástrojů, které jsou v Liberation zabudované. Vyzkoušejte to a uvidíte, co tím myslím!
{% endhint %}

#### Parametry efektů

Parametr do efektu přidáte pomocí _Parameter node._ Systém parametrů umožňuje zvenku upravovat více nastavení uvnitř efektu. Další informace najdete v části [Ovládání parametrů](clip-editor/oscillators/parameter-control.md "mention").

Pomocí otočných ovladačů 1–8 upravíte _parameter_ pro každý efekt. Případně klikněte pravým tlačítkem na tlačítko efektu a upravte posuvníky parametrů. Změna parametru dělá různé věci podle toho, jak je efekt nastavený. Níže najdete seznam výchozích efektů a popis toho, co jejich parametry dělají.

{% hint style="info" %}
Otočné ovladače 1–8 jsou na APC40 Mk2 v horní řadě a na Mk1 vpravo nahoře. Viz také: [Referenční přehled APC40](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
Malá čísla na tlačítkách efektů označují _level_ a _parameter_ daného efektu. _level_ ovládáte faderem na APC40, případně kliknutím a tažením na tlačítku. Parametr upravujete otočnými ovladači na APC40, případně kliknutím pravým tlačítkem a nastavením myší.
{% endhint %}

#### Výchozí efekty

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Aplikuje na výstup Clip chaotický pohyb. Parametr upravuje míru/rychlost chaosu.
2. **Sine wave** :\
   Deformuje veškerý obsah podle pohybující se sinusovky. Parametr upravuje vlnovou délku.
3. **Rotation** :\
   Otáčí vším dokola. Parametr upravuje rychlost otáčení.
4. **Horizontal flip** :\
   Vodorovně stlačuje a roztahuje všechen obsah. Parametr upravuje rychlost.
5. **Scale** :\
   Opakovaně mění měřítko všeho od plné velikosti po nulu. Parametr upravuje rychlost.
6. **Hue** :\
Mění odstín všeho, ale nemění sytost (tj. vše, co je bílé, zůstane bílé). Parametr upravuje odstín.
7. **Saturation and hue** :\
Mění odstín všeho a zároveň barvu plně nasytí (tj. vše, co je bílé, se změní na danou barvu). Parametr upravuje odstín.
8. **Flash** :\
   Opakovaně nechává jas všeho blikat od plné hodnoty po nulu. Parametr upravuje rychlost blikání.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Ve spodní řadě je dalších 16 barevných efektů, které aplikují přednastavené hodnoty odstínu a sytosti.

Upozorňujeme, že jde o výchozí efekty, ale můžete je upravit tak, aby dělaly téměř cokoli chcete!

### Použití na skupiny

Můžete zvolit, které skupiny budou efektem ovlivněny. Klikněte pravým tlačítkem a přepínejte zaškrtávací políčka skupin označená _Apply to groups._

Toto nastavení používám hlavně tehdy, když pracuji odděleně s grafikou na Canvas a laserovými paprsky. Všechny canvas Clips přiřadím do skupiny 5 a potom tuto skupinu vyloučím z efektů, u kterých nechci, aby tyto grafické Clips ovlivňovaly.

Můžete to také použít k tomu, abyste naživo aplikovali 2 různé změny barev na 2 skupiny laserů současně. Vytvořte dva efekty změny barvy a vyberte, na které skupiny Clips se má každý z nich použít.

### Skupina MX

Zkratka pro _Mutually Exclusive_. Jde o způsob, jak seskupit efekty tak, aby mohl být v dané skupině aktivní vždy jen jeden efekt. Všimněte si, že z výchozích efektů měnících barvu může být aktivní vždy jen jeden. Je to proto, že všechny patří do MX Group 1.

Tato funkce je vypnutá, pokud je nastavení _MX Group_ nastaveno na 0.

### Úprava efektů

Klikněte pravým tlačítkem na libovolný efekt a kliknutím na tlačítko _EDIT EFFECT_ otevřete editor efektu. Všimněte si, že tento editor je totožný s Clip Editor!

Efekt upravujete stejně, jako byste upravovali jakýkoli Clip. Viz [Clip Editor](clip-editor/ "mention").

Musíte mít alespoň jeden node typu Creator. Může to být cokoli (čára, kruh, tvar, dokonce i text!), ale pravděpodobně byste měli vybrat něco, co dává v náhledu tlačítka efektu největší smysl.

Když se efekty aplikují, všechny nodes typu Creator v efektu se nahradí výstupem právě spuštěných Clips.

{% hint style="warning" %}
Z mimořádně únavných technických důvodů nejsou nodes „trails“ uvnitř efektu povolené. Totéž platí pro nastavení „delay“ uvnitř pattern nodes (používají stejný systém). V budoucích verzích to bude opraveno.
{% endhint %}
