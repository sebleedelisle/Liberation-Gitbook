---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 變換

## &#x20;Translate

沿 x、y 和／或 z 軸移動所有內容。請注意，座標系以中心為原點，x 軸與 y 軸的範圍延伸到 +/-200。請參閱[座標系](../fundamentals/co-ordinate-system.md)。

* **x** - 沿 x 軸移動的距離（左 - 右）。
* **y** - 沿 y 軸移動的距離（上 - 下）。

#### 3D 選項（選取 3D 時可用）

* **z** - 沿 z 軸移動的距離（向後與向前進入畫面）。

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

旋轉所有內容。數值以度為單位。請參閱[座標系](../fundamentals/co-ordinate-system.md)。

* **rotation** - 內容順時針旋轉的角度，以度為單位。所有內容都會繞著原點 (0,0)（也就是中心）旋轉。
* **pivot point x / pivot point y** - 使用這些數值來偏移旋轉原點。

#### 3D 選項（選取 3D 時可用）

* **rotation x** - 繞 x 軸旋轉（俯仰）。
* **rotation y** - 繞 y 軸旋轉（偏航）。
* **pivot point z** - z 軸上的旋轉偏移位置。

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

縮放所有內容。

* **scale** - 縮放百分比。
* **scale x / scale y** - 如果想要水平和／或垂直縮放，請使用這些選項。

{% hint style="warning" %}
只要任何軸縮放到 0%，內容就會消失！
{% endhint %}
