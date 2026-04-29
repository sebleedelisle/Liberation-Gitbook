---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 依位置變化的變更器

這一系列 node 會依照位置修改內容。預設會沿著水平軸套用效果（由左到右），但你可以將這條軸旋轉到任何角度。每個 node 也包含 _radial_ 模式，會依照每個點相對於中心的角度來驅動效果。

* **Colour Changer by Position** – 沿著選定軸線或依 radial 角度偏移色彩。\
  \&#xNAN;_範例：建立掃過線條的彩虹漸層，或在圓形上使用 radial 模式，產生色輪效果。_
* **Wave Shift by Position** – 套用正弦波失真，將內容垂直偏移（或沿著所選軸線的垂直方向偏移）。\
  \&#xNAN;_範例：讓線條像水面一樣起伏，或使用 radial 模式讓圓形從中心向外脈動。_
* **Noise Shift by Position** – 套用 simplex noise 失真，將內容垂直偏移（或沿著所選軸線的垂直方向偏移）。\
  \&#xNAN;_範例：效果類似 Wave Shift 範例，但更有機、更隨機，非常適合加入自然變化。_

## &#x20;依位置變更色彩

這個 node 會依照位置在內容上套用色彩變化。預設軸線為水平（0°），但你可以旋轉軸線，或切換到 radial 模式。

* **wavelength** – 設定重複色彩循環的大小。
  * _Linear 模式：_ 在 100% 時，一個完整循環會跨越內容的完整寬度。
  * _Radial 模式：_ 在 100% 時，一個完整循環會跨越整個圓（360°）。數值為圓周的百分比：例如 50% = 半個圓（180°）。
* **offset** – 以 wavelength 的百分比偏移色彩循環的起點。你可以調變這個設定（例如使用 sawtooth oscillator），讓色彩平順循環。
* **repeat** – 啟用時，循環會在內容上重複。停用時，漸層只會套用一次：起點之前的所有內容都是起始色，終點之後的所有內容都是結束色。
* **pingpong** – 啟用時，每次重複都會交替方向，產生鏡射效果。如果 _Repeat_ 停用，漸層會先向前再返回一次。_注意：在 Pingpong 模式中，wavelength 會涵蓋正向與返回的掃描。_
* **linear angle** – 旋轉效果的軸線。0° = 水平。
* **radial** – 切換到 radial 模式，依照相對中心的角度套用色彩。
* **radial smooth loop** – 自動調整 wavelength，讓它能平均分割圓周的 100%，避免循環接回時出現可見接縫。

**色彩模式**

這些設定決定哪些色彩調整會套用到內容上。另請參閱：[色彩設定與 HSB](../fundamentals/colour-settings-and-hsb.md)。

* **hue mode**
  * _OFF_ – hue 不變。
  * _FIXED_ – hue 強制設為固定值。
  * _SHIFTED_ – hue 依指定量偏移（不同顏色的元素仍會保持彼此區別，但會一起沿著色輪偏移）。
* **saturation mode**
  * _OFF_ – saturation 不變。
  * _FIXED_ – saturation 設為指定值。
* **brightness mode**
  * _OFF_ – brightness 不變。
  * _FIXED_ – brightness 設為指定值。
  * _MULTIPLY_ – brightness 依指定值縮放。這會保留動態變化（例如閃爍元素仍會閃爍，但限制在較低的亮度範圍內）。

**起始 / 結束值**

這些滑桿定義沿著所選軸線（或 radial 掃描）套用的色彩範圍。

* **start hue** – 漸層起點的 hue。
* **end hue** – 漸層終點的 hue。
* **start saturation** – 起點的 saturation。
* **end saturation** – 終點的 saturation。
* **start brightness** – 起點的 brightness。
* **end brightness** – 終點的 brightness。
* **blend** – 將色彩變化與原始色彩混合。100% 時，效果會完全取代原始色彩。

**範例 1：滑動的彩虹漸層**

從預設設定開始：

