---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Periodisk / blinkende output

Åbn panelet _Laser Overview_, og se på forbindelseslyset ud for den laser, du har problemer med.

**Hvis forbindelseslyset IKKE er konstant grønt:**\
Så har du enten et netværksproblem eller et problem med CPU-ydelsen:

**Netværksydelse -**

* Sørg for, at du ikke er forbundet til et wifi-netværk. Du bør altid bruge en kablet forbindelse. Sørg for, at dit operativsystem prioriterer det kablede netværk over wifi, eller deaktiver wifi, hvis du er i tvivl
* tjek din netværksadapter – og prøv en anden USB-C-adapter
* Windows-brugere – tjek / opdater dine netværksdrivere, og kør de relevante netværkstestværktøjer
* tjek alle kabler, switche og routere. Udskift og test hvert kabel systematisk.
* genstart alt dit netværksudstyr, inklusive switche, routere og hver Ether Dream.

**CPU-ydelse**

Hvis du har en gammel eller lavt specificeret computer, kan den være for langsom til at køre Liberation. Tjek billedhastighedsindikatoren i højre side af ikonlinjen.

Der vises to tal – den faktiske billedhastighed og målbilledhastigheden. Hvis den faktiske billedhastighed falder til under 30, kan du opleve problemer.

Følgende kan hjælpe:

* fjern ubrugte lasere, dvs. hvis du kun har én laser tilsluttet, så slet de andre.
* Skift til Output- eller Canvas-visningen
* Luk alle andre programmer, tjek firewallindstillinger for netværket, luk antivirus, Dropbox osv.
* Reducer din skærmopløsning, og gør Liberation-vinduet mindre

Hvis intet af dette virker, bør du overveje at opgradere din computer.

***

**Hvis forbindelseslyset ER konstant grønt:**

Så er der sandsynligvis tale om et hardwareproblem. Det ligger uden for denne manuals område, men du kan prøve følgende:

* Deaktiver SFS-systemet (Scan Fail Safety). Nogle lasere har en funktion, der deaktiverer output, hvis scannerne holder op med at bevæge sig, dvs. hvis de producerer en kraftig statisk stråle. De kan være lidt for forsigtige / upålidelige.

{% hint style="danger" %}
Vær ekstremt forsigtig, når du deaktiverer scan fail safety-systemet. Kraftige statiske stråler kan forårsage brandmærker! Sørg for at have en stopknap og en brandslukker ved hånden.
{% endhint %}

* Tjek sikkerhedsinterlock-kabler og -systemer
* Tjek alle kabler mellem controlleren og laseren.

En [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) kan være et uvurderligt værktøj til fejlfinding af laserproblemer.
