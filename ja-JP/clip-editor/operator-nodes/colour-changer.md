---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

説明

* **hue, saturation, brightness** - 色の値です。[colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")を参照してください。
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
* **blend** - colour changer をどの程度強く適用するかを指定します。0% はまったく適用せず、100% は完全に適用します。50% は既存の色と新しい値を組み合わせます。
