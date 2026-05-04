# ✅ Laser output 設定パネル

メニュー _View -> Laser Output Settings._ から _Laser output_ 設定パネルを開きます。

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

現在選択されているレーザーの設定が表示され、以下の方法で変更できます。

* _Laser overview_ パネルの番号ボタンから
* キーボードの数字キーから。1〜0 キーでレーザー 1〜10 を開きます
* `Tab` キーでレーザーを順番に切り替えます（`Shift + Tab` で逆方向）。

このパネルの上部には、以下があります。

* 番号ボタン - クリックすると、このレーザーをアーム/解除できます。レーザーがアームされていると赤になります。
* このレーザー専用の _Brightness_ スライダー。これはグローバルの明るさと組み合わされる点に注意してください。
* _Test Pattern_ トグルとパターンセレクター。このレーザー専用のテストパターンを選択できます。（これらのコントロールは Output view toolbar にも同じものがあります）。

### 出力の向き / ミラーリング補正

次の項目は、Liberation 内で一貫して動作するように、レーザーのセットアップを補正するためのものです。

* **Flip horizontal / vertical** - レーザーの出力を補正するためのオプションです

{% hint style="info" %}
レーザーの配線が誤っている場合、または背面の X/Y 反転ボタンが正しく設定されていない場合を除き、horizontal / vertical flip 設定を変更する必要はありません。特定の Clip だけ出力を反転したい場合は、Clip 側で設定できます。
{% endhint %}

* **Orientation** - レーザーが横向きまたは上下逆に設置されている場合、この設定で回転を補正できます。
* **Fine position adjustments** - ごく小さな位置ずれや回転の補正に使用できます。レーザーを一晩または長時間そのままにした場合のドリフトや落ち着きによるずれを補正するためのものです。

{% hint style="info" %}
orientation / mirroring 補正は 3D Visualiser 内の表示を変更しません。3D Visualiser の内容と実際のレーザー出力が一致するように、実機レーザーの出力を補正するために使用してください。
{% endhint %}

### レーザー設定のコピー

[Laser output 設定パネル](./#copy-laser-settings "mention") を参照してください。

### スキャナー設定

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed 設定は、スキャナーがどれだけ速く動くかを決定します。

{% hint style="danger" %}
デフォルト設定はかなり控えめですが、それでも速く動かしすぎるとスキャナーを損傷する可能性があります。特に Speed を上げる場合は注意してください。
{% endhint %}

{% hint style="info" %}
この Speed 設定はポイントレートを変更するものではなく、ポイント同士の間隔を調整します。詳しくは [◼️ Liberation がレーザーコンテンツを生成する仕組み](../../advanced/how-liberation-generates-laser-content.md "mention") を参照してください。
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

スキャナーがビームを動かしている間に、ビームの色が変わり、オン/オフも切り替わりますが、通常この 2 つは完全には同期していません。この設定を調整して、タイミングを揃えます。

{% hint style="info" %}
これは _blank shift_ と呼ばれることもありますが、個人的には _scanner sync_ という用語のほうが少し正確だと思っています。スキャナーの動きに対するすべての色変化のタイミングを調整するものだからです。
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>レーザーの「tails」 - Colour shift が正しく設定されていません</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>レーザーの「tails」なし！Colour shift は良好です！</p></figcaption></figure></div>

レーザー出力に小さな「tails」が見える場合は、scanner sync の調整が必要な可能性があります。どのように調整しても tails が残る場合は、スキャナーまたはレーザードライバーを、処理できる速度より速く駆動している可能性があります。Scanner speed を下げてみてください。

#### Scanner presets

事前に設計されたスキャナー設定を選択するために使用します。通常はデフォルトのオプションで問題ないため、特に性能の低い（または高い）スキャナーを使用している場合を除き、この設定を変更する必要はありません。さらに詳しく知りたい場合は、[◼️ Scanner プリセットとレンダープロファイル](../../advanced/scanner-presets.md "mention") を参照してください。

#### Colour calibration

このシステムを使用して、レーザーの明るさカーブとホワイトバランスを補正できます。[カラーキャリブレーション](../../advanced/colour-calibration.md "mention") を参照してください。

#### Advanced settings

通常、これらを調整する必要はありませんが、詳しく知りたい場合は [◼️ 高度なレーザー設定](../../advanced/advanced-laser-settings.md "mention") を参照してください。