1. 讓 node 保持在 **Linear** 模式（0° 角度 = 水平）。
2. 讓 **wavelength** 保持 100%（跨越完整寬度，這應該也是預設值）。
3. 讓起始與結束值保持預設。
4. 啟用 **repeat**。
5. 在 **offset** 設定加入一個從 0% 到 100% 的 **Sawtooth Oscillator**。

***

**範例 2：黑–白–黑漸層（Pingpong）**

從預設設定開始：

1. 讓 node 保持在 **Linear** 模式（0° 角度 = 水平）。
2. 讓 **wavelength** 保持 100%（跨越完整寬度，這應該也是預設值）。
3. 關閉 **repeat**。
4. 將 **start brightness** 設為 0（黑色）。
5. 將 **end brightness** 設為 100（白色）。
6. 將 **start saturation** 和 **end saturation** 設為 0（轉為灰階）。
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. 啟用 **pingpong**。

_結果：漸層會在寬度方向上從黑色淡入到白色，再淡回黑色。_\
請注意，如果你希望內容保留原本的 hue 和 saturation，請將 **saturation mode** 設為 OFF。 \\

***

**範例 3：旋轉彩虹色輪（Radial）**

1. 啟用 **radial** 模式。
2. 將 **wavelength** 設為 100%（完整 360° 掃描）。
3. 開啟 **repeat**。
4. 在 **offset** 設定加入一個從 0% 到 100% 的 **Sawtooth Oscillator**。

_結果：產生一個會持續繞著圓形旋轉、無接縫的色輪。_

## &#x20;依位置偏移波形

這個 node 會在內容上套用波形失真，將點沿著所選軸線的垂直方向偏移（或從中心做 radial 偏移）。

* **Wavelength** – 設定波形循環的長度。
  * _Linear 模式：_ 在 100% 時，一個完整循環會跨越內容的完整寬度。
  * _Radial 模式：_ 在 100% 時，一個完整循環會跨越完整 360°。（數值為圓周的百分比：50% = 半圈、25% = 四分之一圈，依此類推。）
* **Size** – 控制波形的振幅（內容位移的距離）。
* **Offset** – 沿著軸線偏移波形（在 radial 模式中則沿著圓周偏移）。這是 wavelength 的百分比，因此你可以使用 **Oscillator Node** 讓波形移動。
* **Radial** – 從 linear 切換到 radial 模式，讓位移依照相對中心的角度決定。
* **Radial Smooth Loop** – 調整 wavelength，讓它能平均分割圓周的 100%，避免循環接回時出現可見接縫。
* **Triangle** – 將波形形狀從正弦波改為三角波。
* **Absolute** – 取波形的絕對值，只產生向上的位移（將負值側摺到正值側）。
* **Angle** – 旋轉波形的軸線。0° = 水平。

## &#x20;依位置偏移雜訊

這個 node 會使用雜訊場（類似亂流）扭曲內容，將點沿著所選軸線的垂直方向偏移（或從中心做 radial 偏移）。與 _Wave Shift_ 相比，結果更有機、更隨機。

* **Detail** – 控制雜訊的細緻程度。較高的值 = 較銳利、細節更多的變化。較低的值 = 較平滑的變化。
* **Wavelength** – 設定雜訊圖案的尺度。
  * _Linear 模式：_ 在 100% 時，一個完整雜訊循環會跨越內容寬度。
  * _Radial 模式：_ 在 100% 時，一個完整循環會跨越完整 360°。
* **Size** – 控制位移量（雜訊失真的振幅）。
* **Offset** – 沿著軸線偏移雜訊圖案（或沿著圓周偏移）。這是 wavelength 的百分比，因此你可以使用 **Oscillator Node** 讓雜訊「流動」。
* **Depth Offset** – 在 3D 雜訊場中移動，隨時間產生變化。搭配 Oscillator Node 進行動畫時特別有效。
* **Depth Detail** – 控制深度維度中的變化細節程度。
* **Absolute** – 取雜訊的絕對值，將負值摺到正值（只產生單側位移）。
* **Radial** – 從 linear 切換到 radial 模式，讓位移依照相對中心的角度決定。
* **Radial Smooth Loop** – 調整 wavelength，讓它能平均分割圓周的 100%，避免 radial 模式中出現可見接縫。
