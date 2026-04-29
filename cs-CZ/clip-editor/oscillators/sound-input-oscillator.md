---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Oscilátor Sound input

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Převádí úroveň zvukového vstupu na hodnotu vlastnosti.

{% hint style="info" %}
Oscilátor Sound input používá výchozí zvukové rozhraní, ale můžete ho změnit v _Preferences_. Otevřete menu _Liberation -> Preferences._

V nastavení _Sound Input_ můžete vybrat, které zvukové rozhraní chcete používat, a upravit několik dalších nastavení pro nastavení úrovně hlasitosti.
{% endhint %}

* **range min / range max** - minimální a maximální hodnoty, na které se průběh mapuje
* **channel** - pokud má vaše zvukové rozhraní více než jeden vstupní kanál, zde můžete vybrat, který chcete snímat.

{% hint style="info" %}
Zábavná technika je přivést z mixážního pultu více zvukových signálů. Díky tomu mohou různé Clips reagovat na různé hudební nástroje.
{% endhint %}

{% hint style="info" %}
V rámci všech _Sound Inputs_ (vybraných v panelu _App Settings_) můžete současně používat jen jedno zvukové rozhraní. Pokud k tomu chcete použít více než jedno rozhraní, můžete si v macOS [vytvořit Aggregate Device](https://support.apple.com/en-gb/HT202000), který zkombinuje vstupy do jednoho virtuálního zdroje zvuku. (Ve Windows existuje mnoho aplikací, které to také umí, ale nezkoušel jsem je.)
{% endhint %}

* **clamp min / clamp max** - použijte pro výběr rozsahu úrovní, na které chcete reagovat. Pokud jsou nastavení gate a limit (v panelu _App Settings_) správně nastavena, neměli byste to potřebovat upravovat, ale pro některé kreativní efekty se to může hodit.

{% hint style="info" %}
Kdykoli má Clip oscilátor _Sound Input_, uvidíte na jeho tlačítku malou ikonu mikrofonu.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
