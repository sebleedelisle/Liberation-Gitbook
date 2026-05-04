---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 現場 MIDI 控制器

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40 controller**

這是 Liberation 預設的硬體 controller；我們非常推薦使用，也可以說 Liberation 從一開始就是圍繞這套硬體設計的。只要接上 APC40，Liberation 就會立刻自動連線。

{% hint style="warning" %}
_糟了！表演到一半 USB 接頭被拔掉了！_

不用慌——把它插回去就好，Liberation 會自動重新連線，不會有麻煩。
{% endhint %}

### APC40 Mark 1 還是 Mark 2？

簡單來說，建議使用 Mark 2，因為它有全彩按鈕，能更貼近 Liberation 的 Clip Deck 介面。Mark 1 版本必要時也能使用，但會稍微比較容易混淆，因為它的配置和螢幕上的介面略有不同，而且按鈕只能顯示紅色、橘色或綠色，無法對應 Clip 的顏色。

{% hint style="info" %}
最早的 APC40 Mark 1 在 2009 年推出（！），有些人到現在仍然偏好它的金屬機身結構，以及堅固、像控台一樣的外型。新版 Mark 2 在 2014 年推出，雖然曾在 2024 年停產，但因為視覺藝術家（Resolume 等）和雷射玩家的需求，預計在 2025 年恢復生產。
{% endhint %}

APC40 上所有可用控制項目的完整清單，請參閱 [APC40 參考資料](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 也包含 APC Mini 設定檔。它對應 8x5 Clip 格、zone 按鈕、zone X/Y 翻轉控制、群組按鈕、停止所有 Clips、Clip 頁面移動、zone 頁面移動、Tap Tempo、Bar Reset，以及 tempo nudge。它的推桿可控制效果強度，按住 Shift 使用推桿則可控制效果參數。最後一支推桿控制整體亮度。

### MIDI Fighter Twister

MIDI Fighter Twister 設定檔偏重使用編碼旋鈕控制，而不是啟動 Clip。其中一排編碼旋鈕控制效果插槽 1–8 的參數 1，另一排則對應 Parameters panel 中 8 個隨情境變化的控制項，包括 Clip Shift、zone delay、Global Spin/Scale，以及群組淡入淡出。
