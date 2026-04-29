---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformasjoner

## &#x20;Translate

Flytter alt innhold langs x-, y- og/eller z-aksen. Merk at koordinatsystemet er sentrert, og strekker seg til +/-200 på x- og y-aksen. Se [Koordinatsystem](../fundamentals/co-ordinate-system.md "mention").

* **x** - avstanden som skal flyttes langs x-aksen (venstre - høyre).
* **y** - avstanden som skal flyttes langs y-aksen (topp - bunn).

#### 3D-alternativer (tilgjengelig når 3D er valgt)

* **z** - avstanden som skal flyttes langs z-aksen (bakover og fremover inn i skjermen).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Roterer alt innhold. Verdier er i grader. Se [Koordinatsystem](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - hvor mye innholdet roteres med klokken, i grader. Alt roteres rundt origo (0,0), sentrum.
* **pivot point x / pivot point y** - Bruk disse verdiene til å forskyve rotasjonens origo.

#### 3D-alternativer (tilgjengelig når 3D er valgt)

* **rotation x** - rotasjon rundt x-aksen (pitch).
* **rotation y** - rotasjon rundt y-aksen (yaw).
* **pivot point z** - forskyvningsposisjon for rotasjon langs z-aksen.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Skalerer alt innhold.

* **scale** - skaleringsprosenten.
* **scale x / scale y** - hvis du vil skalere horisontalt og/eller vertikalt, bruker du disse alternativene.

{% hint style="warning" %}
Når noe skaleres til 0 % på en akse, forsvinner det!
{% endhint %}
