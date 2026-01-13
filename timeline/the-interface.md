# 🟧 界面

### Timeline 界面

如果你用过音乐或视频软件，Timeline 的概念会很熟悉：这是一个水平网格，时间从左到右流动，你可以在上面放置 Clips 来定义何时播放。

如果你没用过 Timeline，可以把它理解为乐谱或舞台提示表——每个块代表某段内容在特定时刻被触发。这是一种结构化的方式来设计激光演出随时间展开的过程。

***

#### Timeline Bar Controls

**Enable Button**

在与 Timeline 交互前必须先启用它。点击 **ENABLE** 开关（启用时为橙色）以激活 Timeline 的编辑与播放。

**Timeline Name**

当前 Timeline 的名称显示在 Enable 按钮旁（默认是 **“Timeline”**）。点击可重命名，便于管理多首歌曲或多个段落。

**Timeline List (Three Bars Icon)**

点击打开 Timeline 列表。在此可切换 Timeline 或新增/移除。

**Lock Button**

保护 Timeline，防止误操作。启用后编辑会被锁定，直到解锁。

**Add Clips Button**

将当前选中的 Clips 从 Clip Deck 添加到 Timeline 的播放头位置。适合从现场表演或预选片段快速搭建 Timeline。

**Insert Audio File**

打开文件对话框，在 Timeline 起始位置插入音频文件。支持格式：WAV、MP3、OGG、FLAC。适合让 Timeline 与音乐对齐。

**Default Clip Duration**

设置通过拖拽或 + 按钮添加到 Timeline 的新 Clip 默认长度（以小节计）。可加快编排速度。

**Volume**

调节 Timeline 上所有音频 Clips 的播放音量，不影响激光输出。

***

#### Transport and Playback

**Transport Controls**

用于导航的标准控制按钮&#x20;

* Forward / back（每次移动 1 小节）
* Stop / Rewind to start&#x20;
* Play / pause
* Record

**Bar / Beat / Step Display**

以 bars:beats:frames 格式显示当前 Timeline 位置。播放时实时更新。

***

#### Sync and Timing

**Tempo Map Button**

启用 tempo mapping。开启后会在 Timeline 顶部出现一行，可右键添加 tempo 变化。适合节奏变化或渐变速度的音乐。

**Timecode Panel**

打开 timecode 设置面板。在此可配置 Liberation 与 LTC、MIDI Clock 或 Ableton Link 同步，以便与外部系统精确对齐。

**SNAP Toggle**

开启后，Clips 与编辑操作会吸附到网格，方便精确对齐。关闭则可自由摆放。

**Snap Size**

设置网格分辨率——小节、拍或步。适合精细编辑或快速对齐。

***

#### View and Playback Behavior

**Auto Scroll (Skater Icon)**

启用后，播放时 Timeline 会自动跟随播放头滚动。

**Scrub Mode (Light Bulb Icon)**

启用后，手动移动播放头时激光保持实时输出。适合预览特定帧，但请谨慎使用，尤其是高功率投影器。

**Loop Playback**

按 Timeline 设定长度循环播放，适合打磨特定段落或运行背景视觉。

**Timeline Length**

设置 Timeline 总长度（以小节计）。可拖拽调整，或双击直接输入数值。
