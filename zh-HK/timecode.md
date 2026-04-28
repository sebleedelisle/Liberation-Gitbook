---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ 時間碼

Liberation 支援與外部 SMPTE/LTC 時間碼訊號同步；這類訊號常用於現場音樂演出，讓燈光、煙火特效、影片和伴奏軌保持同步。

{% hint style="info" %}
甚麼是 SMPTE/LTC？

SMPTE 是一種時間碼標準，而 LTC 則是將這種時間碼轉換成音訊訊號。如果你聽這段音訊，會聽到很刺耳的高頻尖叫聲；但對電腦來說，它是高解像度的計時資訊。

**冷知識！**

以往 SMPTE 常用來讓影片和音訊同步；如果要同步到類比磁帶，會把時間碼音訊錄到其中一條軌上，這有時稱為為磁帶「striping」。你可以用這條時間碼軌，讓多部磁帶機互相同步，或讓 MIDI sequencer 跟磁帶同步。（這樣你就不用把 MIDI 樂器錄到磁帶上，可以在混音時直接由 sequencer 即時播放！）

SMPTE 代表 Society of Motion Picture and Television Engineers，即制定此標準的組織。LTC 代表 _Linear TimeCode_。
{% endhint %}

你可以透過電腦上的任何音訊介面接收 LTC 時間碼訊號，但建議使用專業音訊介面，至少要有一個可調校的 XLR input，並具備監聽功能。

我使用 [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) 的經驗不錯，因為它有耳機監聽、2 個 XLR input，而且不需要任何特別 driver（至少在 macOS 上是這樣）。如果你只會用它來接收時間碼，可以選擇稍為便宜一點的 [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html)（它只有一個 input，而且沒有 MIDI），但老實說，任何質素不錯的音訊介面都應該可以使用。

{% hint style="info" %}
LTC 時間碼訊號通常會透過平衡 XLR 線材分配，因為這類線材足夠可靠，可以把低電平音訊訊號傳送到較遠距離。（XLR 是通常用於咪高峰的圓筒式接頭）
{% endhint %}

### 硬件連接

將時間碼訊號的 XLR 線插入音訊介面，並確認你收到良好訊號。調整音訊介面上的音量，直到訊號夠強但沒有 clipping。如果你的音訊介面有耳機插孔，可以聆聽時間碼，確認它沒有斷續或異常，也沒有太多噪音。

{% hint style="info" %}
理論上，你可以透過 MacBook 上的 jack socket 接收訊號，但這需要自製線材。這些插孔通常是 4 極 TRRS mini jack，老實說我不太確定當中哪些接點可用作音訊輸入，也不確定它可承受的電壓水平（我曾經讀過是 +/-1V，但請自行承擔風險！）

我認為與其嘗試這樣做，不如直接買一個便宜的 USB 音訊介面會更好。
{% endhint %}

如果你的音訊介面沒有任何輸入監聽功能，可以到 macOS 系統設定（在 _Sound_ 下）檢查是否收到訊號。（在 Windows，請使用 _Sound Control Panel_）。

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS 會在 Sound 系統設定面板中顯示任何音訊介面的輸入電平</p></figcaption></figure>

### 在 Liberation 中設定

1. 在 Timecode settings Window 中，選擇你的音訊介面和正確的 input channel。

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
請注意，下拉式選單中會為音訊介面的每個 input channel 提供獨立選項

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

留意左邊的方格：如果收到有效的時間碼訊號，它會變成綠色；否則會是紅色。

2. 選擇傳入時間碼的正確幀率。提供時間碼的人應該可以告訴你幀率是多少。（如果設定錯誤，它仍然會同步，但你會注意到每秒有一下輕微「跳動」）
3. 使用 timeline bar 上的小時鐘圖示開啟 Timeline 的時間碼設定，然後選擇 SMPTE(LTC) 選項。

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. 調整 start offset（以小時、分鐘、秒、幀為單位），使它配合歌曲的開始時間。如果你有多個 timeline，需要為每個 timeline 分別設定這些選項。

{% hint style="info" %}
在巡演製作中，一個常見慣例是讓每首歌由不同的小時開始，例如第一首歌為 01:00:00:00，第二首歌為 02:00:00:00，如此類推。

Liberation 會根據時間碼自動切換到相應的 timeline，所以演出期間你不需要手動切換 timeline。
{% endhint %}

請注意，與 MIDI Clock 和 Ableton Link 不同，SMPTE 是一套以小時、分鐘、秒和幀計算的_絕對_時間系統。Liberation 的核心時間系統以拍子和小節為基礎，所以當你接收時間碼時，它會使用 timeline 中設定的 tempo。你需要確認這個 tempo 與任何同樣同步到時間碼的音樂保持同步。
