# 🟧 介绍

Liberation 内置灵活强大的 DMX 系统，可通过 Art-Net 创建灯光效果并控制兼容 DMX 的激光设备。它让灯光与激光演出保持同步变得简单——无需额外灯光控台。

{% hint style="info" %}
**什么是 Art-Net？它与 DMX 的关系是什么？**

**DMX** 是一种多年广泛用于控制灯光、激光、烟机等舞台设备的系统。它通过专用线缆（通常是 XLR 接头）发送控制信号，每个设备监听特定的通道范围来执行动作。

**Art-Net** 是在标准计算机网络上发送同样 DMX 数据的新方式。它不需要专用线缆，而是通过以太网传输，就像普通的网络流量一样。

在 Liberation 中，所有 DMX 输出都通过 Art-Net 发送。你可以直接控制兼容 Art-Net 的设备，也可以连接一个 **Art-Net node** ——一个将 Art-Net 转换回标准 DMX 的小盒子。这样即使设备本身不支持 Art-Net，也能通过 Liberation 控制传统 DMX 灯光与效果。
{% endhint %}

你还可以控制各种舞台设备，例如烟机、雾机、CO₂ 喷射、冷焰火等。只要支持 DMX，就可以设置为 DMX zone，并与激光内容并行触发。

DMX 设备以 **DMX zones** 添加，会与激光 beam zones 和 canvas target areas 一起出现在 zone 列表中。每个 DMX zone 使用一个 **DMX preset**，它告诉 Liberation 如何将激光 Clips 的属性（如位置、颜色、亮度）映射到 DMX 通道值。

当你将一个 Clip 发送到 DMX zone 时，Liberation 会读取 Clip 的第一个元素，并按 preset 将其属性转换为 DMX 值。这让你可以直接用同一套 Clips 来驱动灯光和 DMX 效果。

#### Liberation 在 Glastonbury

<figure><img src="../.gitbook/assets/ArcadiaSpider2023.jpg" alt=""><figcaption></figcaption></figure>

Liberation DMX 系统的首次真实测试是在 2023 年的 Glastonbury。当时 Reach Lasers 在 Arcadia “spider” 舞台安装了共 90 个光束源。&#x20;

其中 18 台激光由内置 Ether Dream 控制，另有 12 组 6 头 beam bars 通过 Art-Net 和 DMX 控制。&#x20;
