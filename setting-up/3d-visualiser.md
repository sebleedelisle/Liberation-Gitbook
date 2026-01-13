# ✅ 3D Visualiser

### 介绍

Liberation 的 3D visualiser 非常实用——你无需任何激光就能设计和完善演出！我本人也非常依赖它，尤其是在激光数量很多、设置复杂时。

### 在 3D 空间中导航

<figure><img src="../.gitbook/assets/3D View RedWhite.png" alt=""><figcaption><p>3D Visualiser 视图</p></figcaption></figure>

* 点击并拖动以围绕轨道点旋转视角
* 滚轮向前/向后移动至轨道点
* 按住 Shift 键并拖动，可在 XY 平面横向移动镜头（向左、向右、向上、向下）
* 双击 visualiser 内任意位置重置镜头位置

### 设置

通过 _Window_ 菜单打开 _3D Visualiser Settings_ 面板。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings 面板</p></figcaption></figure>

* **Visualiser size** - 调整 visualiser 相对应用的尺寸
* **Brightness Adjustment** - 调整激光的显示亮度
* **Show laser numbers** - 在每台激光上方显示编号
* **Show zone names** - 在每台激光下方显示 Zone 名称

### Camera settings

这些设置主要关联 3D 空间中的虚拟相机。你可以看到一个带预设的下拉菜单，支持保存与加载。

* **Camera distance -** 相机始终指向 _Orbit point_。Camera distance 决定它到该点的距离，也可用滚轮调整。
* **FOV -** 视角（Field of view），决定相机视野宽度/缩放程度。
* **Orbit position** - 描述围绕轨道点的当前旋转。第一个值为绕 X 轴（pitch），第二个值为绕 Y 轴（yaw）。
* **Orbit centre point** - 轨道点在 3D 空间中的位置（x、y、z）。
* **Grid height** - 网格相对 “地面”（即 y = 0）的高度。

### Content settings

这些设置决定激光（以及 Canvas）在 3D 环境中的位置。你可以看到一个带预设的下拉菜单，支持保存与加载。

#### Lasers

每台激光都有一组可展开的设置，通过小白三角展开。

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>3D visualiser 激光设置</p></figcaption></figure>

* **3D Position** - 激光的 x、y、z 位置
* **3D Orientation** - 激光绕 x、y、z 轴的旋转
* **Flip X / Flip Y** - 翻转激光的虚拟输出。注意：通常不需要这样做，最好用激光本身的 flip/orientation 设置来纠正硬件差异。
* **Output Range horizontal / vertical** - 对应激光扫描器的最大/最小角度。60º 是常见值，如你的设备不同可自行调整。

#### Canvas

如果你使用 Canvas 系统，也可以将 Canvas 图像显示在 3D 视图中。勾选该复选框后，通过 position、orientation、scale 设置其在 3D 视图中的外观。

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>3D visualiser Canvas 设置</p></figcaption></figure>

{% hint style="info" %}
看到 “ghost” 激光？3D Visualiser 与实际激光设置是相对独立的，因此可能出现 visualiser 内的激光数量多于 Liberation 的情况。每当你在项目中添加激光，visualiser 中会新增一个激光对象。但如果你删除激光，visualiser 中可能仍保留一个 “ghost” 激光对象。

要移除所有 ghost 激光，点击 _Remove extra 3D laser objects_ 按钮（位于 3D Visualiser settings 面板底部）。

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
