---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 使用 Liberation 搭配 Capture

Liberation 支援將 [Capture](https://capture.se) 作為外部視覺化工具（1.0.3 版起）。如果你的工作流程已經在使用 Capture，可以用它在 3D 場景中視覺化 Liberation 的即時雷射輸出。

### 運作方式

不需要特殊的連線流程，也不需要手動連結。

只要：

* Liberation 和 Capture 位於同一個網路
* 你的防火牆允許連線

……那麼你在 Liberation 中設定好的任何雷射，都會自動在 Capture 內顯示為媒體來源。你不需要設定 IP 位址，也不需要啟用任何特殊選項——它會直接出現。

### 在 Capture 中看到雷射

Liberation 中所有已設定的雷射，都會在 Capture 中顯示為可用的媒體來源。

若要實際看到輸出：

* 雷射必須在 Liberation 中處於 armed 狀態
* 來源必須附加到 Capture 內的雷射燈具

一旦處於 armed 狀態，Capture 就會視覺化來自 Liberation 的即時輸出串流。如果雷射在 Liberation 中處於 disarmed 狀態，它仍會在 Capture 中顯示為來源，但不會輸出任何內容。

如需在 Capture 中設定雷射的更多說明與支援，請參閱 [capture.se](https://www.capture.se/) 上的文件。 <br>

### 授權限制與 armed 雷射

Capture 連線的處理方式與實體雷射輸出完全相同。

也就是說：

* 你只能 arm 授權等級允許數量的雷射
* 只有 armed 雷射會主動將資料傳送到 Capture

### 我需要 Capture 嗎？

完全不需要。

Liberation 內建 3D 視覺化工具，隨時可用，而且不受授權等級限制。你可以直接在 Liberation 內設計並預覽演出，不需要任何外部軟體。

如果你已經使用 Capture 進行燈光或演出設計，它只是另一個可選的方式。

### 疑難排解

如果雷射沒有出現在 Capture 中：

* 檢查兩個應用程式是否位於同一個網路
* 檢查防火牆設定
* 確認雷射在 Liberation 中處於 armed 狀態
