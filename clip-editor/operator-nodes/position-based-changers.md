# 🟩 基于位置的变换

这一类 nodes 会根据位置来修改内容。默认效果沿水平轴（从左到右）应用，但你可以将该轴旋转到任意角度。每个 node 还包含 _radial_ 模式，效果由点相对于中心的角度驱动。

* **Colour Changer by Position** – 沿所选轴或径向角度改变颜色。\
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

**Colour Modes**

这些设置决定颜色调整的哪些部分会作用于内容。另见 [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")。

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

**Start / End Values**

这些滑块定义所选轴（或径向扫过）的颜色范围。

* **start hue** – 渐变起点的 hue。
* **end hue** – 渐变终点的 hue。
* **start saturation** – 起点 saturation。
* **end saturation** – 终点 saturation。
* **start brightness** – 起点 brightness。
* **end brightness** – 终点 brightness。
* **blend** – 将颜色变化与原始颜色混合。100% 时完全替换原色。

**示例 1：滑动彩虹渐变**

从默认设置开始：

1. 保持 **Linear** 模式（0° = 水平）。
2. **wavelength** 设为 100%（覆盖全宽，默认值）。
3. 保持起始/结束值为默认。
4. 启用 **repeat**。
5. 将 **Sawtooth Oscillator** 连接到 **offset**，范围设为 0% 到 100%。

***

**示例 2：黑-白-黑渐变（Pingpong）**

从默认设置开始：

1. 保持 **Linear** 模式（0° = 水平）。
2. **wavelength** 设为 100%（覆盖全宽，默认值）。
3. 关闭 **repeat**。
4. **start brightness** 设为 0（黑）。
5. **end brightness** 设为 100（白）。
6. **start saturation** 与 **end saturation** 设为 0（转为灰度）。
7. **hue mode** 设为 OFF。
8. **saturation mode** 设为 FIXED。
9. **brightness mode** 设为 FIXED。
10. 启用 **pingpong**。

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
* **Radial** – 切换为径向模式，根据角度位移。
* **Radial Smooth Loop** – 调整 wavelength 使其整除圆周的 100%，避免径向模式的可见接缝。
