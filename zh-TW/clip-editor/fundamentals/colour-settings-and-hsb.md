---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 顏色設定與 HSB

Liberation 中的顏色是以 HSB 定義，而不是 RGB。你可能還不熟悉這套方式，但我覺得習慣之後，它會是直覺得多的系統。

{% hint style="info" %}
如果你偏好使用 RGB，可以在任何顏色設定中點擊顏色方塊。這會開啟顏色編輯器面板，裡面提供 RGB 和 HSB 的選項。
{% endhint %}

### HSB - Hue、Saturation 與 Brightness

#### Hue

色相的範圍是 0 到 255。0 是紅色，隨著數值增加，你會依序經過彩虹中的所有色相：橙色、黃色、綠色、青色、藍色、紫色、洋紅色，最後在 255 回到紅色。

因為這是一個循環，你可以使用三角波來循環播放所有顏色。

#### Saturation

這個設定會調整顏色的飽和度，也就是顏色有多_鮮豔_，範圍從 0 到 255。將 Saturation 設為 0 會得到灰階；設為 255 則會得到完整的彩虹色彩。介於中間的數值會產生較淡、偏粉彩的顏色。

{% hint style="info" %}
向我的美國朋友們致歉，因為 colour 這個字多了一個母音。Liberation 是在英格蘭製作的，所以預設使用英式英文。未來我希望能提供法文、西班牙文、德文、義大利文、簡體中文，沒錯，甚至還有美式英文的翻譯。:innocent:
{% endhint %}

#### Brightness

這大概是最容易理解的設定：0 是完全黑色，255 是全亮度。

### 使用範例

#### 彩虹循環：

將 _Brightness_ 和 _Saturation_ 設為 255。將 _Sawtooth_ 振盪器連接到 _Hue_ 插槽，並將它的範圍調整為 0 到 255。

#### 亮度脈衝：

將 _Sawtooth_ 振盪器連接到 _Brightness_ 插槽，並將它的範圍調整為 255 到 0。你也可以進一步調整 clamp min 和 max，來控制變化的持續時間。接著使用 easing 函式進一步微調動畫。

#### 強烈閃光／頻閃：

使用 _Hue_ 和 _Saturation_ 選擇顏色，或點擊顏色選擇器來選色。將 _Square Wave_ 振盪器連接到 _Brightness_ 插槽，並將它的範圍調整為 255 到 0。

#### 在自訂色相範圍內循環：

將 _Brightness_ 和 _Saturation_ 設為 255。將 _Triangle Wave_ 振盪器連接到 _Hue_ 插槽，並調整它的範圍：

* 藍色到青色使用 70 到 128 的範圍
* 紅色到黃色使用 0 到 40 的範圍
* 紅色到洋紅色使用 255 到 220 的範圍
