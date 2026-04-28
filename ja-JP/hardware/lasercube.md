---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube プロモーション画像：Wicked Lasers 提供</p></figcaption></figure>

Wicked Lasers の [LaserCube](https://www.laseros.com/lasercube/) は、バッテリー駆動の非常にコンパクトなレーザーユニットで、複数の出力構成が用意されています。使いやすいスマートフォンアプリがあるためホビーユーザーに人気がありますが、最近のモデルはプロフェッショナルなショーでも使用できる性能を備えています。

スマートフォンアプリ（LaserOS という名称で、デスクトップ版もあります）は無料でダウンロードでき、気軽に楽しめるうえ、ほとんどのユーザーには十分な機能があります。ただし、複数のレーザーを使う大規模なショーを運用する場合は、より専門的で強力なものが必要になります。そこで Liberation の出番です。

### LaserCube への接続

初期の LaserCube は USB 経由で制御しますが、現在のモデルはすべてネットワークコントローラーを内蔵しています。これらのネットワーク制御対応のキューブは "LaserCube Wifi" と呼ばれます。Liberation は、USB 接続とネットワーク接続のどちらの場合でも、両方のタイプの LaserCube\* をサポートしています。

\*（LaserCube ネットワークプロトコルのサポートはバージョン 0.7.3 で導入されました）

### USB LaserCube

micro USB ケーブルで LaserCube をコンピューターに接続し、_Controller Assignment_ パネルで確認します（[controller-assignment.md](../setting-up/controller-assignment.md) を参照）。自動的に表示されない場合は、_REFRESH_ ボタンを押してください。

### Network LaserCube "Wifi"

{% hint style="danger" %}
"Wifi" キューブはワイヤレスネットワーク上で動作するように設計されていますが、この方法は推奨しません。ドロップアウトやグリッチが発生する可能性が高くなります。代わりに、Ether Dream と同様に RJ45 ソケットを使用して LaserCube を有線ネットワークに接続してください。
{% endhint %}

LaserCube を有線ネットワークに接続します。

LaserCube を "LAN Client" モードにし、ネットワーク上にルーターがあることを確認します。LaserCube はルーターから IP アドレスを取得し、その後 _Controller Assignment_ パネルに表示されるはずです（[controller-assignment.md](../setting-up/controller-assignment.md) を参照）。

{% hint style="info" %}
ルーターを使わずにネットワークを構成し、すべてのデバイスに固定 IP アドレスを設定することも可能です。イベント業界ではこの方法もよく使われています。個人的には、ネットワークにルーターを追加する方法を好んでおり、ネットワーク設定にあまり慣れていない方にはこの方法をおすすめします。

ルーターが各機器に IP アドレスを動的に割り当てるため、よりシンプルでミスも起こりにくいと感じています。
{% endhint %}

{% hint style="danger" %}
Ether Dream とは異なり、_**LaserCube は、バッファアンダーラン、パケットロス、その他の破損データや不正なデータが発生してもレーザーをブランキングしません**_。

代わりに、停止した位置からそのまま動作を続けます。そのため場合によっては、ライブビームがゾーン外のエリアを横切ったり、さらに悪い場合はソフトウェアマスクを突き抜けたりすることがあります。

私は LaserCube の設計者／開発者とこの件について話しており、将来的にファームウェアアップデートで対応されることを期待しています。ただし現時点では、レーザーを当てたくない場所は必ず物理的にマスクしてください。

公平に言えば、これは本来いずれにしても行うべき対策です。ただ、私自身はカメラやプロジェクターの保護にソフトウェアマスクを使っています。そのため、Ether Dream（エラーやデータ欠落があるとすぐにセーフティストップモードに入ります）と比べて、LaserCube ネットワークプロトコルを使う場合はこの方法の危険性が高いことを認識しておいてください。

また、すでに述べましたが、**LaserCube には有線接続を使用してください**。Wifi では十分ではなく、この問題をさらに悪化させます。
{% endhint %}
