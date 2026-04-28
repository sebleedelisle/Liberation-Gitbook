---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation prend en charge la synchronisation avec un signal de timecode SMPTE/LTC externe, couramment utilisé dans les concerts pour garder les lumières, les pyros, la vidéo et les pistes d’accompagnement synchronisées.

{% hint style="info" %}
Qu’est-ce que SMPTE/LTC ?

SMPTE est une norme de timecode, et LTC correspond à ce timecode converti en signal audio. Si vous écoutez cet audio, cela ressemble à un horrible sifflement aigu, mais pour les ordinateurs, il s’agit d’informations de synchronisation haute résolution.

**Quelques infos pour les curieux !**

Historiquement, SMPTE a été utilisé pour synchroniser la vidéo et l’audio, ou, lors d’une synchronisation avec une bande analogique, une piste pouvait contenir l’audio du timecode enregistré dessus ; on appelait parfois cela le « striping » de la bande. Cette piste de timecode pouvait servir à garder plusieurs magnétophones synchronisés entre eux, ou à synchroniser un séquenceur MIDI avec la bande. (Ainsi, vous n’aviez pas besoin d’enregistrer les instruments MIDI sur bande : le séquenceur pouvait simplement les jouer en direct pendant le mixage !)

SMPTE signifie Society of Motion Picture and Television Engineers, l’organisme qui a défini la norme. LTC signifie _Linear TimeCode._
{% endhint %}

Vous pouvez recevoir un signal de timecode LTC via n’importe quelle interface audio de votre ordinateur, mais il est recommandé d’utiliser une interface professionnelle avec au moins une entrée XLR réglable et une fonction de monitoring.

J’ai eu de bons résultats avec la [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), car elle offre un monitoring au casque, 2 entrées XLR et ne nécessite aucun pilote particulier (au moins sur macOS). Si vous ne comptez l’utiliser que pour le timecode, vous pouvez prendre la [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html), légèrement moins chère (elle ne possède qu’une entrée et pas de MIDI), mais honnêtement, n’importe quelle interface audio correcte devrait fonctionner.

{% hint style="info" %}
Les signaux de timecode LTC sont généralement distribués via des câbles XLR symétriques, car ils sont suffisamment robustes pour transmettre des signaux audio de faible niveau sur de longues distances. (Le XLR est le connecteur cylindrique généralement utilisé avec les microphones.)
{% endhint %}

### Connexions matérielles

Branchez le câble XLR du signal de timecode dans votre interface audio et vérifiez que vous recevez un bon signal. Réglez le niveau sur l’interface audio jusqu’à obtenir un signal fort, mais sans écrêtage. Si votre interface audio dispose d’une sortie casque, vous pouvez écouter le timecode pour vérifier qu’il ne présente pas de coupures et qu’il n’est pas trop bruité.

{% hint style="info" %}
En théorie, il est possible de recevoir le signal via la prise jack de votre MacBook, mais cela nécessiterait un câble personnalisé. Ces prises sont généralement des mini-jacks TRRS 4 pôles, et honnêtement, je ne sais pas lequel de ces connecteurs peut être utilisé comme entrée audio. Je ne suis pas non plus sûr du niveau de tension qu’il peut accepter (j’ai lu quelque part que c’était +/-1V, mais utilisez cette solution à vos risques et périls !)

Je pense qu’il vaut mieux vous procurer une interface audio USB bon marché plutôt que d’essayer cette méthode.
{% endhint %}

Si votre interface audio ne propose aucun type de monitoring d’entrée, vous pouvez vérifier dans les réglages système de macOS (sous _Sound_) que vous recevez bien un signal. (Sous Windows, utilisez le _Sound Control Panel_.)

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS affiche le niveau d’entrée de n’importe quelle interface audio dans le panneau des réglages système Sound</p></figcaption></figure>

### Configuration dans Liberation

1. Sélectionnez votre interface audio et le bon canal d’entrée dans la fenêtre des réglages Timecode.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Notez qu’il existe des options séparées dans le menu déroulant pour chaque canal d’entrée de votre interface audio.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Observez le carré à gauche : si vous recevez un signal de timecode valide, il deviendra vert. Sinon, il restera rouge.

2. Sélectionnez le bon framerate pour le timecode entrant. La personne qui vous fournit le timecode devrait pouvoir vous indiquer le frame rate utilisé. (Si vous vous trompez, la synchronisation fonctionnera quand même, mais vous remarquerez un petit « saut » chaque seconde.)
3. Ouvrez les réglages de timecode de la Timeline à l’aide de la petite icône d’horloge dans la barre de la timeline, puis choisissez l’option SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Ajustez le décalage de départ (en heures, minutes, secondes, frames) pour qu’il corresponde au début du morceau. Si vous avez plusieurs timelines, vous devrez définir ces options séparément pour chacune d’elles.

{% hint style="info" %}
Dans le monde des tournées, il est courant de faire commencer chaque morceau à une heure différente, par exemple 01:00:00:00 pour le premier morceau, 02:00:00:00 pour le deuxième, et ainsi de suite.

Liberation basculera automatiquement vers la timeline correspondant au timecode, vous n’avez donc jamais besoin de changer de timeline manuellement pendant un show.
{% endhint %}

Notez que, contrairement à MIDI Clock et Ableton Link, SMPTE est un système de temps _absolu_, mesuré en heures, minutes, secondes et frames. Le système temporel principal de Liberation est basé sur les beats et les mesures ; lorsque vous recevez du timecode, il utilise donc le tempo défini dans la timeline. Vous devez vous assurer que ce tempo est synchronisé avec la musique également synchronisée au timecode.
