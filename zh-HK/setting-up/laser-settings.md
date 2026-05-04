---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Laser output 設定面板

使用選單 _View -> Laser Output Settings_ 開啟 _Laser output_ 設定面板。

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

這會顯示目前所選激光機的設定，你可以透過以下方式切換要調整的激光機：

* 在 _Laser overview_ 面板中按其編號按鈕
* 使用鍵盤上的數字鍵，1 至 0 會開啟激光機 1 至 10
* 使用 `Tab` 鍵在各激光機之間循環切換（`Shift + Tab` 會向後切換）。

在此面板頂部，你會看到：

* 一個編號按鈕——按一下可 arm/disarm 這部激光機。激光機處於 armed 狀態時，按鈕會顯示紅色。
* 只適用於這部激光機的 _Brightness_ 滑桿。請注意，此設定會與全域亮度合併計算。
* _Test Pattern_ 開關及圖案選擇器。你可以用它為這部激光機指定特定測試圖案。（這些控制項也會同步顯示在 Output view 工具列中）。

### 輸出方向／鏡像校正

以下項目用於校正你的激光機設定，令它在 Liberation 中有一致的表現。

* **Flip horizontal / vertical**——這些選項可讓你校正激光機的輸出

{% hint style="info" %}
除非你的激光機接線不正確，或機背的 X/Y 翻轉按鈕未正確設定，否則不應需要更改水平／垂直翻轉設定。如果你想讓某個 clip 的輸出翻轉，可以直接在該 clip 上設定。
{% endhint %}

* **Orientation**——如果你的激光機是側向或倒轉安裝，可用此設定校正旋轉方向。
* **Fine position adjustments**——可用於校正非常輕微的位移／旋轉。這是為修正激光機放置過夜或長時間後出現的漂移／沉降而設。

{% hint style="info" %}
請注意，方向／鏡像校正不會改變 3D Visualiser 中的任何內容；它們應用於校正實際激光機的輸出，使其與 3D Visualiser 中顯示的內容一致！
{% endhint %}

### 複製激光機設定

請參閱 [複製激光機設定](laser-settings.md#copy-laser-settings "mention")。

### 掃描器設定

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed 設定決定掃描器移動的速度。

{% hint style="danger" %}
雖然預設設定相當保守，但如果驅動速度過快，仍然可能損壞掃描器。請小心使用，尤其是在提高速度時。
{% endhint %}

{% hint style="info" %}
此 Speed 設定不會改變 point rate，而是調整這些點之間的分佈距離。如需更多資料，請參閱 [Liberation 如何產生激光內容](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

光束在掃描器帶動下移動時，會改變顏色並開關輸出，而這兩件事通常不會完全同步。調整此設定可令它們重新對齊。

{% hint style="info" %}
這有時稱為 _blank shift_，但我個人較喜歡 _scanner sync_ 這個說法——它稍為準確一點，因為它調整的是所有色彩變化相對於掃描器移動的時間。
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>激光「尾巴」——Colour shift 未正確設定</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>沒有激光「尾巴」！Colour shift 良好！</p></figcaption></figure></div>

如果你在激光輸出上看到細小的「尾巴」，很可能是 Scanner sync 需要調整。如果無論怎樣調整仍然出現尾巴，通常表示你驅動掃描器／激光驅動器的速度超出其可承受範圍。請嘗試降低掃描器速度。

#### 掃描器預設設定

使用此項選擇預先設計好的掃描器設定。預設選項通常已經足夠，所以除非你的掃描器特別差（或特別好），否則不應需要更改此設定。如果你想深入了解，請參閱 [掃描器預設設定](../advanced/scanner-presets.md "mention")

#### 色彩校準

你可以使用此系統校正激光機的亮度曲線和白平衡。請參閱 [色彩校準](../advanced/colour-calibration.md "mention")

#### 進階設定

你應該不需要調整這些設定，但如果你好奇，可參閱 [進階激光設定](../advanced/advanced-laser-settings.md "mention")
