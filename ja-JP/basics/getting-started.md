# ✅ クイックスタートガイド

## はじめに

**Liberation** へようこそ。Liberation は次世代のレーザーショーソフトウェアです。

Liberation は高機能で複雑な現代的ソフトウェアですが、使いやすさと信頼性を基本に設計されており、創造性を自由に表現できます。高速で効率的、そしてスムーズに動作します。この _クイックスタートガイド_ に沿って、すぐに使い始めましょう。

### レーザーの管理

Liberation は柔軟に設計されているため、実際のレーザーが接続されていなくても、レーザーを設定して視覚化できます。準備ができたら、各出力をレーザーコントローラーにスムーズに割り当てられます。

{% hint style="info" %}
Liberation 内では、必要な数だけレーザーを設定して視覚化できます。ライセンスの種類（Hobbyist、Pro など）で制限されるのは、_arm_ できるレーザーの数だけです。つまり、無料ライセンスでも 100 台のレーザーを使ったショーを設計できます。実際のレーザーで動かす段階になったときにのみ、アップグレードが必要です。
{% endhint %}

デフォルトでは 8 台のレーザーが横方向に並んでいますが、必要に応じて自由にカスタマイズできます。ソフトウェアに慣れるまでは、このデフォルトのままにしておくのがよいでしょう。その後、実際のハードウェア構成に合わせて調整できます。（[setting-up-your-project.md](../setting-up/setting-up-your-project.md "mention") を参照）&#x20;

