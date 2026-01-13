# ✅ 兼容的激光与控制器（DAC）

### 哪些激光与 Liberation 兼容？

如果你的激光具备标准 ILDA 输入，就可以与 Liberation 一起使用（需搭配兼容的激光控制器，如 Ether Dream 或 Helios DAC——[完整列表见下方](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)）。

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC - 家用最便宜的选择</p></figcaption></figure>

以下情况无需外部控制器或 ILDA 输入：

* 你的激光内部安装了 Ether Dream，或
* 你使用 Wicked Lasers 的 LaserCube，或
* 你使用内置 Mercury 的 X-Laser 设备，或&#x20;
* 你使用内置 AVB 控制器的 LaserAnimation Sollinger 激光（目前仅 MacOS，处于测试阶段）

{% hint style="info" %}
#### 什么是激光控制器？

激光控制器（或 DAC）是一种硬件设备，用于接收来自 Liberation 的数字数据并转换成控制扫描器与激光输出所需的模拟信号。（因此 DAC：Digital to Analog Converter。）

控制器通过 USB 或标准网络连接到电脑；它可能是外置设备，也可能安装在激光内部。

如果是外置设备，就通过 ILDA 连接到激光。ILDA 是行业标准，使用老式 25 针 D 形接口。准备一根 ILDA 线，一端接控制器，另一端接激光。
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>外置 Ether Dream 上的 ILDA 输出</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>激光后面板，含 ILDA 输入等多种接口</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>标准 ILDA 线</p></figcaption></figure>

### 哪种控制器最适合我？

如果你是家庭用户，或运行少于 4 台且距离电脑较近的小型演出，USB 控制器如 **Helios DAC** 是**最实惠**的选择。

网络 DAC 如 **Ether Dream** 是专业激光师的**最佳选择**，适合搭建网络并运行大量激光；目前大型的 Liberation 演出几乎都在使用 Ether Dream。

如果你有 **LaserCube**，就不需要单独的激光控制器——Liberation 与所有 LaserCube 兼容。早期型号通过 USB 连接，新型号通过网络连接。

如果你是专业用户且想要最省事的方案，可考虑内置 Mercury 的 X-Laser 设备，或使用 AVB 的 LaserAnimation Sollinger 激光。&#x20;

### 兼容的激光控制器

#### Ether Dream（网络）

[Ether Dream](https://ether-dream.com) 已经存在十多年，目前版本为 4（Liberation 也支持 Ether Dream 1、2、3 版）。它们非常可靠。

通过标准网络连接。可以作为独立设备购买，也可以安装在激光内部。

#### Helios（USB）

[Helios](https://bitlasers.com/helios-laser-dac/) 是入门级最佳选择，价格比 Ether Dream 更低，但由于通过 USB 连接，不建议使用长距离线缆。连接超过 4 台时也可能出现 USB 数据或驱动问题（尤其在 Windows 上）。

如果你只是想在家里运行一两台激光，这是最便宜也最简单的选择。

#### Mercury（内置于 X-Laser 设备）

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) 是 X-Laser 的强大 DMX 激光控制系统，面向希望直接从传统灯光控制台运行激光的灯光设计师。通过最新固件更新，Mercury 还包含 **Ether Dream emulation**，因此可以与 Liberation（以及任何支持 Ether Dream 的软件）无缝配合。

#### AVB（内置于 LaserAnimation Sollinger 设备）

**AVB** 是一种基于网络的开放协议，用于高性能、低延迟的音频和数据传输。许多 LaserAnimation Sollinger 投影器在硬件中直接支持 AVB，使 Liberation 能通过网络连接它们而无需外置 DAC。Liberation 中的 AVB 支持目前**仅限 MacOS 且处于测试阶段**，并且需要**兼容 AVB 的网络设备**。正确设置后，它能提供更简化的工作流、更少的外部设备，并且可靠性更强。

#### 未来将支持的控制器：

* [IDN](http://www.ilda-digital.com)（ILDA 的开放网络协议，可由任意厂商实现）

### 线缆建议

为获得最佳性能，尽量把 USB DAC 放在电脑附近，使用更长的 ILDA 线连接激光。（不过要注意：拆装时 ILDA 线可能像“抓钩”一样容易勾到东西！）

如果使用 Ether Dream，你可以将它们集中放置并用长 ILDA 线连接激光；或将它们安装在激光附近，改用更长的网线。

理想的设置是将 Ether Dream（或其他控制器）直接安装在激光内部（英国的 Stanwax Laser 的 Rob 可以帮你完成）。
