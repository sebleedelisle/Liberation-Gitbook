---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Synkronisere tempo til et lydspor

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Synchronising tempo to an audio track" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

Tidslinjen i Liberation er laget for å fungere med både faste og skiftende tempoer, men pålitelig synkronisering starter alltid med å finne tempoet og plassere lyden riktig. Denne delen beskriver anbefalt arbeidsflyt.

#### 1. Juster første tunge slag

Legg lydsporet på tidslinjen og sørg for at det er festet til et slag, slik at det **første musikalske tunge slaget** i sporet ligger nøyaktig på starten av en takt.

Dette trinnet er avgjørende.

Hvis lyden ikke naturlig starter på et tungt slag, har du to alternativer:

* **Juster clip delay**\
  Høyreklikk på lydklippet og juster Delay-verdien til det første tunge slaget ligger på linje med en slag- eller taktmarkør.
* **Trim lyden eksternt**\
  Rediger lydfilen i et eksternt redigeringsprogram, for eksempel Audacity, slik at filen starter nøyaktig på det første tunge slaget, og importer den deretter på nytt.

{% hint style="info" %}
**Viktig:**\
Hvis starten av lyden ikke er justert til et slag eller en takt, vil den opplevde startposisjonen til musikken flytte seg bakover og fremover når du endrer tempoet. Dette gjør nøyaktig tempotilpasning svært vanskelig.
{% endhint %}

#### 2. Angi et starttempo

Hvis du har en omtrentlig idé om BPM, skriver du den inn i tempokontrollen på tidslinjen og starter avspilling fra begynnelsen.

Følg nøye med på slag- og taktmarkørene mens sporet spilles av.

* Hvis markørene driver foran musikken, reduser tempoet litt.
* Hvis de havner bak, øk tempoet litt.
* Stopp avspillingen, juster tempoet og prøv igjen.

For det meste av moderne musikk er tempoet et fast heltalls-BPM. Når du finner riktig verdi, bør den holde seg låst gjennom hele sporet.

#### 3. Bruk bølgeformen som visuell veiledning

Lydbølgeformen er en nyttig referanse når du skal matche tempo.

* Transienter og topper bør ligge på linje med de vertikale taktmarkørene.
* Zoom tett inn for å kontrollere justeringen over flere takter.

**Tips:**\
Bruk musehjulet eller styreflatebevegelse for å zoome tidslinjen. Bruk det horisontale rullehjulet eller en bevegelse for å flytte deg til venstre og høyre. Det er mye enklere å gjøre små justeringer når du jobber innzoomet.

#### 4. Spor med ikke-heltalls-BPM

Hvis sporet ikke bruker heltalls-BPM, vil drift skje mer gradvis.

* Zoom lenger inn.
* Bruk mindre tempojusteringer.
* Kontroller justeringen over lengre deler av sporet, ikke bare de første få taktene.

#### 5. Musikk med tempoendringer

Hvis musikken går raskere eller langsommere, bruker du Tempo Map:

* Spill av sporet og følg med på slagmarkørene.
* Når drift blir merkbar, legger du til en tempoendring på det punktet.
* Juster tempoet for den nye delen til det låser seg igjen.

Gjenta denne prosessen for hver tempoendring i musikken.

#### 6. Ekstern tempoanalyse (valgfritt)

Som en siste utvei kan du analysere sporet i en DAW, for eksempel Logic Pro, og generere et tempokart automatisk. Vær oppmerksom på at dette ofte lager et stort antall tempoendringer, noen ganger én per takt, som kan være mer detaljert enn nødvendig for de fleste show.
