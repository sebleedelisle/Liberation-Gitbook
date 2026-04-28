---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Crée des effets de type « harpe laser », où les notes MIDI entrantes déclenchent des faisceaux ou des formes sur une plage donnée. Le nœud utilise le contenu que vous lui envoyez comme _source_ pour chaque note : envoyez-lui un point, et vous obtiendrez une rangée de points. Envoyez-lui une forme comme un cercle, et vous obtiendrez une rangée de cercles ; les formes plus complexes seront répliquées de la même manière.

Vous pouvez choisir l’interface MIDI que Liberation écoute dans **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **midi channel** – le canal MIDI à écouter (0 = tous les canaux, 1–16 = canal spécifique)
* **width** – largeur totale sur laquelle les notes se répartissent.
* **midi note min / max** – les valeurs de note MIDI la plus basse et la plus haute de la plage.
* **ignore out of range notes** – filtre toutes les notes situées en dehors de la plage définie. Si cette option est désactivée, les notes hors plage sont « limitées » à la note disponible la plus proche (les notes aiguës déclenchent le haut de la plage, les notes graves déclenchent le bas).
* **auto extend range** – élargit automatiquement la plage si des notes sont jouées en dehors de celle-ci.

{% hint style="info" %}
Vous ne savez pas quelle plage de notes vous recevez ? Activez **auto extend range**, réglez **midi note min** sur une valeur très élevée et **midi note max** sur une valeur très basse, puis jouez vos notes. Le système les détectera toutes et étendra la plage pour vous. Une fois toutes les notes capturées, désactivez simplement **auto extend range** pour verrouiller la plage.
{% endhint %}

* **leave all notes visible** – crée des faisceaux ou des formes pour toutes les notes de la plage, qu’elles soient jouées ou non, ce qui donne un effet de « harpe laser ».
* **hit colour** – la couleur qui apparaît lorsqu’une note est déclenchée.
* **hit colour hold time** – durée pendant laquelle la couleur de déclenchement reste à pleine luminosité avant de s’estomper. La valeur est exprimée en secondes (0–1). _100 % = 1 seconde._
* **hit colour decay time** – durée nécessaire pour que la couleur de déclenchement s’estompe après le temps de maintien. La valeur est exprimée en secondes (0–1). _100 % = 1 seconde._

{% hint style="info" %}
Si votre contenu est déjà blanc pur, définir la couleur de déclenchement sur blanc ne changera rien. Pour de meilleurs résultats, utilisez une couleur saturée pour votre contenu et définissez la couleur de déclenchement sur blanc : cela produit un très bel effet de flash lorsque les notes sont déclenchées.
{% endhint %}

* **note off fade out time** – durée nécessaire pour que la note s’estompe après avoir été relâchée. La valeur est exprimée en secondes (0–1). _100 % = 1 seconde._
* **hit scale factor** – facteur d’agrandissement de la note lorsqu’elle est déclenchée (par exemple, 2 = taille doublée).
* **hit scale hold time** – durée pendant laquelle la note reste agrandie avant de revenir à sa taille initiale. La valeur est exprimée en secondes (0–1). _100 % = 1 seconde._
* **hit scale decay time** – durée nécessaire pour que la note revienne à sa taille initiale. La valeur est exprimée en secondes (0–1). _100 % = 1 seconde._
* **note off shrink time** – durée nécessaire pour revenir à la taille initiale après le relâchement de la note. La valeur est exprimée en secondes (0–1). _100 % = 1 seconde._ (N’a aucun effet lorsque **leave all notes visible** est activé.)

{% hint style="info" %}
Mise à l’échelle : notez que si votre contenu est un simple point, la mise à l’échelle n’aura aucun effet !
{% endhint %}
