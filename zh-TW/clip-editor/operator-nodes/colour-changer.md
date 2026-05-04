---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

變更所有輸入內容的色彩。你可以設定固定的 HSB 數值，或切換到漸層系統，從自訂漸層取樣色彩。

* **hue, saturation, brightness** - 色彩值，請參閱[色彩設定與 HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - 不變更色相
  * FIXED - 將元素的色相設定為 hue 值
  * SHIFT - 依指定值偏移元素的色相，因此不同顏色的元素仍會保持差異，只是沿著色相值偏移。
* **saturation mode** -
  * OFF - 不變更飽和度
  * FIXED - 將飽和度固定為指定值。
* **brightness mode** -
  * OFF - 不變更亮度
  * FIXED - 將元素的亮度設定為 brightness 值
  * MULTIPLY - 將元素的亮度與 brightness 值相乘，因此如果它們正在閃爍，仍會繼續閃爍，但最高只會到這裡指定的亮度。
* **gradient mode** - 從固定 HSB 滑桿切換到漸層編輯器。此 node 會從漸層取樣一個色彩，然後使用上方的色相、飽和度與亮度模式套用。
* **gradient position** - 選擇要取樣漸層中的哪一個位置。可用 Sawtooth Oscillator 將它從 0% 動畫到 100%，讓色彩隨時間在漸層中循環。
* **blend** - Colour change 套用的強度；0% 表示完全不套用，100% 表示完全套用，50% 則是現有顏色與新數值的混合。

{% hint style="info" %}
Colour Change node 會從漸層取樣一個色彩，並套用到整個輸入。如果你想讓漸層依位置沿著形狀分布，請改用 [依位置變更](position-based-changers.md "mention")。
{% endhint %}

### 漸層編輯器

開啟 **gradient mode** 時，漸層編輯器會出現在主要控制項下方。

* 按一下漸層列即可新增色標。
* 左鍵按一下色標即可選取，然後左右拖曳即可移動。
* 將選取的色標向下拖離漸層列，或按 Delete/Backspace，即可移除。漸層一定會保留至少兩個色標。
* 右鍵按一下色標，即可用色彩選擇器編輯。
* 使用 **Position**、**Hue**、**Saturation** 和 **Brightness** 精確編輯選取的色標。
* **interpolation** 選擇色標之間的色彩混合方式：
* **HSB** - 混合色相、飽和度與亮度。最適合在色輪上產生平滑的彩虹式移動。
* **RGB** - 直接混合紅、綠、藍數值。通常會比較像螢幕或燈光控制台的色彩淡變。
* **NONE** - 不混合，直接從一個色標跳到下一個色標。
* **hue direction** 可在 HSB 插值中使用：
* **AUTO** - 沿著色相環採用最短路徑。
* **FORWARDS** - 一律沿著色相值的正向前進。
* **BACKWARDS** - 一律沿著色相值的反向前進。
