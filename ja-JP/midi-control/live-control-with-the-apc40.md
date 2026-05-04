---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Live MIDI Controllers

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40 controller**

これはLiberationの標準ハードウェアコントローラーです。強くおすすめしますし、Liberationは当初からこのハードウェアを中心に設計されてきたと言ってよいでしょう。APC40を接続すると、Liberationはすぐに自動で接続します。

{% hint style="warning" %}
_大変！ショーの途中でUSBプラグが抜けてしまいました！_

慌てなくて大丈夫です。もう一度差し込むだけで、Liberationが自動的に再接続します。問題ありません。
{% endhint %}

### APC40 Mark 1 or Mark 2?

簡単に言うと、Mark 2をおすすめします。LiberationのClip Deckインターフェースにより近いフルカラーのボタンを備えているためです。Mark 1でも必要なら使えますが、画面上のレイアウトと少し異なるためやや分かりにくくなります。また、ボタンは赤、オレンジ、緑にしか点灯しないため、Clipの色とは一致しません。

{% hint style="info" %}
初代APC40 Mark 1は2009年に登場しました（！）。金属製ボディと、コンソールのような頑丈なフォームファクターを理由に、今でも好んで使う人がいます。改良版のMark 2は2014年に登場し、2024年にいったん生産終了となりましたが、ビジュアルアーティスト（Resolumeなど）やレーザーアーティストからの需要により、2025年に生産が再開される予定です。
{% endhint %}

APC40で使用できるコントロールの一覧は、[APC40 リファレンス](../reference/apc40-reference.md "mention")を参照してください。

### APC Mini

Liberation 1.0.3には、APC Mini用のプロファイルも含まれています。8x5のClipグリッド、zoneボタン、zoneのX/Y反転コントロール、グループボタン、すべてのClipの停止、Clipページの移動、zoneページの移動、タップテンポ、小節リセット、テンポの微調整がマッピングされています。フェーダーではエフェクトレベルを操作し、Shift使用時のフェーダーではエフェクトパラメーターを操作します。最後のフェーダーはGlobal Brightnessを操作します。

### MIDI Fighter Twister

MIDI Fighter Twisterプロファイルは、Clipの起動ではなく、エンコーダーを多用したコントロール向けです。エンコーダーの1行はエフェクトスロット1〜8のパラメーター1を操作し、別の1行はParametersパネルの8つのコンテキスト依存コントロールに対応します。これにはClip shift、zone delay、global spin/scale、group fadesが含まれます。
