# 🟩 Canvas target areas

我们已经知道如何将 Canvas 的部分内容发送到每台激光的 zones，但要让内容进入 Canvas，本身需要（名字虽有些绕但确实准确的） _Canvas target areas_。&#x20;

_Canvas target areas_ 是你可以绘制 Clip 内容的 Canvas 区域，在 _CANVAS_ 视图中以蓝色轮廓矩形显示。&#x20;

很多时候你只需要一个 Canvas target area，然后把它拆分成多个 zones 发送到不同激光。&#x20;

有时你也会需要多个 Canvas target areas，用于建筑的不同部分，或利用它们之间的 zone delay。（没错！Zone delay 在 Canvas target areas 之间依然有效。）&#x20;

### 将 Clips 发送到 Canvas target areas

在 Clip Deck 中，beam zone 按钮旁边就是 Canvas target area 按钮。你可能需要滚动输出按钮才能看到它们：使用 SHIFT + 左右方向键，或屏幕上的 ZONE PAGE 按钮，或 APC40 按钮（见 [apc40-reference.md](../reference/apc40-reference.md "mention")）。

像使用 beam zone 按钮一样，通过切换这些按钮将 Clips 分配给 Canvas target areas。&#x20;

### 添加 / 编辑 Canvas target areas

在顶部菜单选择 _View -> Canvas Target Areas_，你会看到项目中每个 Canvas target area 的所有设置。&#x20;

顶部有 _ADD CANVAS TARGET AREA_ 按钮。&#x20;

点击带减号的红色按钮可删除 Canvas target area。&#x20;

使用滑块调整大小和位置。双击滑块可输入数值。&#x20;

### Scale mode

* **FIT TO AREA** - 在保持纵横比的前提下缩小内容，使其完全适配 Canvas target area。（默认）
* **FILL AREA** - 在保持纵横比的前提下拉伸内容以填满 Canvas target area，可能会裁切边缘。&#x20;
* **STRETCH TO FIT** - 拉伸内容以填满 Canvas target area，忽略纵横比。

###
