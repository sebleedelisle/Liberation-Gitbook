---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube 宣傳圖片由 Wicked Lasers 提供</p></figcaption></figure>

Wicked Lasers 的 [LaserCube](https://www.laseros.com/lasercube/) 是一款極為小巧、以電池供電的雷射設備，提供多種不同功率配置。由於智慧型手機 App 容易上手，它很受玩家歡迎；而近期機型的能力也已足以用於專業演出。

手機 App 稱為 LaserOS（也有桌面版），可免費下載，操作起來很有趣，對多數使用者來說也已相當夠用。但如果你要執行多台雷射的大型演出，就需要更專門、更強大的工具——這正是 Liberation 派上用場的地方。

### 連接 LaserCube

早期的 LaserCube 透過 USB 控制，但目前的機型都內建網路控制器。這些以網路控制的 Cube 稱為「LaserCube Wifi」。Liberation 支援這兩種類型的 LaserCube\*，不論是透過 USB 或網路連接都可以使用。

\*（LaserCube 網路通訊協定支援自 0.7.3 版開始提供）

### USB LaserCube

使用 micro USB 線將 LaserCube 連接到電腦，然後在 _Controller Assignment_ 面板中尋找它（請參閱 [Controller Assignment](../setting-up/controller-assignment.md "mention")）。如果沒有自動顯示，請按下 _REFRESH_ 按鈕。

### 網路 LaserCube「Wifi」

{% hint style="danger" %}
雖然「Wifi」Cube 的設計可透過無線網路操作，但不建議這麼做，因為很可能會出現中斷與異常。請改用 RJ45 接孔將 LaserCube 連接到有線網路，就像連接 Ether Dream 一樣。
{% endhint %}

將 LaserCube 連接到你的有線網路。

將 LaserCube 設為「LAN Client」模式，並確認網路中有路由器。LaserCube 會從路由器取得 IP 位址，接著應該就會出現在 _Controller Assignment_ 面板中。（請參閱 [Controller Assignment](../setting-up/controller-assignment.md "mention")）。

{% hint style="info" %}
你也可以不使用路由器來建立網路，並為所有裝置設定固定 IP 位址；這在活動產業非常常見。就我個人而言，我偏好在網路中加入路由器，也會建議不太熟悉網路設定的人採用這個方式。

路由器會動態分配 IP 位址給所有裝置，我覺得這樣比較簡單，也比較不容易出錯。
{% endhint %}

{% hint style="danger" %}
不同於 Ether Dream，_**LaserCube 在遇到緩衝區 underrun、封包遺失，或其他損壞／錯誤資料時，不會關閉雷射輸出**_。

相反地，它會從中斷的位置繼續執行；在某些情況下，這可能會導致實際雷射光束穿過不在任何 zone 內的區域，更糟的是，甚至會穿過軟體中的 mask。

我正在和 LaserCube 的設計者／程式開發者討論，希望他們未來能透過韌體更新處理這個問題。但在此之前，你必須確保任何不希望雷射照射到的地方，都已用實體方式遮擋。

公平地說，你本來就很可能應該這麼做；不過我自己會使用軟體中的 mask 來保護攝影機與投影機。所以請注意：使用 LaserCube 網路通訊協定時，這樣做會比使用 Ether Dream 更危險（Ether Dream 只要發生任何錯誤或資料遺失，就會進入安全停止模式）。

另外，我前面已經說過，但還是要再提醒一次：**請使用有線連線連接 LaserCube**。Wifi 撐不住，還會讓這個問題變得更嚴重。
{% endhint %}
