---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode（時間碼）

Liberation 支援與外部 SMPTE/LTC 時間碼訊號同步。這類訊號常用於現場音樂演出，用來讓燈光、煙火特效、影片和伴奏音軌保持同步。

{% hint style="info" %}
什麼是 SMPTE/LTC？

SMPTE 是一種時間碼標準，而 LTC 是把這種時間碼轉換成音訊訊號。如果你實際聽這段音訊，會像很刺耳的高頻尖叫聲；但對電腦來說，它是高解析度的時間資訊。

**冷知識！**

過去 SMPTE 常用來讓影片和音訊同步；如果是同步到類比磁帶，通常會把時間碼音訊錄在其中一軌上，有時稱為替磁帶「striping」。你可以用這條時間碼軌讓多台錄音座彼此同步，或讓 MIDI sequencer 跟磁帶同步。（這樣你就不需要把 MIDI 樂器錄到磁帶上，可以在混音時讓 sequencer 現場播放！）

SMPTE 是 Society of Motion Picture and Television Engineers（美國電影與電視工程師協會）的縮寫，由他們制定這項標準。LTC 則代表 _Linear TimeCode_。
{% endhint %}

你可以透過電腦上的任何音訊介面接收 LTC 時間碼訊號，但建議使用至少有一個可調整 XLR 輸入、且具備監聽功能的專業音訊介面。

我使用 [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) 的經驗很好，因為它有耳機監聽、2 個 XLR 輸入，而且不需要任何特殊驅動程式（至少在 macOS 上是如此）。如果你只會把它拿來接時間碼，可以選稍微便宜一點的 [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html)（它只有一個輸入且沒有 MIDI），不過老實說，只要是品質還可以的音訊介面應該都能運作。

{% hint style="info" %}
LTC 時間碼訊號通常會透過平衡式 XLR 線材傳送，因為這類線材夠穩定，能把低電平音訊訊號傳送到較遠距離。（XLR 是通常搭配麥克風使用的圓形接頭）
{% endhint %}

### 硬體連接

將時間碼訊號的 XLR 線插入你的音訊介面，並確認收到良好的訊號。調整音訊介面上的音量，直到訊號夠強但沒有削波。如果你的音訊介面有耳機孔，可以聽一下時間碼，確認它沒有中斷或故障，也沒有過多雜訊。

{% hint style="info" %}
理論上，你可以透過 MacBook 上的音訊插孔接收訊號，但這需要自製線材。這些插孔通常是 4 極 TRRS 迷你插孔，而我老實說不確定其中哪些接點可以用作音訊輸入，也不確定它能承受的電壓範圍（我在某處看過是 +/-1V，但請自行承擔風險！）

我認為與其嘗試這種方式，不如直接準備一個便宜的 USB 音訊介面會更好。
{% endhint %}

如果你的音訊介面沒有任何輸入監聽功能，可以到 macOS 系統設定（在 _Sound_ 底下）確認是否有收到訊號。（在 Windows 上，請使用 _Sound Control Panel_）。

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS 會在 Sound 系統設定面板中顯示任何音訊介面的輸入音量</p></figcaption></figure>

### 在 Liberation 中設定

1. 在 Timecode settings Window 中選擇你的音訊介面和正確的輸入聲道。

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
請注意，下拉式選單中會針對音訊介面的每個輸入聲道提供個別選項。

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

注意左側的方塊：如果收到有效的時間碼訊號，它會變成綠色；如果沒有，則會是紅色。

2. 選擇傳入時間碼的正確影格率。提供時間碼給你的人應該能告訴你影格率是多少。（如果選錯，它仍然會同步，但你會注意到每秒有一點「跳動」）
3. 使用 timeline bar 上的小時鐘圖示開啟 Timeline 的 timecode settings，並選擇 SMPTE(LTC) 選項。

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. 調整 start offset（以小時、分鐘、秒、影格為單位），使其符合歌曲開始的位置。如果你有多個 timeline，需要分別為每一個設定這些選項。

{% hint style="info" %}
在巡演領域中，常見慣例是讓每首歌從不同的小時開始，例如第一首歌是 01:00:00:00，第二首歌是 02:00:00:00，以此類推。

Liberation 會依據時間碼自動切換到對應的 timeline，因此演出期間你不需要手動切換 timeline。
{% endhint %}

請注意，SMPTE 與 MIDI Clock 和 Ableton Link 不同，它是以小時、分鐘、秒和影格計算的_絕對_時間系統。Liberation 的核心時間系統是以拍和小節為基礎，因此收到時間碼時，它會使用 timeline 中設定的 tempo。你需要確保這個 tempo 與同樣同步到時間碼的音樂保持一致。
