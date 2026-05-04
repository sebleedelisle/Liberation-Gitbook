---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 按位置變更器

這一系列節點會根據位置修改內容。預設情況下，效果會沿水平軸套用（由左至右），但你可以將這條軸旋轉至任何角度。每個節點亦包含 _radial_ 模式，效果會由每個點相對於中心的角度驅動。

* **Colour Changer by Position** – 沿所選軸或圍繞徑向角度套用漸變。\
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
* **legacy mode** – 切換回較舊的 start/end HSB 滑桿。保持關閉即可使用較新的漸變編輯器。

**Colour Modes**

這些設定決定哪些顏色調整會套用到內容上。另見：[顏色設定與 HSB](../fundamentals/colour-settings-and-hsb.md "mention")。

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

**Gradient editor**

使用與 [顏色變更](colour-changer.md "mention") 相同的漸變編輯器，但會按位置將漸變映射到內容上。

* 按一下漸變列即可加入顏色停點。
* 左鍵按一下停點即可選取，然後向左右拖曳來移動。
* 將已選取的停點向下拖離漸變列，或按 Delete/Backspace，即可移除。漸變最少會保留兩個停點。
* 右鍵按一下停點，即可使用取色器編輯。
* 使用 **Position**、**Hue**、**Saturation** 和 **Brightness** 精確編輯已選取的停點。
* **interpolation** 選擇停點之間的顏色混合方式：
* **HSB** – 混合 hue、saturation 和 brightness。最適合在色相環上製作平滑的彩虹式移動。
* **RGB** – 直接混合紅、綠、藍數值。這通常較像螢幕或燈光控制台的顏色淡變。
* **NONE** – 不作混合，直接由一個停點跳到下一個停點。
* **hue direction** 可在 HSB interpolation 中使用：
* **AUTO** – 沿色相環採用最短路徑。
* **FORWARDS** – 一律沿 hue 數值向前移動。
* **BACKWARDS** – 一律沿 hue 數值向後移動。
* **blend** – 將顏色變化與原本顏色混合。100% 時，效果會完全取代原本顏色。

**Legacy start / end values**

如果開啟 **legacy mode**，漸變編輯器會由較舊的控制項取代：

* **start hue / end hue** – 範圍起點和終點的 hue。
* **start saturation / end saturation** – 範圍起點和終點的 saturation。
* **start brightness / end brightness** – 範圍起點和終點的 brightness。

**範例 1：滑動彩虹漸變**

由預設設定開始：

1. 將節點保持在 **Linear** 模式（0° angle = 水平）。
2. 將 **wavelength** 保持在 100%（橫跨整個寬度，亦應為預設值）。
3. 保留預設漸變。
4. 啟用 **repeat**。
5. 在 **offset** 設定加入一個由 0% 到 100% 的 **Sawtooth Oscillator**。

***

**範例 2：黑–白–黑漸變（Pingpong）**

由預設設定開始：

1. 將節點保持在 **Linear** 模式（0° angle = 水平）。
2. 將 **wavelength** 保持在 100%（橫跨整個寬度，亦應為預設值）。
3. 關閉 **repeat**。
4. 將第一個漸變停點設為黑色。
5. 將最後一個漸變停點設為白色。
6. 將 **hue mode** 設為 OFF。
7. 如要強制結果為灰階，將 **saturation mode** 設為 FIXED。
8. 將 **brightness mode** 設為 FIXED。
9. 啟用 **pingpong**。

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
* **Angle** – 在線性模式中旋轉 noise 的軸。0° = 水平。
* **Radial** – 由 linear 切換至 radial 模式，使位移根據相對中心的角度計算。
* **Radial Smooth Loop** – 調整 wavelength，使其可平均分割圓周的 100%，避免 radial 模式下出現可見接縫。
