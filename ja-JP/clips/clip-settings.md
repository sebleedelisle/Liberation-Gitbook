---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip settings

### Clip settings パネル

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip settings パネル</p></figcaption></figure>

_Scale X_ と _Scale Y_ を使って、Clip の出力サイズを変更します。通常は連動していますが、_SHIFT_ キーを押している間は個別に調整できます。

_Shift X_ と _Shift Y_ を使って、Clip の水平位置と垂直位置を変更します。

_Zone Delay/Chase_ はとても便利で楽しい機能なので、専用のセクションで説明します。[zone-delay-chase.md](zone-delay-chase.md "mention")

### Clip のロック

Clip がロックされている場合、移動や削除はできません。Clip をロックするには、右クリックメニューの _Locked_ チェックボックスを使用します。Clip settings パネルでは、さらにいくつかのオプションを使用できます。

* _UNLOCK ALL -_ Clip Deck 内のすべての Clip のロックを解除します。
* _AUTO-LOCK_ - _Auto-Lock_ がオンの場合、自動再生された Clip（タイムライン、または MIDI の録音／再生システムによる再生）はロックされます。Logic Pro などでショーをプログラムしていて、ショーで使用する Clip を誤って編集したくない場合に便利です。
* _LOCKED CLIPS ZONES_ - これがオンの場合、ロックされた Clip の Zone は変更できません。
* _LOCKED CLIPS PARAMS_ - これがオンの場合、ロックされた Clip のパラメーター（scale、shift など）は変更できません。

### 右クリックメニュー

Clip を右クリックすると、その Clip に関する一部のオプションを含むメニューが表示されます。このメニューの最初のいくつかの項目については、[clip-editor-intro.md](../clip-editor/clip-editor-intro.md "mention")、[clip-settings.md](clip-settings.md "mention")、[groups.md](groups.md "mention")を参照してください。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>Clip settings の右クリックメニュー</p></figcaption></figure>

### Retrigger

Clip はデフォルトで _retrigger_ に設定されています。これは、いつ押しても、その時点から Clip が再生を開始するという意味です。そのため、開始が遅れると、Clip のアニメーションも少し遅れてタイミングから外れます。

{% hint style="info" %}
Retrigger された Clip の再生中に _Tap Tempo_ を行うと、拍のちょうど頭で開始していなくても、システムが Clip をタイミングに合うように「quantise」します。
{% endhint %}

_Retrigger_ が有効でない場合、Clip は常にタイミングに合います。これは、Clip がクロックの最初から開始されていたかのように動作します。外部クロック信号を使って音楽と完全に同期している場合に適しています。

{% hint style="info" %}
Clip は永続的にループするように作られることが多いですが、1 回だけ、または数回だけ再生されるように作ることもできます。そのような Clip は必ず _retrigger_ のままにしてください。そうしないと再スタートしません。
{% endhint %}

### Transition in/out time（フェード）

Clip には、秒単位の時間でフェードイン／フェードアウトを設定できます。デフォルトでは、フェード時間は所属する Group の設定を継承します（Group ボタンを右クリックして変更できます）。

Clip の Group とは異なるフェード時間にしたい場合は、まず _USE GROUP DEFAULT_ ボタンをオフにしてから、Clip の _In time_ と _Out time_ スライダーを調整します。
