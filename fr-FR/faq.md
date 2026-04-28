---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Matériel

#### **Liberation fonctionne-t-il sous Windows ?**

Oui - Liberation prend entièrement en charge **Windows 10 et 11 (64 bits)**, avec exactement les mêmes fonctionnalités que la version Mac. Chaque version est publiée simultanément pour les deux plateformes.

#### **Liberation fonctionne-t-il sur Mac ?**

Oui - Liberation prend entièrement en charge **Mac (macOS 12 Monterey et versions ultérieures)**, avec une parité complète des fonctionnalités avec la version Windows. Toutes les mises à jour sont publiées en même temps.

#### **Quelle est la configuration minimale requise ?**

Cela dépend du nombre de lasers que vous souhaitez contrôler. Si vous n’utilisez que quelques lasers, une machine peu puissante suffira. Tous les Mac Apple Silicon fonctionnent très bien et devraient pouvoir contrôler jusqu’à 100 lasers. Si vous exécutez des shows complexes avec des enjeux importants, nous vous recommandons la meilleure machine que vous puissiez vous permettre.

#### **Combien de lasers puis-je contrôler avec Liberation ?**

Liberation peut piloter de nombreux lasers depuis un seul ordinateur ; il a été testé avec plus de 100 contrôleurs laser. La réponse dépend donc de :

* le processeur de votre ordinateur
* la vitesse du réseau
* votre type d’abonnement

#### **Quels contrôleurs MIDI puis-je utiliser ?**

Liberation a été conçu et optimisé autour du célèbre contrôleur MIDI APC40 Mk2. Il fonctionne également avec l’APC40 Mk1. Voir [live-control-with-the-apc40.md](midi-control/live-control-with-the-apc40.md "mention")

Nous ajoutons progressivement d’autres contrôleurs MIDI et prenons actuellement aussi en charge l’APC Mini Mk2 et le MIDI Fighter Twister.

Il existe également le système MIDI Send/Receive, qui offre un contrôle MIDI supplémentaire. Voir [midi-send-receive.md](midi-control/midi-send-receive.md "mention")

Voir [midi-control](midi-control/ "mention") pour plus d’informations.

#### **Puis-je l’utiliser avec n’importe quel contrôleur MIDI ?**

