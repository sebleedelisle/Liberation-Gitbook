---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 顏色變更

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> 顏色變更

更改所有輸入內容的顏色。你可以設定固定的 HSB 數值，或切換至漸變系統，從自訂漸變中取樣顏色。

* **hue, saturation, brightness** - 顏色數值，請參閱[顏色設定及 HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - 不會更改色相
  * FIXED - 將元素的色相設定為 hue 數值
  * SHIFT - 將元素的色相按此數值偏移，因此不同顏色的元素仍會保持彼此不同，只是沿色相數值作出偏移。
* **saturation mode** -
  * OFF - 不會更改飽和度
  * FIXED - 將飽和度固定為指定數值。
* **brightness mode** -
  * OFF - 不會更改亮度
  * FIXED - 將元素的亮度設定為 brightness 數值
  * MULTIPLY - 將元素的亮度與 brightness 數值結合，因此如果它們正在閃爍，仍會繼續閃爍，但最高只會達到此處指定的亮度。
* **gradient mode** - 由固定 HSB 滑桿切換至漸變編輯器。node 會從漸變中取樣一種顏色，然後使用上方的色相、飽和度及亮度模式套用。
* **gradient position** - 選擇在漸變中的哪一點取樣。配合 Sawtooth Oscillator 將此項由 0% 動畫至 100%，即可隨時間循環掃過整個漸變。
* **blend** - 顏色變更效果的套用強度；0% 表示完全不套用，100% 表示完全套用，50% 則是現有顏色與新數值的混合。

{% hint style="info" %}
Colour Change node 會為整個輸入從漸變中取樣一種顏色。如果你想按位置讓漸變沿形狀分佈，請改用 [以位置為基礎的變換器](position-based-changers.md "mention")。
{% endhint %}

### 漸變編輯器

啟用 **gradient mode** 時，漸變編輯器會顯示在主要控制項下方。

* 按一下漸變列即可新增顏色停止點。
* 左鍵按一下停止點以選取，然後向左右拖曳來移動。
* 將已選取的停止點向下拖離漸變列，或按 Delete/Backspace，即可移除。漸變會始終保留至少兩個停止點。
* 右鍵按一下停止點，即可用顏色選擇器編輯。
* 使用 **Position**、**Hue**、**Saturation** 及 **Brightness**，可精確編輯已選取的停止點。
* **interpolation** 選擇停止點之間的顏色混合方式：
* **HSB** - 混合色相、飽和度及亮度。最適合在色輪上製作平滑的彩虹式移動。
* **RGB** - 直接混合紅、綠、藍數值。效果通常較像螢幕或燈光控制台的顏色淡變。
* **NONE** - 不作混合，直接由一個停止點跳至下一個。
* **hue direction** 可在 HSB interpolation 中使用：
* **AUTO** - 沿色相環採用最短路徑。
* **FORWARDS** - 一律沿色相數值向前移動。
* **BACKWARDS** - 一律沿色相數值向後移動。
