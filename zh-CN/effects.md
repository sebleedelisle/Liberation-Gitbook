---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 效果

Liberation 中的效果系统是一种有趣而灵活的方式，可以实时改变 Clip 输出。效果非常灵活，可以让所有内容闪烁开关、旋转、改变颜色，甚至随机飞动！

你在 Clip Editor 中能做的任何事情，都可以用作效果。事实上，效果使用的正是与 Clips 完全相同的 node 编辑器！请参阅 [编辑效果](effects.md#editing-effects "mention")。创作可能性几乎是无限的。

默认效果按钮 1-8 位于 zone 按钮下方，效果 9-24 是底部的小按钮。

#### 应用效果

按下效果按钮即可切换该效果；更好的方式是使用 APC40 的滑块 1-8 来淡入和淡出效果。如果没有 APC40，也可以在按钮上单击并上下拖动来淡入效果。或者右键单击效果按钮，并调整 level 滑块。

{% hint style="warning" %}
按下效果按钮会立即激活该效果。不过请注意，如果 level 设置为零，就不会发生任何变化！单击并拖动按钮可更改 level，或右键单击并使用 _level_ 滑块，或使用 APC40 的推子。
{% endhint %}

#### 效果与 Clip 的 zone delay

效果会继承每个当前正在运行的 Clip 的 zone delay 设置。因此，如果你的 Clip 有一个从左到右移动的延迟，而你添加了闪烁效果，那么闪烁也会从左到右延迟。

{% hint style="info" %}
Clip 的 zone delay 如何被效果继承，这件事描述起来非常困难，但一试就很明显！

我认为这是 Liberation 内置的最有趣、最有创意的工具之一。试试看，你就会明白我的意思！
{% endhint %}

#### 效果参数

使用 _Parameter node_ 为效果添加参数。Parameter 系统可以让你从外部调整效果内部的多个设置。更多信息请参阅 [参数控制](clip-editor/oscillators/parameter-control.md "mention")。

使用旋钮控制器 1-8 来调整每个效果的 _parameter_。或者右键单击效果按钮，并调整参数滑块。参数变化会执行什么操作，取决于该效果的设置方式。下面列出了默认效果以及它们的参数作用。

{% hint style="info" %}
旋钮控制器 1-8 位于 APC40 Mk2 顶部一排，在 Mk1 上则位于右上方。另请参阅：[APC40 参考](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
你在效果按钮上看到的小数字表示该效果的 _level_ 和 _parameter_。_level_ 由 APC40 上的推子控制，也可以在按钮上单击并拖动来调整。parameter 由 APC40 上的旋钮调整，也可以右键单击后用鼠标调整。
{% endhint %}

#### 默认效果

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**：\
   对 Clip 输出施加混乱运动。参数用于调整混乱程度/速度。
2. **Sine wave**：\
   让所有内容沿移动的正弦波发生扭曲。参数用于调整波长。
3. **Rotation**：\
   让所有内容旋转。参数用于调整旋转速度。
4. **Horizontal flip**：\
   在水平方向压缩和拉伸所有内容。参数用于调整速度。
5. **Scale**：\
   反复将所有内容从完整大小缩放到零。参数用于调整速度。
6. **Hue**：\
   改变所有内容的色相，但不改变饱和度（也就是说，白色内容仍保持白色）。参数用于调整色相。
7. **Saturation and hue**：\
   改变所有内容的色相，并将颜色完全饱和（也就是说，白色内容会变成该颜色）。参数用于调整色相。
8. **Flash**：\
   反复让所有内容的亮度从全亮闪到零。参数用于调整闪烁速度。

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

底部一排还有另外 16 个颜色效果，用于应用预设的色相和饱和度值。

请注意，这些只是默认效果，你可以编辑它们，让它们几乎实现任何你想要的功能！

### 应用于分组

你可以选择哪些分组会受到效果影响。右键单击并切换标记为 _Apply to groups_ 的分组复选框。

我主要在分别处理 canvas 图形和激光 beam 时使用这种设置。我会将所有 canvas Clips 分配到分组 5，然后在不希望影响这些图形 Clip 的效果中排除该分组。

你也可以用它来现场同时对两组激光应用 2 种不同的颜色变化。创建两个颜色变化效果，并选择每个效果要应用到哪些 Clip 分组。

### MX 分组

_Mutually Exclusive_ 的缩写。这是一种将效果组合在一起的方式，使同一分组中同时只能有一个效果处于激活状态。注意，默认的颜色变化效果一次只能激活其中一个。这是因为它们都在 MX Group 1 中。

如果 _MX Group_ 设置为 0，则此功能会被禁用。

### 编辑效果

右键单击任意效果，然后单击 _EDIT EFFECT_ 按钮打开效果编辑器。注意，这个编辑器与 Clip Editor 完全相同！

你可以像编辑任何 Clip 一样编辑效果。请参阅 [Clip Editor](clip-editor/ "mention")。

你至少需要有一个 Creator node；它可以是任何内容（线条、圆形、形状，甚至文本！），但你最好选择一种在效果按钮预览中最合理的内容。

应用效果时，效果中的所有 Creator node 都会被当前正在运行的 Clips 的输出替换。

{% hint style="warning" %}
由于非常繁琐的技术原因，在效果内部时，“trails” node 不会启用。pattern node 内部的 “delay” 设置也是如此（它们使用同一个系统）。这将在未来版本中修复。
{% endhint %}
