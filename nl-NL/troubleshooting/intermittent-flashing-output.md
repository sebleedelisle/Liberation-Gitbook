---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Intermitterende / knipperende uitvoer

Open het _Laser Overview_-paneel en kijk naar het verbindingslampje naast de laser waarmee je problemen hebt.

**Als het verbindingslampje NIET continu groen is :**\
Dan heb je waarschijnlijk een probleem met je netwerk of met de CPU-prestaties :

**Netwerkprestaties -**

* Zorg dat je niet met een wifi-netwerk verbonden bent. Gebruik altijd een bekabelde verbinding. Zorg dat je besturingssysteem voorrang geeft aan het bekabelde netwerk boven wifi, of schakel wifi uit als je het niet zeker weet
* controleer je netwerkadapter - en probeer een andere USB-C-adapter
* Windows-gebruikers - controleer / update je netwerkdrivers en voer de juiste netwerkdiagnosetools uit
* controleer alle bekabeling, switches en routers. Vervang en test elke kabel methodisch.
* herstart al je netwerkapparatuur, inclusief switches, routers en elke Ether Dream.

**CPU-prestaties**

Als je een oude of lichte machine hebt, kan deze te langzaam zijn om Liberation te draaien. Controleer de framerate-indicator aan de rechterkant van de iconenbalk.

Daar staan twee getallen: de actuele framerate en de doelframerate. Als de actuele framerate onder de 30 zakt, kun je problemen krijgen.

De volgende acties kunnen helpen :

* verwijder ongebruikte lasers; als je bijvoorbeeld maar één laser hebt aangesloten, verwijder dan de andere.
* Schakel over naar de Output- of Canvas-weergave
* Sluit alle andere programma’s, controleer de instellingen van je netwerkfirewall en sluit antivirus, Dropbox, enz.
* Verlaag je schermresolutie en maak het Liberation-venster kleiner

Als niets hiervan werkt, overweeg dan om je computer te upgraden.

***

**Als het verbindingslampje WEL continu groen is :**

Dan is het waarschijnlijk een hardwareprobleem. Dit valt buiten de scope van deze handleiding, maar je kunt de volgende acties proberen :

* Schakel het SFS-systeem (Scan Fail Safety) uit. Sommige lasers hebben een functie die de output uitschakelt als de scanners stoppen met bewegen, dus wanneer er een sterke statische bundel ontstaat. Deze systemen kunnen wat overvoorzichtig / onbetrouwbaar zijn.

{% hint style="danger" %}
Wees uiterst voorzichtig wanneer je het scan fail safety-systeem uitschakelt. Sterke statische bundels kunnen brand veroorzaken! Zorg dat je een stopknop en een brandblusser bij de hand hebt.
{% endhint %}

* Controleer veiligheidsinterlock-kabels en -systemen
* Controleer alle bekabeling tussen de controller en de laser.

Een [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) kan een onmisbaar hulpmiddel zijn bij het oplossen van laserproblemen.
