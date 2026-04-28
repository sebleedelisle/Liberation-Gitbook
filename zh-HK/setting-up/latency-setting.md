---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ 延遲設定

在 _Settings_ 面板（_Liberation->Settings_ 或 CMD/CTRL ,）中，你會見到一個標示為 _Latency(ms)._ 的滑桿。（在較舊版本的 Liberation 中，這項設定位於 Laser Overview 面板）

{% hint style="info" %}
預設延遲設定為 150ms，大部分情況下都應該足夠；但如果遇到網絡問題，你可以嘗試將其調高。
{% endhint %}

### 較深入的說明

這個「frame latency」設定，是指由 Liberation 建立一個 frame，到 laser 開始輸出該 frame 之間的最長時間。如果你增加這個數值，可能會留意到 Liberation 與 laser 輸出之間有輕微延遲。

較長 frame latency 的好處，是 Liberation 可以盡快將內容填入 laser controller 的 buffer；如果網絡出現擠塞，controller 較不容易耗盡 points。

這通常只適用於網絡 DAC，而 100ms 的設定一般可在速度與抵禦網絡延遲之間取得良好平衡。如果你的網絡非常穩定，應該可以將它降低至 50ms。&#x20;
