---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Contrôleurs MIDI en live

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **Contrôleur APC40**

C’est le contrôleur matériel par défaut pour Liberation ; il est fortement recommandé, et on peut dire que Liberation a été conçu autour de ce matériel dès le départ. Dès que vous branchez l’APC40, Liberation s’y connecte automatiquement.

{% hint style="warning" %}
_Oh non ! Ma prise USB s’est débranchée en plein show !_

Pas de panique : rebranchez-la simplement, Liberation se reconnectera automatiquement, sans complication.
{% endhint %}

### APC40 Mark 1 ou Mark 2 ?

En bref, le Mark 2 est recommandé, car ses boutons en couleur correspondent mieux à l’interface Clip Deck de Liberation. La version Mark 1 peut dépanner, mais elle sera un peu plus déroutante : sa disposition diffère légèrement de ce qui est affiché à l’écran, et ses boutons ne peuvent s’allumer qu’en rouge, orange ou vert. Ils ne correspondront donc pas aux couleurs des clips.

{% hint style="info" %}
L’APC40 Mark 1 original est sorti en 2009 (!) et certaines personnes le préfèrent encore pour son châssis métallique et son format robuste de type console. Le Mark 2 mis à jour est sorti en 2014 et, bien qu’il ait été arrêté en 2024, il doit être remis en production en 2025 en raison de la demande des artistes visuels (Resolume, etc.) et des laserists.
{% endhint %}

Pour la liste complète des contrôles disponibles sur l’APC40, consultez [Référence APC40](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 inclut également un profil APC Mini. Il associe la grille de Clips 8x5, les boutons de zone, les contrôles d’inversion X/Y des zones, les boutons de groupe, l’arrêt de tous les Clips, la navigation entre pages de Clips, la navigation entre pages de zones, le tap tempo, la réinitialisation de mesure et l’ajustement fin du tempo. Ses faders contrôlent les niveaux d’effet, et les faders utilisés avec Shift contrôlent les paramètres d’effet. Le dernier fader contrôle Global Brightness.

### MIDI Fighter Twister

Le profil MIDI Fighter Twister est conçu pour un contrôle centré sur les encodeurs plutôt que pour le lancement de Clips. Une rangée d’encodeurs contrôle le paramètre 1 des emplacements d’effet 1 à 8, tandis qu’une autre rangée suit les huit contrôles contextuels du panneau Parameters, notamment le décalage de Clip, le retard de zone, la rotation/mise à l’échelle globale et les fondus de groupe.
