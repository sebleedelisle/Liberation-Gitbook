---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# 🟩 DMX-soner

DMX zones er Liberation output zones som sender Art-Net/DMX i stedet for laserpunkter. De vises sammen med beam zones og canvas zones, slik at Clips kan tilordnes dem med den samme arbeidsflyten i zone-velgeren.

Åpne **DMX Zones** fra menyen, eller bruk DMX-delen i Laser overview, for å administrere dem.

* **ADD DMX ZONE** – oppretter en ny DMX zone.
* **ARM** – aktiverer DMX-utgang for denne zone. En DMX zone som ikke er aktivert, nullstiller de tilordnede kanalene.
* **Node** – velger Art-Net node-nummeret.
* **Universe** – velger Art-Net-universet. Verdien som vises er 1-basert, så Universe 1 er det første universet.
* **Address** – angir startadressen til armaturen. Verdien som vises er også 1-basert.
* **Preset** – velger DMX-forhåndsinnstillingen som tilordner Clip-innhold til DMX-kanaler.
* **Edit DMX zone settings** (blyantikon) – åpner innstillinger for zone, for eksempel manuell videresending av zone og retning for armaturen.
* **Edit DMX profile/channel mapping** (skyvebryterikon) – åpner editoren for DMX-forhåndsinnstilling/kanaler.
* **Delete** – fjerner DMX zone.

### Aktiveringsgrenser

Hvor mange DMX zones som kan være aktivert samtidig, avhenger av lisensnivået ditt. Hvis nivået ditt ikke tillater DMX-utgang, eller du allerede har aktivert maksimalt antall DMX zones, er **ARM**-knappen for flere zones deaktivert og viser et adgang forbudt-ikon når du holder pekeren over den.

Deaktiver en annen DMX zone, eller bruk et lisensnivå med høyere DMX-grense, før du aktiverer flere zones.
