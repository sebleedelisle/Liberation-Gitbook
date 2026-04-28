---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ 簡介

Liberation 內置靈活而強大的 DMX 系統，讓你透過 Art-Net 建立燈光效果，以及控制兼容 DMX 的激光設備。它的設計目標，是讓你的燈光可以輕鬆與激光表演同步，無需另設獨立燈光控制台。

{% hint style="info" %}
**甚麼是 Art-Net？它與 DMX 有甚麼關係？**

**DMX** 是多年來用於控制燈具、激光、煙霧機及其他舞台效果的系統。它會透過專用線材（通常使用 XLR 接頭）傳送控制訊號，而每件設備會接收指定的一組 channel，以決定要執行甚麼動作。

**Art-Net** 是一種較新的方式，用普通電腦網絡傳送相同的 DMX data。它不使用專用線材，而是透過 Ethernet 傳送所有資料，就像互聯網或本地網絡流量一樣。

在 Liberation 中，所有 DMX output 都會使用 Art-Net 傳送。你可以直接控制兼容 Art-Net 的設備，亦可以接駁一個 **Art-Net node**——這是一個小型轉換盒，可將 Art-Net 轉回標準 DMX。換言之，即使傳統 DMX 燈具及效果設備本身不支援 Art-Net，你仍然可以控制它們。
{% endhint %}

你亦可以用它控制各種舞台設備，例如煙霧機、薄霧機、CO₂ 噴射器、冷焰火機等。只要設備支援 DMX，你就可以將它設定為 DMX zone，並直接從 Liberation 觸發，與你的激光內容並行使用。

DMX 設備會以 **DMX zone** 形式加入，並與你的 laser beam zones 及 Canvas 目標區域一同顯示在 zone list 中。每個 DMX zone 都會使用一個 **DMX preset**，用來告訴 Liberation 如何將 laser clips 的屬性（例如位置、顏色及亮度）對應至 DMX channel values。

當你將一個 clip 傳送到 DMX zone 時，Liberation 會讀取該 clip 中的第一個元素，並根據 preset 轉換其屬性。這樣你就可以用現有已用於激光的同一批 clips，直接驅動燈具及 DMX 效果。

#### Liberation at Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Liberation DMX 系統的首次實際測試，是在 Glastonbury 2023 進行；當時 Reach Lasers 在 Arcadia「spider」舞台中合共安裝了 90 個 beam sources。

其中 18 部激光以內置 Ether Dreams 控制，另外 12 組 6-head beam bars 則透過 Art net 及 DMX 控制。
