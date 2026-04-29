---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Clip Editor の概要

Clip Editor は、レーザーコンテンツを作成するための多用途なツールで、Liberation の中核となる機能です。シンプルなものは簡単に作成でき、それでいて非常に高度で複雑なエフェクトにも対応できる柔軟性があります。

{% hint style="info" %}
ノードベースのエディターは、Liberation で最初に作られた部分です。2018年に英国のレーザー関連のミートアップで Rob Stanley と、「オブジェクト指向」のレーザーコンテンツデザイナーとはどのようなものかを話したことがきっかけでした。

一見シンプルに見えますが、実際には構築するのがかなり複雑なシステムです。それでも2019年初めにはコンセプトを実証する動作デモが完成し、そこからこのプロジェクト全体が始まりました。
{% endhint %}

これはノードベースのビジュアルエディター（または [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)）で、TouchDesigner、MaxMSP、VVVV などを使ったことがある方にはなじみのある仕組みです。ただし Clip Editor はベクターグラフィックス専用に設計されているため、少し異なり、ややシンプルになっています。

Clip Editor は、clip button を右クリックして _EDIT CLIP_ を選択すると開けます。または、空の clip button を右クリックして _CREATE AND EDIT CLIP_ を選択します。

### 概要

Clip Editor には次のものが表示されます。

* 上部に並ぶ **Creator** と **Operator node buttons**
* 左側に並ぶ **Oscillator node buttons**
* 右側のパネルに表示されるコンテンツのプレビュー。また、ノードをクリックすると、そのノード自体でのコンテンツを表示する2つ目のプレビューが表示されます。
* 編集中の Clip のすべてのノードと接続（新規 Clip の場合は空です）
* 各種オプションを含む Clip Editor パネル

編集中は、背景の 3D visualiser でも Clip の見た目を確認できます。

{% hint style="info" %}
3D visualiser に出力が表示されない場合は、zone buttons を使って必要な Zone をオンにする必要があるかもしれません。また、_Preview to lasers_ が有効になっていることも確認してください。詳しくは下の [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel "mention") を参照してください。
{% endhint %}

### Clip を作成する

通常は、1つ以上の [creator nodes](creator-nodes.md) から開始し、コンテンツを処理する [Operator nodes](operator-nodes/) を左から右へ接続していきます。Creator や Operator を近づけると、自動的に互いに接続されます。また、離すようにドラッグすると再び切断できます。

### Clip にノードを追加する

上部または左側にある node buttons のいずれかをクリックしてドラッグし、Clip Editor 内の空いている場所に配置します。

### ノードの設定を調整する

ノードの cog icon button（ノード右上）をクリックすると、そのノードの properties panel が開きます。

### ノードを有効／無効にする

ノードの power icon button（ノード左上）をクリックすると、そのノードを有効または無効にできます。無効になったノードは暗く表示され、現在アクティブでないことを示します。Operator が無効になっていてもコンテンツは通過しますが、そのノードはコンテンツに影響を与えません。

### ノード同士を接続する

コンテンツは creator node で作成され、左から右へノードを通って渡されます。各 Operator はコンテンツに何らかの処理を行い、次の Operator へ渡します。パスの最後に残ったものが、その Clip のコンテンツになります。Creator と Operator は、近づけると自動的に接続されます。切り離すには、再び離すようにドラッグします。

{% hint style="info" %}
複数のノードを次のノードの入力に接続できます。これは複数のコンテンツを組み合わせるときに便利です。
{% endhint %}

### ノードのプロパティとソケット

各ノードの下部には複数のソケットが並んでおり、それぞれが brightness、position、scale、rotation など、ノード内のプロパティを表します。

[Oscillatorノード](oscillators/) は下側からこれらのソケットに接続し、設定をアニメーションさせるために使用できます。Oscillator node には上部に出力があります。クリックしてドラッグすると接続を引き出せるので、他のノードの property sockets にドロップします。

### Oscillator nodes

Oscillator nodes は、時間の経過に合わせてプロパティを変化させるために使用します。通常は sawtooth や sine wave などの波形を表しますが、一部の oscillator nodes はマイク入力レベルなどの外部入力をソースとして使用します。

{% hint style="info" %}
アナログシンセを使ったことがある方なら、波形を作ったり、時間の経過に合わせて音を変化させたりするためによく使われる oscillator の概念になじみがあるはずです。Liberation の Oscillator も同じような役割を持っています。

**豆知識:** _Liberation_ という名前は、1980年に発売され、Herbie Hancock、Jean-Michel Jarre、さらには James Brown によって有名になったシンセサイザーの「キーター」、Moog Liberation に着想を得ています。
{% endhint %}

Oscillator には必ず _range_ 設定があり、調整するプロパティの最小値と最大値を制御します。また、_Wave Oscillators_ には必ず _duration_ 設定があり、Oscillator が値を変化させる速さを決定します。詳しくは [Wave oscillators](oscillators/wave-oscillators.md "mention") を参照してください。

### Clip editor panel

* Timer - パネル上部に、進行中の Clip の現在時刻が表示されます
* _RETRIGGER_ - Clip を最初から再開始します。ループしない Clip では特に便利です
* _Preview to lasers_ - これをチェックすると、この Clip の編集中に 3D visualiser が更新されます。オフにすると、エディター外で実行中の Clip が表示されます。これは Clip ごとの設定ではなく、グローバル設定です。
* _UNDO/REDO_ - Clip Editor 自体の取り消し／やり直しです。`Cmd / Ctrl + Z` と `Cmd / Ctrl + Shift + Z` にも割り当てられています。
* _SAVE CLIP_ - 編集内容を保存しますが、上書きについて警告します
* _SAVE AS A COPY_ - Clip Deck 内の次に利用可能なスロットに Clip を保存します。これが Clip の新しい位置となり、以降の保存はすべてこの新しい場所に行われます。
* _EXIT EDITOR_ - Clip Editor を閉じます。未保存の変更がある場合は、確認パネルが表示されます。
