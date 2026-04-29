---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/co-ordinate-system
---

# 🟩 座標系統

Clip 內容使用 x/y 座標系統，原點 (0,0) 位於畫面中央。

* 在水平 x 軸上，左側為負值，右側為正值。
* 在垂直 y 軸上，上方為負值，下方為正值。

Clip 的寬度與高度都是 400 像素，因此可見區域的座標範圍是 -200 到 200。

{% hint style="info" %}
Clip Editor 會建立_向量_形狀。這表示形狀不是以像素儲存，而是以一組座標來定義形狀的繪製方式。這類似於 Inkscape 或 Illustrator 定義內容的方式，而不是 Photoshop 的方式。
{% endhint %}

### 3D

此外，你也可以在 3D 空間中移動，沿著 z 軸向前或向後。預設情況下，所有內容的 z 位置都是 0。

* 在 z 軸上，遠離你的後方為負值，朝向你的前方為正值。