Nous travaillons actuellement sur un système MIDI configurable qui permettra cela à l’avenir. En attendant, certains utilisateurs ont réussi à utiliser un interpréteur MIDI capable de convertir n’importe quels messages MIDI pour le système MIDI Send/Receive, mais il s’agit d’un processus délicat et avancé. Recherchez des conseils sur le [forum](https://forum.liberationlaser.com) à propos de cette configuration, mais en pratique l’APC40 reste la meilleure option.

## Contrôleurs laser

#### **Quels contrôleurs laser sont compatibles avec Liberation ?**

* [Ether Dream (recommended)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (vous devrez peut-être mettre à jour votre firmware)
* LaserCube USB (et LaserDock)
* Protocole réseau LaserCube (avec une connexion filaire)
* AVB tel qu’utilisé par les [lasers LASollinger](https://laseranimation.com/en/) (actuellement en test, macOS uniquement)

Voir [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention") pour plus d’informations

#### **Pourquoi ne prenez-vous pas en charge les contrôleurs laser \[d’une autre marque] ?**

Pour encourager une meilleure interopérabilité entre les logiciels et le matériel, Liberation ne prendra en charge que les DAC dont le protocole de communication est publié. Je pense que c’est la meilleure voie à suivre pour l’industrie du laser.

#### **Comment savoir si mon laser peut être utilisé avec Liberation ?**

Si votre laser possède l’un des éléments suivants, vous pouvez l’utiliser avec Liberation :

* Une **entrée ILDA** externe – un connecteur D 25 broches, utilisé avec un contrôleur externe compatible.
* Un **Ether Dream** installé en interne.
* N’importe quel **LaserCube** (fonctionne avec les LaserCube USB et Wi-Fi).
* Une **unité X-Laser avec système Mercury intégré** (en mode Ether Dream).
* Un **projecteur LaserAnimation Sollinger avec AVB intégré** (macOS uniquement, nécessite des appareils réseau compatibles AVB, actuellement en test).

Voir [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention") pour plus d’informations

#### **Puis-je utiliser Liberation avec mon LaserCube ?**

Oui, Liberation fonctionne directement avec n’importe quel LaserCube. Voir [lasercube.md](hardware/lasercube.md "mention")

## Licences

#### **Quel est le prix d’une licence ?**

Consultez la page [shop](https://liberationlaser.com/shop) pour connaître les prix actuels.

#### **Quelles sont les limitations entre les différents niveaux de licence ?**

Consultez la page [shop](https://liberationlaser.com/shop) pour connaître les options de licence actuelles.

Notez que vous pouvez configurer, prévisualiser et concevoir des shows avec autant de lasers que vous le souhaitez dans **tous** les niveaux, même le niveau gratuit. Il n’y a aucune autre limitation, à part le nombre de lasers que vous pouvez _arm_. Toutes les autres fonctionnalités de Liberation sont disponibles pour tout le monde.

#### **Puis-je passer à un niveau supérieur ?**

Vous pouvez passer à un niveau supérieur à tout moment. Vous recevrez un remboursement partiel pour la durée restante de votre licence actuelle, et votre nouveau plan démarrera immédiatement. Voir [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **Puis-je rétrograder ma licence ?**

Vous pouvez rétrograder à tout moment, mais le changement prendra effet à la fin de votre période de licence actuelle. Voir [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **Comment autoriser mon ordinateur avec ma licence ?**

Une fois que vous avez acheté une licence, vous pouvez autoriser l’ordinateur directement dans le logiciel Liberation. Vous verrez un bouton _Authorise_ sur l’écran _About_, qui vous invitera à vous connecter au site web. Suivez les instructions à l’écran pour terminer le processus d’autorisation. Voir [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **À quelle fréquence dois-je connecter mon ordinateur à Internet ?**

À chaque renouvellement de licence, vous devrez connecter Liberation à Internet pour mettre à jour sa licence interne. Pour un paiement récurrent mensuel, vous devrez vous connecter chaque mois.

#### **Que se passe-t-il si je ne peux pas connecter mon ordinateur à Internet après le renouvellement ?**

Liberation vous accorde une période de grâce de 7 jours après le renouvellement de votre licence pour vous connecter à Internet et mettre à jour sa licence interne. Après cette période, Liberation repassera en mode _Free_.

#### **Que se passe-t-il si ma carte bancaire expire ?**

Vous recevrez une notification par e-mail de notre prestataire de paiement, et vous devrez mettre à jour votre moyen de paiement. Connectez-vous au site web et utilisez le lien _Update payment details_ sur la page des abonnements.

#### **Comment annuler ma licence récurrente ?**

Connectez-vous au site web, ouvrez la page _Your subscriptions_, sélectionnez l’abonnement que vous souhaitez annuler, puis cliquez sur le lien _Cancel Subscription_. Vous pouvez continuer à utiliser Liberation jusqu’à la fin de la période de licence.

#### **Sur combien d’ordinateurs puis-je installer Liberation ?**

Vous pouvez installer Liberation sur autant d’ordinateurs que vous le souhaitez. Les autorisations de licence ne sont nécessaires que pour activer la sortie laser / DMX, et votre niveau de licence détermine combien d’ordinateurs peuvent être autorisés pour la sortie en même temps. Voir [how-licensing-works.md](installation/how-licensing-works.md "mention")

#### **Comment déplacer ma licence d’un ordinateur à un autre ?**

* Ouvrez Liberation sur l’ordinateur que vous ne souhaitez plus utiliser
* Assurez-vous d’être connecté à Internet et cliquez sur le bouton _De-authorise this computer_ sur l’écran _About_
* Ouvrez maintenant Liberation sur le nouvel ordinateur
* Cliquez sur le bouton _Authorise this computer_ sur l’écran _About_.
* Le site web s’ouvrira ; connectez-vous et suivez les instructions à l’écran pour terminer l’autorisation

Vous pouvez également désautoriser à distance un ordinateur auquel vous n’avez plus accès (avec certaines limitations). Voir [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **Puis-je désautoriser Liberation sur un ordinateur perdu ou volé ?**

Vous pouvez désautoriser l’ordinateur via le site web. Si l’installation de Liberation n’a pas été en ligne depuis votre dernier renouvellement, cela peut être fait immédiatement.

Sinon, la désautorisation prendra effet au renouvellement de l’abonnement ou lorsque l’ordinateur se connectera à Internet, selon ce qui se produit en premier. Si vous devez réautoriser un nouvel ordinateur en urgence, contactez le support.

### Utiliser Liberation

#### La configuration par défaut comporte 8 lasers - comment la modifier ?

Voir [setting-up-your-project.md](setting-up/setting-up-your-project.md "mention") et [adding-removing-lasers.md](setting-up/adding-removing-lasers.md "mention")

#### Puis-je copier les réglages de zone d’un laser vers les autres ?

Oui ! Voir [copy-zones-between-lasers.md](output-view/copy-zones-between-lasers.md "mention")

#### Puis-je saisir un nombre au lieu d’utiliser un curseur ?

Oui. `Cmd / Ctrl`-cliquez sur le curseur, puis vous pouvez saisir la valeur au clavier.

#### **Comment synchroniser Liberation avec la musique ?**

Il dispose d’un système intelligent de "tap tempo" qui fonctionne comme vous vous y attendez, mais vous pouvez également utiliser une horloge MIDI externe ou Ableton Link. Voir [tempo-synchronisation.md](tempo-synchronisation.md "mention"). La timeline peut être synchronisée avec un timecode LTC/SMPTE entrant via n’importe quelle interface audio. Voir [timecode.md](timecode.md "mention").

#### Quels réglages dois-je ajuster pour obtenir la meilleure sortie du laser ?

Le réglage principal est _Colour Shift_, qui compense le léger délai entre le mouvement des miroirs et le changement de luminosité des lasers. Si les points/faisceaux de votre laser présentent de petites « traînées », vous devrez l’ajuster. (Voir les photos sur la page [laser-settings.md](setting-up/laser-settings.md "mention") pour un exemple de « traînées »)

Vous pouvez également essayer de modifier la vitesse des scanners : plus lente si vos scanners sont basiques, ou plus rapide s’ils sont de bonne qualité. Mais **utilisez ce réglage avec prudence, car vous pouvez endommager vos scanners si vous les poussez trop fort.**

Il existe aussi quelques préréglages de scanners. L’option par défaut est prudente et convient à la plupart des besoins en faisceaux laser. Mais il existe d’autres préréglages si vous avez de meilleurs scanners, ainsi que des préréglages optimisés pour les graphiques.

Pour plus d’informations, voir [laser-settings.md](setting-up/laser-settings.md "mention"), et pour savoir comment créer vos propres préréglages, voir [scanner-presets.md](advanced/scanner-presets.md "mention") (avancé, en cours)

Vous pouvez également corriger la balance des couleurs avec les réglages _Colour calibration_. Voir [colour-calibration.md](advanced/colour-calibration.md "mention") (technique avancée)

#### À quoi sert le réglage _Latency(ms)_ ?

Il s’agit de la latence d’image, c’est-à-dire le temps maximal entre la génération d’une image et son envoi ultérieur à un laser. Vous ne devriez pas avoir besoin de l’ajuster, mais si vous rencontrez des problèmes réseau, vous pouvez essayer de l’augmenter. Voir [latency-setting.md](setting-up/latency-setting.md "mention") pour plus de détails.

### Clips

#### Comment ajuster les zones et les réglages d’un clip sans l’exécuter ?

`Alt / Option`-cliquez pour en faire le _currently selected clip_, mais sans l’activer. Voir aussi [starting-stopping-clips.md](clips/starting-stopping-clips.md "mention")

#### Comment copier des clips ?

Cliquez et faites glisser en maintenant la touche `Alt / Option` enfoncée. Voir aussi [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### Comment supprimer des clips ?

Cliquez et faites-les glisser hors du Clip Deck. Voir aussi [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### Comment effectuer une sélection multiple, supprimer, combiner des Clip Decks, etc. ?

Voir [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### Que signifient le petit symbole de microphone et les autres icônes sur le clip ?

Ils indiquent qu’un clip utilise une entrée audio ou MIDI, et les 3 points indiquent qu’il y a un délai de zone. Voir [what-are-the-small-icons-on-the-clip-buttons.md](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
