# 🟩 MIDI notes

## &#x20;MIDI notes

创建“laser harp”风格的效果：输入的 MIDI 音符会在一段范围内触发光束或形状。该 node 会使用传入的内容作为每个音符的 _source_——如果输入一个点，就会得到一排点；输入圆形，就会得到一排圆形，更复杂的形状也同样复制。

你可以在 **Liberation → Settings (CMD/CTRL ,)** 中选择 Liberation 监听的 MIDI 接口。

* **midi channel** – 监听的 MIDI 通道（0 = 所有通道，1–16 = 指定通道）
* **width** – 音符展开的总宽度。
* **midi note min / max** – 范围内的最低与最高 MIDI 音符值。
* **ignore out of range notes** – 过滤超出范围的音符。关闭时，超出范围的音符会被“夹紧”到最近的音符（高音触发上限，低音触发下限）。
* **auto extend range** – 当演奏超出范围的音符时自动扩展范围。

{% hint style="info" %}
不确定自己能弹到哪些音域？打开 **auto extend range**，将 **midi note min** 设得很高、**midi note max** 设得很低，然后演奏你的音符。系统会捕捉并扩展范围。确认后关闭 **auto extend range** 以锁定范围。
{% endhint %}

* **leave all notes visible** – 为范围内所有音符创建光束/形状，不管它们是否在播放，从而形成“laser harp”效果。
* **hit colour** – 音符触发时出现的颜色。
* **hit colour hold time** – hit colour 保持满亮度的时长。单位为秒（0–1）。_100% = 1 second._
* **hit colour decay time** – hit colour 在保持后淡回的时间。单位为秒（0–1）。_100% = 1 second._

{% hint style="info" %}
如果内容本身已经是纯白色，hit colour 设置为白色不会有变化。最佳做法是让内容本身为饱和色，再将 hit colour 设为白色，这样触发时会有很好的闪光效果。
{% endhint %}

* **note off fade out time** – 音符释放后的淡出时间。单位为秒（0–1）。_100% = 1 second._
* **hit scale factor** – 音符触发时的缩放倍数（如 2 = 放大一倍）。
* **hit scale hold time** – 放大后保持的时间。单位为秒（0–1）。_100% = 1 second._
* **hit scale decay time** – 缩回原大小所需时间。单位为秒（0–1）。_100% = 1 second._
* **note off shrink time** – 音符释放后缩回原大小所需时间。单位为秒（0–1）。_100% = 1 second._（开启 **leave all notes visible** 时无效。）

{% hint style="info" %}
Scaling - 注意：如果内容是单个点，缩放不会有任何效果！
{% endhint %}
