# ✅ The Preset system

The Preset system is throughout various places in Liberation whenever there is a requirement to store multiple selectable settings from a list of _presets_.&#x20;

This system is currently used for :&#x20;

* Scanner settings
* Colour calibration settings
* 3D visualiser camera settings
* 3D visualiser laser settings
* DMX profiles

So if you tune scanner settings for your fancy new CT6210 scanners, you can store that as a preset, call it "CT6210" and it will then be available in the preset list whenever you need it in future and available in the drop-down menu.&#x20;

All of the presets are saved along with your project (or laser settings) whether you are using them or not. So any time you load one of these files, all of the presets inside will be added to your existing presets. If one of the loaded presets has the same name as one of your existing presets, it will overwrite the existing preset.&#x20;

You can additionally import and export preset files using the load/save button (a floppy disk icon) next to the preset drop-down list. This opens a pop up that has import/export buttons and also the option to delete one or more of your presets.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2025-03-21 at 13.45.51.png" alt=""><figcaption><p>The pop up menu that opens when you click the load/save icon</p></figcaption></figure>

If you edit a preset, let's say the scanner setting called _Default_, note that the other lasers won't be automatically updated. Instead each of their scanner settings will now be labelled _Default(edited)_. To update this to the new _Default_ preset, re-select it from the drop-down list.&#x20;

{% hint style="info" %}
If you have a lot of lasers and want to update all of their scanner settings, use the _COPY LASER SETTINGS_ system. See [copy-laser-settings.md](../setting-up/laser-settings/copy-laser-settings.md "mention")
{% endhint %}

If you delete a preset that is used elsewhere, you will not lose the setting, but instead see it labelled as _(deleted)._&#x20;

