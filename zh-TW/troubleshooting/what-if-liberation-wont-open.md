---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ 如果 Liberation 打不開怎麼辦？

這種情況不常見，但有時 Liberation 可能無法啟動，或是一開啟就當機。這幾乎都是因為某個本機設定檔損毀所造成，通常發生在系統當機或電腦出現非預期狀況之後。

好消息是，只要重設本機設定就能輕鬆修復。以下是在 macOS 和 Windows 上的處理方式。

> **重要**
>
> * 進行任何操作前，請先關閉 Liberation。
> * 這些步驟只會影響本機設定、紀錄與快取。你的授權與帳號不會受到影響。

***

#### 工作資料夾在哪裡

每個 Liberation 版本都有自己的工作資料夾。例如，如果你使用的是 1.0.3 版，資料夾名稱就會是 1.0.3。

* **macOS**：`~/Library/Application Support/Liberation/1.0.3`
* **Windows**：`AppData\Local\Liberation\1.0.3`

**快速開啟資料夾的方法**

**macOS**

1. 在 Finder 中按 **Shift + Cmd + G**。
2.  貼上這個路徑，然後按 **Enter**：

    ```
    ~/Library/Application Support/Liberation
    ```
3. 開啟與你的版本號碼相同的資料夾，例如 `1.0.3`。

**Windows**

1.  按 **Win + R**，貼上以下內容，然後按 **Enter**：

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. 開啟與你的版本號碼相同的資料夾，例如 `1.0.3`。

> **Windows 提示**：如果你改用檔案總管瀏覽，請啟用隱藏項目：**檢視 > 顯示 > 隱藏的項目**。

***

#### 步驟 1 – 安全重設設定檔

在你的版本資料夾內，開啟：

```
data/liberation/
```

在 liberation 資料夾中，你應該會看到一個名為 `settings.json` 的檔案。刪除這個檔案。

* **macOS 範例**：`~/Library/Application Support/Liberation/1.0.3/data/liberation/settings.json`
* **Windows 範例**：`%LOCALAPPDATA%\Liberation\1.0.3\data\liberation\settings.json`

現在試著啟動 Liberation。如果可以開啟，就完成了。

***

#### 步驟 2 – 檢查是否有造成問題的 Clip

如果 Liberation 是在你編輯 Clip 時當機，可能是該 Clip 檔案中的某些內容造成問題。

在與 settings.json 檔案相同的資料夾中，你應該會看到一個名為 `clipEdit.json` 的檔案。

先將這個檔案備份到安全的位置（例如桌面），然後從 Liberation 工作資料夾中刪除它。

再次嘗試啟動 Liberation。如果現在可以正常開啟，請將備份的檔案寄到 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)，讓我們調查造成問題的原因。

***

#### 步驟 3 - 先備份，再刪除整個工作資料夾

如果步驟 1 和步驟 2 都沒有幫助：

1. **備份**整個版本資料夾：
* macOS：在 `1.0.3` 資料夾上按右鍵，選擇 **Compress** 建立 zip 檔，或將它複製到安全的位置，例如桌面。
* Windows：在 `1.0.3` 資料夾上按右鍵，選擇 **Send to > Compressed (zipped) folder**，或將它複製到安全的位置，例如桌面。
2. 備份完成後，從 Liberation 工作位置**刪除**原本的 `1.0.3` 資料夾。
3. 再次啟動 Liberation。它會重新建立一個全新的工作資料夾。

如果 Liberation 現在可以開啟，請繼續進行步驟 4。

***

#### 步驟 4 - 將備份寄給我們

這能幫助我們找出造成問題的原因，並在未來版本中避免再次發生。

如果你在步驟 3 尚未將**備份**壓縮成 zip，請先壓縮，然後用電子郵件寄給我們，以便我們診斷原因。

* **收件人**：[info@liberationlaser.com](mailto:info@liberationlaser.com)
* **主旨**：Liberation start-up fix - working folder backup
* **內文**：請包含：
  * 作業系統與版本（例如 macOS 14.6 或 Windows 11 23H2）
* Liberation 版本（例如 1.0.3）
  * 哪個步驟解決了問題（如果有的話：步驟 1、步驟 2 或步驟 3）
  * 問題開始前發生了什麼事的簡短說明
* **附件**：你的 `1.0.3` 工作資料夾 zip 備份檔。

> 如果 zip 檔太大無法透過電子郵件傳送，請上傳到雲端硬碟並分享連結。

***

#### 步驟 3 後仍然無法啟動？

如果刪除工作資料夾後 Liberation 仍然打不開：

* 重新啟動電腦後再試一次。
* 暫時停用可能會阻擋建立新資料夾的防毒或安全工具，然後再嘗試啟動。
* 直接在現有安裝上重新安裝最新版 Liberation。
* 如果以上方法都無效，請聯絡支援：[**info@liberationlaser.com**](mailto:info@liberationlaser.com)，並附上詳細資訊，以及 `logs` 子資料夾中的任何當機紀錄（如果有的話）。

***

#### 摘要

1. 刪除版本工作資料夾中的 `data/liberation/settings.json`。
2. 如果你當時正在編輯 Clip，請先備份再刪除 `data/liberation/clipEdit.json`。
3. 如果仍然打不開，請先備份再刪除整個 `1.0.3`（或你的版本）資料夾。
4. 如果步驟 3 解決了問題（或即使沒有解決），請將備份壓縮成 zip，並連同你的作業系統與 Liberation 版本寄到 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)。
