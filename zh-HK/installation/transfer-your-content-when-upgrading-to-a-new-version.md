---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/installation/transfer-your-content-when-upgrading-to-a-new-version
---

# 🟩 升級至新版本時轉移你的內容

Liberation 會將內容儲存在其 working folder（請參閱[工作資料夾的位置](../troubleshooting/where-to-find-the-working-folder.md "mention")），而每次發佈新版本時，此資料夾都會更改。如果你想將舊版本的工作檔案保留到新版本：&#x20;

1. 開啟原本版本的 Liberation
2. 使用 _File->Project->Export Project_。這會儲存你 Liberation 內的所有內容，包括 laser setup、timelines、Clip Deck，全部都會儲存！&#x20;
3. 關閉此版本，然後開啟新版本的 Liberation
4. 使用 _File->Project->Import Project_，並選擇你在步驟 2 匯出的 project file。&#x20;

你的所有內容現在應該已經在新版本中。

#### 保留多個 Liberation 版本

安裝新版本之前，請先重新命名舊版本。我通常會使用其版本號碼，例如 Liberation103.app（Windows 上則為 .exe）。你可以保留任意數量的 Liberation 版本，但同一時間只可以執行一個版本。 <br>

#### 如果你已用新版本覆蓋了舊版本的 Liberation

最可靠的做法是重新安裝較舊版本的 Liberation，然後按照上述流程操作。&#x20;

或者，你也可以嘗試複製你的 working folder，並將其重新命名為新版本的版本號碼。&#x20;
