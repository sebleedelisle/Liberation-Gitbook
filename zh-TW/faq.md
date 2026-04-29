---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ 常見問題

## 硬體

#### **Liberation 可以在 Windows 上執行嗎？**

可以。Liberation 完整支援 **Windows 10 和 11（64-bit）**，功能與 Mac 版本完全相同。每個版本都會同時在兩個平台發布。

#### **Liberation 可以在 Mac 上執行嗎？**

可以。Liberation 完整支援 **Mac（macOS 12 Monterey 及更新版本）**，功能與 Windows 版本完全一致。所有更新都會同步發布。

#### **最低需要什麼規格的電腦？**

這取決於你想控制多少台雷射。如果只控制少量雷射，低規格電腦也可以。任何 Apple Silicon Mac 的執行效果都很好，應該可以控制多達 100 台雷射。如果你要執行複雜且要求很高的演出，我們建議使用你能力範圍內最好的電腦。

#### **Liberation 可以控制多少台雷射？**

Liberation 可以在一台電腦上執行多台雷射；我們已測試超過 100 個 laser controller，因此答案取決於：

* 你的電腦 CPU
* 網路速度
* 你的訂閱類型

#### **我可以使用哪些 MIDI controllers？**

Liberation 是以常見的 APC40 Mk2 MIDI controller 為核心設計並最佳化，也可搭配 APC40 Mk1 使用。請參閱[使用 APC40 進行現場控制](midi-control/live-control-with-the-apc40.md)

我們也正在逐步加入更多 MIDI controllers，目前也支援 APC Mini Mk2 和 MIDI Fighter Twister。

另外還有 MIDI Send/Receive 系統，可提供額外的 MIDI 控制。請參閱 [MIDI Send/Receive](midi-control/midi-send-receive.md)

更多資訊請參閱 [MIDI 控制](midi-control/)。

#### **我可以使用任何 MIDI controller 嗎？**

