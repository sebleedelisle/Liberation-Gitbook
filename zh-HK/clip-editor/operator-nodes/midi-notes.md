---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI 音符

## MIDI 音符

建立「激光豎琴」風格的效果，讓輸入的 MIDI 音符在一個範圍內觸發光束或圖形。此 node 會使用你傳入的任何內容作為每個音符的 _來源_：輸入一個點，就會得到一排點；輸入圓形之類的圖形，就會得到一排圓形；更複雜的圖形亦會以同樣方式複製。

你可以在 **Liberation → Settings** (`Cmd / Ctrl + ,`) 選擇 Liberation 要監聽的 MIDI 介面。

* **midi channel** – 要監聽的 MIDI channel（0 = 所有 channel，1–16 = 指定 channel）
* **width** – 音符分佈的總寬度。
* **midi note min / max** – 範圍內最低及最高的 MIDI note 數值。
* **ignore out of range notes** – 過濾超出設定範圍的任何音符。如停用，超出範圍的音符會被「夾」到最接近的可用音符（高音會觸發範圍頂端，低音會觸發範圍底端）。
* **auto extend range** – 如播放的音符超出範圍，會自動擴闊範圍。

{% hint style="info" %}
不確定收到的是哪個音符範圍？開啟 **auto extend range**，將 **midi note min** 設得很高，並將 **midi note max** 設得很低，然後逐一播放你的音符。系統會捕捉所有音符並為你擴展範圍。全部捕捉完成後，只需關閉 **auto extend range** 即可鎖定範圍。
{% endhint %}

* **leave all notes visible** – 無論音符是否正在播放，都會為範圍內所有音符建立光束或圖形，形成「激光豎琴」效果。
* **hit colour** – 音符被觸發時顯示的顏色。
* **hit colour hold time** – hit colour 在淡出前保持全亮的時間。數值以秒為單位（0–1）。_100% = 1 秒。_
* **hit colour decay time** – hold time 之後，hit colour 淡回原狀所需的時間。數值以秒為單位（0–1）。_100% = 1 秒。_

{% hint style="info" %}
如果你的內容本身已經是純白色，將 hit colour 設為白色不會有任何分別。為取得最佳效果，建議將內容設為飽和顏色，並將 hit colour 設為白色；這樣在音符被觸發時會產生很好的閃光效果。
{% endhint %}

* **note off fade out time** – 音符釋放後淡出所需的時間。數值以秒為單位（0–1）。_100% = 1 秒。_
* **hit scale factor** – 音符被觸發時放大的程度（例如 2 = 兩倍大小）。
* **hit scale hold time** – 音符在縮回前保持放大的時間。數值以秒為單位（0–1）。_100% = 1 秒。_
* **hit scale decay time** – 音符回復原本大小所需的時間。數值以秒為單位（0–1）。_100% = 1 秒。_
* **note off shrink time** – 音符釋放後縮回原本大小所需的時間。數值以秒為單位（0–1）。_100% = 1 秒。_（啟用 **leave all notes visible** 時沒有作用。）

{% hint style="info" %}
縮放：請注意，如果你的內容只是一個單點，縮放不會有任何效果！
{% endhint %}
