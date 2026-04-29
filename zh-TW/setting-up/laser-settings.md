---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Laser output 設定面板

使用選單 _View -> Laser Output Settings_ 開啟 _Laser output_ 設定面板。

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

這裡會顯示目前選取的雷射設定，你可以透過以下方式切換要調整的雷射：

* 在 _Laser Overview_ 面板中按下對應的編號按鈕
* 使用鍵盤上的數字鍵，1 到 0 會開啟第 1 到第 10 台雷射
* 使用 `Tab` 鍵依序切換雷射（`Shift + Tab` 會反向切換）

在這個面板的頂端，你會看到：

* 編號按鈕：按一下可啟用或停用這台雷射的輸出。雷射啟用時，按鈕會顯示為紅色。
* 只套用於這台雷射的 _Brightness_ 滑桿。請注意，這會與 Global Brightness 合併計算。
* _Test Pattern_ 開關與圖樣選擇器。這可讓你只為這台雷射選擇特定的測試圖樣。（這些控制項也會同步顯示在 Output view 工具列中。）

### 輸出方向／鏡像校正

接下來的項目可用來校正雷射的設定，讓它在 Liberation 中的行為保持一致。

* **Flip horizontal / vertical**：這些選項可用來校正雷射的輸出方向

{% hint style="info" %}
除非你的雷射接線錯誤，或機背的 X/Y 翻轉按鈕設定不正確，否則通常不需要更改水平／垂直翻轉設定。如果你只想讓特定 Clip 的輸出翻轉，可以直接在該 Clip 上設定。
{% endhint %}

* **Orientation**：如果雷射是側掛或倒掛安裝，可以用這個設定校正旋轉方向。
* **Fine position adjustments**：可用來校正非常輕微的位置偏移或旋轉。這項功能設計用於修正雷射放置一夜或長時間使用後產生的漂移／沉降。

{% hint style="info" %}
請注意，方向／鏡像校正不會改變 3D Visualiser 中的任何內容；它們應該用來校正實際雷射輸出，使其符合 3D Visualiser 中的顯示！
{% endhint %}

### 複製雷射設定

請參閱[複製雷射設定](laser-settings.md#copy-laser-settings)。

### 掃描器設定

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

速度設定會決定掃描器移動的速度。

{% hint style="danger" %}
雖然預設值相當保守，但如果驅動速度太快，仍然可能損壞掃描器。請小心使用，特別是在提高速度時。
{% endhint %}

{% hint style="info" %}
這個速度設定不會改變點率，而是調整這些點之間的分布距離。如需更多資訊，請參閱 [Liberation 如何產生雷射內容](../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync（顏色偏移／消隱偏移）**

當掃描器移動光束時，光束會改變顏色並開關輸出；這兩件事通常不會完全同步。調整這項設定，可讓它們重新對齊。

{% hint style="info" %}
這有時稱為 _blank shift_，但我個人比較偏好 _scanner sync_ 這個名稱，因為它更準確一點：它調整的是所有顏色變化與掃描器移動之間的時序。
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>雷射「尾巴」：Colour shift 未正確設定</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>沒有雷射「尾巴」！Colour shift 設定良好！</p></figcaption></figure></div>

如果你在雷射輸出上看到小小的「尾巴」，很可能是因為 scanner sync 需要調整。如果不管怎麼調尾巴都仍然出現，你很可能是讓掃描器或雷射驅動器以超過其負荷的速度運作。請嘗試降低掃描器速度。

#### 掃描器預設值

使用這個選項可選擇預先設計好的掃描器設定。預設選項通常就很好，所以除非你的掃描器特別差（或特別好），否則應該不需要更改這項設定。如果你想深入了解，請參閱[掃描器預設值](../advanced/scanner-presets.md)

#### 顏色校正

你可以使用這個系統校正雷射的亮度曲線與白平衡。請參閱[顏色校正](../advanced/colour-calibration.md)

#### 進階設定

你應該不需要動到這些設定；但如果你有興趣，請參閱[進階雷射設定](../advanced/advanced-laser-settings.md)
