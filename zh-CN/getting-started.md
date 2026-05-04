---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ 快速入门指南

## 简介

欢迎使用 **Liberation** —— 新一代激光秀软件。

Liberation 是一款功能强大、结构复杂的现代软件；它以易用性和可靠性为基础，让你可以自由表达创意。它快速、高效且流程顺畅；按照这份_快速入门指南_操作，你很快就能开始使用！

### 管理激光器

Liberation 非常灵活，即使没有连接任何实际激光器，你也可以设置激光器并进行可视化。等你准备好实际输出时，再把每个输出无缝分配给激光控制器即可。

{% hint style="info" %}
你可以在 Liberation 中设置并可视化任意数量的激光器，许可证等级（Hobbyist、Pro 等）只会限制你可以_启用输出_的激光器数量。这意味着即使使用免费许可证，你也可以设计包含 100 台激光器的激光秀。只有在需要真正用实际激光器运行时，才需要升级许可证。
{% endhint %}

默认设置中有 8 台激光器水平排列，但你可以按需自定义。刚开始熟悉软件时，建议先保留这个默认设置；之后再根据你的硬件配置进行调整。（见[设置项目](setting-up/setting-up-your-project.md "mention")）

{% hint style="warning" %}
重要：在启用任何激光器输出之前，请务必了解相关风险，并仔细阅读[设置激光器](setting-up/setting-up-lasers.md "mention")章节。
{% endhint %}

## 软件概览

### 安全关闭

只要在运行激光器，你就必须随时备有**硬件急停按钮**（见[急停与联锁](hardware/emergency-stop-interlocks.md "mention")）。如果只是想在不那么紧急的情况下关闭所有输出，可以使用 _**DISARM ALL**_ 按钮，或按 `Escape` 键（也可以按 APC40 上的 _**SESSION**_ 键）。你也可以使用屏幕上的滑块或 APC40 上的主推子来降低 Global Brightness。

### 滑块控件

Liberation 中有多种滑块和控制项。

{% hint style="info" %}
如果需要比滑块更精确的控制，可以按住 `Cmd / Ctrl` 并点击滑块，直接输入新的数值。
{% endhint %}

### 键盘快捷键

完整的键盘快捷键列表见这里：[键盘快捷键](reference/keyboard-shortcuts.md "mention")

### 屏幕布局

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
不确定某个按钮的作用？把鼠标悬停在按钮上即可查看说明！
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menu 中可以找到所有文件导入/导出选项，也可以打开各个面板。你还可以在这里使用订阅授权或取消授权当前电脑（位于 _Liberation -> Authorise/Deauthorise this computer_）。

#### Icon bar

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

这里包含常用操作，例如启用/关闭所有激光器输出、Global Brightness、Test Pattern，以及在 3D、Canvas 和 Output view 之间切换。

### Views

屏幕左上方的大区域可以显示 3 个主要 view 之一：**3D**、**CANVAS** 和 **OUTPUT**。使用 Icon bar 上的按钮进行切换（也可以按 `Tab` 键在 3D view 和 Output view 之间切换，然后继续按 Tab 依次切换每一路激光输出）。

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view 会显示你的激光器效果，并且可以配置成与你自己的激光器设置相匹配。点击并拖动可旋转摄像机视角，使用鼠标滚轮可前后移动。更多选项可在 _3D Visualiser settings_ 面板中找到（_View -> 3D Visualiser Settings_）。见 [3D Visualiser](setting-up/3d-visualiser.md "mention")。

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view 用于为每台激光器配置 zone 和 mask。（注意左上角的超大数字，方便你清楚知道当前正在编辑哪台激光器！）

这个 view 表示该激光器的完整输出范围，以及每个 zone 在其中的位置。默认情况下，每台激光器只有一个 zone，但你可以根据实际需要添加任意合理数量的 zone，并且它们都会显示在这个 view 中。

{% hint style="info" %}
**什么是 zone？**

zone 是激光器输出中的一个空间区域，你可以把激光内容发送到其中。每台激光器可以有多个 zone。最简单的 zone 类型是 _beam_ zone，此外还有 _canvas_ zone 和 _DMX_ zone。本指南主要关注 beam zone，它通常用于在空气中创建氛围光束效果。
{% endhint %}

你可以通过以下方式选择要编辑的激光器：

* 顶部栏中的编号按钮
* 按下对应激光器的数字键（_1-9 keys_）
* 使用 `Tab` 键依次循环切换

按 _+_ 按钮可向设置中添加新的激光器。（_Laser Overview_ 面板中也有一个 _ADD LASER_ 按钮）

在 _Laser Overview_ 面板中点击红色 ⊖ 按钮，可从设置中删除一台激光器。

