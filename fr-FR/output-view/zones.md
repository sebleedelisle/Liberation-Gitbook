---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

Le principal type de zone que vous utiliserez pour la plupart de vos projets est la _Beam zone_. Il s’agit d’une zone conçue pour les effets de faisceaux atmosphériques dans l’air. L’autre type de zone est la _Canvas zone_ (voir [Graphiques et système Canvas](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**AVERTISSEMENT - Soyez extrêmement prudent lorsque vous déplacez des zones pendant que le laser fonctionne** et baissez la luminosité au minimum possible. Consultez [Présentation du processus de configuration des lasers](../setting-up/setting-up-lasers.md "mention") pour un guide complet sur l’activation et le zonage des lasers en toute sécurité.
{% endhint %}

Vous pouvez cliquer sur les zones et les faire glisser avec la souris. Activez un motif de test pour voir où cette zone est envoyée.

{% hint style="info" %}
Utilisez les touches fléchées pour **déplacer finement** la zone ou le point actuellement sélectionné. Appuyez sur la touche `Shift` pour déplacer par pas plus grands.
{% endhint %}

{% hint style="info" %}
Astuce : vous pouvez copier rapidement les réglages de zones sur plusieurs lasers ! Voir [Copier les réglages entre lasers](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Ajouter une nouvelle beam zone

Cliquez sur le bouton _Add a new beam zone_ en haut de la barre d’outils : une nouvelle zone apparaît. Notez que les beam zones sont triées dans l’ordre dans lequel vous les ajoutez, mais vous pouvez les réordonner. Voir [Réorganiser les zones de faisceau](re-ordering-beam-zones.md "mention")

### Ajouter une canvas zone existante

Cliquez sur le bouton _Add existing canvas zone_ : vous verrez la liste des canvas zones disponibles et vous pourrez les activer ou les désactiver pour ce laser. Voir [Graphiques et système Canvas](../graphics-and-the-canvas-system/ "mention")

### Types de formes de zone

Il existe 3 types de formes de zone :

* **Quad** - forme de zone rectangulaire par défaut, qui peut être uniforme (alignée sur les axes) ou déformée. Idéale pour les grandes zones rectangulaires ou les canvas zones nécessitant une correction de perspective.
* **Line/Curve** - zone définie par 2 points ou plus et une épaisseur. Idéale pour les zones fines ou pour terminer sur des balcons, des ponts ou d’autres formes courbes.
* **Segmented** - zone pouvant être subdivisée en quads plus petits. Idéale pour le mapping architectural.

Faites un clic droit sur une zone pour ouvrir ses réglages. Depuis ce menu contextuel, vous pouvez :

* Renommer la zone (cela peut aider à l’identifier dans le Clip Deck, surtout si vous avez beaucoup de zones !)
* Activer/désactiver la zone
* Verrouiller sa position
* Modifier son type de forme
* La réinitialiser à la position par défaut
* Accéder aux réglages propres au type de forme
* La supprimer
* Ajouter une _Alt Zone_ (voir [Système de zones Alt](alt-zone-system.md "mention"))

{% hint style="danger" %}
**AVERTISSEMENT -** soyez très prudent lorsque vous changez le type de zone pendant que le laser est actif. La zone revient à la dernière position / taille utilisée pour cette forme, ce qui peut modifier brusquement la sortie. Il est préférable d’éteindre le laser avant de changer le type de zone.
{% endhint %}

### Forme de zone Quad

Vous pouvez déplacer chaque coin du quad avec la souris. Faites `Alt / Option`-clic sur un coin pour le déplacer indépendamment des autres et déformer le quad. Une fois le quad déformé, tous les coins peuvent être déplacés librement.

Vous pouvez supprimer la déformation et revenir à un rectangle aligné sur les axes avec le bouton _REMOVE DISTORTION_ dans le menu contextuel.

#### Correction de perspective

Cette option se règle avec le bouton d’activation dans le menu contextuel et détermine la méthode de déformation. Il est préférable de la laisser désactivée pour les faisceaux, mais si cette zone projette des graphismes sur un plan plat, activez-la pour corriger la perspective de la sortie.

{% hint style="info" %}
Si _Perspective correction_ est désactivé, le contenu est déformé avec une _interpolation bilinéaire_. Autrement dit, le contenu est réparti uniformément dans le quad. C’est pourquoi cette option est préférable pour les faisceaux.

Lorsque la correction de perspective est activée, le contenu est déformé par transformation perspective, ce qui compense le raccourcissement apparent. Ainsi, si vous projetez des graphismes sur un mur avec un angle oblique, vous pouvez utiliser cette option pour redresser la sortie et corriger la déformation de projection.
{% endhint %}

### Forme de zone Line / Curve

La forme de zone Line / Curve est devenue mon option de référence dans les spectacles récents, et on pourrait même considérer qu’elle devrait être le choix par défaut pour les beam zones.

Le plus souvent, mes zones doivent être fines pour s’insérer dans des espaces étroits et peu pratiques sur les lieux, ou entre les fenêtres de bâtiments. J’ai constaté qu’il pouvait être très fastidieux d’ajuster les quatre coins d’un quad lorsqu’ils sont si proches les uns des autres. C’est ainsi qu’est née la zone Line / Curve !

Pour les lignes droites, il suffit de deux points, puis d’ajuster _Zone thickness_ dans le menu contextuel. C’est la méthode la plus rapide pour créer des zones simples.

Faites `Alt / Option`-clic sur la ligne pour créer des points supplémentaires. Ces points sont automatiquement lissés pour créer une forme fluide, et vous pouvez ajuster _Smooth level_ pour éliminer les irrégularités.

Faites `Alt / Option`-clic sur un point pour le supprimer.

Si vous avez l’habitude des applications de graphisme vectoriel (Inkscape, Illustrator, etc.), vous pouvez aussi utiliser l’option _Manually adjust bezier curves_ pour ajuster précisément tous les points de contrôle.

### Forme de zone Segmented

Cette zone subdivisée vous permet d’effectuer des corrections extrêmement détaillées. Elle est utile lorsque vous faites du mapping sur des formes complexes. Vous pouvez ajouter ou supprimer des subdivisions avec les boutons + et - dans le menu contextuel.

### Comment modifier une zone entièrement recouverte par une autre zone

Faites un clic droit sur la zone du dessus, puis cliquez sur le bouton cadenas pour la verrouiller. Vous devriez alors pouvoir modifier et ajuster la zone située en dessous.

<br>

{% hint style="info" %}
Une fois que vous avez ajouté une Beam zone à votre Output, elle pourra être ajoutée à un clip dans le Clip Deck.
{% endhint %}
