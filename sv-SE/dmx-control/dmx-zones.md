---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ DMX-zoner

DMX zone är Liberation-output zones som skickar Art-Net/DMX i stället för laserpunkter. De visas tillsammans med beam zone och canvas zone, så Clips kan tilldelas dem i samma arbetsflöde för zone selector.

Öppna **DMX Zones** från menyn, eller använd DMX-avsnittet i Laser Overview, för att hantera dem.

* **ADD DMX ZONE** - skapar en ny DMX zone.
* **ARM** - aktiverar DMX-output för den zonen. En DMX zone som inte är aktiverad nollställer sina mappade kanaler.
* **Node** - väljer Art-Net node-nummer.
* **Universe** - väljer Art-Net-universe. Värdet som visas är 1-baserat, så Universe 1 är det första universe.
* **Address** - anger armaturens startadress. Värdet som visas är också 1-baserat.
* **Preset** - väljer den DMX-preset som mappar Clip-innehåll till DMX-kanaler.
* **Edit DMX zone settings** (pennikon) - öppnar inställningar för zonen, till exempel manuell zone forwarding och armaturens orientering.
* **Edit DMX profile/channel mapping** (reglageikon) - öppnar editorn för DMX-preset/kanalmappning.
* **Delete** - tar bort DMX zone.

### Aktiveringsgränser

Hur många DMX zones som kan vara aktiverade samtidigt beror på din licensnivå. Om din nivå inte tillåter DMX-output, eller om du redan har aktiverat det maximala antalet DMX zones, är knappen **ARM** inaktiverad för fler zoner och visar en förbudssymbol när du håller pekaren över den.

Inaktivera en annan DMX zone, eller använd en licensnivå med högre DMX-gräns, innan du aktiverar fler zoner.
