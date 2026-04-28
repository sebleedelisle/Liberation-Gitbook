---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 色彩設定與 HSB

Liberation 內的顏色是以 HSB 定義，而不是 RGB。你可能未必熟悉這套系統，但習慣之後，我覺得它直觀得多。

{% hint style="info" %}
如果你偏好使用 RGB，可以在任何色彩設定中按一下顏色方格。這會開啟 colour editor panel，當中提供 RGB 和 HSB 選項。
{% endhint %}

### HSB - Hue、Saturation 與 Brightness

#### Hue

顏色色相的範圍是 0 至 255。0 是紅色；數值增加時，會依次經過彩虹中的各種色相：橙色、黃色、綠色、青色、藍色、紫色、洋紅色，然後在 255 回到紅色。

由於這是一個循環，你可以使用 triangle wave 來循環掃過所有顏色。

#### Saturation

此設定會調整顏色的飽和度或鮮艷程度。換句話說，就是顏色有多「_有色彩_」，範圍是 0 至 255。將 saturation 設為 0 會得到灰階；設為 255 則是完整的彩虹色彩。中間值會產生較淡、較洗淡的粉彩色。

{% hint style="info" %}
各位美國朋友，抱歉，英文單字 colour 多了一個母音。Liberation 在英格蘭製作，所以預設使用英式英文。將來我希望提供法文、西班牙文、德文、意大利文、簡體中文的翻譯，對，甚至包括美式英文。:innocent:
{% endhint %}

#### Brightness

這大概是最容易理解的：0 是完全黑色，255 是最高亮度。

### 使用例子

#### 彩虹循環：

將 _Brightness_ 和 _Saturation_ 設為 255。將 _Sawtooth_ oscillator 連接到 _Hue_ socket，並將其範圍調整為 0 至 255。

#### 亮度脈衝：

將 _Sawtooth_ oscillator 連接到 _Brightness_ socket，並將其範圍調整為 255 至 0。你可以進一步調整 clamp min 和 max，控制變化的持續時間。然後使用 easing functions 進一步微調動畫。

#### 強閃 / 頻閃：

使用 _Hue_ 和 _Saturation_ 選擇顏色，或按一下 colour picker。將 _Square Wave_ oscillator 連接到 _Brightness_ socket，並將其範圍調整為 255 至 0。

#### 在自訂色相範圍內循環：

將 _Brightness_ 和 _Saturation_ 設為 255。將 _Triangle Wave_ oscillator 連接到 _Hue_ socket，並調整其範圍：

* 藍色至青色：使用 70 至 128 的範圍
* 紅色至黃色：使用 0 至 40 的範圍
* 紅色至洋紅色：使用 255 至 220 的範圍
