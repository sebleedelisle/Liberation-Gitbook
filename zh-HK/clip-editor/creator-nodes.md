---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator 節點

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

建立單一光點／光束。

* **Render profile** - 請參閱 [渲染設定檔](fundamentals/render-profile.md "mention")
* **Colour** - 光點的顏色。請參閱 [顏色設定及 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 和 **y** position - 請參閱 [座標系統](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

建立一條線／光片。

* **Render profile** - 請參閱 [渲染設定檔](fundamentals/render-profile.md "mention")
* **Size** - 線的長度
* **Colour** - 線的顏色。請參閱 [顏色設定及 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 和 **y** position - 請參閱 [座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 線的角度，以度數表示
* **resolution** - 請參閱 [解像度](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ 決定線的起點及旋轉中心
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

建立圓形／錐形。

* **Render profile** - 請參閱 [渲染設定檔](fundamentals/render-profile.md "mention")
* **radius** - 圓形的半徑
* **Colour** - 圓形的顏色。請參閱 [顏色設定及 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 和 **y** position - 請參閱 [座標系統](fundamentals/co-ordinate-system.md "mention")
* **resolution** - 請參閱 [解像度](fundamentals/resolution.md "mention")
* **Fill state** - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

建立等邊多邊形，例如三角形、正方形、五邊形等。

* **Render profile** - 請參閱 [渲染設定檔](fundamentals/render-profile.md "mention")
* **size** - 從中心到每個角的距離
* **Colour** - 多邊形的顏色。請參閱 [顏色設定及 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 和 **y** position - 請參閱 [座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 形狀的旋轉角度，以度數表示
* **resolution** - 請參閱 [解像度](fundamentals/resolution.md "mention")
* **Fill state** - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

載入 SVG 檔案以使用自訂形狀。

{% hint style="warning" %}
Liberation 與 _SVGTiny_ 格式相容。建議使用 InkScape，不過大部分向量圖形應用程式都可以匯出此格式。匯出前請確保將所有文字轉換為形狀。Liberation 會渲染線條，亦可選擇將填色用作遮罩。請確保你的線條不是黑色，否則沒有 colour modifier 時就不會顯示！
{% endhint %}

* **Import SVG** - 從磁碟載入 SVG 檔案。

{% hint style="info" %}
載入 SVG 後，內容會被轉換並儲存在 clip 內，因此你不需要保留對該檔案的參照，除非之後想更改遮罩設定。
{% endhint %}

* **Use fills as masks** - 會將任何有填色的形狀處理為 mask，即以黑色填滿。如果你的 SVG 有任何填色形狀，系統會自動啟用此選項。如果沒有填色形狀，則會停用。請參閱 [填色、mask 及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - 如果 SVG 中的形狀沒有外框，我們就無法繪製它們！此選項會為任何填色形狀加入外框（或 _stroke_）。如果你的 SVG 沒有任何帶 stroke 的形狀，系統會自動啟用此選項。如果沒有任何填色形狀，則會停用。
* **Invert black lines** - 如果 SVG 中所有線條都是黑色，你就看不到它們！此選項會將它們變成白色。如果你的 SVG 只有黑色形狀，系統會自動啟用；如果沒有，則會停用。
* **Render profile** - 請參閱 [渲染設定檔](fundamentals/render-profile.md "mention")
* **scale** - 調整 SVG 的大小。載入 SVG 時會自動計算此值（以確保圖像可見），之後亦可手動編輯。
* **x** 和 **y** position - 請參閱 [座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 圖像的旋轉角度，以度數表示
* **resolution** - 請參閱 [解像度](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

從一系列 SVG 檔案建立動畫。

* **Import SVG Sequence** - 選擇包含所有 SVG 檔案的資料夾。請注意，檔案會按英文字母及數字順序載入。

{% hint style="info" %}
載入 SVG 序列後，內容會被轉換並儲存在 clip 內，因此你不需要保留對這些檔案的參照，除非之後想更改遮罩設定。
{% endhint %}

* **Use fills as masks** - 會將任何有填色的形狀處理為 mask，即以黑色填滿。如果你的任何 SVG 有填色形狀，系統會自動啟用此選項。如果全部都沒有填色形狀，則會停用。請參閱 [填色、mask 及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - 如果 SVG 中的形狀沒有任何外框，我們就無法繪製它們！此選項會為任何填色形狀加入外框（或 _stroke_）。如果你的 SVG 沒有任何帶 stroke 的形狀，系統會自動啟用此選項。如果全部都沒有填色形狀，則會停用。
* **Invert black lines** - 如果 SVG 中所有線條都是黑色，你就看不到它們！此選項會將它們變成白色。如果你的 SVG 只有黑色形狀，系統會自動啟用；如果沒有，則會停用。
* **Render profile** - 請參閱 [渲染設定檔](fundamentals/render-profile.md "mention")
* **scale** - 調整圖像大小。
* **x** 和 **y** position - 請參閱 [座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 圖像的旋轉角度，以度數表示
* **resolution** - 請參閱 [解像度](fundamentals/resolution.md "mention")
* **speed** - 整段動畫的持續時間，以小節為單位。
* **time per frame** - 如果啟用此設定，持續時間會套用到每一格，而不是整段動畫。所以如果 _speed_ 設為 ¼，每一格就會是 1 拍。
* **animation direction** -
  * _FORWARDS_ - 動畫向前播放，然後循環返回開頭
  * _BACKWARDS_ - 動畫向後播放，然後循環返回結尾
  * _PINGPONG_ - 動畫向前播放再向後播放，並循環重複
  * _MANUAL_ - 目前影格由 _position manual_ 設定指定
* **position manual** - 設定目前影格；0% 是第一格，100% 是最後一格。可手動設定，或使用外部 oscillator 設定。
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

使用 TrueType 或 OpenType 字體建立文字。

* **Text** - 在這裡輸入你想要的文字
* **Font** - 選擇你想使用的字體

{% hint style="info" %}
如要為 Liberation 加入更多字體，請將 .ttf 或 .otf 檔案複製到 Liberation 工作資料夾內的 `data/fonts` 資料夾，然後重新啟動 Liberation。
{% endhint %}

* **Render profile** - 請參閱 [渲染設定檔](fundamentals/render-profile.md "mention")
* **horizontal alignment** - 選擇 _LEFT_、_CENTRE_ 或 _RIGHT_ 來設定文字對齊方式。
* **Fill state** - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - 文字大小
* **monospace** - 以相同寬度繪製每個字元。這對計時器和計數器很有用，因為數字變更時文字不會左右跳動。
* **character spacing** - 調整字元之間的間距。增加數值可令字距更寬，減少數值則可收緊文字。
* **colour -** 請參閱 [顏色設定及 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 和 **y** position - 請參閱 [座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 圖像的旋轉角度，以度數表示
* **resolution** - 請參閱 [解像度](fundamentals/resolution.md "mention")
* **reveal** - 用來逐步顯示文字，每次顯示一個字元。當此值介乎 0 至 50% 時，文字會由左至右逐漸出現。當介乎 50% 至 100% 時，文字會由左至右消失。你可以將 oscillator 連接到此 socket 來製作動畫。
* **reveal by word** - 啟用後，_reveal_ 會逐字運作，而不是逐字元運作。
* **countdown** - 以倒數取代輸入的文字。當倒數到零時，會顯示正常的 **Text** 值。
* **use seconds** - 以實際秒數計算。關閉此選項時，倒數會以拍子為基準：兩拍等於一秒，因此 120bpm 會對應實際秒數。
* **show minutes/seconds** - 以分鐘和秒顯示剩餘時間。如果超過一小時，亦會包含小時。
* **countdown to date/time** - 倒數至指定的 UTC 日期和時間，而不是從某個數字開始倒數。
* **countdown datetime** - 在 **countdown to date/time** 開啟時，設定 UTC 目標日期／時間。
* **start number** - 在 **countdown to date/time** 關閉時使用的起始數字。
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱 [填色、遮罩及深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
如果字體下拉選單已開啟，可使用上、下方向鍵逐一切換可用字體。
{% endhint %}
