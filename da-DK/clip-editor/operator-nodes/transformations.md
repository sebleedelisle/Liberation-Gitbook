---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformationer

## &#x20;Translate

Flytter alt indhold langs x-, y- og/eller z-akserne. Bemærk, at koordinatsystemet er centreret og går til +/-200 på x- og y-akserne. Se [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention").

* **x** - afstanden, der flyttes langs x-aksen (venstre - højre).
* **y** - afstanden, der flyttes langs y-aksen (top - bund).

#### 3D-indstillinger (tilgængelige, når 3D er valgt)

* **z** - afstanden, der flyttes langs z-aksen (ind i og ud af skærmen).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Roterer alt indhold. Værdier angives i grader. Se [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - hvor meget indholdet roteres med uret, angivet i grader. Alt roteres omkring origo (0,0), centrum.
* **pivot point x / pivot point y** - Brug disse værdier til at forskyde rotationsorigo.

#### 3D-indstillinger (tilgængelige, når 3D er valgt)

* **rotation x** - rotation omkring x-aksen (pitch).
* **rotation y** - rotation omkring y-aksen (yaw).
* **pivot point z** - rotationsforskydningens position på z-aksen.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Skalerer alt indhold.

* **scale** - skaleringsprocenten.
* **scale x / scale y** - brug disse indstillinger, hvis du vil skalere vandret og/eller lodret.

{% hint style="warning" %}
Når noget skaleres til 0% på en vilkårlig akse, forsvinder det!
{% endhint %}
