---
description: >-
  Lasers can be dangerous so it's important to follow best practices and safety
  guidelines. This page is a useful overview that will help you through the
  process of setting up lasers safely.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/setting-up-lasers
---

# ✅ 雷射設定流程概覽

### 安全啟動雷射的流程概覽

本手冊不能取代正式的雷射安全培訓；在公眾場合使用雷射之前，你絕對需要接受相關培訓。某些地區會有額外法律要求，但無論如何，你都應該始終遵守安全及專業操作的最佳做法。

PLASA 提供免費下載的雷射安全指南，一般被視為最佳做法：[https://www.plasa.org/guidance-for-display-lasers/](https://www.plasa.org/guidance-for-display-lasers/)

使用前，請務必確定你了解雷射相關的安全影響！

#### 簡介

本頁旨在讓你概覽安全啟動雷射的流程。每個步驟的具體操作細節會在本節稍後部分說明，但本頁可幫助你掌握整體流程；日後每次設定雷射時，也可以回來作為參考。

<figure><img src="../.gitbook/assets/laser-aperture.jpg" alt=""><figcaption><p>典型的雷射出光口保護蓋</p></figcaption></figure>

### 設定硬件：

1. **關上雷射的出光口保護蓋**
2. **穩固安裝雷射**，並將它指向正確方向
3. **將停止按鈕連接**到雷射
4. **將雷射控制器連接**到電腦
5. **開啟**雷射電源

### 設定 Liberation：

1. **解除所有雷射的 Arm 狀態**，並在 Liberation 中尋找及連接控制器
2. **將&#x20;**_**Global Brightness**_**&#x20;設定調低至 0**（使用圖示列中的滑桿，或 APC40 上的 _Master Fader_）
3. **將雷射 Arm**：出光口保護蓋仍然關上時，確認目前沒有任何 clips 啟用，然後將雷射 Arm（使用 _Laser Overview_ panel 中的 _Arm_ 按鈕）
4. **開啟測試圖案**（使用圖示列中的 ☒ 按鈕，選擇圖案 1，即中間有十字的綠色方形）
5. **調整輸出 zone**：先估算最安全的 zone 大小及位置（例如可以高高投射到天花，但實際取決於你的環境）
6. **確認雷射正常運作**：慢慢提高亮度，直到你能在出光口窗口後方看到光。然後將亮度降回零。
7. **測試停止按鈕**，確保按下後所有雷射輸出都會熄滅

### 開始雷射輸出

1. **清空照射區域**：確保沒有人會被雷射照射，並向所有人員簡報，要求他們在雷射設定期間留在照射區域之外。（你亦應確保所有相機及投影機已被遮蓋，或已蓋上鏡頭蓋！）
2. **打開出光口保護蓋**：站在側邊並避開輸出方向，將出光口保護蓋向下滑開。如果你的 zones 設在較高位置，可以考慮只打開一部分。
3. **提高亮度，直到雷射僅僅可見**：只將雷射調至足夠看見 zone 的亮度
4. **調整 zone(s)**：設定 zone 的大小、形狀及位置，確保它距離任何公眾可進入區域的地面至少 3m，且雷射不會到達任何其他公眾可進入區域
5. **加入實體遮擋**：使用出光口保護蓋及／或黑色鋁箔膠帶，對目標 zone 以外的任何位置作實體遮擋。這一點極其重要，因為任何雷射硬件或軟件都有可能故障。
6. **加入軟件遮罩**：Liberation 內的軟件遮罩可用於保護相機及投影機，但**絕不可**用來取代保護人員所需的實體遮擋。請注意，沒有任何軟件或硬件是絕對可靠的，因此使用軟件遮罩前，必須確保你了解相關風險。

{% hint style="warning" %}
請注意，本指南假設你在室內設定。如果你在戶外工作，必須採取額外步驟以確保航空安全，包括但不限於：

* 向 FAA 或 CAA 等航空機構取得所需許可
* 與附近機場及飛行場聯絡協調
* 檢查公開航班雷達，並安排觀察員留意飛機

即使雷射遠低於安全閾值，仍可能對機師造成災難性的分心。

在將任何雷射射向空域之前，請確保你具備所需資格、牌照及許可。
{% endhint %}
