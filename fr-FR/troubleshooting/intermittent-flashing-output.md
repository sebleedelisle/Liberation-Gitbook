---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Sortie intermittente / clignotante

Ouvrez le panneau _Laser Overview_ et regardez le voyant de connexion à côté du laser qui pose problème.

**Si le voyant de connexion N’EST PAS vert en continu :**\
Vous avez alors probablement un problème de réseau ou de performances CPU :

**Performances réseau -**

* Assurez-vous que vous n’êtes pas connecté à un réseau Wi-Fi. Vous devez toujours utiliser une connexion filaire. Vérifiez que votre système d’exploitation donne la priorité au réseau filaire plutôt qu’au Wi-Fi, ou désactivez le Wi-Fi si vous n’êtes pas sûr.
* Vérifiez votre adaptateur réseau, et essayez un autre adaptateur USB-C.
* Utilisateurs Windows : vérifiez / mettez à jour vos pilotes réseau, et exécutez les outils de test réseau appropriés.
* Vérifiez tous les câbles, switches et routeurs. Remplacez et testez méthodiquement chaque câble.
* Redémarrez tout votre équipement réseau, y compris les switches, les routeurs et chaque Ether Dream.

**Performances CPU**

Si vous avez une machine ancienne ou peu puissante, elle peut être trop lente pour exécuter Liberation. Vérifiez l’indicateur de fréquence d’images sur le côté droit de la barre d’icônes.

Deux nombres sont affichés : la fréquence d’images réelle et la fréquence d’images cible. Si la fréquence réelle descend sous 30, vous pouvez rencontrer des problèmes.

Les actions suivantes peuvent aider :

* Supprimez les lasers inutilisés, par exemple si vous n’avez qu’un seul laser connecté, supprimez les autres.
* Passez à la vue Output ou Canvas.
* Fermez tous les autres programmes, vérifiez les paramètres du pare-feu réseau, fermez l’antivirus, Dropbox, etc.
* Réduisez la résolution de votre écran et diminuez la taille de la fenêtre Liberation.

Si rien de tout cela ne fonctionne, envisagez de mettre à niveau votre ordinateur.

***

**Si le voyant de connexion EST vert en continu :**

Il s’agit alors probablement d’un problème matériel. Cela sort du cadre de ce manuel, mais vous pouvez essayer les actions suivantes :

* Désactivez le système SFS (Scan Fail Safety). Certains lasers disposent d’une fonction qui désactive la sortie si les scanners cessent de bouger, c’est-à-dire s’ils produisent un faisceau statique puissant. Ces systèmes peuvent être un peu trop prudents / peu fiables.

{% hint style="danger" %}
Soyez extrêmement prudent lorsque vous désactivez le système de sécurité Scan Fail Safety. Les faisceaux statiques puissants peuvent provoquer des brûlures ! Assurez-vous d’avoir un bouton d’arrêt et un extincteur à portée de main.
{% endhint %}

* Vérifiez les câbles et systèmes d’interverrouillage.
* Vérifiez tout le câblage entre le contrôleur et le laser.

Un [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) peut être un outil très utile pour diagnostiquer les problèmes laser.
