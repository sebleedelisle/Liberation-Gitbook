---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Promotieafbeelding van LaserCube, met dank aan Wicked Lasers</p></figcaption></figure>

De [LaserCube](https://www.laseros.com/lasercube/) van Wicked Lasers is een extreem compacte laserunit op batterijvoeding, verkrijgbaar in verschillende vermogensconfiguraties. Ze zijn populair bij hobbyisten vanwege de eenvoudig te gebruiken smartphone-app, maar recente modellen zijn krachtig genoeg om ook bij professionele shows te worden gebruikt.

De telefoon-app (LaserOS, ook beschikbaar voor desktop) kun je gratis downloaden. Hij is erg leuk om mee te spelen en goed genoeg voor de meeste gebruikers. Maar als je grotere shows draait met meerdere lasers, heb je iets gespecialiseerders en krachtigers nodig — en daar komt Liberation in beeld.

### Verbinden met een LaserCube

Vroege LaserCubes worden via USB aangestuurd, maar de huidige modellen hebben allemaal een ingebouwde netwerkcontroller. Deze netwerkgestuurde cubes staan bekend als "LaserCube Wifi". Liberation ondersteunt beide typen LaserCube\*, zowel via USB als via een netwerk.

\*(Ondersteuning voor het LaserCube-netwerkprotocol is geïntroduceerd in versie 0.7.3)

### USB LaserCube

Verbind je LaserCube met je computer via een micro-USB-kabel en zoek hem daarna op in het _Controller Assignment_-paneel (zie [Controllertoewijzing](../setting-up/controller-assignment.md "mention")). Als hij niet automatisch verschijnt, klik dan op de knop _REFRESH_.

### Netwerk-LaserCube "Wifi"

{% hint style="danger" %}
Hoewel de "Wifi"-cubes zijn ontworpen om via een draadloos netwerk te werken, wordt dit niet aanbevolen. Je krijgt waarschijnlijk drop-outs en storingen. Gebruik in plaats daarvan de RJ45-aansluiting om je LaserCube met een bekabeld netwerk te verbinden, net zoals je dat met Ether Dreams zou doen.
{% endhint %}

Verbind je LaserCube met je bekabelde netwerk.

Zet je LaserCube in de modus "LAN Client" en zorg dat er een router in je netwerk aanwezig is. De LaserCube krijgt een IP-adres van je router en zou daarna moeten verschijnen in het _Controller Assignment_-paneel. (Zie [Controllertoewijzing](../setting-up/controller-assignment.md "mention")).

{% hint style="info" %}
Het is mogelijk om een netwerk zonder router op te zetten en al je apparaten vaste IP-adressen te geven. Dit komt veel voor in de evenementenbranche. Persoonlijk geef ik er de voorkeur aan om een router aan het netwerk toe te voegen, en ik raad deze optie aan voor iedereen met minder netwerkervaring.

De router wijst dynamisch een IP-adres toe aan alles. Ik vind dat eenvoudiger en minder foutgevoelig.
{% endhint %}

{% hint style="danger" %}
In tegenstelling tot de Ether Dream _**BLANKEN LaserCubes DE LASER NIET**_ wanneer ze een buffer underrun, verloren pakket of andere corrupte/onjuiste data tegenkomen.

In plaats daarvan gaan ze gewoon verder vanaf het punt waar ze waren gebleven. In sommige gevallen kan daardoor een actieve straal door gebieden gaan die niet binnen zones vallen, en nog erger: dwars door software masks heen snijden.

Ik ben hierover in gesprek met de ontwerpers/coders van LaserCube en hoop dat ze dit in de toekomst met een firmware-update oplossen. Tot die tijd moet je er echter voor zorgen dat je fysiek alles afschermt waar je niet wilt dat de laser komt.

Eerlijk gezegd zou je dat waarschijnlijk sowieso moeten doen, maar ik gebruik zelf software masks om camera’s en projectoren te beschermen. Wees je er dus van bewust dat dit gevaarlijker is met het LaserCube-netwerkprotocol dan met de Ether Dream (die in een safety stop-modus gaat zodra er een fout of ontbrekende data is).

Ook heb ik het al gezegd, maar **gebruik een bekabelde verbinding met je LaserCube**. Wifi is hiervoor niet goed genoeg en maakt dit probleem alleen maar erger.
{% endhint %}
