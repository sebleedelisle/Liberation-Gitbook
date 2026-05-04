---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 现场 MIDI 控制器

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40 controller**&#x20;

这是 Liberation 默认的硬件控制器；强烈推荐，可以说 Liberation 从一开始就是围绕它设计的。只要插入 APC40，Liberation 会自动连接。&#x20;

{% hint style="warning" %}
_糟了！演出中 USB 被拔掉了！_&#x20;

别慌——再插回去，Liberation 会自动重新连接，一切正常。&#x20;
{% endhint %}

### APC40 Mark 1 还是 Mark 2？&#x20;

简而言之，推荐 Mark 2，因为它有全彩按钮，更接近 Liberation 的 Clip Deck 界面。Mark 1 也能用，但布局与屏幕略有差异，而且按钮只能显示红/橙/绿三色，无法匹配 Clip 颜色，会更难用。&#x20;

{% hint style="info" %}
原版 APC40 Mark 1 于 2009 年发布（没错！），至今仍有人偏爱它的金属机身和控制台般的结实手感。更新后的 Mark 2 于 2014 年发布，虽然在 2024 年停产，但因视觉艺术家（Resolume 等）和激光师的需求，2025 年将重新投产。
{% endhint %}

APC40 的完整控制列表见 [APC40 参考](../reference/apc40-reference.md "mention")。

### APC Mini

Liberation 1.0.3 还包含 APC Mini 配置文件。它映射了 8x5 Clip 网格、zone 按钮、zone X/Y 翻转控制、分组按钮、停止所有 Clip、Clip 页面移动、zone 页面移动、tap tempo、小节重置和速度微调。它的推子用于控制效果电平，按住 Shift 后的推子用于控制效果参数。最后一个推子用于控制 Global Brightness。

### MIDI Fighter Twister

MIDI Fighter Twister 配置文件更适合以编码器为主的控制，而不是启动 Clip。其中一排编码器控制效果槽 1–8 的参数 1，另一排则跟随 Parameters 面板中的八个上下文控制，包括 Clip 偏移、zone 延迟、全局旋转/缩放以及分组淡入淡出。
