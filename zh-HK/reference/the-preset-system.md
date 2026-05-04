---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ 預設系統

在 Liberation 中，只要需要從一系列_預設_中儲存多個可選設定，都會使用預設系統。

此系統目前用於：

* 掃描器設定
* 顏色校準設定
* 3D Visualiser 攝影機設定
* 3D Visualiser 鐳射設定
* DMX profiles

因此，如果你為全新的 CT6210 掃描器調整好掃描器設定，就可以將它儲存為預設，命名為「CT6210」。之後每當你需要使用時，它都會出現在預設清單及下拉式選單中。

不論你是否正在使用某個預設，所有預設都會隨你的 project（或 laser settings）一同儲存。因此，每次你載入這些檔案時，檔案內的所有預設都會加入到你現有的預設中。如果載入的其中一個預設與現有預設同名，它會覆蓋現有的預設。

你亦可以使用預設下拉式清單旁邊的 load/save 按鈕（磁碟圖示）匯入及匯出預設檔案。這會開啟一個彈出視窗，當中有 import/export 按鈕，亦可刪除一個或多個預設。

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>The pop-up menu that opens when you click the load/save icon</p></figcaption></figure>

如果你編輯某個預設，例如名為 _Default_ 的掃描器設定，請注意其他鐳射不會自動更新。相反，它們各自的掃描器設定現在會標示為 _Default(edited)_。如要更新為新的 _Default_ 預設，請在下拉式清單中重新選取它。

{% hint style="info" %}
如果你有很多部鐳射，並想更新它們所有的掃描器設定，請使用 _COPY LASER SETTINGS_ 系統。請參閱[複製鐳射設定](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

如果你刪除了某個在其他地方使用中的預設，你不會失去該設定；它只會改為標示為 _(deleted)._
