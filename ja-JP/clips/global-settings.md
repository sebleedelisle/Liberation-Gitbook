---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Global transformations

Clip の変形（shift x/y、scale x/y）に加えて、実行するすべての Clip に適用される Global Transformations があります。確認するには _Global Transformations_ パネルを開きます。（通常、このパネルは _Clip Settings_ と同じ並びのタブにあります）。

デフォルトでは、再生中の Clip がなくなると、これらの設定はすべてリセットされます。このリセット動作は、_Global Transformations_ パネル下部の _AUTO RESET_ ボタンで無効にできます。

{% hint style="info" %}
Global Transformations は Canvas 内の要素には影響せず、Beam と DMX ゾーンにのみ影響します。
{% endhint %}

### Scale X/Y

水平および垂直方向のスケールです。`Shift` を押さない限り、これらの値は連動します。デフォルトでは APC40 Device Control ノブ 4 と 8 にもマッピングされており、Clip Deck の右側のパネルに表示されます。

### Shift X/Y

水平および垂直方向のシフトです。すべてを水平方向／垂直方向に移動します。

### Spin

すべてのコンテンツを中心の周りで回転させます。正の値では時計回りに、負の値では反時計回りに回転します。この設定が _Rotation_ 変形に影響することが分かります。デフォルトでは APC40 Device Control ノブ 3 にマッピングされており、Clip Deck の右側のパネルに表示されます。

### Spin 3D

すべてのコンテンツを Y 軸（中心を通る垂直線）の周りで回転させます。この設定が _Rotation3D_ 変形に影響することが分かります。デフォルトでは APC40 Device Control ノブ 7 にマッピングされており、Clip Deck の右側のパネルに表示されます。

### Rotation

中心の周りの回転です。値は度数です。

### Rotation 3D

Y 軸（中心を通る垂直線）の周りの回転です。値は度数です。

### Auto reset

オンにすると、現在実行中の Clip がすべて無効になった時点で、すべての Global Transformations がリセットされます。これにより、次回 Clip を実行するときに予期しない状態になるのを防げます。
