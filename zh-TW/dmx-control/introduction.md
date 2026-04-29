---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ 簡介

Liberation 內建一套彈性且功能完整的 DMX 系統，可讓你建立燈光效果，並透過 Art-Net 控制支援 DMX 的雷射。這套系統的設計目標，是讓你的燈光能輕鬆與雷射秀同步，不需要另外準備燈光控制台。

{% hint style="info" %}
**什麼是 Art-Net？它和 DMX 有什麼關係？**

**DMX** 是多年來用於控制燈光、雷射、煙霧機與其他舞台特效的系統。它透過專用線材傳送控制訊號（通常使用 XLR 接頭），每個燈具或設備會監聽指定的一組通道，藉此決定要執行的動作。

**Art-Net** 則是以一般電腦網路傳送相同 DMX 資料的較新方式。它不使用專用線材，而是透過 Ethernet 傳送所有資料，就像網際網路或區域網路流量一樣。

在 Liberation 中，所有 DMX 輸出都會使用 Art-Net 傳送。你可以直接控制支援 Art-Net 的設備，也可以連接一台 **Art-Net 節點**——這是一個小型轉換盒，會將 Art-Net 轉回標準 DMX。這表示即使傳統 DMX 燈具與特效設備本身不支援 Art-Net，你仍然可以控制它們。
{% endhint %}

你也可以用它控制各種舞台設備，例如煙霧機、薄霧機、CO₂ 噴射機、冷焰火機等等。只要設備支援 DMX，就可以將它設定為 DMX zone，並直接從 Liberation 觸發，與你的雷射內容一起使用。

DMX 燈具會加入為 **DMX zone**，並與雷射 beam zone 和 canvas 目標區域一起顯示在 zone 清單中。每個 DMX zone 都會使用一個 **DMX preset**，用來告訴 Liberation 如何將雷射 Clip 的屬性（例如位置、色彩與亮度）對應到 DMX 通道值。

當你將 Clip 傳送到 DMX zone 時，Liberation 會讀取 Clip 中的第一個元素，並依照 preset 將其屬性轉換。如此一來，你就可以直接使用已經用於雷射的相同 Clip，來驅動燈光與 DMX 特效。

#### Glastonbury 的 Liberation

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Liberation DMX 系統的第一次實際測試，是在 Glastonbury 2023。當時 Reach Lasers 在 Arcadia「spider」舞台中，總共安裝了 90 個光束來源。

其中 18 台雷射使用內建 Ether Dream 控制，另外 12 組 6 頭光束條則透過 Art-Net 與 DMX 控制。
