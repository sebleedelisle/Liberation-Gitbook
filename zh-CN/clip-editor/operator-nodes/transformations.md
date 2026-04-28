# 🟩 Transformations

## &#x20;Translate

沿 x、y 和/或 z 轴移动所有内容。注意坐标系以中心为原点，x/y 轴范围为 +/-200。见 [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention")。

* **x** - 沿 x 轴移动距离（左 - 右）。
* **y** - 沿 y 轴移动距离（上 - 下）。

#### 3D 选项（选择 3D 时可用）

* **z** - 沿 z 轴移动距离（向屏幕内/向屏幕外）。

## <img src="../../.gitbook/assets/image (2) (1).png" alt="" data-size="line"> Rotate

旋转所有内容。数值单位为度。见 [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention")。

* **rotation** - 内容顺时针旋转角度（度）。旋转中心为原点 (0,0)。
* **pivot point x / pivot point y** - 用于偏移旋转中心。

#### 3D 选项（选择 3D 时可用）

* **rotation x** - 绕 x 轴旋转（pitch）。
* **rotation y** - 绕 y 轴旋转（yaw）。
* **pivot point z** - z 轴上的旋转偏移位置。

## <img src="../../.gitbook/assets/image (3) (1).png" alt="" data-size="line"> Scale

缩放所有内容。

* **scale** - 缩放百分比。
* **scale x / scale y** - 只在水平/垂直方向缩放时使用。

{% hint style="warning" %}
任一轴缩放为 0% 时，该内容会消失！
{% endhint %}
