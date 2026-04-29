---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

建立「雷射豎琴」風格的效果，讓輸入的 MIDI notes 在一個範圍內觸發光束或圖形。這個 node 會使用你傳入的任何內容作為每個 note 的_來源_：輸入一個點，就會得到一排點；輸入像圓形這樣的圖形，就會得到一排圓形；更複雜的圖形也會以同樣方式複製。

你可以在 **Liberation → Settings** (`Cmd / Ctrl + ,`) 選擇 Liberation 要監聽的 MIDI 介面。

* **midi channel** – 要監聽的 MIDI channel（0 = 所有 channel，1–16 = 指定 channel）
* **width** – notes 展開的總寬度。
* **midi note min / max** – 範圍內最低與最高的 MIDI note 值。
* **ignore out of range notes** – 濾除超出設定範圍的 notes。如果停用，超出範圍的 notes 會被限制到最接近的可用 note（高音會觸發範圍頂端，低音會觸發範圍底端）。
* **auto extend range** – 如果播放的 notes 超出範圍，會自動加寬範圍。

{% hint style="info" %}
不確定目前收到哪些 notes 範圍嗎？開啟 **auto extend range**，把 **midi note min** 設得很高、**midi note max** 設得很低，然後播放你的 notes。系統會全部捕捉並替你擴展範圍。全部取得後，只要關閉 **auto extend range** 就能鎖定範圍。
{% endhint %}

* **leave all notes visible** – 無論 notes 是否正在播放，都為範圍內的所有 notes 建立光束或圖形，產生「雷射豎琴」效果。
* **hit colour** – note 被觸發時顯示的顏色。
* **hit colour hold time** – hit colour 在開始淡出前維持全亮的時間。值以秒為單位（0–1）。_100% = 1 秒。_
* **hit colour decay time** – hold time 結束後，hit colour 淡回原狀所需的時間。值以秒為單位（0–1）。_100% = 1 秒。_

{% hint style="info" %}
如果你的內容本來就是純白色，把 hit colour 設成白色不會有任何差異。為了取得最佳效果，請讓內容使用飽和色彩，並將 hit colour 設為白色；這樣在 notes 被觸發時會產生很漂亮的閃光效果。
{% endhint %}

* **note off fade out time** – note 放開後淡出所需的時間。值以秒為單位（0–1）。_100% = 1 秒。_
* **hit scale factor** – note 被觸發時放大的比例（例如 2 = 兩倍大小）。
* **hit scale hold time** – note 在縮回前維持放大的時間。值以秒為單位（0–1）。_100% = 1 秒。_
* **hit scale decay time** – note 回到原始大小所需的時間。值以秒為單位（0–1）。_100% = 1 秒。_
* **note off shrink time** – note 放開後縮回原始大小所需的時間。值以秒為單位（0–1）。_100% = 1 秒。_（啟用 **leave all notes visible** 時不會有作用。）

{% hint style="info" %}
縮放 - 請注意，如果你的內容只有單一個點，縮放不會有任何效果！
{% endhint %}
