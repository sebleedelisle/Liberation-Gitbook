---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas-Überblick

Das Canvas-System von Liberation ist relativ einfach, kann am Anfang aber verwirrend wirken. Hier bekommst du einen konzeptionellen Überblick für den Einstieg.

{% hint style="info" %}
**Moment, brauche ich das Canvas-System überhaupt?**

Vielleicht nicht! Wenn du nur eine einzelne Grafik auf einen einzelnen Laser projizierst, kannst du das problemlos mit einer Beam Zone machen. Beachte aber, dass Inhalte in Beam Zones standardmäßig horizontal gespiegelt werden, du musst den Clip also auf der X-Achse spiegeln.

Wenn du grafische Inhalte jedoch auf mehrere Laser verteilen oder in verschiedene Bereiche aufteilen möchtest, um sie auf Architektur zu mappen, dann ist das Canvas-System genau dafür gedacht.
{% endhint %}

### Canvas

Zuerst gibt es den Canvas selbst. Das ist der Bereich, den du in der _CANVAS_-Ansicht siehst. Er stellt eine große, nun ja, Leinwand dar, auf der du Inhalte an beliebigen Stellen platzieren kannst.

### Canvas-Zielbereiche

Diese werden in der Canvas-Ansicht als blaue Umrissrechtecke angezeigt. Es sind Bereiche, an die du Inhalte senden kannst. Du sendest den Inhalt eines Clips an einen Canvas-Zielbereich, ähnlich wie du einen Clip an eine Beam Zone senden würdest. Die Buttons für die Canvas-Zielbereiche findest du im Clip Deck rechts neben den Beam-Zone-Buttons.

{% hint style="info" %}
Wenn du die Canvas-Buttons im Clip Deck nicht sehen kannst, versuche, die Beam-Zone-Buttons mit `Shift + Left / Right Arrow` zu scrollen. Du solltest für jeden Canvas-Zielbereich einen Button mit der Beschriftung _CANVAS 1, CANVAS 2_ usw. sehen.
{% endhint %}

### Canvas Zones

Canvas Zones sind Bereiche innerhalb des Canvas, die du an einen Laser sendest. Sie werden in der Canvas-Ansicht als pinke Umrissrechtecke dargestellt. Du kannst mit der rechten Maustaste auf jede Zone klicken und die Laser auswählen, denen sie zugewiesen werden soll. Wenn du jetzt zur _OUTPUT_-Ansicht dieses Lasers wechselst, siehst du, dass eine neue Zone erschienen ist.

{% hint style="danger" %}
WARNUNG: Wenn der Laser aktiviert ist, könntest du plötzlich Inhalte in einer standardmäßigen Canvas Zone projizieren. Am besten deaktivierst du den Laser, bevor du ihm Canvas Zones zuweist.
{% endhint %}

{% hint style="info" %}
Du kannst eine Canvas Zone auch einem Laser zuweisen, indem du in der _OUTPUT_-Ansicht auf den Button _add canvas zone_ klickst. Siehe [Zonen](../output-view/zones.md "mention").
{% endhint %}

### Guide Images

Du kannst ein Guide Image in den Canvas einfügen und es als Vorlage für deine Grafiken verwenden. Es empfiehlt sich, den Farbton des Guide Image anzupassen (Rechtsklick-Menü) und es abzudunkeln, damit du deine Inhalte darüber besser erkennen kannst.

{% hint style="info" %}
Für Architektur-Mapping hat es sich als hilfreich erwiesen, eine „abgewickelte“ Ansicht des Gebäudes zu erstellen, die alle Flächen des Gebäudes als flaches, unverzerrtes Bild darstellt. Die Perspektivkorrektur für die verschiedenen Bereiche kann dann über die Canvas Zone in der _OUTPUT_-Ansicht erfolgen.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Ein „abgeflachtes“ Guide Image für Saltwell Hall in Gateshead, UK</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Die Canvas Zones in einer sehr frühen Version von Liberation (ca. 2017!). Beachte, dass die pinken Rechtecke auswählen, welcher Teil des Canvas angezeigt wird. Die darunterliegenden Output-Ansichten zeigen dann, auf welchen Bereich des jeweiligen Lasers diese Zonen ausgegeben werden.</p></figcaption></figure>

### Canvas im 3D Visualiser

Es wäre wahrscheinlich ziemlich fummelig (um es vorsichtig auszudrücken), dein komplexes Multi-Laser-Projektionssystem im 3D Visualiser nachzubauen. Stattdessen hast du die Möglichkeit, deinen Canvas im 3D-Raum zu platzieren. Aktiviere die Checkbox _Show canvas_ im Panel _3D visualiser settings_. (Alle Guide Images, die du im Canvas hast, werden ebenfalls im Visualiser angezeigt.)

{% hint style="info" %}
Beachte, dass der Visualiser die Canvas-Projektionen weiterhin als atmosphärische Effekte darstellt, die von den Lasern ausgehen. Du kannst sie entweder einfach aus dem Sichtbereich verschieben oder, wenn du es besonders genau machen möchtest, mit dem Canvas ausrichten.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Es kann extrem befriedigend sein, wenn du die Strahlen des Lasers im 3D Visualiser mit dem Canvas-Bild ausrichtest!</p></figcaption></figure>
