---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Maakt effecten in “laserharp”-stijl, waarbij inkomende MIDI-noten stralen of vormen binnen een bereik triggeren. De node gebruikt de content die je erin stuurt als de _source_ voor elke noot: stuur er een punt in en je krijgt een rij punten. Stuur er een vorm zoals een cirkel in en je krijgt een rij cirkels. Complexere vormen worden op dezelfde manier herhaald.

Je kunt kiezen naar welke MIDI-interface Liberation luistert via **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – naar welk MIDI-kanaal wordt geluisterd (0 = alle kanalen, 1–16 = specifiek kanaal)
* **width** – de totale breedte waarover de noten worden verdeeld.
* **MIDI note min / max** – de laagste en hoogste MIDI-nootwaarden in het bereik.
* **ignore out of range notes** – filtert alle noten buiten het ingestelde bereik weg. Als dit is uitgeschakeld, worden noten buiten het bereik “vastgezet” op de dichtstbijzijnde beschikbare noot (hoge noten triggeren de bovenkant van het bereik, lage noten de onderkant).
* **auto extend range** – maakt het bereik automatisch groter als er noten buiten het bereik worden gespeeld.

{% hint style="info" %}
Weet je niet zeker welk notenbereik je binnenkrijgt? Schakel **auto extend range** in, zet **MIDI note min** heel hoog en **MIDI note max** heel laag, en speel daarna je noten. Het systeem vangt ze allemaal op en vergroot het bereik voor je. Zodra je alles hebt, schakel je **auto extend range** weer uit om het vast te zetten.
{% endhint %}

* **leave all notes visible** – maakt stralen of vormen voor alle noten in het bereik, of ze nu spelen of niet, voor een “laserharp”-effect.
* **hit colour** – de kleur die verschijnt wanneer een noot wordt getriggerd.
* **hit colour hold time** – hoe lang de hitkleur op volledige helderheid blijft voordat deze vervaagt. De waarde is in seconden (0–1). _100% = 1 seconde._
* **hit colour decay time** – hoe lang het duurt voordat de hitkleur na de hold time terug vervaagt. De waarde is in seconden (0–1). _100% = 1 seconde._

{% hint style="info" %}
Als je content al puur wit is, maakt het instellen van de hitkleur op wit geen verschil. Voor het beste resultaat gebruik je een verzadigde kleur voor je content en zet je de hitkleur op wit. Dit geeft een heel mooi flitseffect wanneer noten worden getriggerd.
{% endhint %}

* **note off fade out time** – hoe lang het duurt voordat de noot vervaagt nadat deze is losgelaten. De waarde is in seconden (0–1). _100% = 1 seconde._
* **hit scale factor** – hoeveel de noot wordt vergroot wanneer deze wordt getriggerd (bijv. 2 = dubbele grootte).
* **hit scale hold time** – hoe lang de noot vergroot blijft voordat deze weer terug krimpt. De waarde is in seconden (0–1). _100% = 1 seconde._
* **hit scale decay time** – hoe lang het duurt voordat de noot terugkeert naar de oorspronkelijke grootte. De waarde is in seconden (0–1). _100% = 1 seconde._
* **note off shrink time** – hoe lang het duurt om terug te krimpen naar de oorspronkelijke grootte nadat de noot is losgelaten. De waarde is in seconden (0–1). _100% = 1 seconde._ (Heeft geen effect wanneer **leave all notes visible** is ingeschakeld.)

{% hint style="info" %}
Schalen - Let op: als je content uit één enkel punt bestaat, heeft schalen geen effect!
{% endhint %}
