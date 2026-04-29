# ✅ クイックスタートガイド

## はじめに

**Liberation** へようこそ。次世代のレーザーショーソフトウェアです。

Liberation は高機能で複雑な現代的ソフトウェアですが、使いやすさと信頼性を土台に、創造性を自由に表現できるよう設計されています。高速で効率的、そしてスムーズに使えます。この_クイックスタートガイド_に沿って、すぐに使い始めましょう。

### レーザーの管理

Liberation では、実際のレーザーを接続していなくても、laser の設定や可視化ができます。準備ができたら、各出力を laser controller にスムーズに割り当てられます。

{% hint style="info" %}
Liberation 内では、必要な数だけ laser を設定して可視化できます。ライセンス種別（Hobbyist、Pro など）で制限されるのは、_arm_ できる laser の数だけです。つまり、無料ライセンスでも 100 台の laser を使ったレーザーショーを設計できます。実際の laser で出力する段階になったときだけ、アップグレードが必要です。
{% endhint %}

デフォルトでは 8 台の laser が横一列に配置されていますが、必要に応じて自由に変更できます。ソフトウェアに慣れるまでは、このデフォルト設定のまま使うのがおすすめです。その後、実際のハードウェア構成に合わせて調整できます。（[プロジェクトの設定](../setting-up/setting-up-your-project.md)を参照）&#x20;

{% hint style="warning" %}
重要：laser を arm 状態にする前に、必ずリスクを理解し、[レーザーの設定](../setting-up/setting-up-lasers.md)の章を慎重に確認してください。
{% endhint %}

## ソフトウェアの概要

### 安全停止

レーザーを動作させるときは、必ず**ハードウェアの非常停止ボタン**を手元に用意してください（[非常停止とインターロック](../hardware/emergency-stop-interlocks.md)を参照）。緊急性が低い状態ですべてを disarm したい場合は、_**DISARM ALL**_ ボタン、`Escape` キー、または APC40 の _**SESSION**_ キーを使用できます。画面上のスライダーや APC40 のメインフェーダーで、Global Brightness を下げることもできます。

### スライダー要素

Liberation には、さまざまなスライダーやコントロールがあります。

{% hint style="info" %}
スライダーだけでは細かく調整しにくい場合は、スライダーを `Cmd / Ctrl` キーを押しながらクリックすると、新しい値を入力できます。
{% endhint %}

### キーボードショートカット

キーボードショートカットの全一覧はこちらにあります：[キーボードショートカット](../reference/keyboard-shortcuts.md)

### 画面レイアウト

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
特定のボタンの機能が分からない場合は、マウスカーソルを重ねると説明が表示されます。
{% endhint %}

#### メニュー

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

メニューでは、すべてのファイルのインポート／エクスポート項目や、各 panel を開く項目を見つけられます。また、サブスクリプションでこのコンピューターを認証する項目もここにあります（_Liberation -> Authorise/Deauthorise this computer_）。

#### アイコンバー

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

ここには、すべての laser の arm／disarm、Global Brightness、test pattern、3D view／Canvas view／Output view の切り替えなど、よく使う操作がまとまっています。

### Views

画面左上の大きな領域は、主に **3D**、**CANVAS**、**OUTPUT** の 3 つの view のいずれかになります。アイコンバーのボタンで切り替えます（または `Tab` キーで 3D view と Output view を切り替え、その後は各 laser 出力を順番に移動できます）。

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view では、laser の見え方を確認でき、実際の laser 構成に合わせて設定できます。クリックしてドラッグするとカメラを回転でき、マウスホイールで前後に移動できます。その他多くのオプションは、_3D Visualiser settings_ panel（_View -> 3D Visualiser Settings_）にあります。[3D Visualiser](../setting-up/3d-visualiser.md)を参照してください。

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view は、各 laser の zone と mask を設定するために使用します。（左上に大きな番号が表示されるので、どの laser を操作しているかすぐに分かります。）

この view は、その laser の出力全体と、その中で各 zone がどこに配置されているかを表します。デフォルトでは laser ごとに zone は 1 つだけですが、実用上問題のない範囲でいくつでも zone を追加でき、この view でそれらをすべて確認できます。

