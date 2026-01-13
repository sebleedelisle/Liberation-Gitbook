# 🟩 加载与保存

Liberation 会持续将状态保存到磁盘，因此即使遇到断电或系统问题，重新启动也会回到离开的位置，你不应丢失 Zones、Timeline 或其他内容。&#x20;

不过，你仍可以导出设置用于备份或迁移到另一台电脑。

### Project Import/Export

Project 文件几乎包含当前设置中的所有内容，包括：&#x20;

* [#laser-settings-import-export](loading-and-saving.md#laser-settings-import-export "mention") 中列出的所有内容
* Clips、effects 与 group 设置&#x20;
* 所有 timelines（不包含音频和视频媒体）
* Art-Net 设置&#x20;
* MIDI send/receive 设置
* Tempo / synchronisation 设置

目前不保存/加载：&#x20;

* MIDI notes node 和 Sound Input Oscillator 中的音频/MIDI 输入设置（但会保存 MIDI send/receive 设置以及 timecode 的音频输入）
* 界面缩放&#x20;
* Canvas guide images 的媒体文件&#x20;
* Timeline 的音频与视频媒体&#x20;
* Text node 使用的字体

{% hint style="danger" %}
Timeline 的音频与视频文件不会随 project 文件保存，如需迁移到其他电脑，请单独保存。见 [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files "mention")。
{% endhint %}

### Laser settings Import / Export&#x20;

* 每台激光的 Laser settings&#x20;
* Beam zones
* Canvas target areas&#x20;
* DMX zones
* Laser controller assignment（以及已重命名控制器的别名）&#x20;
* Laser scanner 与 colour calibration 设置及 presets&#x20;
* 3D visualiser 设置与 presets

### Clip Deck Import / Export

* 所有 Clips 及其 zone 分配、设置与参数
* 所有 group 设置、flash mode、淡入/淡出时间等

目前不保存/加载：&#x20;

* 所有 effects 及其参数与设置&#x20;

{% hint style="info" %}
#### 只从 project 文件导入 Clips（不加载整个项目）

要仅导入 Clips，选择 _**Clips->Import Clip Deck**_，并选择 project 文件而不是 Clip Deck 文件（.cpdk）。
{% endhint %}

### Append Clip Deck

使用 _Append Clip Deck_ 将导出的 Clip Deck 文件追加到当前项目。Clips 会添加到当前 Clip Deck 的末尾，但文件中的 effects 与 group 设置不会导入。&#x20;

### Export Selected Clips

将当前选中的 Clips 导出到文件。不会保存 group 设置与 effects，仅保存 Clips。注意：正在运行的 Clips 若未被选中则不会导出。&#x20;

{% hint style="info" %}
Option/Alt - shift - 点击 Clips 进行选择（或使用套索）。被选中的 Clips 会有较粗的白色轮廓。见 [starting-stopping-clips.md](clips/starting-stopping-clips.md "mention")。
{% endhint %}

### Effects Import / Export

保存与加载所有 effects 以及其 group 设置和参数。&#x20;

{% hint style="info" %}
#### 只从 project 文件导入 Effects（不加载整个项目）

要仅导入 Effects，选择 _**Effects->Import Effects**_，并选择 project 文件而不是 effects 文件（.efts）。
{% endhint %}

### Timeline Export

导出包含一个或多个 timelines 的 timeline 文件。注意：导出的 timeline 文件**始终包含** Clip Deck（不过你在导入时可选择要导入哪些 clips，见下方 [#timeline-import](loading-and-saving.md#timeline-import "mention")）。

如果项目中有多个 timelines，会出现面板让你选择要导出的 timelines。

{% hint style="danger" %}
Timeline 的音频与视频文件不会随 timeline 文件保存，如需迁移内容请单独保存。见 [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files "mention")。
{% endhint %}

### Timeline Import&#x20;

从单个 timeline 文件中导入一个或多个 timelines。选中文件后会弹出面板，提供多种导入选项。&#x20;

若 timeline 文件包含多个 timelines，它们都会列出，勾选要导入的即可。

* Replace existing timelines\
  用导入的 timelines 替换当前所有 timelines
* Import used clips only\
  仅导入被使用的 Clips，并按 Timeline 分组排列。若不选中该项，则会将 timeline 文件的整个 Clip Deck 追加到现有 Clips。&#x20;
* Replace existing clip deck\
  用 timeline 文件中的 Clips 替换当前 Clip Deck。仅在勾选 _Replace existing timelines_ 时可用。&#x20;

{% hint style="info" %}
#### 只从 project 文件导入 Timelines（不加载整个项目）

要仅导入 Timelines，选择 _**Timeline->Import Timeline(s)**_，并选择 project 文件而不是 timeline 文件（.ltml）。
{% endhint %}

### DMX / Art-Net import / export

保存并加载 Art-Net nodes 及其 IP 地址，同时包含 DMX zones 和所有 DMX presets。



### 关于 Timeline 媒体文件的重要说明

Timeline 的音频与视频文件**不会**随 timeline 文件导出，如需迁移到其他电脑，请确保一并携带这些文件。&#x20;

{% hint style="info" %}
#### Timeline 对媒体文件的查找方式&#x20;

加载 Timeline 时，系统会在 Timeline（或 project）文件所在目录及其子目录中查找媒体文件。所以只要媒体文件在同一目录或子目录（如 _/videos_ 或 _/sound_）中，就能被正确加载。&#x20;
{% endhint %}
