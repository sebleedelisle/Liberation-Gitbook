# ✅ MIDI send/receive 默认映射

**Clip 的开/关由通道 1 到 14 的 MIDI note on / off 触发**

Clips 有水平（x）和垂直（y）位置，右键点击 Clip 可看到其位置。MIDI 可从 0,0 开始触发 Clips。

{% hint style="info" %}
注意：此系统的 Clip 控制是绝对的，Clip 位置不会随着 Clip Deck 滚动而变化。&#x20;
{% endhint %}

MIDI 通道 1 的 note 1 对应 clip 0,0，note 2 对应 clip 0,1，note 3 对应 clip 0,2，按行向下、按列向右依次排列。到 128 后会进入下一个通道并重新开始。因此你可以通过 MIDI 访问总计 128 x 14 = 1792 个 clips。

Clip 坐标对应的 MIDI note：&#x20;

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Note : 1</td><td>Note : 6</td><td>Note : 11</td><td>Note : 16</td><td>Note : 20 </td></tr><tr><td><strong>y : 1</strong></td><td>Note : 2</td><td>Note : 7</td><td>Note : 12</td><td>Note : 17</td><td>...etc</td></tr><tr><td><strong>y : 2</strong></td><td>Note : 3</td><td>Note : 8</td><td>Note : 13</td><td>Note : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Note : 4</td><td>Note : 9</td><td>Note : 14</td><td>Note : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Note : 5</td><td>Note : 10</td><td>Note : 15</td><td>Note : 20</td><td></td></tr></tbody></table>

注意：MIDI note on 事件会启动 Clip，note off 事件会停止 Clip。这与 Group 的 trigger mode 无关。该系统最初用于回放与录制，因此让按键切换 Clip 并不理想。

### **Effects**

通道 **15** 的 MIDI 控制变更（CC）消息用于调整 effects。\
Effect 1 使用 CC 0-3，值 0-127\
Effect 2 使用 CC 4-7，值 0-127\
Effect 3 使用 CC 8-11，值 0-127\
……依此类推。

每组四个控制对应该 effect 的 level 和 3 个参数：&#x20;

<table><thead><tr><th width="164">Effect :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Level</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...etc</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3 </td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Global settings**

通道 **16** 的 MIDI 控制变更消息用于改变全局设置：\
CC 1：Shift X（水平）0 -127，64 为中间\
CC 2：Shift Y（垂直）0 -127，64 为中间\
CC 4：Scale X\
CC 5：Scale Y\
CC 8：Rotation 3D（Y）\
CC 9：Rotation 2D（Z）

最重要的是：\
CC 15：Global brightness

请注意：该系统最初为录制与回放设计，便于使用 Logic、Ableton 或其他 DAW 创建 Timeline 动画。虽然可用于现场控制，但并未针对现场优化，且部分现场控制功能不如 APC40 完整。
