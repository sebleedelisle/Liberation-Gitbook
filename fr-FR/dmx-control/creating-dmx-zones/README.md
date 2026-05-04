---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Créer des zones DMX

1. Connectez votre nœud Art-Net et configurez-le dans [connexion à un nœud Art-Net](../connecting-to-an-artnet-node.md "mention").
2. Ouvrez **DMX Zones** et cliquez sur **ADD DMX ZONE**.
3. Réglez les champs **Node**, **Universe** et **Address** de la zone pour qu’ils correspondent à l’appareil.
4. Choisissez un **Preset** pour l’appareil. Le preset définit quels canaux DMX reçoivent des valeurs fixes, des valeurs d’activation/désactivation du contenu, la couleur RGB, la position X/Y, la luminosité ou des entrées DMX Value explicites.
5. Cliquez sur **Edit DMX profile/channel mapping** (icône de curseurs) pour modifier l’affectation des canaux. Le preset par défaut commence avec un canal d’activation/désactivation du contenu et des canaux de couleur RGB.
6. Assignez des Clips à la zone DMX de la même manière que pour des beam zones ou des canvas zones.
7. Appuyez sur **ARM** lorsque vous êtes prêt à ce que la zone envoie du DMX.

{% hint style="warning" %}
Seules les zones DMX armées envoient des valeurs en direct. Les zones DMX non armées remettent leurs canaux affectés à zéro, ce qui est plus sûr lors de la configuration des appareils.
{% endhint %}

La sortie DMX est également limitée par votre niveau de licence. Si le bouton **ARM** est désactivé, vérifiez si votre niveau inclut la sortie DMX ou si le nombre maximal de zones DMX armées a déjà été atteint.
