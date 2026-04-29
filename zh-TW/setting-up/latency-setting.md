---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ 延遲設定

在 _Settings_ 面板（_Liberation->Settings_ 或 CMD/CTRL ,）中，你會看到標示為 _Latency(ms)_ 的滑桿。（在較舊版本的 Liberation 中，這項設定位於 Laser Overview 面板）

{% hint style="info" %}
預設的延遲設定 150ms 在大多數情況下都適用；但如果你遇到網路問題，可以嘗試將它調高。
{% endhint %}

### 較完整的說明

這個「影格延遲」設定，是指從 Liberation 建立一個影格，到雷射開始輸出該影格之間的最長時間。如果提高這個數值，你可能會注意到 Liberation 與雷射輸出之間有些微延遲。

較長的影格延遲的好處是，Liberation 可以盡快將內容填入 laser controller 的緩衝區；如果網路出現壅塞，controller 比較不容易用完點資料。

這通常只適用於網路 DAC，而 100ms 的設定通常能在速度與防護網路延遲之間取得良好平衡。如果你的網路非常穩定，應該可以將它降低到 50ms。&#x20;
