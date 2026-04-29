---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Attribution des contrôleurs

Une fois les lasers configurés dans Liberation, vous pouvez attribuer chacun d’eux à un contrôleur laser dans le monde réel. (Consultez [Lasers et contrôleurs compatibles (DAC)](../hardware/compatible-lasers-and-controllers-dacs.md "mention") pour vérifier quel matériel vous pouvez utiliser). Les contrôleurs seront connectés soit en USB, soit via le réseau.

* Ouvrez le panneau _Controller Assignment_ depuis le menu _View -> Controller Assignment_. (Vous pouvez également utiliser le bouton _ASSIGN LASER CONTROLLERS_ dans le panneau _Laser Overview_.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment panel"><figcaption></figcaption></figure>

* Le panneau est divisé en deux : la liste des lasers à gauche et la liste des contrôleurs disponibles à droite. Si vous ne voyez pas votre contrôleur laser dans la liste, appuyez sur le bouton _REFRESH_. Si le problème persiste, consultez la section [Dépannage](../troubleshooting/ "mention").
* Pour attribuer un contrôleur à un laser, cliquez-déposez depuis la droite vers un emplacement de laser libre à gauche. Cela indique à Liberation quel contrôleur utiliser pour quel laser. (Si vous changez d’avis, vous pouvez déplacer librement les contrôleurs de haut en bas, d’un laser à un autre.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="List of controllers" width="375"><figcaption></figcaption></figure>

* Si vous voyez un carré vert à côté du contrôleur, cela signifie que Liberation s’y est connecté avec succès.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Un Ether Dream et un DAC Helios attribués respectivement aux lasers 2 et 3</p></figcaption></figure>

{% hint style="info" %}
Notez qu’à chaque connexion à un contrôleur, le laser est automatiquement désarmé.
{% endhint %}

* Un carré orange 🟧 signifie que le contrôleur rencontre des problèmes de connexion intermittents. C’est généralement dû à un problème réseau ; consultez la section [Dépannage](../troubleshooting/ "mention").
* Un carré rouge 🟥 signifie que le contrôleur est injoignable ; consultez la section [Dépannage](../troubleshooting/ "mention").
* Le _bouton de déconnexion_ (X) déconnecte le contrôleur, mais ne le retire pas de l’attribution du laser. Vous pouvez ensuite utiliser le _bouton de reconnexion_ (icône de flèche d’actualisation) pour le reconnecter, ou cliquer de nouveau sur le _bouton de déconnexion_ pour effacer l’attribution.
* _Fonction avancée :_ ouvrez le panneau d’analyse du contrôleur en cliquant sur le bouton qui ressemble à un graphique. Il s’agit d’une fonction avancée qui vous donne des informations détaillées sur le flux de données et peut vous aider à diagnostiquer des problèmes. (Cette option peut ne pas être disponible pour certains types de contrôleurs.)
* Vous pouvez utiliser le _bouton de renommage_ (crayon) pour donner à ce contrôleur le nom de votre choix. Il est préférable de choisir un nom qui permet de l’associer facilement à un matériel précis. S’il est intégré à un laser, vous pouvez le nommer en conséquence, par exemple _LaserCube Ultra #1_ ou _Triton T5 #3._ Ces noms seront enregistrés avec votre installation de Liberation et apparaîtront désormais ainsi ; cela peut être très utile pour identifier rapidement vos lasers.

{% hint style="info" %}
Astuce - faites un **double-clic** sur un contrôleur à droite pour l’attribuer automatiquement au prochain laser disponible à gauche. Cela peut vous faire gagner beaucoup de temps si vous avez de nombreux lasers à attribuer !
{% endhint %}

Vous pouvez utiliser les boutons _DISCONNECT ALL_ et _RECONNECT ALL_ pour réinitialiser rapidement toutes les connexions. C’est utile si vous rencontrez des problèmes réseau.
