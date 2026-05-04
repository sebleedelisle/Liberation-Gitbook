---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-zones
---

# 🟩 Canvas zone

Canvas view では、canvas zone はピンク色のアウトラインの長方形として表示されます。Canvas 内の長方形の範囲を選択し、その内容を 1 台または複数のレーザーへ送るために使用します。

ゾーンはマウスでクリックしてドラッグできます。角をドラッグすると、サイズと形状を変更できます。

### 新しい canvas zone を追加する

ツールバーの _Add a new canvas zone_ ボタンをクリックします。

### canvas zone をレーザーに割り当てる

ゾーンを右クリックし、番号ボタンを切り替えて、この canvas zone を割り当てるレーザーを選択します。

{% hint style="danger" %}
警告 - レーザーが armed 状態の場合、デフォルトの canvas zone でコンテンツの投影が突然始まる可能性があります。canvas zone を割り当てる前に、レーザーを disarm しておくことをおすすめします。
{% endhint %}

そのレーザーの _OUTPUT_ view に移動すると、そこに canvas zone が表示されます。これは他の beam zone とまったく同じように編集できます。[ゾーン](../output-view/zones.md "mention") を参照してください。

{% hint style="info" %}
_OUTPUT_ view から直接レーザーに canvas zone を追加することもできます。左側のツールバーにある _Add existing canvas zone_ ボタンをクリックします。
{% endhint %}

### 右クリックメニュー

ゾーンを右クリックすると、この canvas zone の削除、背面への移動、ロックを行うためのオプションが表示されます。