{% hint style="info" %}
**zone とは？**

zone は、laser 出力内の空間で、laser コンテンツの出力先として指定できます。1 台の laser に複数の zone を持たせることもできます。最もシンプルな zone は _beam_ zone ですが、_canvas_ zone や _DMX_ zone もあります。このガイドでは主に beam zone を扱います。beam zone は通常、空中に雰囲気のある beam エフェクトを作るために使われます。
{% endhint %}

編集したい laser は、次のいずれかの方法で選択できます。

* 上部バーの番号付きボタン
* 目的の laser に対応する数字キー（_1〜9_ キー\_）\_
* `Tab` キーで順番に切り替え

設定に新しい laser を追加するには、_+_ ボタンを押します。（_Laser Overview_ panel にも _ADD LASER_ ボタンがあります）

設定から laser を削除するには、_Laser Overview_ panel の赤い ⊖ ボタンを押します。

マウスのスクロールホイールで拡大／縮小でき、zone がない場所をクリックしてドラッグすると view を移動できます。

zone をクリックすると選択でき、マウスでコーナーポイントを調整できます。コーナーをドラッグしている間に `Alt / Option` キーを使うと、均一でない形にできます。zone を右クリックすると、zone の種類変更など、その他のオプションが表示されます。

左側には一連のアイコンボタンが並んだバーがあります。各ボタンにマウスカーソルを重ねると、その機能の説明が表示されます。ここでは beam zone、canvas zone、mask を追加できます。また、この laser だけに test pattern を設定するオプションや、グリッド、スナップの設定もあります。

詳しくは [Outputビュー](../output-view/)を参照してください。

#### Canvas

Canvas システムは、主にグラフィックや建築物へのマッピングに使用します。複雑な画像を複数の laser に分配し、各セクションを遠近補正できます。[グラフィックと Canvas システム](../graphics-and-the-canvas-system/)を参照してください。

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

マウスとキーボードでも Liberation を操作できますが、APC40 MIDI controller インターフェースを使う方がはるかに便利です（Mark 2 が最適ですが、Mark 1 も使用できます）。

関連項目：[APC40 リファレンス](../reference/apc40-reference.md)

現在は APC Mini Mark 2 と MIDI Fighter Twister にも対応しており、さらに対応機種を開発中です。ただし、多くの場合は APC40 Mark 2 が最適です。&#x20;

### Clips とエフェクト

{% hint style="info" %}
**Clip とは？**

Clip は、Liberation 内のあらゆる laser コンテンツを入れるコンテナです。Clip には beam やグラフィックアニメーションを含めることができ、通常はループするサイクルです。任意の zone（または _Canvas target area_）に出力でき、Clip Deck 内の Clip ボタンでトリガーします。
{% endhint %}

#### Clip Deck の概要

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

このグリッドは _Clip Deck_ と呼ばれ、すべての laser Clip が保存される場所です。APC40 の 8 x 5 ボタングリッドに直接対応するように設計されています。

**Clip Deck の移動**

Clip Deck は、次の方法で左右にスクロールできます。

* 左右の矢印キー。`Cmd / Ctrl` を追加すると、1 ページ単位でスクロールできます。
* トラックパッド：スワイプ
* マウス：横スクロール対応のマウスであれば、Clip Deck 上にカーソルを置いた状態で使用できます
* APC40 のスクロールノブ
* APC40 の _<- DEVICE ->_ ボタン

現在位置を把握しやすいように、上部には Clip Deck のミニビジュアライザーがあります。関連項目：[Clips と Clip Deck](../clips/)

#### Clip の開始と停止

Clip ボタンを押すと（マウスでも APC40 でも）、Clip が開始します。もう一度押すと停止します。Clip を開始すると、_shift_ を押していない限り、同じ色の他の Clip は自動的に停止します。

一部の Clip は _Flash mode_（デフォルトでは赤の Clip）になっており、この場合は Clip ボタンを離すとすぐに停止します。

_STOP_ ボタンは、現在実行中のすべての Clip を停止します。

