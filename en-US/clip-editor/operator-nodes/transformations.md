---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformations

## &#x20;Translate

Moves all content along the x, y, and/or z axes. Note that the coordinate system is centered, and extends to +/-200 in the x and y axes. See [Coordinate system](../fundamentals/co-ordinate-system.md "mention").

* **x** - the distance to move along the x axis (left - right).
* **y** - the distance to move along the y axis (top - bottom).

#### 3D options (available when 3D is selected)

* **z** - the distance to move along the z axis (backwards and forwards into the screen).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Rotates all content. Values are in degrees. See [Coordinate system](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - the amount that the content is rotated clockwise in degrees. Everything is rotated around the origin (0,0), the center.
* **pivot point x / pivot point y** - Use these values to offset the rotation origin.

#### 3D options (available when 3D is selected)

* **rotation x** - rotation around the x axis (pitch).
* **rotation y** - rotation around the y axis (yaw).
* **pivot point z** - rotation offset position in the z axis.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Scales all content.

* **scale** - the scale percentage.
* **scale x / scale y** - if you want to scale horizontally and/or vertically, use these options.

{% hint style="warning" %}
Whenever something is scaled to 0% in any axis, it disappears!
{% endhint %}
