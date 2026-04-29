---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / synchronizace

Synchronizace s hudbou je v Liberation zásadní prvek. Jakmile sladíte tempo a doby s hudbou, můžete si být jistí, že vše poběží synchronně. Pokud máte k dispozici MIDI clock nebo Ableton Link, nemusíte ruční synchronizaci vůbec řešit. Pokud ne, nevadí – můžete se sladit ručně pomocí funkce tempa _Live_.

Pokud máte zkušenosti s hudebním nebo osvětlovacím softwarem, bude vám tento postup povědomý. Pokud ne, vyplatí se věnovat nějaký čas seznámení se systémem a nácviku doma, než půjdete na živé vystoupení.

## Panel Tempo

Panel _Tempo_ je vždy zobrazený na obrazovce a obsahuje všechna nastavení synchronizace. Nahoře uvidíte aktuální počítadlo taktů/dob a transport s tlačítky přehrát/pozastavit a přetočit zpět/vpřed.

Pod tím je značka doby: čtyři čtverce, které „pulzují“ do rytmu. Tato _beat marker_ je mimořádně užitečná vizualizace a při používání systému tempa _Live_ se na ni budete neustále odkazovat.

### Nastavení tempa

Tempo můžete nastavit několika způsoby:

* Klikněte a táhněte posuvník _Tempo_
* Podržte Shift, klikněte a táhněte posuvník _Tempo_ pro změny po 0,1
* Dvakrát klikněte na posuvník _Tempo_ a zadejte číslo ručně
* Použijte knob _Tempo_ na APC40 (pro kroky po 0,1 podržte Shift)
* Tap Tempo

{% hint style="info" %}
Tempo se udává v „dobách za minutu“ a tradiční výchozí hodnota bývá 120.
{% endhint %}

## Tap Tempo

Nastavte tempo automaticky klikáním na tlačítko _TAP_ do rytmu. Začátek taktu nastavíte tlačítkem _RESET_.

{% hint style="info" %}
Systém Tap Tempo je dost chytrý na to, aby poznal, že jste na chvíli přestali klepat, nebo že jste vynechali několik dob. Pokud začnete klepat ve dvojnásobném tempu, pochopí, že chcete tempo zdvojnásobit. Totéž platí, když klepete v polovičním tempu.

Dokáže také rozpoznat, když tempo klepou současně dva lidé najednou (například jeden na klávesnici a druhý na APC40). Liberation dvojité klepnutí zprůměruje.
{% endhint %}

#### Klávesové příkazy:

T - nastavit tempo klepáním\
R - resetovat takt\
Y - zaokrouhlit tempo na nejbližší dobu za minutu.

{% hint style="info" %}
Protože se dnes většina hudby vytváří digitálně, tempo bude pravděpodobně zaokrouhlené celé číslo. Pokud tedy tempo naklepané pomocí Tap Tempo vypadá blízko správné hodnotě, použijte klávesu Y (nebo posuňte knob tempa na APC40 o jeden „krok“) a zaokrouhlete ho na celé číslo.
{% endhint %}

#### Ovládání APC40:

APC40 má vyhrazené tlačítko _TAP TEMPO_, případně můžete použít připojený nožní spínač a klepat tempo nohou!

K úpravě použijte knob _TEMPO_. Pro jemné úpravy podržte při použití knobu _TEMPO_ tlačítko _SHIFT_.

Tlačítkem _METRONOME_ **resetujete takt**. (Tlačítko _METRONOME_ také bliká do rytmu.)

Otočením knobu _TEMPO_ o jeden „krok“ doprava nebo doleva **zaokrouhlíte tempo** nahoru nebo dolů na celé BPM.

Viz také [Referenční příručka APC40](reference/apc40-reference.md)

### Nudge tempo

Pokud jste si jistí, že jste dostatečně blízko skutečnému tempu, ale zjišťujete, že se časově rozjíždíte, použijte k opravě tlačítka _NUDGE_.

Pokud tempo Liberation předbíhá hudbu, podržte _NUDGE -_ a dočasně ho zpomalte, dokud se znovu nesrovná.

Pokud tempo Liberation zaostává za hudbou, podržte _NUDGE +_ a dočasně ho zrychlete, dokud se znovu nesrovná.

{% hint style="info" %}
Můžete použít buď tlačítka NUDGE na obrazovce, nebo vyhrazená tlačítka na APC40.
{% endhint %}

### Poloviční tempo / dvojnásobné tempo

Tlačítky _÷2_ a _x2_ tempo trvale rozpůlíte nebo zdvojnásobíte. Na rozdíl od násobiče tempa jde o trvalou změnu aktuálního tempa.

## Tempo Multiplier

Systém _Tempo Multiplier_ umožňuje dočasně upravit tempo a potom se vrátit k původní hodnotě.

Přepněte _Tempo Multiplier_ stisknutím tlačítka _TEMPO MULTIPLIER_ nebo tlačítka _BANK_ na APC40. Upravujte ho pomocí posuvníku na obrazovce nebo posuvníku A-B na APC40. Případně použijte tlačítka předvoleb _25%, 50%, 100% 200%_.

## Externí zdroje tempa

### MIDI Clock

Chcete-li synchronizovat s externím signálem MIDI clock, vyberte přepínač _MIDI CLOCK_ a v rozevírací nabídce zvolte MIDI zařízení. Všimněte si barevné stavové kontrolky vedle rozevíracích nabídek:

* Zelená – přijímá se signál MIDI clock
* Oranžová – k MIDI zařízení se lze připojit, ale aktuálně není přítomen žádný signál clock
* Červená – k MIDI zařízení se nelze připojit

{% hint style="info" %}
MIDI Clock vysílá řadu rámců (24 na čtvrťovou notu), ale zprávy neobsahují žádná poziční data. To znamená, že pomáhá držet tempo, ale stále může být potřeba resetovat takt.

Zdroj tempa MIDI Clock v Liberation reaguje také na zprávy **MIDI Machine Control (MMC)**, takže pokud je váš zdroj clock vysílá, nebudete muset takt resetovat ručně.
{% endhint %}



### Timeline

Každá timeline má vlastní tempo, které může být pevná hodnota nebo _Tempo Map_. _Tempo Map_ umožňuje upravit tempo v konkrétních časech v rámci timeline.

Tempo timeline se použije, když je jako zdroj tempa vybráno _TIMELINE_.

{% hint style="info" %}
Timeline můžete spustit společně s _jakýmkoli_ zdrojem tempa! Pokud tedy máte živou kapelu, která nehraje podle kliku, můžete timeline spustit ručně a udržovat ji synchronizovanou pomocí zdroje tempa _LIVE_. Nebo pokud máte signál MIDI clock, můžete použít ten!
{% endhint %}
