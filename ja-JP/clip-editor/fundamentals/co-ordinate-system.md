---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/co-ordinate-system
---

# 🟩 座標系

Clip コンテンツでは、画面の中心を原点 (0,0) とする x/y 座標系を使用します。

* 水平方向の x 軸では、左が負、右が正です。
* 垂直方向の y 軸では、上が負、下が正です。

Clip の幅と高さは 400 ピクセルなので、表示領域の座標範囲は -200 から 200 です。

{% hint style="info" %}
Clip editor は _ベクター_ 形状を作成します。つまり、形状はピクセルとして保存されるのではなく、形状の描画方法を定義する座標の集合として保存されます。これは Photoshop とは異なり、Inkscape や Illustrator がコンテンツを定義する方法に似ています。
{% endhint %}

### 3D

さらに、3D 空間内で z 軸に沿って前後に移動できます。デフォルトでは、すべての z 位置は 0 です。

* z 軸では、自分から遠ざかる後方が負、自分に近づく前方が正です。
