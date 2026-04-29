---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube promotional image courtesy of Wicked Lasers</p></figcaption></figure>

[LaserCube](https://www.laseros.com/lasercube/) från Wicked Lasers är en extremt kompakt batteridriven laserenhet som finns i flera olika effektkonfigurationer. Den är populär bland hobbyanvändare tack vare den lättanvända smartphone-appen, men de senaste modellerna är tillräckligt kapabla för att användas i professionella shower.

Telefonappen (som heter LaserOS och även finns för dator) är gratis att ladda ner, väldigt rolig att använda och räcker för de flesta användare. Men om du kör större shower med flera lasrar behöver du något mer specialiserat och kraftfullt – och det är här Liberation kommer in.

### Ansluta till en LaserCube

Tidiga LaserCube-enheter styrs via USB, men de nuvarande modellerna har alla en inbyggd nätverksstyrenhet. Dessa nätverksstyrda kuber kallas "LaserCube Wifi". Liberation stöder båda typerna av LaserCube\*, oavsett om de är anslutna via USB eller via nätverk.

\*(Stöd för LaserCube-nätverksprotokollet introducerades i version 0.7.3)

### USB LaserCube

Anslut din LaserCube till datorn med en micro-USB-kabel och leta sedan efter den i panelen _Controller Assignment_ (se [Tilldela kontroller](../setting-up/controller-assignment.md "mention")). Om den inte visas automatiskt trycker du på knappen _REFRESH_.

### Nätverks-LaserCube "Wifi"

{% hint style="danger" %}
Även om "Wifi"-kuberna är utformade för att användas via ett trådlöst nätverk rekommenderas det inte, eftersom du sannolikt får avbrott och störningar. Använd i stället RJ45-uttaget för att ansluta din LaserCube till ett trådbundet nätverk, precis som du skulle göra med Ether Dreams.
{% endhint %}

Anslut din LaserCube till ditt trådbundna nätverk.

Sätt din LaserCube i läget "LAN Client" och se till att det finns en router i nätverket. LaserCube får en IP-adress från routern och bör sedan visas i panelen _Controller Assignment_. (Se [Tilldela kontroller](../setting-up/controller-assignment.md "mention")).

{% hint style="info" %}
Det går att konfigurera ett nätverk utan router och ge alla enheter fasta IP-adresser, och detta är mycket vanligt inom eventbranschen. Personligen föredrar jag att lägga till en router i nätverket och rekommenderar det alternativet till alla som har mindre erfarenhet av nätverk.

Routern tilldelar dynamiskt en IP-adress till allt, och jag tycker att det är enklare och mindre felbenäget.
{% endhint %}

{% hint style="danger" %}
Till skillnad från Ether Dream _**BLANKAR LaserCubes INTE LASERN**_ om de råkar ut för en buffer under-run, förlorat paket eller annan skadad/felaktig data.

I stället fortsätter de bara från där de slutade, och i vissa fall kan det göra att en aktiv stråle korsar områden som inte ligger inom zoner, och ännu värre, den kan skära rakt igenom mjukvarumasker.

Jag pratar med designerna/utvecklarna bakom LaserCube och hoppas att detta är något de åtgärdar i framtiden med en firmwareuppdatering, men tills dess måste du se till att fysiskt maska alla platser där du inte vill att lasern ska kunna gå.

För att vara rättvis bör du antagligen göra detta ändå, men jag använder själv mjukvarumasker för att skydda kameror och projektorer. Var därför medveten om att det är farligare att göra detta med LaserCube-nätverksprotokollet än med Ether Dream (som går in i ett säkerhetsstoppläge så snart det uppstår ett fel eller data saknas).

Dessutom har jag redan sagt det, men **använd en trådbunden anslutning till din LaserCube**. Wifi räcker inte och kommer att göra det här problemet ännu värre.
{% endhint %}
