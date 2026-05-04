---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Preset 系统

Preset 系统会在 Liberation 的多个位置使用，用于存储并从 _presets_ 列表中选择多组设置。&#x20;

目前该系统用于：&#x20;

* Scanner settings
* Colour calibration settings
* 3D visualiser camera settings
* 3D visualiser laser settings
* DMX profiles

例如你为新买的 CT6210 扫描器调好设置后，可以存为一个 preset，命名为 “CT6210”。以后需要时，它会出现在 preset 列表和下拉菜单中。

所有 presets 都会随项目（或激光设置）一起保存，无论你是否正在使用它们。所以每次加载这些文件时，里面的所有 presets 都会加入到你现有的 presets 中。如果加载的 preset 名称与现有名称相同，会覆盖现有 preset。&#x20;

你也可以使用 preset 下拉列表旁的 load/save 按钮（软盘图标）来导入/导出 preset 文件。它会打开一个弹窗，包含导入/导出按钮，以及删除一个或多个 preset 的选项。

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>The pop-up menu that opens when you click the load/save icon</p></figcaption></figure>

如果你编辑了某个 preset，比如名为 _Default_ 的扫描器设置，请注意其他激光不会自动更新。它们的扫描器设置会显示为 _Default(edited)_。要更新到新的 _Default_ preset，请在下拉列表中重新选择它。&#x20;

{% hint style="info" %}
如果你有很多激光且想更新它们的扫描器设置，使用 _COPY LASER SETTINGS_ 系统。见 [在激光之间复制设置](../setting-up/copy-laser-settings.md "mention")。
{% endhint %}

如果你删除了一个正在使用的 preset，不会丢失设置，但它会显示为 _(deleted)_。&#x20;
