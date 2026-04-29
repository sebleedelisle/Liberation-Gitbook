---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ クイックスタートガイド

## はじめに

**Liberation** へようこそ。次世代のレーザーショーソフトウェアです。

Liberation は、現代的で高機能なソフトウェアです。使いやすさと信頼性を基本に設計されており、自由に創造性を表現できます。高速で効率的、そしてスムーズに動作します。この _Quick start guide_ に沿って進めれば、すぐに使い始められます。

### レーザーの管理

Liberation は柔軟に設計されており、実際のレーザーを接続していなくても、レーザーをセットアップしてビジュアライズできます。準備ができたら、各 Output をレーザーコントローラーへスムーズに割り当てられます。

{% hint style="info" %}
Liberation では、必要な数だけレーザーをセットアップし、ビジュアライズできます。ライセンスの種類（Hobbyist、Pro など）で制限されるのは、_arm_ できるレーザーの数だけです。つまり、無料ライセンスでも 100 台のレーザーを使ったショーを設計できます。実際のレーザーで出力する段階になったときにのみ、アップグレードが必要です。
{% endhint %}

初期設定では、8 台のレーザーが横一列に配置されていますが、必要に応じて自由にカスタマイズできます。ソフトウェアに慣れるまでは、この初期設定のまま使うのがおすすめです。その後、実際のハードウェア構成に合わせて調整してください。（[プロジェクトの設定](setting-up/setting-up-your-project.md) を参照）

{% hint style="warning" %}
重要：レーザーを arm する前に、必ず関連するリスクを理解し、[Laser セットアップ手順の概要](setting-up/setting-up-lasers.md) の章を慎重に確認してください。
{% endhint %}

## ソフトウェアの概要

### 安全停止

レーザーを動作させるときは、必ず **ハードウェアの非常停止ボタン** を手元に用意してください（[非常停止 / インターロック](hardware/emergency-stop-interlocks.md) を参照）。緊急度が低い状態ですべてを disarm したい場合は、_**DISARM ALL**_ ボタン、または `Escape` キー（APC40 では _**SESSION**_ キー）を使用できます。画面上のスライダーや APC40 のメインフェーダーで、全体の明るさを下げることもできます。

### スライダー要素

Liberation 全体で、さまざまなスライダーやコントロールを使用します。

{% hint style="info" %}
スライダーだけでは細かく調整できない場合は、スライダーを `Cmd / Ctrl`-クリックすると、数値を直接入力できます。
{% endhint %}

### キーボードショートカット

キーボードショートカットの一覧はこちらで確認できます：[キーボードショートカット](reference/keyboard-shortcuts.md)

### 画面レイアウト

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
特定のボタンの機能が分からない場合は、マウスカーソルを重ねると説明が表示されます。
{% endhint %}

#### メニュー

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

メニューでは、ファイルのインポート／エクスポートに関するすべての項目や、各種パネルを開く項目を利用できます。また、サブスクリプションでこのコンピューターを認証する項目もここにあります（_Liberation -> Authorise/Deauthorise this computer_）。

#### アイコンバー

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

すべてのレーザーの arm／disarm、global brightness、test pattern、3D／Canvas／Output ビューの切り替えなど、よく使う操作がここにあります。

### ビュー

画面左上の大きな領域には、主に **3D**、**CANVAS**、**OUTPUT** の 3 種類のビューのいずれかが表示されます。アイコンバーのボタンで切り替えます（または `Tab` キーで 3D ビューと OUTPUT ビューを切り替え、その後は各レーザー出力を順番に切り替えられます）。

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D ビューでは、レーザーがどのように見えるかを確認でき、実際のレーザー構成に合わせて設定できます。クリック＆ドラッグでカメラを回転し、マウスホイールで前後に移動します。その他の多くのオプションは、_3D Visualiser settings_ パネル（_View -> 3D Visualiser Settings_）にあります。[3D Visualiser](setting-up/3d-visualiser.md) を参照してください。

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output ビューは、各レーザーのゾーンとマスクを設定するために使用します。（左上に大きな番号が表示されるため、現在どのレーザーを操作しているかがすぐに分かります。）

