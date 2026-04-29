---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Unterbrochene / blinkende Ausgabe

Öffne das _Laser Overview_-Panel und sieh dir die Verbindungsanzeige neben dem Laser an, mit dem du Probleme hast.

**Wenn die Verbindungsanzeige NICHT dauerhaft grün ist:**\
Dann hast du entweder ein Netzwerkproblem oder ein Problem mit der CPU-Leistung:

**Netzwerkleistung -**

* Stelle sicher, dass du nicht mit einem WLAN verbunden bist. Du solltest immer eine kabelgebundene Verbindung verwenden. Stelle sicher, dass dein Betriebssystem das kabelgebundene Netzwerk gegenüber WLAN priorisiert, oder deaktiviere WLAN, wenn du dir nicht sicher bist.
* Prüfe deinen Netzwerkadapter – und probiere einen anderen USB-C-Adapter aus.
* Windows-Nutzer: Prüfe / aktualisiere deine Netzwerktreiber und führe die passenden Netzwerk-Testtools aus.
* Prüfe alle Kabel, Switches und Router. Tausche jedes Kabel systematisch aus und teste es.
* Starte deine gesamte Netzwerk-Hardware neu, einschließlich Switches, Routern und jedem Ether Dream.

**CPU-Leistung**

Wenn du einen alten oder leistungsschwachen Rechner hast, ist er möglicherweise zu langsam, um Liberation auszuführen. Prüfe die Frame-Rate-Anzeige auf der rechten Seite der Symbolleiste.

Dort gibt es zwei Werte: die tatsächliche Frame Rate und die Ziel-Frame-Rate. Wenn die tatsächliche Frame Rate unter 30 fällt, können Probleme auftreten.

Die folgenden Maßnahmen können helfen:

* Entferne ungenutzte Laser, z. B. wenn du nur einen Laser angeschlossen hast, lösche die anderen.
* Wechsle zur Output- oder Canvas-Ansicht.
* Schließe alle anderen Programme, prüfe die Netzwerk-Firewall-Einstellungen, schließe Antivirenprogramme, Dropbox usw.
* Reduziere deine Bildschirmauflösung und mache das Liberation-Fenster kleiner.

Wenn nichts davon hilft, solltest du ein Upgrade deines Computers in Betracht ziehen.

***

**Wenn die Verbindungsanzeige dauerhaft grün ist:**

Dann handelt es sich wahrscheinlich um ein Hardwareproblem. Das liegt außerhalb des Umfangs dieses Handbuchs, aber du kannst Folgendes versuchen:

* Deaktiviere das SFS-System (Scan Fail Safety). Einige Laser haben eine Funktion, die die Ausgabe deaktiviert, wenn sich die Scanner nicht mehr bewegen, also einen starken statischen Strahl erzeugen. Diese Funktion kann etwas übervorsichtig / unzuverlässig sein.

{% hint style="danger" %}
Sei extrem vorsichtig, wenn du das Scan-Fail-Safety-System deaktivierst. Starke statische Strahlen können Verbrennungen verursachen! Stelle sicher, dass du einen Stopp-Taster und einen Feuerlöscher griffbereit hast.
{% endhint %}

* Prüfe Interlock-Kabel und -Systeme.
* Prüfe alle Kabel zwischen dem Controller und dem Laser.

Ein [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) kann ein äußerst hilfreiches Werkzeug zur Fehlersuche bei Laserproblemen sein.
