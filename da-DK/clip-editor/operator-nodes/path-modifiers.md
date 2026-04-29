---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

Denne node erstatter indhold med linjer og figurer med jævnt fordelte prikker (eksisterende prikker ændres ikke).

* **Colour** – prikkernes farve. Ignoreres, hvis _Inherit Colour_ er aktiveret, se nedenfor. _Se også_ [Farveindstillinger og HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – afstanden mellem prikker, målt i pixels. Mindre værdier = flere prikker, større værdier = færre.
* **Offset** – forskyder prikkernes startposition som en procentdel af afstanden. Kan animeres (f.eks. med en sawtooth Oscillator Node) for at skabe "vandrende" prikkeffekter.
* **Keep Original** – hvis aktiveret, bevares de oprindelige linjer/figurer, og prikkerne tegnes ovenpå.
* **Render Profile** – vælger renderingskvaliteten. _Se_ [Renderprofil](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – justerer automatisk afstanden, så stilængden kan deles jævnt.
* **Fade Out Ends** – reducerer gradvist prikkernes lysstyrke mod starten og slutningen af stien. Nyttigt, når du animerer **Offset** med en sawtooth Oscillator Node, så prikkerne fader blødt ind/ud, når de bevæger sig til figurens ende.

## &#x20;Trimmer

Denne node beskærer den synlige længde af linjer og figurer, så du kan vise, skjule eller animere dem over tid.

* **Offset** – styrer, hvor den synlige del af figuren starter. Selv med _Trim Size_ på 0% vil en animation af Offset fra 0% → 100% få figuren til at blive tegnet frem, være fuldt synlig ved 50% og derefter forsvinde igen.
* **Trim Size** – angiver, hvor meget af figuren der bevares, som en procentdel af dens samlede længde.
* **Loop** – behandler figuren som et sammenhængende loop, så slutningen forbindes tilbage til begyndelsen i stedet for at forsvinde.
* **All Shapes** – kombinerer alle inputfigurer og beskærer dem, som om de var én samlet sti. Hvis den er slået fra, beskæres hver figur individuelt.
* **Add Dot at Start / Add Dot at End** – tilføjer en prik i den valgte farve ved beskæringspunkterne. (Hvis der ikke er anvendt beskæring, tilføjes der ingen prikker.)
* **Colour** – farven på beskæringsprikkerne. _Se også_ [Farveindstillinger og HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – vælger renderprofilen for prikkerne. _Se_ [Renderprofil](../fundamentals/render-profile.md "mention")
