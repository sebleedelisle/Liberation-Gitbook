---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input oscillator

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

サウンド入力レベルをプロパティ値に変換します。

{% hint style="info" %}
Sound input oscillator はデフォルトのサウンドインターフェイスを使用しますが、_Preferences_ で変更できます。メニューから _Liberation -> Preferences_ を開いてください。

_Sound Input_ 設定では、使用するサウンドインターフェイスを選択できます。また、音量レベルを調整するためのいくつかの設定もあります。
{% endhint %}

* **range min / range max** - 波形をマッピングする最小値と最大値
* **channel** - サウンドインターフェイスに複数の入力チャンネルがある場合、ここで使用するチャンネルを選択できます。

{% hint style="info" %}
ミキシングデスクから複数のサウンドフィードを取り込むのは楽しいテクニックです。これにより、異なる Clip を異なる楽器に反応させることができます。
{% endhint %}

{% hint style="info" %}
すべての _Sound Inputs_ で同時に使用できるサウンドインターフェイスは 1 つだけです（_App Settings_ panel で選択）。この用途で複数のインターフェイスを使いたい場合、macOS では [Aggregate Device を作成](https://support.apple.com/en-gb/HT202000)して、複数の入力を 1 つの仮想サウンドソースにまとめることができます。（Windows にも同様のことができるアプリは多数ありますが、私は試していません）。
{% endhint %}

* **clamp min / clamp max** - 反応させたいレベル範囲を選択するために使用します。_App Settings_ panel の gate と limit 設定が適切に調整されていれば、通常はこれを調整する必要はありませんが、クリエイティブな効果にも使えます。

{% hint style="info" %}
Clip button に _Sound Input_ oscillator がある場合、小さなマイクアイコンが表示されます。

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
