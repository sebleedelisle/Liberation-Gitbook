---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Nous sommes tous d’accord : plus il y a de lasers, plus c’est amusant. Mais s’ils font tous exactement la même chose, vous passez à côté de possibilités créatives.

Le système de zone delay est une méthode simple mais efficace pour introduire de la variété entre les zones, et il permet de tirer pleinement parti d’une configuration multi-laser. Il peut aussi servir à créer un effet de chase plus traditionnel.

#### Fonctionnement

Le _Zone delay_ ajoute un délai au timing du clip pour chaque zone, ce qui crée une sorte de balayage entre les zones.

Il est particulièrement efficace d’appliquer un zone delay à un clip déjà en cours de lecture, puis d’utiliser la commande correspondante sur l’APC40 pour ajuster le niveau et le motif. (Voir [Référence APC40](../reference/apc40-reference.md "mention")). Vous pouvez aussi utiliser le panneau _Clip Settings_.

Paramètres de Zone delay :

* **Zone delay** - contrôle la durée du délai appliqué à chaque zone, mesurée en quadruples croches.
* **Pattern** - choisissez l’ordre des zones
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Le pattern fonctionne à partir des numéros de zone et suppose que vos zones sont ordonnées de gauche à droite. Pour calculer les patterns, Zone delay traite les zones Canvas et les zones DMX comme des groupes distincts.
{% endhint %}

* **Delay mode**
  1. No delay - utilisez ce mode en chase mode
  2. Delay - mode par défaut, décale le timing de chaque zone
  3. Delay with re-trigger - réinitialise le clip au début à chaque étape du pattern. Ce mode fonctionne bien avec _Chase mode_.
* **Chase mode** - lorsque chase mode est activé, chaque zone s’allume et s’éteint comme dans un effet de chase traditionnel. Ajustez l’apparence du chase avec les réglages _Fade in, Hold,_ et _Fade out_. Ces réglages sont définis comme une proportion de la valeur _Zone delay_ ; une valeur de 1 correspond donc à la même durée que celle indiquée dans _Zone delay_. Ce n’est pas évident à expliquer, le plus simple est donc d’essayer par vous-même.

{% hint style="info" %}
Zone delay s’applique aussi à tous les effets actifs. Par exemple, un effet de clignotement sera retardé entre les zones, tout comme l’animation à l’intérieur du clip lui-même.
{% endhint %}

Lorsqu’un clip utilise un _Zone delay_, vous verrez une icône à trois points en haut à droite du clip. Ces points sont animés pour vous indiquer le style de _Zone delay_ utilisé par ce clip. Voir [Que signifient les petites icônes sur les boutons de clip ?](what-are-the-small-icons-on-the-clip-buttons.md "mention") pour plus de détails.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Le symbole à trois points qui indique qu’un clip utilise un zone delay, ainsi que son mode</p></figcaption></figure>

{% hint style="info" %}
Zone delay est un réglage propre à chaque clip. Il n’est pas global ; il fait partie de la conception créative d’un clip.
{% endhint %}
