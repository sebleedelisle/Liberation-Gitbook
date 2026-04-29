---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input oscillator

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

將聲音輸入音量轉換為屬性值。

{% hint style="info" %}
Sound input oscillator 會使用預設的音訊介面，但你可以在 _Preferences_ 中變更。開啟選單 _Liberation -> Preferences_。

在 _Sound Input_ 設定中，你可以選擇要使用的音訊介面，也可以調整其他與音量大小相關的設定。
{% endhint %}

* **range min / range max** - 波形對應到的最小值與最大值
* **channel** - 如果你的音訊介面有多個輸入聲道，可以在這裡選擇要擷取哪一個聲道。

{% hint style="info" %}
從混音台取得多組聲音來源是一個很有趣的技巧，這樣就能讓不同 Clips 回應不同的樂器。
{% endhint %}

{% hint style="info" %}
所有 _Sound Inputs_ 一次只能使用一個音訊介面（在 _App Settings_ panel 中選取）。如果你想要使用多個介面，在 macOS 上可以[建立 Aggregate Device](https://support.apple.com/en-gb/HT202000)，把多個輸入合併成單一虛擬聲音來源。（Windows 上也有很多應用程式可以做到這件事，不過我沒有試過。）
{% endhint %}

* **clamp min / clamp max** - 用來選擇你想要回應的音量範圍。如果 gate 和 limit 設定（在 _App Settings_ panel 中）已正確調整，通常不需要調整這個項目；不過它也可以用來做一些創意效果。

{% hint style="info" %}
只要 Clip 按鈕上有 _Sound Input_ oscillator，你就會看到一個小麥克風圖示。

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
