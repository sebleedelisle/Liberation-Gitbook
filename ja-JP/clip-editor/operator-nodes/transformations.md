---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 変形

## &#x20;Translate

すべてのコンテンツを x、y、または z 軸方向に移動します。座標系は中央を原点とし、x 軸と y 軸は +/-200 まで広がります。[座標系](../fundamentals/co-ordinate-system.md "mention") を参照してください。

* **x** - x 軸方向（左 - 右）に移動する距離。
* **y** - y 軸方向（上 - 下）に移動する距離。

#### 3D options（3D が選択されている場合に使用可能）

* **z** - z 軸方向（画面の奥行き方向、手前と奥）に移動する距離。

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

すべてのコンテンツを回転します。値は度数です。[座標系](../fundamentals/co-ordinate-system.md "mention") を参照してください。

* **rotation** - コンテンツを時計回りに回転する角度（度）。すべては原点 (0,0)、つまり中心を軸に回転します。
* **pivot point x / pivot point y** - これらの値を使用して、回転の原点をオフセットします。

#### 3D options（3D が選択されている場合に使用可能）

* **rotation x** - x 軸まわりの回転（ピッチ）。
* **rotation y** - y 軸まわりの回転（ヨー）。
* **pivot point z** - z 軸方向の回転オフセット位置。

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

すべてのコンテンツをスケールします。

* **scale** - スケール率（パーセント）。
* **scale x / scale y** - 水平方向および垂直方向に個別にスケールしたい場合は、これらのオプションを使用します。

{% hint style="warning" %}
いずれかの軸で 0% にスケールすると、そのコンテンツは表示されなくなります。
{% endhint %}
