---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Introduction

Liberation intègre un système DMX souple et puissant qui vous permet de créer des effets d’éclairage et de contrôler des lasers compatibles DMX via Art-Net. Il est conçu pour vous aider à garder facilement vos éclairages synchronisés avec votre show laser, sans avoir besoin d’une console lumière séparée.

{% hint style="info" %}
**Qu’est-ce qu’Art-Net, et quel est son lien avec le DMX ?**

**DMX** est un système utilisé depuis des années pour contrôler des projecteurs, lasers, machines à fumée et autres effets de scène. Il envoie des signaux de contrôle via des câbles spécifiques, généralement avec des connecteurs XLR, et chaque appareil écoute un ensemble précis de canaux pour savoir quoi faire.

**Art-Net** est une méthode plus récente qui permet d’envoyer ces mêmes données DMX sur un réseau informatique classique. Au lieu d’utiliser des câbles spécifiques, tout passe par Ethernet, comme le trafic Internet ou réseau local.

Dans Liberation, toute la sortie DMX est envoyée avec Art-Net. Vous pouvez l’utiliser pour contrôler directement des appareils compatibles Art-Net, ou connecter un **nœud Art-Net** : un petit boîtier qui reconvertit l’Art-Net en DMX standard. Vous pouvez ainsi continuer à contrôler des éclairages et effets DMX traditionnels, même s’ils ne prennent pas eux-mêmes en charge Art-Net.
{% endhint %}

Vous pouvez aussi l’utiliser pour contrôler toutes sortes d’équipements de scène, comme des machines à fumée, des hazers, des jets de CO₂, des machines à étincelles froides, et bien plus encore. Si l’appareil prend en charge le DMX, vous pouvez le configurer comme zone DMX et le déclencher directement depuis Liberation, en même temps que votre contenu laser.

Les appareils DMX sont ajoutés en tant que **zones DMX**, qui apparaissent dans la liste des zones avec vos zones de faisceaux laser et vos zones cibles de Canvas. Chaque zone DMX utilise un **préréglage DMX**, qui indique à Liberation comment mapper les propriétés de vos clips laser, comme la position, la couleur et la luminosité, vers les valeurs des canaux DMX.

Lorsque vous envoyez un clip vers une zone DMX, Liberation examine le premier élément du clip et convertit ses propriétés selon le préréglage. Cela permet de piloter simplement des éclairages et des effets DMX directement à partir des mêmes clips que ceux que vous utilisez déjà pour les lasers.

#### Liberation à Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Le premier véritable test du système DMX de Liberation a eu lieu à Glastonbury 2023, où Reach Lasers a installé un total de 90 sources de faisceaux dans le cadre de la scène « spider » d’Arcadia.

18 lasers étaient contrôlés avec des Ether Dreams internes, et 12 barres de faisceaux supplémentaires à 6 têtes étaient contrôlées via Art-Net et DMX.
