---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Ustabil / blinkende output

Åpne panelet _Laser Overview_ og se på tilkoblingslampen ved siden av laseren du har problemer med.

**Hvis tilkoblingslampen IKKE lyser konstant grønt:**\
Da har du enten et nettverksproblem eller et problem med CPU-ytelsen:

**Nettverksytelse -**

* Sørg for at du ikke er koblet til et wifi-nettverk. Du bør alltid bruke kablet tilkobling. Sørg for at operativsystemet prioriterer det kablede nettverket over wifi, eller deaktiver wifi hvis du er usikker
* Sjekk nettverksadapteren din – og prøv en annen USB-C-adapter
* Windows-brukere – sjekk / oppgrader nettverksdriverne, og kjør relevante verktøy for nettverkstesting
* Sjekk all kabling, svitsjer og rutere. Bytt ut og test hver kabel systematisk.
* Start alt nettverksutstyret på nytt, inkludert svitsjer, rutere og hver Ether Dream.

**CPU-ytelse**

Hvis du har en gammel maskin eller en maskin med lave spesifikasjoner, kan den være for treg til å kjøre Liberation. Sjekk indikatoren for bildefrekvens på høyre side av ikonlinjen.

Det vises to tall der – faktisk bildefrekvens og målbildefrekvens. Hvis den faktiske bildefrekvensen faller under 30, kan du få problemer.

Følgende tiltak kan hjelpe:

* Fjern lasere som ikke er i bruk, f.eks. hvis du bare har én laser tilkoblet, slett de andre.
* Bytt til Output- eller Canvas-visningen
* Lukk alle andre programmer, sjekk brannmurinnstillinger for nettverk, lukk antivirus, Dropbox osv.
* Reduser skjermoppløsningen, og gjør Liberation-vinduet mindre

Hvis ingenting av dette fungerer, bør du vurdere å oppgradere datamaskinen.

***

**Hvis tilkoblingslampen lyser konstant grønt:**

Da er det sannsynligvis et maskinvareproblem. Dette ligger utenfor omfanget av denne manualen, men du kan prøve følgende tiltak:

* Deaktiver SFS-systemet (Scan Fail Safety). Noen lasere har en funksjon som deaktiverer output hvis skannerne slutter å bevege seg, altså hvis de lager en kraftig statisk stråle. De kan være litt overforsiktige / upålitelige.

{% hint style="danger" %}
Vær ekstremt forsiktig når du deaktiverer Scan Fail Safety-systemet. Kraftige statiske stråler kan forårsake brannskader! Sørg for at du har en stoppknapp og et brannslukningsapparat tilgjengelig.
{% endhint %}

* Sjekk sikkerhetsinterlock-kabler og -systemer
* Sjekk all kabling mellom kontrolleren og laseren.

En [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) kan være et uvurderlig verktøy for feilsøking av laserproblemer.
