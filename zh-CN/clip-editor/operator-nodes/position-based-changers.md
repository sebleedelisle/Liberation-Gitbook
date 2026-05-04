---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 基于位置的变换

这一类 nodes 会根据位置来修改内容。默认效果沿水平轴（从左到右）应用，但你可以将该轴旋转到任意角度。每个 node 还包含 _radial_ 模式，效果由点相对于中心的角度驱动。

* **Colour Changer by Position** – 沿所选轴或围绕径向角度应用渐变。\
  _示例：让彩虹渐变沿线扫过，或在圆形上使用径向模式形成色环。_
* **Wave Shift by Position** – 应用正弦波形扭曲，使内容在垂直方向（或所选轴的垂直方向）偏移。\
  _示例：让线条像水面一样起伏，或使用径向模式让圆形从中心向外脉动。_
* **Noise Shift by Position** – 应用 simplex 噪声扭曲，使内容在垂直方向（或所选轴的垂直方向）偏移。\
  _示例：类似 Wave Shift，但更自然随机，适合加入有机变化。_

## &#x20;Colour change by position

该 node 会根据位置在内容上应用颜色变化。默认轴为水平（0°），你可以旋转或切换到径向模式。

* **wavelength** – 设置重复颜色周期的长度。
  * _Linear mode:_ 100% 时，一个完整周期覆盖内容的全宽。
  * _Radial mode:_ 100% 时，一个完整周期覆盖整个圆（360°）。数值为圆周百分比，例如 50% = 半圈（180°）。
* **offset** – 按 wavelength 百分比偏移颜色周期起点。可调制该值（例如用 sawtooth oscillator）以平滑循环颜色。
* **repeat** – 开启后在内容上重复周期；关闭则只应用一次渐变：起点之前都是起始色，终点之后都是结束色。
* **pingpong** – 开启后，每次重复都会反向交替，形成镜像效果。若 _Repeat_ 关闭，则渐变仅前后往返一次。_注意：Pingpong 模式下，wavelength 覆盖前进与回程。_
* **linear angle** – 旋转效果轴，0° 为水平。
* **radial** – 切换到径向模式，根据角度应用颜色。
* **radial smooth loop** – 自动调整 wavelength 以整除圆周的 100%，避免循环处出现明显接缝。
* **legacy mode** – 切换回较旧的起始/结束 HSB 滑块。保持关闭即可使用较新的渐变编辑器。

**Colour Modes**

这些设置决定颜色调整的哪些部分会作用于内容。另见 [颜色设置与 HSB](../fundamentals/colour-settings-and-hsb.md "mention")。

* **hue mode**
  * _OFF_ – 不改变 hue。
  * _FIXED_ – hue 固定为指定值。
  * _SHIFTED_ – hue 按指定量偏移（不同颜色仍保持差异，但会一起绕色环移动）。
* **saturation mode**
  * _OFF_ – saturation 不变。
  * _FIXED_ – saturation 固定为指定值。
* **brightness mode**
  * _OFF_ – brightness 不变。
  * _FIXED_ – brightness 固定为指定值。
  * _MULTIPLY_ – brightness 与指定值相乘，保留动态（例如闪烁仍闪烁，但亮度受限制）。

**Gradient editor**

使用与 [Colour Changer](colour-changer.md "mention") 相同的渐变编辑器，但会按位置将渐变映射到内容上。

* 点击渐变条可添加一个颜色停止点。
* 左键点击停止点将其选中，然后横向拖动即可移动。
* 将选中的停止点向下拖离渐变条，或按 Delete/Backspace，即可删除。渐变始终至少保留两个停止点。
* 右键点击停止点，可使用颜色选择器编辑。
* 使用 **Position**、**Hue**、**Saturation** 和 **Brightness** 精确编辑所选停止点。
* **interpolation** 用于选择停止点之间的颜色混合方式：
* **HSB** – 混合 hue、saturation 和 brightness。最适合在色相环上实现平滑的彩虹式变化。
* **RGB** – 直接混合红、绿、蓝数值。通常更像屏幕或灯光控制台中的颜色淡变。
* **NONE** – 从一个停止点直接跳到下一个停止点，不进行混合。
* **hue direction** 在 HSB 插值模式下可用：
* **AUTO** – 沿色相环选择最短路径。
* **FORWARDS** – 始终按 hue 数值的正向前进。
* **BACKWARDS** – 始终按 hue 数值的反向前进。
* **blend** – 将颜色变化与原始颜色混合。100% 时完全替换原色。

