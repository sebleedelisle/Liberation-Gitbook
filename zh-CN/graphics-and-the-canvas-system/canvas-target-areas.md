---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas 目标区域

我们已经了解了如何把 Canvas 的不同部分发送到每台激光器内的 zone 中；但如果想先把内容放到 Canvas 上，就需要使用（名字有点容易混淆，但确实准确的）_Canvas target areas_。

_Canvas target areas_ 是 Canvas 上可供 Clip 绘制到其中的区域，在 _CANVAS_ view 中以蓝色描边矩形显示。

很多时候，你可能只需要一个 Canvas target area，然后再把它拆分成多个 zone，分别发送到不同的激光器。

有时你也可能希望为建筑物的不同部分使用多个 Canvas target area，或者利用它们之间的 zone 延迟。（没错！zone 延迟在不同 Canvas target area 之间仍然有效！）

### 将 Clip 发送到 Canvas target area

查看 Clip Deck 时，在 beam zone 按钮旁边会看到 Canvas target area 按钮。你可能需要滚动 output 按钮才能看到它们，可以使用 `Shift + Left / Right Arrow`，或屏幕上的 ZONE PAGE 按钮，或 APC40 按钮（参见 [APC40 参考](../reference/apc40-reference.md "mention")）。

分配 Clip 到 Canvas target area 的方式与使用 beam zone 按钮完全相同：切换这些按钮即可。

### 添加 / 编辑 Canvas target area

在顶部菜单栏中选择 _View -> Canvas Target Areas_，你会看到项目中每个 Canvas target area 的全部设置。

顶部有 _ADD CANVAS TARGET AREA_ 按钮。

使用带减号的红色按钮可以删除 Canvas target area。

使用滑块调整大小和位置。双击滑块可输入数值。

### 缩放模式

* **FIT TO AREA** - 将内容缩小，使其完整放入 Canvas target area 内，同时保持宽高比。（这是默认设置）
* **FILL AREA** - 将内容拉伸以填满 Canvas target area，同时保持宽高比。内容可能会在边缘被裁切。
* **STRETCH TO FIT** - 将内容拉伸以填满整个 Canvas target area，忽略宽高比。
