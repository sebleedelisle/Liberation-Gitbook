---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Tempo synchroniseren met een audiotrack

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Tempo synchroniseren met een audiotrack" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

De timeline van Liberation is ontworpen om te werken met vaste of veranderende tempo’s, maar betrouwbare synchronisatie begint altijd met het vinden van het juiste tempo en het correct uitlijnen van de audio. In dit gedeelte lees je de aanbevolen werkwijze.

#### 1. Lijn de eerste downbeat uit

Voeg je audiotrack toe aan de timeline en zorg dat deze aan een tel is gesnapt, zodat de **eerste muzikale downbeat** van de track exact samenvalt met het begin van een maat.

Deze stap is essentieel.

Als de audio niet vanzelf op een downbeat begint, heb je twee opties:

* **Pas de clipvertraging aan**\
  Klik met de rechtermuisknop op de audioclip en pas de waarde Delay aan totdat de eerste downbeat samenvalt met een tel- of maatmarkering.
* **Trim de audio extern**\
  Bewerk het audiobestand in een externe editor zoals Audacity, zodat het bestand exact op de eerste downbeat begint, en importeer het daarna opnieuw.

{% hint style="info" %}
**Belangrijk:**\
Als het begin van de audio niet is uitgelijnd met een tel of maat, verschuift de waargenomen startpositie van de muziek naar achteren en naar voren wanneer je het tempo wijzigt. Daardoor wordt nauwkeurig tempo matchen extreem lastig.
{% endhint %}

#### 2. Stel een begintempo in

Als je ongeveer weet wat de BPM is, voer je die in bij de tempobesturing van de timeline en start je de weergave vanaf het begin.

Let tijdens het afspelen goed op de tel- en maatmarkeringen.

* Als de markeringen vóór de muziek gaan lopen, verlaag je het tempo iets.
* Als ze achterblijven, verhoog je het tempo iets.
* Stop de weergave, pas het tempo aan en probeer het opnieuw.

Bij de meeste moderne muziek is het tempo een vast BPM-getal zonder decimalen. Zodra je de juiste waarde hebt gevonden, zou deze voor de hele track vergrendeld moeten blijven.

#### 3. Gebruik de waveform als visuele hulp

De audiowaveform is een handige referentie bij het matchen van het tempo.

* Transiënten en pieken moeten samenvallen met de verticale maatmarkeringen.
* Zoom ver in om de uitlijning over meerdere maten te controleren.

**Tip:**\
Gebruik het muiswiel of een trackpadgebaar om in en uit te zoomen op de timeline. Gebruik het horizontale scrollwiel of gebaar om naar links en rechts te bewegen. Ingezoomd werken maakt kleine aanpassingen veel eenvoudiger.

#### 4. Tracks met niet-gehele BPM

Als de track geen BPM gebruikt zonder decimalen, zal de drift geleidelijker zijn.

* Zoom verder in.
* Gebruik kleinere tempoaanpassingen.
* Controleer de uitlijning over langere delen van de track, niet alleen over de eerste paar maten.

#### 5. Muziek met tempoveranderingen

Als de muziek versnelt of vertraagt, gebruik je de Tempo Map:

* Speel de track af en let op de telmarkeringen.
* Wanneer de drift merkbaar wordt, voeg je op dat punt een tempoverandering toe.
* Pas het tempo voor het nieuwe gedeelte aan totdat het weer vastloopt.

Herhaal dit proces voor elke tempoverandering in de muziek.

#### 6. Externe tempoanalyse (optioneel)

Als laatste redmiddel kun je de track analyseren in een DAW zoals Logic Pro en automatisch een tempo map genereren. Houd er rekening mee dat dit vaak een groot aantal tempoveranderingen oplevert, soms één per maat, wat voor de meeste shows gedetailleerder kan zijn dan nodig.
