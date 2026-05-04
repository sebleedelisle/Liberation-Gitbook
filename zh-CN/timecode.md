---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ 时间码

Liberation 支持与外部 SMPTE/LTC 时间码信号同步。现场音乐演出中常用这种方式，让灯光、烟火、视频和伴奏轨保持同步。

{% hint style="info" %}
什么是 SMPTE/LTC？

SMPTE 是一种时间码标准，LTC 则是把这种时间码转换成音频信号。如果你直接听这段音频，会听到非常刺耳的高频尖叫声；但对计算机来说，它是高精度的时序信息。

**硬核小知识！**

过去，SMPTE 常用于保持视频和音频同步；如果要同步到模拟磁带，通常会把时间码音频录到其中一轨上，有时也称为给磁带“划码”（striping）。你可以用这条时间码轨让多台磁带机彼此同步，或者让 MIDI 音序器与磁带同步。（这样你就不必把 MIDI 乐器录到磁带上，只需要在混音时让音序器实时播放它们！）

SMPTE 是 Society of Motion Picture and Television Engineers（电影与电视工程师协会）的缩写，该组织定义了这项标准。LTC 是 _Linear TimeCode_（线性时间码）的缩写。
{% endhint %}

你可以通过计算机上的任意音频接口接收 LTC 时间码信号，但建议使用专业音频接口，至少带一个可调电平的 XLR 输入，并具备监听能力。

我使用 [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) 的体验不错，因为它支持耳机监听，有 2 个 XLR 输入，而且不需要任何专用驱动（至少在 macOS 上是这样）。如果你只打算把它用于时间码，可以选择稍便宜的 [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html)（它只有一个输入，也没有 MIDI），不过说实话，任何还算过得去的音频接口应该都能用。

{% hint style="info" %}
LTC 时间码信号通常通过平衡 XLR 线缆传输，因为这种线缆足够可靠，可以在较长距离上传输低电平音频信号。（XLR 是通常用于麦克风的圆筒形接口）
{% endhint %}

### 硬件连接

将时间码信号的 XLR 线缆插入音频接口，并确认信号良好。调节音频接口上的输入电平，直到信号足够强但没有削波。如果音频接口带耳机插孔，可以监听时间码，确认没有断续、毛刺，且噪声不过多。

{% hint style="info" %}
理论上，可以通过 MacBook 上的耳机/音频插孔接收信号，但这需要自制线缆。这类插孔通常是 4 极 TRRS 迷你插孔。说实话，我不确定其中哪些触点可以用作音频输入，也不确定它能承受多大的电压电平（我在某处看到过是 +/-1V，但请自行承担风险！）

与其尝试这种方式，我认为你最好直接找一个便宜的 USB 音频接口。
{% endhint %}

如果你的音频接口没有任何输入监听功能，可以在 macOS 系统设置中（_Sound_ 下）检查是否有信号。（在 Windows 上，请使用 _Sound Control Panel_）。

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS 会在 Sound 系统设置面板中显示任意音频接口的输入电平</p></figcaption></figure>

### 在 Liberation 中设置

1. 在 Timecode 设置窗口中选择你的音频接口和正确的输入通道。

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
请注意，下拉菜单中会为音频接口的每个输入通道分别提供选项

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

留意左侧的方块：如果正在接收有效的时间码信号，它会变成绿色；否则会显示为红色。

2. 为传入的时间码选择正确的帧率。提供时间码的人应该能告诉你帧率是多少。（如果选错了，仍然可以同步，但你会注意到每秒会有一点“跳动”）
3. 使用时间线栏上的小钟图标打开 Timeline 的 timecode 设置，并选择 SMPTE(LTC) 选项。

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. 调整起始偏移量（小时、分钟、秒、帧），使其与歌曲开头匹配。如果你有多个 timeline，需要分别为每一个设置这些选项。

{% hint style="info" %}
在巡演行业中，一个常见约定是让每首歌从不同的小时数开始，例如第一首歌为 01:00:00:00，第二首歌为 02:00:00:00，依此类推。

Liberation 会根据时间码自动切换到对应的 timeline，因此演出过程中你不需要手动切换 timeline。
{% endhint %}

请注意，与 MIDI Clock 和 Ableton Link 不同，SMPTE 是一种_绝对_时间系统，以小时、分钟、秒和帧计量。Liberation 的核心时间系统基于拍和小节，因此在接收时间码时，它会使用 timeline 中设置的速度。你需要确保这个速度与同样同步到时间码的音乐保持一致。
