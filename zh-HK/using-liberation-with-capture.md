---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 將 Liberation 配合 Capture 使用

Liberation 支援以 [Capture](https://capture.se) 作為外置視覺化器（版本 1.0.3 起）。如果你在工作流程中已經使用 Capture，可以用它在 3D 場景中視覺化 Liberation 的即時雷射輸出。

### 運作方式

不需要特別的連線程序，也不需要手動連結。

只要：

* Liberation 和 Capture 在同一網絡上
* 你的防火牆允許連線

……那麼你在 Liberation 中設定好的任何雷射，都會自動在 Capture 內顯示為媒體來源。你不需要設定 IP 位址或啟用任何特別選項——它會自動出現。

### 在 Capture 內查看雷射

Liberation 中所有已設定的雷射，都會在 Capture 中顯示為可用的媒體來源。

要實際看到輸出：

* 雷射必須在 Liberation 中已啟用輸出（armed）
* 來源必須連接到 Capture 內的 laser fixture

啟用輸出後，Capture 會視覺化來自 Liberation 的即時輸出串流。如果某個雷射在 Liberation 中停用輸出（disarmed），它仍會在 Capture 中作為來源顯示，但不會輸出任何內容。

有關在 Capture 中設定雷射的更多指引和支援，請參閱 [capture.se](https://www.capture.se/) 的文件。 <br>

### 授權限制與已啟用輸出的雷射

Capture 連線的處理方式與實體雷射輸出完全相同。

這表示：

* 你只能啟用授權級別所允許數量的雷射
* 只有已啟用輸出（armed）的雷射才會主動傳送資料到 Capture

### 我需要 Capture 嗎？

完全不需要。

Liberation 內置 3D Visualiser，隨時可用，並且不受授權級別限制。你可以直接在 Liberation 內設計和預覽演出，無需任何外部軟件。

如果你已經使用 Capture 進行燈光或演出設計，它只是一個額外選項。

### 疑難排解

如果雷射沒有在 Capture 中出現：

* 檢查兩個應用程式是否在同一網絡上
* 檢查你的防火牆設定
* 確保雷射已在 Liberation 中啟用輸出
