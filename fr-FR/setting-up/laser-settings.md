---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Panneau des paramètres de sortie laser

Ouvrez le panneau de paramètres _Laser output_ avec le menu _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Cela affiche les paramètres du laser actuellement sélectionné, que vous pouvez changer :

* via son bouton numéroté dans le panneau _Laser overview_
* avec une touche numérique de votre clavier : les touches 1 à 0 ouvrent les lasers 1 à 10
* avec la touche `Tab` pour passer d’un laser à l’autre (`Shift + Tab` revient en arrière).

En haut de ce panneau, vous trouverez :

* un bouton numéroté : cliquez dessus pour armer/désarmer ce laser. Il est rouge lorsque le laser est armé.
* un curseur _Brightness_ pour ce laser uniquement. Notez que cette valeur est combinée avec la luminosité globale.
* un interrupteur _Test Pattern_ et un sélecteur de mire. Cela vous permet de choisir une mire de test spécifique pour ce laser uniquement. (Ces contrôles sont également présents dans la barre d’outils de la vue Output).

### Correction de l’orientation de la sortie / mise en miroir

Les éléments suivants servent à corriger la configuration de votre laser afin qu’il se comporte de manière cohérente dans Liberation.

* **Flip horizontal / vertical** - ces options vous permettent de corriger la sortie de votre laser

{% hint style="info" %}
Vous ne devriez pas avoir besoin de modifier les paramètres de flip horizontal / vertical, sauf si votre laser a été câblé incorrectement ou si des boutons X/Y flip situés à l’arrière ne sont pas correctement réglés. Si vous souhaitez inverser la sortie pour un clip particulier, cela peut être fait directement sur le clip.
{% endhint %}

* **Orientation** - si votre laser a été accroché sur le côté ou à l’envers, vous pouvez corriger la rotation avec ce paramètre.
* **Fine position adjustments** - peut servir à corriger de très légers décalages ou rotations. Conçu pour compenser une dérive ou un tassement lorsqu’un laser est resté en place toute une nuit ou pendant une longue période.

{% hint style="info" %}
Notez que les corrections d’orientation / mise en miroir ne changent rien dans le 3D Visualiser. Elles doivent être utilisées pour corriger la sortie du laser réel afin qu’elle corresponde à ce qui est affiché dans le 3D Visualiser !
{% endhint %}

### Copier les paramètres du laser

Voir [Panneau des paramètres de sortie laser](laser-settings.md#copy-laser-settings "mention").

### Paramètres des scanners

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Le paramètre Speed détermine la vitesse de déplacement des scanners.

{% hint style="danger" %}
Même si les paramètres par défaut sont assez prudents, vous pouvez tout de même endommager vos scanners si vous les faites fonctionner trop vite. Soyez prudent, en particulier lorsque vous augmentez la vitesse.
{% endhint %}

{% hint style="info" %}
Ce paramètre de vitesse ne change pas le taux de points ; il ajuste plutôt l’espacement de ces points. Pour plus d’informations, consultez [◼️ Comment Liberation génère du contenu laser](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Le faisceau change de couleur et s’allume ou s’éteint pendant que les scanners le déplacent, et ces deux actions ne sont généralement pas parfaitement synchronisées. Ajustez ce paramètre pour les réaligner.

{% hint style="info" %}
On appelle parfois cela _blank shift_, mais je préfère personnellement le terme _scanner sync_ : il est un peu plus précis, car il ajuste le timing de tous les changements de couleur par rapport au mouvement des scanners.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>« Tails » laser - Colour shift mal réglé</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Pas de « tails » laser ! Colour shift correct !</p></figcaption></figure></div>

Si vous voyez de petites « tails » sur la sortie de votre laser, il est probable que le paramètre Scanner sync doive être ajusté. Si ces tails apparaissent toujours quoi qu’il arrive, vous pilotez probablement vos scanners ou pilotes laser plus vite qu’ils ne peuvent le supporter. Essayez de réduire la vitesse des scanners.

#### Scanner presets

Utilisez ce réglage pour choisir un paramètre de scanner prédéfini. L’option par défaut convient généralement, vous ne devriez donc pas avoir besoin de modifier ce paramètre, sauf si vous avez des scanners particulièrement mauvais (ou bons). Si vous voulez aller plus loin, consultez [◼️ Préréglages de scanner et profils de rendu](../advanced/scanner-presets.md "mention")

#### Colour calibration

Vous pouvez utiliser ce système pour corriger la courbe de luminosité et la balance des blancs de votre laser. Voir [Étalonnage des couleurs](../advanced/colour-calibration.md "mention")

#### Advanced settings

Vous ne devriez pas avoir besoin de toucher à ces paramètres, mais si vous êtes curieux, consultez [◼️ Paramètres laser avancés](../advanced/advanced-laser-settings.md "mention")
