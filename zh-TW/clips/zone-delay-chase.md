---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

我們都同意，雷射燈越多越有趣；但如果它們全都做完全一樣的事，就少了很多創作可能性。

Zone delay 系統是一個簡單但很有效的方法，可以在不同 zones 之間加入變化，讓多雷射燈配置發揮更好的效果。它也可以用來製作較傳統的 chase 效果。

#### 運作方式

_Zone delay_ 會在每個 zone 的 Clip 時間點上加入延遲，形成一種掃過各個 zones 的效果。

在 Clip 已經播放時加入 zone delay 會很有效果；你可以使用 APC40 上的相關控制來調整程度與 pattern。（請參閱 [APC40 參考](../reference/apc40-reference.md "mention")）。或者，你也可以使用 _Clip Settings_ 面板。

Zone delay 設定：

* **Zone delay** - 控制套用到每個 zone 的延遲時間量，以 64 分音符為單位。
* **Pattern** - 選擇 zone 的順序
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern 是依照 zone 編號運作，並假設你的 zones 是由左到右依序排列。在計算 patterns 時，Zone delay 會將 canvas zones 與 DMX zones 視為不同的群組。
{% endhint %}

* **Delay mode**
  1. No delay - 在 chase mode 中使用此模式
  2. Delay - 預設模式，會延遲每個 zone 的時間點
  3. Delay with re-trigger - 每次沿著 pattern 前進時，都會將 Clip 重設回開頭。這很適合搭配 _Chase mode_。
* **Chase mode** - 開啟 chase mode 時，每個 zone 會像傳統 chase 效果一樣依序開啟與關閉。可使用 _Fade in, Hold,_ 和 _Fade out_ 設定來調整 chase 的外觀。這些設定是以 zone delay 值的比例來設定，因此數值 1 代表與 _Zone delay_ 值中指定的時間相同。這有點難用文字說明，所以我建議你直接試試看。

{% hint style="info" %}
Zone delay 也會套用到任何啟用中的 effects。舉例來說，閃爍效果除了會延遲 Clip 本身的動畫，也會在各 zones 之間延遲。
{% endhint %}

當 Clip 具有任何形式的 _Zone delay_ 時，你會在 Clip 右上角看到三點圖示。這些點會以動畫顯示該 Clip 的 _Zone delay_ 樣式。更多詳細資訊請參閱 [Clip 按鈕上的小圖示是什麼？](what-are-the-small-icons-on-the-clip-buttons.md "mention")。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>表示 Clip 具有 zone delay 及其模式的三點符號</p></figcaption></figure>

{% hint style="info" %}
Zone delay 是屬於每個 Clip 的設定，並不是全域設定；它是 Clip 創意設計的一部分。
{% endhint %}
