---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 読み込みと保存

Liberation は状態を常にディスクへ保存しているため、停電やシステムの問題が発生した場合でも、終了した時点からそのまま起動できます。Zones、timeline、その他のコンテンツが失われることは基本的にありません。

ただし、バックアップや別のコンピューターへの移行のために、設定をエクスポートできます。

### Project の Import/Export

Project ファイルには、現在の設定のほぼすべてが保存されます。内容は次のとおりです。

* 以下の [#laser-settings-import-export](loading-and-saving.md#laser-settings-import-export) に記載されているすべて
* Clips、effects、group settings
* すべての timeline（オーディオおよびビデオメディアは含まれません）
* Artnet set up
* MIDI send/receive settings
* Tempo / synchronisation settings

現在、保存および読み込みの対象外となるものは次のとおりです。

* MIDI notes node および Sound Input Oscillator で使用する Sound と Midi の入力設定（MIDI send/receive settings と timecode sound input は保存されます）
* Interface scaling
* Canvas guide images 用のメディア
* timeline 用の Sound および Video メディア
* Text node で使用するフォント

{% hint style="danger" %}
timeline 内の Sound および video ファイルは project ファイルに保存されません。別のコンピューターへ移行する場合は、必ず別途保存してください。詳しくは [読み込みと保存](loading-and-saving.md#important-note-about-timeline-media-files) を参照してください。
{% endhint %}

### Laser settings Import / Export

* 各 laser の Laser settings
* Beam zones
* Canvas target areas
* DMX zones
* Laser controller assignment（名前を変更した controller の alias も含む）
* Laser scanner と colour calibration settings および presets
* 3D visualiser settings および presets

### Clip Deck Import / Export

* すべての clips と、それらの zone assignments、settings、parameters
* すべての group settings、flash mode、fade in/out times など

現在、保存および読み込みの対象外となるものは次のとおりです。

* すべての effects と、それらの parameters および settings

{% hint style="info" %}
**Project ファイルから project 全体を読み込まずに clips だけを読み込む**

project から clips だけをインポートするには、_**Clips->Import Clip Deck**_ を選択し、clip deck ファイル（.cpdk）ではなく project ファイルを選択します。
{% endhint %}

### Append clip deck

_Append Clip Deck_ を使用すると、エクスポート済みの clip deck ファイルから現在の project に clips を追加できます。Clips は現在の clip deck の末尾に追加されますが、ファイル内の effects と group settings はインポートされません。

### Export Selected Clips

現在選択されている clips がファイルにエクスポートされます。保存されるのは clips のみで、group settings と effects は保存されません。現在実行中の active clips は、選択されていない限りエクスポートされない点に注意してください。

{% hint style="info" %}
Option/Alt - shift - click clips で選択できます（または lasso を使用します）。選択されている clips は、周囲の太い白いアウトラインで確認できます。詳しくは [クリップの開始／停止](clips/starting-stopping-clips.md) を参照してください。
{% endhint %}

### Effects Import / Export

すべての effects を、それらの group settings および parameters と一緒に読み込み、保存します。

{% hint style="info" %}
**Project ファイルから project 全体を読み込まずに effects だけを読み込む**

project から effects だけをインポートするには、_**Effects->Import Effects**_ を選択し、effects ファイル（.efts）ではなく project ファイルを選択します。
{% endhint %}

### Timeline Export

1 つ以上の timeline を含む timeline ファイルをエクスポートします。エクスポートした timeline ファイルには、常に clipdeck が含まれます（ただし、再インポート時にどの clips を取り込むかは選択できます。詳しくは [#timeline-import](loading-and-saving.md#timeline-import) を参照してください）。

project ファイルに複数の timeline がある場合は、どの timeline をエクスポートするか選択するためのパネルが開きます。

{% hint style="danger" %}
timeline 内の Sound および video ファイルは timeline ファイルに保存されません。コンテンツを別のコンピューターへ移行する場合は、必ず別途保存してください。詳しくは [読み込みと保存](loading-and-saving.md#important-note-about-timeline-media-files) を参照してください。
{% endhint %}

### Timeline Import

単一の timeline ファイルから 1 つ以上の timeline をインポートします。timeline ファイルを選択すると、複数のインポートオプションを含むパネルが開きます。

timeline ファイルに複数の timeline が含まれている場合は、すべて一覧表示されます。含めたいものにチェックを入れてください。

* Replace existing timelines\
  現在のすべての timeline を削除し、インポートした timeline に置き換えます
* Import used clips only\
  使用されている clips のみをインポートし、timeline ごとに 1 つの group として clips を配置します。このオプションを選択しない場合、timeline ファイル内の clip deck 全体が既存の clips に追加されます。
* Replace existing clip deck\
  現在の clip deck を timeline ファイル内の clips に置き換えます。_Replace existing timelines_ が選択されている場合のみ使用できます。

{% hint style="info" %}
**Project ファイルから project 全体を読み込まずに timelines だけを読み込む**

project から timelines だけをインポートするには、_**Timeline->Import Timeline(s)**_ を選択し、timeline ファイル（.ltml）ではなく project ファイルを選択します。
{% endhint %}

### DMX / Artnet import / export

Artnet nodes を IP addresses と一緒に保存および読み込みます。DMX zones と、すべての DMX presets も含まれます。

### timeline メディアファイルに関する重要な注意

Sound および video ファイルは現在、timeline ファイルと一緒にエクスポート**されません**。コンテンツを別のコンピューターへ移動する必要がある場合は、必ずこれらのファイルも含めてください。

{% hint style="info" %}
**timeline がメディアファイルを探す仕組み**

timeline が読み込まれると、timeline（または project）ファイルと同じフォルダーを確認し、その中とすべてのサブフォルダーを検索します。そのため、ファイルが同じフォルダー内、または _/videos_ や _/sound_ などのサブフォルダー内にあれば、読み込み時に見つけることができます。
{% endhint %}
