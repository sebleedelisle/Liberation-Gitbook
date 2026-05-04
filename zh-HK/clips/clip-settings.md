---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip 設定

### Clip 設定面板

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip 設定面板</p></figcaption></figure>

使用 _Scale X_ 和 _Scale Y_ 更改 Clip 的輸出大小。除非你按住 _SHIFT_ 鍵，否則兩者會鎖定並同步調整。

使用 _Shift X_ 和 _Shift Y_ 更改 Clip 的水平及垂直位置。

_Zone Delay/Chase_ 是一個很有趣的功能，所以有獨立章節介紹。[Zone Delay/Chase](zone-delay-chase.md "mention")

### Parameters 面板

Clip Deck 右側的面板會顯示八個按情境變化的參數。選取 Clip 後，最先幾個控制項是所選 Clip 的 _Shift X_、_Shift Y_ 和 _Zone Delay_，其後是全域的 _Spin_ 和 _Scale_ 控制項。

這些相同參數亦會鏡射到支援的 MIDI 控制器。如果未有選取 Clip，Clip 專用的欄位會留空。如果你按住群組按鈕，首兩個控制項會改為該群組的淡入及淡出時間。

### 鎖定 Clips

如果 Clip 已鎖定，就不能移動或刪除。要鎖定 Clip，請在右鍵選單中使用 _Locked_ 剔選框。在 Clip 設定面板中，你會看到更多選項。

* _UNLOCK ALL -_ 解鎖 Clip Deck 中所有 Clip。
* _AUTO-LOCK_ - 當 _Auto-Lock_ 開啟時，任何自動播放的 Clip（透過 timeline 或 MIDI 錄製／播放系統）都會被鎖定。如果你已在 Logic Pro（或類似軟件）編排好一場 show，而不想意外修改 show 中使用的 Clips，這會很有用。
* _LOCKED CLIPS ZONES_ - 如果開啟此選項，你就不能更改任何已鎖定 Clip 的 zones。
* _LOCKED CLIPS PARAMS_ - 如果開啟此選項，你就不能更改任何已鎖定 Clip 的參數（scale、shift 等）。

### 右鍵選單

如果你在 Clip 上按右鍵，會顯示一個選單，內有該 Clip 的部分選項。關於此選單前幾項的更多資料，請參閱 [Clip Editor 簡介](../clip-editor/clip-editor-intro.md "mention")、[Clip 設定](clip-settings.md "mention") 及 [群組](groups.md "mention")。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Clips 預設會設定為 _retrigger_。這表示無論你何時按下，Clip 都會由該刻開始運行。所以如果你啟動得較遲，Clip 的動畫也會稍為延遲，與節奏不同步。

{% hint style="info" %}
如果在已 retrigger 的 Clip 運行期間使用 _Tap Tempo_，系統會將 Clip「量化」至同步，即使你並非剛好在拍點上啟動它。
{% endhint %}

如果未啟用 _Retrigger_，Clip 會一直保持同步——就像 Clip 在時鐘一開始時已經啟動一樣。當你透過外部 clock 訊號與音樂完全同步時，這個設定很適合使用。

{% hint style="info" %}
Clips 通常設計成無限循環，但你也可以設計成只播放一次或循環幾次。記得要讓這些 Clips 保持 _retrigger_，否則它們不會重新開始！
{% endhint %}

### Transition in/out time（fade）

Clips 可以設定以秒為單位的淡入及淡出時間。預設情況下，淡入淡出時間會繼承其群組設定（可在群組按鈕上按右鍵更改）。

如果你想使用與 Clip 所屬 group 不同的 fade duration，請先關閉 _USE GROUP DEFAULT_ 按鈕，然後調整 Clip 的 _In time_ 和 _Out time_ 滑桿。
