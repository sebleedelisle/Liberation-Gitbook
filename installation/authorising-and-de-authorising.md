# ✅ 授权与取消授权

### 授权 Liberation

首次打开 Liberation 时会以 _demo mode_ 运行，你会看到 _About panel_：

<figure><img src="../.gitbook/assets/authorisation-about-panel.png" alt="" width="375"><figcaption></figcaption></figure>

点击 _AUTHORISE ONLINE_ 按钮，浏览器会打开。如果你尚未登录，会提示你先登录。&#x20;

系统会自动将你的安装与订阅关联完成授权，并显示如下消息：

<figure><img src="../.gitbook/assets/authorisation-machine-added" alt=""><figcaption></figcaption></figure>

返回 Liberation 后，你会看到 _About panel_ 已更新（可能需要等待几秒）。&#x20;

<figure><img src="../.gitbook/assets/authorise-about-panel-authorised" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="warning" %}
如果你的订阅已达到可授权电脑的上限，需要先取消其他电脑的授权，或升级订阅。&#x20;
{% endhint %}

{% hint style="info" %}
如果你有多个订阅，系统会提示你选择要分配给这台电脑的订阅。&#x20;
{% endhint %}

恭喜！你的 Liberation 安装已授权，现在可以输出到激光设备了。但在 arm 激光之前，请先阅读 [getting-started.md](../basics/getting-started.md "mention") 和 [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention")。&#x20;

{% hint style="info" %}
你可以随时通过菜单 _Liberation -> About Liberation_ 或 _Liberation -> Authorise/Deauthorise this computer_ 打开 _About panel_。
{% endhint %}

### 取消 Liberation 授权

**在 Liberation 内操作**：打开菜单 _Liberation -> Authorise / De-authorise this Computer_，点击 _DEAUTHORISE COMPUTER_ 按钮即可。此操作需要联网。

<figure><img src="../.gitbook/assets/Screenshot 2024-08-28 at 10.18.57.png" alt=""><figcaption></figcaption></figure>

也可以在网站上操作：在菜单中选择 _Your subscriptions_，然后点击 _Manage Subscription_ 打开订阅页面。你会看到订阅信息和已授权的电脑列表。

点击要取消授权的电脑旁边的 _De-authorise_ 链接。

<figure><img src="../.gitbook/assets/Screenshot 2024-08-28 at 10.16.40.png" alt=""><figcaption></figcaption></figure>

如果该电脑自上次续订以来没有联网，会立即取消授权。否则会进入 _queued_ 状态，等该电脑下次联网或到达下一次续订日期时自动取消授权，以先发生者为准。&#x20;
