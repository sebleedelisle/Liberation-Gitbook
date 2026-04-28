---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Bruke Liberation med Capture

Liberation støtter [Capture](https://capture.se) som ekstern visualiserer (fra og med versjon 1.0.3). Hvis du allerede bruker Capture i arbeidsflyten din, kan du bruke det til å visualisere Liberation sin direkte laserutgang i 3D-scenen din.

### Slik fungerer det

Det kreves ingen egen tilkoblingsprosess eller manuell kobling.

Så lenge:

* Liberation og Capture er på samme nettverk
* Brannmuren din tillater tilkoblingen

…vil alle lasere du har satt opp i Liberation, automatisk vises i Capture som mediekilder. Du trenger ikke å konfigurere IP-adresser eller aktivere noe spesielt – de bare dukker opp.

### Se lasere i Capture

Alle konfigurerte lasere i Liberation vises i Capture som tilgjengelige mediekilder.

For å faktisk se utgangssignalet:

* Laseren må være armert i Liberation
* Kilden må være knyttet til en laser-fixture i Capture

Når laseren er armert, visualiserer Capture den direkte utgangsstrømmen fra Liberation. Hvis en laser deaktiveres i Liberation, vil den fortsatt være synlig i Capture som en kilde, men den sender ikke ut noe.

Se dokumentasjonen på [capture.se](https://www.capture.se/) for flere instruksjoner og støtte for oppsett av lasere i Capture. <br>

### Lisensgrenser og armerte lasere

Tilkoblinger til Capture behandles på nøyaktig samme måte som fysiske laserutganger.

Det betyr:

* Du kan bare armere så mange lasere som lisensnivået ditt tillater
* Bare armerte lasere sender aktivt data til Capture

### Trenger jeg Capture?

Nei, ikke i det hele tatt.

Liberation har en innebygd 3D Visualiser, som alltid er tilgjengelig og ikke avhenger av lisensnivået ditt. Du kan designe og forhåndsvise show direkte i Liberation uten ekstern programvare.

Capture er ganske enkelt et ekstra alternativ hvis du allerede bruker det til lys- eller showdesign.

### Feilsøking

Hvis lasere ikke vises i Capture:

* Kontroller at begge programmene er på samme nettverk
* Kontroller brannmurinnstillingene dine
* Sørg for at laseren er armert i Liberation
