# ✅ 启动 / 停止 Clips

{% hint style="info" %}
你可以用屏幕上的按钮启动和停止 Clips，但更好的方式是使用 APC40 MIDI 控制器。Liberation 针对该硬件进行了优化，应把它视为激光系统的重要投入。&#x20;
{% endhint %}

### 启动与停止 Clips

要启动 Clip，按下该 Clip 的按钮（屏幕上或 MIDI 控制器上均可）。

要停止 Clip，再按一次。

如果你在同一 Group 中启动新 Clip，原先的 Clip 会自动停止。

要在不停止其他 Clips 的情况下启动新 Clip，可以：

* 按住 shift 键（或 APC40 的 shift 按钮）启动新 Clip；或
* 在启动新 Clip 的同时，再次按住正在运行的 Clip。

各 Group 相互独立，在一个 Group 中启动 Clip 不会影响其他 Group。见 [groups.md](groups.md "mention")。

### Flash mode

如果某个 Clip 所在 Group 设置为 _flash mode_，其行为会略有不同：Clip 只会在你按住按钮期间运行，松开即停止。（默认情况下 Group 3（红色）为 _flash mode_。）

### 停止所有 Clips

要**停止所有正在运行的 Clips**，按 **STOP** 按钮。&#x20;

{% hint style="info" %}
连续按 **STOP** 两次可跳过 Clips 的淡出时间并立即熄灭。&#x20;
{% endhint %}

要停止某个特定 Group 中的所有 Clips，先按该 Group 按钮，再按 **STOP** 按钮。&#x20;

要停止除一个之外的所有 Clips，按住你想保留的 Clip，然后同时按 **STOP**，再松开 Clip 按钮。（也适用于多个 Clip，只要你按得住！）



### 当前选中的 Clip

<figure><img src="../.gitbook/assets/clips-selected-active.png" alt="" width="269"><figcaption><p>两条正在运行的 Clip。右侧 Clip 的白色边框表示它是 <em>currently selected clip</em>。</p></figcaption></figure>

运行中的 Clip 会在屏幕上点亮（其 mini clip visualiser 也会闪烁）。你会注意到最后一次按下的 Clip 也有白色边框，这表示它是 _currently selected clip_。

ALT/OPTION 点击 Clip 可在不激活的情况下选中它。ALT/OPTION + SHIFT 点击可多选。&#x20;

你也可以在 Clip Deck 上拖拽套索进行多选。&#x20;

{% hint style="info" %}
APC40 也有 ALT 和 SHIFT 按钮用于选择。&#x20;
{% endhint %}
