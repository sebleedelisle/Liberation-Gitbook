---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 按位置變更器

這一系列節點會根據位置修改內容。預設情況下，效果會沿水平軸套用（由左至右），但你可以將這條軸旋轉至任何角度。每個節點亦包含 _radial_ 模式，效果會由每個點相對於中心的角度驅動。

* **Colour Changer by Position** – 沿所選軸或圍繞徑向角度偏移顏色。\
  \&#xNAN;_範例：建立一道橫掃直線的彩虹漸變，或在圓形上使用 radial 模式，製作色輪效果。_
* **Wave Shift by Position** – 套用正弦波扭曲，將內容垂直偏移（或沿所選軸的垂直方向偏移）。\
  \&#xNAN;_範例：令直線像水面一樣起伏，或使用 radial 模式令圓形由中心向外脈動。_
* **Noise Shift by Position** – 套用 simplex noise 扭曲，將內容垂直偏移（或沿所選軸的垂直方向偏移）。\
  \&#xNAN;_範例：效果類似 Wave Shift 範例，但更自然和隨機，非常適合加入自然變化。_

## &#x20;按位置改變顏色

此節點會根據位置在你的內容上套用顏色變化。預設軸向為水平（0°），但你可以旋轉它，或切換至 radial 模式。

* **wavelength** – 設定重複顏色循環的大小。
  * _Linear mode:_ 100% 時，一個完整循環會橫跨內容的整個寬度。
  * _Radial mode:_ 100% 時，一個完整循環會覆蓋整個圓（360°）。數值是圓周的百分比：例如 50% = 半個圓（180°）。
* **offset** – 以 wavelength 的百分比偏移顏色循環的起點。你可以對它進行調變（例如使用 sawtooth oscillator），令顏色平滑循環。
* **repeat** – 啟用後，循環會在內容上重複。如果停用，漸變只會套用一次：起點之前的所有內容都是起始顏色，終點之後的所有內容都是結束顏色。
* **pingpong** – 啟用後，每次重複都會交替方向，產生鏡像效果。如果 _Repeat_ 已停用，漸變會向前再向後一次。_注意：在 Pingpong 模式下，wavelength 會涵蓋向前及返回兩段掃描。_
* **linear angle** – 旋轉效果的軸向。0° = 水平。
* **radial** – 切換至 radial 模式，根據相對中心的角度套用顏色。
* **radial smooth loop** – 自動調整 wavelength，使其可平均分割圓周的 100%，避免循環接合位置出現明顯接縫。

**Colour Modes**

這些設定決定哪些顏色調整會套用到內容上。另見：[顏色設定與 HSB](../fundamentals/colour-settings-and-hsb.md)。

* **hue mode**
  * _OFF_ – hue 不變。
  * _FIXED_ – hue 強制設為固定值。
  * _SHIFTED_ – hue 按指定數值偏移（不同顏色的元素仍會保持區別，但會一起沿色輪偏移）。
* **saturation mode**
  * _OFF_ – saturation 不變。
  * _FIXED_ – saturation 設為指定值。
* **brightness mode**
  * _OFF_ – brightness 不變。
  * _FIXED_ – brightness 設為指定值。
  * _MULTIPLY_ – brightness 按指定值縮放。這會保留動態變化（例如閃爍元素仍會閃爍，但會限制在指定亮度範圍內）。

**Start / End Values**

這些滑桿定義沿所選軸（或徑向掃描）套用的顏色範圍。

* **start hue** – 漸變起點的 hue。
* **end hue** – 漸變終點的 hue。
* **start saturation** – 起點的 saturation。
* **end saturation** – 終點的 saturation。
* **start brightness** – 起點的 brightness。
* **end brightness** – 終點的 brightness。
* **blend** – 將顏色變化與原本顏色混合。100% 時，效果會完全取代原本顏色。

**範例 1：滑動彩虹漸變**

由預設設定開始：

