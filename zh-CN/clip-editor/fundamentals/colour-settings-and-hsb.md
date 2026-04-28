# 🟩 颜色设置与 HSB

Liberation 中的颜色使用 HSB 而不是 RGB。你可能不太熟悉，但一旦习惯就会发现更直观。&#x20;

{% hint style="info" %}
如果你更喜欢 RGB，可以点击任意颜色设置中的颜色方块。这会打开颜色编辑面板，可选择 RGB 或 HSB。&#x20;
{% endhint %}

### HSB - Hue, Saturation and Brightness

#### Hue &#x20;

Hue 的范围是 0 到 255。0 为红色，数值增加会依次经过彩虹的每一种色相：橙、黄、绿、青、蓝、紫、洋红，最后在 255 回到红色。&#x20;

由于这是一个循环，你可以用三角波在所有颜色间循环。&#x20;

#### Saturation

该设置控制颜色的饱和度/鲜艳程度，范围 0 到 255。饱和度设为 0 为灰度，255 为完全饱和，中间值会得到柔和的粉彩色。&#x20;

{% hint style="info" %}
给美国朋友道个歉，color 我这里多了一个 u。Liberation 在英格兰开发，所以默认是英式拼写。未来我希望提供法语、西班牙语、德语、意大利语、简体中文，甚至美式英语的翻译。:innocent:
{% endhint %}

#### Brightness

最容易理解：0 为全黑，255 为最亮。&#x20;

### 示例

#### 彩虹循环：&#x20;

将 _Brightness_ 和 _Saturation_ 设为 255。把 _Sawtooth_ oscillator 连接到 _Hue_ socket，并将其范围设为 0 到 255。&#x20;

#### 亮度呼吸：&#x20;

把 _Sawtooth_ oscillator 连接到 _Brightness_ socket，并将范围设为 255 到 0。你还可以调整 clamp min/max 来控制变化时长，再用 easing functions 细化动画。&#x20;

#### 硬闪 / 频闪：&#x20;

通过 _Hue_ 和 _Saturation_ 或颜色选择器选定颜色。把 _Square Wave_ oscillator 连接到 _Brightness_ socket，将范围设为 255 到 0。&#x20;

#### 在自定义色相范围内循环：&#x20;

将 _Brightness_ 和 _Saturation_ 设为 255。把 _Triangle Wave_ oscillator 连接到 _Hue_ socket，并设置范围：&#x20;

* 蓝到青：范围 70 到 128
* 红到黄：范围 0 到 40
* 红到洋红：范围 255 到 220