你可以使用鼠标滚轮放大和缩小；在没有 zone 的任意位置点击并拖动可移动视图。

点击某个 zone 可选中它，然后用鼠标调整其角点。拖动角点时按住 `Alt / Option` 键，可进行非等比例调整。右键点击 zone 可查看更多选项，包括更改 zone 类型。

左侧有一列图标按钮，将鼠标悬停在任意按钮上即可查看其功能说明。这里的按钮可用于添加 beam zone、canvas zone 和 mask。还有一些选项可只为当前激光器设置 Test Pattern，以及配置网格和吸附设置。

更多详情见 [Output 视图](output-view/ "mention")。

#### Canvas

Canvas 系统主要用于图形和建筑投影映射。你可以把复杂图像分配到多台激光器上，并对每个部分进行透视校正。见[图形与 Canvas 系统](graphics-and-the-canvas-system/ "mention")。

### APC40 MIDI 控制器

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

虽然可以用鼠标和键盘控制 Liberation，但使用 APC40 MIDI 控制界面会好得多（Mark 2 最合适，Mark 1 也可以使用）。

另见：[APC40 参考](reference/apc40-reference.md "mention")

Liberation 也支持 APC Mini 和 MIDI Fighter Twister。对于大多数场景，APC40 Mark 2 仍然是最佳选择。

### Clip 和效果

{% hint style="info" %}
**什么是 Clip？**

Clip 是 Liberation 中用于容纳任何激光内容的容器。Clip 可以包含光束或图形动画，通常会循环播放。它们可以被发送到任意 zone（或 _Canvas target area_），并通过 Clip Deck 中的 Clip 按钮触发。
{% endhint %}

#### Clip Deck 概览

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

这个网格称为 _Clip Deck_，所有激光 Clip 都存放在这里。它的设计与 APC40 上 8 x 5 的按钮网格直接对应。

**浏览 Clip Deck。**

你可以通过以下方式左右滚动 Clip Deck：

* 左右方向键。加按 `Cmd / Ctrl` 可一次滚动整页。
* 触控板：滑动
* 鼠标：如果鼠标支持横向滚动，将鼠标悬停在 Clip Deck 上即可使用
* APC40 滚动旋钮
* APC40 _<- DEVICE ->_ 按钮

为了帮助你定位，顶部有一个 Clip Deck 的迷你可视化视图。另见 [Clips 与 Clip Deck](clips/ "mention")

#### 启动和停止 Clip

按下 Clip 按钮（用鼠标或 APC40 都可以）即可启动 Clip。再次按下可停止。当你启动一个 Clip 时，除非按住 _shift_，否则所有同色的其他 Clip 都会自动停止。

有些 Clip 会处于 _Flash mode_（默认情况下为红色 Clip），这类 Clip 会在你松开 Clip 按钮后立即停止。

_STOP_ 按钮会停止当前正在运行的所有 Clip。

#### 为 Clip 设置输出 zone

在 Clip 按钮下方，你会看到 zone 按钮，默认是 beam zone 1 到 8（_BEAM 1_、_BEAM 2_ 等）。zone 按钮会亮起，表示哪些 zone 已分配给当前选中的 Clip。

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

在 zone 按钮下方再往下两行，你会看到 X/Y 翻转按钮，可用它们将 Clip 水平或垂直翻转。

{% hint style="info" %}
请注意，这些 zone 分配和 X/Y 翻转设置是绑定到 Clip 本身的；下次运行该 Clip 时会保留。它们不是全局设置。
{% endhint %}

右键点击某个 Clip 可编辑更多 Clip 设置。另见 [Clip 设置](clips/clip-settings.md "mention")

### Groups

你会注意到每个 Clip 都有彩色轮廓，这个颜色表示它所在的 _group_。APC40 的 Clip 按钮也会以这个颜色亮起。

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>青色</td></tr><tr><td>Group 2</td><td>橙色</td></tr><tr><td>Group 3</td><td>红色</td></tr><tr><td>Group 4</td><td>靛蓝色</td></tr><tr><td>Group 5</td><td>绿色</td></tr></tbody></table>

group 系统非常灵活，可以让你：

* 保持一个 group 中的 Clip 继续运行，同时切换另一个 group 中的 Clip
* 快速为同一 group 中的所有 Clip 分配 zone 和 X/Y 翻转
* 为 Clip 设置 _Flash mode_（Group 3 默认设置为 _Flash mode_）

group 还包含淡入/淡出过渡设置，这些设置可以被其中的 Clip 继承，也可以被覆盖。

你可以使用右键菜单中的按钮为 Clip 分配 group；如果使用 APC40，可以按住 group 按钮，_在它仍被按住时_再按 Clip 按钮。

