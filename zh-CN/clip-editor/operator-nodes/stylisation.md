# 🟩 Stylisation nodes

## &#x20;Randomise

使用一致性的噪声场生成输入元素的散布复制。换句话说，它会以可控的“噪声”方式复制并移动你的形状和点，让内容不再整齐堆在一处，而是像粒子在流场中一样分散。

* **count** – 每个输入元素的复制数量（1–20）。1 表示每个元素只产生一个抖动副本；值越高，散布越多。
* **noise offset** – 在噪声场中循环（0–100%）。可无缝循环，用 Oscillator Node 动画化时所有副本会平滑移动。
* **noise jitter** – 控制噪声纹理尺度。值低则变化平滑，值高则更紧密、更随机。它改变的是图案，不是强度。
* **change between points** – 控制每个副本与前一个副本的差异程度。值低则聚拢相似，值高则分散更明显。
* **face direction** – 让每个副本朝噪声场的运动方向旋转，形成箭头/粒子朝向流动的效果。
* **amount** – 效果整体强度（0–100%），同时缩放位移与 Face direction 的旋转。

{% hint style="info" %}
Randomise node 是 Randomise effect 的核心！
{% endhint %}

## &#x20;Trails

生成内容的“拖尾”，在原始内容移动时留下逐渐变淡或缩放的副本。

* **change render profile for trail** – 开启后，所有拖尾副本使用所选 **render profile**。_见_ [render-profile.md](../fundamentals/render-profile.md "mention")。
* **render profile** – 当上面的开关开启时，用于拖尾副本的 profile。常见用法是主内容设为 **DETAIL**，拖尾设为 **FAST**，这样主形状细节清晰，拖尾渲染更高效。
* **delay** – 拖尾副本之间的时间间隔，以 **1/64-note** 为单位。
  参考：
  * 16 = 1/16 小节（十六分音符）
  * 32 = 1/8 小节（八分音符）
  * 64 = 1/4 小节（四分音符）
  * 128 = 1/2 小节（二分音符）
  * 256 = 1 小节
* **trail size** – 拖尾副本数量。
* **freeze trails** – 将连续流动的拖尾变为一连串静止快照，适合制作断奏、节拍同步的拖尾效果。
* **brightness start / brightness end** – 控制拖尾从最新副本（**start**）到最旧副本（**end**）的亮度变化。通常设 **brightness start** 为 100%，**brightness end** 为 0%，拖尾会逐渐淡出。
* **scale start / scale end** – 控制拖尾从最新副本到最旧副本的缩放。想让拖尾逐渐缩小至消失，可设 **scale start** 100%、**scale end** 0%。

## &#x20;Shimmer

为内容添加闪烁的亮度变化，从轻微闪光到强烈频闪。

* **speed** – 闪烁速度，数值越高闪烁越快；0 则暂停效果。
* **separation** – 相邻点/元素之间的相位差。
  * 0：所有点同步闪烁。
  * >0：邻近点逐渐不同步，闪烁在形状中产生渐变。
  * <0：同上，但相位方向相反。
* **threshold** – 不再平滑渐变，而是根据亮度全开/全关地闪烁。亮度高的元素更频繁亮起。注意亮度 100% 的元素总是亮，0% 的元素总是灭。适合制造清晰的亮点或星光效果。

{% hint style="info" %}
开启 **threshold** 是非常好用的隐藏特性，能让粒子或内容更有生命力。点会根据亮度快速开关。由于同时绘制的点更少，输出更亮、动画更平滑。

但要注意：如果内容本身已经是 100% 亮度，效果不会有变化！
{% endhint %}

* **use whole shape** – 为整个形状应用统一的 shimmer 值。关闭后 node 会细分形状，使不同部分独立闪烁，形成颗粒感。

## &#x20;Particles

这是一个实验性效果，会基于内容生成并动画化粒子。所有点状元素会被视为发射器位置。由于粒子路径是预计算的，如果输入内容变化，可能需要刷新/重新计算粒子（随便改一个设置即可）。

**General**

* **keep original** – 开启后保留原始内容，并在其上叠加粒子。适合让发射器点保持可见。
* **number of particles** – 每次发射生成的粒子数量。值高更密集，值低更简洁。
* **emission period** – 粒子发射在循环中的分布跨度（单位为小节）。100% 时在整个循环内均匀分布；数值更小会更集中爆发。
* **loop length** – 粒子循环时长（小节）。
* **loop count** – 循环重复次数。设为 1 时每次都完全重复；值更高在重置前会引入更多变化。
* **delay** – 发射起始时间偏移，以 1/64 音符计。

**Motion**

* **speed** – 粒子远离发射器的速度。
* **speed variation** – 为速度添加随机性，使粒子不完全一致，分散更自然。
* **direction** – 粒子发射的基础方向，以 **x, y, z angles** 定义。这些角度在 3D 空间旋转向量，可向上、向侧或任意斜向发射。配合 **spread** 使用可形成更宽的锥形或更混乱的爆发。

{% hint style="info" %}
**Euler angles**\
Liberation 使用 **Euler angles** 来描述 3D 空间中的朝向，即绕三条主轴的旋转：

* **X** – 前后倾（像点头）
* **Y** – 左右转（像摇头）
* **Z** – 顺/逆时针翻转（像侧倾脑袋）

通过调整这三个值，你可以将粒子指向任意方向。
{% endhint %}

* **direction variation** – 为方向增加随机扩散，适合制作锥形、喷射或爆炸效果。
* **drag** – 随时间减速，值越高越“沉重”。
* **gravity** – 重力拉下（正值）或推上（负值）。
* **gravity variation** – 为每个粒子的重力增加随机变化，使运动更混沌。

**Life**

* **life duration** – 粒子存活时间（以 1/64 音符为单位）。值小则快速消失，值大则持续更久。
* **life variation** – 为粒子寿命增加随机性，避免同时消失。
* **start delay / start delay variation** – 粒子可见的延迟（1/64-note）。粒子在此期间已生成并运动，但亮度为 0，因此不可见。适合制作延迟出现的烟花“闪点”。

**Colour & brightness**

* **hue start** – 粒子初始颜色。
* **hue variation** – 为颜色增加随机性。
* **hue change** – 粒子生命周期内的色相变化，形成变色拖尾。
* **brightness start / brightness end** – 粒子生命周期中的亮度变化。通常设 brightness start 高、brightness end 低以自然淡出。
* **brightness variation** – 随机化起始亮度，提升动态感。
* **saturation start / saturation end** – 设定起始与结束饱和度。
* **saturation variation** – 为饱和度增加随机变化。

**Simulation**

* **time adjustment** – 加快或减慢整个粒子模拟。适合匹配不同节奏或夸张运动。
