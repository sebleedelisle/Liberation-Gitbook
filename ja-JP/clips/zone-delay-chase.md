---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

レーザーの数が多いほど楽しくなる、という点には誰もが同意するでしょう。ただし、すべてのレーザーがまったく同じ動きをしているだけでは、クリエイティブな可能性を活かしきれません。

Zone delay システムは、ゾーンごとに変化を加えるためのシンプルで効果的な方法です。複数レーザーのセットアップをより活用できます。また、従来型の chase エフェクトを作る用途にも使用できます。

#### 仕組み

_Zone delay_ は、各ゾーンで clip のタイミングに遅延を加え、ゾーン全体にスイープするような動きを作ります。

すでに再生中の clip に zone delay を加えると非常に効果的です。APC40 の対応するコントロールを使って、レベルや pattern を調整できます（[APC40 リファレンス](../reference/apc40-reference.md "mention") を参照）。または、_Clip Settings_ パネルから設定することもできます。

Zone delay settings :

* **Zone delay** - 各ゾーンに適用する遅延時間の量を制御します。単位は 64分音符です。
* **Pattern** - ゾーンの順序を選択します。
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern はゾーン番号に基づいて動作し、ゾーンが左から右の順に並んでいることを前提とします。Zone delay は pattern を計算する際、canvas zones と DMX zones を別々のグループとして扱います。
{% endhint %}

* **Delay mode**
  1. No delay - chase mode で使用します。
  2. Delay - デフォルトのモードです。各ゾーンのタイミングを遅らせます。
  3. Delay with re-trigger - pattern に沿って進むたびに、clip を毎回先頭にリセットします。_Chase mode_ と組み合わせると効果的です。
* **Chase mode** - chase mode をオンにすると、各ゾーンが従来の chase エフェクトのようにオン／オフされます。_Fade in, Hold,_ and _Fade out_ settings を使って chase の見え方を調整します。これらの設定は zone delay 値に対する割合として設定されるため、値が 1 の場合は _Zone delay_ の値で指定した時間と同じになります。少し説明しにくいので、実際に試してみることをおすすめします。

{% hint style="info" %}
Zone delay は、有効になっているすべてのエフェクトにも適用されます。たとえば、点滅エフェクトは clip 内のアニメーションと同様に、ゾーン間で遅延されます。
{% endhint %}

clip に何らかの _Zone delay_ が設定されている場合、clip の右上に三点アイコンが表示されます。この点はアニメーションし、その clip の _Zone delay_ のスタイルを示します。詳しくは [Clipボタンに表示される小さなアイコンは何ですか？](what-are-the-small-icons-on-the-clip-buttons.md "mention") を参照してください。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>clip に zone delay が設定されていることと、そのモードを示す三点シンボル</p></figcaption></figure>

{% hint style="info" %}
Zone delay は各 clip に属する設定であり、グローバル設定ではありません。clip のクリエイティブなデザインの一部です。
{% endhint %}
