# ✅ 雷射輸出設定面板

從選單 _View -> Laser Output Settings_ 開啟 _Laser output_ 設定面板。

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

這會顯示目前選取雷射的設定，你可以透過以下方式切換要設定的雷射：

* 在 _Laser overview_ 面板中按它的編號按鈕
* 按鍵盤上的數字鍵；1 到 0 會開啟雷射 1 - 10
* 按 `Tab` 鍵在各雷射之間循環切換（`Shift + Tab` 會反向切換）。

在此面板頂端，你會看到：

* 一個編號按鈕 — 按一下可讓此雷射進入或解除待輸出狀態。雷射處於待輸出狀態時會顯示紅色。
* 只套用於此雷射的 _Brightness_ 滑桿。請注意，這會與 Global Brightness 合併計算。
* _Test Pattern_ 開關與圖案選擇器。這可讓你只為此雷射選擇特定的 Test Pattern。（這些控制項也會同步出現在 Output view 工具列中）。

### 輸出方向／鏡像校正

接下來的項目用來校正雷射的設定，讓它在 Liberation 中的行為保持一致。

* **Flip horizontal / vertical** - 這些選項可用來校正雷射輸出

{% hint style="info" %}
除非你的雷射配線不正確，或背面的 X/Y 翻轉按鈕沒有正確設定，否則通常不需要更改水平／垂直翻轉設定。如果你想讓某個 Clip 的輸出翻轉，可以直接在該 Clip 上設定。
{% endhint %}

* **Orientation** - 如果你的雷射是側掛或倒掛，可以用此設定校正旋轉方向。
* **Fine position adjustments** - 可用來校正非常細微的位移／旋轉。設計用途是修正雷射放置過夜或長時間後產生的漂移／沉降。

{% hint style="info" %}
請注意，方向／鏡像校正不會改變 3D Visualiser 中的任何內容；它們應用來校正實際雷射的輸出，使其符合 3D Visualiser 中顯示的結果！
{% endhint %}

### 複製雷射設定

請參閱 [複製雷射設定](./#copy-laser-settings)。

### 掃描器設定

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **速度**

速度設定會決定掃描器移動的快慢。

{% hint style="danger" %}
雖然預設值相當保守，但如果驅動速度過快，仍然可能損壞掃描器。請謹慎操作，尤其是在提高速度時。
{% endhint %}

{% hint style="info" %}
此速度設定不會改變點率，而是調整這些點的分布間距。如需更多資訊，請參閱 [Liberation 如何產生雷射內容](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **掃描器同步（顏色偏移／消隱偏移）**

光束在掃描器移動時會變換顏色並開關，而這兩件事通常不會彼此完全同步。調整此設定可讓它們重新對齊。

{% hint style="info" %}
這有時稱為 _blank shift_，但我個人比較偏好 _scanner sync_ 這個詞，因為它更準確一些：它調整的是所有顏色變化相對於掃描器移動的時序。
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>雷射「尾巴」— 顏色偏移未正確設定</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>沒有雷射「尾巴」！顏色偏移設定良好！</p></figcaption></figure></div>

如果你在雷射輸出上看到小小的「尾巴」，很可能是因為需要調整掃描器同步。如果不論怎麼調整尾巴都仍然出現，表示你驅動掃描器／雷射驅動器的速度可能超過了它們能承受的範圍。請嘗試降低掃描器速度。

#### 掃描器預設值

用此項目選擇預先設計好的掃描器設定。通常預設選項就可以正常使用，所以除非你的掃描器特別差（或特別好），否則不需要更改此設定。如果你想深入了解，請參閱 [掃描器預設值](../../advanced/scanner-presets.md)

#### 色彩校正

你可以使用此系統校正雷射的亮度曲線與白平衡。請參閱 [色彩校正](../../advanced/colour-calibration.md)

#### 進階設定

你通常不需要調整這些項目，但如果你有興趣了解，請參閱 [進階雷射設定](../../advanced/advanced-laser-settings.md)
