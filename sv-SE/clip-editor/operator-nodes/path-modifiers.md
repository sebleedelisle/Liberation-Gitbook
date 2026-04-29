---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

Den här noden ersätter linjer och forminnehåll med jämnt fördelade punkter (befintliga punkter lämnas oförändrade).

* **Colour** – punktens färg. Ignoreras om _Inherit Colour_ är aktiverat, se nedan. _Se även_ [Färginställningar och HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – avståndet mellan punkterna, mätt i pixlar. Lägre värden = fler punkter, högre värden = färre.
* **Offset** – förskjuter punkternas startposition som en procentandel av avståndet. Kan animeras (t.ex. med en sågtandsformad Oscillator Node) för att skapa "vandrande" punkteffekter.
* **Keep Original** – om aktiverat behålls de ursprungliga linjerna/formerna och punkterna ritas ovanpå.
* **Render Profile** – väljer renderingskvalitet. _Se_ [Render profile](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – justerar automatiskt avståndet så att banans längd delas jämnt.
* **Fade Out Ends** – minskar gradvis punkternas ljusstyrka mot banans början och slut. Användbart när du animerar **Offset** med en sågtandsformad Oscillator Node, så att punkter tonas in/ut mjukt när de rör sig mot formens slut.

## &#x20;Trimmer

Den här noden trimmar den synliga längden på linjer och former, så att du kan visa, dölja eller animera dem över tid.

* **Offset** – styr var den synliga delen av formen börjar. Även med _Trim Size_ på 0% gör en animering av Offset från 0% → 100% att formen ritas upp, blir helt synlig vid 50% och sedan försvinner igen.
* **Trim Size** – anger hur mycket av formen som behålls, som en procentandel av dess totala längd.
* **Loop** – behandlar formen som en kontinuerlig loop, så att slutet ansluter tillbaka till början i stället för att försvinna.
* **All Shapes** – kombinerar alla inkommande former och trimmar dem som om de vore en enda bana. Om avstängt trimmas varje form individuellt.
* **Add Dot at Start / Add Dot at End** – lägger till en punkt med vald färg vid trimningspunkterna. (Om ingen trimning används läggs inga punkter till.)
* **Colour** – trimningspunkternas färg. _Se även_ [Färginställningar och HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – väljer renderingsprofil för punkterna. _Se_ [Render profile](../fundamentals/render-profile.md "mention")
