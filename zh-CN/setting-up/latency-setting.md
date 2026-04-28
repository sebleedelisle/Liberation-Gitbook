# ✅ 延迟设置

在 _Settings_ 面板（_Liberation->Settings_ 或 CMD/CTRL ,）中，你会看到标注为 _Latency(ms)_ 的滑块。（在旧版本的 Liberation 中，它位于 Laser Overview 面板中）

{% hint style="info" %}
默认延迟 150ms 在大多数情况下足够；如果有网络问题，可以尝试提高。
{% endhint %}

### 稍微复杂一点的解释

这个“帧延迟”设置是 Liberation 生成一帧到激光开始输出这一帧之间的最大时间。如果提高这个值，你可能会感觉 Liberation 与激光输出之间略有延迟。

更长的帧延迟可以让 Liberation 尽早把内容填充到激光控制器的缓冲区；如果网络拥塞，控制器不容易出现点数据耗尽。

这通常只适用于网络 DAC，100ms 的设置应该可以在响应速度和防止网络延迟之间取得良好平衡。如果你的网络非常稳定，应该可以把它降低到 50ms。&#x20;
