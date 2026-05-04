---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line">  Colour change

更改所有传入内容的颜色。你可以设置固定的 HSB 值，也可以切换到渐变系统，并从自定义渐变中采样颜色。

* **hue, saturation, brightness** - 颜色数值，见 [颜色设置与 HSB](../fundamentals/colour-settings-and-hsb.md "mention")
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
* **gradient mode** - 从固定的 HSB 滑块切换到渐变编辑器。该 node 会从渐变中采样一种颜色，然后使用上方的色相、饱和度和亮度模式来应用它。
* **gradient position** - 选择在渐变中的哪个位置进行采样。使用 Sawtooth Oscillator 将它从 0% 动画到 100%，即可随时间循环遍历渐变。
* **blend** - 颜色变换的强度，0% 不生效，100% 完全替换，50% 为原色与新色混合。

{% hint style="info" %}
Colour Change node 会从渐变中采样一种颜色，并应用到整个输入。如果你希望渐变按位置分布在形状上，请改用 [基于位置的变换器](position-based-changers.md "mention")。
{% endhint %}

### 渐变编辑器

启用 **gradient mode** 后，渐变编辑器会显示在主要控制项下方。

* 单击渐变条可添加一个颜色停靠点。
* 左键单击停靠点将其选中，然后横向拖动即可移动。
* 将选中的停靠点向下拖离渐变条，或按 Delete/Backspace，即可将其移除。渐变始终会保留至少两个停靠点。
* 右键单击停靠点，可使用颜色选择器编辑它。
* 使用 **Position**、**Hue**、**Saturation** 和 **Brightness** 精确编辑选中的停靠点。
* **interpolation** 选择停靠点之间的颜色混合方式：
* **HSB** - 混合色相、饱和度和亮度。最适合在色轮上实现平滑的彩虹式运动。
* **RGB** - 直接混合红、绿、蓝数值。通常更像屏幕或灯光控台上的颜色淡变。
* **NONE** - 从一个停靠点直接跳到下一个停靠点，不进行混合。
* **hue direction** 可用于 HSB 插值：
* **AUTO** - 沿色相环采用最短路径。
* **FORWARDS** - 始终按色相值的正向移动。
* **BACKWARDS** - 始终按色相值的反向移动。
