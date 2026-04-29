---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ 如果 Liberation 無法開啟，應該怎樣做？

雖然不常見，但有時 Liberation 可能無法啟動，或在開啟後立即當機。這幾乎總是因為某個本機設定檔已損壞——通常是在系統當機或電腦發生意外情況後出現。

好消息是，只要重設本機設定，通常就可以輕鬆修復。以下是在 macOS 和 Windows 上的處理方法。

> **重要**
>
> * 執行任何步驟前，請先關閉 Liberation。
> * 這些步驟只會影響本機設定、記錄檔和快取。你的授權和帳戶不會受影響。

***

#### 在哪裏找到工作資料夾

每個 Liberation 版本都有自己的工作資料夾。例如，如果你正在使用 1.0.0 版本，資料夾名稱就會是 1.0.0。

* **macOS**：`~/Library/Application Support/Liberation/1.0.0`
* **Windows**：`AppData\Local\Liberation\1.0.0`

**快速開啟資料夾的方法**

**macOS**

1. 在 Finder 中，按 **Shift + Cmd + G**。
2.  貼上以下路徑，然後按 **Enter**：

    ```
    ~/Library/Application Support/Liberation
    ```
3. 開啟與你版本號碼相符的資料夾，例如 `1.0.0`。

**Windows**

1.  按 **Win + R**，貼上以下內容，然後按 **Enter**：

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. 開啟與你版本號碼相符的資料夾，例如 `1.0.0`。

> **Windows 提示**：如果你改用 File Explorer 瀏覽，請啟用隱藏項目：**View > Show > Hidden items**。

***

#### 步驟 1 – 安全地重設設定檔

在你的版本資料夾內，開啟：

```
data/liberation/
```

在 liberation 資料夾內，你應該會找到一個名為 `settings.json` 的檔案。刪除此檔案。

* **macOS 範例**：`~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows 範例**：`%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

現在嘗試啟動 Liberation。如果能夠開啟，就完成了。

***

#### 步驟 2 – 檢查是否有問題 Clip

如果 Liberation 在你編輯 Clip 時當機，該 Clip 檔案的某些內容可能導致問題。

在 settings.json 檔案所在的同一資料夾內，你應該會找到一個名為 `clipEdit.json` 的檔案。

先將此檔案備份到安全位置（例如 Desktop），然後從 Liberation 工作資料夾中刪除它。

再次嘗試啟動 Liberation。如果現在可以正常開啟，請將已備份的檔案電郵至 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)，讓我們調查問題原因。

***

#### 步驟 3 - 備份，然後刪除整個工作資料夾

如果步驟 1 和步驟 2 都沒有幫助：

1. **備份**整個版本資料夾：
   * macOS：在 `1.0.0` 資料夾上按右鍵，選擇 **Compress** 以建立 zip 檔，或將它複製到安全位置，例如 Desktop。
   * Windows：在 `1.0.0` 資料夾上按右鍵，選擇 **Send to > Compressed (zipped) folder**，或將它複製到安全位置，例如 Desktop。
2. 備份後，從 Liberation 工作位置**刪除**原本的 `1.0.0` 資料夾。
3. 再次啟動 Liberation。它會重新建立一個全新的工作資料夾。

如果 Liberation 現在可以開啟，請繼續步驟 4。

***

#### 步驟 4 - 將備份傳送給我們

這有助我們找出問題原因，並在未來版本中避免同類問題。

如果你在步驟 3 尚未將**備份**壓縮成 zip，請先壓縮，然後電郵給我們以便診斷原因。

* **收件人**：[info@liberationlaser.com](mailto:info@liberationlaser.com)
* **主旨**：Liberation start-up fix - working folder backup
* **內容**：請包括：
  * 作業系統及版本（例如 macOS 14.6 或 Windows 11 23H2）
  * Liberation 版本（例如 1.0.0）
  * 哪個步驟解決了問題（如適用）：步驟 1、步驟 2 或步驟 3
  * 問題開始前發生了甚麼事的簡短描述
* **附件**：你的 `1.0.0` 工作資料夾 zip 備份。

> 如果 zip 檔案太大，無法透過電郵傳送，請上載到雲端硬碟並分享連結。

***

#### 完成步驟 3 後仍然無法啟動？

如果刪除工作資料夾後，Liberation 仍然無法開啟：

* 重新啟動電腦，然後再試一次。
* 暫時停用可能阻止建立新資料夾的防毒或安全工具，然後嘗試啟動。
* 在現有安裝上重新安裝最新的 Liberation build。
* 如果以上方法都無效，請聯絡支援：[**info@liberationlaser.com**](mailto:info@liberationlaser.com)，並提供詳情；如 `logs` 子資料夾中有當機記錄，也請一併提供。

***

#### 摘要

1. 在你的版本化工作資料夾中刪除 `data/liberation/settings.json`。
2. 如果你當時正在編輯 Clip，請先備份，然後刪除 `data/liberation/clipEdit.json`。
3. 如果仍然無法開啟，請先備份，然後刪除整個 `1.0.0`（或你的版本）資料夾。
4. 如果步驟 3 解決了問題（或即使沒有解決），請將備份壓縮成 zip，並連同你的作業系統及 Liberation 版本傳送至 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)。
