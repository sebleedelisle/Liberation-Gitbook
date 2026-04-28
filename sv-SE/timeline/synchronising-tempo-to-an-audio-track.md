---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Synkronisera tempo med ett ljudspår

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Synkronisera tempo med ett ljudspår" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

Liberations tidslinje är utformad för att fungera med fasta eller föränderliga tempon, men pålitlig synk börjar alltid med att hitta tempot och placera ljudet korrekt. Det här avsnittet beskriver det rekommenderade arbetsflödet.

#### 1. Rikta in det första nedslaget

Lägg till ditt ljudspår på tidslinjen och se till att det snäpps mot ett slag, så att spårets **första musikaliska nedslag** ligger exakt i början av en takt.

Det här steget är avgörande.

Om ljudet inte naturligt börjar på ett nedslag har du två alternativ:

* **Justera klippfördröjningen**\
  Högerklicka på ljudklippet och justera värdet Delay tills det första nedslaget ligger i linje med en slag- eller taktmarkör.
* **Trimma ljudet externt**\
  Redigera ljudfilen i ett externt redigeringsprogram, till exempel Audacity, så att filen börjar exakt på det första nedslaget. Importera den sedan igen.

{% hint style="info" %}
**Viktigt:**\
Om början av ljudet inte är inriktad mot ett slag eller en takt kommer musikens upplevda startposition att flyttas bakåt och framåt när du ändrar tempot. Det gör exakt tempomatchning mycket svårt.
{% endhint %}

#### 2. Ställ in ett initialt tempo

Om du har en ungefärlig uppfattning om BPM-värdet anger du det i tidslinjens tempokontroll och startar uppspelningen från början.

Titta noga på slag- och taktmarkörerna medan spåret spelas upp.

* Om markörerna driver före musiken, sänk tempot något.
* Om de hamnar efter, höj tempot något.
* Stoppa uppspelningen, justera tempot och försök igen.

För det mesta av modern musik är tempot ett fast heltals-BPM. När du har hittat rätt värde bör det ligga låst genom hela spåret.

#### 3. Använd vågformen som visuell guide

Ljudets vågform är en användbar referens när du matchar tempo.

* Transienter och toppar bör ligga i linje med de vertikala taktmarkörerna.
* Zooma in ordentligt för att kontrollera inriktningen över flera takter.

**Tips:**\
Använd mushjulet eller en styrplattegest för att zooma tidslinjen. Använd det horisontella scrollhjulet eller en gest för att flytta åt vänster och höger. Det blir mycket enklare att göra små justeringar när du arbetar inzoomat.

#### 4. Spår med icke-heltals-BPM

Om spåret inte använder ett heltals-BPM blir driften mer gradvis.

* Zooma in mer.
* Använd mindre tempojusteringar.
* Kontrollera inriktningen över längre delar av spåret i stället för bara de första takterna.

#### 5. Musik med tempoändringar

Om musiken ökar eller sänker tempot använder du Tempo Map:

* Spela upp spåret och titta på slagmarkörerna.
* När driften blir märkbar lägger du till en tempoändring vid den punkten.
* Justera tempot för det nya avsnittet tills det ligger rätt igen.

Upprepa processen för varje tempoändring i musiken.

#### 6. Extern tempoanalys (valfritt)

Som en sista utväg kan du analysera spåret i en DAW, till exempel Logic Pro, och generera en tempokarta automatiskt. Tänk på att detta ofta skapar ett stort antal tempoändringar, ibland en per takt, vilket kan vara mer detaljerat än vad som behövs för de flesta shower.
