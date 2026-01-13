# ✅ 常见问题（FAQ）

## 硬件

#### **Liberation 支持 Windows 吗？**

是的——Liberation 完全支持 **Windows 10 和 11（64 位）**，功能与 Mac 版一致。每次发布都会同步支持两个平台。

#### **Liberation 支持 Mac 吗**

是的——Liberation 完全支持 **Mac（macOS 12 Monterey 及以上）**，功能与 Windows 版一致。所有更新同步发布。

#### **最低硬件配置是什么？**

这取决于你要控制的激光数量。如果只运行少量激光，较低配置即可。任何 Apple Silicon Mac 都运行良好，应该能控制多达 100 台激光。如果你要跑复杂且关键的演出，建议使用你能负担的最佳配置。

#### **我可以用 Liberation 控制多少台激光？**

Liberation 可以在一台电脑上控制大量激光，已测试超过 100 个激光控制器，具体取决于：

* 你的电脑 CPU
* 网络速度
* 订阅类型

#### **我可以使用哪些 MIDI 控制器？**

Liberation 围绕流行的 APC40 Mk2 MIDI 控制器设计并优化，也支持 APC40 Mk1。参见 [live-control-with-the-apc40.md](midi-control/live-control-with-the-apc40.md "mention")

我们正在逐步增加更多 MIDI 控制器，目前也支持 APC Mini Mk2 和 MIDI Fighter Twister。&#x20;

还可以使用 MIDI Send/Receive 系统提供更多 MIDI 控制能力。参见 [midi-send-receive.md](midi-control/midi-send-receive.md "mention")

更多信息请见 [midi-control](midi-control/ "mention")。

#### **我可以使用任意 MIDI 控制器吗？**&#x20;

