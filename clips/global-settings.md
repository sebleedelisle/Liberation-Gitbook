# 🟩 全局变换

除了 Clip 变换（shift x/y、scale x/y）之外，还有作用于所有运行中 Clips 的 Global Transformations。打开 _Global Transformations_ 面板即可查看（该面板通常与 _Clip Settings_ 在同一标签页中）。&#x20;

默认情况下，当没有 Clip 运行时这些设置会立即重置。你可以在 _Global Transformations_ 面板底部用 _AUTO RESET_ 按钮关闭此行为。&#x20;

{% hint style="info" %}
注意：Global Transformations 不会影响 Canvas，只作用于 Beam 和 DMX zones。&#x20;
{% endhint %}

### Scale X/Y

水平与垂直缩放。除非按住 SHIFT，否则两者联动。默认映射到 APC40 Device Control 旋钮 4 和 8，并显示在 Clip Deck 右侧面板中。

### Shift X/Y

水平与垂直位移，将全部内容整体平移。&#x20;

### Spin

围绕中心旋转所有内容。正值顺时针，负值逆时针。该设置会影响 _Rotation_ 变换。默认映射到 APC40 Device Control 旋钮 3，并显示在 Clip Deck 右侧面板中。&#x20;

### Spin 3D

围绕 Y 轴（中心垂直线）旋转所有内容。该设置会影响 _Rotation3D_ 变换。默认映射到 APC40 Device Control 旋钮 7，并显示在 Clip Deck 右侧面板中。&#x20;

### Rotation

围绕中心旋转，单位为度。&#x20;

### Rotation 3D

围绕 Y 轴（中心垂直线）旋转，单位为度。&#x20;

### Auto reset

开启后，只要当前运行的所有 Clips 都被关闭，所有 Global Transformations 就会立即重置，确保下次运行时不会出现意外。&#x20;
