---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Wave oscillators

## このページの内容：

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Sawtooth wave](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Triangle wave](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sine wave](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Square wave](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Wave oscillator settings

すべての Wave oscillator には、次の設定があります：

* **range min / range max** - oscillator が制御するプロパティの値の範囲を決めます。波形が一番下にあるとき、プロパティは _range min_ に設定されます。波形が一番上にあるとき、プロパティは _range max_ に設定されます。

{% hint style="info" %}
たとえば、ドットを -100 から 100 の間で左右に動かしたい場合は、oscillator を _x property socket_ に接続し、_min range_ を -100、_max range_ を 100 に設定します。
{% endhint %}

* **duration** - 1 サイクル（または _loop_）が完了するまでの時間です。テンポに対する小節単位の相対値です。つまり ¼ は 1 拍、1 は 1 小節です。
* **duration multiplier** - 基本の duration に、選択した係数を掛けます。たとえば duration を 4 分音符に設定し、multiplier を 3 にすると、oscillator は 4 分音符 3 つ分（付点 2 分音符）の長さになります。小数の multiplier にも対応しています。スライダーをドラッグするときに _SHIFT_ を押したままにすると整数以外の値を設定でき、フェージング効果や微妙なタイミングのずれを作るときに便利です。
* **offset** - duration に対する割合で指定する、波形の開始オフセットです。波形を 4 分の 1 進んだ位置から開始したい場合は、25% に設定します。
* **repeat count** - 停止するまでに loop を実行する回数です。デフォルトは _FOREVER_ ですが、oscillator を無期限に動かしたくない場合は変更できます。停止後、プロパティは波形の終端の値に設定されます。
* **delay count** - oscillator が動作を開始するまでの拍数による遅延です。動作開始前、プロパティは波形の開始値に設定されます。

{% hint style="info" %}
_repeat count_ と _delay count_ をうまく使うと、独自のタイムラインのように、非常に複雑なアニメーションを作成できます。
{% endhint %}

## Common settings

* **steps** - モーションをいくつかの離散的なステップに分割します。プロパティを滑らかに動かすのではなく、値へ「ジャンプ」させたい場合に便利です。

{% hint style="info" %}
steps は値ではなく時間で分割される点に注意してください。たとえば duration が 1 小節の波形を 4 steps に分割した場合、プロパティは 1 拍ごとに即座に変化します。
{% endhint %}

* **clamp min / clamp max -** 波形のスケールを最小値または最大値の範囲外まで広げ、結果をクランプします。

{% hint style="info" %}
_clamp_ の概念は少し説明しにくいのですが、波形がグラフの上端または下端を越えて、そのあと端に押さえ込まれるようなイメージです。実際に試してみることをおすすめします。のこぎり波の開始を遅らせたり、早めに終わらせたりしたい場合にとても便利です。
{% endhint %}

* **ease function** - Sawtooth wave と Triangle wave には ease function もあり、アニメーションカーブを微妙に変化させて、より表現力のあるアニメーションにできます。
  * **LINEAR** - デフォルトです。イージングなしで、min と max の値の間を直線的に移動します。
* **EASE OUT** - 最初は速く、終わりに近づくにつれて減速します。停止に向けて遅くなるような物理的な動きのシミュレーションに適しています。
  * **EASE IN** - ゆっくり始まり、徐々に加速します。勢いがついていく動きのシミュレーションに適しています。
  * **EASE IN/OUT** - 両方を組み合わせたもので、とても自然な動きになります。

{% hint style="warning" %}
**Easing -** ロボットのような動きを意図している場合を除き、デフォルトのリニアアニメーションはできるだけ避けることをおすすめします。Easing を使うと、アニメーションがずっと滑らかで自然になります。
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sawtooth wave

_cycle_ の最後で急激に下がる前に上昇していくため、_ramp waveform_ と呼ばれることもあります。おそらく最も一般的な Wave oscillator で、_hue_ や _rotation_ のようなプロパティを循環させる loop を作成できます。

次の項目については、上記のセクションを参照してください：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Sawtooth 固有の設定：

* **cycle range compensation** - **steps** が設定されている場合に使用できます。たとえば 0 から 360 までの rotation のように、値を循環させる場合に便利です。これを設定しない場合、開始値と終了値が同じになり、開始点で引っかかるように見えることがあります（0 と 360 は同じ角度のため）。これをオンにすると、ステップ位置を補正するために最大範囲が縮小されます。

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Triangle wave

_cycle_ ごとに先頭へジャンプして戻る _sawtooth wave_ とは異なり、_triangle wave_ は直線的に前進してから、直線的に戻ります。

次の項目については、上記のセクションを参照してください：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sine wave

最も滑らかな波形です。振り子のように、2 つの値の間を穏やかに振動します。

次の項目については、上記のセクションを参照してください：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Square wave

最もシンプルな波形です。2 つの値の間を行ったり来たりするだけです。

次の項目については、上記のセクションを参照してください：

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Square wave 固有の設定：

* **pulse width** - 全体の duration に対して、波形が最大値でいる時間の長さです。デフォルトは 50% で、ちょうど半分ずつになります。4 分の 1 の時間だけ「オン」にしたい場合は、25% に設定します。このパルスが発生するタイミングは _offset_ の値で調整できます。

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

Liberation の強みのひとつは、ランダムでありながら再現可能なエフェクトを生成できることです。_noise_ oscillator を使うと、必要なだけ細かさや揺らぎを持たせた、有機的にループするランダムモーションを作成できます。

次の項目については、上記のセクションを参照してください：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Noise 固有の設定：

* **noise type** - noise の生成に使用するアルゴリズムです。
  * **SIMPLEX** - デフォルトです。ゆったりと上下しながら、loop で繰り返す値です。
  * **RANDOM** - より一般的な乱数アルゴリズムを使用します。完全にノイジーでカオスな動きになります。

{% hint style="info" %}
**Simplex noise** は、Ken Perlin が 1983 年に映画 _Tron_ の制作の一環として開発した「Perlin noise」アルゴリズムを改良するものとして、2001 年に設計されました（その功績でアカデミー賞を受賞しています）。

このいわゆる「gradient」noise は、それ以前の「機械的」なコンピューター生成画像への不満から生まれました。CGI の世界では、雲、水面、さらにはリアルな地形用の height-map のレンダリングに特に適しています。

Liberation では、一見予測できないのに滑らかで自然なモーションを作るのに役立ちます。
{% endhint %}

* **seed** - noise の作成に使用される値です。現在の noise wave の見た目が気に入らない場合は、この値を変更してみてください。

{% hint style="info" %}
ちょっとマニアックな豆知識です。完全にループする simplex noise を得るために、2D noise plane 上の円をたどるように反復しています。そして seed 値を変更すると、この平面が第 3 の次元方向へ移動します。
{% endhint %}

* **simplex detail** - noise の細かさや揺らぎ具合を変更します。繰り返しパターンを目立ちにくくしたい場合は、duration を長くし、この値を大きくします。

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

完全にカスタムの波形を作成します。複雑なアニメーションを作成する場合にとても便利です。

次の項目については、上記のセクションを参照してください：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

この下には、位置と値のリストがあります。duration は 64 steps に分割され、これらの任意のポイントに値を配置できます。

各 step には、次の設定があります：

* **Step** - duration 内の時間ステップです。0 が開始位置、64 が終了位置です。
* **Level** - その時間ステップでの波形のレベルです。レベルの範囲は 0 から 1 です。
* **Animation type** - ドロップダウンメニューで、前の step からこのレベルへどのように移動するかを選択できます。
  * **None** - トランジションなしで、指定した時間にこのレベルへ直接ジャンプします。
  * **Linear** - 前のレベルからこのレベルまで、完全に直線的に移動します。
  * **Ease in / Ease out / Ease in/out** - 前のレベルからこのレベルまでイージングします。アニメーションタイプの説明については、上記の _ease function_ を参照してください。

***