我们正在开发可配置的 MIDI 系统，未来将支持这一点。目前，一些用户通过 MIDI 解释器把任意 MIDI 消息转换为 MIDI Send/Receive 系统使用，但这过程较为繁琐且高级。可在[论坛](https://forum.liberationlaser.com)搜索配置建议，但现实中 APC40 仍是最佳选择。&#x20;

## 激光控制器

#### **哪些激光控制器与 Liberation 兼容？**

* [Ether Dream（推荐）](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system)（可能需要更新固件）
* LaserCube USB（以及 LaserDock）
* LaserCube 网络协议（需有线连接）
* AVB（用于 [LASollinger lasers](https://laseranimation.com/en/)）（目前仅 MacOS，处于测试阶段）

更多信息参见 [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention")

#### **为什么不支持 [其他品牌] 激光控制器？**

为促进软件与硬件之间更好的互通，Liberation 只支持公开通讯协议的 DAC。我认为这是激光行业更好的方向。

#### **如何判断我的激光能否与 Liberation 一起使用？**

如果你的激光具备以下任一项，即可与 Liberation 一起使用：

* 外部 **ILDA 输入**——25 针 D 口，需要配合兼容的外部控制器。
* 内置 **Ether Dream**。
* 任何 **LaserCube**（支持 USB 和 Wi-Fi LaserCube）。
* 内置 **Mercury 系统的 X-Laser 设备**（以 Ether Dream 模式运行）。
* 内置 **AVB 的 LaserAnimation Sollinger 投影器**（仅 MacOS，需兼容 AVB 的网络设备，当前在测试中）。

更多信息参见 [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention")

#### **可以用 Liberation 控制我的 LaserCube 吗？**

可以，Liberation 可直接连接任何 LaserCube。参见 [lasercube.md](hardware/lasercube.md "mention")

## 许可证

#### **许可证价格是多少？**

当前价格请见 [shop](https://liberationlaser.com/shop) 页面。

#### **不同授权档位的限制是什么？**

请见 [shop](https://liberationlaser.com/shop) 页面查看当前许可选项。

注意：你可以在 **所有** 档位（包括免费版）中设置、预览并设计任意数量的激光演出。除可 _arm_ 的激光数量外没有其他限制。Liberation 的其他功能对所有档位都可用。

#### **我可以升级到更高档位吗？**

你可以随时升级到更高档位。系统会按当前许可证剩余时间进行部分退款，新方案立即生效。参见 [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **我可以降级许可证吗？**

你可以随时降级，但更改会在当前许可证周期结束时生效。参见 [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **如何用许可证授权我的电脑？**

购买许可证后，可在 Liberation 内进行授权。你会在 _About_ 页面看到 _Authorise_ 按钮，点击后会提示你登录网站。按屏幕提示完成授权流程。参见 [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **需要多久连接一次互联网？**

每次许可证续订时都需要将 Liberation 连接到互联网以更新内部许可证。如果是按月续费，则每月需要连接一次。

#### **续订后无法连接互联网会怎样？**

许可证续订后，Liberation 会提供 7 天宽限期让你连接互联网并更新内部许可证。超过该期限后，Liberation 将回到 _Free_ 模式。

#### **信用卡过期会怎样？**

你会收到支付服务商的邮件通知，需要更新支付信息。登录网站，在订阅页面使用 _Update payment details_ 链接。

#### **如何取消自动续费？**

登录网站，打开 _Your subscriptions_ 页面，选择要取消的订阅，然后点击 _Cancel Subscription_ 链接。你仍可在当前许可证周期内继续使用 Liberation。

#### **我可以在多少台电脑上安装 Liberation？**

你可以在任意数量的电脑上安装 Liberation。只有启用激光 / DMX 输出时才需要授权，许可证档位决定可同时授权输出的电脑数量。参见 [how-licensing-works.md](installation/how-licensing-works.md "mention")

#### **如何把许可证从一台电脑转移到另一台？**

* 在不再使用的电脑上打开 Liberation
* 确保已连接互联网，在 _About_ 页面点击 _De-authorise this computer_ 按钮
* 在新电脑上打开 Liberation
* 在 _About_ 页面点击 _Authorise this computer_ 按钮
* 网站会打开，登录并按屏幕提示完成授权

你也可以远程取消授权无法访问的电脑（有一定限制）。参见 [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **丢失或被盗的电脑可以取消授权吗？**

可以在网站上取消该电脑的授权。如果该电脑自上次续订后一直未联网，可以立即取消。

否则，取消授权会在订阅续订时或该电脑连接互联网时生效，以先发生者为准。如果你需要紧急重新授权新电脑，请联系支持。

### 使用 Liberation

#### 默认设置是 8 台激光，如何更改？

参见 [setting-up-your-project.md](setting-up/setting-up-your-project.md "mention") 和 [adding-removing-lasers.md](setting-up/adding-removing-lasers.md "mention")

#### 可以把一个激光的 Zones 设置复制到其他激光吗？

可以！参见 [copy-zones-between-lasers.md](output-view/copy-zones-between-lasers.md "mention")

#### 可以不用滑块直接输入数值吗？

可以！按住 CMD/CTRL 点击滑块，然后用键盘输入数值。

#### **如何让 Liberation 与音乐同步？**

它有一个智能的 “tap tempo” 系统，使用方式与预期一致；你也可以使用外部 MIDI 时钟或 Ableton Link。参见 [tempo-synchronisation.md](tempo-synchronisation.md "mention")。Timeline 还可以通过任意音频接口输入的 LTC/SMPTE timecode 同步。参见 [timecode.md](timecode.md "mention")。

#### 为了获得最佳激光输出，需要调整哪些设置？

主要设置是 _Colour Shift_，用于补偿反光镜移动与激光亮度变化之间的轻微延迟。如果激光点/光束出现小 “tails”，就需要调整此项。（示例可见 [laser-settings](setting-up/laser-settings/ "mention") 页面中的照片）

你也可以尝试调整扫描器速度：扫描器较基础时可降低，较好时可提高。但 **请谨慎使用，因为过度驱动可能损坏扫描器。**

还有一些扫描器预设。默认选项较保守，适合大多数激光束需求。如果你有更好的扫描器，或需要针对图形的预设，也可以选择其他预设。

更多信息参见 [laser-settings](setting-up/laser-settings/ "mention")；如何创建自定义预设请见 [scanner-presets.md](advanced/scanner-presets.md "mention")（高级，进行中）。

你还可以通过 _Colour calibration_ 设置校正颜色平衡。参见 [colour-calibration.md](advanced/colour-calibration.md "mention")（高级技术）。

#### _Latency(ms)_ 设置的作用是什么？

这是帧延迟，即从生成帧到发送给激光之间的最大时间。通常无需调整，但若出现网络问题可以尝试提高。详见 [latency-setting.md](setting-up/latency-setting.md "mention")。

### Clips

#### 不运行 clip 也能调整 zones 和设置吗？

按住 ALT/OPTION 点击，使其成为 _currently selected clip_ 但不激活。另见 [starting-stopping-clips.md](clips/starting-stopping-clips.md "mention")

#### 如何复制 clips？

按住 ALT/OPTION 点击并拖动。另见 [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### 如何删除 clips？

将它们从 Clip Deck 上拖出去。另见 [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### 如何多选、删除、合并 Clip Deck 等？

参见 [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### Clip 上的小麦克风和其他图标表示什么？

这些图标表示该 clip 需要声音或 MIDI 输入，3 个点表示有 zone delay。参见 [what-are-the-small-icons-on-the-clip-buttons.md](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
