# 🟩 Zone delay / chase

大家都知道激光越多越好玩，但如果它们做的完全一样，就会错过不少创意可能。

Zone delay 系统是一种简单但有效的方法，可在不同 Zones 之间制造变化，并充分发挥多激光设置的优势；它也可用于更传统的 chase 效果。

#### 原理

_Zone delay_ 会在各个 Zone 之间加入时间延迟，形成一种扫过 Zones 的效果。

将 Zone delay 加在已经运行的 Clip 上效果很好，可使用 APC40 的相关控制来调节级别和模式。（见 [apc40-reference.md](../reference/apc40-reference.md "mention")）。你也可以通过 _Clip Settings_ 面板调整。

Zone delay 设置：

* **Zone delay** - 控制每个 Zone 的延迟量，以 64 分音符计。
* **Pattern** - 选择 Zone 的顺序
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern 基于 Zone 编号，并假设你的 Zones 从左到右排列。在计算 Pattern 时，Zone delay 会将 canvas zones 和 DMX zones 视为独立组。
{% endhint %}

* **Delay mode**
  1. No delay - chase 模式使用
  2. Delay - 默认模式，为每个 Zone 延迟时间
  3. Delay with re-trigger - 每次沿 Pattern 扫过时将 Clip 重置到开头，适合配合 _Chase mode_ 使用
* **Chase mode** - 开启后，每个 Zone 会像传统 chase 效果一样开关。通过 _Fade in_、_Hold_、_Fade out_ 调整效果外观。这些设置按 _Zone delay_ 值的比例计算，例如值为 1 表示与 _Zone delay_ 相同时间。文字不好解释，建议亲自试试。

{% hint style="info" %}
Zone delay 也会作用于任何激活的效果。例如闪烁效果会在 Zones 之间延迟，并且 Clip 本身的动画也会延迟。
{% endhint %}

当 Clip 启用了任何 _Zone delay_ 时，你会在 Clip 右上角看到三个点的图标。这些点会动画显示该 Clip 的 _Zone delay_ 模式。详见 [what-are-the-small-icons-on-the-clip-buttons.md](what-are-the-small-icons-on-the-clip-buttons.md "mention")。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>表示 Clip 有 zone delay 及其模式的三点图标</p></figcaption></figure>

{% hint style="info" %}
Zone delay 是每个 Clip 自身的设置，不是全局；它是 Clip 的创作设计的一部分。
{% endhint %}
