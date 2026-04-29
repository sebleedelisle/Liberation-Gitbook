---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

每個 _Creator_ node 都有 _Render Profile_ 設定，這會決定形狀如何由雷射繪製（或算繪）。

**對大多數用途來說，**_**DEFAULT**_** 設定完全足夠**。但如果你正在處理圖形或複雜內容，可能會想更精細地控制每個形狀的算繪方式。

{% hint style="info" %}
與大多數雷射軟體不同，Liberation 會在即將送到 laser controller 前即時產生點資料流。這能為你節省大量磁碟空間；Clip 通常只有幾 kB，而不是預先算繪好的數 MB 點資料流。

這也代表你可以針對每台雷射的不同掃描器類型調整同一份內容，而不需要修改 Clip 本身。

更多詳細資訊請參閱 [Liberation 如何產生雷射內容](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

共有三個預設的 _Render Profiles_：_DEFAULT_、_FAST_ 和 _DETAIL_。

_**DEFAULT**_ - 適用於大多數情況的通用 profile

_**FAST** -_ 如果你的 Clip 內容很多，而且其中有些只是很簡單的點和直線，選擇這個選項可能可以減少閃爍。

_**DETAIL**_ - 如果你要繪製需要銳利轉角的內容，請使用這個選項。但請注意，掃描器的移動速度會變慢，可能讓輸出看起來更閃爍。

{% hint style="info" %}
在 Clip Editor 中，你可以將 Creator 指派到不同的 render profile，但每台雷射會依據自己的掃描器設定來處理這些 profile。請參閱 [掃描器預設值](../../advanced/scanner-presets.md)
{% endhint %}
