---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/unable-to-deauthorise-on-windows
---

# ✅ Kan du ikke deautorisere på Windows?

#### Kan du ikke deautorisere på Windows?

Hvis du ikke kan deautorisere en computer på Windows, skal du først sikre dig, at du deautoriserer licensen med den samme version af Liberation, som oprindeligt autoriserede den, før du autoriserer den igen i en anden version.

Hvis dette ikke virker, og du bruger en version tidligere end 1.0, skyldes problemet sandsynligvis den måde, ældre Windows-builds af Liberation identificerede computeren på. I disse versioner var det system, der blev brugt til at generere et maskin-id, mindre pålideligt, og i nogle tilfælde kunne id'et ændre sig mellem genstarter, selvom der ikke tydeligt var ændret hardware.

Hvis du sidder fast og prøver at deautorisere, og du ikke har skiftet version, kan du kontakte support@liberationlaser.com, så kan vi deautorisere maskinen manuelt for dig.

**Hvorfor dette sker**

I tidlige Windows-builds af Liberation (før 1.0) brugte vi den anbefalede Windows-systemmetode til at generere et maskin-id. Desværre viste den sig at være inkonsekvent i nogle situationer. Derfor blev licenssystemet omskrevet til version 1.0, så det bruger en mere robust kombination af metoder, som nu fungerer pålideligt.

Som følge heraf kan det computer-id, der bruges af ældre versioner af Liberation, være forskelligt fra det, der bruges af aktuelle versioner. Hvis id'et allerede har ændret sig, skal support håndtere deautoriseringen manuelt.

***
