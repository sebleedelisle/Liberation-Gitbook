---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

入力されたすべてのコンテンツの色を変更します。固定の HSB 値を設定することも、グラデーションシステムに切り替えてカスタムグラデーションから色をサンプリングすることもできます。

* **hue, saturation, brightness** - 色の値です。[カラー設定と HSB](../fundamentals/colour-settings-and-hsb.md "mention")を参照してください。
* **hue mode** -
  * OFF - hue は変更されません。
  * FIXED - 要素の hue を hue の値に設定します。
  * SHIFT - 要素の hue を指定した値だけオフセットします。異なる色の要素は異なる色のまま、hue の値に沿ってシフトされます。
* **saturation mode** -
  * OFF - saturation は変更されません。
  * FIXED - saturation を指定した値に固定します。
* **brightness mode** -
  * OFF - brightness は変更されません。
  * FIXED - 要素の brightness を brightness の値に設定します。
  * MULTIPLY - 要素の brightness を brightness の値と組み合わせます。点滅している場合は点滅したままですが、ここで指定した brightness までに制限されます。
* **gradient mode** - 固定の HSB スライダーからグラデーションエディターに切り替えます。この node はグラデーションから 1 色をサンプリングし、上記の色相、彩度、明るさの各モードを使って適用します。
* **gradient position** - グラデーション内のどの位置をサンプリングするかを選択します。Sawtooth Oscillator を使って 0% から 100% までアニメーションさせると、時間とともにグラデーションを循環できます。
* **blend** - colour changer をどの程度強く適用するかを指定します。0% はまったく適用せず、100% は完全に適用します。50% は既存の色と新しい値を組み合わせます。

{% hint style="info" %}
Colour Change node は、入力全体に対してグラデーションから 1 色をサンプリングします。位置に基づいて形状全体にグラデーションを適用したい場合は、代わりに [位置ベースの Changer](position-based-changers.md "mention") を使用してください。
{% endhint %}

### グラデーションエディター

**gradient mode** がオンの場合、メインコントロールの下にグラデーションエディターが表示されます。

* グラデーションバーをクリックすると、カラーストップを追加できます。
* ストップを左クリックして選択し、左右にドラッグして移動します。
* 選択したストップをバーから下方向へドラッグするか、Delete/Backspace を押すと削除できます。グラデーションには常に少なくとも 2 つのストップが保持されます。
* ストップを右クリックすると、カラーピッカーで編集できます。
* 選択したストップを正確に編集するには、**Position**、**Hue**、**Saturation**、**Brightness** を使用します。
* **interpolation** では、ストップ間の色のブレンド方法を選択します。
* **HSB** - 色相、彩度、明るさをブレンドします。カラーホイール上を滑らかに移動する、虹のような動きに最適です。
* **RGB** - 赤、緑、青の値を直接ブレンドします。スクリーンや照明コンソールのカラーフェードに近い見え方になることがよくあります。
* **NONE** - ブレンドせず、1 つのストップから次のストップへ切り替わります。
* **hue direction** は HSB 補間で使用できます。
* **AUTO** - 色相ホイール上で最短経路を取ります。
* **FORWARDS** - 常に色相値を順方向に進みます。
* **BACKWARDS** - 常に色相値を逆方向に進みます。
