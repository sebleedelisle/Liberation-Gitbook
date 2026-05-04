---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ 创建 DMX zones

1. 连接 Art-Net 节点，并按照[连接到 Art-Net 节点](../connecting-to-an-artnet-node.md "mention")中的说明完成设置。
2. 打开 **DMX Zones**，然后点击 **ADD DMX ZONE**。
3. 设置该 zone 的 **Node**、**Universe** 和 **Address**，使其与灯具匹配。
4. 为灯具选择一个 **Preset**。该预设定义哪些 DMX 通道接收固定值、内容开/关值、RGB 颜色、X/Y 位置、亮度，或明确的 DMX Value 输入。
5. 点击 **Edit DMX profile/channel mapping**（滑块图标）来编辑通道映射。默认预设会从一个内容开/关通道和 RGB 颜色通道开始。
6. 将 Clip 分配给 DMX zone，方式与分配给 beam zone 或 canvas zone 相同。
7. 当你准备好让该 zone 输出 DMX 时，按下 **ARM**。

{% hint style="warning" %}
只有已启用的 DMX zone 会发送实时数值。未启用的 DMX zone 会将其映射的通道清零，这在设置灯具时更安全。
{% endhint %}

DMX 输出也会受到你的许可证等级限制。如果 **ARM** 按钮被禁用，请检查你的等级是否包含 DMX 输出，或者已启用的 DMX zone 数量是否已达到上限。
