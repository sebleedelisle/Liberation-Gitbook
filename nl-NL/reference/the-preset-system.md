---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Het Preset-systeem

Het Preset-systeem wordt op verschillende plekken in Liberation gebruikt wanneer je meerdere selecteerbare instellingen uit een lijst met _presets_ moet kunnen opslaan.

Dit systeem wordt momenteel gebruikt voor:

* Scanner-instellingen
* Kleurkalibratie-instellingen
* Camera-instellingen voor de 3D Visualiser
* Laserinstellingen voor de 3D Visualiser
* DMX-profielen

Dus als je scanner-instellingen afstemt voor je nieuwe CT6210-scanners, kun je die als preset opslaan, bijvoorbeeld met de naam "CT6210". Daarna is deze preset beschikbaar in de presetlijst wanneer je hem later nodig hebt, en kun je hem kiezen via het drop-downmenu.

Alle presets worden samen met je project (of laserinstellingen) opgeslagen, of je ze nu gebruikt of niet. Telkens wanneer je een van deze bestanden laadt, worden alle presets daarin toegevoegd aan je bestaande presets. Als een geladen preset dezelfde naam heeft als een van je bestaande presets, wordt de bestaande preset overschreven.

Je kunt presetbestanden ook importeren en exporteren met de load/save-knop (een diskettepictogram) naast de preset-drop-downlijst. Hiermee open je een pop-up met import/export-knoppen en ook de optie om een of meer van je presets te verwijderen.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Het pop-upmenu dat wordt geopend wanneer je op het load/save-pictogram klikt</p></figcaption></figure>

Als je een preset bewerkt, bijvoorbeeld de scanner-instelling met de naam _Default_, houd er dan rekening mee dat de andere lasers niet automatisch worden bijgewerkt. In plaats daarvan krijgen hun scanner-instellingen nu het label _Default(edited)_. Om dit bij te werken naar de nieuwe _Default_-preset, selecteer je die opnieuw in de drop-downlijst.

{% hint style="info" %}
Als je veel lasers hebt en de scanner-instellingen van allemaal wilt bijwerken, gebruik dan het _COPY LASER SETTINGS_-systeem. Zie [Instellingen kopiëren tussen lasers](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

Als je een preset verwijdert die ergens anders wordt gebruikt, raak je de instelling niet kwijt. In plaats daarvan zie je dat deze het label _(deleted)_ krijgt.
