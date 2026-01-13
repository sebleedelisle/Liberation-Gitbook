# 🟩 Zones

你在大多数项目中使用的主要 Zone 类型是 _Beam zone_，用于空气中的光束效果。另一种是 _Canvas zone_（见 [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention")）。&#x20;

{% hint style="danger" %}
**警告 - 在激光运行时移动 Zones 必须极度谨慎**，并将亮度降到最低。完整安全指南见 [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention")。
{% endhint %}

你可以用鼠标点击并拖动 Zones。打开测试图案以观察该 Zone 的位置。&#x20;

{% hint style="info" %}
使用方向键**微调**当前选中的 Zone/点位。按住 SHIFT 可进行更大步进。&#x20;
{% endhint %}

{% hint style="info" %}
小技巧：可以快速在多台激光间复制 Zone 设置！见 [copy-laser-settings.md](../setting-up/laser-settings/copy-laser-settings.md "mention")。
{% endhint %}

### 添加新的 beam zone

点击工具栏顶部的 _Add a new beam zone_ 按钮，新的 Zone 会出现。注意 beam zones 会按添加顺序排序，但可以重新排序。见 [re-ordering-beam-zones.md](re-ordering-beam-zones.md "mention")。

### 添加已有的 canvas zone

点击 _Add existing canvas zone_ 按钮，会显示可用的 canvas zones 列表，可为该激光启用或关闭。见 [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention")。

### Zone 形状类型

共有 3 种 Zone 形状：&#x20;

* **Quad** - 默认矩形 Zone，可为轴对齐或变形。适合大矩形 Zones 或需要透视校正的 Canvas zones。&#x20;
* **Line/Curve** - 由 2 个或更多点与厚度定义的 Zone。适合细长 Zones，或用于阳台、桥梁等曲线边界。&#x20;
* **Segmented** - 可细分为多个小 Quad 的 Zone，适合建筑映射。&#x20;

在任意 Zone 上右键可打开设置菜单，可执行：

* 重命名 Zone（便于在 Clip Deck 中识别，尤其是 Zones 很多时）
* 启用/禁用 Zone&#x20;
* 锁定位置&#x20;
* 更改形状类型
* 重置为默认位置
* 访问形状特定设置
* 删除&#x20;
* 添加 _Alt Zone_（见 [alt-zone-system.md](alt-zone-system.md "mention")）

{% hint style="danger" %}
**警告 -** 激光启用时切换 Zone 类型务必小心。Zone 会恢复到该形状上次的大小/位置，输出可能突然变化。最好在切换 Zone 类型前先关闭激光。&#x20;
{% endhint %}

### Quad zone 形状

用鼠标移动 Quad 的每个角。ALT/OPTION 点击角点可独立移动并扭曲 Quad。Quad 一旦扭曲，所有角点都可自由移动。&#x20;

通过右键菜单中的 _REMOVE DISTORTION_ 按钮可取消扭曲并恢复为轴对齐矩形。&#x20;

#### Perspective correction

此选项可通过右键菜单中的开关设置，用于选择扭曲方式。用于 beams 时最好关闭；若此 Zone 用于在平面上投影图形，则应打开以进行透视校正。&#x20;

{% hint style="info" %}
当 _Perspective correction_ 关闭时，内容使用 _bi-linear interpolation_ 扭曲，也就是内容在 Quad 内均匀分布，因此更适合 beams。

开启透视校正后，内容通过透视扭曲来补偿近大远小。如果你在斜角墙面投影图形，可用此功能纠正投影失真。&#x20;
{% endhint %}

### Line / Curve zone 形状

Line / Curve 已成为我最近演出中的首选，有人甚至认为它应作为 beam zones 的默认形状。&#x20;

实际场地里，Zones 往往需要很细以适配狭窄空间或建筑窗间缝隙；这时调整 Quad 的四个角会非常繁琐，因此 Line / Curve Zone 就诞生了！&#x20;

直线只需两个点，然后在右键菜单中调整 _Zone thickness_。这是创建简单 Zones 的最快方式。&#x20;

ALT/OPTION 点击线条可添加点。这些点会自动平滑形成流线形，你可通过 _Smooth level_ 调整弧度。&#x20;

ALT/OPTION 点击某个点可删除。&#x20;

如果你熟悉矢量软件（Inkscape、Illustrator 等），还可以使用 _Manually adjust bezier curves_ 选项精细调整控制点。&#x20;

### Segmented zone 形状

该分段 Zone 可进行非常精细的校正，适合复杂形状的映射。可在右键菜单中使用 + 和 - 按钮添加或减少分段。&#x20;

### 如何编辑被另一 Zone 完全覆盖的 Zone

右键上层 Zone，点击锁形按钮将其锁定。然后即可编辑下方 Zone。&#x20;



<br>

{% hint style="info" %}
当你在输出中添加一个 Beam zone 后，它会出现在 Clip Deck 中供 Clip 选择。&#x20;
{% endhint %}
