---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/installation/authorising-and-de-authorising
---

# ✅ 認証と認証解除

### Liberation を認証する

Liberation を初めて開くと、_demo mode_ で起動し、_About panel:_ が表示されます。

<figure><img src="../.gitbook/assets/authorisation-about-panel.png" alt="" width="375"><figcaption></figcaption></figure>

_AUTHORISE ONLINE_ ボタンをクリックすると、Web ブラウザーが開きます。まだログインしていない場合は、この時点でログインを求められます。

システムが自動的に、このインストールをあなたのサブスクリプションに対して認証します。完了すると、次のメッセージが表示されます。

<figure><img src="../.gitbook/assets/authorisation-machine-added" alt=""><figcaption></figcaption></figure>

Liberation に戻ると、_About panel_ が更新されています（数秒待つ必要がある場合があります）。

<figure><img src="../.gitbook/assets/authorise-about-panel-authorised" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="warning" %}
サブスクリプションで認証可能な最大台数のコンピューターをすでに認証している場合は、他のマシンのいずれかを認証解除するか、サブスクリプションをアップグレードする必要があります。
{% endhint %}

{% hint style="info" %}
複数のサブスクリプションがある場合は、そのコンピューターに割り当てるサブスクリプションを選択するよう求められます。
{% endhint %}

これで Liberation のインストールが認証され、レーザーに出力できるようになりました。おめでとうございます！ただし、レーザーをアームする前に、[クイックスタートガイド](../getting-started.md) と [Laser セットアップ手順の概要](../setting-up/setting-up-lasers.md) をお読みください。

{% hint style="info" %}
_About panel_ は、メニューの _Liberation -> About Liberation_ または _Liberation -> Authorise/Deauthorise this computer_ からいつでも開くことができます。
{% endhint %}

### Liberation の認証を解除する

**Liberation 内から行う場合** - メニューの _Liberation -> Authorise / De-authorise this Computer_ を開き、_DEAUTHORISE COMPUTER_ ボタンをクリックします。これだけです。この操作を行うにはオンラインである必要があります。

<figure><img src="../.gitbook/assets/Screenshot 2024-08-28 at 10.18.57.png" alt=""><figcaption></figcaption></figure>

または、Web サイトから行うこともできます。メニューから _Your subscriptions_ を選択し、_Manage Subscription_ をクリックしてサブスクリプションページを開きます。サブスクリプションに関する情報と、認証済みのコンピューター一覧が表示されます。

認証解除したいマシンの横にある _De-authorise_ リンクをクリックします。

<figure><img src="../.gitbook/assets/Screenshot 2024-08-28 at 10.16.40.png" alt=""><figcaption></figcaption></figure>

前回の更新以降、そのマシンがオンラインになっていない場合は、すぐに認証解除されます。そうでない場合、そのマシンは認証解除の _queued_ 状態になります。つまり、次にそのマシンがインターネットに接続されたとき、または次回の更新日のどちらか早い時点で、認証解除が自動的に実行されます。
