---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Liberation mit Capture verwenden

Liberation unterstützt [Capture](https://capture.se) als externen Visualiser (ab Version 1.0.3). Wenn du Capture bereits in deinem Workflow verwendest, kannst du damit die Live-Laserausgabe von Liberation in deiner 3D-Szene visualisieren.

### So funktioniert es

Es ist kein spezieller Verbindungsprozess und keine manuelle Verknüpfung erforderlich.

Solange:

* Liberation und Capture im selben Netzwerk sind
* deine Firewall die Verbindung zulässt

…erscheinen alle Laser, die du in Liberation eingerichtet hast, automatisch in Capture als Medienquellen. Du musst keine IP-Adressen konfigurieren oder etwas Besonderes aktivieren – es wird einfach angezeigt.

### Laser in Capture anzeigen

Alle in Liberation konfigurierten Laser erscheinen in Capture als verfügbare Medienquellen.

Damit tatsächlich eine Ausgabe sichtbar ist:

* Der Laser muss in Liberation aktiviert sein
* Die Quelle muss in Capture einem Laser-Fixture zugewiesen sein

Sobald der Laser aktiviert ist, visualisiert Capture den Live-Ausgabestream von Liberation. Wenn ein Laser in Liberation deaktiviert ist, bleibt er in Capture als Quelle sichtbar, gibt aber nichts aus.

Weitere Anleitungen und Unterstützung zum Einrichten von Lasern in Capture findest du in der Dokumentation unter [capture.se](https://www.capture.se/). <br>

### Lizenzgrenzen und aktivierte Laser

Verbindungen zu Capture werden genauso behandelt wie physische Laserausgänge.

Das bedeutet:

* Du kannst nur so viele Laser aktivieren, wie deine Lizenzstufe erlaubt
* Nur aktivierte Laser senden aktiv Daten an Capture

### Brauche ich Capture?

Nein, überhaupt nicht.

Liberation enthält einen integrierten 3D Visualiser, der immer verfügbar ist und nicht von deiner Lizenzstufe abhängt. Du kannst Shows direkt in Liberation gestalten und vorab ansehen, ohne externe Software.

Capture ist einfach eine zusätzliche Option, wenn du es bereits für Licht- oder Showdesign verwendest.

### Fehlerbehebung

Wenn Laser nicht in Capture erscheinen:

* Prüfe, ob beide Anwendungen im selben Netzwerk sind
* Prüfe deine Firewall-Einstellungen
* Stelle sicher, dass der Laser in Liberation aktiviert ist
