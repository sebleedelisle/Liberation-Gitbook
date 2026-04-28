---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

単一のドット／ビームを作成します。

* **Render profile** - [render-profile.md](fundamentals/render-profile.md "mention") を参照してください
* **Colour** - ドットの色です。[colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention") を参照してください
* **x** and **y** position - [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention") を参照してください
* _MOVE TO FRONT / MOVE TO BACK_ - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

ライン／シートを作成します。

* **Render profile** - [render-profile.md](fundamentals/render-profile.md "mention") を参照してください
* **Size** - ラインの長さです
* **Colour** - ラインの色です。[colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention") を参照してください
* **x** and **y** position - [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention") を参照してください
* **rotation** - ラインの角度です（度単位）
* **resolution** - [resolution.md](fundamentals/resolution.md "mention") を参照してください
* **alignment** - _LEFT / CENTRE / RIGHT -_ ラインの開始点と回転中心を決定します
* _MOVE TO FRONT / MOVE TO BACK_ - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

円／コーンを作成します。

* **Render profile** - [render-profile.md](fundamentals/render-profile.md "mention") を参照してください
* **radius** - 円の半径です
* **Colour** - 円の色です。[colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention") を参照してください
* **x** and **y** position - [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention") を参照してください
* **resolution** - [resolution.md](fundamentals/resolution.md "mention") を参照してください
* **Fill state** - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください
* _MOVE TO FRONT / MOVE TO BACK_ - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

正多角形（三角形、四角形、五角形など）を作成します。

* **Render profile** - [render-profile.md](fundamentals/render-profile.md "mention") を参照してください
* **size** - 中心から各頂点までの距離です
* **Colour** - ポリゴンの色です。[colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention") を参照してください
* **x** and **y** position - [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention") を参照してください
* **rotation** - 図形の回転角度です（度単位）
* **resolution** - [resolution.md](fundamentals/resolution.md "mention") を参照してください
* **Fill state** - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください
* _MOVE TO FRONT / MOVE TO BACK_ - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

カスタム図形用に SVG ファイルを読み込みます。

{% hint style="warning" %}
Liberation は _SVGTiny_ 形式に対応しています。InkScape を推奨しますが、多くのベクターグラフィックアプリでもこの形式で書き出せます。書き出す前に、テキストは必ず図形に変換してください。Liberation はストロークを描画し、必要に応じて塗りをマスクとして使用します。ラインが黒になっていないことを確認してください。黒いラインは、カラーモディファイアなしでは表示されません。
{% endhint %}

* **Import SVG** - ディスクから SVG ファイルを読み込みます。

{% hint style="info" %}
SVG を読み込むと、その内容は変換されてクリップ内に保存されます。そのため、後でマスク設定を変更したい場合を除き、元ファイルへの参照を維持する必要はありません。
{% endhint %}

* **Use fills as masks** - 塗りのある図形をマスクとして処理します。つまり黒で塗りつぶされたものとして扱います。SVG に塗りのある図形が含まれている場合は自動的に有効になります。塗りのある図形がない場合は無効になります。[fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください
* **Add outlines to filled shapes** - SVG 内の図形にアウトラインがない場合、その図形は描画できません。このオプションは、塗りのある図形にアウトライン（または _stroke_）を追加します。SVG にストローク付きの図形がない場合は自動的に有効になります。塗りのある図形がない場合は無効になります。
* **Invert black lines** - SVG 内のすべてのラインが黒の場合、表示されません。このオプションはそれらを白に変換します。SVG に黒い図形しかない場合は自動的に有効になりますが、該当する図形がない場合は無効になります。
* **Render profile** - [render-profile.md](fundamentals/render-profile.md "mention") を参照してください
* **scale** - SVG のサイズを調整します。SVG の読み込み時に自動計算されます（画像が見えるようにするため）が、後から手動で編集できます。
* **x** and **y** position - [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention") を参照してください
* **rotation** - 画像の回転角度です（度単位）
* **resolution** - [resolution.md](fundamentals/resolution.md "mention") を参照してください
* _MOVE TO FRONT / MOVE TO BACK_ - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

一連の SVG ファイルからアニメーションを作成します。

* **Import SVG Sequence** - すべての SVG ファイルが入っているフォルダーを選択します。ファイルは英数字順に読み込まれる点に注意してください。

{% hint style="info" %}
SVG シーケンスを読み込むと、その内容は変換されてクリップ内に保存されます。そのため、後でマスク設定を変更したい場合を除き、元ファイルへの参照を維持する必要はありません。
{% endhint %}

* **Use fills as masks** - 塗りのある図形をマスクとして処理します。つまり黒で塗りつぶされたものとして扱います。いずれかの SVG に塗りのある図形が含まれている場合は自動的に有効になります。どの SVG にも塗りのある図形がない場合は無効になります。[fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください
* **Add outlines to filled shapes** - SVG 内の図形にアウトラインがない場合、その図形は描画できません。このオプションは、塗りのある図形にアウトライン（または _stroke_）を追加します。SVG にストローク付きの図形がない場合は自動的に有効になります。塗りのある図形がない場合は無効になります。
* **Invert black lines** - SVG 内のすべてのラインが黒の場合、表示されません。このオプションはそれらを白に変換します。SVG に黒い図形しかない場合は自動的に有効になりますが、該当する図形がない場合は無効になります。
* **Render profile** - [render-profile.md](fundamentals/render-profile.md "mention") を参照してください
* **scale** - 画像のサイズを調整します。
* **x** and **y** position - [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention") を参照してください
* **rotation** - 画像の回転角度です（度単位）
* **resolution** - [resolution.md](fundamentals/resolution.md "mention") を参照してください
* **speed** - アニメーション全体の長さです（小節単位）。
* **time per frame** - これを設定すると、長さはアニメーション全体ではなくフレームごとの長さになります。たとえば _speed_ を ¼ に設定すると、各フレームは 1 拍になります。
* **animation direction** -
  * _FORWARDS_ - アニメーションは順方向に再生され、その後先頭に戻ってループします
  * _BACKWARDS_ - アニメーションは逆方向に再生され、その後末尾に戻ってループします
  * _PINGPONG_ - アニメーションは順方向に再生された後、逆方向に戻る動きをループします
  * _MANUAL_ - 現在のフレームは _position manual_ 設定で指定します
* **position manual** - 現在のフレームを設定します。0% が最初のフレーム、100% が最後のフレームです。手動、または外部オシレーターで設定できます。
* _MOVE TO FRONT / MOVE TO BACK_ - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

TrueType または OpenType フォントを使用してテキストを作成します。

* **Text** - ここに使用したいテキストを入力します
* **Font** - 使用したいフォントを選択します

{% hint style="info" %}
Liberation にフォントを追加するには、.ttf または .otf ファイルを data/resources/fonts フォルダーにコピーします。
{% endhint %}

* **Render profile** - [render-profile.md](fundamentals/render-profile.md "mention") を参照してください
* **horizontal alignment** - _LEFT_、_CENTRE_、または _RIGHT_ を選択して、テキストの配置を指定します。
* **Fill state** - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください
* **size** - テキストサイズです
* **colour -** [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention") を参照してください
* **x** and **y** position - [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention") を参照してください
* **rotation** - 画像の回転角度です（度単位）
* **resolution** - [resolution.md](fundamentals/resolution.md "mention") を参照してください
* **reveal** - テキストを 1 文字ずつ徐々に表示するために使用します。この値が 0〜50% の間の場合、テキストは左から右へ徐々に表示されます。50〜100% の間の場合、テキストは左から右へ消えていきます。このソケットにオシレーターを接続すると、アニメーションを作成できます。
* **reveal by word** - 設定すると、_reveal_ は文字単位ではなく単語単位で動作します。
* **countdown** - （急いで実装された）カウントダウンシステムです。2 拍ごとに変化するため、秒として使いたい場合は 120bpm に設定してください。
* **countdown start** - カウントダウンを開始したい数値です
* _MOVE TO FRONT / MOVE TO BACK_ - [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention") を参照してください
