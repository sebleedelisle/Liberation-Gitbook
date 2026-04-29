---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Kleurkalibratie

Kleurkalibratie zorgt ervoor dat de rode, groene en blauwe lasers van je projector op alle helderheidsniveaus op een vloeiende en voorspelbare manier licht geven. Verschillende projectoren kunnen niet-lineaire helderheidscurves hebben. Daardoor kan 50% rood er veel helderder of juist donkerder uitzien dan de helft van de intensiteit van 100% rood. Kalibratie corrigeert dit, zodat kleuren netjes mengen, verlopen vloeiend ogen en wit goed in balans is.

#### Je projector laten opwarmen

Laserdiodes gedragen zich anders naarmate ze opwarmen. Laat je projector daarom altijd stabiliseren voordat je gaat kalibreren:

* Projecteer minstens **15–20 minuten** een helder frame, zoals het **White rectangle test pattern (11)**.
* Zo blijft de kleurbalans die je instelt tijdens een show consistent.

#### Hoe de kalibratietest werkt

Gebruik de testpatronen voor kalibratie (zie [Testpatronen](../output-view/test-patterns.md "mention"))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Elk van deze patronen toont vier bewegende lijnen:

* **Bovenste lijn** – 100% helderheid op volledige snelheid
* **Tweede lijn** – 75% helderheid op 75% snelheid
* **Derde lijn** – 50% helderheid op 50% snelheid
* **Vierde lijn** – 25% helderheid op 25% snelheid

Omdat zowel de helderheid _als de snelheid_ samen worden geschaald, zouden alle lijnen even helder moeten lijken. Als een lijn lichter of donkerder lijkt, pas je de bijbehorende slider aan totdat ze overeenkomen.

Elk testpatroon heeft ook een vijfde lijn op **0% helderheid** die niet zichtbaar zou moeten zijn. Deze wordt gebruikt om lasers te corrigeren die op zeer lage niveaus nog geen licht geven. Als je laser bij lage helderheid onzichtbaar blijft, verhoog dan geleidelijk de **0% setting** totdat de lijn net zichtbaar is. Zet hem daarna iets terug totdat de lijn weer verdwijnt. Het doel is om de drempel te vinden waarop de laser begint op te lichten, en daar net onder te blijven - zodat je fades natuurlijk beginnen zonder het onderste bereik af te kappen.

#### Het paneel Colour Calibration gebruiken

Het paneel geeft je afzonderlijke bediening voor elk kanaal (rood, groen, blauw) op de niveaus 100, 75, 50, 25 en 0%.

1. **Selecteer een testpatroon** (begin met rood).
2. **Pas de sliders aan** zodat de lijnen van 100, 75, 50 en 25% even helder lijken.
3. **Stel de 0% slider bij** als de “uit”-lijn nog vaag zichtbaar is.
4. **Herhaal dit voor groen en blauw.**
5. Schakel over naar het **White test pattern (8)**. Alle vier lijnen moeten gelijk lijken, en het wit moet neutraal overkomen (zonder kleurzweem).

#### De witbalans aanpassen

Je kunt dit systeem ook gebruiken om de **witbalans** aan te passen. Nadat je elk kanaal afzonderlijk hebt gekalibreerd, schakel je over naar het **White test pattern (8)**. Als de output een kleurzweem heeft (bijvoorbeeld te groen of te blauw), pas dan de relatieve niveaus van de rode, groene en blauwe kanalen aan totdat de lijnen neutraal wit lijken. Zelfs als je lasers behoorlijk verschillen in vermogen, helpt kalibratie nog steeds om ze dichter bij elkaar te brengen en een schonere, beter gebalanceerde kleurmenging te maken.

#### Je kalibratie opslaan

* Gebruik **Store** om de huidige preset te overschrijven.
* Gebruik **Store As** om een nieuwe preset te maken (handig als je met meerdere lasers werkt).
