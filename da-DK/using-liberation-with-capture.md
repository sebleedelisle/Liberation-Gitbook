---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Brug Liberation med Capture

Liberation understøtter [Capture](https://capture.se) som ekstern visualiser (fra version 1.0.3). Hvis du allerede bruger Capture i dit workflow, kan du bruge det til at visualisere Liberations live-laseroutput i din 3D-scene.

### Sådan fungerer det

Der kræves ingen særlig forbindelsesproces eller manuel sammenkobling.

Så længe:

* Liberation og Capture er på samme netværk
* Din firewall tillader forbindelsen

…vil alle lasere, du har sat op i Liberation, automatisk blive vist i Capture som mediekilder. Du behøver ikke konfigurere IP-adresser eller aktivere noget særligt – de vises bare.

### Se lasere i Capture

Alle konfigurerede lasere i Liberation vises i Capture som tilgængelige mediekilder.

For rent faktisk at se output:

* Laseren skal være armeret i Liberation
* Kilden skal være knyttet til et laserfixture i Capture

Når laseren er armeret, visualiserer Capture live-outputstreamen fra Liberation. Hvis en laser dearmeres i Liberation, forbliver den synlig i Capture som kilde, men den sender ikke noget output.

Se dokumentationen på [capture.se](https://www.capture.se/) for flere instruktioner og support til opsætning af lasere i Capture. <br>

### Licensgrænser og armerede lasere

Forbindelser til Capture behandles præcis som fysiske laseroutput.

Det betyder:

* Du kan kun armere så mange lasere, som dit licensniveau tillader
* Kun armerede lasere sender aktivt data til Capture

### Har jeg brug for Capture?

Slet ikke.

Liberation har en indbygget 3D-visualiser, som altid er tilgængelig og ikke afhænger af dit licensniveau. Du kan designe og forhåndsvise shows direkte i Liberation uden ekstern software.

Capture er blot en ekstra mulighed, hvis du allerede bruger det til lys- eller showdesign.

### Fejlfinding

Hvis lasere ikke vises i Capture:

* Kontrollér, at begge programmer er på samme netværk
* Kontrollér dine firewallindstillinger
* Sørg for, at laseren er armeret i Liberation
