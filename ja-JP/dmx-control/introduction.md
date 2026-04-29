---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ はじめに

Liberation には、柔軟で強力な DMX システムが搭載されています。Art-Net 経由で照明エフェクトを作成したり、DMX 対応レーザーを制御したりできます。レーザーショーと照明を簡単に同期できるように設計されており、別途照明卓を用意する必要はありません。

{% hint style="info" %}
**Art-Net とは何ですか？DMX とはどのような関係がありますか？**

**DMX** は、照明、レーザー、スモークマシン、その他のステージエフェクトを制御するために長年使われてきた方式です。専用ケーブル（通常は XLR コネクター付き）で制御信号を送信し、各フィクスチャは特定のチャンネル範囲を受信して動作内容を判断します。

**Art-Net** は、同じ DMX データを通常のコンピューターネットワーク上で送信するための、より新しい方式です。専用ケーブルの代わりに、インターネットやローカルネットワークの通信と同じように Ethernet 経由でデータを送信します。

Liberation では、すべての DMX 出力が Art-Net を使用して送信されます。Art-Net 対応デバイスを直接制御することもできますし、**Art-Net ノード**（Art-Net を標準 DMX に変換する小型の機器）を接続することもできます。これにより、機器自体が Art-Net に対応していない従来の DMX 照明やエフェクトも制御できます。
{% endhint %}

スモークマシン、ヘイザー、CO₂ ジェット、コールドスパークマシンなど、さまざまなステージ機器の制御にも使用できます。DMX に対応していれば、DMX ゾーンとして設定し、レーザーコンテンツと並べて Liberation から直接トリガーできます。

DMX フィクスチャは **DMX ゾーン**として追加され、レーザービームゾーンや Canvas ターゲットエリアと並んでゾーンリストに表示されます。各 DMX ゾーンでは **DMX プリセット**を使用します。このプリセットにより、レーザー Clip のプロパティ（位置、色、明るさなど）を DMX チャンネル値へどのようにマッピングするかを Liberation に指定します。

Clip を DMX ゾーンへ送信すると、Liberation はその Clip 内の最初の要素を参照し、プリセットに基づいてそのプロパティを変換します。これにより、レーザーで使用している同じ Clip から、照明や DMX エフェクトを直接簡単に動かせます。

#### Glastonbury での Liberation

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Liberation の DMX システムが初めて実際に試されたのは Glastonbury 2023 でした。Reach Lasers は Arcadia "spider" ステージの一部として、合計 90 台のビームソースを設置しました。

18 台のレーザーは内蔵 Ether Dreams で制御され、さらに 12 台の 6 ヘッドビームバーは Art-Net と DMX 経由で制御されました。
