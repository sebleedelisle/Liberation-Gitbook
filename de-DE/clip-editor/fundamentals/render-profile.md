---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profile

In jedem _Creator_-Node gibt es die Einstellung _Render Profile_. Sie legt fest, wie die Formen mit den Lasern gezeichnet (oder _gerendert)_ werden.

**Für die meisten Anwendungen ist die Einstellung&#x20;**_**DEFAULT**_**&#x20;völlig ausreichend**. Wenn du jedoch mit Grafiken oder komplexen Inhalten arbeitest, möchtest du vielleicht genauer steuern, wie jede Form gerendert wird.

{% hint style="info" %}
Anders als die meisten Laserprogramme erzeugt Liberation den Punktstrom in Echtzeit, direkt bevor er an die Laser-Controller übergeben wird. Das spart dir viel Speicherplatz: Clips sind nur wenige kB groß, statt MB an vorgerenderten Punktströmen.

Außerdem kannst du denselben Inhalt für unterschiedliche Scanner-Typen pro Laser abstimmen, ohne die Clips selbst ändern zu müssen.

Weitere Details findest du unter [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

Es gibt drei voreingestellte _Render Profiles_: _DEFAULT_, _FAST_ und _DETAIL._

_**DEFAULT**_ – ein gutes allgemeines Profil, das für die meisten Dinge am besten geeignet ist

_**FAST** -_ wenn dein Clip viele Inhalte enthält und ein Teil davon nur aus sehr einfachen Punkten und geraden Linien besteht, kann diese Option das Flimmern reduzieren.

_**DETAIL**_ – wenn du etwas zeichnest, das scharfe Ecken braucht, verwende diese Option. Bedenke aber, dass sich deine Scanner langsamer bewegen und die Ausgabe dadurch stärker flimmern kann.

{% hint style="info" %}
Im Clip-Editor kannst du Creator unterschiedlichen Render Profiles zuweisen. Jeder Laser verarbeitet diese Profile jedoch abhängig von seinen Scanner-Einstellungen. Siehe [scanner-presets.md](../../advanced/scanner-presets.md "mention")
{% endhint %}
