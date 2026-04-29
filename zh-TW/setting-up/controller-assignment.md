---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Controller Assignment

在 Liberation 中設定好雷射後，就可以把每一台雷射指派給現場實際使用的雷射控制器。（請參閱[相容的雷射與控制器（DAC）](../hardware/compatible-lasers-and-controllers-dacs.md)，確認可使用哪些硬體。）控制器會透過 USB 或網路連線。

* 透過 _View -> Controller Assignment_ 選單開啟 _Controller Assignment_ 面板。（或者，也可以使用 _Laser Overview_ 面板中的 _ASSIGN LASER CONTROLLERS_ 按鈕。）

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment 面板"><figcaption></figcaption></figure>

* 面板分成兩側：左側是雷射清單，右側是可用控制器清單。如果清單中沒有看到你的雷射控制器，請按 _REFRESH_ 按鈕。如果仍然遇到問題，請參閱[疑難排解](../troubleshooting/)。
* 若要將控制器指派給雷射，請從右側點選並拖曳到左側空的雷射欄位。這會告訴 Liberation 哪一個控制器要用於哪一台雷射。（如果改變主意，也可以自由地把控制器在不同雷射之間上下拖曳。）

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="控制器清單" width="375"><figcaption></figcaption></figure>

* 如果控制器旁邊顯示綠色方塊，表示 Liberation 已成功連線到該控制器。

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>一台 Ether Dream 與一台 Helios DAC 分別指派給第 2 與第 3 台雷射</p></figcaption></figure>

{% hint style="info" %}
請注意，每次連線到控制器時，雷射都會自動解除啟用。
{% endhint %}

* 橘色方塊 🟧 表示控制器有間歇性的連線問題。這通常是網路問題造成的，請參閱[疑難排解](../troubleshooting/)。
* 紅色方塊 🟥 表示無法連線到控制器，請參閱[疑難排解](../troubleshooting/)。
* 中斷連線按鈕（X）會中斷控制器連線，但不會清除該雷射的指派設定。之後可以使用重新連線按鈕（重新整理箭頭圖示）重新連線；或者再次點擊中斷連線按鈕，以清除指派設定。
* _進階功能：_ 點擊看起來像圖表的按鈕，可開啟控制器分析面板。這是進階功能，可提供資料串流的詳細資訊，並協助排查問題。（某些控制器類型可能無法使用此選項。）
* 你可以使用重新命名按鈕（鉛筆）把這個控制器改成任何你想要的名稱。建議使用容易對應到特定硬體的命名方式。如果控制器內建在某台雷射中，可以依照該雷射命名，例如 _LaserCube Ultra #1_ 或 _Triton T5 #3_。這些名稱會儲存在你的 Liberation 安裝中，之後都會顯示出來；這對快速辨識雷射非常有幫助。

{% hint style="info" %}
小技巧：在右側的控制器上**按兩下**，即可自動指派到左側下一個可用的雷射。如果有很多台雷射要指派，這可以節省不少時間！
{% endhint %}

你可以使用 _DISCONNECT ALL_ 和 _RECONNECT ALL_ 按鈕，快速重設所有連線。這在遇到網路問題時很實用。
