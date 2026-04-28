---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/unable-to-deauthorise-on-windows
---

# ✅ Kan du inte avauktorisera på Windows?

#### Kan du inte avauktorisera på Windows?

Om du inte kan avauktorisera en dator på Windows ska du först kontrollera att du avauktoriserar licensen med samma version av Liberation som ursprungligen auktoriserade den, innan du auktoriserar den igen i en annan version.

Om detta inte fungerar och du använder en version äldre än 1.0 beror problemet troligen på hur äldre Windows-versioner av Liberation identifierade datorn. I de versionerna var systemet som användes för att skapa ett maskin-ID mindre tillförlitligt, och i vissa fall kunde ID:t ändras mellan omstarter även om ingen maskinvara uppenbart hade ändrats.

Om du har fastnat när du försöker avauktorisera och inte har bytt version, kontakta support@liberationlaser.com så kan vi avauktorisera datorn manuellt åt dig.

**Varför detta händer**

I tidiga Windows-versioner av Liberation (före 1.0) använde vi den rekommenderade Windows-systemmetoden för att skapa ett maskin-ID. Tyvärr visade den sig vara inkonsekvent i vissa situationer. Därför skrevs licenssystemet om inför version 1.0 för att använda en mer robust kombination av metoder, som nu fungerar tillförlitligt.

Det innebär att dator-ID:t som används av äldre versioner av Liberation kan skilja sig från det som används av aktuella versioner. Om ID:t redan har ändrats måste support hantera avauktoriseringen manuellt.

***
