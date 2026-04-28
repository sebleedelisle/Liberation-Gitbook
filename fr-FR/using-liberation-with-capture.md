---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Utiliser Liberation avec Capture

Liberation prend en charge [Capture](https://capture.se) comme visualiseur externe (à partir de la version 1.0.3). Si vous utilisez déjà Capture dans votre flux de travail, vous pouvez l’utiliser pour visualiser la sortie laser en direct de Liberation dans votre scène 3D.

### Fonctionnement

Aucune procédure de connexion particulière ni liaison manuelle n’est nécessaire.

Tant que :

* Liberation et Capture sont sur le même réseau
* Votre pare-feu autorise la connexion

… tous les lasers que vous avez configurés dans Liberation apparaîtront automatiquement dans Capture comme sources média. Vous n’avez pas besoin de configurer des adresses IP ni d’activer quoi que ce soit de spécial : les sources apparaissent simplement.

### Voir les lasers dans Capture

Tous les lasers configurés dans Liberation apparaîtront dans Capture comme sources média disponibles.

Pour voir réellement la sortie :

* Le laser doit être armé dans Liberation
* La source doit être associée à un projecteur laser dans Capture

Une fois le laser armé, Capture visualisera le flux de sortie en direct provenant de Liberation. Si un laser est désarmé dans Liberation, il restera visible dans Capture comme source, mais il ne produira aucune sortie.

Consultez la documentation sur [capture.se](https://www.capture.se/) pour obtenir plus d’instructions et d’aide sur la configuration des lasers dans Capture. <br>

### Limites de licence et lasers armés

Les connexions Capture sont traitées exactement comme des sorties laser physiques.

Cela signifie que :

* Vous ne pouvez armer qu’autant de lasers que le permet votre niveau de licence
* Seuls les lasers armés enverront activement des données vers Capture

### Ai-je besoin de Capture ?

Pas du tout.

Liberation inclut un 3D Visualiser intégré, toujours disponible et indépendant de votre niveau de licence. Vous pouvez concevoir et prévisualiser des shows directement dans Liberation, sans logiciel externe.

Capture est simplement une option supplémentaire si vous l’utilisez déjà pour l’éclairage ou la conception de shows.

### Dépannage

Si les lasers n’apparaissent pas dans Capture :

* Vérifiez que les deux applications sont sur le même réseau
* Vérifiez les paramètres de votre pare-feu
* Assurez-vous que le laser est armé dans Liberation
