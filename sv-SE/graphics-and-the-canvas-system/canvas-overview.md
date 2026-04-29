---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Översikt över Canvas

Liberations Canvas-system är relativt enkelt, men det kan vara lite förvirrande i början. Här är en konceptuell översikt som hjälper dig att komma igång.

{% hint style="info" %}
**Vänta, behöver jag Canvas-systemet?**

Kanske inte! Om du bara projicerar en enda grafik på en enda laser kan du enkelt göra det med en strålzon, även om innehåll i strålzoner som standard spegelvänds horisontellt, så du behöver X-vända clipet.

Men om du vill sprida grafiskt innehåll över flera lasrar, eller dela upp det i olika sektioner för att mappa det på arkitektur, är Canvas-systemet rätt verktyg för jobbet!
{% endhint %}

### Canvas

Först och främst finns själva Canvas. Det är det du ser i _CANVAS_-vyn och representerar en stor, ja, canvas, där du kan rita innehåll var som helst inom ytan.

### Canvas-målområden

De visas som blå rektanglar med kontur i Canvas-vyn, och är områden som du kan skicka innehåll till. Du skickar ett clips innehåll till ett Canvas-målområde på samma sätt som du skulle skicka ett clip till en strålzon. Knapparna för Canvas-målområden visas till höger om strålzonsknapparna i Clip Deck.

{% hint style="info" %}
Om du inte kan se Canvas-knapparna i Clip Deck kan du prova att bläddra bland strålzonsknapparna med `Shift + Left / Right Arrow`. Du bör se en knapp för varje Canvas-målområde, märkt _CANVAS 1, CANVAS 2_ osv.
{% endhint %}

### Canvas-zoner

Canvas-zoner är områden inom Canvas som du väljer att skicka till en laser. De visas som rosa rektanglar med kontur i Canvas-vyn. Du kan högerklicka på varje zon och välja vilka lasrar den ska tilldelas till. Om du sedan växlar till _OUTPUT_-vyn för den lasern ser du att en ny zon har dykt upp.

{% hint style="danger" %}
VARNING – om lasern är armerad kan du plötsligt börja projicera innehåll i en standardzon för Canvas. Det är bäst att avarmera lasern innan du tilldelar Canvas-zoner till den.
{% endhint %}

{% hint style="info" %}
Du kan också tilldela en Canvas-zon till en laser genom att klicka på knappen _add canvas zone_ i _OUTPUT_-vyn. Se [Zones](../output-view/zones.md "mention").
{% endhint %}

### Guidebilder

Du kan lägga till en guidebild i Canvas och använda den som mall för din grafik. Det är en bra idé att justera färgtonen på guidebilden (högerklicksmenyn) och göra den mörkare, så att du lättare ser ditt innehåll ovanpå den.

{% hint style="info" %}
För arkitekturmappning har jag märkt att det är hjälpsamt att skapa en ”utvikt” visualisering av byggnaden, där alla ytor på byggnaden visas som en platt, oförvrängd bild. Perspektivkorrigeringen för de olika sektionerna kan göras med Canvas-zonen i _OUTPUT_-vyn.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>En ”tillplattad” guidebild för Saltwell Hall i Gateshead, Storbritannien</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Canvas-zonerna i en tidig version av Liberation (ca 2017!) Observera att de rosa rektanglarna väljer vilken del av Canvas som ska visas, och att Output-vyerna nedanför sedan visar vilken del av respektive laser som zonerna skickas till.</p></figcaption></figure>

### Canvas i 3D visualiser

Det skulle förmodligen vara ganska pilligt (minst sagt) att återskapa ditt komplicerade projektionssystem med flera lasrar i 3D visualiser! Därför har du i stället möjlighet att placera din Canvas i 3D-rymden. Aktivera kryssrutan _Show canvas_ i panelen _3D visualiser settings_. (Alla guidebilder du har i Canvas visas också i visualiseraren.)

{% hint style="info" %}
Observera att visualiseraren fortfarande visar Canvas-projektionerna som atmosfäriska effekter från lasrarna. Du kan antingen bara flytta dem ur vyn, eller, om du vill vara extra noggrann, linjera dem med Canvas!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Det kan vara extremt tillfredsställande när du linjerar strålarna från lasern med Canvas-bilden i 3D visualiser!</p></figcaption></figure>
