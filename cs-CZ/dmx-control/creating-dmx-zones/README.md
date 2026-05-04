---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Vytváření DMX zones

1. Připojte svůj Art-Net node a nastavte ho podle části [Připojení k Art-Net node](../connecting-to-an-artnet-node.md "mention").
2. Otevřete **DMX Zones** a klikněte na **ADD DMX ZONE**.
3. Nastavte u zone hodnoty **Node**, **Universe** a **Address** tak, aby odpovídaly zařízení.
4. Vyberte pro zařízení **Preset**. Preset určuje, které DMX kanály dostávají pevné hodnoty, hodnoty zapnutí/vypnutí obsahu, barvu RGB, polohu X/Y, jas nebo explicitní vstupy DMX Value.
5. Kliknutím na **Edit DMX profile/channel mapping** (ikona posuvníků) upravte mapování kanálů. Výchozí preset začíná kanálem pro zapnutí/vypnutí obsahu a kanály barev RGB.
6. Přiřaďte Clips k DMX zone stejným způsobem, jako je přiřazujete k beam zone nebo canvas zone.
7. Až budete připraveni, aby zone vysílala DMX, stiskněte **ARM**.

{% hint style="warning" %}
Pouze aktivované DMX zones odesílají živé hodnoty. Neaktivované DMX zones vynulují své namapované kanály, což je při nastavování zařízení bezpečnější.
{% endhint %}

DMX výstup je také omezen úrovní vaší licence. Pokud je tlačítko **ARM** neaktivní, zkontrolujte, zda vaše úroveň zahrnuje DMX výstup nebo zda už nebyl dosažen maximální počet aktivovaných DMX zones.