我們目前正在開發可設定的 MIDI 系統，未來會支援這種用法。在此之前，有些使用者透過 MIDI 轉譯器，將任意 MIDI 訊息轉換給 MIDI Send/Receive 系統使用，也取得了一些成果；但這是相當繁瑣且進階的流程。你可以在[論壇](https://forum.liberationlaser.com)搜尋相關設定建議，不過實際上 APC40 仍是最佳選擇。

## Laser controllers

#### **哪些 laser controllers 與 Liberation 相容？**

* [Ether Dream（建議使用）](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system)（你可能需要更新韌體）
* LaserCube USB（以及 LaserDock）
* LaserCube 網路通訊協定（需使用有線連線）
* [LASollinger 雷射設備](https://laseranimation.com/en/)所使用的 AVB（目前僅限 macOS，測試中）

更多資訊請參閱[相容的雷射與 controllers / DACs](hardware/compatible-lasers-and-controllers-dacs.md)

#### **為什麼不支援［其他品牌的］laser controller？**

為了促進軟體與硬體之間更好的互通性，Liberation 只會支援已公開通訊協定的 DAC。我相信這是雷射產業最好的前進方向。

#### **我如何確認我的雷射是否可搭配 Liberation 使用？**

如果你的雷射具備以下其中一項，就可以搭配 Liberation 使用：

* 外部 **ILDA 輸入**：25-pin D 接頭，可搭配相容的外部 controller 使用。
* 內建安裝的 **Ether Dream**。
* 任何 **LaserCube**（支援 USB 與 Wi-Fi LaserCube）。
* **內建 Mercury 系統的 X-Laser 設備**（以 Ether Dream 模式）。
* **內建 AVB 的 LaserAnimation Sollinger 雷射投影機**（僅限 macOS，需要 AVB 相容的網路裝置，目前測試中）。

更多資訊請參閱[相容的雷射與 controllers / DACs](hardware/compatible-lasers-and-controllers-dacs.md)

#### **我可以將 Liberation 搭配我的 LaserCube 使用嗎？**

可以，Liberation 可直接搭配任何 LaserCube 使用。請參閱 [LaserCube](hardware/lasercube.md)

## 授權

#### **授權價格是多少？**

請參閱 [shop](https://liberationlaser.com/shop) 頁面取得目前價格。

#### **不同授權等級有哪些限制？**

請參閱 [shop](https://liberationlaser.com/shop) 頁面取得目前授權選項。

請注意，**每個**等級（包含免費等級）都可以設定、預覽並設計任意數量雷射的演出；除了可 _arm_ 的雷射數量以外，沒有其他限制。所有其他 Liberation 功能都對所有使用者開放。

#### **我可以升級到新的等級嗎？**

你可以隨時升級到更高等級。系統會依照目前授權剩餘時間提供部分退款，新的方案會立即開始。請參閱[升級或降級你的授權](installation/upgrade-downgrade-your-license.md)

#### **我可以降級我的授權嗎？**

你可以隨時降級，但變更會在目前授權期間結束後生效。請參閱[升級或降級你的授權](installation/upgrade-downgrade-your-license.md)

#### **我要如何用授權啟用我的電腦？**

購買授權後，你可以在 Liberation 軟體內授權這台電腦。在 _About_ 畫面上會看到 _Authorise_ 按鈕，按下後會提示你登入網站。依照畫面上的指示完成授權流程。請參閱[授權與取消授權](installation/authorising-and-de-authorising.md)

#### **我的電腦多久需要連線到網際網路一次？**

每次授權續訂時，你都需要讓 Liberation 連線到網際網路，以更新其內部授權。如果是每月循環付款，你就需要每個月連線一次。

#### **如果續訂後我的電腦無法連線到網際網路，會發生什麼事？**

授權續訂後，Liberation 會提供 7 天寬限期，讓你連線到網際網路並更新內部授權。超過這段時間後，Liberation 會回到 _Free_ 模式。

#### **如果我的信用卡過期會怎麼樣？**

你會收到我們付款服務供應商寄出的電子郵件通知，並需要更新付款方式。登入網站後，在訂閱頁面使用 _Update payment details_ 連結。

#### **我要如何取消循環授權？**

登入網站，開啟 _Your subscriptions_ 頁面，選取你要取消的訂閱，然後點擊 _Cancel Subscription_ 連結。你仍可在授權期間剩餘時間內繼續使用 Liberation。

#### **我可以在幾台電腦上安裝 Liberation？**

你可以在任意數量的電腦上安裝 Liberation。只有在啟用雷射 / DMX 輸出時才需要授權；你的授權等級會決定同一時間可授權輸出的電腦數量。請參閱[授權機制如何運作](installation/how-licensing-works.md)

#### **我要如何將授權從一台電腦移到另一台電腦？**

* 在你不再使用的那台電腦上開啟 Liberation
* 確認已連線到網際網路，並在 _About_ 畫面點擊 _De-authorise this computer_ 按鈕
* 接著在新的電腦上開啟 Liberation
* 在 _About_ 畫面點擊 _Authorise this computer_ 按鈕。
* 網站會開啟；登入後依照畫面上的指示完成授權

你也可以遠端取消授權一台已無法存取的電腦（有部分限制）。請參閱[授權與取消授權](installation/authorising-and-de-authorising.md)

#### **如果電腦遺失或被竊，我可以取消該電腦上的 Liberation 授權嗎？**

你可以透過網站取消該電腦的授權。如果該 Liberation 安裝在你上次續訂後未曾上線，就可以立即完成。

如果不是，取消授權會在訂閱續訂時，或該電腦連線到網際網路時生效，以較早發生者為準。如果你急需重新授權一台新電腦，請聯絡支援團隊。

### 使用 Liberation

#### 預設設定有 8 台雷射，我要如何變更？

請參閱[設定你的專案](setting-up/setting-up-your-project.md)和[新增與移除雷射](setting-up/adding-removing-lasers.md)

#### 我可以把一台雷射的 zone 設定複製到其他雷射嗎？

可以！請參閱[在雷射之間複製 zones](output-view/copy-zones-between-lasers.md)

#### 我可以輸入數字，而不是使用滑桿嗎？

可以。按住 `Cmd / Ctrl` 並點擊滑桿，就可以用鍵盤輸入數值。

#### **我要如何讓 Liberation 與音樂同步？**

它具備智慧型「tap tempo」系統，用法如你預期；你也可以使用外部 MIDI clock 或 Ableton Link。請參閱[節拍同步](tempo-synchronisation.md)。Timeline 可與透過任何音訊介面輸入的 LTC/SMPTE timecode 同步。請參閱 [Timecode（時間碼）](timecode.md)。

#### 我需要調整哪些設定，才能讓雷射輸出達到最佳效果？

主要設定是 _Colour Shift_，它會補償掃描鏡移動與雷射亮度變化之間的輕微延遲。如果你的雷射點或光束有一點「尾巴」，就需要調整這個設定。（請參閱 [Laser Settings](setting-up/laser-settings.md)頁面上的照片，了解「尾巴」的範例）

你也可以嘗試變更掃描器速度。如果你的掃描器較基本，就調慢一點；如果品質較好，可以調快一點。但**請謹慎使用，因為過度驅動可能會損壞掃描器。**

另外也有一些預設掃描器設定。預設選項較保守，適用於大多數雷射光束需求。如果你有更好的掃描器，也可以使用其他 preset；也有針對圖形調校的 preset。

更多資訊請參閱 [Laser Settings](setting-up/laser-settings.md)；若要了解如何建立自己的 preset，請參閱[掃描器 presets](advanced/scanner-presets.md)（進階，撰寫中）

你也可以使用 _Colour calibration_ 設定修正色彩平衡。請參閱[色彩校正](advanced/colour-calibration.md)（進階技巧）

#### _Latency(ms)_ 設定的作用是什麼？

這是影格延遲，也就是從產生影格到隨後送到雷射之間的最大時間。通常不需要調整，但如果遇到網路問題，可以嘗試增加此數值。更多細節請參閱[延遲設定](setting-up/latency-setting.md)。

### Clips

#### 不執行 Clip 時，要如何調整它的 zones 和設定？

按住 `Alt / Option` 並點擊，可讓它成為目前選取的 Clip，但不啟動它。另請參閱[啟動與停止 Clips](clips/starting-stopping-clips.md)

#### 我要如何複製 Clips？

按住 `Alt / Option` 鍵並點擊拖曳。另請參閱[整理你的 Clip Deck](clips/organising-your-clip-deck.md)

#### 我要如何刪除 Clips？

點擊並把它們拖出 Clip Deck。另請參閱[整理你的 Clip Deck](clips/organising-your-clip-deck.md)

#### 我要如何多選、刪除、合併 Clip Deck 等？

請參閱[整理你的 Clip Deck](clips/organising-your-clip-deck.md)

#### Clip 上的小麥克風符號和其他圖示代表什麼？

它們用來表示該 Clip 會接收聲音或 MIDI 輸入；3 個點則表示有 zone delay。請參閱 [Clip 按鈕上的小圖示是什麼？](clips/what-are-the-small-icons-on-the-clip-buttons.md)
