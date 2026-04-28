---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input 振盪器

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

將聲音輸入音量轉換成屬性值。

{% hint style="info" %}
Sound input 振盪器會使用預設聲音介面，但你可以在 _Preferences_ 中更改。開啟選單 _Liberation -> Preferences._

在 _Sound Input_ 設定下，你可以選擇要使用哪個聲音介面，並調整一些與音量水平相關的其他設定。
{% endhint %}

* **range min / range max** - 波形會映射到的最小值和最大值
* **channel** - 如果你的聲音介面有多於一個輸入通道，可以在這裡選擇要接收哪一個通道。

{% hint style="info" %}
一個有趣的做法是從混音台取得多組聲音訊號，這樣就可以讓不同 Clip 回應不同樂器。
{% endhint %}

{% hint style="info" %}
所有 _Sound Inputs_（在 _App Settings_ 面板中選取）同一時間只能使用一個聲音介面。如果你想為此使用多於一個介面，在 macOS 上可以[建立 Aggregate Device](https://support.apple.com/en-gb/HT202000)，將多個輸入合併成單一虛擬聲音來源。（Windows 上也有很多 app 可以做到這件事，但我未試過。）
{% endhint %}

* **clamp min / clamp max** - 用來選擇你想回應的音量水平範圍。如果 gate 和 limit 設定（在 _App Settings_ 面板中）已正確調整，通常不需要更改這項；不過它們也可用於一些創意效果。

{% hint style="info" %}
只要 Clip 有 _Sound Input_ 振盪器，你會在 Clip 按鈕上看到一個小咪高峰圖示。

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
