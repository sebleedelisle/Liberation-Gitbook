---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### はじめに

Liberation の 3D visualiser は非常に便利な機能です。レーザーを一切用意しなくても、ショーの設計や調整ができます。特に多数のレーザーを使う複雑なセットアップでは、私にとって欠かせないツールになっています。

### 3D 空間内の操作

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>3D Visualiser ビュー</p></figcaption></figure>

* クリックしてドラッグすると、オービットポイントを中心にビューを回転できます
* マウスホイールで、オービットポイントに向かって前後に移動できます
* Shift キーを押したままクリックしてドラッグすると、XY 平面に沿ってカメラを左右・上下に横移動（ストレイフ）できます
* Visualiser 上の任意の場所をダブルクリックすると、カメラ位置をリセットできます

### Settings

_Window_ メニューから _3D Visualiser Settings_ パネルを開きます。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings パネル</p></figcaption></figure>

* **Visualiser size** - アプリの他の部分に対する Visualiser のサイズを変更します
* **Brightness Adjustment** - レーザーの表示の明るさを変更します
* **Show laser numbers** - 各レーザーの上に対応する番号を表示します
* **Show zone names** - 各レーザーの下に対応するゾーン名を表示します

### Camera settings

これらの設定は、主に 3D 空間内の仮想カメラに関するものです。これらの設定にはプリセット用のドロップダウンがあり、保存して再読み込みできます。

* **Camera distance -** カメラは常に自身の _Orbit point_ を向いています。Camera distance は、そのポイントからカメラまでの距離です。この設定はマウスのスクロールホイールでも調整できます。
* **FOV -** Field of view（視野角）です。カメラがどれだけ広角になるか、またはズームインされるかを決定します。
* **Orbit position** - オービットポイントを中心とした現在の回転を表します。1 つ目の値は X 軸まわりの回転（ピッチ）、2 つ目の値は Y 軸まわりの回転（ヨー）です。
* **Orbit centre point** - 3D 空間内のオービットポイントの位置（x、y、z）です。
* **Grid height** - 「地面」（つまり y = 0 の位置）からのグリッドの高さです。

### Content settings

これらの設定では、3D 環境内でレーザー（および Canvas）をどこに配置するかを決定します。これらの設定にはプリセット用のドロップダウンがあり、保存して再読み込みできます。

#### Lasers

各レーザーには個別の設定グループがあり、小さな白い三角形で展開できます。

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>3D visualiser のレーザー設定</p></figcaption></figure>

* **3D Position** - レーザーの x、y、z 位置です。
* **3D Orientation** - レーザーの x、y、z 各軸まわりの回転です。
* **Flip X / Flip Y** - レーザーの仮想出力を反転します。注意：通常これは必要ありません。ハードウェアとの不一致を修正する場合は、レーザー側の flip / orientation 設定を使用する方が適切です。
* **Output Range horizontal / vertical** - レーザーのスキャナーの最大 / 最小角度に関する設定です。標準は 60º ですが、使用するレーザーが異なる場合は調整できます。

#### Canvas

Canvas システムを使用している場合は、Canvas 画像を 3D ビュー内に含めることもできます。チェックボックスを有効にすると Canvas が表示されます。position、orientation、scale の各設定を使って、3D ビュー内での見え方を決定します。

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>3D visualiser の Canvas 設定</p></figcaption></figure>

{% hint style="info" %}
「ゴースト」レーザーが表示されていますか？3D Visualiser はレーザー設定からある程度独立しているため、Liberation 内のレーザー数より多くのレーザーが Visualiser 内に存在する場合があります。プロジェクトにレーザーを追加すると、Visualiser 内にも新しいレーザーオブジェクトが追加されます。ただしレーザーを削除しても、Visualiser 内には「ゴースト」レーザーオブジェクトが残ります。

すべてのゴーストレーザーを削除するには、_Remove extra 3D laser objects_ ボタン（3D Visualiser settings パネルの下部）をクリックします。

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
