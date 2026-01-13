# ✅ 激光输出设置面板

通过菜单 _View -> Laser Output Settings_ 打开 _Laser output_ 设置面板。

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

面板会显示当前选中激光的设置，可通过以下方式切换：

* 在 _Laser Overview_ 面板中点击其编号按钮
* 使用键盘数字键 1 到 0 打开激光 1-10
* 使用 _TAB_ 键在激光之间循环（_SHIFT + TAB_ 反向）。

在面板顶部你会看到：

* 一个编号按钮——点击以 arm/disarm 该激光。激光 arm 时为红色。
* 该激光独立的 _Brightness_ 滑块。注意它会与全局亮度叠加。
* _Test Pattern_ 开关和图案选择器。可为该激光单独指定测试图案。（这些控件在 Output view 工具栏中也有对应）。

### 输出方向 / 镜像修正

以下设置用于修正激光的安装方向，使其在 Liberation 中表现一致。

* **Flip horizontal / vertical** - 用于校正激光输出方向

{% hint style="info" %}
除非激光接线错误或背面有 X/Y flip 按钮且设置不正确，否则不需要调整 horizontal / vertical flip。如果你想为某个 Clip 翻转输出，可以在 Clip 本身设置。
{% endhint %}

* **Orientation** - 当激光侧装或倒装时，可用此设置校正旋转方向。
* **Fine position adjustments** - 用于细微的位移/旋转修正，适合修正激光长时间运行后的漂移或沉降。

{% hint style="info" %}
注意：orientation / mirroring 修正不会影响 3D Visualiser，它们用于校正实际激光输出以匹配 3D Visualiser 中的显示。
{% endhint %}

### 复制激光设置

参见 [#copy-laser-settings](./#copy-laser-settings "mention")。

### 扫描器设置

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

速度设置决定扫描器移动速度。

{% hint style="danger" %}
尽管默认设置较为保守，但若速度过高仍可能损坏扫描器。提高速度时请谨慎。
{% endhint %}

{% hint style="info" %}
此速度设置不会改变点率，而是调整点的分布范围。更多信息见 [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")。
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

光束在扫描器移动时改变颜色并开关，但两者通常并非完全同步。该设置用于校正两者的时间对齐。

{% hint style="info" %}
这有时被称为 _blank shift_，但我更喜欢 _scanner sync_ 这一说法，因为它更准确：它调整的是所有颜色变化与扫描器移动之间的时序。
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>激光 “tails” - Colour shift 设置不当</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>没有激光 “tails”！Colour shift 正常！</p></figcaption></figure></div>

如果看到激光输出有小 “tails”，通常是 scanner sync 需要调整。如果无论如何都存在 tails，可能是扫描器/激光驱动被你开得过快。尝试降低扫描器速度。

#### Scanner presets

用于选择预设的扫描器设置。默认选项通常足够，除非你的扫描器特别差（或特别好），否则无需更改。想深入了解请见 [scanner-presets.md](../../advanced/scanner-presets.md "mention")。

#### Colour calibration

可用此系统校正激光的亮度曲线与白平衡。参见 [colour-calibration.md](../../advanced/colour-calibration.md "mention")。

#### Advanced settings

通常不需要调整，但如果你想了解更多，请见 [advanced-laser-settings.md](../../advanced/advanced-laser-settings.md "mention")。
