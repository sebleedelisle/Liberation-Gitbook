---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Das Preset-System

Das Preset-System wird an verschiedenen Stellen in Liberation verwendet, immer dann, wenn mehrere auswählbare Einstellungen in einer Liste von _Presets_ gespeichert werden sollen.

Dieses System wird derzeit verwendet für:

* Scanner-Einstellungen
* Einstellungen zur Farbkalibrierung
* Kameraeinstellungen des 3D Visualiser
* Lasereinstellungen des 3D Visualiser
* DMX-Profile

Wenn du also die Scanner-Einstellungen für deine neuen CT6210-Scanner einrichtest, kannst du sie als Preset speichern, es „CT6210“ nennen, und es steht dir künftig jederzeit in der Preset-Liste sowie im Dropdown-Menü zur Verfügung.

Alle Presets werden zusammen mit deinem Projekt (oder deinen Lasereinstellungen) gespeichert, unabhängig davon, ob du sie verwendest oder nicht. Jedes Mal, wenn du eine dieser Dateien lädst, werden alle darin enthaltenen Presets zu deinen vorhandenen Presets hinzugefügt. Wenn eines der geladenen Presets denselben Namen hat wie eines deiner vorhandenen Presets, wird das vorhandene Preset überschrieben.

Zusätzlich kannst du Preset-Dateien über den Load/Save-Button (ein Diskettensymbol) neben der Preset-Dropdown-Liste importieren und exportieren. Dadurch öffnet sich ein Pop-up mit Import-/Export-Buttons und der Möglichkeit, eines oder mehrere deiner Presets zu löschen.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Das Pop-up-Menü, das sich öffnet, wenn du auf das Load/Save-Symbol klickst</p></figcaption></figure>

Wenn du ein Preset bearbeitest, zum Beispiel die Scanner-Einstellung namens _Default_, beachte, dass die anderen Laser nicht automatisch aktualisiert werden. Stattdessen werden ihre Scanner-Einstellungen nun als _Default(edited)_ gekennzeichnet. Um sie auf das neue _Default_-Preset zu aktualisieren, wähle es erneut in der Dropdown-Liste aus.

{% hint style="info" %}
Wenn du viele Laser hast und alle ihre Scanner-Einstellungen aktualisieren möchtest, verwende das System _COPY LASER SETTINGS_. Siehe [Einstellungen zwischen Lasern kopieren](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

Wenn du ein Preset löschst, das an anderer Stelle verwendet wird, verlierst du die Einstellung nicht. Sie wird stattdessen als _(deleted)._ gekennzeichnet.
