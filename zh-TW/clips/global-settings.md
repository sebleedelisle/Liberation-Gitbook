---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Global Transformations（全域變形）

除了 Clip 變形（shift x/y、scale x/y）之外，還有 Global Transformations，會套用到你執行的每一個 Clip。開啟 _Global Transformations_ 面板即可查看這些設定。（這個面板通常會在 _Clip Settings_ 旁邊的分頁中）。

預設情況下，只要沒有任何 Clip 還在播放，這些設定都會被重設。你可以使用 _Global Transformations_ 面板底部的 _AUTO RESET_ 按鈕停用這個重設行為。

{% hint style="info" %}
請注意，Global Transformations 不會影響 Canvas 中的任何內容，只會影響 Beam 和 DMX zones。
{% endhint %}

### Scale X/Y

水平與垂直縮放。除非按住 `Shift`，否則這兩個值會鎖定在一起。預設也會對應到 APC40 Device Control 旋鈕 4 和 8，並顯示在 Clip Deck 右側的面板中。

### Shift X/Y

水平與垂直位移。會將所有內容往水平方向／垂直方向平移。

### Spin

讓所有內容以中心點為軸旋轉。正值會順時針旋轉，負值會逆時針旋轉。你會看到這個設定會影響 _Rotation_ 變形。預設會對應到 APC40 Device Control 旋鈕 3，並顯示在 Clip Deck 右側的面板中。

### Spin 3D

讓所有內容繞著 Y 軸旋轉（也就是位於中心的垂直線）。你會看到這個設定會影響 _Rotation3D_ 變形。預設會對應到 APC40 Device Control 旋鈕 7，並顯示在 Clip Deck 右側的面板中。

### Rotation

以中心點為軸的旋轉，數值單位為度。

### Rotation 3D

繞著 Y 軸旋轉（也就是位於中心的垂直線），數值單位為度。

### Auto reset

啟用後，只要目前正在執行的所有 Clips 都被停用，就會重設所有 Global Transformations。這樣你下次執行 Clip 時，就不用擔心出現意外的設定！
