---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformationen

## &#x20;Translate

Verschiebt alle Inhalte entlang der x-, y- und/oder z-Achse. Beachte, dass das Koordinatensystem zentriert ist und sich auf der x- und y-Achse bis +/-200 erstreckt. Siehe [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention").

* **x** - die Distanz, um die entlang der x-Achse verschoben wird (links - rechts).
* **y** - die Distanz, um die entlang der y-Achse verschoben wird (oben - unten).

#### 3D-Optionen (verfügbar, wenn 3D ausgewählt ist)

* **z** - die Distanz, um die entlang der z-Achse verschoben wird (nach hinten und nach vorne in den Bildschirm hinein).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Dreht alle Inhalte. Werte werden in Grad angegeben. Siehe [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - der Betrag, um den der Inhalt im Uhrzeigersinn gedreht wird, in Grad. Alles wird um den Ursprung (0,0), also die Mitte, gedreht.
* **pivot point x / pivot point y** - Verwende diese Werte, um den Ursprung der Drehung zu verschieben.

#### 3D-Optionen (verfügbar, wenn 3D ausgewählt ist)

* **rotation x** - Drehung um die x-Achse (Pitch).
* **rotation y** - Drehung um die y-Achse (Yaw).
* **pivot point z** - Versatzposition der Drehung auf der z-Achse.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Skaliert alle Inhalte.

* **scale** - der Skalierungsprozentsatz.
* **scale x / scale y** - wenn du horizontal und/oder vertikal skalieren möchtest, verwende diese Optionen.

{% hint style="warning" %}
Wenn etwas auf einer Achse auf 0 % skaliert wird, verschwindet es!
{% endhint %}
