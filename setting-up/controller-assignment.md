# ✅ 控制器分配

当你在 Liberation 中设置好激光后，就可以将每台激光分配到实际的激光控制器。（参见 [compatible-lasers-and-controllers-dacs.md](../hardware/compatible-lasers-and-controllers-dacs.md "mention") 以确认可用硬件）。控制器要么通过 USB 连接，要么通过网络连接。&#x20;

* 通过菜单 _View -> Controller Assignment_ 打开 _Controller Assignment_ 面板。（也可以在 _Laser Overview_ 面板中点击 _ASSIGN LASER CONTROLLERS_ 按钮。）

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment panel"><figcaption></figcaption></figure>

* 面板分为左右两部分：左侧是激光列表，右侧是可用控制器列表。如果列表里看不到你的控制器，点击 _REFRESH_ 按钮。若仍有问题，请参见 [troubleshooting](../troubleshooting/ "mention")。&#x20;
* 将控制器分配给激光：从右侧拖拽到左侧的空激光槽位即可。这样 Liberation 就知道哪台激光对应哪个控制器。（如果你改变主意，也可以随时在激光之间上下拖拽控制器。）&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="List of controllers" width="375"><figcaption></figcaption></figure>

* 若控制器旁显示绿色方块，表示 Liberation 已成功连接。&#x20;

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>一台 Ether Dream 和一台 Helios DAC 分别分配给激光 2 和 3</p></figcaption></figure>

{% hint style="info" %}
注意：每次连接控制器时，激光会自动 disarm。&#x20;
{% endhint %}

* 橙色方块 🟧 表示控制器连接不稳定，通常由网络问题引起，参见 [troubleshooting](../troubleshooting/ "mention")。
* 红色方块 🟥 表示无法连接控制器，参见 [troubleshooting](../troubleshooting/ "mention")。&#x20;
* _disconnect button_（X）会断开连接，但不会清除分配。你可以用 _reconnect button_（刷新箭头图标）重新连接，或再次点击 _disconnect button_ 来清除分配。&#x20;
* _Advanced feature :_ 点击图表形状的按钮可打开控制器分析面板。这是高级功能，可提供数据流细节并帮助排错。（某些控制器类型可能不支持。）
* 可使用 _rename button_（铅笔）为控制器重命名，以便与硬件对应。例如 _LaserCube Ultra #1_ 或 _Triton T5 #3._ 这些名称会随 Liberation 安装保存，之后会一直显示，便于快速识别。&#x20;

{% hint style="info" %}
小技巧：在右侧控制器上**双击**，可自动分配到左侧下一个可用激光槽位。如果你有很多激光需要分配，会非常省时间！&#x20;
{% endhint %}

你可以使用 _DISCONNECT ALL_ 和 _RECONNECT ALL_ 按钮快速重置所有连接，适用于处理网络问题。&#x20;
