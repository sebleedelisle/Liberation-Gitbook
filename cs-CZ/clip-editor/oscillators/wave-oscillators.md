---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Vlnové oscilátory

## Na této stránce:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Pilovitá vlna](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Trojúhelníková vlna](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sinusová vlna](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Obdélníková vlna](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Šum](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Vlastní oscilátor](wave-oscillators.md#custom-oscillator-1)

## Nastavení vlnového oscilátoru

Všechny vlnové oscilátory mají tato nastavení:

* **range min / range max** - určuje rozsah hodnot vlastnosti, kterou oscilátor ovládá. Když je průběh vlny dole, vlastnost je nastavena na _range min_. Když je průběh nahoře, vlastnost je nastavena na _range max_.

{% hint style="info" %}
Pokud například chcete, aby se bod pohyboval doleva a doprava mezi hodnotami -100 a 100, připojte oscilátor k _x property socket_, nastavte _min range_ na -100 a _max range_ na 100.
{% endhint %}

* **duration** - doba, za kterou proběhne jeden celý cyklus neboli _smyčka_. Je relativní k tempu v taktech. Hodnota ¼ tedy znamená jednu dobu, 1 celý takt atd.
* **duration multiplier** - násobí základní dobu zvoleným faktorem. Pokud je například duration nastaveno na čtvrťovou notu a multiplier na 3, oscilátor bude trvat tři čtvrťové noty (tečkovanou půlovou notu). Podporované jsou i desetinné násobiče — při tažení posuvníku podržte _SHIFT_ a můžete nastavit necelá čísla, což se hodí pro fázové efekty nebo jemné časové posuny.
* **offset** - počáteční posun vlny jako procento délky duration. Pokud chcete, aby vlna začala ve čtvrtině průběhu, nastavte tuto hodnotu na 25 %.
* **repeat count** - počet opakování smyčky před zastavením. Výchozí hodnota je _FOREVER_, ale můžete ji změnit, pokud nechcete, aby oscilátor běžel donekonečna. Po zastavení se vlastnost nastaví na hodnotu na konci vlny.
* **delay count** - zpoždění v dobách před spuštěním oscilátoru. Než se spustí, vlastnost bude nastavena na hodnotu na začátku vlny.

{% hint style="info" %}
Pečlivým použitím _repeat count_ a _delay count_ můžete vytvářet velmi složité animace, skoro jako vlastní časovou osu!
{% endhint %}

## Společná nastavení

* **steps** - rozdělí pohyb na určitý počet diskrétních kroků. Hodí se, když chcete, aby vlastnosti na hodnoty „skákaly“, místo aby se plynule měnily.

{% hint style="info" %}
Kroky se dělí podle času, ne podle hodnoty. Takže u vlny rozdělené na 4 kroky s duration 1 takt se vlastnost okamžitě změní na každou dobu.
{% endhint %}

* **clamp min / clamp max -** zvětší měřítko vlny za její minimální nebo maximální hodnoty a výsledek omezí.

{% hint style="info" %}
Princip _clamp_ se vysvětluje trochu obtížně, ale představte si, že průběh vlny přesahuje horní nebo dolní okraj grafu a pak se ořízne na jeho hranách. Doporučuji si s těmito hodnotami pohrát! Jsou ale velmi užitečné, když chcete, aby pilovitá vlna začala později nebo skončila dříve.
{% endhint %}

* **ease function** - pilovitá a trojúhelníková vlna mají také funkci easing, která jemně mění animační křivku a dokáže animacím dodat výraz!
  * **LINEAR** - výchozí nastavení, bez easing, jednoduše se lineárně pohybuje mezi minimální a maximální hodnotou.
  * **EASE OUT** - začne rychle a ke konci zpomaluje. Velmi dobré pro simulaci fyziky, například zpomalení až do zastavení.
  * **EASE IN** - začne pomalu a postupně zrychluje. Hodí se pro simulaci nabírání hybnosti.
  * **EASE IN/OUT** - kombinace obou variant, vytváří velmi přirozený pohyb.

{% hint style="warning" %}
**Easing -** výchozí lineární animaci bych používal jen tehdy, když opravdu chcete roboticky působící pohyb. Easing dokáže animace udělat mnohem plynulejší a organičtější!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Pilovitá vlna

Někdy se jí říká také _ramp waveform_, protože stoupá nahoru a na konci cyklu prudce spadne. Je to pravděpodobně nejběžnější vlnový oscilátor, protože vytváří smyčku pro cyklické vlastnosti, jako je _hue_ nebo _rotation_.

