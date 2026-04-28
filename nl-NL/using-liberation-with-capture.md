---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Liberation gebruiken met Capture

Liberation ondersteunt [Capture](https://capture.se) als externe visualiser (vanaf versie 1.0.3). Als je Capture al in je workflow gebruikt, kun je hiermee de live laser-output van Liberation visualiseren in je 3D-scène.

### Hoe het werkt

Er is geen speciaal verbindingsproces of handmatige koppeling nodig.

Zolang:

* Liberation en Capture zich op hetzelfde netwerk bevinden
* Je firewall de verbinding toestaat

…verschijnen alle lasers die je in Liberation hebt ingesteld automatisch in Capture als mediabronnen. Je hoeft geen IP-adressen te configureren of iets speciaals in te schakelen - ze verschijnen gewoon.

### Lasers zien in Capture

Alle geconfigureerde lasers in Liberation verschijnen in Capture als beschikbare mediabronnen.

Om daadwerkelijk output te zien:

* De laser moet in Liberation armed zijn
* De bron moet in Capture aan een laser fixture gekoppeld zijn

Zodra de laser armed is, visualiseert Capture de live outputstream van Liberation. Als een laser in Liberation disarmed is, blijft deze in Capture zichtbaar als bron, maar wordt er niets uitgevoerd.

Zie de documentatie op [capture.se](https://www.capture.se/) voor meer instructies en ondersteuning bij het instellen van lasers in Capture. <br>

### Licentielimieten en armed lasers

Capture-verbindingen worden precies hetzelfde behandeld als fysieke laser-outputs.

Dat betekent:

* Je kunt slechts zoveel lasers armen als je licentieniveau toestaat
* Alleen armed lasers sturen actief data naar Capture

### Heb ik Capture nodig?

Helemaal niet.

Liberation bevat een ingebouwde 3D Visualiser, die altijd beschikbaar is en niet afhankelijk is van je licentieniveau. Je kunt shows rechtstreeks in Liberation ontwerpen en previewen zonder externe software.

Capture is simpelweg een extra optie als je het al gebruikt voor belichting of showontwerp.

### Problemen oplossen

Als lasers niet in Capture verschijnen:

* Controleer of beide applicaties zich op hetzelfde netwerk bevinden
* Controleer je firewallinstellingen
* Zorg dat de laser in Liberation armed is