このビューは、そのレーザーの出力全体と、その中に各ゾーンがどのように配置されているかを表します。初期設定では各レーザーに 1 つのゾーンだけがありますが、実用上問題のない範囲でいくつでもゾーンを追加でき、このビューですべて確認できます。

{% hint style="info" %}
**ゾーンとは？**

ゾーンとは、レーザーの出力内にある空間で、レーザーコンテンツをそこへ向けて出力できます。1 台のレーザーに複数のゾーンを持たせることもできます。最も基本的なゾーンは _beam_ ゾーンですが、_canvas_ ゾーンや _DMX_ ゾーンもあります。このガイドでは主に beam ゾーンに焦点を当てます。beam ゾーンは通常、空中に雰囲気のあるビームエフェクトを作るために使用します。
{% endhint %}

編集するレーザーは、次のいずれかの方法で選択できます。

* 上部のバーにある番号付きボタン
* 対象レーザーの番号キーを押す _(1-9_ keys\_)\_
* `Tab` キーで順番に切り替える

セットアップに新しいレーザーを追加するには、_+_ ボタンを押します。（_Laser Overview_ パネルにも _ADD LASER_ ボタンがあります）

セットアップからレーザーを削除するには、_Laser Overview_ パネルの赤い ⊖ ボタンを押します。

マウスのスクロールホイールでズームイン／ズームアウトできます。また、ゾーンがない場所をクリック＆ドラッグすると、ビューを移動できます。

ゾーンをクリックして選択し、マウスでコーナーポイントを調整します。コーナーをドラッグしている間に `Alt / Option` キーを使うと、均一ではない変形ができます。ゾーンを右クリックすると、ゾーンタイプの変更など、さらに多くのオプションが表示されます。

左側には、アイコンボタンが並んだバーがあります。各ボタンにマウスカーソルを重ねると、機能の説明が表示されます。ここにあるボタンで、beam ゾーン、canvas ゾーン、マスクを追加できます。また、このレーザーだけに test pattern を設定するオプションや、グリッド／スナップ設定もあります。

詳しくは [Output view](output-view/) を参照してください。

#### Canvas

Canvas システムは、主にグラフィックや建築物へのマッピングに使用します。複雑な画像を複数のレーザーに分配し、各セクションを遠近補正できます。[Graphics と Canvas システム](graphics-and-the-canvas-system/) を参照してください。

### APC40 MIDI コントローラー

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

マウスとキーボードで Liberation を操作することもできますが、APC40 MIDI コントロールインターフェースを使う方がはるかに快適です（Mark 2 が最適ですが、Mark 1 も使用できます）。

関連項目：[APC40 リファレンス](reference/apc40-reference.md)

現在は APC Mini Mark 2 と MIDI Fighter Twister のサポートも実装済みで、さらに対応機種を開発中です。ただし、ほとんどの場合は APC40 Mark 2 が最適です。

### Clips と Effects

{% hint style="info" %}
**Clip とは？**

Clip は、Liberation 内のレーザーコンテンツを入れるコンテナです。Clip にはビームやグラフィックアニメーションを含めることができ、通常はループ再生されます。任意のゾーン（または _Canvas target area_）に出力でき、Clip Deck 内の clip ボタンでトリガーします。
{% endhint %}

#### Clip Deck の概要

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

このグリッドは _clip deck_ と呼ばれ、すべてのレーザー Clip が保存される場所です。APC40 の 8 x 5 ボタングリッドに直接対応するよう設計されています。

**Clip Deck の移動**

Clip Deck は、次の方法で左右にスクロールできます。

* 左右の矢印キー。`Cmd / Ctrl` を加えると、1 ページ単位でスクロールします。
* トラックパッド：スワイプ
* マウス：マウスに横スクロール機能がある場合、Clip Deck 上にカーソルを置いて使用できます。
* APC40 のスクロールノブ
* APC40 の _<- DEVICE ->_ ボタン

現在位置を把握しやすいように、上部には Clip Deck のミニビジュアライザーがあります。関連項目：[Clips & Clip deck](clips/)

#### Clip の開始と停止

Clip ボタン（マウスまたは APC40）を押すと、Clip が開始します。もう一度押すと停止します。Clip を開始すると、_shift_ を押していない限り、同じ色の他の Clip は自動的に停止します。

