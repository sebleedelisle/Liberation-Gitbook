---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Clip Editor 简介

Clip Editor 是创建激光内容的多功能工具，也是 Liberation 的核心部分。用它制作简单内容很容易，同时它也足够灵活，可以做出非常精细、复杂的效果。

{% hint style="info" %}
基于 node 的编辑器是 Liberation 最早开发的部分！它源于 2018 年在英国一次激光聚会上与 Rob Stanley 的一次讨论：一个“面向对象”的激光内容设计器会是什么样子？

虽然它看起来很简单，但实际构建起来是一个相当复杂的系统。不过到 2019 年初，我已经做出了一个可运行的演示，验证了这个概念——也正是它开启了后来的整个旅程！
{% endhint %}

它是一个基于 node 的可视化编辑器（或称 [node 图架构](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)）。如果你用过 TouchDesigner、MaxMSP 或 VVVV，这种方式会很熟悉。不过 Clip Editor 略有不同，也更简单一些，因为它是专门为矢量图形设计的。

你可以右键点击 Clip 按钮并选择 _EDIT CLIP_ 来打开 Clip Editor。也可以右键点击一个空的 Clip 按钮，然后选择 _CREATE AND EDIT CLIP_。

### 概览

在 Clip Editor 中你会看到：

* 顶部的 **Creator** 和 **Operator node 按钮**
* 左侧的 **Oscillator node 按钮**
* 右侧面板中的内容预览；如果点击某个 node，还会看到第二个预览，用来显示该 node 本身的内容。
* 当前正在编辑的 Clip 的所有 node 和连接（如果是新 Clip，这里会是空的）
* 带有各种选项的 Clip Editor 面板

编辑时，你还会在背景中的 3D 可视化器里看到这个 Clip 的效果。

{% hint style="info" %}
如果在 3D 可视化器中看不到任何输出，可能需要使用 zone 按钮打开你想要的 zone。你还需要确保 _Preview to lasers_ 已启用，参见下方的 [Clip Editor 面板](clip-editor-intro.md#clip-editor-panel "mention")。
{% endhint %}

### 构建 Clip

通常你会从一个或多个 [Creator node](creator-nodes.md) 开始，然后从左到右连接用于处理内容的 [Operator nodes](operator-nodes/)。当你把 Creator 和/或 Operator 移动到一起时，会看到它们自动互相连接。你也可以把它们拖开，再次断开连接。

### 向 Clip 添加 node

从顶部或左侧的某个 node 按钮点击并拖拽到 Clip Editor 中的空白区域。

### 调整 node 的设置

点击齿轮图标按钮（node 右上角）打开该 node 的属性面板。

### 启用和禁用 node

点击电源图标按钮（node 左上角）来启用或禁用该 node。node 会变暗，表示它当前未处于活动状态。请注意，即使某个 Operator 被禁用，内容仍会从中通过，只是该 node 不会影响内容。

### 连接 node

内容由 Creator node 生成，并沿着 node 从左向右传递；每个 Operator 都会以某种方式影响内容，然后将其传递给下一个 Operator。路径末端剩下的内容就是这个 Clip 的内容。当你把 Creator 和 Operator 移近时，它们会自动相互连接。要分开它们，只需再次把它们拖开。

{% hint style="info" %}
你可以将多个 node 连接到下一个 node 的输入端。这对于组合多段内容很有帮助。
{% endhint %}

### Node 属性和插口

每个 node 底部都有一组插口，每个插口代表该 node 内的一个属性，例如亮度、位置、缩放、旋转等。

[Oscillator node](oscillators/) 可以从下方连接到这些插口，用来为这些设置添加动画。Oscillator node 顶部有一个输出端，点击并拖拽即可拉出连接，然后放到其他 node 的某个属性插口上。

### Oscillator node

Oscillator node 用于随时间改变属性。它们通常表示锯齿波或正弦波等波形，但有些 Oscillator node 会使用外部输入（例如麦克风输入电平）作为来源。

{% hint style="info" %}
如果你用过模拟合成器，就会熟悉振荡器的概念：它们通常用于生成波形，或随时间调整声音。Liberation 中的 Oscillator 作用类似。

**趣味知识：** _Liberation_ 这个名字的灵感来自 Moog Liberation，这是一款 1980 年发布的“键盘吉他”式合成器，并因 Herbie Hancock、Jean-Michel Jarre 甚至 James Brown 的使用而闻名！
{% endhint %}

Oscillator 始终具有 _range_ 设置，用来控制要调整属性的最小值和最大值。_Wave Oscillators_ 始终具有 _duration_ 设置，用来决定 Oscillator 改变数值的速度。更多信息请参见 [波形 Oscillator](oscillators/wave-oscillators.md "mention")。

### Clip Editor 面板

* Timer - 面板顶部会显示 Clip 播放过程中的当前时间
* _RETRIGGER_ - 从开头重新启动 Clip；如果你的 Clip 不循环，这会特别有用
* _Preview to lasers_ - 勾选后，编辑此 Clip 时你会看到 3D 可视化器同步更新。如果关闭它，你会看到编辑器之外正在运行的 Clip。这是全局设置，不是按 Clip 单独设置。
* _UNDO/REDO_ - 用于 Clip Editor 本身。也映射到 `Cmd / Ctrl + Z` 和 `Cmd / Ctrl + Shift + Z`。
* _SAVE CLIP_ - 保存你的编辑，但会提示你正在覆盖原内容
* _SAVE AS A COPY_ - 将你的 Clip 保存到 Clip Deck 中下一个可用槽位。这会成为该 Clip 的新位置，之后的所有保存都会保存到这个新位置。
* _EXIT EDITOR_ - 关闭 Clip Editor。如果有未保存的更改，会显示确认面板。
