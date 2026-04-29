# 🟩 Path Modifiers

## &#x20;Dotter

该 node 将线条和形状替换为均匀分布的点（原有点不变）。

* **Colour** – 点的颜色。若启用 _Inherit Colour_ 则忽略此项，见下方。_另见_ [颜色设置与 HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – 点之间的距离（像素）。值越小点越密，值越大点越稀。
* **Offset** – 点序列起始位置的偏移（Spacing 的百分比）。可动画化（例如用 sawtooth Oscillator Node），实现“流动”的点效果。
* **Keep Original** – 开启后保留原有线条/形状，并在其上叠加点。
* **Render Profile** – 选择渲染质量。_见_ [Render profile](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – 自动调整 Spacing，使路径长度可整除。
* **Fade Out Ends** – 让点在路径起点和终点逐渐变暗。适合将 **Offset** 用 sawtooth Oscillator Node 动画化，使点在形状末端平滑淡入淡出。

## &#x20;Trimmer

该 node 会裁剪线条与形状的可见长度，可用于显示/隐藏或随时间动画化。

* **Offset** – 控制可见段的起点。即使 _Trim Size_ 为 0%，把 Offset 从 0% 动画到 100% 也能让形状逐渐显现，在 50% 时完全可见，然后再消失。
* **Trim Size** – 保留的形状长度（占总长度百分比）。
* **Loop** – 将形状视为闭合环路，末端回到起点，而不是消失。
* **All Shapes** – 将所有输入形状合并后当作单一路径裁剪。关闭时每个形状分别裁剪。
* **Add Dot at Start / Add Dot at End** – 在裁剪端点添加指定颜色的点。（若未裁剪则不添加。）
* **Colour** – 裁剪点颜色。_另见_ [颜色设置与 HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – 选择点的 render profile。_见_ [Render profile](../fundamentals/render-profile.md "mention")
