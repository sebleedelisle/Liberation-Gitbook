---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 顏色變更

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> 顏色變更

說明

* **hue, saturation, brightness** - 顏色數值，請參閱[顏色設定及 HSB](../fundamentals/colour-settings-and-hsb.md)
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
* **blend** - 顏色變更效果的套用強度；0% 表示完全不套用，100% 表示完全套用，50% 則是現有顏色與新數值的混合。
