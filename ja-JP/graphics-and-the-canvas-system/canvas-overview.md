---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas の概要

Liberation の Canvas システムは比較的シンプルですが、最初は少し分かりにくく感じるかもしれません。まずは全体像をつかむための概念的な概要を説明します。

{% hint style="info" %}
**Canvas システムは必要ですか？**

必要ない場合もあります。1 つのグラフィックを 1 台のレーザーに投影するだけなら、beam zone で簡単に実現できます（ただし、デフォルトでは beam zone のコンテンツは水平方向に反転されるため、Clip に X flip を適用する必要があります）。

一方で、グラフィックコンテンツを複数のレーザーに分散したい場合や、建築物にマッピングするために複数のセクションへ分割したい場合は、Canvas システムが役立ちます。
{% endhint %}

### Canvas

まず、Canvas そのものがあります。これは _CANVAS_ view に表示される大きな「キャンバス」で、この領域内の任意の場所にコンテンツを描画できます。

### Canvas target areas

Canvas target area は、Canvas view 内に青い枠線の長方形として表示されます。ここにコンテンツを送信できます。Clip を beam zone に送るのと同じように、Clip のコンテンツを Canvas target area に送ります。Clip Deck では、beam zone ボタンの右側に Canvas target area のボタンが表示されます。

{% hint style="info" %}
Clip Deck に Canvas ボタンが表示されない場合は、`Shift + Left / Right Arrow` で beam zone ボタンをスクロールしてみてください。各 Canvas target area に対応する _CANVAS 1, CANVAS 2_ などのボタンが表示されるはずです。
{% endhint %}

### Canvas zones

Canvas zone は、レーザーへ送信する Canvas 内の領域です。Canvas view では、ピンクの枠線の長方形として表示されます。各 zone を右クリックして、割り当てたいレーザーを選択できます。そのレーザーの _OUTPUT_ view に切り替えると、新しい zone が表示されていることを確認できます。

{% hint style="danger" %}
警告 - レーザーがアーム状態の場合、デフォルトの Canvas zone にコンテンツが突然投影される可能性があります。Canvas zone をレーザーに割り当てる前に、レーザーのアームを解除しておくことをおすすめします。
{% endhint %}

{% hint style="info" %}
_OUTPUT_ view の _add canvas zone_ ボタンをクリックして、Canvas zone をレーザーに割り当てることもできます。[ゾーン](../output-view/zones.md "mention") を参照してください。
{% endhint %}

### Guide images

Canvas に guide image を追加し、グラフィック制作のテンプレートとして使用できます。コンテンツを見やすくするため、guide image の色味（右クリックメニュー）を調整し、暗めにしておくことをおすすめします。

{% hint style="info" %}
建築マッピングでは、建物上のすべての面を、歪みのない平坦な画像として表した「展開図」のビジュアルを作成しておくと便利です。各セクションのパース補正は、_OUTPUT_ view の Canvas zone を使って行えます。
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>英国 Gateshead の Saltwell Hall 用に作成した「平面化」された guide image</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Liberation の初期バージョン（2017 年頃）での Canvas zone。ピンクの長方形で Canvas のどの部分を表示するかを選び、下の Output view でそれらの zone を各レーザーのどの部分へ送るかを示しています。</p></figcaption></figure>

### 3D visualiser 内の Canvas

複雑なマルチレーザー投影システムを 3D visualiser 内で再現するのは、控えめに言ってもかなり手間がかかります。そこで、Canvas を 3D 空間内に配置するオプションが用意されています。_3D visualiser settings_ panel で _Show canvas_ チェックボックスを有効にしてください。（Canvas に追加している guide image も visualiser 内に表示されます。）

{% hint style="info" %}
visualiser では、Canvas への投影もレーザーから出る空間効果として表示されます。単に表示範囲の外へ移動してもよいですし、こだわる場合は Canvas と位置を合わせることもできます。
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>3D visualiser でレーザーのビームと Canvas 画像の位置がぴったり合うと、非常に気持ちよく確認できます。</p></figcaption></figure>
