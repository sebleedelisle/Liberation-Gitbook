---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube 宣傳圖片由 Wicked Lasers 提供</p></figcaption></figure>

Wicked Lasers 的 [LaserCube](https://www.laseros.com/lasercube/) 是一款極之細小、以電池供電的雷射裝置，提供多種不同功率配置。由於智能手機 app 容易使用，它很受業餘玩家歡迎；而近期型號的性能亦足以用於專業演出。

手機 app（名為 LaserOS，亦有桌面版）可免費下載，玩起來很有趣，對大部分用戶來說已經足夠。不過，如果你要處理較大型、包含多部雷射的演出，就需要更專門、更強大的工具——這正是 Liberation 的用途。

### 連接至 LaserCube

早期 LaserCube 透過 USB 控制，但現行型號全部都有內置網絡控制器。這些網絡控制的 cube 稱為「LaserCube Wifi」。Liberation 支援兩種類型的 LaserCube\*，不論是透過 USB 還是網絡連接。

\*（LaserCube 網絡協議支援於 0.7.3 版本加入）

### USB LaserCube

用 micro USB 線將 LaserCube 連接到電腦，然後在 _Controller Assignment_ panel 中尋找它（見 [控制器分配](../setting-up/controller-assignment.md "mention")）。如果它沒有自動出現，請按 _REFRESH_ 按鈕。

### 網絡 LaserCube「Wifi」

{% hint style="danger" %}
雖然「Wifi」cube 設計上可透過無線網絡操作，但不建議這樣做，因為很可能會出現斷線和 glitches。請改用 RJ45 插座，將 LaserCube 連接到有線網絡，就像連接 Ether Dream 一樣。
{% endhint %}

將 LaserCube 連接到你的有線網絡。

將 LaserCube 設定為 "LAN Client" 模式，並確保網絡上有一部路由器。LaserCube 會從路由器取得 IP 地址，然後應該會在 _Controller Assignment_ panel 中出現。（見 [控制器分配](../setting-up/controller-assignment.md "mention")）。

{% hint style="info" %}
你亦可以在沒有路由器的情況下建立網絡，並為所有裝置設定固定 IP 地址；這在活動製作行業十分常見。就我個人而言，我較喜歡在網絡中加入路由器，亦會向網絡經驗較少的人建議這個做法。

路由器會為所有裝置動態分配 IP 地址，我覺得這樣更簡單，亦較少出錯。
{% endhint %}

{% hint style="danger" %}
與 Ether Dream 不同，如果 LaserCube 遇到 buffer under-run、封包遺失或其他損壞／錯誤資料，_**LaserCube 不會將雷射 blank**_。

相反，它們只會由中斷的位置繼續輸出；在某些情況下，這可能令實際光束穿過不在 zones 內的範圍，更嚴重的是，甚至會切過軟件 masks。

我正在與 LaserCube 的設計師／程式開發人員溝通，希望他們日後可透過 firmware update 處理這個問題；但在此之前，你必須確保以實體方式遮擋所有不希望雷射到達的位置。

公平來說，你其實本來就應該這樣做；不過我自己會使用軟件 masks 來保護攝影機和投影機。因此請注意，使用 LaserCube 網絡協議這樣做，比使用 Ether Dream 更危險（Ether Dream 一旦出現任何錯誤或資料遺失，便會立即進入安全停止模式）。

另外，我已經說過，但還是要再提醒一次：**請使用有線連接到你的 LaserCube**。Wifi 並不足夠，而且會令這個問題更加嚴重。
{% endhint %}
