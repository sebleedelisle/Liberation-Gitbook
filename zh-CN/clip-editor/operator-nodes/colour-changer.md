# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line">  Colour change

说明

* **hue, saturation, brightness** - 颜色数值，见 [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - 不改变 hue
  * FIXED - 将 hue 固定为指定值
  * SHIFT - 在指定值基础上偏移 hue，不同颜色仍保持差异，只是整体偏移
* **saturation mode** -
  * OFF - 不改变 saturation
  * FIXED - saturation 固定为指定值
* **brightness mode** -
  * OFF - 不改变 brightness
  * FIXED - brightness 固定为指定值
  * MULTIPLY - brightness 与指定值相乘，因此元素仍会闪烁，但最高亮度受该值限制
* **blend** - 颜色变换的强度，0% 不生效，100% 完全替换，50% 为原色与新色混合。
