---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 變換

## &#x20;Translate

沿 x、y 及／或 z 軸移動所有內容。請注意，座標系統以中心為原點，x 軸及 y 軸的範圍延伸至 +/-200。請參閱 [座標系統](../fundamentals/co-ordinate-system.md)。

* **x** - 沿 x 軸移動的距離（左 - 右）。
* **y** - 沿 y 軸移動的距離（上 - 下）。

#### 3D 選項（選擇 3D 時可用）

* **z** - 沿 z 軸移動的距離（向螢幕內外的前後方向）。

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

旋轉所有內容。數值以度為單位。請參閱 [座標系統](../fundamentals/co-ordinate-system.md)。

* **rotation** - 內容順時針旋轉的角度（以度為單位）。所有內容都會圍繞原點 (0,0)，即中心點旋轉。
* **pivot point x / pivot point y** - 使用這些數值來偏移旋轉原點。

#### 3D 選項（選擇 3D 時可用）

* **rotation x** - 圍繞 x 軸旋轉（pitch）。
* **rotation y** - 圍繞 y 軸旋轉（yaw）。
* **pivot point z** - z 軸上的旋轉偏移位置。

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

縮放所有內容。

* **scale** - 縮放百分比。
* **scale x / scale y** - 如要水平及／或垂直縮放，請使用這些選項。

{% hint style="warning" %}
每當任何軸縮放至 0% 時，內容都會消失！
{% endhint %}