更改同一 group 中所有 Clip 的 zone 设置

使用 APC40 时，先按下 group 按钮，然后_在它仍被按住时_，使用 zone 和 X/Y 按钮切换该 group 中所有 Clip 的 zone 设置。

另见 [Clip 分组](clips/groups.md "mention")

### 效果

Liberation 的效果系统功能强大且灵活，可实时改变 Clip 输出。默认效果按钮 1-8 位于 zone 按钮下方。

#### 应用效果

按下效果按钮可切换效果开关；更推荐使用 APC40 的推子 1-8 来淡入淡出效果。

#### 效果参数

使用旋转控制器 1-8\* 调整每个效果的 _parameter_。（也可以用鼠标右键点击来调整 level 和 parameter）。parameter 的变化会根据效果设置的不同产生不同作用。默认效果见下方列表。

{% hint style="info" %}
效果按钮上显示的小数字表示该效果的 _level_ 和 _parameter_。_level_ 由 APC40 上的推子控制，也可以在按钮上点击并拖动。parameter 由 APC40 上的旋钮调整，也可以右键点击后用鼠标调整。
{% endhint %}

_\*旋转控制器 1-8 位于 APC40 Mk2 顶部，在 Mk1 上位于右上方。另见：_ [APC40 参考](reference/apc40-reference.md "mention")

#### 默认效果

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**：\
   为 Clip 输出应用混乱运动。parameter 调整混乱程度/速度。
2. **Sine wave**：\
   将所有内容沿移动的正弦波进行扭曲。parameter 调整波长。
3. **Rotation**：\
   旋转所有内容。parameter 调整旋转速度。
4. **Horizontal flip**：\
   水平方向挤压和拉伸所有内容。parameter 调整速度。
5. **Scale**：\
   反复将所有内容从完整尺寸缩放到零。parameter 调整速度。
6. **Hue**：\
   改变所有内容的色相，但不改变饱和度（也就是说，白色内容仍保持白色）。parameter 调整色相。
7. **Saturation and hue**：\
   改变所有内容的色相，并将颜色完全饱和（也就是说，白色内容会变为对应颜色）。parameter 调整色相。
8. **Flash**：\
   反复将所有内容的亮度从满亮闪烁到零。parameter 调整闪烁速度。

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

底部一行还有另外 16 个颜色效果，用于应用预设的色相和饱和度值。

请注意，这些是默认效果，但你几乎可以把它们编辑成任何想要的效果！

#### 什么是_“当前选中的 Clip”_？

当你启动一个 Clip 时，它会亮起，表示正在运行。它周围还会有白色轮廓，表示这是当前_选中的_ Clip。每当你切换 zone 按钮或调整 Clip 设置时，这些操作都会应用到_当前选中的 Clip_。

{% hint style="info" %}
如果想选中某个 Clip 但不触发它，请在按 Clip 按钮前先按住 `Alt / Option` 键。这是在不运行 Clip 的情况下调整其 zone 和其他设置的好方法。
{% endhint %}

### Clip Settings 面板

使用 _Clip Settings_ 面板可编辑缩放、X/Y 位置，并访问强大的 zone delay 系统。

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings 面板

使用 _Global Settings_ 面板可调整影响所有 zone 中所有输出的全局输出设置。

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

开启 AUTO RESET 后，当没有 Clip 播放时，会自动重置所有 _Global settings_。

### Timing

几乎所有激光演出都会配合某种音乐音轨，因此 Liberation 的 Timing 系统基于每分钟节拍数的速度。在 _Tempo Panel_ 中，你可以看到时间的可视化表示；每个方块代表一拍，并会按节拍闪烁。

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

这里有多种同步选项，包括 MIDI clock 和 Ableton Link。如果你知道音乐的速度，可以使用屏幕上的滑块或 APC40 的 Tempo 旋钮手动调整；也可以使用 _Tap Tempo_ 系统跟随音乐节拍。

#### Tap Tempo

_Tap Tempo_ 是音乐应用中常用的术语，它让你可以在音乐播放时按节拍敲击来设置速度。你可以使用屏幕上的按钮，但建议使用 _T_ 键或 APC40 上的 _Tap Tempo_ 按钮（如果愿意，也可以使用脚踏开关）。

按 _R_ 键或 APC40 上的 _Metronome_ 按钮，可将速度重置到小节开头。

按 _Y_ 键或转动 APC40 上的 _Tempo_ 旋钮，可将速度取整为整数。这对电子音乐很有用，因为电子音乐的每分钟节拍数通常是整数。

### 整理 Clip Deck

