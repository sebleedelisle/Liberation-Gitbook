---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

Un réglage _Render Profile_ est disponible dans chaque nœud _Creator_. Il détermine la façon dont les formes sont dessinées, ou _rendues_, par les lasers.

**Dans la plupart des cas, le réglage&#x20;**_**DEFAULT**_**&#x20;convient parfaitement**. Mais si vous travaillez avec des graphismes ou du contenu complexe, vous pouvez avoir besoin de contrôler plus précisément le rendu de chaque forme.

{% hint style="info" %}
Contrairement à la plupart des logiciels laser, Liberation génère un flux de points en temps réel, juste avant de l’envoyer aux contrôleurs laser. Cela permet d’économiser beaucoup d’espace disque : les clips ne pèsent que quelques ko, au lieu de plusieurs Mo de flux de points prérendus.

Cela signifie aussi que vous pouvez adapter le même contenu à différents types de scanners, laser par laser, sans avoir à modifier les clips eux-mêmes.

Pour plus de détails, consultez [◼️ Comment Liberation génère du contenu laser](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

Il existe trois préréglages _Render Profile_ : _DEFAULT_, _FAST_ et _DETAIL._

_**DEFAULT**_ - un bon profil général, adapté à la plupart des utilisations

_**FAST** -_ si votre clip contient beaucoup d’éléments et que certains sont simplement des points ou des lignes droites très simples, cette option peut réduire le scintillement.

_**DETAIL**_ - si vous dessinez quelque chose qui nécessite des angles nets, utilisez cette option. Gardez toutefois à l’esprit que vos scanners se déplaceront plus lentement, ce qui peut rendre la sortie plus scintillante.

{% hint style="info" %}
Dans l’éditeur de clips, vous pouvez attribuer des creators à différents Render Profiles, mais chaque laser traitera ces profils en fonction de ses paramètres de scanner. Consultez [◼️ Préréglages de scanner et profils de rendu](../../advanced/scanner-presets.md "mention")
{% endhint %}
