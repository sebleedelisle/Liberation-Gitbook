---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 DMX-Zonen erstellen

1. Verbinde deinen Art-Net-node und richte ihn wie in [Verbindung mit einem Art-Net-node herstellen](../connecting-to-an-artnet-node.md "mention") beschrieben ein.
2. Öffne **DMX Zones** und klicke auf **ADD DMX ZONE**.
3. Stelle **Node**, **Universe** und **Address** der zone passend zum Fixture ein.
4. Wähle ein **Preset** für das Fixture. Das Preset legt fest, welche DMX-Kanäle feste Werte, Werte für Inhalt ein/aus, RGB-Farbe, X/Y-Position, Helligkeit oder explizite DMX Value-Eingänge erhalten.
5. Klicke auf **Edit DMX profile/channel mapping** (Schieberegler-Symbol), um das Kanal-Mapping zu bearbeiten. Das Standard-Preset beginnt mit einem Kanal für Inhalt ein/aus und RGB-Farbkanälen.
6. Weise der DMX zone Clips genauso zu wie beam zones oder canvas zones.
7. Drücke **ARM**, wenn die zone DMX ausgeben soll.

{% hint style="warning" %}
Nur aktivierte DMX zones senden Live-Werte. Nicht aktivierte DMX zones setzen ihre zugeordneten Kanäle auf null zurück. Das ist sicherer, wenn du Fixtures einrichtest.
{% endhint %}

Die DMX-Ausgabe ist außerdem durch deine Lizenzstufe begrenzt. Wenn die Schaltfläche **ARM** deaktiviert ist, prüfe, ob deine Lizenzstufe DMX-Ausgabe umfasst oder ob die maximale Anzahl aktivierter DMX zones bereits erreicht ist.