#### Clip の出力 zone の設定

Clip ボタンの下には zone ボタンがあり、デフォルトでは beam zone 1〜8（_BEAM 1_、_BEAM 2_ など）です。zone ボタンは、現在選択されている Clip にどの zone が割り当てられているかを点灯で示します。

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

zone ボタンの 2 行下には X/Y flip ボタンがあります。これを切り替えると、Clip を水平または垂直に反転できます。

{% hint style="info" %}
これらの zone 割り当てと X/Y flip 設定は、Clip 自体に紐付いています。次回その Clip を実行したときも保持されます。グローバル設定ではありません。
{% endhint %}

Clip を右クリックすると、その Clip の詳細設定を編集できます。[Clip の設定](../clips/clip-settings.md)も参照してください。

### グループ

各 Clip には色付きの枠があり、この色はその Clip が属する_グループ_を表します。APC40 の Clip ボタンもこの色で点灯します。

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>グループ 1</td><td>シアン</td></tr><tr><td>グループ 2</td><td>オレンジ</td></tr><tr><td>グループ 3</td><td>赤</td></tr><tr><td>グループ 4</td><td>インディゴ</td></tr><tr><td>グループ 5</td><td>緑</td></tr></tbody></table>

グループシステムは非常に柔軟で、次のことができます。

* あるグループの Clip を再生したまま、別のグループの Clip を切り替える
* グループ内のすべての Clip に、zone と X/Y flip を素早く割り当てる
* Clip に _Flash mode_ を設定する（グループ 3 はデフォルトで _Flash mode_ に設定されています）

グループには、Clip が継承できるトランジションのイン／アウト設定もあり、個別に上書きすることもできます。

Clip のグループは、右クリックメニューのボタンで割り当てられます。APC40 を使う場合は、グループボタンを押し、_押したまま_ Clip ボタンを押します。

グループ内のすべての Clip の zone 設定を変更する

APC40 を使う場合は、グループボタンを押し、_押したまま_ zone ボタンと X/Y ボタンで、そのグループ内のすべての Clip の zone 設定を切り替えます。

関連項目：[グループ](../clips/groups.md)

### エフェクト

Liberation のエフェクトシステムは、Clip 出力をリアルタイムに変更するための強力で汎用的な仕組みです。デフォルトのエフェクトボタン 1〜8 は、zone ボタンの下にあります。

#### エフェクトの適用

エフェクトボタンを押すとエフェクトを切り替えられます。さらに便利なのは、APC40 のスライダー 1〜8 を使って、エフェクトをフェードイン／フェードアウトする方法です。

#### エフェクトパラメーター

ロータリーコントローラー 1〜8\* を使って、各エフェクトの _parameter_ を調整します。（または、マウスで右クリックして level と parameter を調整することもできます）。parameter の変更内容は、エフェクトの設定によって異なります。デフォルトエフェクトについては、下の一覧を参照してください。

{% hint style="info" %}
エフェクトボタンに表示される小さな数字は、そのエフェクトの _level_ と _parameter_ を示します。_level_ は APC40 のフェーダーで操作するか、ボタン上でクリックしてドラッグします。parameter は APC40 のロータリーで調整するか、マウスで右クリックして調整できます。
{% endhint %}

_\*ロータリーコントローラー 1〜8 は、APC40 Mk2 では上部、Mk1 では右上にあります。関連項目：_ [APC40 リファレンス](../reference/apc40-reference.md)

#### デフォルトエフェクト

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**：\
   Clip 出力にカオスな動きを加えます。parameter でカオスの量／速度を調整します。
2. **Sine wave**：\
   すべてのコンテンツを、動くサイン波に沿って歪ませます。parameter で波長を調整します。
3. **Rotation**：\
   すべてを回転させます。parameter で回転速度を調整します。
4. **Horizontal flip**：\
   すべてを水平方向に縮めたり伸ばしたりします。parameter で速度を調整します。
5. **Scale**：\
   すべてをフルサイズからゼロまで繰り返しスケールします。parameter で速度を調整します。
