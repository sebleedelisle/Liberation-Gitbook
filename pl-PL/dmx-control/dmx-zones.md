---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ Strefy DMX

DMX zone to strefy Output w Liberation, które wysyłają Art-Net/DMX zamiast punktów lasera. Są widoczne obok beam zone i canvas zone, więc Clips można przypisywać do nich w tym samym procesie wyboru zone.

Aby nimi zarządzać, otwórz **DMX Zones** z menu albo użyj sekcji DMX w Laser Overview.

* **ADD DMX ZONE** — tworzy nową DMX zone.
* **ARM** — włącza wyjście DMX dla tej zone. DMX zone, która nie jest uzbrojona, zeruje przypisane do niej kanały.
* **Node** — wybiera numer node Art-Net.
* **Universe** — wybiera universe Art-Net. Wyświetlana wartość jest liczona od 1, więc Universe 1 to pierwszy universe.
* **Address** — ustawia adres początkowy urządzenia. Wyświetlana wartość również jest liczona od 1.
* **Preset** — wybiera preset DMX, który mapuje zawartość Clip na kanały DMX.
* **Edit DMX zone settings** (ikona ołówka) — otwiera ustawienia zone, takie jak ręczne przekazywanie zone i orientacja urządzenia.
* **Edit DMX profile/channel mapping** (ikona suwaków) — otwiera edytor presetów/kanałów DMX.
* **Delete** — usuwa DMX zone.

### Limity uzbrajania

Liczba DMX zone, które można uzbroić jednocześnie, zależy od poziomu licencji. Jeśli Twój poziom nie pozwala na wyjście DMX albo uzbrojono już maksymalną liczbę DMX zone, przycisk **ARM** dla kolejnych zone jest wyłączony, a po najechaniu kursorem wyświetla ikonę zakazu.

Przed uzbrojeniem kolejnych zone rozbrój inną DMX zone albo użyj poziomu licencji z wyższym limitem DMX.
