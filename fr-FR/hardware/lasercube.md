---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Image promotionnelle du LaserCube avec l’aimable autorisation de Wicked Lasers</p></figcaption></figure>

Le [LaserCube](https://www.laseros.com/lasercube/) de Wicked Lasers est une unité laser extrêmement compacte, alimentée par batterie, disponible dans plusieurs configurations de puissance. Il est populaire auprès des passionnés grâce à son application pour smartphone facile à utiliser, mais les modèles récents sont suffisamment performants pour être utilisés sur des spectacles professionnels.

L’application mobile (appelée LaserOS, également disponible sur ordinateur) est téléchargeable gratuitement. Elle est très agréable à utiliser et suffisante pour la plupart des utilisateurs. Mais si vous gérez des spectacles plus importants avec plusieurs lasers, vous avez besoin d’un outil plus spécialisé et plus puissant — c’est là que Liberation intervient.

### Connexion à un LaserCube

Les premiers LaserCube sont contrôlés via USB, mais les modèles actuels disposent tous d’un contrôleur réseau intégré. Ces cubes contrôlés par le réseau sont appelés « LaserCube Wifi ». Liberation prend en charge les deux types de LaserCube\*, qu’ils soient connectés en USB ou via un réseau.

\*(La prise en charge du protocole réseau LaserCube a été introduite dans la version 0.7.3)

### LaserCube USB

Connectez votre LaserCube à votre ordinateur avec un câble micro USB, puis recherchez-le dans le panneau _Controller Assignment_ (voir [Attribution des contrôleurs](../setting-up/controller-assignment.md "mention")). S’il n’apparaît pas automatiquement, cliquez sur le bouton _REFRESH_.

### LaserCube réseau « Wifi »

{% hint style="danger" %}
Même si les cubes « Wifi » sont conçus pour fonctionner sur un réseau sans fil, ce n’est pas recommandé : vous risquez d’avoir des coupures et des glitches. Utilisez plutôt la prise RJ45 pour connecter votre LaserCube à un réseau filaire, comme vous le feriez avec des Ether Dreams.
{% endhint %}

Connectez votre LaserCube à votre réseau filaire.

Placez votre LaserCube en mode « LAN Client » et assurez-vous qu’un routeur est présent sur votre réseau. Le LaserCube recevra une adresse IP depuis votre routeur, puis devrait apparaître dans le panneau _Controller Assignment_. (Voir [Attribution des contrôleurs](../setting-up/controller-assignment.md "mention")).

{% hint style="info" %}
Il est possible de configurer un réseau sans routeur et d’attribuer des adresses IP fixes à tous vos appareils ; c’est très courant dans le secteur de l’événementiel. Personnellement, je préfère ajouter un routeur au réseau, et je recommande cette option à toute personne moins expérimentée en réseau.

Le routeur attribue dynamiquement une adresse IP à chaque appareil ; je trouve cela plus simple et moins sujet aux erreurs.
{% endhint %}

{% hint style="danger" %}
Contrairement à l’Ether Dream, _**les LaserCubes NE COUPENT PAS LE FAISCEAU LASER**_ s’ils rencontrent un buffer under-run, un paquet perdu ou d’autres données corrompues / incorrectes.

À la place, ils continuent simplement à partir du dernier point reçu, et dans certains cas cela peut faire passer un faisceau actif dans des zones qui ne sont pas couvertes par les zones définies, ou pire encore, à travers des masques logiciels.

J’échange avec les concepteurs/développeurs de LaserCube et j’espère qu’ils corrigeront ce comportement à l’avenir via une mise à jour du firmware. En attendant, vous devez impérativement masquer physiquement toutes les zones où vous ne voulez pas que le laser puisse aller.

En toute honnêteté, vous devriez probablement le faire dans tous les cas, mais j’utilise moi-même des masques logiciels pour protéger les caméras et les projecteurs. Gardez donc à l’esprit qu’il est plus dangereux de s’appuyer sur cette méthode avec le protocole réseau LaserCube qu’avec l’Ether Dream (qui passe en mode d’arrêt de sécurité dès qu’il détecte une erreur ou des données manquantes).

Je l’ai déjà dit, mais **utilisez une connexion filaire vers votre LaserCube**. Le Wifi ne sera pas suffisant et aggravera encore ce problème.
{% endhint %}
