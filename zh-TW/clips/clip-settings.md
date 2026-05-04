---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip settings

### Clip settings 面板

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip settings 面板</p></figcaption></figure>

使用 _Scale X_ 和 _Scale Y_ 變更 Clip 的輸出大小。除非按住 _SHIFT_ 鍵，否則兩者會保持連動。

使用 _Shift X_ 和 _Shift Y_ 變更 Clip 的水平與垂直位置。

_Zone Delay/Chase_ 是個很有趣的功能，所以有獨立章節介紹。[Zone Delay/Chase](zone-delay-chase.md "mention")

### Parameters panel

Clip Deck 右側的面板會顯示八個情境相關參數。選取 Clip 時，前幾個控制項是所選 Clip 的 _Shift X_、_Shift Y_ 和 _Zone Delay_，接著是全域的 _Spin_ 和 _Scale_ 控制項。

這些相同的參數也會同步到支援的 MIDI 控制器。如果沒有選取 Clip，Clip 專用的欄位會是空白。如果按住群組按鈕，前兩個控制項會改為該群組的淡入與淡出時間。

### 鎖定 Clips

如果 Clip 被鎖定，就無法移動或刪除。若要鎖定 Clip，請使用右鍵選單中的 _Locked_ 核取方塊。在 Clip settings 面板中，你會看到更多選項。

* _UNLOCK ALL -_ 解鎖 Clip Deck 中的所有 Clip。
* _AUTO-LOCK_ - 開啟 _Auto-Lock_ 時，任何自動播放的 Clip（無論是透過 timeline，或 MIDI 錄製/播放系統）都會被鎖定。如果你已經在 Logic Pro（或類似軟體）中編好一場演出，且不想不小心編輯到演出中使用的 Clips，這會很有用。
* _LOCKED CLIPS ZONES_ - 開啟後，你將無法變更任何已鎖定 Clip 的 zones。
* _LOCKED CLIPS PARAMS_ - 開啟後，你將無法變更任何已鎖定 Clip 的參數（scale、shift 等）。

### 右鍵選單

在 Clip 上按右鍵時，會出現一個選單，其中包含該 Clip 的部分選項。關於這個選單前幾個項目的更多資訊，請參閱 [Clip Editor 簡介](../clip-editor/clip-editor-intro.md "mention")、[Clip 設定](clip-settings.md "mention") 和 [群組](groups.md "mention")。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Clips 預設會設定為 _retrigger_。這表示無論你何時按下，Clip 都會從當下開始播放。因此如果你啟動得太晚，Clip 的動畫就會稍微延後，節奏也會不準。

{% hint style="info" %}
如果在已 retrigger 的 Clip 播放時使用 _Tap Tempo_，系統會將 Clip「量化」到正確拍點，即使你一開始沒有精準地在拍點上啟動它也一樣。
{% endhint %}

如果未啟用 _Retrigger_，Clip 會永遠保持在正確時間點上——就像 Clip 從 clock 的最一開始就已經啟動。當你透過外部 clock 訊號與音樂完美同步時，這很適合使用。

{% hint style="info" %}
Clips 通常設計成會無限循環，但你也可以把它們設計成只播放一次或幾次循環。請務必讓這類 Clip 保持 _retrigger_，否則它們不會重新開始！
{% endhint %}

### 轉場進入/退出時間（fade）

Clips 可以設定以秒為單位的淡入與淡出時間。預設情況下，淡化時間會繼承其群組設定（可在群組按鈕上按右鍵變更）。

如果你想使用不同於 Clip 所屬 group 的 fade duration，請先關閉 _USE GROUP DEFAULT_ 按鈕，然後調整該 Clip 的 _In time_ 和 _Out time_ 滑桿。
