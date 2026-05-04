---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip 设置

### Clip settings 面板

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip settings 面板</p></figcaption></figure>

使用 _Scale X_ 和 _Scale Y_ 调整 Clip 输出大小。除非按住 _SHIFT_，否则它们会联动。&#x20;

使用 _Shift X_ 和 _Shift Y_ 调整 Clip 的水平和垂直位置。

_Zone Delay/Chase_ 是非常有趣的功能，单独有一节说明。见 [Zone Delay/Chase](zone-delay-chase.md "mention")。

### 参数面板

Clip Deck 右侧的面板会显示八个与当前上下文相关的参数。选中某个 Clip 后，前几个控件分别是所选 Clip 的 _Shift X_、_Shift Y_ 和 _Zone Delay_，之后是全局的 _Spin_ 和 _Scale_ 控件。

这些参数也会同步映射到受支持的 MIDI 控制器。如果未选中 Clip，Clip 专用的几个位置会留空。如果按住某个分组按钮，前两个控件会改为该分组的淡入和淡出时间。

### 锁定 Clips

Clip 被锁定后无法移动或删除。要锁定 Clip，在右键菜单中勾选 _Locked_。在 Clip settings 面板中还有更多选项：

* _UNLOCK ALL -_ 解锁 Clip Deck 中的所有 Clips。&#x20;
* _AUTO-LOCK_ - 当 _Auto-Lock_ 开启时，任何自动播放的 Clip（通过 Timeline 或 MIDI record/playback 系统）都会被锁定。这在你用 Logic Pro（或类似软件）编排演出时很有用，可避免误改用于演出的 Clips。&#x20;
* _LOCKED CLIPS ZONES_ - 开启后无法更改任何已锁定 Clip 的 Zones
* _LOCKED CLIPS PARAMS_ - 开启后无法更改任何已锁定 Clip 的参数（scale、shift 等）。&#x20;

### 右键菜单

右键点击 Clip 会出现该 Clip 的部分选项。关于菜单前几项的更多说明，见 [Clip Editor 介绍](../clip-editor/clip-editor-intro.md "mention")、[Clip 设置](clip-settings.md "mention") 和 [Clip 分组](groups.md "mention")。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

默认情况下，Clips 处于 _retrigger_。这意味着无论你在何时按下，Clip 都会从当前时刻开始播放。因此如果你启动得晚，动画也会晚一点。 &#x20;

{% hint style="info" %}
如果在 retriggered Clip 运行时执行 _Tap Tempo_，系统会将 Clip “quantise” 到节拍上，即使你没有精确地在拍点启动。&#x20;
{% endhint %}

如果未启用 _Retrigger_，Clip 将始终保持在节拍上——就好像它从时钟起点开始播放。这适用于通过外部时钟信号与音乐严格同步的情况。 &#x20;

{% hint style="info" %}
Clips 通常设计为无限循环，但你也可以让它只运行一次或几次。请确保这些 Clip 仍设置为 _retrigger_，否则它们不会重新开始！
{% endhint %}

### Transition in/out time（fade）

可以为 Clip 设置淡入和淡出，时长以秒为单位。默认情况下，淡入淡出时间会继承其分组设置（可通过右键点击分组按钮更改）。

如果你希望与 Group 的淡入淡出不同，先关闭 _USE GROUP DEFAULT_，然后调整 Clip 的 _In time_ 和 _Out time_ 滑块。&#x20;
