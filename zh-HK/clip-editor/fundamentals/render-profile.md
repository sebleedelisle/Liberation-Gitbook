---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

每個 _Creator_ 節點都有一個 _Render Profile_ 設定，用來決定形狀如何以激光繪畫（或 _rendered_）。

**對大部分用途來說，**_**DEFAULT**_** 設定已經完全足夠**。不過，如果你正在處理圖像或複雜內容，可能會想更仔細控制每個形狀的 render 方式。

{% hint style="info" %}
與大部分激光軟件不同，Liberation 會在即將傳送到激光控制器之前，才即時產生 point stream。這樣可以節省大量磁碟空間：Clip 只需幾 kB，而不是預先 render 好、以 MB 計的 point stream。

這亦代表你可以按每部激光的不同 scanner 類型，為同一份內容作調整，而無需改動 Clip 本身。

詳情請參閱 [Liberation 如何產生激光內容](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

共有三個預設 _Render Profiles_：_DEFAULT_、_FAST_ 及 _DETAIL_。

_**DEFAULT**_ - 適合大部分情況的通用 profile

_**FAST** -_ 如果你的 Clip 有很多內容，而其中部分只是非常簡單的點和直線，選擇此選項可能會減少閃爍。

_**DETAIL**_ - 如果你要繪畫需要銳利角位的圖形，請使用此選項。但請留意，你的 scanner 會移動得較慢，令輸出較容易閃爍。

{% hint style="info" %}
在 Clip Editor 內，你可以將 creator 指派到不同的 render profile；但每部激光都會根據其 scanner 設定來處理這些 profile。請參閱 [Scanner presets](../../advanced/scanner-presets.md)
{% endhint %}
