---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Laser output 設定パネル

メニューの _View -> Laser Output Settings_ から、_Laser output_ 設定パネルを開きます。

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

ここでは、現在選択されているレーザーの設定を変更できます。対象のレーザーは次の方法で選択できます。

* _Laser overview_ パネルの番号ボタンを使う
* キーボードの数字キーを使う。1 から 0 のキーでレーザー 1 - 10 を開きます
* `Tab` キーでレーザーを順に切り替える（`Shift + Tab` で逆方向に切り替え）

このパネルの上部には、次の項目があります。

* 番号ボタン - クリックすると、このレーザーをアーム/ディスアームできます。レーザーがアーム状態のときは赤色になります。
* このレーザー専用の _Brightness_ スライダー。これは全体の明るさ設定と組み合わされる点に注意してください。
* _Test Pattern_ トグルとパターンセレクター。このレーザー専用のテストパターンを選択できます。（これらのコントロールは Output ビューのツールバーにもあります）

### 出力の向き / ミラーリング補正

次の項目は、Liberation 内でレーザーが一貫して動作するよう、レーザーのセットアップを補正するためのものです。

* **Flip horizontal / vertical** - レーザーの出力を補正するためのオプションです

{% hint style="info" %}
レーザーの配線が間違っている場合、または背面の X/Y 反転ボタンが正しく設定されていない場合を除き、horizontal / vertical flip の設定を変更する必要はありません。特定の Clip だけ出力を反転したい場合は、Clip 側で設定できます。
{% endhint %}

* **Orientation** - レーザーが横向きや上下逆さに設置されている場合、この設定で回転を補正できます。
* **Fine position adjustments** - ごく小さな位置ずれや回転の補正に使用できます。レーザーを一晩または長時間そのままにした後のドリフトやなじみによるずれを補正するためのものです。

{% hint style="info" %}
orientation / mirroring の補正は 3D Visualiser の表示には影響しません。3D Visualiser に表示されている内容と実際のレーザー出力を一致させるために使用してください。
{% endhint %}

### Copy laser settings

[#copy-laser-settings](laser-settings.md#copy-laser-settings "mention") を参照してください。

### Scanner settings

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed 設定は、スキャナーがどれだけ速く動くかを決定します。

{% hint style="danger" %}
デフォルト設定はかなり控えめですが、それでも速く動かしすぎるとスキャナーを損傷する可能性があります。特に Speed を上げる場合は注意してください。
{% endhint %}

{% hint style="info" %}
この Speed 設定はポイントレートを変更するものではなく、ポイント同士の間隔を調整します。詳しくは [◼️ Liberation がレーザーコンテンツを生成する仕組み](../advanced/how-liberation-generates-laser-content.md "mention") を参照してください。
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

スキャナーがビームを動かしている間、ビームは色を変えたりオン/オフしたりしますが、この 2 つは通常、完全には同期していません。この設定を調整して、タイミングを合わせます。

{% hint style="info" %}
これは _blank shift_ と呼ばれることもありますが、個人的には _scanner sync_ という表現の方が少し正確だと考えています。スキャナーの動きに対する、すべての色変化のタイミングを調整するためです。
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>レーザーの「テール」 - Colour shift が正しく設定されていない状態</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>レーザーの「テール」がない状態。Colour shift は良好です。</p></figcaption></figure></div>

レーザー出力に小さな「テール」が見える場合は、scanner sync の調整が必要な可能性があります。どのように調整してもテールが消えない場合は、スキャナーまたはレーザードライバーの処理能力を超える速さで動かしている可能性があります。Scanner speed を下げてみてください。

#### Scanner presets

事前に用意されたスキャナー設定を選択するために使用します。通常はデフォルトオプションで問題ないため、スキャナーの性能が特に低い（または高い）場合を除き、この設定を変更する必要はありません。さらに詳しく知りたい場合は、[◼️ Scanner プリセットとレンダープロファイル](../advanced/scanner-presets.md "mention") を参照してください。

#### Colour calibration

このシステムを使って、レーザーの明るさカーブとホワイトバランスを補正できます。[カラーキャリブレーション](../advanced/colour-calibration.md "mention") を参照してください。

#### Advanced settings

通常、これらを調整する必要はありませんが、詳しく知りたい場合は [◼️ 高度なレーザー設定](../advanced/advanced-laser-settings.md "mention") を参照してください。