6. **Hue**：\
   すべての色相を変更しますが、彩度は変更しません（つまり、白いものは白のままです）。parameter で色相を調整します。
7. **Saturation and hue**：\
   すべての色相を変更し、色を完全に彩度のある状態にします（つまり、白いものもその色に変わります）。parameter で色相を調整します。
8. **Flash**：\
   すべての明るさをフルからゼロまで繰り返し点滅させます。parameter で点滅速度を調整します。

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

下段にはさらに 16 個のカラーエフェクトがあり、プリセットされた色相と彩度の値を適用できます。

これらはデフォルトエフェクトですが、ほぼ自由に編集できます。

#### _「現在選択されている Clip」_とは？

Clip を開始すると、その Clip が点灯してアクティブであることを示します。また、白い枠が表示され、これが現在選択されている Clip であることを示します。zone ボタンの切り替えや Clip 設定の調整は、常に_現在選択されている Clip_ に適用されます。

{% hint style="info" %}
Clip をトリガーせずに選択するには、Clip ボタンを押す前に `Alt / Option` キーを押します。実行せずに zone やその他の設定を調整するのに便利です。
{% endhint %}

### Clip Settings panel

_Clip Settings_ panel を使うと、スケーリング、X/Y 位置を編集でき、強力な zone delay システムにもアクセスできます。

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings panel

_Global Settings_ panel では、すべての zone にわたる全出力に影響するグローバル出力設定を調整できます。

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

AUTO RESET をオンにすると、Clip が再生されていないときに、すべての _Global settings_ が自動的にリセットされます。&#x20;

### タイミング

ほとんどのレーザー演出には何らかの音楽トラックがあるため、Liberation のタイミングシステムは BPM（1 分あたりの拍数）のテンポを基準にしています。_Tempo Panel_ では時間の表現を確認できます。各四角が 1 拍を表し、テンポに合わせて点滅します。

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

MIDI clock や Ableton Link など、複数の同期オプションがあります。音楽のテンポが分かっている場合は、画面上のスライダーや APC40 Tempo ノブで手動調整できます。また、_Tap Tempo_ システムを使って、音楽に合わせることもできます\_.\_

#### Tap Tempo

_Tap Tempo_ は音楽アプリでよく使われる用語で、音楽の再生中にビートに合わせてタップすることでテンポを設定できます。画面上のボタンも使えますが、_T_ キー、または APC40 の _Tap Tempo_ ボタンを使うことをおすすめします（好みによってはフットスイッチも使えます）。

_R_ キーまたは APC40 の _Metronome_ ボタンを押すと、テンポを小節の先頭にリセットできます。

_Y_ キーを押す、または APC40 の _Tempo_ ノブを回すと、テンポを整数に丸められます。これは、BPM が整数になりやすいエレクトロニックミュージックで便利です。

### Clip Deck の整理

Clip Deck 上で Clip を移動するには、クリックして新しい位置へドラッグします。ドラッグ中にカーソルキー（または APC40 のスクロールホイール／ボタン）を使うと、左右にスクロールできます。

ドラッグ中に `Alt / Option` キーを押すと、コピーを作成できます。

`Alt / Option` キーを押しながら Clip をクリックすると、開始せずに選択できます。

`Alt / Option + Shift` キーを押しながら Clip をクリックすると複数選択できます。または、Clip の外側をクリックしてドラッグすると、「なげなわ」選択ができます。&#x20;

クリックしてドラッグすると、選択されているすべての Clip がドラッグされます。

1 つ以上の Clip を削除するには、Clip Deck の外へドラッグする（ゴミ箱アイコンが表示されます）か、Clip の右クリックメニューから DELETE ボタンを使用します。

### Laser Overview panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser Overview panel_ では、現在実行中の laser の状態をすばやく確認できます。右側の緑の四角は、laser controller が正常であることを示します。オレンジになった場合は、時々ドロップアウトが発生しています。赤の場合は切断されています。グレーの場合は、controller にまったく接続されていません。&#x20;

中央のグラフはフレーム長の履歴で、右側の数字は現在のフレームレートです。コンテンツが複雑になるほど、フレームレートは低くなります（つまり、ちらつきが増えます）。約 25fps を下回ると、少しちらついて見え始めます。&#x20;