要在 Clip Deck 中移动某个 Clip，请点击并拖动到新位置。拖动时，你可以使用方向键（或 APC40 上的滚轮/按钮）左右滚动。

拖动时按住 `Alt / Option` 键可复制一份。

按住 `Alt / Option` 并点击 Clip，可在不启动它的情况下选中它。

按住 `Alt / Option + Shift` 并点击 Clip 可进行多选，或在 Clip 外点击并拖动进行“套索”选择。

点击并拖动会拖动所有已选中的 Clip。

要删除一个或多个 Clip，可以把它们拖出 Clip Deck（会出现垃圾桶图标），也可以使用 Clip 右键菜单中的 DELETE 按钮。

### Laser Overview 面板

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser Overview_ 面板可以让你快速查看当前运行的激光器状态。右侧的绿色方块表示激光控制器状态正常。如果变成橙色，表示偶尔有掉线；如果变成红色，表示已断开连接。如果是灰色，则表示根本没有连接到控制器。

中间的图表是帧长度历史记录，右侧的数字是当前帧率。内容越复杂，帧率就会越低（也就是更容易闪烁）。低于约 25fps 时，画面就会开始显得有些闪烁。

### 连接到激光器 - Controller Assignment 面板

点击 _Assign Laser Controllers_ 按钮可打开 _Controller Assignment_ 面板。（也可以通过菜单栏中的 _View -> Controller Assignment_ 打开此面板）。

你可以在这里选择哪些激光输出发送到哪些激光控制器。将右侧列表中的控制器拖放到左侧的槽位中即可。你也可以重命名控制器，使其名称与配对的激光器一致（使用笔形图标按钮）。

更多详情请阅读 [控制器分配](setting-up/controller-assignment.md "mention")章节。

{% hint style="danger" %}
在启用任何激光器输出之前，请务必阅读[设置激光器](setting-up/setting-up-lasers.md "mention")章节。
{% endhint %}

### Laser Settings 面板

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

此面板显示_当前选中的激光器_的设置（由顶部的数字表示）。可使用 _tab_ 键、按数字键、点击 _Laser Overview_ 面板中的激光器编号，或在 _Output view_ 中点击来切换当前选中的激光器。

* **Number button** 启用或关闭该激光器输出；如果为红色，表示该激光器已启用输出。
* **Brightness** 调整该激光器的亮度，不影响其他激光器（并且会与 _global brightness_ 设置叠加——也就是说，如果两者都是 50%，该激光器最终亮度为 25%）。
* **Test Pattern** 只为这台激光器开启测试图案（会覆盖全局测试图案设置）
* **Orientation** 校正侧挂或倒挂安装的激光器。
* **Flip Horizontal and Flip Vertical** 反转激光器输出。对于接线不一致的激光器，可用于输出校正。
* **Copy Laser Settings** 打开一个面板，可将这台激光器的各种设置复制到其他激光器。

### 扫描器设置

显示用激光器的工作方式是：极高速移动单束激光，并快速开关光束，从而在空气中绘制形状。你看到的线条、形状和图像，实际上是光束以快到眼睛无法跟上的速度沿路径扫描出来的。

点流是告诉激光器下一步移动到哪里、以及光束何时开启或关闭的数据。在 Liberation 中，Clip 会在发送到激光器时实时转换成这种点流。

Liberation 让你可以详细控制点流的生成方式，从而为每台激光器在平滑度、亮度和性能之间取得平衡。

{% hint style="info" %}
如果你习惯了依赖预计算点流的旧式激光软件，这种方式一开始可能会感觉不同。不过，实时点生成允许同一内容针对每台激光器进行不同优化。这样在使用多台扫描速度或质量不同的激光器时，就不需要复制或重建内容，工作会更简单。它也让 Clip 文件保持得非常小，这就是为什么整个默认 Liberation Clip Deck 只有几 MB，而不是数 GB。
{% endhint %}

基本扫描器设置包括：

* **Speed** 是扫描器速度，也就是激光移动绘制形状的速度。这相当于在传统激光软件中调整点率，但在 Liberation 中，你可以在_不依赖点率_的情况下改变激光移动速度。通常不需要调整此项。
* **Scanner sync**（有时称为 _blank shift_，以前称为 Colour Shift）扫描器会非常快速地移动激光，但亮度和颜色变化通常会与移动不同步。这会表现为光束和线条边缘出现轻微闪烁的光“尾巴”。使用此项调整可让移动与颜色彼此同步。见 [Laser Settings](setting-up/laser-settings.md "mention")

其他高级扫描器设置在[高级](advanced/ "mention")章节中说明。

### Zoning

关于设置激光器和划分 zone 的完整指南，见：[设置激光器](setting-up/setting-up-lasers.md "mention")
