# 🟩 Render profile

每个 _Creator_ node 都有一个 _Render Profile_ 设置，用于决定激光如何绘制（或 _rendered_）形状。&#x20;

**对大多数用途来说，_**DEFAULT**_ 设置完全足够**。但如果你在处理图形或复杂内容，可能希望更精细地控制渲染方式。&#x20;

{% hint style="info" %}
与多数激光软件不同，Liberation 会在输出到激光控制器之前实时生成点流。这能节省大量磁盘空间，Clips 只有几 kB，而不是预渲染点流的 MB 级别。&#x20;

这也意味着你可以针对不同扫描器，在不同激光上调节同一内容，而无需修改 Clips 本身。&#x20;

更多细节见 [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")。
{% endhint %}

有三个预设 _Render Profiles_：_DEFAULT_、_FAST_ 和 _DETAIL_。&#x20;

_**DEFAULT**_ - 通用配置，适合大多数场景

_**FAST** -_ 如果你的 Clip 内容很多且包含大量简单点和直线，选择该选项可能会减少闪烁。&#x20;

_**DETAIL**_ - 需要清晰锐利的转角时使用，但扫描器会更慢，输出可能更闪烁。&#x20;

{% hint style="info" %}
在 Clip Editor 中，你可以为 Creators 选择不同的 render profiles，但每台激光会根据各自的扫描器设置来处理这些 profiles。见 [scanner-presets.md](../../advanced/scanner-presets.md "mention")。
{% endhint %}
