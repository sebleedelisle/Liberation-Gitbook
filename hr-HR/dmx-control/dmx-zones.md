---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# 🟩 DMX zones

DMX zones su Liberation izlazne zone koje šalju Art-Net/DMX umjesto laserskih točaka. Prikazuju se uz beam zone i canvas zone, pa im se Clips mogu dodjeljivati istim postupkom odabira zone.

Otvorite **DMX Zones** iz izbornika ili upotrijebite odjeljak DMX u Laser overview za upravljanje njima.

* **ADD DMX ZONE** - stvara novu DMX zone.
* **ARM** - omogućuje DMX izlaz za tu zone. DMX zone koja nije aktivirana briše svoje mapirane kanale na nulu.
* **Node** - odabire broj Art-Net node.
* **Universe** - odabire Art-Net universe. Prikazana vrijednost počinje od 1, pa je Universe 1 prvi universe.
* **Address** - postavlja početnu adresu rasvjetnog uređaja. Prikazana vrijednost također počinje od 1.
* **Preset** - odabire DMX preset koji mapira sadržaj Clip na DMX kanale.
* **Edit DMX zone settings** (ikona olovke) - otvara postavke zone, kao što su ručno prosljeđivanje zone i orijentacija rasvjetnog uređaja.
* **Edit DMX profile/channel mapping** (ikona klizača) - otvara editor za DMX preset/kanale.
* **Delete** - uklanja DMX zone.

### Ograničenja aktiviranja

Broj DMX zones koje mogu biti istodobno aktivirane ovisi o razini vaše licence. Ako vaša razina ne dopušta DMX izlaz ili ste već aktivirali najveći dopušteni broj DMX zones, gumb **ARM** za dodatne zone onemogućen je i pri prelasku pokazivačem prikazuje ikonu zabrane ulaza.

Prije aktiviranja dodatnih zone deaktivirajte neku drugu DMX zone ili upotrijebite razinu licence s višim DMX ograničenjem.
