# ✅ Liberation 无法打开怎么办？

这种情况不常见，但有时 Liberation 可能无法启动，或打开后立即崩溃。几乎都是因为本地配置文件损坏——通常发生在系统崩溃或电脑出现意外之后。

好消息是，重置本地设置即可轻松解决。下面是 macOS 和 Windows 的处理方法。

> **重要**
>
> * 操作前请先关闭 Liberation。
> * 这些步骤只影响本地设置、日志和缓存。你的许可证和账号是安全的。

***

#### 工作文件夹在哪里

每个版本的 Liberation 都有独立的工作文件夹。例如你运行的是 1.0.0，则文件夹名为 1.0.0。

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**快速打开文件夹的方法**

**macOS**

1. 在 Finder 中按 **Shift+Cmd+G**。
2. 粘贴以下路径并按 **Enter**：

    ```
    ~/Library/Application Support/Liberation
    ```
3. 打开与你版本号对应的文件夹，例如 `1.0.0`。

**Windows**

1. 按 **Win+R**，粘贴以下内容并按 **Enter**：

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. 打开与你版本号对应的文件夹，例如 `1.0.0`。

> **Windows 小提示**：如果你通过文件资源管理器浏览，请启用隐藏项目：**View > Show > Hidden items**。

***

#### Step 1 – 安全重置 settings 文件

在你的版本文件夹中打开：

```
data/liberation/
```

在 liberation 文件夹中应该能看到 `settings.json`。删除该文件。&#x20;

* **macOS 示例**：`~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows 示例**：`%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

现在尝试启动 Liberation。如果能正常打开，完成。

***

#### Step 2 – 检查是否是某个 Clip 导致问题

如果 Liberation 在编辑某个 Clip 时崩溃，可能是该 Clip 文件导致的问题。

在 settings.json 同一目录下，应该有一个名为 `clipEdit.json` 的文件。

请先将该文件备份到安全位置（如桌面），然后从 Liberation 工作文件夹中删除它。

再尝试启动 Liberation。如果现在能正常打开，请将备份文件发送到 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)，以便我们分析问题原因。

***

#### Step 3 - 备份后删除整个工作文件夹

如果 Step 1 和 Step 2 都无效：

1. **备份**整个版本文件夹：
   * macOS：右键 `1.0.0` 文件夹并选择 **Compress** 生成 zip，或复制到桌面等安全位置。
   * Windows：右键 `1.0.0` 文件夹并选择 **Send to > Compressed (zipped) folder**，或复制到桌面等安全位置。
2. 备份完成后，**删除** Liberation 工作目录中的原 `1.0.0` 文件夹。
3. 重新启动 Liberation。它会自动创建新的工作文件夹。

如果 Liberation 现在能打开，请继续 Step 4。

***

#### Step 4 - 将备份发送给我们

这有助于我们定位问题并在后续版本中避免它。

如果还没压缩，请先将 Step 3 的**备份**打包为 zip，然后发送邮件给我们：

* **收件人**： [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **主题**：Liberation start-up fix - working folder backup
* **邮件正文**：请包含以下信息
  * 操作系统与版本（例如 macOS 14.6 或 Windows 11 23H2）
  * Liberation 版本（例如 1.0.0）
  * 哪一步解决了问题（Step 1、Step 2 或 Step 3）
  * 问题发生前的简要描述
* **附件**：`1.0.0` 工作文件夹的压缩备份

> 如果 zip 过大，请上传到云盘并分享链接。

***

#### Step 3 之后仍无法启动？

如果删除工作文件夹后 Liberation 仍无法打开：

* 重启电脑再试。
* 临时关闭可能阻止新文件夹创建的杀毒或安全工具，然后再试。
* 重新安装最新版本的 Liberation（覆盖安装）。
* 如果仍不行，请联系 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)，并附上 `logs` 子文件夹中的崩溃日志（如果存在）。

***

#### Summary

1. 删除版本工作文件夹中的 `data/liberation/settings.json`。
2. 如果你正在编辑 Clip，备份并删除 `data/liberation/clipEdit.json`。
3. 如果仍无法打开，备份并删除整个 `1.0.0`（或你的版本号）文件夹。
4. 如果 Step 3 修复了问题（或没有修复），将备份打包后发送到 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)，并注明系统与版本信息。
