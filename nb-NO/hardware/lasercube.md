---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube-promobilde gjengitt med tillatelse fra Wicked Lasers</p></figcaption></figure>

[LaserCube](https://www.laseros.com/lasercube/) fra Wicked Lasers er en svært kompakt batteridrevet laserenhet som finnes i flere ulike effektkonfigurasjoner. Den er populær blant hobbybrukere på grunn av den brukervennlige smarttelefonappen, men nyere modeller er kraftige nok til å brukes på profesjonelle show.

Telefonappen (som heter LaserOS, og som også finnes for desktop) kan lastes ned gratis, er morsom å bruke, og er god nok for de fleste brukere. Men hvis du kjører større show med flere lasere, trenger du noe mer spesialisert og kraftig – og det er her Liberation kommer inn.

### Koble til en LaserCube

Tidlige LaserCube-enheter styres via USB, men alle nåværende modeller har en innebygd nettverkskontroller. Disse nettverksstyrte kubene kalles «LaserCube Wifi». Liberation støtter begge typer LaserCube\*, enten de er koblet til via USB eller på et nettverk.

\*(Støtte for LaserCube-nettverksprotokollen ble introdusert i versjon 0.7.3)

### USB LaserCube

Koble LaserCube til datamaskinen med en micro-USB-kabel, og se deretter etter den i _Controller Assignment_-panelet (se [Kontrollertildeling](../setting-up/controller-assignment.md "mention")). Hvis den ikke vises automatisk, trykker du på _REFRESH_-knappen.

### Nettverks-LaserCube "Wifi"

{% hint style="danger" %}
Selv om «Wifi»-kubene er laget for å brukes over et trådløst nettverk, anbefales ikke dette. Du vil sannsynligvis få dropouts og glitches. Bruk i stedet RJ45-kontakten til å koble LaserCube til et kablet nettverk, akkurat som du ville gjort med Ether Dreams.
{% endhint %}

Koble LaserCube til det kablede nettverket.

Sett LaserCube i «LAN Client»-modus, og sørg for at det finnes en ruter på nettverket. LaserCube får en IP-adresse fra ruteren, og skal deretter dukke opp i _Controller Assignment_-panelet. (Se [Kontrollertildeling](../setting-up/controller-assignment.md "mention")).

{% hint style="info" %}
Det er mulig å sette opp et nettverk uten ruter og gi alle enhetene faste IP-adresser, og dette er veldig vanlig i eventbransjen. Personlig foretrekker jeg å legge til en ruter på nettverket, og jeg anbefaler dette alternativet til alle som har mindre erfaring med nettverk.

Ruteren tildeler en IP-adresse dynamisk til alt på nettverket, og jeg synes det er enklere og gir færre feil.
{% endhint %}

{% hint style="danger" %}
I motsetning til Ether Dream, _**BLANKER LaserCubes IKKE LASEREN**_ hvis de opplever buffer-underrun, en tapt pakke eller andre korrupte / feil data.

I stedet fortsetter de bare der de slapp, og i noen tilfeller kan dette føre til at en aktiv stråle krysser områder som ikke er innenfor soner, og enda verre, skjærer gjennom programvaremasker.

Jeg snakker med designerne/utviklerne av LaserCube, og jeg håper dette er noe de løser i fremtiden med en firmware-oppdatering. I mellomtiden må du sørge for at du fysisk maskerer alle steder der du ikke vil at laseren skal treffe.

For å være rettferdig bør du sannsynligvis gjøre dette uansett, men jeg bruker selv programvaremasker for å beskytte kameraer og projektorer. Så vær oppmerksom på at det er farligere å gjøre dette med LaserCube-nettverksprotokollen enn med Ether Dream (som går i en sikkerhetsstoppmodus så snart det oppstår en feil eller mangler data).

Og som jeg allerede har sagt: **bruk en kablet tilkobling til LaserCube**. Wifi holder ikke, og vil gjøre dette problemet enda verre.
{% endhint %}
