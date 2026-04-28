---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

このノードは、ラインやシェイプの内容を等間隔のドットに置き換えます（既存のドットは変更されません）。

* **Colour** – ドットの色です。_Inherit Colour_ が有効な場合は無視されます。下記を参照してください。_関連項目_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – ドット間の距離です。ピクセル単位で指定します。値を小さくするとドットが増え、大きくすると少なくなります。
* **Offset** – ドットの開始位置を、Spacing に対する割合でずらします。アニメーション可能です（例：のこぎり波の Oscillator Node と組み合わせる）。“移動する” ドット効果を作れます。
* **Keep Original** – 有効にすると、元のライン／シェイプを残したまま、その上にドットを描画します。
* **Render Profile** – レンダリング品質を選択します。_参照_ [render-profile.md](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – パスの長さが均等に割り切れるように、Spacing を自動調整します。
* **Fade Out Ends** – パスの始点と終点に向かって、ドットの明るさを徐々に下げます。**Offset** をのこぎり波の Oscillator Node でアニメーションする場合に便利です。ドットがシェイプの端へ移動するとき、滑らかにフェードイン／フェードアウトします。

## &#x20;Trimmer

このノードは、ラインやシェイプの表示される長さをトリミングします。時間の経過に合わせて、表示、非表示、アニメーションさせることができます。

* **Offset** – シェイプの表示部分がどこから始まるかを制御します。_Trim Size_ が 0% の場合でも、Offset を 0% → 100% にアニメーションすると、シェイプが描かれ始め、50% で完全に表示され、その後ふたたび消えていきます。
* **Trim Size** – シェイプ全体の長さに対して、どれだけ残すかを割合で設定します。
* **Loop** – シェイプを連続したループとして扱います。終点で消えるのではなく、終点が始点につながります。
* **All Shapes** – すべての入力シェイプを結合し、1 本のパスとしてトリミングします。オフの場合は、各シェイプが個別にトリミングされます。
* **Add Dot at Start / Add Dot at End** – トリム位置に、選択した色のドットを追加します。（トリムが適用されていない場合、ドットは追加されません。）
* **Colour** – トリムドットの色です。_関連項目_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – ドットに使用する Render Profile を選択します。_参照_ [render-profile.md](../fundamentals/render-profile.md "mention")
