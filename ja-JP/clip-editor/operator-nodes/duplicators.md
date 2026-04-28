---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

すべてのコンテンツのミラー複製を作成します。デフォルトでは、ミラー軸は中央の垂直線です。

* **angle** - ミラー軸のラインの角度です。
* **offset position** - ミラー軸を移動します（軸に対して垂直方向に移動）。
* **delay** - ミラーされたコンテンツの時間遅延です。コンテンツに何らかのアニメーションがある場合にのみ効果があります。

#### 3D options（3D が選択されている場合に使用可能）

* **angle X / angle Y** - ミラー軸が平面になり、これらの設定で 3D 空間内の平面を回転できます。

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

コンテンツを円形パターンで複製します。

* **radius** - 回転前にコンテンツを中心点から移動する距離です。
* **count** - 作成するオブジェクトのコピー数です。
* **use each objects pivot point** - 選択すると、各要素がそれぞれの中心点を基準に移動および回転します。（複数の要素を複製する場合にのみ効果があります）
* **delay** - 複製された各要素に、段階的に長くなる時間遅延を追加します。これが目に見える効果を持つには、コンテンツに何らかのアニメーションが必要です。
* **rotation** - 要素に追加されるオフセット回転です。

#### 3D options（3D が選択されている場合に使用可能）

* **rotation x / rotation y** - 円形パターン全体を x 軸および y 軸を中心に回転します。

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

コンテンツを行と列のグリッドパターンで複製します。

* **spacing** - 要素間の距離です。
* **count X**- 水平方向（列）のコピー数です。
* **count Y**- 垂直方向（行）のコピー数です。
* **horizontal alignment** - 列の開始位置です。LEFT、CENTRE、RIGHT から選択します。
* **vertical alignment** - 行の開始位置です。TOP、MIDDLE、BOTTOM から選択します。
* **delay** - 複製された各要素に、段階的に長くなる時間遅延を追加します。これが目に見える効果を持つには、コンテンツに何らかのアニメーションが必要です。
