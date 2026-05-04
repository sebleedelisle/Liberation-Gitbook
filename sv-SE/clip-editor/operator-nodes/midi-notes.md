---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Skapar effekter i stil med en “laserharpa”, där inkommande MIDI-noter triggar strålar eller former över ett intervall. Noden använder det innehåll du skickar in i den som _källa_ för varje not – skickar du in en punkt får du en rad med punkter. Skickar du in en form, till exempel en cirkel, får du en rad med cirklar, och mer komplexa former replikeras på samma sätt.

Du kan välja vilket MIDI-gränssnitt Liberation lyssnar på i **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – vilken MIDI-kanal som ska lyssnas på (0 = alla kanaler, 1–16 = specifik kanal)
* **width** – den totala bredden som noterna sprids över.
* **MIDI note min / max** – de lägsta och högsta MIDI-notvärdena i intervallet.
* **ignore out of range notes** – filtrerar bort alla noter utanför det angivna intervallet. Om detta är avstängt begränsas noter utanför intervallet till närmaste tillgängliga not (höga noter triggar överkanten av intervallet, låga noter triggar nederkanten).
* **auto extend range** – breddar automatiskt intervallet om noter spelas utanför det.

{% hint style="info" %}
Osäker på vilket notintervall du får in? Slå på **auto extend range**, sätt **MIDI note min** riktigt högt och **MIDI note max** riktigt lågt, och spela sedan igenom dina noter. Systemet fångar upp dem alla och utökar intervallet åt dig. När du har fått med allt stänger du bara av **auto extend range** för att låsa intervallet.
{% endhint %}

* **leave all notes visible** – skapar strålar eller former för alla noter i intervallet, oavsett om de spelas eller inte, vilket ger en “laserharpa”-effekt.
* **hit colour** – färgen som visas när en not triggas.
* **hit colour hold time** – hur länge träfffärgen ligger kvar med full ljusstyrka innan den tonas ut. Värdet anges i sekunder (0–1). _100 % = 1 sekund._
* **hit colour decay time** – hur lång tid det tar för träfffärgen att tona tillbaka efter hålltiden. Värdet anges i sekunder (0–1). _100 % = 1 sekund._

{% hint style="info" %}
Om ditt innehåll redan är helt vitt gör det ingen skillnad att sätta hit colour till vitt. För bästa resultat använder du en mättad färg för innehållet och sätter hit colour till vitt – det ger en riktigt fin blixteffekt när noter triggas.
{% endhint %}

* **note off fade out time** – hur lång tid det tar för noten att tona ut efter att den har släppts. Värdet anges i sekunder (0–1). _100 % = 1 sekund._
* **hit scale factor** – hur mycket noten skalas upp när den triggas (t.ex. 2 = dubbel storlek).
* **hit scale hold time** – hur länge noten förblir uppskalad innan den krymper tillbaka. Värdet anges i sekunder (0–1). _100 % = 1 sekund._
* **hit scale decay time** – hur lång tid det tar för noten att återgå till sin ursprungliga storlek. Värdet anges i sekunder (0–1). _100 % = 1 sekund._
* **note off shrink time** – hur lång tid det tar att krympa tillbaka till ursprunglig storlek efter att noten har släppts. Värdet anges i sekunder (0–1). _100 % = 1 sekund._ (Har ingen effekt när **leave all notes visible** är aktiverat.)

{% hint style="info" %}
Skalning – tänk på att om ditt innehåll är en enda punkt har skalningen ingen effekt!
{% endhint %}