**旧版起始/结束值**

如果开启 **legacy mode**，渐变编辑器会替换为较旧的控件：

* **start hue / end hue** – 范围起点和终点的 hue。
* **start saturation / end saturation** – 范围起点和终点的 saturation。
* **start brightness / end brightness** – 范围起点和终点的 brightness。

**示例 1：滑动彩虹渐变**

从默认设置开始：

1. 保持 **Linear** 模式（0° = 水平）。
2. **wavelength** 设为 100%（覆盖全宽，默认值）。
3. 保持默认渐变不变。
4. 启用 **repeat**。
5. 将 **Sawtooth Oscillator** 连接到 **offset**，范围设为 0% 到 100%。

***

**示例 2：黑-白-黑渐变（Pingpong）**

从默认设置开始：

1. 保持 **Linear** 模式（0° = 水平）。
2. **wavelength** 设为 100%（覆盖全宽，默认值）。
3. 关闭 **repeat**。
4. 将第一个渐变停止点设为黑色。
5. 将最后一个渐变停止点设为白色。
6. 将 **hue mode** 设为 OFF。
7. 如果要强制结果为灰度，请将 **saturation mode** 设为 FIXED。
8. 将 **brightness mode** 设为 FIXED。
9. 启用 **pingpong**。

_结果：渐变从黑到白，再从白回黑。_\
注意：如果想保留原有 hue 与 saturation，请关闭 Saturation mode。

***

**示例 3：旋转彩虹轮（Radial）**

1. 启用 **radial** 模式。
2. **wavelength** 设为 100%（完整 360°）。
3. 打开 **repeat**。
4. 将 **Sawtooth Oscillator** 连接到 **offset**，范围设为 0% 到 100%。

_结果：无缝旋转的色轮。_

## &#x20;Wave shift by position

该 node 在内容上应用波形扭曲，使点沿所选轴的垂直方向（或径向）偏移。

* **Wavelength** – 设置波形周期长度。
  * _Linear mode:_ 100% 时一个完整周期覆盖内容全宽。
  * _Radial mode:_ 100% 时一个完整周期覆盖 360°（数值为圆周百分比：50% 半圈、25% 四分之一圈等）。
* **Size** – 控制波形振幅（位移大小）。
* **Offset** – 沿轴（或径向）偏移波形，为 wavelength 的百分比。可用 **Oscillator Node** 动画化，使波形“流动”。
* **Radial** – 切换为径向模式，根据角度位移。
* **Radial Smooth Loop** – 调整 wavelength 使其整除圆周的 100%，避免循环接缝。
* **Triangle** – 将波形从正弦变为三角。
* **Absolute** – 取波形绝对值，仅产生单向位移（将负半周期折叠到正向）。
* **Angle** – 旋转波形轴，0° 为水平。

## &#x20;Noise shift by position

该 node 使用噪声场（类似湍流）扭曲内容，使点沿所选轴的垂直方向（或径向）偏移。与 _Wave Shift_ 相比，效果更有机、更随机。

* **Detail** – 控制噪声细节程度。值越高越细碎，越低越平滑。
* **Wavelength** – 设置噪声图案尺度。
  * _Linear mode:_ 100% 时一个完整噪声周期覆盖内容全宽。
  * _Radial mode:_ 100% 时一个完整周期覆盖 360°。
* **Size** – 位移幅度（噪声扭曲强度）。
* **Offset** – 沿轴（或径向）偏移噪声图案，为 wavelength 的百分比。可用 **Oscillator Node** 动画化，使噪声“流动”。
* **Depth Offset** – 在 3D 噪声场中移动，产生时间变化。用 Oscillator Node 动画化时效果尤佳。
* **Depth Detail** – 控制深度维度上的变化细节。
* **Absolute** – 取噪声绝对值，将负值折叠为正值（产生单向位移）。
* **Angle** – 在线性模式下旋转噪声的轴向。0° = 水平。
* **Radial** – 切换为径向模式，根据角度位移。
* **Radial Smooth Loop** – 调整 wavelength 使其整除圆周的 100%，避免径向模式的可见接缝。
