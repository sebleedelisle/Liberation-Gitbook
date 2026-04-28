---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Preset-systemet

Preset-systemet brukes flere steder i Liberation når det er behov for å lagre flere valgbare innstillinger fra en liste med _presets_.

Systemet brukes for øyeblikket til:

* Scanner-innstillinger
* Fargekalibreringsinnstillinger
* Kamerainnstillinger for 3D visualiser
* Laserinnstillinger for 3D visualiser
* DMX-profiler

Så hvis du finjusterer scanner-innstillingene for de nye, flotte CT6210-scannerne dine, kan du lagre dette som et preset, kalle det "CT6210", og det vil da være tilgjengelig i preset-listen når du trenger det senere, og i nedtrekksmenyen.

Alle presets lagres sammen med prosjektet ditt (eller laserinnstillingene), enten du bruker dem eller ikke. Hver gang du laster inn en av disse filene, blir derfor alle presets i filen lagt til i de eksisterende presetsene dine. Hvis et av de innlastede presetsene har samme navn som et preset du allerede har, overskrives det eksisterende presetet.

Du kan også importere og eksportere preset-filer med load/save-knappen (et diskettikon) ved siden av nedtrekkslisten for presets. Dette åpner et popup-vindu med import/export-knapper, samt mulighet til å slette ett eller flere av presetsene dine.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Popup-menyen som åpnes når du klikker på load/save-ikonet</p></figcaption></figure>

Hvis du redigerer et preset, for eksempel scanner-innstillingen som heter _Default_, må du være klar over at de andre laserne ikke oppdateres automatisk. I stedet vil hver av scanner-innstillingene deres nå merkes som _Default(edited)_. For å oppdatere dette til det nye _Default_-presetet velger du det på nytt fra nedtrekkslisten.

{% hint style="info" %}
Hvis du har mange lasere og vil oppdatere scanner-innstillingene for alle, bruker du _COPY LASER SETTINGS_-systemet. Se [copy-laser-settings.md](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

Hvis du sletter et preset som brukes et annet sted, mister du ikke innstillingen. I stedet vises den som _(deleted)._
