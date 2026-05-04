---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Introduction

Le 3D Visualiser de Liberation est une fonction extrêmement utile : vous pouvez concevoir et ajuster vos shows sans avoir besoin du moindre laser ! Il s’est révélé être un outil précieux pour moi, surtout dans les configurations particulièrement complexes avec un grand nombre de lasers.

### Naviguer dans l’espace 3D

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>La vue 3D Visualiser</p></figcaption></figure>

* Cliquez et faites glisser pour faire pivoter la vue autour du point d’orbite
* Utilisez la molette de la souris pour avancer ou reculer par rapport au point d’orbite
* Cliquez et faites glisser tout en maintenant la touche Shift enfoncée pour déplacer la caméra latéralement (strafe) vers la gauche, la droite, le haut et le bas sur le plan XY
* Double-cliquez n’importe où dans le visualiseur pour réinitialiser la position de la caméra

### Settings

Ouvrez le panneau _3D Visualiser Settings_ depuis le menu _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Le panneau 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** - modifie la taille du visualiser par rapport au reste de l’application
* **Brightness Adjustment** - modifie la luminosité apparente des lasers
* **Show laser numbers** - affiche le numéro correspondant au-dessus de chaque laser
* **Show zone names** - affiche les noms de zones correspondants sous chaque laser

### Camera settings

Ces réglages concernent principalement la caméra virtuelle dans l’espace 3D. Un menu déroulant propose des préréglages pour ces réglages, que vous pouvez enregistrer et recharger.

* **Camera distance -** La caméra est toujours orientée vers son _Orbit point_. La distance de caméra correspond à son éloignement par rapport à ce point. Vous pouvez également ajuster ce réglage avec la molette de la souris.
* **FOV -** Champ de vision : détermine si la caméra est en grand angle ou plus zoomée.
* **Orbit position** - décrit la rotation actuelle autour du point d’orbite. La première valeur correspond à la rotation autour de l’axe X (pitch), et la seconde à la rotation autour de l’axe Y (yaw).
* **Orbit centre point** - position du point d’orbite dans l’espace 3D, x, y, z.
* **Grid height** - hauteur de la grille par rapport au « sol » (c’est-à-dire là où y = 0).

### Content settings

Ces réglages déterminent où les lasers (et le Canvas) sont placés dans l’environnement 3D. Un menu déroulant propose des préréglages pour ces réglages, que vous pouvez enregistrer et recharger.

#### Lasers

Chaque laser possède son propre groupe de réglages, que vous pouvez développer avec le petit triangle blanc.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Réglages laser du 3D Visualiser</p></figcaption></figure>

* **3D Position** - position x, y et z du laser.
* **3D Orientation** - rotation du laser autour de chacun des axes x, y et z.
* **Flip X / Flip Y** - inverse la sortie virtuelle du laser. REMARQUE : cela ne devrait pas être nécessaire ; il est préférable d’utiliser les réglages de flip / orientation du laser pour corriger les incohérences éventuelles de votre matériel.
* **Output Range horizontal / vertical** - correspond à l’angle max / min des scanners de votre laser. 60º est la valeur standard, mais vous pouvez l’ajuster si vos lasers sont différents.

#### Canvas

Si vous utilisez le système de canvas, vous pouvez également choisir d’inclure l’image du canvas dans la vue 3D. Activez la case à cocher pour afficher le canvas, puis utilisez les réglages de position, d’orientation et d’échelle pour définir son apparence dans votre vue 3D.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Réglages canvas du 3D Visualiser</p></figcaption></figure>

{% hint style="info" %}
Vous voyez des lasers « fantômes » ? Le 3D Visualiser est relativement indépendant de la configuration laser, et il est possible d’avoir plus de lasers dans le visualiser que dans Liberation. Quand vous ajoutez un laser à votre projet, un nouvel objet laser est également ajouté dans le visualiser. Mais si vous supprimez un laser, un objet laser « fantôme » reste présent dans le visualiser.

Pour supprimer tous les lasers fantômes, cliquez sur le bouton _Remove extra 3D laser objects_ (en bas du panneau de réglages 3D Visualiser).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
