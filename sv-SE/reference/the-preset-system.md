---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Preset-systemet

Preset-systemet används på flera ställen i Liberation när det finns behov av att spara flera valbara inställningar i en lista med _förinställningar_.

Systemet används för närvarande för:

* Scanner-inställningar
* Färgkalibreringsinställningar
* Kamerainställningar för 3D visualiser
* Laserinställningar för 3D visualiser
* DMX-profiler

Om du till exempel justerar scanner-inställningarna för dina nya CT6210-scanners kan du spara det som en förinställning, kalla den "CT6210", och sedan finns den tillgänglig i preset-listan när du behöver den i framtiden och i rullgardinsmenyn.

Alla förinställningar sparas tillsammans med ditt projekt (eller dina laserinställningar), oavsett om du använder dem eller inte. Varje gång du läser in en sådan fil läggs därför alla förinställningar i filen till bland dina befintliga förinställningar. Om en av de inlästa förinställningarna har samma namn som en befintlig förinställning skrivs den befintliga över.

Du kan även importera och exportera preset-filer med load/save-knappen (en diskettikon) bredvid preset-rullgardinslistan. Detta öppnar ett popup-fönster med knappar för import/export samt möjlighet att radera en eller flera av dina förinställningar.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Popup-menyn som öppnas när du klickar på load/save-ikonen</p></figcaption></figure>

Om du redigerar en förinställning, till exempel scanner-inställningen som heter _Default_, uppdateras inte de andra lasrarna automatiskt. I stället får deras scanner-inställningar nu etiketten _Default(edited)_. För att uppdatera detta till den nya _Default_-förinställningen väljer du den igen i rullgardinslistan.

{% hint style="info" %}
Om du har många lasrar och vill uppdatera alla deras scanner-inställningar använder du systemet _COPY LASER SETTINGS_. Se [copy-laser-settings.md](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

Om du raderar en förinställning som används någon annanstans förlorar du inte inställningen, utan ser den i stället markerad som _(deleted)._
