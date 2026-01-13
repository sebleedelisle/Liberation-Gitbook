# ✅ Timecode

Liberation 支持与外部 SMPTE/LTC timecode 信号同步，这在现场音乐演出中常用于让灯光、烟火、视频与伴奏保持同步。

{% hint style="info" %}
什么是 SMPTE/LTC？&#x20;

SMPTE 是 timecode 标准，LTC 是将 timecode 转换为音频信号的形式。如果你听这个音频，会是刺耳的高频尖叫，但对电脑来说它是高精度的时间信息。&#x20;

**Nerd facts!**

历史上 SMPTE 用于让视频与音频同步；如果同步到模拟磁带，通常会在磁带上录入 timecode 音频轨道，这被称为 “striping”。你可以用该轨道让多台磁带机同步，或让 MIDI sequencer 与磁带同步。（这样你无需把 MIDI 乐器录入磁带，混音时由 sequencer 实时播放即可。）

SMPTE 全称 Society of Motion Picture and Television Engineers。LTC 是 _Linear TimeCode_。&#x20;
{% endhint %}

你可以通过电脑上的任何音频接口接收 LTC timecode 信号，但建议使用至少带一个可调 XLR 输入和监听功能的专业接口。&#x20;

我用过 [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) 效果很好，它有耳机监听、2 个 XLR 输入，并且（至少在 MacOS 上）不需要特殊驱动。若你只用于 timecode，可选择略便宜的 [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html)（只有一个输入且无 MIDI）。不过说实话，任何半靠谱的音频接口都应该能用。&#x20;

{% hint style="info" %}
LTC timecode 信号通常通过平衡 XLR 线缆分发，足够稳定地在长距离传输低电平音频信号。（XLR 是麦克风常用的圆形接口）
{% endhint %}

### 硬件连接

将 timecode 的 XLR 线接入你的音频接口，并确保信号良好。调整输入电平，使信号足够强但不过载。如果接口有耳机输出，可直接监听 timecode，确认没有卡顿或噪声过大。&#x20;

{% hint style="info" %}
理论上可以通过 MacBook 的耳机孔接收信号，但需要定制线缆。这些接口通常是 4 极 TRRS 小插孔，我不确定哪些触点可用于音频输入，也不确定可承受电压（听说是 +/-1V，但风险自担！）

我建议直接买个便宜的 USB 音频接口，不要折腾这个。&#x20;
{% endhint %}

如果你的音频接口没有输入监听，可在 OSX 系统设置（_Sound_）中检查是否有信号。（Windows 则用 _Sound Control Panel_）。&#x20;

<figure><img src=".gitbook/assets/Screenshot 2025-03-12 at 11.48.03.png" alt=""><figcaption><p>MacOS 的声音设置面板可显示任何音频接口的输入电平</p></figcaption></figure>

### 在 Liberation 中设置

1. 在 Timecode settings Window 中选择你的音频接口与正确的输入通道。&#x20;

![](<.gitbook/assets/Screenshot 2025-03-12 at 12.13.40.png>)

{% hint style="info" %}
注意：下拉菜单中会为音频接口的每个输入通道提供单独选项。

![](<.gitbook/assets/Screenshot 2025-03-12 at 12.17.11.png>)
{% endhint %}

观察左侧的方块：若接收到有效 timecode 信号会变为绿色，否则为红色。&#x20;

2. 选择输入 timecode 的正确帧率。提供 timecode 的人应能告诉你帧率。（如果设置错误仍能同步，但会每秒出现一个小“跳动”）
3. 在 Timeline 的 timecode 设置中，点击 Timeline bar 上的小钟图标，选择 SMPTE(LTC) 选项。

<figure><img src=".gitbook/assets/Screenshot 2025-03-12 at 12.22.43.png" alt=""><figcaption></figcaption></figure>

4. 调整起始偏移（小时、分钟、秒、帧），与歌曲开始对齐。如果有多个 timelines，每个都需要分别设置。&#x20;

{% hint style="info" %}
在巡演中常见做法是让每首歌从不同的小时开始，例如第一首为 01:00:00:00，第二首为 02:00:00:00，依此类推。

Liberation 会根据 timecode 自动切换 Timeline，因此演出中无需手动切换。&#x20;
{% endhint %}

注意：与 MIDI Clock 或 Ableton Link 不同，SMPTE 是一种 _absolute_ 时间系统，以小时、分钟、秒和帧计。Liberation 的核心时间系统基于节拍和小节，因此接收 timecode 时会使用 Timeline 中设置的 tempo。你需要确保该 tempo 与 timecode 同步的音乐一致。&#x20;
