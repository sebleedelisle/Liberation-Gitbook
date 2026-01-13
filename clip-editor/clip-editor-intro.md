# 🟩 Clip Editor 介绍

Clip Editor 是创建激光内容的核心工具，功能灵活：简单内容易做，同时也足够强大，可制作非常复杂的效果。&#x20;

{% hint style="info" %}
节点式编辑器是 Liberation 的第一个模块！它源于我在 2018 年英国激光聚会时与 Rob Stanley 的一次讨论：什么样的“面向对象”激光内容设计器才是理想的？

看起来简单，但实现起来非常复杂。到了 2019 年初我做出了可运行的原型，证明了概念可行，也因此开启了整个旅程！
{% endhint %}

它是一个基于节点的可视化编辑器（或称 [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)），如果你用过 TouchDesigner、MaxMSP 或 VVVV 会很熟悉。Clip Editor 与它们略有不同，且更简单，因为它是专为矢量图形设计的。&#x20;

你可以右键点击 Clip 按钮并选择 _EDIT CLIP_ 来打开 Clip Editor；或者右键点击空的 Clip 按钮，选择 _CREATE AND EDIT CLIP_。&#x20;

### 概览

你会在 Clip Editor 中看到：&#x20;

* 顶部的 **Creator** 与 **Operator node buttons**&#x20;
* 左侧的 **Oscillator node buttons**
* 右侧的内容预览面板；点击某个 node 后会出现第二个预览，显示该 node 的输出
* 当前 Clip 的所有 nodes 与连接（若是新 Clip 则为空）
* Clip Editor 面板及其各种选项

编辑时，你还会在后台的 3D visualiser 中看到 Clip 的样子。&#x20;

{% hint style="info" %}
如果 3D visualiser 中没有输出，可能需要用 Zone 按钮开启所需 Zones。同时确保 _Preview to lasers_ 已启用，详见下方 [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel "mention")。
{% endhint %}

### 构建 Clip

通常从一个或多个 [creator nodes](creator-nodes.md) 开始，然后从左到右连接 [operators](operator-nodes/) 对内容进行处理。你会发现当 Creator 和 Operator 靠近时会自动连接，也可以拖开以断开。&#x20;

### 向 Clip 添加 nodes

从顶部或左侧的 node 按钮点击并拖入 Clip Editor 空白区域。&#x20;

### 调整 node 设置

点击 node 右上角的齿轮按钮打开该 node 的属性面板。&#x20;

### 启用/禁用 node

点击 node 左上角的电源按钮可启用或禁用 node。禁用时 node 变暗。注意：即使禁用，内容仍会通过该 operator，只是不会被该 node 影响。&#x20;

### 连接 nodes

内容由 creator node 生成，并从左到右经过各个 nodes；每个 operator 会处理内容并传递给下一个。路径末端剩下的就是 Clip 内容。Creators 与 Operators 靠近会自动连接，拖开即可断开。&#x20;

{% hint style="info" %}
你可以将多个 nodes 连接到同一个输入，以合并多份内容。
{% endhint %}

### Node 属性与 sockets

每个 node 底部都有一排 sockets，每个 socket 对应 node 的一个属性，如亮度、位置、缩放、旋转等。&#x20;

[Oscillator nodes](oscillators/) 可从下方连接到这些 sockets，用于随时间改变这些属性。Oscillator nodes 顶部有输出口，点击拖出连接线并放到其他 nodes 的属性 socket 上即可。&#x20;

### Oscillator nodes

Oscillator nodes 用于随时间变化属性。它们通常代表锯齿波或正弦波等波形，但有些 oscillator nodes 使用外部输入（如麦克风输入电平）作为源。&#x20;

{% hint style="info" %}
如果你用过模拟合成器，你会熟悉 oscillators，它们常用于生成波形或随时间调整声音。Liberation 中的 oscillators 也是类似作用。&#x20;

**Fun fact:** _Liberation_ 这个名字灵感来自 Moog Liberation——1980 年发布的“键tar”合成器，由 Herbie Hancock、Jean-Michel Jarre 甚至 James Brown 使用而闻名！&#x20;
{% endhint %}

Oscillators 总有 _range_ 设置，用于控制属性的最小/最大值。_Wave Oscillators_ 还带 _duration_ 设置，用于决定变化速度。更多信息见 [wave-oscillators.md](oscillators/wave-oscillators.md "mention")。&#x20;





&#x20;

### Clip editor panel

* Timer - 面板顶部显示 Clip 当前运行时间
* _RETRIGGER_ - 从开头重新开始播放；当 Clip 不是循环时特别有用
* _Preview to lasers_ - 勾选后，编辑 Clip 时 3D visualiser 会实时更新；关闭后则显示编辑器之外正在运行的 Clips。这是全局设置，不是单个 Clip 设置。&#x20;
* _UNDO/REDO_ - Clip Editor 的撤销/重做，同时映射到 CTL/CMD Z 与 CTL/CMD SHIFT Z
* _SAVE CLIP_ - 保存编辑，会提示你覆盖
* _SAVE AS A COPY_ - 将 Clip 保存到 Clip Deck 中下一个可用位置，保存位置会变为新位置，后续保存都写入这个位置&#x20;
* _EXIT EDITOR_ - 关闭 Clip Editor。若有未保存更改，会弹出确认面板。&#x20;
