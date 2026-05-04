---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ Zones DMX

Les DMX zones sont des zones Output de Liberation qui envoient de l’Art-Net/DMX au lieu de points laser. Elles apparaissent avec les beam zones et les canvas zones, ce qui permet d’y assigner des Clips avec le même sélecteur de zone.

Ouvrez **DMX Zones** depuis le menu, ou utilisez la section DMX dans Laser Overview, pour les gérer.

* **ADD DMX ZONE** - crée une nouvelle DMX zone.
* **ARM** - active la sortie DMX pour cette zone. Une DMX zone non armée remet à zéro les canaux qui lui sont mappés.
* **Node** - sélectionne le numéro du node Art-Net.
* **Universe** - sélectionne l’univers Art-Net. La valeur affichée commence à 1 ; Universe 1 correspond donc au premier univers.
* **Address** - définit l’adresse de départ de l’appareil. La valeur affichée commence également à 1.
* **Preset** - choisit le preset DMX qui mappe le contenu du Clip vers les canaux DMX.
* **Edit DMX zone settings** (icône crayon) - ouvre les réglages de zone, comme le transfert manuel de zone et l’orientation de l’appareil.
* **Edit DMX profile/channel mapping** (icône curseurs) - ouvre l’éditeur de preset/canaux DMX.
* **Delete** - supprime la DMX zone.

### Limites d’activation

Le nombre de DMX zones pouvant être activées en même temps dépend de votre niveau de licence. Si votre niveau n’autorise pas la sortie DMX, ou si vous avez déjà activé le nombre maximal de DMX zones, le bouton **ARM** des zones supplémentaires est désactivé et affiche une icône d’interdiction au survol.

Désactivez une autre DMX zone, ou utilisez un niveau de licence avec une limite DMX plus élevée, avant d’activer d’autres zones.