{% hint style="warning" %}
重要：レーザーを arm する前に、必ず関連するリスクを理解し、[setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention") の章を慎重に確認してください。
{% endhint %}

## ソフトウェアの概要

### 安全停止

レーザーを運用するときは、必ず **ハードウェア非常停止ボタン** を手元に用意してください（[emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md "mention") を参照）。緊急度が低い状況で全体を disarm したい場合は、_**DISARM ALL**_ ボタン、`Escape` キー、または APC40 の _**SESSION**_ キーを使用できます。画面上のスライダー、または APC40 のメインフェーダーでグローバル輝度を下げることもできます。

### スライダー要素

Liberation 全体には、さまざまなスライダーやコントロールがあります。

{% hint style="info" %}
スライダーだけでは細かく調整しきれない場合は、スライダーを `Cmd / Ctrl`-クリックすると新しい値を入力できます。
{% endhint %}

### キーボードショートカット

キーボードショートカットの一覧はこちらにあります：[keyboard-shortcuts.md](../reference/keyboard-shortcuts.md "mention")

### 画面レイアウト

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
特定のボタンの機能がわからない場合は、マウスカーソルを重ねると説明が表示されます。
{% endhint %}

#### メニュー

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

メニューには、すべてのファイルのインポート／エクスポートオプションと、各パネルを開く項目があります。サブスクリプションでこのコンピューターを認証するための項目もここにあります（_Liberation -> Authorise/Deauthorise this computer_）。

#### アイコンバー

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

ここには、すべてのレーザーの arm／disarm、グローバル輝度、テストパターン、3D、Canvas、Output ビューの切り替えなど、よく使う操作があります。

### ビュー

画面左上の大きなエリアは、主に **3D**、**CANVAS**、**OUTPUT** の 3 つのビューのいずれかになります。アイコンバーのボタンで切り替えます（または `Tab` キーを使って 3D ビューと OUTPUT ビューを切り替え、その後は各レーザー出力を順番に切り替えます）。

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D ビューでは、レーザーがどのように見えるかを確認でき、自分のレーザー構成に合わせて設定できます。クリック＆ドラッグでカメラを回転し、マウスホイールで前後に移動します。その他の多くのオプションは _3D Visualiser settings_ パネル（_View -> 3D Visualiser Settings_）にあります。[3d-visualiser.md](../setting-up/3d-visualiser.md "mention") を参照してください。

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output ビューは、各レーザーのゾーンとマスクを設定するために使用します。（左上に大きな番号が表示されるため、どのレーザーを操作しているかを簡単に確認できます。）

このビューは、そのレーザー全体の出力と、その中で各ゾーンがどこに配置されているかを表します。デフォルトではレーザー 1 台につき 1 つのゾーンだけですが、実用上無理のない範囲でいくつでもゾーンを追加でき、このビューですべて確認できます。

{% hint style="info" %}
**ゾーンとは何ですか？**

ゾーンとは、レーザー出力内の空間で、レーザーコンテンツをそこへ送ることができます。1 台のレーザーに複数のゾーンを持たせることもできます。最もシンプルなゾーンは _beam_ ゾーンですが、_canvas_ ゾーンや _DMX_ ゾーンもあります。このガイドでは主に beam ゾーンを扱います。beam ゾーンは通常、空中にアトモスフェリックなビームエフェクトを作るために使用します。
{% endhint %}

編集したいレーザーは、次のいずれかの方法で選択できます。

* 上部バーの番号付きボタン
* 対象レーザーの番号キーを押す（_1-9_ キー\_）\_
* `Tab` キーで順番に切り替える

_+_ ボタンを押すと、セットアップに新しいレーザーを追加できます。（_Laser Overview_ パネルにも _ADD LASER_ ボタンがあります）

_Laser Overview_ パネルの赤い ⊖ ボタンを押すと、セットアップからレーザーを削除できます。

マウスのスクロールホイールでズームイン／ズームアウトできます。また、ゾーンがない場所をクリック＆ドラッグするとビューを移動できます。

ゾーンをクリックして選択し、マウスで四隅のポイントを調整します。角をドラッグしている間に `Alt / Option` キーを使うと、非均一に変形できます。ゾーンを右クリックすると、ゾーンの種類変更を含む追加オプションが表示されます。

左側には一連のアイコンボタンが並ぶバーがあります。ボタンにカーソルを重ねると、その機能の説明が表示されます。ここでは beam ゾーン、canvas ゾーン、マスクを追加できます。また、このレーザーだけにテストパターンを設定するオプションや、グリッド／スナップ設定もあります。

詳しくは [output-view](../output-view/ "mention") を参照してください。

#### Canvas

Canvas システムは、主にグラフィックや建築マッピングに使用します。複雑な画像を複数のレーザーに分配し、各セクションをパース補正できます。[graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention") を参照してください。

### APC40 MIDI コントローラー

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

マウスとキーボードで Liberation を操作することもできますが、APC40 MIDI コントロールインターフェースを使う方がはるかに快適です（Mark 2 が最適ですが、Mark 1 も使用できます）。

関連項目：[apc40-reference.md](../reference/apc40-reference.md "mention")

現在は APC Mini Mark 2 と MIDI Fighter Twister のサポートも実装されており、さらに対応機種を開発中です。ただし、多くの場合は APC40 Mark 2 が最適な選択です。&#x20;

### Clips とエフェクト

{% hint style="info" %}
**Clip とは何ですか？**

Clip は、Liberation 内のあらゆるレーザーコンテンツを入れるコンテナです。Clip にはビームやグラフィックアニメーションを含めることができ、通常はループ再生されます。任意のゾーン（または _Canvas target area_）へ送ることができ、Clip Deck 内の Clip ボタンでトリガーします。
{% endhint %}

#### Clip Deck の概要

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

このグリッドは _Clip Deck_ と呼ばれ、すべてのレーザー Clip が保存される場所です。APC40 の 8 x 5 ボタングリッドに直接対応するよう設計されています。

**Clip Deck の移動**

Clip Deck は、次の方法で左右にスクロールできます。

* 左右矢印キー。`Cmd / Ctrl` を追加すると、1 ページ単位でスクロールします。
* トラックパッド：スワイプ
* マウス：横スクロール対応のマウスであれば、Clip Deck にカーソルを重ねた状態で使用できます。
* APC40 のスクロールノブ
* APC40 の _<- DEVICE ->_ ボタン

現在位置を把握しやすいよう、上部には Clip Deck のミニビジュアライザーがあります。関連項目：[clips](../clips/ "mention")

#### Clip の開始と停止

Clip ボタンを押すと（マウスまたは APC40 で）Clip が開始します。もう一度押すと停止します。Clip を開始すると、_shift_ を押していない限り、同じ色の他の Clip は自動的に停止します。

一部の Clip は _Flash mode_（デフォルトでは赤い Clip）になっており、この場合は Clip ボタンを離すとすぐに停止します。

_STOP_ ボタンは、現在再生中のすべての Clip を停止します。

#### Clip の出力ゾーン設定

Clip ボタンの下にはゾーンボタンがあります。デフォルトでは beam ゾーン 1〜8（_BEAM 1_、_BEAM 2_ など）です。ゾーンボタンは、現在選択されている Clip に割り当てられているゾーンを示すために点灯します。

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

ゾーンボタンの 2 段下には X/Y フリップボタンがあります。これらを切り替えると、Clip を水平方向または垂直方向に反転できます。

{% hint style="info" %}
これらのゾーン割り当てと X/Y フリップ設定は、その Clip 自体に紐づいています。次回その Clip を実行したときにも保持されます。グローバル設定ではありません。
{% endhint %}

Clip を右クリックすると、その Clip の追加設定を編集できます。[clip-settings.md](../clips/clip-settings.md "mention") も参照してください。

### Groups

各 Clip には色付きのアウトラインがあり、この色はその Clip が属する _group_ を表します。APC40 の Clip ボタンも同じ色で点灯します。

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>シアン</td></tr><tr><td>Group 2</td><td>オレンジ</td></tr><tr><td>Group 3</td><td>赤</td></tr><tr><td>Group 4</td><td>インディゴ</td></tr><tr><td>Group 5</td><td>緑</td></tr></tbody></table>

Group システムは非常に柔軟で、次のことができます。

* ある Group の Clip を再生し続けながら、別の Group を切り替える
* Group 内のすべての Clip にゾーンと X/Y フリップをすばやく割り当てる
* Clip に _Flash mode_ を設定する（Group 3 はデフォルトで _Flash mode_ に設定されています）

Group には、Clip に継承させる、または上書きできるトランジションイン／アウト設定もあります。

Clip の Group は右クリックメニューのボタンで割り当てられます。また APC40 では、Group ボタンを押し、_押したままの状態で_ Clip ボタンを押すことで割り当てられます。

Group 内のすべての Clip のゾーン設定を変更する

APC40 を使用する場合は、Group ボタンを押し、_押したままの状態で_ ゾーンボタンと X/Y ボタンを使って、その Group 内のすべての Clip のゾーン設定を切り替えます。

関連項目：[groups.md](../clips/groups.md "mention")

### エフェクト

Liberation のエフェクトシステムは、Clip 出力をリアルタイムで変更するための強力で柔軟な仕組みです。デフォルトのエフェクトボタン 1〜8 は、ゾーンボタンの下にあります。

#### エフェクトの適用

エフェクトボタンを押すとエフェクトのオン／オフが切り替わります。さらに便利なのは、APC40 のスライダー 1〜8 を使ってエフェクトをフェードイン／フェードアウトする方法です。

#### エフェクトパラメーター

ロータリーコントローラー 1〜8\* を使って、各エフェクトの _parameter_ を調整します。（または、マウスで右クリックして level と parameter を調整できます。）parameter の変更内容は、エフェクトの設定によって異なります。デフォルトエフェクトについては下の一覧を参照してください。

{% hint style="info" %}
エフェクトボタンに表示されている小さな数字は、エフェクトの _level_ と _parameter_ を表しています。_level_ は APC40 のフェーダーで操作するか、ボタンをクリック＆ドラッグして調整できます。parameter は APC40 のロータリーで調整するか、マウスで右クリックして調整できます。
{% endhint %}

_\*ロータリーコントローラー 1〜8 は、APC40 Mk2 では上部、Mk1 では右上にあります。関連項目：_ [apc40-reference.md](../reference/apc40-reference.md "mention")

#### デフォルトエフェクト

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**：\
   Clip 出力にカオス的な動きを適用します。parameter でカオスの量／速度を調整します。
2. **Sine wave**：\
   すべてのコンテンツを、移動するサイン波に沿って歪ませます。parameter で波長を調整します。
3. **Rotation**：\
   すべてを回転させます。parameter で回転速度を調整します。
4. **Horizontal flip**：\
   すべてを水平方向に縮めたり伸ばしたりします。parameter で速度を調整します。
5. **Scale**：\
   すべてをフルサイズからゼロまで繰り返し拡大縮小します。parameter で速度を調整します。
6. **Hue**：\
   すべての色相を変更しますが、彩度は変更しません（つまり、白いものは白いままです）。parameter で色相を調整します。
7. **Saturation and hue**：\
   すべての色相を変更し、さらに色を完全に飽和させます（つまり、白いものもその色に変わります）。parameter で色相を調整します。
8. **Flash**：\
   すべての明るさをフルからゼロまで繰り返し点滅させます。parameter で点滅速度を調整します。

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

下段には、プリセットの色相と彩度の値を適用する 16 個の追加カラーエフェクトがあります。

これらはデフォルトエフェクトですが、ほぼ自由に編集できます。

#### _「現在選択されている Clip」_ とは？

Clip を開始すると、アクティブであることを示すために点灯します。また、その周囲に白いアウトラインが表示され、これが現在 _選択されている_ Clip であることを示します。ゾーンボタンを切り替えたり Clip 設定を調整したりすると、その内容は _現在選択されている Clip_ に適用されます。

{% hint style="info" %}
Clip をトリガーせずに選択するには、Clip ボタンを押す前に `Alt / Option` キーを押します。Clip を実行せずにゾーンやその他の設定を調整するのに便利です。
{% endhint %}

### Clip Settings パネル

_Clip Settings_ パネルでは、スケーリング、X/Y 位置の編集、および強力なゾーンディレイシステムへのアクセスができます。

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings パネル

_Global Settings_ パネルでは、すべてのゾーンにわたる全出力に影響するグローバル出力設定を調整できます。

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

AUTO RESET をオンにすると、Clip が何も再生されていないときに、すべての _Global settings_ が自動的にリセットされます。&#x20;

### タイミング

ほとんどのレーザー表示には何らかの音楽トラックがあるため、Liberation のタイミングシステムは BPM（beats per minute）のテンポを基準にしています。_Tempo Panel_ では時間の表現を確認できます。各四角は 1 拍を表し、テンポに合わせて点滅します。

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

MIDI clock や Ableton Link など、複数の同期オプションがあります。音楽のテンポがわかっている場合は、画面上のスライダーまたは APC40 Tempo ノブで手動調整できます。また、_Tap Tempo_ システムを使って音楽に合わせることもできます\_.\_

#### Tap Tempo

_Tap Tempo_ は音楽アプリでよく使われる用語で、音楽の再生中にビートに合わせてタップすることでテンポを設定できます。画面上のボタンも使用できますが、_T_ キー、APC40 の _Tap Tempo_ ボタン、または好みに応じてフットスイッチを使うことをおすすめします。

_R_ キーまたは APC40 の _Metronome_ ボタンを押すと、テンポが小節の先頭にリセットされます。

_Y_ キーを押す、または APC40 の _Tempo_ ノブを回すと、テンポが整数に丸められます。BPM が整数になりやすいエレクトロニックミュージックでは便利です。

### Clip Deck の整理

Clip Deck 上の Clip を移動するには、クリック＆ドラッグして新しい位置へ移動します。ドラッグ中は、カーソルキー（または APC40 のスクロールホイール／ボタン）で左右にスクロールできます。

ドラッグ中に `Alt / Option` キーを押すとコピーを作成できます。

`Alt / Option`-クリックすると、Clip を開始せずに選択できます。

`Alt / Option + Shift`-クリックで複数選択できます。または、Clip の外側をクリック＆ドラッグして「投げ縄」選択できます。&#x20;

クリック＆ドラッグすると、選択されているすべての Clip がドラッグされます。

1 つ以上の Clip を削除するには、Clip Deck の外へドラッグする（ゴミ箱アイコンが表示されます）か、Clip の右クリックメニューから DELETE ボタンを使用します。

### Laser Overview パネル

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser overview panel_ では、現在動作中のレーザーの状態を素早く確認できます。右側の緑の四角は、レーザーコントローラーが正常であることを示します。オレンジになった場合は時々ドロップアウトが発生しており、赤の場合は切断されています。グレーの場合は、コントローラーにまったく接続されていません。&#x20;

中央のグラフはフレーム長の履歴で、右側の数字は現在のフレームレートです。コンテンツが複雑になるほど、フレームレートは低くなります（つまり、ちらつきが増えます）。約 25fps を下回ると、少しちらついて見え始めます。&#x20;

### レーザーへの接続 - Controller Assignment パネル

_Assign Laser Controllers_ ボタンをクリックすると、_Controller Assignment_ パネルが開きます。（このパネルはメニューバーの _View -> Controller Assignment_ からもアクセスできます。）

ここでは、どのレーザー出力をどのレーザーコントローラーに送るかを選択できます。右側のリストからコントローラーを左側のスロットへドラッグ＆ドロップします。コントローラーの名前は、ペアになっているレーザーに合わせて変更できます（ペンアイコンのボタンを使用します）。

詳しくは [controller-assignment.md](../setting-up/controller-assignment.md "mention") の章を参照してください。

{% hint style="danger" %}
レーザーを arm する前に、必ず [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention") の章を確認してください。
{% endhint %}

### Laser Output パネル

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

このパネルには、_現在選択されているレーザー_（上部の番号で示されます）の設定が表示されます。現在選択されているレーザーは、_tab_ キー、番号キー、_Laser Overview_ パネル内のレーザー番号、または _output view_ 内のレーザー番号をクリックして変更できます。

* **Number button** レーザーを arm／disarm します。赤い場合、そのレーザーは armed 状態です。
* **Brightness** 他のレーザーとは独立してレーザー輝度を調整します（_global brightness_ 設定と組み合わされます。つまり、両方が 50% の場合、そのレーザーは 25% になります）。
* **Test Pattern** このレーザーだけにテストパターンをオンにします（グローバルのテストパターン設定を上書きします）。
* **Orientation** 横向きまたは上下逆に設置されたレーザーを補正します。
* **Flip Horizontal and Flip Vertical** レーザーの出力を反転します。配線が一定でないレーザーの出力補正に便利です。
* **Copy Laser Settings** このレーザーの各種設定を他のレーザーへコピーできるパネルを開きます。

### スキャナー設定

ディスプレイ用レーザーは、1 本のレーザービームを非常に高速に動かし、オン／オフを切り替えることで空中に形状を描画します。線、形、画像として見えているものは、実際には目で追えないほど速くビームが経路をなぞっているものです。

ポイントストリームとは、レーザーが次にどこへ移動するか、ビームをオンにするかオフにするかを指示するデータです。Liberation では、Clip がレーザーへ送られる際に、リアルタイムでこのポイントストリームへ変換されます。

Liberation では、このポイントストリームの生成方法を細かく制御でき、各レーザーごとに滑らかさ、明るさ、パフォーマンスのバランスを調整できます。

{% hint style="info" %}
事前計算されたポイントストリームに依存する旧来のレーザーソフトウェアに慣れている場合、このアプローチは最初は違って感じるかもしれません。しかし、リアルタイムのポイント生成では、同じコンテンツを各レーザーに合わせて異なる形で最適化できます。これにより、スキャナー速度や品質が異なる複数のレーザーを扱う場合でも、コンテンツを複製したり作り直したりせずに作業しやすくなります。また、Clip ファイルを非常に小さく保てるため、Liberation のデフォルト Clip Deck 全体はギガバイトではなく、わずか数メガバイトに収まっています。
{% endhint %}

基本的なスキャナー設定は次のとおりです。

* **Speed** はスキャナー速度、つまりレーザーが形状を描画するためにどれだけ速く動くかを表します。従来のレーザーソフトウェアでポイントレートを調整するのに相当しますが、Liberation ではレーザーの移動速度を _ポイントレートとは独立して_ 変更できます。通常、この設定を調整する必要はありません。
* **Scanner sync**（_blank shift、以前は Colour Shift_ と呼ばれることもあります）スキャナーはレーザーを非常に高速に動かしますが、通常、明るさや色の変化はその動きと同期していません。その結果、ビームや線の端に小さくちらつく光の「尾」が現れます。この調整を使って、動きと色を同期させます。[laser-settings](../setting-up/laser-settings/ "mention") を参照してください。

その他の高度なスキャナー設定については、[advanced](../advanced/ "mention") の章で説明しています。

### ゾーニング

レーザーの設定とゾーニングの完全なガイドについては、[setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention") を参照してください。
