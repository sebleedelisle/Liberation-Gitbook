---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ 間歇性／閃爍輸出

開啟 _Laser Overview_ 面板，查看出現問題的雷射旁邊的連線燈號。

**如果連線燈號不是持續綠色：**\
即表示你可能遇到網絡或 CPU 效能問題：

**網絡效能 -**

* 確保你沒有連接到 Wi-Fi 網絡。你應該一律使用有線連接。確保作業系統優先使用有線網絡而非 Wi-Fi；如果不確定，請停用 Wi-Fi
* 檢查你的網絡轉接器，並嘗試使用另一個 USB-C 轉接器
* Windows 用戶：檢查／更新你的網絡驅動程式，並執行合適的網絡測試工具
* 檢查所有線材、交換器、路由器。逐一有系統地更換並測試每條線材。
* 重新啟動所有網絡設備，包括交換器、路由器及每部 Ether Dream。

**CPU 效能**

如果你的電腦較舊或規格較低，可能太慢而無法運行 Liberation。請查看圖示列右側的幀率指示器。

那裡有兩個數字：實際幀率和目標幀率。如果實際幀率跌至 30 以下，可能會出現問題。

以下做法可能有幫助：

* 移除未使用的雷射，例如如果你只連接了一部雷射，請刪除其他雷射。
* 切換到 Output 或 Canvas view
* 關閉所有其他程式，檢查網絡防火牆設定，關閉防毒軟件、Dropbox 等。
* 降低顯示解像度，並縮小 Liberation 視窗

如果以上方法都無效，請考慮升級你的電腦。

***

**如果連線燈號是持續綠色：**

那很可能是硬件問題。這超出本手冊範圍，但你可以嘗試以下做法：

* 停用 SFS（Scan Fail Safety）系統。有些雷射具備一項功能，當掃描器停止移動時（即產生強烈的靜態光束），會停用輸出。它們有時可能過於保守／不太可靠。

{% hint style="danger" %}
停用 scan fail safety 系統時必須極度小心。強烈的靜態光束可以造成灼燒！請確保手邊有停止按鈕和滅火筒。
{% endhint %}

* 檢查 interlock 線材及系統
* 檢查控制器與雷射之間的所有線材。

[ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) 可以是排查雷射問題時非常有用的工具。
