# 🟧 Tempo / synchronisation

音乐同步是 Liberation 的基础能力；只要把 tempo 与拍点对齐音乐，就能确保一切同步。如果你能使用 MIDI clock（或 Ableton Link），几乎无需手动同步。但即使没有也不用担心——你可以使用 _Live_ tempo 功能手动对齐。

如果你有音乐或灯光软件经验，这个流程会很熟悉。若没有，建议先花时间熟悉系统，并在家里练习后再用于现场演出。

## Tempo panel

_Tempo_ 面板始终显示在屏幕上，包含所有同步设置。顶部显示当前小节/拍计数，以及播放/暂停与快退/快进的传输控制。

下方是拍点指示器：四个方块随节拍“脉冲”闪烁。这个 _beat marker_ 非常有用，你会在使用 _Live_ tempo 系统时频繁依赖它。

### 设置 tempo

你可以通过以下方式设置 tempo：

* 拖动 _Tempo_ 滑块
* 按住 Shift 拖动 _Tempo_ 滑块，以 0.1 为步进调整
* 双击 _Tempo_ 滑块并手动输入数值
* 使用 APC40 上的 _Tempo_ 旋钮（按 Shift 为 0.1 步进）
* Tap Tempo

{% hint style="info" %}
Tempo 以 “beats per minute” 定义，传统默认值通常是 120。
{% endhint %}

## Tap Tempo

点击 _TAP_ 按钮跟随节拍来自动设置 tempo。用 _RESET_ 按钮设定小节起点。

{% hint style="info" %}
Tap Tempo 足够智能：它能判断你是否暂停了一段时间，或漏了几拍。如果你以双倍速度点击，它会理解为要加倍 tempo；半速点击也同理。

它还能处理两个人同时在敲击 tempo（例如键盘与 APC40 同时 tap）。Liberation 会对双击进行平均。
{% endhint %}

#### 键盘命令：

T - tap tempo\
R - reset 小节\
Y - 将 tempo 四舍五入到最近的 BPM

{% hint style="info" %}
如今大多数音乐都是数字制作，tempo 通常为整数。如果 tap 的 tempo 接近整数，可使用 Y 键（或把 APC40 tempo 旋钮微调一个“tick”）将其四舍五入到整数。
{% endhint %}

#### APC40 控制：

APC40 有专用 _TAP TEMPO_ 按钮，也可以用连接的脚踏开关来 tap！

使用 _TEMPO_ 旋钮调整。按 _SHIFT_ 可进行更细微调整。

使用 _METRONOME_ 按钮来**重置小节**。（注意 _METRONOME_ 按钮也会随拍点闪烁）

将 _TEMPO_ 旋钮向左或向右移动一个“tick”可**将 tempo 上/下四舍五入**到整数 BPM。

另见 [apc40-reference.md](reference/apc40-reference.md "mention")。

### Nudge tempo

如果你感觉 tempo 已经接近，但仍逐渐偏离，可使用 _NUDGE_ 按钮修正。

如果 Liberation tempo 领先音乐，按住 _NUDGE -_ 让它临时变慢直到重新对齐。

如果 Liberation tempo 落后音乐，按住 _NUDGE +_ 让它临时变快直到重新对齐。

{% hint style="info" %}
你可以使用屏幕上的 NUDGE 按钮，也可以使用 APC40 的专用按钮。
{% endhint %}

### Half time / double time

使用 _÷2_ 和 _x2_ 按钮将 tempo 永久减半或加倍。与 tempo multiplier 不同，这是对当前 tempo 的永久修改。

## Tempo Multiplier

_Tempo Multiplier_ 系统允许你临时调整 tempo，然后恢复为原值。

点击 _TEMPO MULTIPLIER_ 按钮或 APC40 上的 _BANK_ 按钮启用。使用屏幕滑块或 APC40 A-B 滑块调整。也可使用 _25%、50%、100%、200%_ 预设按钮。

## 外部 tempo 源

### MIDI Clock

要同步外部 MIDI clock 信号，选择 _MIDI CLOCK_ 单选项并在下拉菜单中选择 MIDI 设备。留意下拉菜单旁的状态灯：

* 绿色 - 正在接收 MIDI clock 信号
* 橙色 - 可连接设备，但当前没有 clock 信号
* 红色 - 无法连接设备

{% hint style="info" %}
MIDI Clock 会广播一系列帧（每四分音符 24 帧），但消息中不包含位置信息。因此它适合保持节拍，但你可能仍需重置小节。

Liberation 的 MIDI Clock tempo source 也响应 **MIDI Machine Control (MMC)** 消息，因此如果 clock 源发送 MMC，你无需手动重置小节。
{% endhint %}

### Timeline

每条 Timeline 都有自己的 tempo，可为固定值或 _Tempo Map_。_Tempo Map_ 允许你在 Timeline 的特定时间点调整 tempo。

当选择 _TIMELINE_ 作为 tempo source 时，会使用 Timeline 的 tempo。

{% hint style="info" %}
你可以让 Timeline 与_任意_ tempo source 同时运行！例如乐队没有 click，你可以手动启动 Timeline 并使用 _LIVE_ tempo 保持同步；如果有 MIDI clock 信号，也可以直接使用它！
{% endhint %}
