---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

說明

* **hue, saturation, brightness** - 色彩值，請參閱[色彩設定與 HSB](../fundamentals/colour-settings-and-hsb.md)
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
* **blend** - Colour change 套用的強度；0% 表示完全不套用，100% 表示完全套用，50% 則是現有顏色與新數值的混合。
