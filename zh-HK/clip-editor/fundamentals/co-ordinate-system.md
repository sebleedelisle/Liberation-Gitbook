---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/co-ordinate-system
---

# 🟩 座標系統

Clip 內容使用 x/y 座標系統，原點 (0,0) 位於畫面中央。

* 在水平 x 軸上，左方為負值，右方為正值。
* 在垂直 y 軸上，上方為負值，下方為正值。

Clip 的寬度和高度都是 400 像素，所以可見範圍的座標由 -200 至 200。

{% hint style="info" %}
Clip editor 會建立_向量_圖形。這表示圖形不是以像素儲存，而是以一組座標儲存，用來定義圖形如何繪畫。這類似 Inkscape 或 Illustrator 定義內容的方式，而不是 Photoshop 的方式。
{% endhint %}

### 3D

此外，你可以在 3D 空間中沿 z 軸前後移動。預設情況下，所有內容的 z 位置都是 0。

* 在 z 軸上，向後、遠離你的方向為負值；向前、朝向你的方向為正值。
