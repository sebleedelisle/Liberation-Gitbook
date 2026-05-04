---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Opretter effekter i “laser harp”-stil, hvor indkommende MIDI-noter udløser stråler eller former på tværs af et område. Noden bruger det indhold, du sender ind i den, som _source_ for hver note – sender du en prik ind, får du en række prikker. Sender du en form ind, f.eks. en cirkel, får du en række cirkler, og mere komplekse former replikeres på samme måde.

Du kan vælge, hvilket MIDI-interface Liberation skal lytte til, i **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – hvilken MIDI-kanal der skal lyttes til (0 = alle kanaler, 1–16 = bestemt kanal)
* **width** – den samlede bredde, som noderne fordeles over.
* **MIDI note min / max** – den laveste og højeste MIDI-noteværdi i området.
* **ignore out of range notes** – filtrerer alle noter uden for det angivne område fra. Hvis funktionen er slået fra, bliver noter uden for området “clamped” til nærmeste tilgængelige note (høje noter udløser toppen af området, lave noter udløser bunden).
* **auto extend range** – udvider automatisk området, hvis der spilles noter uden for det.

{% hint style="info" %}
Er du ikke sikker på, hvilket noteområde du får ind? Slå **auto extend range** til, sæt **MIDI note min** meget højt og **MIDI note max** meget lavt, og spil derefter dine noter igennem. Systemet fanger dem alle og udvider området for dig. Når du har fanget det hele, slår du blot **auto extend range** fra for at låse området.
{% endhint %}

* **leave all notes visible** – opretter stråler eller former for alle noter i området, uanset om de spilles eller ej, så du får en “laser harp”-effekt.
* **hit colour** – den farve, der vises, når en note udløses.
* **hit colour hold time** – hvor længe hit-farven forbliver ved fuld lysstyrke, før den fader ud. Værdien er i sekunder (0–1). _100% = 1 sekund._
* **hit colour decay time** – hvor lang tid det tager for hit-farven at fade tilbage efter hold-tiden. Værdien er i sekunder (0–1). _100% = 1 sekund._

{% hint style="info" %}
Hvis dit indhold allerede er helt hvidt, gør det ingen forskel at sætte hit-farven til hvid. For det bedste resultat skal du bruge en mættet farve til dit indhold og sætte hit-farven til hvid – det giver en rigtig flot flash-effekt, når noter udløses.
{% endhint %}

* **note off fade out time** – hvor lang tid det tager for noden at fade ud, efter den er sluppet. Værdien er i sekunder (0–1). _100% = 1 sekund._
* **hit scale factor** – hvor meget noden skaleres op, når den udløses (f.eks. 2 = dobbelt størrelse).
* **hit scale hold time** – hvor længe noden forbliver skaleret op, før den krymper tilbage. Værdien er i sekunder (0–1). _100% = 1 sekund._
* **hit scale decay time** – hvor lang tid det tager for noden at vende tilbage til sin oprindelige størrelse. Værdien er i sekunder (0–1). _100% = 1 sekund._
* **note off shrink time** – hvor lang tid det tager at krympe tilbage til oprindelig størrelse, efter noden er sluppet. Værdien er i sekunder (0–1). _100% = 1 sekund._ (Har ingen effekt, når **leave all notes visible** er aktiveret.)

{% hint style="info" %}
Skalering – Bemærk, at hvis dit indhold er en enkelt prik, har skaleringen ingen effekt!
{% endhint %}
