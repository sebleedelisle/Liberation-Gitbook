---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ MIDI 送受信のデフォルトマッピング

**Clip のオン／オフは、チャンネル 1〜14 の MIDI note on / off でトリガーされます**

Clip には水平位置（x）と垂直位置（y）があります。Clip を右クリックすると、その位置を確認できます。MIDI では、0,0 から始まる Clip をトリガーできます。

{% hint style="info" %}
このシステムでの Clip コントロールは絶対指定です。Clip Deck をスクロールしても、Clip の位置は変わりません。
{% endhint %}

MIDI チャンネル 1、ノート 1 は Clip 0,0、ノート 2 は Clip 0,1、ノート 3 は Clip 0,2 です。行方向に下へ進み、列方向に横へ進みます。128 に達すると次のチャンネルへ移り、再び最初から始まります。つまり、MIDI からアクセスできる Clip は合計で 128 x 14 = 1792 個です。

Clip 座標に対応する MIDI ノート：

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>ノート : 1</td><td>ノート : 6</td><td>ノート : 11</td><td>ノート : 16</td><td>ノート : 20</td></tr><tr><td><strong>y : 1</strong></td><td>ノート : 2</td><td>ノート : 7</td><td>ノート : 12</td><td>ノート : 17</td><td>...など</td></tr><tr><td><strong>y : 2</strong></td><td>ノート : 3</td><td>ノート : 8</td><td>ノート : 13</td><td>ノート : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>ノート : 4</td><td>ノート : 9</td><td>ノート : 14</td><td>ノート : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>ノート : 5</td><td>ノート : 10</td><td>ノート : 15</td><td>ノート : 20</td><td></td></tr></tbody></table>

MIDI note on イベントで Clip が開始され、対応する note off イベントで Clip が停止します。これは Group のトリガーモードに関係なく動作します。このシステムはもともと再生と録音向けに設計されていたため、ノートで Clip をトグルする方式は望ましくありませんでした。

### **エフェクト**

**チャンネル 15** の MIDI control change（CC）メッセージでエフェクトを調整します。\
Effect 1 は CC 0-3、値 0-127 を使用します\
Effect 2 は CC 4-7、値 0-127 を使用します\
Effect 3 は CC 8-11、値 0-127 を使用します\
…以降も同様です。

4 つずつのグループで、そのエフェクトのレベルと 3 つのパラメーターを制御します：

<table><thead><tr><th width="164">Effect :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Level</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...など</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **グローバル設定**

**チャンネル 16** の MIDI control change メッセージでグローバル設定を変更します：\
CC 1 : Shift X（水平）0 -127、64 が中央です\
CC 2 : Shift Y（垂直）0 -127、64 が中央です\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

重要な項目：\
CC 15 : Global brightness

このシステムは、もともと録音と再生向けに設計されたものです。Logic、Ableton、その他の DAW を使ってタイムラインアニメーションを作成できます。ライブコントロールにも使用できますが、その用途に最適化されているわけではなく、APC40 セットアップと比べるとライブコントロール用の一部機能が不足しています。
