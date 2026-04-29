---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas target areas

キャンバスの一部を各レーザー内のゾーンへ送る方法は分かりましたが、そもそもコンテンツをキャンバスに入れるには、（紛らわしいですが正確な名前の）_Canvas target areas_ が必要です。

_Canvas target areas_ は、Clip を描画できるキャンバス上の領域です。_CANVAS_ ビューでは、青いアウトラインの長方形として表示されます。

多くの場合、必要な canvas target area は 1 つだけで、それを複数のゾーンに分割して別々のレーザーへ送る、という使い方で十分です。

また、建物の異なる部分ごとに複数の canvas target areas を使いたい場合や、それらの間で zone delay を活用したい場合もあります。（そうです。zone delay は canvas target areas 間でも機能します！）

### Clip を canvas target areas へ送る

Clip Deck を見ると、beam zone ボタンの横に canvas target area ボタンがあります。表示するには output ボタンをスクロールする必要がある場合があります。`Shift + Left / Right Arrow`、画面上の ZONE PAGE ボタン、または APC40 のボタンを使用してください（[APC40 リファレンス](../reference/apc40-reference.md) を参照）。

beam zone ボタンの場合とまったく同じように、これらのボタンを切り替えて Clip を canvas target areas に割り当てます。

### canvas target areas の追加 / 編集

上部メニューバーで _View -> Canvas Target Areas_ を選択すると、プロジェクト内にある各 canvas target area の設定がすべて表示されます。

上部には _ADD CANVAS TARGET AREA_ ボタンがあります。

canvas target area を削除するには、マイナス記号の付いた赤いボタンを使用します。

サイズと位置はスライダーで調整します。値を入力するには、スライダーをダブルクリックします。

### Scale mode

* **FIT TO AREA** - アスペクト比を維持したまま、コンテンツ全体が canvas target area 内に収まるように縮小します。（これがデフォルト設定です）
* **FILL AREA** - アスペクト比を維持したまま、canvas target area を埋めるようにコンテンツを拡大・縮小します。コンテンツが端で切れる場合があります。
* **STRETCH TO FIT** - アスペクト比を無視して、canvas target area 全体を埋めるようにコンテンツを引き伸ばします。
