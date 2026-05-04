---
description: >-
  Lasers can be dangerous so it's important to follow best practices and safety
  guidelines. This page is a useful overview that will help you through the
  process of setting up lasers safely.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/setting-up-lasers
---

# ✅ 雷射架設流程總覽

### 安全開啟雷射的流程總覽

本手冊不能取代正式的雷射安全訓練；在公共場合使用雷射之前，你絕對需要接受相關訓練。部分地區另有法律要求，但無論如何，你都應始終遵守安全與專業的最佳實務。

PLASA 提供免費下載的雷射安全指南，普遍被視為最佳實務：[https://www.plasa.org/guidance-for-display-lasers/](https://www.plasa.org/guidance-for-display-lasers/)

使用前，請務必確認你了解雷射相關的安全影響！

#### 簡介

本頁旨在提供安全啟動雷射流程的總覽。各步驟的詳細操作會在本章節後續頁面說明；本頁可幫助你先掌握整體流程，也可以在每次架設雷射時回來作為參考。

<figure><img src="../.gitbook/assets/laser-aperture.jpg" alt=""><figcaption><p>典型的雷射出光口護蓋</p></figcaption></figure>

### 架設硬體：

1. **關閉雷射的出光口護蓋**
2. **牢固架設雷射**，並將其指向正確方向
3. **將停止按鈕連接到雷射**
4. **將雷射控制器連接到電腦**
5. **開啟雷射電源**

### 設定 Liberation：

1. **解除所有雷射的啟用狀態**，並在 Liberation 中找到並連接控制器
2. **將 _Global Brightness_ 設定降到 0**（使用圖示列中的滑桿，或 APC40 上的 _Master Fader_）
3. **啟用雷射** - 在出光口護蓋仍然關閉的情況下，確認目前沒有任何 Clip 正在作用，然後啟用雷射（使用 _Laser Overview_ panel 中的 _Arm_ 按鈕）
4. **開啟測試圖案**（使用圖示列中的 ☒ 按鈕，選擇 pattern 1，也就是中間有十字的綠色方形）
5. **調整輸出 zone** - 先估算最安全的 zone 大小與位置（例如可以將其設在很高、朝向天花板的位置，但這取決於你的實際環境）
6. **確認雷射正常運作** - 慢慢提高亮度，直到你能在出光口視窗後方看到光線。然後再將亮度降回零。
7. **測試停止按鈕**，確認按下時所有雷射輸出都會熄滅

### 開始雷射輸出

1. **清空暴露區域** - 確保沒有人會暴露在雷射下，並告知所有人員在雷射架設期間不得進入暴露區域。（你也應確認所有相機與投影機都已遮蓋，或已裝上鏡頭蓋！）
2. **打開出光口護蓋** - 站在側邊並避開輸出方向，將出光口護蓋滑下。如果你的 zone 設在高處，可以考慮讓護蓋保持部分關閉。
3. **提高亮度，直到雷射剛好可見** - 只需將雷射調到足以看見 zone 的亮度
4. **調整 zone** - 設定 zone 的大小、形狀與位置，確保它在任何公眾可進入區域的地面以上 3 公尺，且雷射不會到達任何其他公眾可進入區域
5. **加入實體遮罩** - 使用出光口護蓋及／或黑色鋁箔膠帶，將所需 zone 以外的位置做實體遮蔽。這非常重要，因為任何雷射硬體或軟體都有可能故障。
6. **加入軟體 mask** - Liberation 內的軟體 mask 可用來保護相機與投影機，但**絕不可**用來取代保護人員用的實體遮蔽。請注意，沒有任何軟體或硬體是絕對可靠的；使用軟體 mask 前，請務必了解相關風險。

{% hint style="warning" %}
請注意，本指南假設是在室內架設。如果你在戶外作業，必須採取額外步驟以確保航空安全，包括但不限於：

* 取得 FAA 或 CAA 等航空主管機關的必要許可
* 與附近機場和飛行場聯繫協調
* 查看公開航班雷達，並指派觀察員留意航空器

即使雷射強度遠低於安全門檻，仍可能對飛行員造成災難性的干擾。

在將任何雷射射向空域之前，請確保你具備必要的資格、執照與許可。
{% endhint %}