Viz výše uvedené části:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Specifické pro pilovitou vlnu:

* **cycle range compensation** - dostupné, když je nastaveno **steps**. Hodí se pro cyklování hodnot, například rotaci od 0 do 360. Když není zapnuté, počáteční a koncová hodnota budou stejné, což může způsobit zaseknutí v počátečním bodě (protože 0 a 360 jsou stejný úhel). Zapněte tuto volbu a maximální rozsah se zmenší tak, aby se opravily pozice kroků.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Trojúhelníková vlna

Na rozdíl od _pilovité vlny_, která se v každém cyklu skokově vrací na začátek, se _trojúhelníková vlna_ pohybuje lineárně dopředu a potom zpět.

Viz výše uvedené části:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sinusová vlna

Nejhladší průběh vlny! Jemně osciluje mezi dvěma hodnotami jako kyvadlo.

Viz výše uvedené části:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Obdélníková vlna

Nejjednodušší průběh vlny - jen přepíná mezi dvěma hodnotami tam a zpět!

Viz výše uvedené části:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Specifické pro obdélníkovou vlnu:

* **pulse width** - doba, po kterou je vlna na maximální hodnotě, vzhledem k celkové duration. Výchozí hodnota je 50 %, tedy přesně půl na půl. Pokud chcete, aby byla „zapnutá“ jen čtvrtinu času, nastavte ji na 25 %. Okamžik, kdy tento puls proběhne, můžete upravit pomocí hodnoty _offset_.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Šum

Jednou ze silných stránek Liberation je, že umí vytvářet náhodné, ale opakovatelné efekty. Oscilátor _noise_ lze použít k vytvoření organického smyčkovaného náhodného pohybu s libovolnou mírou detailu nebo chvění.

Viz výše uvedené části:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Specifické pro šum:

* **noise type** - algoritmus použitý pro generování šumu.
  * **SIMPLEX** - výchozí nastavení, plynule se vlnící hodnota, která stoupá a klesá a opakuje se ve smyčce.
  * **RANDOM** - používá tradičnější algoritmus náhodných čísel, je zcela zašuměný a chaotický.

{% hint style="info" %}
**Simplex noise** navrhl Ken Perlin v roce 2001 jako vylepšení svého algoritmu „Perlin noise“, který vyvinul v roce 1983 při práci na filmu _Tron_ (za kterou získal Oscara!).

Tento takzvaný „gradientní“ šum vznikl z jeho frustrace z dřívější, „strojově“ působící počítačové grafiky. Ve světě CGI se obzvlášť dobře hodí pro vykreslování mraků, vodních hladin nebo i výškových map pro realistický terén.

V Liberation je ale užitečný pro zdánlivě nepředvídatelný pohyb, který přesto zůstává plynulý a organický.
{% endhint %}

* **seed** - hodnota použitá k vytvoření šumu. Pokud se vám vzhled šumové vlny nelíbí, zkuste tuto hodnotu změnit.

{% hint style="info" %}
Zábavný nerdovský fakt! Abych získal dokonale smyčkovaný simplex noise, iteruji po kružnici na 2D rovině šumu. A změna hodnoty seed posouvá tuto rovinu třetím rozměrem!
{% endhint %}

* **simplex detail** - mění míru detailu nebo chvění šumu. Pokud chcete, aby byl opakující se vzor méně zřejmý, zvyšte duration a zároveň i tuto hodnotu.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Vlastní oscilátor

Vytváří zcela vlastní průběhy vlny. Je velmi užitečný pro tvorbu komplexních animací.

Viz výše uvedené části:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Pod tím je seznam pozic a hodnot. Duration je rozdělena na 64 kroků a hodnotu můžete umístit do libovolného z těchto bodů.

Každý krok má tato nastavení:

* **Step** - časový krok v rámci duration. 0 je na začátku a 64 na konci.
* **Level** - úroveň vlny v daném časovém kroku. Level je v rozsahu 0 až 1.
* **Animation type** - rozbalovací nabídka umožňuje zvolit, jak se má z předchozího kroku přejít na tuto úroveň.
  * **None** - bez přechodu, v daném čase rovnou skočí na tuto úroveň.
  * **Linear** - zcela lineární pohyb z předchozí úrovně na tuto.
  * **Ease in / Ease out / Ease in/out** - provede easing mezi předchozí úrovní a touto. Popis typů animace najdete výše v části _ease function_.

***
