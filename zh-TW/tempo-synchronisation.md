---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / 同步

音樂同步是 Liberation 的基本要素；只要 Tempo 和拍點與音樂對齊，就能確保所有內容保持同步。如果你剛好可以取得 MIDI clock（或 Ableton Link），就完全不需要擔心手動同步。不過如果沒有也不用擔心，你可以使用 _Live_ Tempo 功能手動對齊。

如果你有音樂或燈光軟體的使用經驗，這個流程應該會很熟悉。如果沒有，建議在正式演出前花點時間熟悉系統，並在家多練習。

## Tempo 面板

_Tempo_ 面板會一直顯示在畫面上，裡面包含所有同步設定。上方會顯示目前的小節 / 拍計數器，以及包含播放 / 暫停、倒轉 / 快轉按鈕的播放控制。

下方會看到 beat marker：四個會隨拍點「脈動」的方塊。這個 _beat marker_ 是非常實用的視覺指示；使用 _Live_ Tempo 系統時，你會經常參考它。

### 設定 Tempo

你可以用以下方式設定 Tempo：

* 在 _Tempo_ 滑桿上按住並拖曳
* Shift-click 並拖曳 _Tempo_ 滑桿，以 0.1 為單位調整 Tempo
* 在 _Tempo_ 滑桿上按兩下，手動輸入數值
* 使用 APC40 上的 _Tempo_ 旋鈕（按住 shift 可用 0.1 為單位調整）
* Tap Tempo

{% hint style="info" %}
Tempo 以「每分鐘拍數」（beats per minute）定義，傳統預設值通常是 120。
{% endhint %}

## Tap Tempo

配合拍點點擊 _TAP_ 按鈕，即可自動設定 Tempo。使用 _RESET_ 按鈕設定小節開頭。

{% hint style="info" %}
Tap Tempo 系統很聰明，能判斷你是否暫停敲擊了一段時間，或是否漏掉了幾拍。如果你開始用 double time 敲擊，它會理解你想把 Tempo 加倍；如果你用 half time 敲擊，也同樣能判斷。

它也能判斷是否有兩個人同時在敲 Tap Tempo（例如一個人在鍵盤上，另一個人在 APC40 上）。Liberation 會將重複敲擊取平均。
{% endhint %}

#### 鍵盤指令：

T - tap tempo\
R - 重設小節\
Y - 將 Tempo 四捨五入到最接近的每分鐘拍數。

{% hint style="info" %}
現在大多數音樂都是數位製作，因此 Tempo 通常會是四捨五入後的整數。如果 tap 出來的 Tempo 看起來已經接近，可使用 Y 鍵（或將 APC40 Tempo 旋鈕轉動一「格」）將它整理成整數。
{% endhint %}

#### APC40 控制：

APC40 有專用的 _TAP TEMPO_ 按鈕，你也可以使用已連接的腳踏開關，用腳來 tap！

使用 _TEMPO_ 旋鈕進行調整。使用 _TEMPO_ 旋鈕時按住 _SHIFT_ 可進行細部調整。

使用 _METRONOME_ 按鈕來**重設小節**。（請注意，_METRONOME_ 按鈕也會隨拍點亮起）

將 _TEMPO_ 旋鈕向右或向左轉動一「格」，可將 **Tempo 四捨五入**到整數 BPM。

另請參閱 [APC40 參考資料](reference/apc40-reference.md)

### 微調 Tempo

如果你確定已經很接近實際 Tempo，但發現仍逐漸偏離拍點，可以使用 _NUDGE_ 按鈕修正。

如果 Liberation 的 Tempo 跑在音樂前面，按住 _NUDGE -_ 暫時放慢，直到重新對齊。

如果 Liberation 的 Tempo 落在音樂後面，按住 _NUDGE +_ 暫時加快，直到重新對齊。

{% hint style="info" %}
你可以使用畫面上的 NUDGE 按鈕，也可以使用 APC40 上的專用按鈕。
{% endhint %}

### 半速 / 倍速

使用 _÷2_ 和 _x2_ 按鈕可永久將 Tempo 減半或加倍。這與 Tempo Multiplier 不同，是對目前 Tempo 的永久變更。

## Tempo Multiplier

_Tempo Multiplier_ 系統可讓你暫時調整 Tempo，之後再回到原本的 Tempo。

按下 _TEMPO MULTIPLIER_ 按鈕或 APC40 上的 _BANK_ 按鈕，即可切換 _Tempo Multiplier_。可使用畫面上的滑桿調整，或使用 APC40 A-B 滑桿調整。也可以使用 _25%, 50%, 100% 200%_ 預設按鈕。

## 外部 Tempo 來源

### MIDI Clock

若要同步到外部 MIDI clock 訊號，請選取 _MIDI CLOCK_ 單選按鈕，並從下拉選單選擇 MIDI 裝置。請注意下拉選單旁的彩色狀態燈：

* 綠色 - 正在接收 MIDI clock 訊號
* 橘色 - 可以連線到 MIDI 裝置，但目前沒有 clock 訊號
* 紅色 - 無法連線到 MIDI 裝置

{% hint style="info" %}
MIDI Clock 會廣播一連串 frame（每個四分音符 24 個），但訊息中沒有位置資料。這表示它有助於維持拍點同步，但你可能仍需要重設小節。

Liberation 的 MIDI Clock Tempo 來源也會回應 **MIDI Machine Control (MMC)** 訊息，因此如果你的 clock 來源會傳送這些訊息，就不需要手動重設小節。
{% endhint %}



### Timeline

每個 timeline 都有自己的 Tempo，可以是固定值，也可以是 _Tempo Map_。_Tempo Map_ 可讓你在 timeline 中的特定時間點調整 Tempo。

當 Tempo 來源選取為 _TIMELINE_ 時，會使用 timeline 的 Tempo。

{% hint style="info" %}
你可以讓 timeline 搭配_任何_ Tempo 來源一起執行！所以如果你有一個不跟 click 演奏的現場樂團，可以手動啟動 timeline，並使用 _LIVE_ Tempo 來源讓它保持同步。或者如果你有 MIDI clock 訊號，也可以使用它！
{% endhint %}
