---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 全域變換

除了 Clip 變換（shift x/y、scale x/y）之外，還有會套用到你執行的每個 Clip 的 Global Transformations。開啟 _Global Transformations_ 面板即可查看。（此面板通常會與 _Clip Settings_ 並列在同一組分頁中）。

預設情況下，只要沒有任何 Clip 正在播放，所有這些設定都會立即重設。你可以使用 _Global Transformations_ 面板底部的 _AUTO RESET_ 按鈕停用這個自動重設行為。

{% hint style="info" %}
請注意，Global Transformations 不會影響 Canvas 內的任何內容，只會影響 Beam 和 DMX zones
{% endhint %}

### Scale X/Y

水平及垂直縮放。除非你按住 `Shift`，否則這兩個數值會鎖定在一起。預設情況下，這些設定亦會對應到 APC40 Device Control 旋鈕 4 和 8，並顯示在 Clip Deck 右側的情境 Parameters 面板中。

### Shift X/Y

水平及垂直位移。將所有內容向水平／垂直方向平移。

### Spin

將所有內容圍繞中心旋轉。正數值會順時針旋轉，負數值會逆時針旋轉。你會看到此設定會影響 _Rotation_ 變換。預設情況下，此設定會對應到 APC40 Device Control 旋鈕 3，並顯示在 Clip Deck 右側的情境 Parameters 面板中。

### Spin 3D

將所有內容圍繞 Y 軸旋轉（即位於中心的垂直線）。你會看到此設定會影響 _Rotation3D_ 變換。預設情況下，此設定會對應到 APC40 Device Control 旋鈕 7，並顯示在 Clip Deck 右側的情境 Parameters 面板中。

### Rotation

圍繞中心旋轉，數值以度為單位。

### Rotation 3D

圍繞 Y 軸旋轉（即位於中心的垂直線），數值以度為單位。

### Auto reset

啟用後，只要所有目前正在執行的 Clip 都被停用，所有 Global Transformations 便會重設。這樣你下次執行 Clip 時，就可以確保不會出現任何意料之外的效果！
