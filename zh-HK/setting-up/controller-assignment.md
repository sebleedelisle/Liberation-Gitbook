---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ 控制器指派

在 Liberation 內設定好各部激光機後，你便可以將每部激光機指派到現實中的激光控制器。（可參閱[兼容的激光機及控制器 (DACs)](../hardware/compatible-lasers-and-controllers-dacs.md)，查看可使用哪些硬件。）控制器可以透過 USB 或網絡連接。

* 透過 _View -> Controller Assignment_ 選單選項開啟 _Controller Assignment_ 面板。（或者，你亦可以使用 _Laser Overview_ 面板中的 _ASSIGN LASER CONTROLLERS_ 按鈕。）

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment 面板"><figcaption></figcaption></figure>

* 面板分為兩部分：左邊是激光機列表，右邊是可用控制器列表。如果列表中看不到你的激光控制器，請按 _REFRESH_ 按鈕。如果仍然有問題，請參閱[疑難排解](../troubleshooting/)。
* 要將控制器指派到激光機，請由右邊點擊並拖曳到左邊一個空置的激光機位置。這會告訴 Liberation 哪個控制器應該用於哪部激光機。（如果你改變主意，可以隨時將控制器上下拖曳，由一部激光機移到另一部。）

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="控制器列表" width="375"><figcaption></figcaption></figure>

* 如果控制器旁邊顯示綠色方格，表示 Liberation 已成功連接到該控制器。

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>一個 Ether Dream 及一個 Helios DAC 分別指派到第 2 及第 3 部激光機</p></figcaption></figure>

{% hint style="info" %}
請注意，每次連接到控制器時，激光機都會自動設為未啟動狀態。
{% endhint %}

* 橙色方格 🟧 表示控制器出現間歇性連接問題。這通常由網絡問題引起，請參閱[疑難排解](../troubleshooting/)。
* 紅色方格 🟥 表示無法連接到控制器，請參閱[疑難排解](../troubleshooting/)。
* _disconnect button_ (X) 會中斷控制器連接，但不會從激光機指派中清除它。之後你可以使用 _reconnect button_（重新整理箭咀圖示）重新連接，或者再次點擊 _disconnect button_ 以清除指派。
* _進階功能：_ 點擊看起來像圖表的按鈕，即可開啟控制器分析面板。這是一項進階功能，可提供資料串流的詳細資訊，並有助於排查問題。（某些控制器類型可能沒有此選項。）
* 你可以使用 _rename button_（鉛筆）將此控制器重新命名為任何你想要的名稱。建議使用容易將它與特定硬件聯繫起來的名稱。如果控制器內置於激光機，你可以相應命名，例如 _LaserCube Ultra #1_ 或 _Triton T5 #3_。這些名稱會儲存在你的 Liberation 安裝中，並會由此以後顯示；這對快速識別你的激光機非常有幫助。

{% hint style="info" %}
專業提示 — 在右邊的控制器上**雙擊**，即可自動將它指派到左邊下一個可用的激光機。如果你有很多激光機需要指派，這可以節省不少時間！
{% endhint %}

你可以使用 _DISCONNECT ALL_ 及 _RECONNECT ALL_ 按鈕快速重設所有連接。當你遇到網絡問題時，這會很有用。
