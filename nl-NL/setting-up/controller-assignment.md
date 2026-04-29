---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Controllertoewijzing

Zodra je de lasers in Liberation hebt ingesteld, kun je elke laser toewijzen aan een lasercontroller in de echte wereld. (Zie [Compatibele lasers en controllers (DACs)](../hardware/compatible-lasers-and-controllers-dacs.md "mention") om te controleren welke hardware je kunt gebruiken.) De controllers zijn via USB of via het netwerk verbonden.

* Open het paneel _Controller Assignment_ via de menuoptie _View -> Controller Assignment_. (Je kunt ook de knop _ASSIGN LASER CONTROLLERS_ in het paneel _Laser Overview_ gebruiken.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Paneel Controller Assignment"><figcaption></figcaption></figure>

* Het paneel is in twee delen verdeeld: links staat een lijst met lasers en rechts de lijst met beschikbare controllers. Als je je lasercontroller niet in de lijst ziet, druk dan op de knop _REFRESH_. Als je problemen blijft houden, zie [Probleemoplossing](../troubleshooting/ "mention").
* Om een controller aan een laser toe te wijzen, klik en sleep je vanaf rechts naar een lege lasersleuf links. Hiermee vertel je Liberation welke controller voor welke laser moet worden gebruikt. (Als je van gedachten verandert, kun je de controllers vrij omhoog en omlaag slepen van de ene laser naar de andere.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Lijst met controllers" width="375"><figcaption></figcaption></figure>

* Als je een groen vierkant naast de controller ziet, betekent dit dat Liberation er succesvol verbinding mee heeft gemaakt.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Een Ether Dream en een Helios DAC die respectievelijk aan lasers 2 en 3 zijn toegewezen</p></figcaption></figure>

{% hint style="info" %}
Let op: telkens wanneer je verbinding maakt met een controller, wordt de laser automatisch disarmed.
{% endhint %}

* Een oranje vierkant 🟧 betekent dat de controller af en toe verbindingsproblemen heeft. Dit wordt meestal veroorzaakt door een netwerkprobleem; zie [Probleemoplossing](../troubleshooting/ "mention").
* Een rood vierkant 🟥 betekent dat de controller niet bereikbaar is; zie [Probleemoplossing](../troubleshooting/ "mention").
* De _disconnect button_ (X) verbreekt de verbinding met de controller, maar verwijdert deze niet uit de lasertoewijzing. Je kunt daarna de _reconnect button_ (pictogram met refresh-pijl) gebruiken om opnieuw verbinding te maken, of nogmaals op de _disconnect button_ klikken om de toewijzing te wissen.
* _Geavanceerde functie:_ Open het controlleranalysepaneel door op de knop te klikken die eruitziet als een grafiek. Dit is een geavanceerde functie die gedetailleerde informatie geeft over de datastream en kan helpen bij het oplossen van problemen. (Deze optie is mogelijk niet beschikbaar voor sommige controllertypen.)
* Je kunt de _rename button_ (potlood) gebruiken om deze controller elke gewenste naam te geven. Het is handig om een naam te kiezen waarmee je de controller makkelijk aan specifieke hardware kunt koppelen. Als de controller in een laser is ingebouwd, kun je de naam daarop afstemmen, bijvoorbeeld _LaserCube Ultra #1_ of _Triton T5 #3._ Deze namen worden opgeslagen in je Liberation-installatie en verschijnen vanaf nu steeds opnieuw; dit kan erg handig zijn om je lasers snel te herkennen.

{% hint style="info" %}
Pro tip: **dubbelklik** op een controller aan de rechterkant om deze automatisch toe te wijzen aan de volgende beschikbare laser aan de linkerkant. Dit kan veel tijd besparen als je veel lasers moet toewijzen!
{% endhint %}

Je kunt de knoppen _DISCONNECT ALL_ en _RECONNECT ALL_ gebruiken om alle verbindingen snel te resetten. Dit is handig als je netwerkproblemen hebt.
