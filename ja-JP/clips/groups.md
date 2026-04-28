---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/groups
---

# 🟩 Clip グループ

各 Clip には色付きのアウトラインがあり、この色はその Clip が属している _group_ を表します。APC40 の Clip ボタンも、対応する group の色で点灯します。

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>シアン</td></tr><tr><td>Group 2</td><td>オレンジ</td></tr><tr><td>Group 3</td><td>赤</td></tr><tr><td>Group 4</td><td>インディゴ</td></tr><tr><td>Group 5</td><td>緑</td></tr></tbody></table>

group システムは非常に柔軟で、次のような使い方ができます。

* ある group の Clip を再生したまま、別の group を切り替える
* group 内のすべての Clip に対して、ゾーンや X/Y 反転を素早く割り当てる
* Clip に _Flash mode_ を設定する（Group 3 はデフォルトで _Flash mode_ に設定されています）
* Clip が継承できるデフォルトのトランジションのイン／アウト時間を設定する、または上書きする

_group_ システムをどう使うかは自由ですが、ゾーンやレーザーの数が多い場合は、レーザーのグループごとに別々の group を使うと便利です。もちろん、使い方は自由です。出発点として、私は通常、各 group を次のように使っています。

<table data-header-hidden><thead><tr><th width="108"></th><th width="121"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>シアン</td><td>最もよく使うビームゾーン用のデフォルト group。</td></tr><tr><td>Group 2</td><td>オレンジ</td><td>レーザービームゾーンのセカンダリ group</td></tr><tr><td>Group 3</td><td>赤</td><td><em>flash</em> mode に割り当て。ライブ演奏用で、通常は素早い光のスタブに使用</td></tr><tr><td>Group 4</td><td>インディゴ</td><td>デフォルトのフェードイン／アウトが遅めの、ゆったりした Clip</td></tr><tr><td>Group 5</td><td>緑</td><td>グラフィック / Canvas Clip</td></tr></tbody></table>

### _Group_ ボタン

_Group_ ボタンは Clip Deck の右側に並んでいます。有効にすると、次の操作ができます。

* Clip を group に割り当てる
* group 内のすべての Clip について、ゾーン設定と X/Y 反転を変更する

_group_ ボタンを有効にするには：

* APC40 の _group_ ボタンを長押しする
* 画面上の _group_ ボタンをマウスでクリックする。もう一度クリックするとオフになります。

_group_ ボタンが有効な状態で Clip を押すと、その Clip を簡単に group に割り当てられます。（別の方法として、Clip の右クリックメニューからも group を割り当てられます）。

### group 内のすべての Clip のゾーン設定を変更する

_group_ ボタンが有効なとき、_zone_ ボタン（BEAM 1 - 8、CANVAS 1 など）は次のように点灯します。

* OFF：このゾーンは、その group 内のどの Clip にも設定されていません
* FLASHING：このゾーンは、group 内の Clip のうち _**一部**_**&#x20;には設定されていますが、&#x20;**_**すべて**_ には設定されていません
* ON：このゾーンは、group 内の _**すべて**_ の Clip に設定されています

ゾーンボタンを押すと、その group 内の _**すべて**_ の Clip で、そのゾーンを有効／無効にできます。

X/Y 反転ボタンにも、まったく同じ考え方が適用されます。