### laser への接続 - Controller Assignment panel

_Assign Laser Controllers_ ボタンをクリックすると、_Controller Assignment_ panel が開きます。（この panel は、メニューバーの _View -> Controller Assignment_ からも開けます）。

ここでは、どの laser 出力をどの laser controller に送るかを選択できます。右側の一覧から controller をドラッグ＆ドロップして、左側のスロットに入れます。controller には、ペアになっている laser に合わせた名前を付けられます（ペンアイコンボタンを使用します）。

詳しくは、[コントローラーの割り当て](../setting-up/controller-assignment.md)の章をお読みください。

{% hint style="danger" %}
laser を arm 状態にする前に、必ず[レーザーの設定](../setting-up/setting-up-lasers.md)の章を確認してください。
{% endhint %}

### Laser Output panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

この panel には、_現在選択されている laser_ の設定が表示されます（上部の番号で示されます）。現在選択されている laser は、_tab_ キー、数字キー、_Laser Overview_ panel の laser 番号、または _output view_ 内の番号をクリックして変更できます。

* **Number button** laser の arm／disarm を切り替えます。赤の場合、その laser は armed です。
* **Brightness** 他の laser とは独立して laser の明るさを調整します（_global brightness_ 設定と組み合わされます。つまり、両方が 50% の場合、laser は 25% になります）。
* **Test Pattern** この laser だけに test pattern をオンにします（グローバルの test pattern 設定を上書きします）
* **Orientation** 横向きまたは上下逆さに設置された laser を補正します。
* **Flip Horizontal and Flip Vertical** laser の出力を反転します。配線が統一されていない laser の出力補正に便利です。
* **Copy Laser Settings** この laser から他の laser へ、さまざまな設定をコピーできる panel を開きます。

### Scanner settings

ディスプレイ用 laser は、1 本のレーザービームを非常に高速に動かし、オン／オフを切り替えることで空中に図形を描きます。線、形、画像として見えているものは、実際には目で追えないほど速く beam が経路をなぞっているものです。

ポイントストリームは、laser が次にどこへ移動するか、そして beam をオンにするかオフにするかを指示するデータです。Liberation では、Clip が laser へ送られるときに、リアルタイムでこのポイントストリームへ変換されます。

Liberation では、このポイントストリームの生成方法を細かく制御できます。これにより、各 laser について、滑らかさ、明るさ、パフォーマンスのバランスを調整できます。

{% hint style="info" %}
事前計算されたポイントストリームに依存する従来のレーザーソフトウェアに慣れている場合、この方式は最初は少し違って感じるかもしれません。しかし、リアルタイムのポイント生成により、同じコンテンツを laser ごとに異なる方法で最適化できます。scanner の速度や品質が異なる複数の laser を扱う場合でも、コンテンツを複製したり作り直したりせずに作業しやすくなります。また、Clip ファイルを非常に小さく保てます。Liberation のデフォルト Clip Deck 全体が、ギガバイトではなく数メガバイトに収まっているのはそのためです。
{% endhint %}

基本的な scanner settings は次のとおりです。

* **Speed** は scanner speed、つまり laser が図形を描くためにどれだけ速く動くかです。従来のレーザーソフトウェアでポイントレートを調整することに相当しますが、Liberation では _point rate とは独立して_ laser の移動速度を変更できます。通常、調整する必要はありません。
* **Scanner sync**（_blank shift、以前の Colour Shift_ と呼ばれることもあります）scanner は laser を非常に高速に動かしますが、通常、明るさや色の変化はその動きと同期していません。その結果、beam や線の端に小さくちらつく光の「尾」が現れます。この調整を使って、動きと色が互いに同期するようにします。[Laser Settings](../setting-up/laser-settings/)を参照してください。

その他の高度な scanner settings については、[高度な機能](../advanced/)の章で説明します。

### Zoning

laser の設定と zoning の詳しいガイドについては、[レーザーの設定](../setting-up/setting-up-lasers.md)を参照してください。
