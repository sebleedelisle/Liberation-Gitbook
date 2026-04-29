---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas-overzicht

Het Canvas-systeem van Liberation is relatief eenvoudig, maar kan in het begin verwarrend zijn. Hieronder vind je een conceptueel overzicht om je op weg te helpen.

{% hint style="info" %}
**Wacht, heb ik het Canvas-systeem nodig?**

Misschien niet! Als je alleen één graphic op één laser projecteert, kun je dat eenvoudig doen met een beam zone (al wordt content in een beam zone standaard horizontaal gespiegeld, dus je moet de clip dan X flippen).

Maar als je grafische content over meerdere lasers wilt verdelen, of wilt opsplitsen in verschillende secties om die op architectuur te mappen, dan is het Canvas-systeem precies wat je nodig hebt.
{% endhint %}

### Canvas

Allereerst is er de canvas zelf. Dit is wat je ziet in de _CANVAS_-weergave. Het stelt een groot canvas voor, waarop je overal binnen deze ruimte content kunt tekenen.

### Canvas-doelgebieden

Deze worden in de canvas-weergave weergegeven als blauwe rechthoeken met alleen een rand. Dit zijn gebieden waarnaar je content kunt sturen. Je stuurt de content van een clip naar een canvas-doelgebied, op dezelfde manier waarop je een clip naar een beam zone zou sturen. Je ziet de knoppen voor canvas-doelgebieden rechts van de beam zone-knoppen in het clip deck.

{% hint style="info" %}
Als je de canvas-knoppen in het clip deck niet ziet, probeer dan door de beam zone-knoppen te scrollen met `Shift + Left / Right Arrow`. Je zou een knop moeten zien voor elk canvas-doelgebied, gelabeld als _CANVAS 1, CANVAS 2_ enzovoort.
{% endhint %}

### Canvas-zones

Canvas-zones zijn gebieden binnen de canvas die je naar een laser kunt sturen. Ze worden in de canvas-weergave weergegeven als roze rechthoeken met alleen een rand. Je kunt met de rechtermuisknop op elke zone klikken en de lasers selecteren waaraan je die zone wilt toewijzen. Als je nu overschakelt naar de _OUTPUT_-weergave voor die laser, zie je dat er een nieuwe zone is verschenen.

{% hint style="danger" %}
WAARSCHUWING - als de laser armed is, kun je ineens content gaan projecteren in een standaard canvas-zone. Je kunt de laser het beste disarmen voordat je er canvas-zones aan toewijst.
{% endhint %}

{% hint style="info" %}
Je kunt ook een canvas-zone aan een laser toewijzen door in de _OUTPUT_-weergave op de knop _add canvas zone_ te klikken. Zie [Zones](../output-view/zones.md "mention").
{% endhint %}

### Guide images

Je kunt een guide image aan de canvas toevoegen en deze gebruiken als sjabloon voor je graphics. Het is aan te raden om de kleurtint van de guide image aan te passen (rechtermuisknopmenu) en deze donkerder te maken, zodat je je content er beter overheen kunt zien.

{% hint style="info" %}
Voor architectural mapping vond ik het handig om een 'uitgevouwen' visual van het gebouw te maken, waarbij alle oppervlakken van het gebouw als een vlak, onvervormd beeld worden weergegeven. De perspectiefcorrectie voor de verschillende secties kun je doen met de canvas-zone in de _OUTPUT_-weergave.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Een 'afgevlakte' guide image voor Saltwell Hall in Gateshead, VK</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>De canvas-zones in een vroege versie van Liberation (rond 2017!) Let op: de roze rechthoeken bepalen welk deel van de canvas wordt getoond, en de output-weergaven eronder laten zien naar welk deel van elke laser die zones gaan.</p></figcaption></figure>

### Canvas in de 3D visualiser

Het zou waarschijnlijk nogal omslachtig zijn (op z’n zachtst gezegd) om je complexe multi-laserprojectiesysteem opnieuw op te bouwen in de 3D visualiser. Daarom heb je in plaats daarvan de optie om je canvas binnen de 3D-ruimte te plaatsen. Activeer het selectievakje _Show canvas_ in het paneel _3D visualiser settings_. (Alle guide images die je in de canvas hebt, worden ook in de visualiser weergegeven.)

{% hint style="info" %}
Let op: de visualiser toont de canvas-projecties nog steeds als atmosferische effecten die uit de lasers komen. Je kunt ze gewoon buiten beeld verplaatsen, of, als je het netjes wilt doen, ze uitlijnen met de canvas!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Het kan enorm bevredigend zijn als je de beams van de laser uitlijnt met de canvas-afbeelding in de 3D visualiser!</p></figcaption></figure>
