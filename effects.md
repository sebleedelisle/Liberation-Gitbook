# 🟩 Effects

Liberation 的 Effects 系统是一种有趣而灵活的实时方式，用来改变 Clip 输出。Effects 非常自由，可以让一切闪烁、旋转、改变颜色，甚至随机飞舞！&#x20;

你在 Clip Editor 里能做的任何东西都可以作为 effect 使用。实际上，Effects 使用与 Clips 完全相同的节点编辑器来编辑！见 [#editing-effects](effects.md#editing-effects "mention")。创作可能性几乎无限。&#x20;

默认的 effects 按钮 1-8 在 Zone 按钮下方，effects 9-24 是最底部的小按钮。&#x20;

#### 应用一个 effect

按下 effect 按钮可切换该 effect；更好的方式是使用 APC40 的 1-8 号推子来淡入/淡出 effects。没有 APC40 时，可在按钮上点击并上下拖动。或者右键 effect 按钮并调整 level 滑块。&#x20;

{% hint style="warning" %}
按下 effect 按钮会立即激活该 effect。但注意：如果 level 为 0，就不会有任何效果！点击/拖动按钮改变 level，或右键使用 _level_ 滑块，或用 APC40 推子。
{% endhint %}

#### Effects 与 Clip 的 zone delay

Effects 会继承当前运行的每个 Clip 的 zone delay 设置。所以如果你的 Clip 从左到右有延迟，再加上 flash effect，闪烁也会从左到右延迟。&#x20;

{% hint style="info" %}
Effect 如何继承 Clip 的 zone delay 非常难描述，但一试就懂！

我认为这是 Liberation 里最有趣、最有创造力的工具之一。试试就知道了！&#x20;
{% endhint %}

#### Effect 参数

使用 _Parameter node_ 为 effect 添加参数。Parameter 系统允许你从外部调整 effect 内部的多个设置。见 [parameter-control.md](clip-editor/oscillators/parameter-control.md "mention")。&#x20;

使用旋钮 1-8 调整每个 effect 的 _parameter_。或者右键 effect 按钮并调整参数滑块。参数的具体作用取决于 effect 的设置。下方列出了默认 effects 及其参数作用。

{% hint style="info" %}
旋钮 1-8 位于 APC40 Mk2 顶部，Mk1 则在右上方。另见：[apc40-reference.md](reference/apc40-reference.md "mention")。
{% endhint %}

{% hint style="info" %}
Effect 按钮上的小数字表示该 effect 的 _level_ 和 _parameter_。_level_ 由 APC40 推子控制，也可以在按钮上点击拖动；parameter 由 APC40 旋钮控制，也可右键用鼠标调整。&#x20;
{% endhint %}



#### 默认 Effects

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   对 Clip 输出施加混沌运动。参数调节混沌程度/速度。
2. **Sine wave** :\
   将所有内容沿移动的正弦波形扭曲。参数调节波长。
3. **Rotation** :\
   让所有内容旋转。参数调节旋转速度。
4. **Horizontal flip** :\
   水平方向挤压和拉伸所有内容。参数调节速度。
5. **Scale** :\
   将所有内容从满幅到 0 反复缩放。参数调节速度。
6. **Hue** :\
   改变所有内容的色相，但不改变饱和度（即白色仍是白色）。参数调节色相。
7. **Saturation and hue** :\
   改变所有内容的色相，并将颜色完全饱和（即白色也会变为颜色）。参数调节色相。
8. **Flash** :\
   将所有内容的亮度从满到 0 反复闪烁。参数调节闪烁速度。

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

底部一排还有 16 个颜色 effects，用于应用预设的 hue 与 saturation。

注意：以上是默认 effects，但你可以把它们编辑成几乎任何你想要的效果！

### Apply to groups

你可以选择 effect 作用的 group。右键并切换标为 _Apply to groups_ 的 group 复选框。&#x20;

我通常在分别处理 canvas 图形和激光光束时使用该设置。我会把所有 canvas clips 放到 group 5，然后将不希望影响图形 clips 的 effects 排除该 group。&#x20;

你也可以用它在不同激光组上同时应用两种不同的颜色变化。创建两个 colour change effects，并分别选择它们作用的 clip groups。&#x20;

### MX group

_Mutually Exclusive_ 的缩写，用于将 effects 分组，使同组内一次只能激活一个 effect。你会发现默认的颜色变化 effects 只能同时启用一个，因为它们都在 MX Group 1。&#x20;

当 _MX Group_ 设为 0 时，该功能禁用。

### Editing effects

右键任意 effect，点击 _EDIT EFFECT_ 打开 effect editor。这个编辑器与 Clip Editor 完全一致！&#x20;

像编辑 Clip 一样编辑 effect。见 [clip-editor](clip-editor/ "mention")。

你至少需要一个 creator node；可以是任意类型（line、circle、shape、甚至 text！），但最好选择一个在 effect 按钮预览中看起来合理的内容。&#x20;

当 effect 被应用时，effect 中的所有 creator nodes 会被当前运行 Clips 的输出替换。&#x20;

{% hint style="warning" %}
由于一些非常繁琐的技术原因，“trails” nodes 在 effect 中不会启用。pattern nodes 中的 “delay” 设置也是如此（它们使用同一系统）。未来会修复。&#x20;
{% endhint %}

###