一部の Clip は _Flash mode_（初期設定では赤の Clip）になっており、その場合は Clip ボタンを離すとすぐに停止します。

_STOP_ ボタンは、現在実行中のすべての Clip を停止します。

#### Clip の出力ゾーン設定

Clip ボタンの下には zone ボタンがあります。初期設定では beam zone 1〜8（_BEAM 1_、_BEAM 2_ など）です。zone ボタンは点灯し、現在選択されている Clip に割り当てられているゾーンを示します。

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

zone ボタンの 2 段下には X/Y flip ボタンがあります。これらを切り替えることで、Clip を水平または垂直に反転できます。

{% hint style="info" %}
これらのゾーン割り当てと X/Y flip 設定は Clip 自体に紐づいています。次回その Clip を実行したときにも保持されます。グローバル設定ではありません。
{% endhint %}

Clip を右クリックすると、その Clip の詳細設定を編集できます。関連項目：[Clip settings](clips/clip-settings.md)

### Groups

各 Clip には色付きのアウトラインがあり、この色はその Clip が属する _group_ を表します。APC40 の Clip ボタンも同じ色で点灯します。

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>シアン</td></tr><tr><td>Group 2</td><td>オレンジ</td></tr><tr><td>Group 3</td><td>赤</td></tr><tr><td>Group 4</td><td>インディゴ</td></tr><tr><td>Group 5</td><td>緑</td></tr></tbody></table>

Group システムは非常に柔軟で、次のような操作ができます。

* ある Group の Clip を再生したまま、別の Group を切り替える
* Group 内のすべての Clip に、ゾーンと X/Y flip をすばやく割り当てる
* Clip に _Flash mode_ を設定する（Group 3 は初期設定で _Flash mode_ です）

Group には、Clip が継承できる transition in/out の設定もあります。必要に応じて上書きすることもできます。

Clip の Group は、右クリックメニュー内のボタンで割り当てられます。APC40 を使用する場合は、Group ボタンを押し、_押したまま_ Clip ボタンを押します。

Group 内のすべての Clip のゾーン設定を変更する

APC40 を使用する場合は、Group ボタンを押し、_押したまま_ zone ボタンと X/Y ボタンを使って、その Group 内のすべての Clip のゾーン設定を切り替えます。

関連項目：[Clip グループ](clips/groups.md)

### Effects

Liberation の Effects システムは、Clip 出力をリアルタイムで変更するための強力で柔軟な機能です。初期設定の effect ボタン 1〜8 は、zone ボタンの下にあります。

#### Effect の適用

effect ボタンを押すと Effect のオン／オフを切り替えられます。さらに便利なのは、APC40 のスライダー 1〜8 を使って Effect をフェードイン／フェードアウトする方法です。

#### Effect パラメーター

各 Effect の _parameter_ を調整するには、ロータリーコントローラー 1〜8\* を使用します。（または、マウスで右クリックして level と parameter を調整できます）。parameter の変更内容は、Effect の設定によって異なります。初期設定の Effects については、下の一覧を参照してください。

{% hint style="info" %}
effect ボタンに表示される小さな数字は、その Effect の _level_ と _parameter_ を示しています。_level_ は APC40 のフェーダーで制御するか、ボタンをクリック＆ドラッグして調整できます。parameter は APC40 のロータリーで調整するか、マウスで右クリックして調整できます。
{% endhint %}

_\*ロータリーコントローラー 1〜8 は、APC40 Mk2 では上部、Mk1 では右上にあります。関連項目：_ [APC40 リファレンス](reference/apc40-reference.md)

#### 初期設定の Effects

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Clip 出力にランダムでカオスな動きを適用します。parameter でカオスの量／速度を調整します。
2. **Sine wave** :\
   すべてのコンテンツを、動くサイン波に沿って歪ませます。parameter で波長を調整します。
3. **Rotation** :\
   すべてを回転させます。parameter で回転速度を調整します。
4. **Horizontal flip** :\
   すべてを水平方向に縮めたり伸ばしたりします。parameter で速度を調整します。
5. **Scale** :\
   すべてをフルサイズからゼロまで繰り返しスケーリングします。parameter で速度を調整します。
