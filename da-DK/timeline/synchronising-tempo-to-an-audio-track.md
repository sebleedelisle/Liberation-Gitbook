---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Synkronisering af tempo til et lydspor

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Synkronisering af tempo til et lydspor" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

Liberations tidslinje er designet til at arbejde med faste eller skiftende tempi, men pålidelig synkronisering starter altid med at finde tempoet og placere lyden korrekt. Dette afsnit beskriver den anbefalede arbejdsgang.

#### 1. Juster det første taktslag

Tilføj dit lydspor til tidslinjen, og sørg for, at det er snapped til et slag, så **det første musikalske taktslag** i sporet ligger præcist ved starten af en takt.

Dette trin er afgørende.

Hvis lyden ikke naturligt starter på et taktslag, har du to muligheder:

* **Juster clip-forsinkelsen**\
  Højreklik på lydclippet, og juster værdien Delay, indtil det første taktslag ligger på linje med et slag- eller taktmærke.
* **Trim lyden eksternt**\
  Rediger lydfilen i en ekstern editor som Audacity, så filen starter præcist på det første taktslag, og importér den derefter igen.

{% hint style="info" %}
**Vigtigt:**\
Hvis starten af lyden ikke er justeret til et slag eller en takt, vil musikkens oplevede startposition flytte sig frem og tilbage, når du ændrer tempoet. Det gør præcis tempomatching meget vanskelig.
{% endhint %}

#### 2. Indstil et starttempo

Hvis du har en omtrentlig idé om BPM, skal du indtaste den i tidslinjens tempokontrol og starte afspilning fra begyndelsen.

Hold nøje øje med slag- og taktmærkerne, mens sporet afspilles.

* Hvis markørerne driver foran musikken, skal du sænke tempoet en smule.
* Hvis de kommer bagud, skal du øge tempoet en smule.
* Stop afspilningen, juster tempoet, og prøv igen.

For det meste moderne musik er tempoet en fast BPM i hele tal. Når du har fundet den korrekte værdi, bør det forblive låst for hele sporet.

#### 3. Brug bølgeformen som visuel guide

Lydens bølgeform er en nyttig reference, når du matcher tempo.

* Transienter og peaks bør ligge på linje med de lodrette taktmærker.
* Zoom tæt ind for at kontrollere justeringen over flere takter.

**Tip:**\
Brug musehjulet eller en trackpad-bevægelse til at zoome på tidslinjen. Brug det vandrette rullehjul eller en bevægelse til at flytte til venstre og højre. Det er meget nemmere at lave små justeringer, når du arbejder zoomet ind.

#### 4. Spor med ikke-heltals-BPM

Hvis sporet ikke bruger en BPM i hele tal, vil drift ske mere gradvist.

* Zoom længere ind.
* Brug mindre tempojusteringer.
* Kontrollér justeringen over længere dele af sporet i stedet for kun de første par takter.

#### 5. Musik med temposkift

Hvis musikken bliver hurtigere eller langsommere, skal du bruge Tempo Map:

* Afspil sporet, og hold øje med slagmarkørerne.
* Når drift bliver tydelig, skal du tilføje et temposkift på det punkt.
* Juster tempoet for den nye sektion, indtil det låser igen.

Gentag denne proces for hvert temposkift i musikken.

#### 6. Ekstern tempoanalyse (valgfrit)

Som en sidste udvej kan du analysere sporet i en DAW som Logic Pro og automatisk generere et tempo map. Vær opmærksom på, at dette ofte giver et stort antal temposkift, nogle gange ét pr. takt, hvilket kan være mere detaljeret end nødvendigt for de fleste shows.
