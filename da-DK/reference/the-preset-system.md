---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Preset-systemet

Preset-systemet bruges flere steder i Liberation, når der er behov for at gemme flere valgbare indstillinger fra en liste med _presets_.

Systemet bruges i øjeblikket til:

* Scannerindstillinger
* Farvekalibreringsindstillinger
* Kameraindstillinger for 3D Visualiser
* Laserindstillinger for 3D Visualiser
* DMX-profiler

Så hvis du finjusterer scannerindstillingerne til dine nye CT6210-scannere, kan du gemme dem som et preset, kalde det "CT6210", og det vil derefter være tilgængeligt i presetlisten, når du får brug for det fremover, og i rullemenuen.

Alle presets gemmes sammen med dit projekt (eller dine laserindstillinger), uanset om du bruger dem eller ej. Hver gang du indlæser en af disse filer, bliver alle presets i filen derfor føjet til dine eksisterende presets. Hvis et af de indlæste presets har samme navn som et af dine eksisterende presets, overskriver det det eksisterende preset.

Du kan også importere og eksportere presetfiler med load/save-knappen (et disketteikon) ved siden af preset-rullelisten. Dette åbner et pop op-vindue med import-/eksportknapper samt mulighed for at slette et eller flere af dine presets.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Pop op-menuen, der åbnes, når du klikker på load/save-ikonet</p></figcaption></figure>

Hvis du redigerer et preset, for eksempel scannerindstillingen _Default_, skal du være opmærksom på, at de andre lasere ikke opdateres automatisk. I stedet vil hver af deres scannerindstillinger nu være mærket _Default(edited)_. For at opdatere dette til det nye _Default_-preset skal du vælge det igen fra rullelisten.

{% hint style="info" %}
Hvis du har mange lasere og vil opdatere scannerindstillingerne for dem alle, skal du bruge _COPY LASER SETTINGS_-systemet. Se [copy-laser-settings.md](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

Hvis du sletter et preset, der bruges et andet sted, mister du ikke indstillingen. Den vil i stedet blive vist som _(deleted)._
