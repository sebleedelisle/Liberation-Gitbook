---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ 常見問題

## 硬件

#### **Liberation 可以在 Windows 上運行嗎？**

可以。Liberation 完全支援 **Windows 10 及 11（64-bit）**，功能與 Mac 版本完全相同。每個版本都會同時在兩個平台發佈。

#### **Liberation 可以在 Mac 上運行嗎？**

可以。Liberation 完全支援 **Mac（macOS 12 Monterey 或以上）**，功能與 Windows 版本完全一致。所有更新都會同步發佈。

#### **最低需要甚麼規格的電腦？**

這取決於你想控制多少部激光。如果只運行少量激光，規格較低的電腦也可以。任何 Apple Silicon Mac 都運行得很好，應該可以控制最多 100 部激光。如果你正在運行複雜而要求很高的演出，我們建議使用你預算內最好的電腦。

#### **Liberation 可以控制多少部激光？**

Liberation 可以在一部電腦上運行多部激光，並已使用超過 100 個激光控制器測試。因此答案取決於：

* 你的電腦 CPU
* 網絡速度
* 你的訂閱類型

#### **我可以使用哪些 MIDI 控制器？**

Liberation 是圍繞常見的 APC40 Mk2 MIDI 控制器設計及優化的。它亦支援 APC40 Mk1。請參閱[使用 APC40 進行現場控制](midi-control/live-control-with-the-apc40.md)

我們會逐步加入更多 MIDI 控制器，目前亦支援 APC Mini Mk2 及 MIDI Fighter Twister。

另外亦有 MIDI Send/Receive 系統，可提供額外 MIDI 控制。請參閱 [MIDI Send/Receive](midi-control/midi-send-receive.md)

如需更多資料，請參閱 [MIDI 控制](midi-control/)。

#### **我可以使用任何 MIDI 控制器嗎？**

