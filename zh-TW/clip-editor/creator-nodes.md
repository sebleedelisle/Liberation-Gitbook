---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

建立單一光點 / 光束。

* **Render profile** - 請參閱 [Render profile](fundamentals/render-profile.md "mention")
* **Colour** - 光點的顏色。請參閱[顏色設定與 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 與 **y** position - 請參閱[座標系統](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

建立一條線 / 光片。

* **Render profile** - 請參閱 [Render profile](fundamentals/render-profile.md "mention")
* **Size** - 線段的長度
* **Colour** - 線段的顏色。請參閱[顏色設定與 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 與 **y** position - 請參閱[座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 線段的角度，單位為度
* **resolution** - 請參閱[解析度](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ 決定線段的起點與旋轉中心
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

建立一個圓形 / 圓錐光束。

* **Render profile** - 請參閱 [Render profile](fundamentals/render-profile.md "mention")
* **radius** - 圓形的半徑
* **Colour** - 圓形的顏色。請參閱[顏色設定與 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 與 **y** position - 請參閱[座標系統](fundamentals/co-ordinate-system.md "mention")
* **resolution** - 請參閱[解析度](fundamentals/resolution.md "mention")
* **Fill state** - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

建立等邊多邊形，例如三角形、正方形、五邊形等。

* **Render profile** - 請參閱 [Render profile](fundamentals/render-profile.md "mention")
* **size** - 從中心到每個角的距離
* **Colour** - 多邊形的顏色。請參閱[顏色設定與 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 與 **y** position - 請參閱[座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 圖形的旋轉角度，單位為度
* **resolution** - 請參閱[解析度](fundamentals/resolution.md "mention")
* **Fill state** - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

載入 SVG 檔案以使用自訂圖形。

{% hint style="warning" %}
Liberation 相容於 _SVGTiny_ 格式。建議使用 InkScape，但大多數向量繪圖應用程式都能匯出此格式。匯出前請務必將所有文字轉換為圖形。Liberation 會算繪描邊，也可以選擇將填色作為 masks 使用。請確認線條不是黑色，否則在沒有顏色修改器時會看不見！
{% endhint %}

* **Import SVG** - 從磁碟載入 SVG 檔案。

{% hint style="info" %}
SVG 載入後，內容會被轉換並儲存在 clip 內，因此不需要保留對該檔案的參照，除非之後想變更 mask 設定。
{% endhint %}

* **Use fills as masks** - 會將任何有填色的圖形處理為 mask，也就是以黑色填滿。如果你的 SVG 有任何填色圖形，此選項會自動啟用；如果沒有任何填色圖形，則會停用。請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - 如果 SVG 中的圖形沒有外框，我們就無法繪製它們！此選項會為任何填色圖形加入外框（或 _stroke_）。如果你的 SVG 沒有任何描邊圖形，會自動啟用；如果沒有任何填色圖形，則會停用。
* **Invert black lines** - 如果 SVG 中所有線條都是黑色，就會看不見！此選項會將它們轉成白色。如果你的 SVG 只有黑色圖形，會自動啟用；如果沒有，則會停用。
* **Render profile** - 請參閱 [Render profile](fundamentals/render-profile.md "mention")
* **scale** - 調整 SVG 的大小。載入 SVG 時會自動計算此值（以確保影像可見），之後也可以手動編輯。
* **x** 與 **y** position - 請參閱[座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 影像的旋轉角度，單位為度
* **resolution** - 請參閱[解析度](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

從一系列 SVG 檔案建立動畫。

* **Import SVG Sequence** - 選擇包含所有 SVG 檔案的資料夾。請注意，檔案會依英數順序載入。

{% hint style="info" %}
SVG 序列載入後，內容會被轉換並儲存在 clip 內，因此不需要保留對這些檔案的參照，除非之後想變更 mask 設定。
{% endhint %}

* **Use fills as masks** - 會將任何有填色的圖形處理為 mask，也就是以黑色填滿。如果你的任何 SVG 有填色圖形，此選項會自動啟用；如果全部都沒有填色圖形，則會停用。請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - 如果 SVG 中的圖形沒有任何外框，我們就無法繪製它們！此選項會為任何填色圖形加入外框（或 _stroke_）。如果你的 SVG 沒有任何描邊圖形，會自動啟用；如果全部都沒有填色圖形，則會停用。
* **Invert black lines** - 如果 SVG 中所有線條都是黑色，就會看不見！此選項會將它們轉成白色。如果你的 SVG 只有黑色圖形，會自動啟用；如果沒有，則會停用。
* **Render profile** - 請參閱 [Render profile](fundamentals/render-profile.md "mention")
* **scale** - 調整影像大小。
* **x** 與 **y** position - 請參閱[座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 影像的旋轉角度，單位為度
* **resolution** - 請參閱[解析度](fundamentals/resolution.md "mention")
* **speed** - 整段動畫的持續時間，單位為小節。
* **time per frame** - 啟用後，持續時間會套用到每一格，而不是整段動畫。所以如果 _speed_ 設為 ¼，每一格就是 1 拍。
* **animation direction** -
  * _FORWARDS_ - 動畫向前播放，然後循環回到開頭
  * _BACKWARDS_ - 動畫向後播放，然後循環回到結尾
  * _PINGPONG_ - 動畫向前播放後再向後播放，並持續循環
  * _MANUAL_ - 目前影格由 _position manual_ 設定
* **position manual** - 設定目前影格；0% 是第一格，100% 是最後一格。可以手動設定，也可以使用外部振盪器設定。
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

使用 TrueType 或 OpenType 字型建立文字。

* **Text** - 在這裡輸入想要的文字
* **Font** - 選擇想要使用的字型

{% hint style="info" %}
若要在 Liberation 中加入更多字型，請將 .ttf 或 .otf 檔案複製到 Liberation 工作資料夾內的 `data/fonts` 資料夾，然後重新啟動 Liberation。
{% endhint %}

* **Render profile** - 請參閱 [Render profile](fundamentals/render-profile.md "mention")
* **horizontal alignment** - 選擇 _LEFT_、_CENTRE_ 或 _RIGHT_ 來設定文字對齊方式。
* **Fill state** - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - 文字大小
* **monospace** - 以相同寬度繪製每個字元。這對計時器和計數器很有用，因為數字變化時文字不會左右跳動。
* **character spacing** - 調整字元之間的間距。增加可讓字距更寬，減少可讓文字更緊密。
* **colour -** 請參閱[顏色設定與 HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** 與 **y** position - 請參閱[座標系統](fundamentals/co-ordinate-system.md "mention")
* **rotation** - 影像的旋轉角度，單位為度
* **resolution** - 請參閱[解析度](fundamentals/resolution.md "mention")
* **reveal** - 用來逐字顯示文字。此值介於 0 到 50% 時，文字會由左到右逐漸出現；介於 50% 到 100% 時，文字會由左到右消失。你可以將振盪器連接到這個 socket 來製作動畫。
* **reveal by word** - 啟用後，_reveal_ 會以逐字詞為單位運作，而不是逐字元。
* **countdown** - 以倒數取代輸入的文字。倒數到零時，會顯示一般的 **Text** 值。
* **use seconds** - 以實際秒數計數。關閉時，倒數會以節拍為基準：兩拍計為一秒，因此 120bpm 會符合實際秒數。
* **show minutes/seconds** - 以分和秒顯示剩餘時間。如果超過一小時，也會包含小時。
* **countdown to date/time** - 倒數到指定的 UTC 日期與時間，而不是從某個數字開始倒數。
* **countdown datetime** - 在 **countdown to date/time** 開啟時，設定 UTC 目標日期/時間。
* **start number** - 在 **countdown to date/time** 關閉時使用的起始數字。
* _MOVE TO FRONT / MOVE TO BACK_ - 請參閱[填色、masks 與深度排序](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
如果字型下拉式選單已開啟，可使用向上與向下方向鍵逐一切換可用字型。
{% endhint %}
