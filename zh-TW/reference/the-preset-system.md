---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Preset 系統

在 Liberation 中，只要需要從一組 _Preset_ 清單裡儲存多個可選設定，就會使用 Preset 系統。

這套系統目前用於：

* 掃描器設定
* 色彩校正設定
* 3D 視覺化器攝影機設定
* 3D 視覺化器雷射設定
* DMX profiles

因此，如果你替新的 CT6210 掃描器調整好掃描器設定，可以將它儲存成一個 Preset，命名為「CT6210」。之後需要時，它就會出現在 Preset 清單中，也可以從下拉選單選取。

無論你是否正在使用某個 Preset，所有 Preset 都會跟著你的專案（或雷射設定）一起儲存。因此，每次載入這類檔案時，檔案內的所有 Preset 都會加入你現有的 Preset。如果載入的某個 Preset 名稱與現有 Preset 相同，將會覆寫現有的 Preset。

你也可以使用 Preset 下拉清單旁的 load/save 按鈕（磁碟片圖示）匯入或匯出 Preset 檔案。這會開啟一個彈出視窗，其中有匯入／匯出按鈕，也可以刪除一個或多個 Preset。

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>The pop-up menu that opens when you click the load/save icon</p></figcaption></figure>

如果你編輯某個 Preset，例如名為 _Default_ 的掃描器設定，請注意其他雷射不會自動更新。它們各自的掃描器設定會改標示為 _Default(edited)_。若要更新成新的 _Default_ Preset，請從下拉清單重新選取它。

{% hint style="info" %}
如果你有很多雷射，並且想更新所有雷射的掃描器設定，請使用 _COPY LASER SETTINGS_ 系統。請參閱[複製雷射設定](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

如果你刪除了其他地方正在使用的 Preset，該設定不會遺失，而是會顯示為 _(deleted)_。