我們目前正在開發可配置的 MIDI 系統，將來會支援這項功能。在此之前，有些用戶成功使用 MIDI interpreter，將任何 MIDI 訊息轉換給 MIDI Send/Receive 系統使用，但這是一個較繁瑣且進階的流程。你可以在[討論區](https://forum.liberationlaser.com)搜尋相關設定建議；不過實際上 APC40 仍然是最佳選擇。

## 激光控制器

#### **哪些激光控制器兼容 Liberation？**

* [Ether Dream（建議使用）](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system)（你可能需要更新 firmware）
* LaserCube USB（及 LaserDock）
* LaserCube network protocol（使用有線連接）
* [LASollinger lasers](https://laseranimation.com/en/) 使用的 AVB（目前只在 macOS 測試中）

如需更多資料，請參閱[兼容的激光及控制器（DAC）](hardware/compatible-lasers-and-controllers-dacs.md)

#### **為甚麼不支援 \[其他品牌的] 激光控制器？**

為了促進軟件與硬件之間更高的互通性，Liberation 只會支援已公開通訊協定的 DAC。我相信這是激光行業最好的發展方向。

#### **如何判斷我的激光能否與 Liberation 一起使用？**

如果你的激光具備以下其中一項，就可以與 Liberation 一起使用：

* 外置 **ILDA input** — 25-pin D connector，配合兼容的外置控制器使用。
* 內置 **Ether Dream**。
* 任何 **LaserCube**（USB 及 Wi-Fi LaserCube 均可使用）。
* **內置 Mercury 系統的 X-Laser 裝置**（使用 Ether Dream mode）。
* **內置 AVB 的 LaserAnimation Sollinger 投影機**（只限 macOS，需要 AVB 兼容的網絡裝置，目前測試中）。

如需更多資料，請參閱[兼容的激光及控制器（DAC）](hardware/compatible-lasers-and-controllers-dacs.md)

#### **我可以將 Liberation 與 LaserCube 一起使用嗎？**

可以，Liberation 可直接配合任何 LaserCube 使用。請參閱 [LaserCube](hardware/lasercube.md)

## 授權

#### **授權的價格是多少？**

請查看[商店](https://liberationlaser.com/shop)頁面以取得目前價格。

#### **不同授權級別之間有甚麼限制？**

請查看[商店](https://liberationlaser.com/shop)頁面以了解目前的授權選項。

請注意，在**每個**級別（包括免費級別）中，你都可以設定、預覽及設計包含任意數量激光的演出。除了可以 _arm_ 的激光數量外，沒有其他任何限制。所有其他 Liberation 功能均開放給所有用戶。

#### **我可以升級到新的級別嗎？**

你可以隨時升級到較高級別。你目前授權剩餘時間會獲得部分退款，而新方案會立即生效。請參閱[升級或降級你的授權](installation/upgrade-downgrade-your-license.md)

#### **我可以降級我的授權嗎？**

你可以隨時降級，但變更會在目前授權期結束時生效。請參閱[升級或降級你的授權](installation/upgrade-downgrade-your-license.md)

#### **如何使用我的授權為電腦授權？**

購買授權後，你可以在 Liberation 軟件內為電腦授權。你會在 _About_ 畫面看到 _Authorise_ 按鈕，按下後會提示你登入網站。按照畫面上的指示完成授權流程。請參閱[授權及取消授權](installation/authorising-and-de-authorising.md)

#### **我的電腦需要多久連接一次互聯網？**

每次授權續期時，你都需要將 Liberation 連接到互聯網，以更新其內部授權。若使用每月循環付款，你需要每月連接一次。

#### **如果續期後電腦無法連接互聯網，會發生甚麼事？**

Liberation 會在你的授權續期後提供 7 天寬限期，讓你連接互聯網並更新其內部授權。超過該期限後，Liberation 會返回 _Free_ 模式。

#### **如果我的信用卡到期，會發生甚麼事？**

你會收到我們付款服務供應商發出的電郵通知，並需要更新付款資料。登入網站，然後在 subscriptions 頁面使用 _Update payment details_ 連結。

#### **如何取消我的循環授權？**

登入網站，開啟 _Your subscriptions_ 頁面，選擇你想取消的訂閱，然後按 _Cancel Subscription_ 連結。你仍可在授權期餘下時間繼續使用 Liberation。

#### **我可以在多少部電腦上安裝 Liberation？**

你可以在任意數量的電腦上安裝 Liberation。只有啟用激光／DMX output 時才需要授權，而你的授權級別會決定可同時獲授權作 output 的電腦數量。請參閱[授權機制如何運作](installation/how-licensing-works.md)

#### **如何將我的授權由一部電腦移到另一部電腦？**

* 在你不再想使用的電腦上開啟 Liberation
* 確保已連接互聯網，然後在 _About_ 畫面按 _De-authorise this computer_ 按鈕
* 現在在新電腦上開啟 Liberation
* 在 _About_ 畫面按 _Authorise this computer_ 按鈕。
* 網站會開啟，登入並按照畫面上的指示完成授權

你亦可以遠端取消授權一部已無法存取的電腦（有部分限制）。請參閱[授權及取消授權](installation/authorising-and-de-authorising.md)

#### **如果電腦遺失或被盜，我可以取消該電腦上的 Liberation 授權嗎？**

你可以透過網站取消該電腦的授權。如果該 Liberation 安裝在你上次續期後未曾上線，便可以立即完成。

否則，取消授權會在訂閱續期時或該電腦連接互聯網時生效，以較早發生者為準。如果你急需重新授權新電腦，請聯絡支援。

### 使用 Liberation

#### 預設設定有 8 部激光 — 如何更改？

請參閱[設定你的專案](setting-up/setting-up-your-project.md)及[新增／移除激光](setting-up/adding-removing-lasers.md)

#### 可以將一部激光的 Zone 設定複製到其他激光嗎？

可以！請參閱[在激光之間複製 Zone](output-view/copy-zones-between-lasers.md)

#### 可以直接輸入數字，而不是使用 slider 嗎？

可以。`Cmd / Ctrl`-click slider，然後你就可以使用鍵盤輸入數值。

#### **如何將 Liberation 與音樂同步？**

它有一個智能的「tap tempo」系統，運作方式如你所預期；你亦可以使用外部 MIDI clock 或 Ableton Link。請參閱 [Tempo 同步](tempo-synchronisation.md)。Timeline 可同步至經由任何 audio interface 輸入的 LTC/SMPTE timecode。請參閱 [Timecode](timecode.md)。

#### 要獲得最佳激光 output，需要調整哪些設定？

主要設定是 _Colour Shift_，用來補償 mirrors 移動與激光亮度變化之間的輕微延遲。如果你的激光點／光束出現細小的「拖尾」，就需要調整這項設定。（請參閱[激光設定](setting-up/laser-settings.md)頁面的相片，查看「拖尾」示例）

你亦可以嘗試更改 scanner speed；如果你的 scanners 較基本，可調慢一點；如果質素較好，可調快一點。但**請小心使用，因為如果驅動過度，可能會損壞 scanners。**

另外亦有一些預設 scanner settings。預設選項較保守，適合大部分激光光束需求。如果你有較好的 scanners，亦有其他 presets 可用，並且有針對 graphics 調校的 presets。

如需更多資料，請參閱[激光設定](setting-up/laser-settings.md)；如需了解如何建立自己的 presets，請參閱[掃描器預設](advanced/scanner-presets.md)（進階，編寫中）

你亦可以使用 _Colour calibration_ 設定修正色彩平衡。請參閱[顏色校準](advanced/colour-calibration.md)（進階技巧）

#### _Latency(ms)_ 設定有甚麼作用？

這是 frame latency，即由 frame 產生到隨後送往激光之間的最長時間。你一般不需要調整它，但如果遇到網絡問題，可以嘗試增加此值。詳情請參閱[延遲設定](setting-up/latency-setting.md)。

### Clips

#### 如何在不運行 Clip 的情況下調整它的 Zone 和設定？

`Alt / Option`-click，將它設為 _currently selected clip_，但不啟動它。另請參閱[啟動及停止 Clip](clips/starting-stopping-clips.md)

#### 如何複製 Clips？

按住 `Alt / Option` 鍵時 click 並拖曳。另請參閱[整理你的 Clip Deck](clips/organising-your-clip-deck.md)

#### 如何刪除 Clips？

Click 並將它們拖離 clip deck。另請參閱[整理你的 Clip Deck](clips/organising-your-clip-deck.md)

#### 如何多選、刪除、合併 Clip Deck 等？

請參閱[整理你的 Clip Deck](clips/organising-your-clip-deck.md)

#### Clip 上的小咪高峰符號和其他圖示代表甚麼？

它們用來表示該 Clip 會接收聲音或 MIDI input，而三點圖示表示有 Zone delay。請參閱 [Clip 按鈕上的小圖示是甚麼](clips/what-are-the-small-icons-on-the-clip-buttons.md)
