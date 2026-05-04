---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Lager effekter i «laserharpe»-stil, der innkommende MIDI-noter utløser stråler eller former over et område. Noden bruker innholdet du sender inn som _source_ for hver note – sender du inn en prikk, får du en rad med prikker. Sender du inn en form, for eksempel en sirkel, får du en rad med sirkler, og mer komplekse former replikeres på samme måte.

Du kan velge hvilket MIDI-grensesnitt Liberation skal lytte til i **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – hvilken MIDI-kanal det skal lyttes til (0 = alle kanaler, 1–16 = bestemt kanal)
* **width** – total bredde som notene fordeles over.
* **MIDI note min / max** – laveste og høyeste MIDI-noteverdi i området.
* **ignore out of range notes** – filtrerer bort noter som ligger utenfor det angitte området. Hvis dette er deaktivert, blir noter utenfor området «klemt» til nærmeste tilgjengelige note (høye noter utløser toppen av området, lave noter utløser bunnen).
* **auto extend range** – utvider området automatisk hvis det spilles noter utenfor det.

{% hint style="info" %}
Usikker på hvilket noteområde du får inn? Slå på **auto extend range**, sett **MIDI note min** veldig høyt og **MIDI note max** veldig lavt, og spill deretter gjennom notene dine. Systemet fanger dem alle og utvider området for deg. Når du har fått med alt, slår du bare av **auto extend range** for å låse området.
{% endhint %}

* **leave all notes visible** – lager stråler eller former for alle noter i området, enten de spilles eller ikke, slik at du får en «laserharpe»-effekt.
* **hit colour** – fargen som vises når en note utløses.
* **hit colour hold time** – hvor lenge treffargen blir værende på full lysstyrke før den tones ut. Verdien er i sekunder (0–1). _100% = 1 sekund._
* **hit colour decay time** – hvor lang tid treffargen bruker på å tone tilbake etter hold-tiden. Verdien er i sekunder (0–1). _100% = 1 sekund._

{% hint style="info" %}
Hvis innholdet ditt allerede er helt hvitt, vil det ikke gjøre noen forskjell å sette **hit colour** til hvit. For best resultat bør du bruke en mettet farge på innholdet og sette **hit colour** til hvit – dette gir en veldig fin blinkeffekt når noter utløses.
{% endhint %}

* **note off fade out time** – hvor lang tid noten bruker på å fade ut etter at den slippes. Verdien er i sekunder (0–1). _100% = 1 sekund._
* **hit scale factor** – hvor mye noten skaleres opp når den utløses (f.eks. 2 = dobbel størrelse).
* **hit scale hold time** – hvor lenge noten forblir skalert opp før den krymper tilbake. Verdien er i sekunder (0–1). _100% = 1 sekund._
* **hit scale decay time** – hvor lang tid noten bruker på å gå tilbake til opprinnelig størrelse. Verdien er i sekunder (0–1). _100% = 1 sekund._
* **note off shrink time** – hvor lang tid noten bruker på å krympe tilbake til opprinnelig størrelse etter at den er sluppet. Verdien er i sekunder (0–1). _100% = 1 sekund._ (Har ingen effekt når **leave all notes visible** er aktivert.)

{% hint style="info" %}
Skalering – merk at hvis innholdet ditt bare er én enkelt prikk, har skalering ingen effekt!
{% endhint %}