1. 將節點保持在 **Linear** 模式（0° angle = 水平）。
2. 將 **wavelength** 保持在 100%（橫跨整個寬度，亦應為預設值）。
3. 保持 start 和 end 數值為預設。
4. 啟用 **repeat**。
5. 在 **offset** 設定加入一個由 0% 到 100% 的 **Sawtooth Oscillator**。

***

**範例 2：黑–白–黑漸變（Pingpong）**

由預設設定開始：

1. 將節點保持在 **Linear** 模式（0° angle = 水平）。
2. 將 **wavelength** 保持在 100%（橫跨整個寬度，亦應為預設值）。
3. 關閉 **repeat**。
4. 將 **start brightness** 設為 0（黑色）。
5. 將 **end brightness** 設為 100（白色）。
6. 將 **start saturation** 和 **end saturation** 設為 0（轉換為灰階）。
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. 啟用 **pingpong**。

_結果：漸變會在寬度上由黑色淡入至白色，然後再返回黑色。_\
請注意，如果你想內容保留原本的 hue 和 saturation，請將 Saturation mode 設為 OFF。 \\

***

**範例 3：旋轉彩虹色輪（Radial）**

1. 啟用 **radial** 模式。
2. 將 **wavelength** 設為 100%（完整 360° 掃描）。
3. 開啟 **repeat**。
4. 在 **offset** 設定加入一個由 0% 到 100% 的 **Sawtooth Oscillator**。

_結果：一個無縫色輪會圍繞圓形持續旋轉。_

## &#x20;按位置波形偏移

此節點會在你的內容上套用波形扭曲，將點沿所選軸的垂直方向偏移（或由中心作徑向偏移）。

* **Wavelength** – 設定波形循環的長度。
  * _Linear mode:_ 100% 時，一個完整循環會橫跨內容的整個寬度。
  * _Radial mode:_ 100% 時，一個完整循環會覆蓋整個 360°。（數值是圓周的百分比：50% = 半圈，25% = 四分之一圈，如此類推。）
* **Size** – 控制波形的振幅（內容被位移的距離）。
* **Offset** – 沿軸向偏移波形（或在 radial 模式下沿圓周偏移）。這是 wavelength 的百分比，因此你可以用 **Oscillator Node** 為它加入動畫，令波形移動。
* **Radial** – 由 linear 切換至 radial 模式，使位移根據相對中心的角度計算。
* **Radial Smooth Loop** – 調整 wavelength，使其可平均分割圓周的 100%，避免循環接合位置出現可見接縫。
* **Triangle** – 將波形形狀由正弦波改為三角波。
* **Absolute** – 取波形的絕對值，只產生向上的位移（將負值一側摺到正值一側）。
* **Angle** – 旋轉波形的軸向。0° = 水平。

## &#x20;按位置雜訊偏移

此節點會使用 noise field（類似 turbulence）扭曲內容，將點沿所選軸的垂直方向偏移（或由中心作徑向偏移）。與 _Wave Shift_ 相比，結果更自然和隨機。

* **Detail** – 控制 noise 的精細程度。數值越高，變化越銳利、細節越多；數值越低，變化越平滑。
* **Wavelength** – 設定 noise 圖案的尺度。
  * _Linear mode:_ 100% 時，一個完整 noise 循環會橫跨內容寬度。
  * _Radial mode:_ 100% 時，一個完整循環會覆蓋整個 360°。
* **Size** – 控制位移量（noise 扭曲的振幅）。
* **Offset** – 沿軸向（或沿圓周）偏移 noise 圖案。這是 wavelength 的百分比，因此你可以用 **Oscillator Node** 為它加入動畫，令 noise「流動」。
* **Depth Offset** – 在 3D noise field 中移動，隨時間產生變化。配合 Oscillator Node 製作動畫時特別有效。
* **Depth Detail** – 控制深度維度上的變化細節程度。
* **Absolute** – 取 noise 的絕對值，將負值摺到正值（只產生單向位移）。
* **Radial** – 由 linear 切換至 radial 模式，使位移根據相對中心的角度計算。
* **Radial Smooth Loop** – 調整 wavelength，使其可平均分割圓周的 100%，避免 radial 模式下出現可見接縫。
