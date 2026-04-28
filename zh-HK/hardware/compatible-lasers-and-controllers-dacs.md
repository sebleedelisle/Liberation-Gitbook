---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ 兼容的激光及控制器（DAC）

### 哪些激光可與 Liberation 兼容？

如果你的激光設有標準 ILDA 輸入，就可以配合 Liberation 使用（另需兼容的激光控制器，例如 Ether Dream 或 Helios DAC——[請參閱下方完整清單](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)）。

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC——家用最便宜的選擇</p></figcaption></figure>

在以下情況下，你不需要外置控制器或 ILDA 輸入：

* 你的激光內置 Ether Dream；或
* 你有 Wicked Lasers 的 LaserCube；或
* 你有內置 Mercury 的 X-Laser 燈具；或
* 你有內置 AVB 控制器的 Laser Animation Sollinger 激光（目前只在 macOS 上測試中）

{% hint style="info" %}
**甚麼是激光控制器？**

激光控制器（或 DAC）是一件硬件裝置，可接收 Liberation 的數碼資料，並將其轉換為控制激光掃描器及輸出的所需模擬訊號。（因此稱為 DAC：Digital to Analog Converter，數碼至模擬轉換器。）

控制器會透過 USB 或標準電腦網絡連接到你的電腦；它可以是外置裝置，亦可以安裝在激光內部。

如果是外置控制器，你會透過 ILDA 連接把它接到激光。ILDA 是業界標準，使用舊式 25-pin「D」型接頭。準備一條 ILDA 線，一端插入控制器，另一端插入激光即可。
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>外置 Ether Dream 上的 ILDA 輸出</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>激光後面板，顯示各種連接，包括 ILDA 輸入</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>標準 ILDA 線</p></figcaption></figure>

### 哪款控制器最適合我？

如果你是家用用戶，或是進行 4 部或以下激光、並且激光距離電腦較近的小型演出，USB 控制器如 **Helios DAC** 會是**最經濟**的選擇。

**Ether Dream** 這類網絡 DAC，最適合願意設定網絡、並希望運行大量激光的**專業**激光操作人員；至今所有大型 Liberation 演出都使用 Ether Dream 運行。

如果你有 **LaserCube**，就完全不需要另配激光控制器——Liberation 兼容所有 LaserCube。較早期型號使用 USB 線連接，較新的型號則透過網絡連接。

如果你是專業用戶並想要最簡單的方案，可考慮內置 Mercury 的 X-Laser 裝置，或使用 AVB 的 Laser Animation Sollinger 激光。

### 兼容的激光控制器

#### Ether Dream（網絡）

[Ether Dream](https://ether-dream.com) 已推出超過十年，目前為第 4 版（不過 Liberation 亦支援 Ether Dream 第 1、2、3 版）。它們非常可靠。

你可以透過標準網絡連接。它們可以購買獨立裝置版本；更理想的是，亦可安裝在激光內部。

#### Helios（USB）

[Helios](https://bitlasers.com/helios-laser-dac/) 是初學者的最佳選擇，價格亦比 Ether Dream 便宜。不過由於它透過 USB 連接，不建議用於長距離走線。另外，當你連接超過 4 部時，可能會遇到 USB 數據及驅動程式問題（尤其在 Windows 上）。

但如果你只是想在家中運行幾部激光，這是最便宜、最簡單的選擇。

#### Mercury（內置於 X-Laser 裝置）

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) 是 X-Laser 強大的 DMX 激光控制系統，專為希望直接從傳統燈光控制台運行激光的燈光設計師而設。透過最新 firmware 更新，Mercury 亦加入了 **Ether Dream emulation**，即代表它現在可與 Liberation 無縫配合使用，同時亦支援任何支援 Ether Dream 的其他軟件。

#### AVB（內置於 Laser Animation Sollinger 裝置）

**AVB** 是一種開放式、以網絡為基礎的協議，用於高效能、低延遲的音訊及數據串流。許多 LaserAnimation Sollinger 投影機都在硬件中直接支援 AVB，讓 Liberation 無需外置 DAC 亦可透過網絡連接。Liberation 的 AVB 支援目前**只限 macOS，並仍在測試中**，而且需要**兼容並支援 AVB 的網絡裝置**。設定正確後，它可為專業演出提供更簡單的工作流程、減少外置裝置，並帶來穩定可靠的運作。I

#### 未來將會支援的控制器：

* [IDN](http://www.ilda-digital.com)（來自 ILDA 的開放式網絡協議，可由任何廠商實作）

### 線材建議

為獲得最佳效能，請將 USB DAC 放近電腦，並使用較長的 ILDA 線連接到激光。（不過要小心，拆台時 ILDA 線很容易像鉤子一樣勾住其他物件！）

如果你使用 Ether Dream，仍然可以把它們集中放在一起，並使用較長的 ILDA 線連接到激光；或者你可以把它們安裝在激光附近，然後使用較長的網絡線。

最理想的設定，是把 Ether Dream（或其他控制器）直接安裝在激光內部（英國的 Rob at Stanwax Laser 可以代你處理）。
