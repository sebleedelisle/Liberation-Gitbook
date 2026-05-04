---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ DMX-zoner

DMX zones er Liberation-output zones, der sender Art-Net/DMX i stedet for laserpunkter. De vises sammen med beam zones og canvas zones, så Clips kan tildeles dem i den samme arbejdsgang med zone-vælgeren.

Åbn **DMX Zones** fra menuen, eller brug DMX-afsnittet i Laser Overview, for at administrere dem.

* **ADD DMX ZONE** - opretter en ny DMX zone.
* **ARM** - aktiverer DMX-output for den pågældende zone. En DMX zone, der ikke er aktiveret, nulstiller sine tilknyttede kanaler.
* **Node** - vælger Art-Net node-nummeret.
* **Universe** - vælger Art-Net-universet. Den viste værdi er 1-baseret, så Universe 1 er det første univers.
* **Address** - angiver fixture-enhedens startadresse. Den viste værdi er også 1-baseret.
* **Preset** - vælger den DMX-preset, der mapper Clip-indhold til DMX-kanaler.
* **Edit DMX zone settings** (blyantikon) - åbner zone-indstillinger som manuel zone-videresendelse og fixture-orientering.
* **Edit DMX profile/channel mapping** (skyderikon) - åbner editoren til DMX-presets/kanaler.
* **Delete** - fjerner DMX zone.

### Aktiveringsgrænser

Antallet af DMX zones, der kan være aktiveret samtidig, afhænger af dit licensniveau. Hvis dit niveau ikke tillader DMX-output, eller hvis du allerede har aktiveret det maksimale antal DMX zones, er knappen **ARM** for yderligere zones deaktiveret og viser et adgang-forbudt-ikon, når du holder markøren over den.

Deaktiver en anden DMX zone, eller brug et licensniveau med en højere DMX-grænse, før du aktiverer flere zones.
