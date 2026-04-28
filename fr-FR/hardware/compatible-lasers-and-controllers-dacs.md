---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Lasers et contrôleurs compatibles (DAC)

### Quels lasers sont compatibles avec Liberation ?

Si votre laser dispose d’une entrée ILDA standard, vous pouvez l’utiliser avec Liberation, avec un contrôleur laser compatible comme l’Ether Dream ou le DAC Helios - [voir la liste complète ci-dessous](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Le DAC Helios - l’option la moins chère pour un usage domestique</p></figcaption></figure>

Vous n’avez pas besoin de contrôleur externe ni d’entrée ILDA si :

* Votre laser intègre un Ether Dream, ou ;
* Vous avez un LaserCube de Wicked Lasers, ou ;
* Vous avez un projecteur X-Laser avec Mercury intégré, ou ;
* Vous avez un laser Laser Animation Sollinger avec un contrôleur AVB intégré (actuellement en test sur macOS uniquement)

{% hint style="info" %}
**Qu’est-ce qu’un contrôleur laser ?**

Un contrôleur laser (ou DAC) est un appareil matériel qui reçoit les données numériques de Liberation et les convertit en signaux analogiques nécessaires au pilotage des scanners et de la sortie de votre laser. (D’où DAC : Digital to Analog Converter.)

Le contrôleur se connecte à votre ordinateur par USB ou via un réseau informatique standard ; il peut être externe ou intégré directement dans le laser.

S’il est externe, vous le connectez à votre laser via la connexion ILDA. ILDA est un standard de l’industrie qui utilise un ancien connecteur « D » à 25 broches. Procurez-vous un câble ILDA, branchez une extrémité au contrôleur et l’autre au laser.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>La sortie ILDA sur un Ether Dream externe</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Le panneau arrière d’un laser montrant les différentes connexions, dont l’entrée ILDA</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Un câble ILDA standard</p></figcaption></figure>

### Quel contrôleur me convient le mieux ?

Si vous utilisez le logiciel à la maison, ou si vous réalisez de petits spectacles avec 4 lasers ou moins proches de l’ordinateur, les contrôleurs USB comme le **DAC Helios** sont l’option **la plus abordable**.

Les DAC réseau comme l’**Ether Dream** sont la **meilleure option pour les professionnels** qui sont à l’aise avec la configuration d’un réseau et souhaitent piloter un grand nombre de lasers ; tous les grands spectacles Liberation réalisés jusqu’à présent ont utilisé des Ether Dream.

Si vous avez un **LaserCube**, vous n’avez pas besoin de contrôleur laser séparé : Liberation est compatible avec tous les LaserCube. Les premiers modèles se connectent avec un câble USB, et les modèles plus récents se connectent via un réseau.

Si vous êtes un professionnel à la recherche de l’option la plus simple, envisagez des appareils X-Laser avec Mercury intégré ou des lasers Laser Animation Sollinger utilisant AVB.

### Contrôleurs laser compatibles

#### Ether Dream (réseau)

L’[Ether Dream](https://ether-dream.com) existe depuis plus de dix ans et en est actuellement à la version 4 (même si Liberation fonctionne aussi avec les versions 1, 2 et 3 d’Ether Dream). Ces contrôleurs sont extrêmement fiables.

Vous vous y connectez via un réseau standard. Ils peuvent être achetés sous forme d’unités autonomes, ou mieux encore, être installés à l’intérieur des lasers.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) est la meilleure option pour débuter. Il est moins cher que les Ether Dream, mais comme il se connecte en USB, il n’est pas recommandé pour les grandes longueurs de câble. Vous pouvez aussi rencontrer des problèmes de données USB et de pilotes dès que vous connectez plus de 4 contrôleurs (surtout sous Windows).

Mais si vous voulez simplement piloter quelques lasers chez vous, c’est l’option la moins chère et la plus simple.

#### Mercury (intégré aux appareils X-Laser)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) est le puissant système de contrôle laser DMX de X-Laser, conçu pour les éclairagistes qui veulent piloter des lasers directement depuis une console d’éclairage traditionnelle. Avec la dernière mise à jour du firmware, Mercury inclut également une **émulation Ether Dream**, ce qui signifie qu’il fonctionne désormais parfaitement avec Liberation, ainsi qu’avec tout autre logiciel prenant en charge Ether Dream.

#### AVB (intégré aux appareils Laser Animation Sollinger)

**AVB** est un protocole ouvert basé sur le réseau, destiné au streaming audio et données haute performance à faible latence. De nombreux projecteurs LaserAnimation Sollinger intègrent directement la prise en charge AVB dans le matériel, ce qui permet à Liberation de s’y connecter via le réseau sans DAC externe. La prise en charge d’AVB dans Liberation est actuellement **limitée à macOS et en phase de test**, et nécessite des **appareils réseau compatibles AVB**. Une fois correctement configuré, AVB offre un flux de travail plus simple, moins d’appareils externes et une fiabilité robuste pour les spectacles professionnels. I

#### Contrôleurs qui seront pris en charge à l’avenir :

* [IDN](http://www.ilda-digital.com) (un protocole réseau ouvert d’ILDA, pouvant être implémenté par n’importe quel fabricant)

### Conseils de câblage

Pour des performances optimales, gardez les DAC USB près de votre ordinateur et connectez-les aux lasers avec des câbles ILDA plus longs. (Attention toutefois : les câbles ILDA peuvent se comporter comme un grappin pendant le démontage !)

Si vous utilisez des Ether Dream, vous pouvez également les regrouper et les connecter aux lasers avec de longs câbles ILDA, ou les installer près des lasers et utiliser des câbles réseau plus longs.

La configuration idéale consiste à installer les Ether Dream (ou d’autres contrôleurs) directement à l’intérieur de vos lasers (Rob chez Stanwax Laser peut le faire pour vous au Royaume-Uni)
