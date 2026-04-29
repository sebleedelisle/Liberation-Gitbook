---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ 相容的雷射與控制器 (DAC)

### 哪些雷射可與 Liberation 相容？

如果你的雷射有標準 ILDA 輸入，就可以搭配 Liberation 使用（同時需要相容的雷射控制器，例如 Ether Dream 或 Helios DAC — [請參閱下方完整清單](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)）。

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC — 居家使用最便宜的選項</p></figcaption></figure>

如果符合以下情況，就不需要外部控制器或 ILDA 輸入：

* 你的雷射內建 Ether Dream；或
* 你有 Wicked Lasers 的 LaserCube；或
* 你有內建 Mercury 的 X-Laser 燈具；或
* 你有內建 AVB 控制器的 Laser Animation Sollinger 雷射（目前僅在 macOS 上測試中）

{% hint style="info" %}
**什麼是雷射控制器？**

雷射控制器（或 DAC）是一種硬體裝置，可接收 Liberation 輸出的數位資料，並轉換成控制雷射掃描器與輸出所需的類比訊號。（因此稱為 DAC：Digital to Analog Converter，數位類比轉換器。）

控制器會透過 USB 或標準電腦網路連接到你的電腦；它可能是外部裝置，也可能安裝在雷射內部。

如果是外部控制器，你會透過 ILDA 連接到雷射。ILDA 是業界標準，使用較傳統的 25-pin「D」型連接器。準備一條 ILDA 線，一端接到控制器，另一端接到雷射即可。
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>外接 Ether Dream 上的 ILDA 輸出</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>雷射後面板，可看到各種連接埠，包括 ILDA 輸入</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>標準 ILDA 線</p></figcaption></figure>

### 哪一種控制器最適合我？

如果你是居家使用者，或執行小型演出，雷射數量不超過 4 台且靠近電腦，那麼像 **Helios DAC** 這類 USB 控制器是**最經濟實惠**的選項。

像 **Ether Dream** 這類網路 DAC，則是**專業**雷射技術人員的最佳選擇，適合願意架設網路、並需要控制大量雷射的使用情境；目前為止，所有大型 Liberation 演出都是使用 Ether Dream 執行。

如果你有 **LaserCube**，就完全不需要另外的雷射控制器 — Liberation 與所有 LaserCube 相容。較早期的型號使用 USB 線連接，較新的型號則透過網路連接。

如果你是專業使用者，並且想要最簡單的方案，可以考慮內建 Mercury 的 X-Laser 裝置，或使用 AVB 的 Laser Animation Sollinger 雷射。

### 相容的雷射控制器

#### Ether Dream（網路）

[Ether Dream](https://ether-dream.com) 已推出超過十年，目前是第 4 版（不過 Liberation 也支援 Ether Dream 第 1、2、3 版）。它們非常可靠。

你可以透過標準網路連接。它可以購買獨立機型；更好的做法是直接安裝在雷射內部。

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) 是初學者的最佳選項，而且比 Ether Dream 便宜。不過由於它透過 USB 連接，不建議使用很長的線路。此外，當你連接超過 4 台時，可能會遇到 USB 資料傳輸與驅動程式問題（尤其是在 Windows 上）。

但如果你只是想在家裡控制幾台雷射，這是最便宜也最簡單的選項。

#### Mercury（內建於 X-Laser 裝置）

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) 是 X-Laser 強大的 DMX 雷射控制系統，專為想直接從傳統燈光控制台操作雷射的燈光設計師而設計。透過最新韌體更新，Mercury 也加入了 **Ether Dream 模擬**，這表示它現在可以與 Liberation 無縫搭配使用，也能與任何支援 Ether Dream 的其他軟體搭配使用。

#### AVB（內建於 Laser Animation Sollinger 裝置）

**AVB** 是一種開放式、以網路為基礎的協定，用於高效能、低延遲的音訊與資料串流。許多 LaserAnimation Sollinger 投影機在硬體中直接支援 AVB，讓 Liberation 可以透過網路連接，而不需要外部 DAC。Liberation 的 AVB 支援目前**僅限 macOS，且仍在測試中**，並且需要**相容且支援 AVB 的網路裝置**。正確設定後，它能為專業演出提供更簡單的工作流程、減少外部裝置，並帶來可靠的穩定性。

#### 未來將支援的控制器：

* [IDN](http://www.ilda-digital.com)（ILDA 的開放式網路協定，可由任何製造商實作）

### 佈線建議

為了獲得最佳效能，請將 USB DAC 放在電腦附近，並使用較長的 ILDA 線連接到雷射。（不過要注意，拆台時 ILDA 線很容易像鉤爪一樣勾到東西！）

如果你使用 Ether Dream，仍然可以把它們集中放在一起，並用較長的 ILDA 線連接到雷射；或者也可以將它們架設在雷射附近，再使用較長的網路線。

理想的設定方式，是將 Ether Dream（或其他控制器）直接安裝在雷射內部（在英國，Stanwax Laser 的 Rob 可以幫你處理）。
