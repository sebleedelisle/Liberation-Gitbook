---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Oscilator Sound input

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Pretvara razinu ulaznog zvuka u vrijednost svojstva.

{% hint style="info" %}
Oscilator Sound input koristi zadano zvučno sučelje, ali ga možete promijeniti u _Preferences_. Otvorite izbornik _Liberation -> Preferences._

U postavkama _Sound Input_ možete odabrati koje zvučno sučelje želite koristiti, zajedno s još nekoliko postavki za prilagodbu razine glasnoće.
{% endhint %}

* **range min / range max** - najmanja i najveća vrijednost na koje se valni oblik mapira
* **channel** - ako vaše zvučno sučelje ima više od jednog ulaznog kanala, ovdje možete odabrati koji kanal preuzimate.

{% hint style="info" %}
Zgodna je tehnika uzeti više zvučnih kanala s miks-pulta; tako možete postaviti da svaki Clip reagira na različit glazbeni instrument.
{% endhint %}

{% hint style="info" %}
Možete koristiti samo jedno zvučno sučelje odjednom za sve _Sound Inputs (_&#x6F;dabrano u panelu _App Settings_). Ako za ovo želite koristiti više od jednog sučelja, na macOS-u možete [izraditi Aggregate Device](https://support.apple.com/en-gb/HT202000) kako biste spojili ulaze u jedan virtualni izvor zvuka. (Postoji mnogo aplikacija za Windows koje također to omogućuju, ali nisam ih isprobao).
{% endhint %}

* **clamp min / clamp max** - upotrijebite ovo za odabir raspona razina na koje želite reagirati. Ovo ne biste trebali morati podešavati ako su postavke gate i limit (u panelu _App Settings_) pravilno namještene, ali mogu se koristiti za neke kreativne efekte.

{% hint style="info" %}
Na gumbu Clip vidjet ćete malu ikonu mikrofona kad god ima oscilator _Sound Input_.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
