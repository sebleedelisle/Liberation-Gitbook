---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ 対応レーザーとコントローラー（DAC）

### Liberation と互換性のあるレーザーはどれですか？

レーザーに標準の ILDA 入力があれば、Liberation で使用できます（Ether Dream や Helios DAC などの対応レーザーコントローラーも必要です - [下記の全リストを参照](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)）。

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC - 自宅用途で最も低価格な選択肢</p></figcaption></figure>

次の場合は、外部コントローラーや ILDA 入力は必要ありません。

* レーザー本体に Ether Dream が内蔵されている場合、または
* Wicked Lasers の LaserCube を使用している場合、または
* Mercury 内蔵の X-Laser フィクスチャーを使用している場合、または
* AVB コントローラー内蔵の Laser Animation Sollinger レーザーを使用している場合（現在は macOS のみでテスト中）

{% hint style="info" %}
**レーザーコントローラーとは？**

レーザーコントローラー（または DAC）は、Liberation からのデジタルデータを、レーザーのスキャナーや出力を制御するために必要なアナログ信号へ変換するハードウェアデバイスです。（そのため DAC、つまり Digital to Analog Converter と呼ばれます。）

コントローラーは USB または標準的なコンピューターネットワーク経由でコンピューターに接続します。外部デバイスの場合もあれば、レーザー本体に内蔵されている場合もあります。

外部デバイスの場合は、ILDA 接続でレーザーに接続します。ILDA は、従来型の 25 ピン「D」コネクターを使用する業界標準です。ILDA ケーブルを用意し、一方をコントローラーに、もう一方をレーザーに接続します。
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>外部 Ether Dream の ILDA 出力</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>ILDA 入力を含む各種接続端子があるレーザーのリアパネル</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>標準的な ILDA ケーブル</p></figcaption></figure>

### どのコントローラーを選べばよいですか？

自宅で使用する場合、またはコンピューターの近くにある 4 台以下のレーザーで小規模なショーを行う場合は、**Helios DAC** のような USB コントローラーが**最も手頃**な選択肢です。

**Ether Dream** のようなネットワーク DAC は、ネットワークのセットアップに慣れていて、多数のレーザーを運用したいプロのレーザーオペレーターにとって**最適な選択肢**です。これまでの大規模な Liberation ショーはすべて Ether Dream で運用されています。

**LaserCube** をお持ちの場合、別途レーザーコントローラーはまったく必要ありません。Liberation はすべての LaserCube に対応しています。初期モデルは USB ケーブルで接続し、新しいモデルはネットワーク経由で接続します。

プロ用途で、できるだけ簡単な構成を求める場合は、Mercury 内蔵の X-Laser ユニット、または AVB を使用する Laser Animation Sollinger レーザーを検討してください。

### 対応レーザーコントローラー

#### Ether Dream（ネットワーク）

[Ether Dream](https://ether-dream.com) は 10 年以上前から存在しており、現在はバージョン 4 です（ただし Liberation は Ether Dream バージョン 1、2、3 にも対応しています）。非常に信頼性の高い製品です。

標準的なネットワーク経由で接続します。単体ユニットとして購入できるほか、さらに便利な方法として、レーザー本体に組み込むこともできます。

#### Helios（USB）

[Helios](https://bitlasers.com/helios-laser-dac/) は初心者に最適な選択肢で、Ether Dream より安価です。ただし USB 接続のため、長いケーブルでの運用にはおすすめしません。また、4 台を超えて接続すると、USB データやドライバーの問題が発生することがあります（特に Windows）。

ただ、自宅で数台のレーザーを動かしたいだけであれば、最も安く、最もシンプルな選択肢です。

#### Mercury（X-Laser ユニット内蔵）

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) は、従来のライティングコンソールからレーザーを直接制御したい照明デザイナー向けに設計された、X-Laser の強力な DMX レーザー制御システムです。最新のファームウェアアップデートにより、Mercury には **Ether Dream エミュレーション**も含まれるようになりました。これにより、Liberation はもちろん、Ether Dream に対応する他のソフトウェアでもスムーズに使用できます。

#### AVB（Laser Animation Sollinger ユニット内蔵）

**AVB** は、高性能かつ低レイテンシーのオーディオおよびデータストリーミング向けに設計された、オープンなネットワークベースのプロトコルです。多くの LaserAnimation Sollinger プロジェクターは、ハードウェアに AVB サポートを直接搭載しており、外部 DAC を必要とせずに Liberation からネットワーク経由で接続できます。Liberation の AVB サポートは現在 **macOS のみ対応でテスト中**であり、**AVB 対応の互換ネットワークデバイス**が必要です。正しくセットアップすれば、プロフェッショナルなショーにおいて、よりシンプルなワークフロー、少ない外部デバイス、高い信頼性を実現できます。

#### 今後対応予定のコントローラー :

* [IDN](http://www.ilda-digital.com)（ILDA によるオープンなネットワークプロトコル。どのメーカーでも実装可能）

### ケーブル接続のヒント

最適なパフォーマンスを得るには、USB DAC をコンピューターの近くに置き、長めの ILDA ケーブルでレーザーに接続します。（ただし、撤収時に ILDA ケーブルが引っかかりやすいので注意してください！）

Ether Dream を使用する場合も、すべてを一か所にまとめて長い ILDA ケーブルでレーザーに接続できます。または、Ether Dream をレーザーの近くに設置し、長いネットワークケーブルを使用することもできます。

理想的な構成は、Ether Dream（または他のコントローラー）をレーザー本体に直接内蔵することです（英国では Stanwax Laser の Rob が対応してくれます）。
