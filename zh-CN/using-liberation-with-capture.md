# 🟩 在 Capture 中使用 Liberation

Liberation 支持将 [Capture](https://capture.se) 作为外部 visualiser（1.0.3 及以上版本）。如果你已经在工作流中使用 Capture，可以用它在 3D 场景中可视化 Liberation 的实时激光输出。

### 工作方式

不需要额外的连接流程，也不需要手动绑定。

只要满足以下条件：

* Liberation 和 Capture 在同一网络中
* 防火墙允许连接

……那么你在 Liberation 中设置的所有激光都会自动出现在 Capture 中，作为 media source。你不需要配置 IP 地址，也不需要启用额外选项，它会直接出现。

### 在 Capture 中看到激光

Liberation 中已配置的所有激光都会在 Capture 中显示为可用的 media sources。

若要真正看到输出：

* 该激光必须在 Liberation 中处于 armed 状态
* 该 source 必须已附加到 Capture 中的某个激光 fixture

当激光 arm 后，Capture 会可视化来自 Liberation 的实时输出流。如果某台激光在 Liberation 中被 disarm，它仍会在 Capture 中显示为 source，但不会输出任何内容。

更多设置与支持请参阅 [capture.se](https://www.capture.se/) 上的文档。 <br>

### 许可证限制与 armed lasers

Capture 连接与真实激光输出被视为完全相同。

这意味着：

* 你只能 arm 与许可证档位允许数量相同的激光
* 只有已 arm 的激光才会主动向 Capture 发送数据

### 我一定需要 Capture 吗？

完全不需要。

Liberation 内置了 3D visualiser，始终可用，也不受许可证档位影响。你可以直接在 Liberation 中完成设计与预览，而无需任何外部软件。

如果你本来就在使用 Capture 做灯光或演出设计，它只是一个额外选项。

### 故障排除

如果激光没有出现在 Capture 中：

* 检查两个应用是否在同一网络
* 检查防火墙设置
* 确认该激光已在 Liberation 中 arm
