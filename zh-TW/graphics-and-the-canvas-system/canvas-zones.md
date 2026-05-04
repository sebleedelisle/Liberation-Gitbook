---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-zones
---

# 🟩 Canvas zones

在 Canvas view 中，canvas zone 會顯示為粉紅色外框矩形。它用來選取 Canvas 內的一塊矩形區域，並將其中的內容傳送到一台或多台雷射。

你可以用滑鼠點按並拖曳 zones 來移動它們。拖曳角落即可調整大小與形狀。

### 新增 canvas zone

按一下工具列中的 _Add a new canvas zone_ 按鈕。

### 將 canvas zone 指派給雷射

在 zone 上按右鍵，切換數字按鈕來選擇要將這個 canvas zone 指派給哪些雷射。

{% hint style="danger" %}
警告：如果雷射處於 armed 狀態，你可能會突然開始從預設 canvas zone 投射內容。建議先將雷射 disarm，再將 canvas zones 指派給它。
{% endhint %}

如果你現在前往該雷射的 _OUTPUT_ view，就會在其中看到這個 canvas zone；現在可以像編輯任何 beam zone 一樣編輯它。請參閱 [Zones](../output-view/zones.md "mention")。

{% hint style="info" %}
你也可以直接從 _OUTPUT_ view 將 canvas zone 加入雷射：按一下左側工具列中的 _Add existing canvas zone_ 按鈕。
{% endhint %}

### 右鍵選單

在 zone 上按右鍵，你會看到刪除此 canvas zone、將它移到後方，以及鎖定它的選項。
