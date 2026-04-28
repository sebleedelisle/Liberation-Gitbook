---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas-oversigt

Liberation Canvas-systemet er relativt enkelt, men det kan virke forvirrende i starten. Her er en konceptuel oversigt, der hjælper dig i gang.

{% hint style="info" %}
**Vent, har jeg brug for canvas-systemet?**

Måske ikke! Hvis du bare projicerer én grafik på én laser, kan du nemt gøre det med en beam zone (som standard spejles indhold i beam zones dog vandret, så du skal X-flippe klippet).

Men hvis du vil fordele grafisk indhold på flere lasere eller opdele det i forskellige sektioner, der skal mappes på arkitektur, så er canvas-systemet lige det, du skal bruge.
{% endhint %}

### Canvas

Først og fremmest er der selve canvaset. Det er det, du ser i _CANVAS_-visningen, og det repræsenterer et stort, ja, canvas, hvor du kan tegne indhold hvor som helst inden for dette område.

### Canvas-målområder

Disse vises som blå rektangler med omrids i canvas-visningen, og det er områder, du kan sende indhold til. Du sender et klips indhold til et canvas-målområde på samme måde, som du ville sende et klip til en beam zone. Du kan se knapperne til canvas-målområder til højre for beam zone-knapperne i clip deck.

{% hint style="info" %}
Hvis du ikke kan se canvas-knapperne i clip deck, så prøv at rulle gennem beam zone-knapperne med `Shift + Left / Right Arrow`. Du bør se en knap for hvert canvas-målområde med labels som _CANVAS 1, CANVAS 2_ osv.
{% endhint %}

### Canvas-zoner

Canvas-zoner er områder i canvaset, som du vælger at sende til en laser. De vises som lyserøde rektangler med omrids i canvas-visningen. Du kan højreklikke på hver zone og vælge de lasere, den skal tildeles til. Hvis du nu skifter til _OUTPUT_-visningen for den laser, kan du se, at der er dukket en ny zone op.

{% hint style="danger" %}
ADVARSEL - hvis laseren er armed, kan du pludselig begynde at projicere indhold i en standard canvas-zone. Det er bedst at disarm laseren, før du tildeler canvas-zoner til den.
{% endhint %}

{% hint style="info" %}
Du kan også tildele en canvas-zone til en laser ved at klikke på knappen _add canvas zone_ i _OUTPUT_-visningen. Se [zones.md](../output-view/zones.md "mention").
{% endhint %}

### Guide-billeder

Du kan tilføje et guide-billede i canvaset og bruge det som skabelon for din grafik. Det anbefales at justere farvetonen på guide-billedet (højreklikmenuen) og gøre det mørkere, så du lettere kan se dit indhold oven på det.

{% hint style="info" %}
Til architectural mapping har jeg oplevet, at det er nyttigt at lave en "unwrapped" visualisering af bygningen, som viser alle bygningens flader som et fladt, uforvrænget billede. Perspektivkorrektionen for de forskellige sektioner kan udføres med canvas-zonen i _OUTPUT_-visningen.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Et "flattened" guide-billede for Saltwell Hall i Gateshead, UK</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Canvas-zonerne i en tidlig version af Liberation (ca. 2017!) Bemærk, at de lyserøde rektangler vælger, hvilken del af canvaset der skal vises, og at output-visningerne nedenunder derefter viser, hvilken del af hver laser de zoner sendes til.</p></figcaption></figure>

### Canvas i 3D visualiser

Det ville sandsynligvis være besværligt (for at sige det mildt) at genskabe dit komplicerede multi-laser-projektionssystem i 3D visualiser! Derfor har du i stedet mulighed for at placere dit canvas i 3D-rummet. Aktivér afkrydsningsfeltet _Show canvas_ i panelet _3D visualiser settings_. (Eventuelle guide-billeder, du har i canvaset, vises også i visualiseren.)

{% hint style="info" %}
Bemærk, at visualiseren stadig viser canvas-projektionerne som atmosfæriske effekter, der kommer fra laserne. Du kan enten bare flytte dem ud af visningen, eller, hvis du vil gøre det lidt elegant, kan du justere dem, så de passer med canvaset!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Det kan være ekstremt tilfredsstillende, når du får strålerne fra laseren til at flugte med canvas-billedet i 3D visualiser!</p></figcaption></figure>
