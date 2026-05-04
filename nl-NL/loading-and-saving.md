---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Laden en opslaan

Liberation slaat de huidige staat continu op schijf op. Zo weet je zeker dat het programma na een stroomstoring of systeemprobleem weer opstart waar het was gebleven. Je zou je zones, tijdlijn of andere content dus niet moeten kwijtraken.

Je kunt je setup daarnaast exporteren voor een back-up of om deze naar een andere computer over te zetten.

### Project importeren/exporteren

Het projectbestand slaat bijna alles uit je huidige setup op, waaronder:

* Alles wat hieronder wordt beschreven bij [Laden en opslaan](loading-and-saving.md#laser-settings-import-export "mention")
* Clips, effecten en groepsinstellingen
* Al je tijdlijnen (zonder audio- en videomedia)
* Art-Net-setup
* Instellingen voor MIDI verzenden/ontvangen
* Tempo- en synchronisatie-instellingen

Momenteel worden de volgende zaken niet opgeslagen en geladen:

* Instellingen voor Sound- en MIDI-invoer zoals gebruikt in de MIDI notes-node en de Sound Input Oscillator (instellingen voor MIDI verzenden/ontvangen worden _wel_ opgeslagen, net als de geluidsinvoer voor timecode)
* Interfaceschaling
* Media voor Canvas-hulpafbeeldingen
* Geluids- en videomedia voor tijdlijnen
* Lettertypen die in de Text-node worden gebruikt

{% hint style="danger" %}
Geluids- en videobestanden in de tijdlijn worden niet opgeslagen in projectbestanden. Sla ze dus apart op als je ze naar een andere computer wilt overzetten. Zie [Laden en opslaan](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Laserinstellingen importeren/exporteren

* Laserinstellingen voor elke laser
* Beam-zones
* Canvas-doelgebieden
* DMX-zones
* Toewijzing van lasercontrollers (en aliassen voor controllers die je een andere naam hebt gegeven)
* Kalibratie-instellingen en presets voor laserscanners en kleuren
* Instellingen en presets voor de 3D Visualiser

### Clip Deck importeren/exporteren

* Alle clips en hun zonetoewijzingen, instellingen en parameters
* Alle groepsinstellingen, flash mode, fade in/out-tijden enzovoort

Momenteel worden de volgende zaken niet opgeslagen en geladen:

* Alle effecten en hun parameters en instellingen

{% hint style="info" %}
**Clips uit een projectbestand laden zonder het hele project te laden**

Als je alleen de clips uit een project wilt importeren, selecteer je _**Clips->Import Clip Deck**_ en kies je in plaats van een Clip Deck-bestand (.cpdk) een projectbestand.
{% endhint %}

### Clip Deck toevoegen

Je kunt clips uit een geëxporteerd Clip Deck-bestand aan je huidige project toevoegen met _Append Clip Deck_. Clips worden toegevoegd aan het einde van je huidige Clip Deck, maar de effecten en groepsinstellingen in het bestand worden niet geïmporteerd.

### Geselecteerde clips exporteren

Alle clips die op dat moment geselecteerd zijn, worden naar een bestand geëxporteerd. Groepsinstellingen en effecten worden niet opgeslagen, alleen de clips. Let op: actieve clips die op dat moment afspelen, worden niet geëxporteerd tenzij ze ook geselecteerd zijn.

{% hint style="info" %}
Gebruik Option/Alt - shift - click op clips om ze te selecteren (of gebruik de lasso). Je herkent geselecteerde clips aan de dikke witte omlijning eromheen. Zie [Clips starten / stoppen](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Effecten importeren/exporteren

Laadt en slaat alle effecten op, samen met hun groepsinstellingen en parameters.

{% hint style="info" %}
**Effecten uit een projectbestand laden zonder het hele project te laden**

Als je alleen de effecten uit een project wilt importeren, selecteer je _**Effects->Import Effects**_ en kies je in plaats van een effectenbestand (.efts) een projectbestand.
{% endhint %}

### Tijdlijn exporteren

Exporteer een tijdlijnbestand met één of meer tijdlijnen. Let op: de Clip Deck wordt altijd opgenomen in geëxporteerde tijdlijnbestanden (hoewel je kunt kiezen welke Clips je later weer importeert, zie [tijdlijn importeren](loading-and-saving.md#timeline-import "mention") hieronder).

Als je projectbestand meer dan één tijdlijn bevat, wordt er een paneel geopend waarin je kunt selecteren welke tijdlijnen je wilt exporteren.

{% hint style="danger" %}
Geluids- en videobestanden in de tijdlijn worden niet opgeslagen in tijdlijnbestanden. Sla ze dus apart op als je je content naar een andere computer wilt overzetten. Zie [Laden en opslaan](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Tijdlijn importeren

Importeer één of meer tijdlijnen uit één tijdlijnbestand. Nadat je het tijdlijnbestand hebt geselecteerd, wordt er een paneel geopend met meerdere importopties.

Als het tijdlijnbestand meer dan één tijdlijn bevat, worden ze allemaal weergegeven. Vink de tijdlijnen aan die je wilt opnemen.

* Replace existing timelines\
  Verwijdert al je huidige tijdlijnen en vervangt ze door de geïmporteerde tijdlijnen
* Import used clips only\
  Importeert alleen de gebruikte clips en plaatst de clips in groepen, één groep per tijdlijn. Als deze optie niet is geselecteerd, wordt de volledige Clip Deck uit het tijdlijnbestand aan je bestaande clips toegevoegd.
* Replace existing clip deck\
  Vervangt je huidige Clip Deck door de clips in het tijdlijnbestand. Alleen beschikbaar als _Replace existing timelines_ is geselecteerd.

{% hint style="info" %}
**Tijdlijnen uit een projectbestand laden zonder het hele project te laden**

Als je alleen de tijdlijnen uit een project wilt importeren, selecteer je _**Timeline->Import Timeline(s)**_ en kies je in plaats van een tijdlijnbestand (.ltml) een projectbestand.
{% endhint %}

### DMX / Art-Net importeren/exporteren

Slaat de Art-Net-nodes en hun IP-adressen op en laadt ze weer. Bevat ook de DMX-zones en al je DMX-presets.

### Belangrijke opmerking over mediabestanden voor tijdlijnen

Geluids- en videobestanden worden momenteel **niet** met het tijdlijnbestand geëxporteerd. Als je content naar een andere computer moet verplaatsen, zorg er dan voor dat je deze bestanden ook meeneemt.

{% hint style="info" %}
**Hoe een tijdlijn naar mediabestanden zoekt**

Wanneer de tijdlijn wordt geladen, kijkt deze in dezelfde map als het tijdlijn- of projectbestand en zoekt daarin en in alle submappen. Zolang de bestanden dus in dezelfde map of in een submap staan (zoals _/videos_ of _/sound_), worden ze gevonden bij het laden.
{% endhint %}