6. **Hue** :\
   すべての色相を変更しますが、彩度は変更しません（つまり、白いものは白いままです）。parameter で色相を調整します。
7. **Saturation and hue** :\
   すべての色相を変更し、さらに色を完全に彩度の高い状態にします（つまり、白いものもその色に変わります）。parameter で色相を調整します。
8. **Flash** :\
   すべての明るさをフルからゼロまで繰り返し点滅させます。parameter で点滅速度を調整します。

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

下段には、プリセットの hue と saturation 値を適用する 16 個の追加カラー Effect があります。

これらは初期設定の Effects ですが、ほぼ自由に編集できます。

#### _現在選択されている Clip_ とは？

Clip を開始すると、その Clip が点灯してアクティブであることを示します。また、白いアウトラインが表示され、これが現在選択されている Clip であることを示します。zone ボタンを切り替えたり Clip 設定を調整したりすると、それらは _現在選択されている Clip_ に適用されます。

{% hint style="info" %}
Clip をトリガーせずに選択するには、Clip ボタンを押す前に `Alt / Option` キーを押します。Clip を実行せずにゾーンやその他の設定を調整するのに便利な方法です。
{% endhint %}

### Clip Settings パネル

_Clip Settings_ パネルでは、スケーリング、X/Y 位置の編集や、強力な zone delay システムへのアクセスができます。

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings パネル

_Global Settings_ パネルでは、すべてのゾーンのすべての出力に影響するグローバル出力設定を調整できます。

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

AUTO RESET をオンにすると、Clip が再生されていないときにすべての _Global settings_ が自動的にリセットされます。

### Timing

ほとんどのレーザー演出には何らかの音楽トラックがあるため、Liberation の Timing システムは BPM（beats per minute）のテンポを基準にしています。_Tempo Panel_ では時間の表示を確認できます。各四角が 1 拍を表し、テンポに合わせて点滅します。

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

MIDI clock や Ableton Link など、複数の同期オプションがあります。音楽のテンポが分かっている場合は、画面上のスライダーまたは APC40 の Tempo ノブで手動調整できます。また、_Tap Tempo_ システムを使って音楽に合わせることもできます\_.\_

#### Tap Tempo

_Tap Tempo_ は音楽アプリでよく使われる用語で、音楽再生中にビートに合わせてタップすることでテンポを設定できます。画面上のボタンも使用できますが、_T_ キーまたは APC40 の _Tap Tempo_ ボタンを使用することをおすすめします（必要であればフットスイッチも使用できます）。

_R_ キーまたは _Metronome_ ボタン（APC40）を押すと、テンポを小節の先頭にリセットできます。

_Y_ キーを押す、または _Tempo_ ノブ（APC40）を回すと、テンポを整数に丸められます。BPM が整数になりやすい電子音楽では便利です。

### Clip Deck の整理

Clip Deck 上で Clip を移動するには、クリックして新しい位置へドラッグします。ドラッグ中は、カーソルキー（または APC40 のスクロールホイール／ボタン）で左右にスクロールできます。

ドラッグ中に `Alt / Option` キーを押すと、コピーを作成できます。

Clip を開始せずに選択するには、Clip を `Alt / Option`-クリックします。

複数選択するには、Clip を `Alt / Option + Shift`-クリックするか、Clip の外側をクリック＆ドラッグして「投げ縄」選択します。

クリック＆ドラッグすると、選択中のすべての Clip がドラッグされます。

1 つまたは複数の Clip を削除するには、Clip Deck の外へドラッグする（ゴミ箱アイコンが表示されます）か、Clip の右クリックメニューにある DELETE ボタンを使用します。

### Laser Overview パネル

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser overview panel_ では、現在動作しているレーザーの状態をすばやく確認できます。右側の緑の四角は、レーザーコントローラーが正常であることを示します。オレンジになった場合は、時々ドロップアウトが発生しています。赤の場合は切断されています。グレーの場合は、コントローラーにまったく接続されていません。

中央のグラフは frame length の履歴で、右側の数字は現在の frame rate です。コンテンツが複雑になるほど frame rate は低くなります（つまり、ちらつきが増えます）。約 25fps を下回ると、少しちらついて見え始めます。

