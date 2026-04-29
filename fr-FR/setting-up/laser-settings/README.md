# ✅ Panneau des paramètres de sortie laser

Ouvrez le panneau de paramètres _Laser output_ avec le menu _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Cela affiche les paramètres du laser actuellement sélectionné, que vous pouvez changer :

* via son bouton numéroté dans le panneau _Laser overview_
* avec une touche numérique de votre clavier : les touches 1 à 0 ouvrent les lasers 1 à 10
* avec la touche `Tab` pour parcourir les lasers (`Shift + Tab` revient en arrière).

En haut de ce panneau, vous verrez :

* un bouton numéroté : cliquez dessus pour armer/désarmer ce laser. Il est rouge lorsque le laser est armé.
* un curseur _Brightness_ uniquement pour ce laser. Notez que ce réglage est combiné avec la luminosité globale.
* un interrupteur _Test Pattern_ et un sélecteur de motif. Cela vous permet de choisir un motif de test spécifique à ce laser uniquement. (Ces contrôles sont repris dans la barre d’outils de la vue Output).

### Orientation de la sortie / correction du miroir

Les éléments suivants servent à corriger la configuration de votre laser afin qu’il se comporte de manière cohérente dans Liberation.

* **Flip horizontal / vertical** : ces options vous permettent de corriger la sortie de votre laser

{% hint style="info" %}
Vous ne devriez pas avoir besoin de modifier les réglages de retournement horizontal / vertical, sauf si votre laser a été câblé de manière incorrecte ou s’il possède des boutons de retournement X/Y à l’arrière qui ne sont pas réglés correctement. Si vous souhaitez retourner la sortie pour un clip particulier, vous pouvez le faire directement sur le clip.
{% endhint %}

* **Orientation** : si votre laser a été installé sur le côté ou à l’envers, vous pouvez corriger la rotation avec ce réglage.
* **Fine position adjustments** : peuvent être utilisés pour corriger de très légers décalages ou rotations. Conçus pour corriger une dérive ou un léger déplacement si un laser est resté en place toute une nuit ou pendant de longues périodes.

{% hint style="info" %}
Notez que les corrections d’orientation / miroir ne changent rien dans le 3D Visualiser. Elles doivent être utilisées pour corriger la sortie du laser réel afin qu’elle corresponde à ce qui est affiché dans le 3D Visualiser !
{% endhint %}

### Copier les paramètres du laser

Voir [Panneau des paramètres de sortie laser](./#copy-laser-settings "mention").

### Paramètres des scanners

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Le réglage de vitesse détermine la rapidité de déplacement des scanners.

{% hint style="danger" %}
Même si les réglages par défaut sont assez prudents, vous pouvez tout de même endommager vos scanners si vous les pilotez trop rapidement. Soyez prudent, en particulier lorsque vous augmentez la vitesse.
{% endhint %}

{% hint style="info" %}
Ce réglage de vitesse ne change pas le débit de points ; il ajuste plutôt l’espacement entre ces points. Pour plus d’informations, consultez [◼️ Comment Liberation génère du contenu laser](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Le faisceau change de couleur et s’allume ou s’éteint pendant que les scanners le déplacent, et ces deux éléments ne sont généralement pas parfaitement synchronisés. Ajustez ce réglage pour les réaligner.

{% hint style="info" %}
Ce réglage est parfois appelé _blank shift_, mais je préfère personnellement le terme _scanner sync_ : il est un peu plus précis, car il ajuste le timing de tous les changements de couleur par rapport au mouvement des scanners.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>« Queues » laser : Colour shift mal réglé</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Aucune « queue » laser ! Colour shift correct !</p></figcaption></figure></div>

Si vous voyez de petites « queues » sur la sortie de votre laser, c’est probablement que la synchronisation des scanners doit être ajustée. Si les queues apparaissent toujours quoi que vous fassiez, vous pilotez probablement vos scanners ou vos drivers laser plus vite qu’ils ne peuvent le supporter. Essayez de réduire la vitesse des scanners.

#### Préréglages des scanners

Utilisez ce réglage pour choisir un paramètre de scanner prédéfini. L’option par défaut convient généralement, vous ne devriez donc pas avoir besoin de modifier ce réglage, sauf si vos scanners sont particulièrement mauvais (ou particulièrement bons). Si vous souhaitez aller plus loin, consultez [◼️ Préréglages de scanner et profils de rendu](../../advanced/scanner-presets.md "mention")

#### Calibration des couleurs

Vous pouvez utiliser ce système pour corriger la courbe de luminosité et la balance des blancs de votre laser. Voir [Étalonnage des couleurs](../../advanced/colour-calibration.md "mention")

#### Paramètres avancés

Vous ne devriez pas avoir besoin de modifier ces réglages, mais si vous êtes curieux, consultez [◼️ Paramètres laser avancés](../../advanced/advanced-laser-settings.md "mention")
