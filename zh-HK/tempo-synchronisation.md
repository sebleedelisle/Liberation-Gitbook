---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / 同步

音樂同步是 Liberation 的基本元素；當 Tempo 和拍子對準音樂後，你就可以確保所有內容保持同步。如果你有 MIDI clock（或 Ableton Link），就完全不用擔心手動同步。不過如果沒有也不用擔心——你可以使用 _Live_ tempo 功能手動對拍。

如果你有使用音樂或燈光軟件的經驗，這個流程應該會很熟悉。如果沒有，建議在正式演出前花點時間熟習系統，並在家中練習。

## Tempo panel

_Tempo_ panel 會一直顯示在畫面上，並包含所有同步設定。頂部會顯示目前的小節/拍子計數器，以及帶有播放/暫停和倒帶/快轉按鈕的 transport。

下方會顯示 beat marker；四個會隨拍子「跳動」的方格。這個 _beat marker_ 是非常有用的視覺提示；使用 _Live_ tempo 系統時，你會經常參考它。

### 設定 Tempo

你可以用以下方式設定 Tempo：

* 在 _Tempo_ slider 上按住並拖曳
* Shift-click 並在 _Tempo_ slider 上拖曳，以 0.1 為增量調整 Tempo
* Double click _Tempo_ slider，然後手動輸入數值
* 使用 APC40 上的 _Tempo_ knob（按住 shift 可作 0.1 增量調整）
* Tap Tempo

{% hint style="info" %}
Tempo 以「每分鐘拍數」（beats per minute）定義，傳統預設通常是 120。
{% endhint %}

## Tap Tempo

按音樂拍子點擊 _TAP_ button，即可自動設定 Tempo。使用 _RESET_ button 設定小節起點。

{% hint style="info" %}
Tap Tempo 系統足夠聰明，可以判斷你是否暫停點按了一段時間，或是否漏掉了幾拍。如果你開始以雙倍速度點按，它會理解你想把 Tempo 加倍；如果你以半速點按，亦同樣會理解。

它亦能判斷是否有兩個人同時在 tap tempo（例如一個用鍵盤、另一個用 APC40）。Liberation 會將重複點按平均處理。
{% endhint %}

#### 鍵盤指令：

T - tap tempo\
R - reset the bar\
Y - 將 Tempo 四捨五入至最接近的每分鐘拍數。

{% hint style="info" %}
現今大部分音樂都是以數碼方式製作，因此 Tempo 很可能是四捨五入後的整數。如果 tap tempo 的結果似乎已很接近，可以使用 Y 鍵（或將 APC40 tempo knob 移動一個「tick」）將它四捨五入至整數。
{% endhint %}

#### APC40 控制：

APC40 有專用的 _TAP TEMPO_ button，你亦可以使用已連接的 footswitch 用腳點按！

使用 _TEMPO_ knob 進行調整。使用 _TEMPO_ knob 時按住 _SHIFT_ 可作精細調整。

使用 _METRONOME_ button **reset the bar**。（請注意，_METRONOME_ button 亦會按拍子亮起）

將 _TEMPO_ knob 向右或向左轉一個「tick」，即可將 Tempo **四捨五入**至上一個或下一個整數 BPM。

另請參閱 [APC40 參考](reference/apc40-reference.md)

### Nudge tempo

如果你確定 Tempo 已經夠接近實際 Tempo，但發現它逐漸走拍，可以使用 _NUDGE_ buttons 修正。

如果 Liberation tempo 比音樂快了，按住 _NUDGE -_ 暫時減慢，直至重新對齊。

如果 Liberation tempo 比音樂慢了，按住 _NUDGE +_ 暫時加快，直至重新對齊。

{% hint style="info" %}
你可以使用畫面上的 NUDGE buttons，或 APC40 上的專用按鈕。
{% endhint %}

### Half time / double time

使用 _÷2_ 和 _x2_ buttons 可永久將 Tempo 減半或加倍。與 Tempo Multiplier 不同，這會永久更改目前 Tempo。

## Tempo Multiplier

_Tempo Multiplier_ 系統可讓你暫時調整 Tempo，之後再回復原本的 Tempo。

按 _TEMPO MULTIPLIER_ button 或 APC40 上的 _BANK_ button，可切換 _Tempo Multiplier_。你可以使用畫面上的 slider 或 APC40 A-B slider 進行調整，亦可使用 _25%, 50%, 100% 200%_ preset buttons。

## 外部 Tempo 來源

### MIDI Clock

要同步至外部 MIDI clock 訊號，請選擇 _MIDI CLOCK_ radio button，並從下拉式選單選擇 MIDI 裝置。請留意下拉式選單旁的彩色狀態燈：

* Green - 正在接收 MIDI clock 訊號
* Orange - 可以連接至 MIDI 裝置，但目前沒有 clock 訊號
* Red - 無法連接至 MIDI 裝置

{% hint style="info" %}
MIDI Clock 會廣播一連串 frame（每個四分音符 24 個），但訊息內沒有位置資料。這表示它有助保持拍子同步，但你可能仍需要 reset the bar。

Liberation MIDI Clock tempo source 亦會回應 **MIDI Machine Control (MMC)** 訊息；因此如果你的 clock source 會傳送這些訊息，你就不需要手動 reset the bar。
{% endhint %}



### Timeline

每個 timeline 都有自己的 Tempo，可以是固定值或 _Tempo Map_。_Tempo Map_ 可讓你在 timeline 內的特定時間調整 Tempo。

當 _TIMELINE_ 被選為 tempo source 時，將會使用 timeline tempo。

{% hint style="info" %}
你可以配合 _任何_ tempo source 運行 timeline！因此，如果你有一隊不跟 click 演奏的 live band，你可以手動啟動 timeline，並使用 _LIVE_ tempo source 保持同步。或者，如果你有 MIDI clock 訊號，也可以使用它！
{% endhint %}