### レーザーへの接続 - Controller Assignment パネル

_Assign Laser Controllers_ ボタンをクリックすると、_Controller Assignment_ パネルが開きます。（このパネルはメニューバーの _View -> Controller Assignment_ からも開けます）。

ここでは、どのレーザー Output をどのレーザーコントローラーへ送るかを選択できます。右側のリストからコントローラーを左側のスロットへドラッグ＆ドロップします。どのレーザーとペアになっているか分かるように、コントローラー名を変更できます（ペンアイコンのボタンを使用します）。

詳しくは [コントローラーの割り当て](setting-up/controller-assignment.md) の章を参照してください。

{% hint style="danger" %}
レーザーを arm する前に、必ず [Laser セットアップ手順の概要](setting-up/setting-up-lasers.md) の章を確認してください。
{% endhint %}

### Laser Output パネル

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

このパネルには、_currently selected laser_（上部の番号で表示）の設定が表示されます。現在選択されているレーザーは、_tab_ キー、番号キー、_Laser Overview_ パネル内のレーザー番号、または _output view_ 内のレーザー番号をクリックして変更できます。

* **Number button** レーザーを arm／disarm します。赤の場合、そのレーザーは armed 状態です。
* **Brightness** 他のレーザーとは独立してレーザーの明るさを調整します（_global brightness_ 設定と組み合わされます。つまり両方が 50% の場合、そのレーザーは 25% になります）。
* **Test Pattern** このレーザーだけに test pattern をオンにします（global test pattern 設定を上書きします）。
* **Orientation** 横向きまたは上下逆に設置されたレーザーを補正します。
* **Flip Horizontal and Flip Vertical** レーザーの出力を反転します。配線が統一されていないレーザーの出力補正に便利です。
* **Copy Laser Settings** このレーザーの各種設定を他のレーザーへコピーできるパネルを開きます。

### Scanner settings

ディスプレイ用レーザーは、1 本のレーザービームを非常に高速に動かし、オン／オフを切り替えることで空中に形状を描画します。線、形、画像として見えているものは、実際にはビームが目で追えないほど高速に経路をなぞっているものです。

point stream は、レーザーに次にどこへ移動するか、ビームをオンにするかオフにするかを伝えるデータです。Liberation では、Clip はレーザーへ送信される際にリアルタイムでこの point stream に変換されます。

Liberation では、この point stream の生成方法を詳細に制御できます。これにより、各レーザーごとに滑らかさ、明るさ、パフォーマンスのバランスを調整できます。

{% hint style="info" %}
事前計算された point stream に依存する古いレーザーソフトウェアに慣れている場合、この方式は最初は少し違って感じるかもしれません。しかし、リアルタイムの point 生成により、同じコンテンツを各レーザーに合わせて別々に最適化できます。scanner の速度や品質が異なる複数のレーザーを扱う場合でも、コンテンツを複製したり作り直したりせずに作業しやすくなります。また、Clip ファイルを非常に小さく保てるため、Liberation の初期 Clip Deck 全体はギガバイトではなく、わずか数メガバイトに収まっています。
{% endhint %}

基本的な scanner settings は次のとおりです。

* **Speed** は scanner speed、つまりレーザーが形状を描くためにどれだけ速く動くかです。従来のレーザーソフトウェアで point rate を調整することに相当しますが、Liberation ではレーザーの移動速度を _point rate とは独立して_ 変更できます。通常、この設定を調整する必要はありません。
* **Scanner sync**（_blank shift、以前は Colour Shift_ と呼ばれることもあります）scanners はレーザーを非常に高速に動かしますが、通常、明るさや色の変化は動きと同期していません。これにより、ビームや線の端に小さなちらつく光の「尾」が現れます。この調整を使って、動きと色を同期させます。[Laser output 設定パネル](setting-up/laser-settings.md) を参照してください。

その他の高度な scanner settings については、[高度な機能](advanced/) の章で説明しています。

### Zoning

レーザーのセットアップとゾーニングに関する完全なガイドは、こちらを参照してください：[Laser セットアップ手順の概要](setting-up/setting-up-lasers.md)
