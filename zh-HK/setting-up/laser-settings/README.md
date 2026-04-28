# ✅ 激光輸出設定面板

透過選單 _View -> Laser Output Settings._ 開啟 _Laser output_ 設定面板。

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

這會顯示目前所選激光機的設定，你可以用以下方式切換要設定的激光機：

* 在 _Laser overview_ 面板按其編號按鈕
* 按鍵盤上的數字鍵；1 至 0 會開啟激光機 1 - 10
* 按 `Tab` 鍵循環切換激光機（`Shift + Tab` 會反方向切換）。

在此面板頂部，你會看到：

* 一個編號按鈕 - 按一下可 arm/disarm 這部激光機。激光機已 armed 時會顯示為紅色。
* 只適用於這部激光機的 _Brightness_ 滑桿。請注意，這會與全域 brightness 合併計算。
* _Test Pattern_ 開關及圖案選擇器。這可讓你只為這部激光機選擇指定測試圖案。（這些控制項亦會同步顯示在 Output view 工具列中）。

### 輸出方向／鏡像校正

接下來的項目用於校正激光機設定，令它在 Liberation 中表現一致。

* **Flip horizontal / vertical** - 這些選項可讓你校正激光機的輸出

{% hint style="info" %}
除非你的激光機接線不正確，或機背的 X/Y flip 按鈕未正確設定，否則你不應需要更改 horizontal / vertical flip 設定。如果你想讓某個 clip 的輸出翻轉，可以直接在該 clip 上設定。
{% endhint %}

* **Orientation** - 如果你的激光機是側掛或倒掛，可用此設定校正旋轉方向。
* **Fine position adjustments** - 可用於修正非常輕微的位置偏移／旋轉。設計用途是校正激光機放置過夜或長時間後出現的漂移／沉降。

{% hint style="info" %}
請注意，orientation / mirroring 校正不會改變 3D Visualiser 中的任何內容；它們應用於校正實際激光輸出，使其與 3D Visualiser 中的內容一致！
{% endhint %}

### 複製激光設定

請參閱 [複製激光設定](./#copy-laser-settings)。

### Scanner 設定

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed 設定決定 scanners 的移動速度。

{% hint style="danger" %}
雖然預設設定相當保守，但如果推動速度過快，仍然可能損壞 scanners。請小心使用，特別是在提高速度時。
{% endhint %}

{% hint style="info" %}
此 Speed 設定不會改變 point rate，而是調整這些點的分佈疏密。詳情請參閱 [Liberation 如何產生激光內容](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync（Colour shift / blank shift）**

光束在 scanners 移動期間會改變顏色並開關，而這兩件事通常不會完全同步。調整此設定可令它們重新對齊。

{% hint style="info" %}
這有時稱為 _blank shift_，但我個人較喜歡 _scanner sync_ 這個說法——它更準確一點，因為此設定調整的是所有顏色變化相對於 scanner movement 的時間。
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>激光「尾巴」- Colour shift 未正確設定</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>沒有激光「尾巴」！Colour shift 設定良好！</p></figcaption></figure></div>

如果你在激光輸出上看到小小的「尾巴」，很可能是 scanner sync 需要調整。如果無論如何調整仍然出現尾巴，通常表示你推動 scanners／laser drivers 的速度超出它們可處理的範圍。請嘗試降低 scanner speed。

#### Scanner 預設

用此項選擇預先設計的 scanner 設定。預設選項通常已足夠，所以除非你的 scanners 特別差（或特別好），否則不需要更改此設定。如果想深入了解，請參閱 [Scanner 預設](../../advanced/scanner-presets.md)

#### 色彩校準

你可以使用此系統校正激光機的亮度曲線及白平衡。請參閱 [色彩校準](../../advanced/colour-calibration.md)

#### 進階設定

你不應需要調整這些設定；但如果你有興趣了解，請參閱 [進階激光設定](../../advanced/advanced-laser-settings.md)
