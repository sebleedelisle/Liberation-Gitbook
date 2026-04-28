# 🟩 升级到新版本时迁移内容

Liberation 会把内容存放在工作文件夹中（见 [where-to-find-the-working-folder.md](../troubleshooting/where-to-find-the-working-folder.md "mention")），且每次新版本发布时该路径都会变化。如果你想把旧版本的工作文件保留到新版本：&#x20;

1. 打开旧版本的 Liberation
2. 使用 _File->Project->Export Project_。这会保存你在 Liberation 中的所有内容：激光设置、Timeline、Clip Deck 等。&#x20;
3. 关闭旧版本，再打开新版本的 Liberation
4. 使用 _File->Project->Import Project_，选择第 2 步导出的项目文件。&#x20;

现在你的所有内容应该已经在新版本中。

#### 保留多个 Liberation 版本

安装新版本前，先重命名旧版本——我通常用版本号命名，例如 Liberation103.app（Windows 下是 .exe）。你可以保留任意多个版本，但一次只能运行一个。 <br>

#### 如果你用新版本覆盖了旧版本

最稳妥的做法是重新安装旧版本，再按上述流程操作。&#x20;

或者，你也可以尝试复制工作文件夹并将其重命名为新版本号。&#x20;
