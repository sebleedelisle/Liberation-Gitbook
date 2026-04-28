---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Mappage MIDI par défaut pour l’envoi/la réception

**L’activation et la désactivation des Clips sont déclenchées par les messages MIDI note on / off sur les canaux 1 à 14**

Les Clips ont une position horizontale (x) et verticale (y). Faites un clic droit sur un Clip pour voir sa position. Le MIDI peut déclencher les Clips à partir de 0,0.

{% hint style="info" %}
Notez que le contrôle des Clips avec ce système est absolu : les positions des Clips ne changent pas lorsque vous faites défiler le Clip Deck.
{% endhint %}

Le canal MIDI 1, note 1 correspond au Clip 0,0 ; la note 2 au Clip 0,1 ; la note 3 au Clip 0,2, en descendant par lignes puis en avançant par colonnes. Une fois arrivé à 128, le système passe au canal suivant et recommence. Vous disposez donc d’un total de 128 x 14 = 1792 Clips accessibles via MIDI.

Note MIDI pour les coordonnées de Clip :

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Note : 1</td><td>Note : 6</td><td>Note : 11</td><td>Note : 16</td><td>Note : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Note : 2</td><td>Note : 7</td><td>Note : 12</td><td>Note : 17</td><td>...etc</td></tr><tr><td><strong>y : 2</strong></td><td>Note : 3</td><td>Note : 8</td><td>Note : 13</td><td>Note : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Note : 4</td><td>Note : 9</td><td>Note : 14</td><td>Note : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Note : 5</td><td>Note : 10</td><td>Note : 15</td><td>Note : 20</td><td></td></tr></tbody></table>

Notez qu’un événement MIDI note on lance le Clip, et que l’événement note off équivalent l’arrête. Cela s’applique quel que soit le mode de déclenchement du groupe. Le système a été conçu à l’origine pour la lecture et l’enregistrement ; il n’aurait donc pas été souhaitable que les notes basculent simplement l’état d’un Clip.

### **Effets**

Les messages MIDI control change (CC) sur le **canal 15** règlent les effets.\
L’effet 1 utilise les CC 0-3, valeur 0-127\
L’effet 2 utilise les CC 4-7, valeur 0-127\
L’effet 3 utilise les CC 8-11, valeur 0-127\
… et ainsi de suite.

Chaque groupe de quatre contrôles règle le niveau et 3 paramètres de cet effet :

<table><thead><tr><th width="164">Effet :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Niveau</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Paramètre 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...etc</td></tr><tr><td><strong>Paramètre 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Paramètre 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Paramètres globaux**

Les messages MIDI control change sur le **canal 16** modifient les paramètres globaux :\
CC 1 : Shift X (horizontal) 0 -127, 64 est au centre\
CC 2 : Shift Y (vertical) 0 -127, 64 est au centre\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Et surtout :\
CC 15 : Global brightness

Notez que ce système a été conçu à l’origine pour l’enregistrement et la lecture, afin de vous permettre d’utiliser Logic, Ableton ou un autre DAW pour créer des animations sur une timeline. Vous pouvez l’utiliser pour le contrôle en live, mais il n’a pas été optimisé pour cet usage, et certaines fonctions de contrôle live sont absentes par rapport à la configuration APC40.
