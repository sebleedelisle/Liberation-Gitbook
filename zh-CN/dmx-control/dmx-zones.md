---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# 🟩 DMX zones

DMX zone 是 Liberation 的 Output zone，用于发送 Art-Net/DMX，而不是激光点。它们会与 beam zone 和 canvas zone 一起显示，因此可以在相同的 zone 选择流程中将 Clip 分配给它们。

从菜单打开 **DMX Zones**，或使用 Laser overview 中的 DMX 部分来管理它们。

* **ADD DMX ZONE** - 创建一个新的 DMX zone。
* **ARM** - 启用该 zone 的 DMX 输出。未启用的 DMX zone 会将其映射的通道清零。
* **Node** - 选择 Art-Net node 编号。
* **Universe** - 选择 Art-Net universe。显示值从 1 开始，因此 Universe 1 表示第一个 universe。
* **Address** - 设置灯具的起始地址。显示值同样从 1 开始。
* **Preset** - 选择用于将 Clip 内容映射到 DMX 通道的 DMX 预设。
* **Edit DMX zone settings**（铅笔图标）- 打开 zone 设置，例如手动 zone 转发和灯具方向。
* **Edit DMX profile/channel mapping**（滑块图标）- 打开 DMX 预设/通道编辑器。
* **Delete** - 移除该 DMX zone。

### 启用数量限制

可同时启用的 DMX zone 数量取决于你的许可证等级。如果你的等级不允许 DMX 输出，或你已经启用了数量上限的 DMX zone，其他 zone 的 **ARM** 按钮会被禁用，并在悬停时显示禁止进入图标。

在启用更多 zone 之前，请先停用另一个 DMX zone，或使用具有更高 DMX 限额的许可证等级。
