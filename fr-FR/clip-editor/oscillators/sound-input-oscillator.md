---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Oscillateur d’entrée audio

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Convertit le niveau d’entrée audio en une valeur de propriété.

{% hint style="info" %}
L’oscillateur Sound input utilise l’interface audio par défaut, mais vous pouvez la modifier dans _Preferences_. Ouvrez le menu _Liberation -> Preferences._

Dans les paramètres _Sound Input_, vous pouvez sélectionner l’interface audio que vous souhaitez utiliser, ainsi que quelques autres paramètres permettant d’ajuster le niveau de volume.
{% endhint %}

* **range min / range max** - les valeurs minimale et maximale sur lesquelles la forme d’onde est mappée
* **channel** - si votre interface audio possède plusieurs canaux d’entrée, vous pouvez sélectionner ici celui que vous souhaitez capter.

{% hint style="info" %}
Une technique intéressante consiste à récupérer plusieurs flux audio depuis la console de mixage. Vous pouvez ainsi faire réagir différents clips à différents instruments de musique.
{% endhint %}

{% hint style="info" %}
Vous ne pouvez utiliser qu’une seule interface audio à la fois pour tous les _Sound Inputs (_&#x73;électionnée dans le panneau _App Settings_). Si vous souhaitez utiliser plusieurs interfaces pour cela, vous pouvez, sur macOS, [créer un Aggregate Device](https://support.apple.com/en-gb/HT202000) afin de combiner les entrées en une seule source audio virtuelle. (Il existe aussi de nombreuses applications sur Windows qui permettent de le faire, mais je ne les ai pas essayées).
{% endhint %}

* **clamp min / clamp max** - utilisez ces réglages pour choisir la plage de niveaux à laquelle vous souhaitez réagir. Vous ne devriez pas avoir besoin de les ajuster si les paramètres gate et limit (dans le panneau _App Settings_) sont correctement réglés, mais ils peuvent servir à créer certains effets créatifs.

{% hint style="info" %}
Une petite icône de microphone apparaît sur le bouton du clip dès qu’il possède un oscillateur _Sound Input_.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
