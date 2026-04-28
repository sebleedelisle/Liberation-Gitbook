---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input -oskillaattori

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Muuntaa äänitulon tason ominaisuuden arvoksi.

{% hint style="info" %}
Sound input -oskillaattori käyttää oletusääniliitäntää, mutta voit vaihtaa sen _Preferences_-asetuksissa. Avaa valikko _Liberation -> Preferences._

_Sound Input_ -asetuksissa voit valita käytettävän ääniliitännän sekä säätää muutamia äänenvoimakkuuteen liittyviä asetuksia.
{% endhint %}

* **range min / range max** - pienin ja suurin arvo, joille aaltomuoto skaalataan
* **channel** - jos ääniliitännässä on useampi kuin yksi tulokanava, voit valita tästä, mitä kanavaa käytetään.

{% hint style="info" %}
Miksauspöydästä kannattaa kokeilla ottaa useita äänisyöttöjä. Näin eri Clipit voivat reagoida eri soittimiin.
{% endhint %}

{% hint style="info" %}
Voit käyttää kaikissa _Sound Inputs_ -kohteissa vain yhtä ääniliitäntää kerrallaan (valitaan _App Settings_ -paneelissa). Jos haluat käyttää tähän useampaa kuin yhtä liitäntää, macOS:ssä voit [luoda Aggregate Device -laitteen](https://support.apple.com/en-gb/HT202000), jolla tulot yhdistetään yhdeksi virtuaaliseksi äänilähteeksi. (Windowsille on myös paljon sovelluksia, jotka tekevät saman, mutta en ole itse kokeillut niitä.)
{% endhint %}

* **clamp min / clamp max** - valitse tällä, mihin tasoalueeseen haluat reagoida. Tätä ei yleensä tarvitse säätää, jos gate- ja limit-asetukset (_App Settings_ -paneelissa) on säädetty oikein, mutta asetuksia voi käyttää myös luoviin tehosteisiin.

{% hint style="info" %}
Clip-painikkeessa näkyy pieni mikrofonikuvake aina, kun siinä on _Sound Input_ -oskillaattori.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
