---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ DMX-Zonen

DMX zones sind Liberation-Ausgabezonen, die Art-Net/DMX statt Laserpunkten senden. Sie erscheinen neben beam zones und canvas zones, sodass Clips ihnen im gleichen Ablauf über den zone selector zugewiesen werden können.

Öffne **DMX Zones** über das Menü oder verwende den DMX-Bereich in Laser Overview, um sie zu verwalten.

* **ADD DMX ZONE** - erstellt eine neue DMX zone.
* **ARM** - aktiviert die DMX-Ausgabe für diese zone. Eine nicht aktivierte DMX zone setzt ihre zugeordneten Kanäle auf null zurück.
* **Node** - wählt die Art-Net-Node-Nummer aus.
* **Universe** - wählt das Art-Net-Universe aus. Der angezeigte Wert ist 1-basiert, Universe 1 ist also das erste Universe.
* **Address** - legt die Startadresse des Fixtures fest. Der angezeigte Wert ist ebenfalls 1-basiert.
* **Preset** - wählt das DMX-Preset aus, das Clip-Inhalte DMX-Kanälen zuordnet.
* **Edit DMX zone settings** (Stiftsymbol) - öffnet zone-Einstellungen wie manuelle zone-Weiterleitung und Fixture-Ausrichtung.
* **Edit DMX profile/channel mapping** (Schieberegler-Symbol) - öffnet den DMX-Preset-/Kanal-Editor.
* **Delete** - entfernt die DMX zone.

### Aktivierungslimits

Die Anzahl der DMX zones, die gleichzeitig aktiviert sein können, hängt von deiner Lizenzstufe ab. Wenn deine Stufe keine DMX-Ausgabe erlaubt oder du bereits die maximale Anzahl an DMX zones aktiviert hast, ist die Schaltfläche **ARM** für weitere zones deaktiviert und zeigt beim Darüberfahren ein Verbotssymbol an.

Deaktiviere eine andere DMX zone oder verwende eine Lizenzstufe mit höherem DMX-Limit, bevor du weitere zones aktivierst.
