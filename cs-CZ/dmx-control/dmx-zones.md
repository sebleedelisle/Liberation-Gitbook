---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# 🟩 DMX zones

DMX zones jsou výstupní zone v Liberation, které místo laserových bodů posílají Art-Net/DMX. Zobrazují se vedle beam zone a canvas zone, takže jim lze Clips přiřazovat stejným postupem ve výběru zone.

Pro jejich správu otevřete z nabídky **DMX Zones**, případně použijte sekci DMX v Laser Overview.

* **ADD DMX ZONE** - vytvoří novou DMX zone.
* **ARM** - povolí DMX výstup pro danou zone. DMX zone, která není aktivovaná, vynuluje své namapované kanály.
* **Node** - vybere číslo Art-Net node.
* **Universe** - vybere Art-Net universe. Zobrazená hodnota je číslovaná od 1, takže Universe 1 je první universe.
* **Address** - nastaví počáteční adresu zařízení. Zobrazená hodnota je také číslovaná od 1.
* **Preset** - vybere DMX preset, který mapuje obsah Clip na DMX kanály.
* **Edit DMX zone settings** (ikona tužky) - otevře nastavení zone, například ruční přeposílání zone a orientaci zařízení.
* **Edit DMX profile/channel mapping** (ikona posuvníků) - otevře editor DMX preset/kanálů.
* **Delete** - odstraní DMX zone.

### Limity aktivace

Počet DMX zones, které mohou být aktivované současně, závisí na úrovni vaší licence. Pokud vaše úroveň DMX výstup nepovoluje nebo jste už aktivovali maximální počet DMX zones, tlačítko **ARM** pro další zones je deaktivované a při najetí myší zobrazuje ikonu zákazu vstupu.

Než aktivujete další zones, deaktivujte jinou DMX zone nebo použijte úroveň licence s vyšším limitem pro DMX.
