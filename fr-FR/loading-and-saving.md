---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Chargement et enregistrement

Liberation enregistre constamment son état sur le disque. Ainsi, en cas de coupure de courant ou de problème système, il redémarre exactement là où il s’était arrêté : vous ne devriez jamais perdre vos zones, votre timeline ou tout autre contenu.

Vous pouvez toutefois exporter votre configuration pour la sauvegarder ou la transférer vers un autre ordinateur.

### Import / Export de projets

Le fichier Project stocke presque tous les éléments de votre configuration actuelle, notamment :

* Tout ce qui est détaillé dans [Chargement et enregistrement](loading-and-saving.md#laser-settings-import-export "mention") ci-dessous
* Les clips, effets et réglages de groupes
* Toutes vos timelines (hors médias audio et vidéo)
* La configuration Art-Net
* Les réglages d’envoi/réception MIDI
* Les réglages de tempo / synchronisation

Actuellement, il n’enregistre et ne recharge pas :

* Les réglages d’entrée audio et MIDI utilisés dans le node MIDI notes et le Sound Input Oscillator (il enregistre bien les réglages d’envoi/réception MIDI ainsi que l’entrée audio de timecode)
* La mise à l’échelle de l’interface
* Les médias des images guides du Canvas
* Les médias audio et vidéo des timelines
* Les polices utilisées dans le nœud Text

{% hint style="danger" %}
Les fichiers audio et vidéo de la timeline ne sont pas enregistrés avec les fichiers de projet. Veillez donc à les enregistrer séparément si vous voulez les transférer vers un autre ordinateur. Voir [Chargement et enregistrement](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Import / Export des Laser settings

* Les Laser settings de chaque laser
* Les zones de faisceau
* Les zones cibles du Canvas
* Les zones DMX
* L’assignation des contrôleurs laser (ainsi que les alias de tous les contrôleurs que vous avez renommés)
* Les réglages et préréglages de calibration des scanners laser et des couleurs
* Les réglages et préréglages du 3D Visualiser

### Import / Export du Clip Deck

* Tous les clips, ainsi que leurs assignations de zones, réglages et paramètres
* Tous les réglages de groupes, le flash mode, les durées de fade in/out, etc.

Actuellement, il n’enregistre et ne recharge pas :

* Tous les effets, ainsi que leurs paramètres et réglages

{% hint style="info" %}
**Charger les clips d’un fichier de projet sans charger tout le projet**

Pour importer uniquement les clips d’un projet, sélectionnez _**Clips->Import Clip Deck**_, puis choisissez un fichier de projet au lieu de sélectionner un fichier de Clip Deck (.cpdk).
{% endhint %}

### Ajouter un Clip Deck

Vous pouvez ajouter des clips depuis un fichier de Clip Deck exporté à votre projet actuel avec _Append Clip Deck_. Les clips sont ajoutés à la fin de votre Clip Deck actuel, mais les effets et les réglages de groupes contenus dans le fichier ne sont pas importés.

### Exporter les clips sélectionnés

Tous les clips actuellement sélectionnés seront exportés dans un fichier. Les réglages de groupes et les effets ne seront pas enregistrés, seuls les clips le seront. Notez que les clips actifs en cours de lecture ne sont pas exportés, sauf s’ils sont également sélectionnés.

{% hint style="info" %}
Option/Alt - shift - click sur les clips pour les sélectionner (ou utilisez le lasso). Les clips sélectionnés sont reconnaissables à leur épais contour blanc. Voir [Démarrer / arrêter des clips](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Import / Export des effets

Charge et enregistre tous les effets, avec leurs réglages de groupes et paramètres.

{% hint style="info" %}
**Charger les effets d’un fichier de projet sans charger tout le projet**

Pour importer uniquement les effets d’un projet, sélectionnez _**Effects->Import Effects**_, puis choisissez un fichier de projet au lieu de sélectionner un fichier d’effets (.efts).
{% endhint %}

### Export de timeline

Exportez un fichier de timeline contenant une ou plusieurs timelines. Notez que le Clip Deck est toujours inclus dans les fichiers de timeline exportés (même si vous pouvez choisir quels clips réimporter, voir [Chargement et enregistrement](loading-and-saving.md#timeline-import "mention") ci-dessous).

Si votre fichier de projet contient plusieurs timelines, un panneau s’ouvrira pour vous permettre de sélectionner celles que vous voulez exporter.

{% hint style="danger" %}
Les fichiers audio et vidéo de la timeline ne sont pas enregistrés avec les fichiers de timeline. Veillez donc à les enregistrer séparément si vous voulez transférer votre contenu vers un autre ordinateur. Voir [Chargement et enregistrement](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Import de timeline

Importez une ou plusieurs timelines depuis un seul fichier de timeline. Après avoir sélectionné votre fichier de timeline, un panneau s’ouvrira avec plusieurs options d’import.

Si le fichier de timeline contient plusieurs timelines, elles seront toutes listées. Cochez celles que vous voulez inclure.

* Replace existing timelines\
  Supprime toutes vos timelines actuelles et les remplace par celles importées
* Import used clips only\
  Importe uniquement les clips utilisés, et organise les clips en groupes, un pour chaque timeline. Si cette option n’est pas sélectionnée, tout le Clip Deck du fichier de timeline sera ajouté à vos clips existants.
* Replace existing clip deck\
  Remplace votre Clip Deck actuel par les clips du fichier de timeline. Disponible uniquement si _Replace existing timelines_ est sélectionné.

{% hint style="info" %}
**Charger les timelines d’un fichier de projet sans charger tout le projet**

Pour importer uniquement les timelines d’un projet, sélectionnez _**Timeline->Import Timeline(s)**_, puis choisissez un fichier de projet au lieu de sélectionner un fichier de timeline (.ltml).
{% endhint %}

### Import / Export DMX / Art-Net

Enregistre et charge les nœuds Art-Net, avec leurs adresses IP. Inclut également les zones DMX et tous vos préréglages DMX.

### Remarque importante sur les fichiers médias des timelines

Les fichiers audio et vidéo **ne sont pas** actuellement exportés avec le fichier de timeline. Si vous devez déplacer du contenu vers un autre ordinateur, assurez-vous donc de les inclure.

{% hint style="info" %}
**Comment une timeline recherche les fichiers médias**

Lorsque la timeline est chargée, elle recherche dans le même dossier que le fichier de timeline (ou de projet), ainsi que dans ce dossier et tous ses sous-dossiers. Tant que les fichiers se trouvent dans le même dossier ou dans un sous-dossier (comme _/videos_ ou _/sound_), elle les trouvera au chargement.
{% endhint %}
