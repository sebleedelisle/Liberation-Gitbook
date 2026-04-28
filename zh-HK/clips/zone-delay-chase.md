---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

大家都同意，Laser 越多就越好玩；但如果所有 Laser 都做完全相同的動作，就會錯過很多創作可能性。

Zone delay 系統是一個簡單但有效的方法，可在不同 zone 之間加入變化，充分發揮多 Laser 設定的效果。它亦可用來製作較傳統的 chase 效果。

#### 運作方式

_Zone delay_ 會在各個 zone 之間為 clip 的時間加入延遲，形成一種橫掃各 zone 的效果。

在 clip 已經播放時加入 Zone delay 會非常有效；你可以使用 APC40 上的相關控制來調整程度和 pattern。（請參閱 [APC40 參考](../reference/apc40-reference.md)）。你亦可以使用 _Clip Settings_ panel。

Zone delay 設定：

* **Zone delay** - 控制套用到每個 zone 的延遲時間，以六十四分音符為單位。
* **Pattern** - 選擇 zone 的次序
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern 會根據 zone 編號運作，並假設你的 zone 是由左至右順序排列。計算 pattern 時，Zone delay 會將 canvas zone 和 DMX zone 視為不同群組。
{% endhint %}

* **Delay mode**
  1. No delay - 在 chase mode 中使用此模式
  2. Delay - 預設模式，延遲每個 zone 的時間
  3. Delay with re-trigger - 每次按 pattern 前進時，都會將 clip 重設到開頭。這配合 _Chase mode_ 使用效果不錯。
* **Chase mode** - 啟用 chase mode 後，每個 zone 會像傳統 chase 效果一樣逐一開啟和關閉。你可以使用 _Fade in, Hold,_ 和 _Fade out_ 設定來調整 chase 的外觀。這些設定是以 Zone delay 數值的比例來設定，因此數值 1 代表與 _Zone delay_ 數值指定的時間相同。這有點難用文字解釋，所以建議你親自試一試。

{% hint style="info" %}
Zone delay 亦會套用到任何正在啟用的 effect。例如，閃爍效果會在各個 zone 之間延遲，clip 內的動畫本身亦一樣會延遲。
{% endhint %}

當 clip 有任何形式的 _Zone delay_ 時，你會在 clip 右上角看到一個三點圖示。這些點會以動畫顯示該 clip 的 _Zone delay_ 類型。詳情請參閱 [Clip 按鈕上的小圖示是甚麼？](what-are-the-small-icons-on-the-clip-buttons.md)。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>表示 clip 設有 zone delay 及其模式的三點符號</p></figcaption></figure>

{% hint style="info" %}
Zone delay 是屬於每個 clip 的設定，並非全域設定；它是 clip 創作設計的一部分。
{% endhint %}
