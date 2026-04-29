# 🟩 MIDI Send/Receive

MIDI Send/Receive 系统与 APC40 控制是分开的，用于在 Liberation 中发送和接收 MIDI 数据。诸如启动/停止 Clips、调整全局设置、Effects 与 Clip 参数等功能，都有对应的 MIDI 指令。&#x20;

{% hint style="info" %}
MIDI Send/Receive 系统最初是在 Liberation 还没有 Timeline 功能时建立的；你可以用它将演出录制/回放到 Logic Pro 或 Cubase 等音乐软件中。&#x20;

它能直接控制 Clips、Effects 和设置，不受显示或 Clip Deck 滚动位置影响。诸如 tap tempo、分配 zones、arm/disarm 等更系统的现场控制功能尚未实现。&#x20;
{% endhint %}

### MIDI Send/Receive 设置&#x20;

打开 _MIDI Send/Receive_ 面板（菜单 _View -> MIDI Send/Receive_）。你会看到 _SEND、RECEIVE_ 或 _BOTH_ 的发送/接收选项，并可选择要使用的 MIDI 接口。&#x20;

{% hint style="danger" %}
谨慎使用 _BOTH_。某些 MIDI 设备或软件会把接收到的数据回传，这可能造成 MIDI 数据的反馈循环，非常危险！&#x20;
{% endhint %}

### MIDI 映射

见 [MIDI send/receive 默认映射](../reference/midi-send-receive-default-mapping.md "mention")。

未来我计划加入更可定制的 MIDI 映射。在此之前，你可以使用 [BOME](https://www.bome.com/products/miditranslator) 和 [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) 等应用在 Liberation 与自定义硬件之间进行映射转换。&#x20;
