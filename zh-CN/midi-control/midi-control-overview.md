---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 MIDI 控制概览

Liberation 使用 MIDI 的方式有多种：&#x20;

* 作为现场控制器。APC40 Mk1/Mk2、APC Mini 和 MIDI Fighter Twister 在匹配设备可用时可以自动连接。见 [现场 MIDI 控制器](live-control-with-the-apc40.md "mention")。
* 作为时钟同步源，使用 MIDI clock 与 MIDI song position 消息。见 [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")。
* 在 MIDI notes node 中作为交互输入，创建“激光竖琴”风格效果。见 [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")。
* 作为更通用的输入/输出系统，使用 MIDI Send/Receive。见 [MIDI Send/Receive](midi-send-receive.md "mention")。

受支持的现场控制器会跟随 Liberation 的屏幕状态：Clip 按钮会以其分组颜色亮起，zone 按钮会显示 zone 状态，已映射的旋钮或编码器会跟随当前效果或 Parameters 面板中的控件。
