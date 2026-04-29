---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube-promobillede udlånt af Wicked Lasers</p></figcaption></figure>

[LaserCube](https://www.laseros.com/lasercube/) fra Wicked Lasers er en ekstremt kompakt batteridrevet laserenhed, som fås i flere forskellige effektkonfigurationer. Den er populær blandt hobbybrugere på grund af den brugervenlige smartphone-app, men nyere modeller er kraftige nok til også at kunne bruges til professionelle shows.

Telefonappen (kaldet LaserOS, som også findes til desktop) kan downloades gratis, er rigtig sjov at lege med og er god nok til de fleste brugere. Men hvis du afvikler større shows med flere lasere, har du brug for noget mere specialiseret og kraftfuldt – og det er her, Liberation kommer ind i billedet.

### Tilslutning til en LaserCube

Tidlige LaserCubes styres via USB, men de nuværende modeller har alle en indbygget netværkscontroller. Disse netværksstyrede cubes kaldes "LaserCube Wifi". Liberation understøtter begge typer LaserCube\*, uanset om de er tilsluttet via USB eller på et netværk.

\*(Understøttelse af LaserCube-netværksprotokollen blev introduceret i version 0.7.3)

### USB LaserCube

Tilslut din LaserCube til din computer med et micro-USB-kabel, og find den derefter i panelet _Controller Assignment_ (se [Tildeling af controllere](../setting-up/controller-assignment.md "mention")). Hvis den ikke vises automatisk, skal du trykke på knappen _REFRESH_.

### Netværks-LaserCube "Wifi"

{% hint style="danger" %}
Selvom "Wifi"-cubes er designet til at blive betjent via et trådløst netværk, anbefales det ikke, da du sandsynligvis vil opleve udfald og fejl. Brug i stedet RJ45-stikket til at tilslutte din LaserCube til et kablet netværk, præcis som du ville gøre med Ether Dreams.
{% endhint %}

Tilslut din LaserCube til dit kablede netværk.

Sæt din LaserCube i "LAN Client"-tilstand, og sørg for, at der er en router på dit netværk. LaserCube får en IP-adresse fra din router, og den bør derefter dukke op i panelet _Controller Assignment_. (Se [Tildeling af controllere](../setting-up/controller-assignment.md "mention")).

{% hint style="info" %}
Det er muligt at opsætte et netværk uden router og give alle dine enheder faste IP-adresser, og det er meget almindeligt i eventbranchen. Personligt foretrækker jeg at tilføje en router på netværket, og jeg anbefaler denne løsning til alle, der har mindre erfaring med netværk.

Routeren tildeler dynamisk en IP-adresse til alt, og jeg synes, det er enklere og giver færre fejl.
{% endhint %}

{% hint style="danger" %}
I modsætning til Ether Dream _**BLANKER LaserCubes IKKE LASEREN**_, hvis de støder på buffer under-run, mistede pakker eller andre beskadigede/forkerte data.

I stedet fortsætter de bare fra det punkt, hvor de slap, og i nogle tilfælde kan det få en aktiv stråle til at krydse områder, der ikke ligger inden for zoner – og endnu værre: den kan skære hen over softwarebaserede masks.

Jeg er i dialog med designerne/udviklerne af LaserCube, og jeg håber, at det er noget, de løser i fremtiden med en firmwareopdatering. Indtil da skal du sikre dig, at du fysisk maskerer alle steder, hvor du ikke vil have, at laseren skal ramme.

For at være fair bør du sandsynligvis gøre det alligevel, men jeg bruger selv softwarebaserede masks til at beskytte kameraer og projektorer. Så vær opmærksom på, at det er farligere at gøre dette med LaserCube-netværksprotokollen, end det er med Ether Dream (som går i sikkerhedsstoptilstand, så snart der er en fejl eller manglende data).

Og jeg har allerede sagt det, men **brug en kablet forbindelse til din LaserCube**. Wifi er ikke godt nok og vil gøre dette problem endnu værre.
{% endhint %}
