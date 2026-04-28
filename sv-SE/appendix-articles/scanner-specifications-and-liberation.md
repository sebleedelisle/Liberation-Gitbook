---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Scannerspecifikationer och Liberation

### Den röriga verkligheten bakom scannerspecifikationer

Punkthastigheter och scannerspecifikationer kan vara lite förvirrande. Du ser ofta specifikationer som 30kpps @ 8º eller 50kpps @ 4º, men det är inte alltid självklart vad de siffrorna faktiskt betyder.

{% hint style="info" %}
Ansvarsfriskrivning – jag är inte specialist på scannerhårdvara, men jag har många års praktisk erfarenhet av att få scannrar av väldigt olika kvalitet att se bra ut med hjälp av mjukvara och generering av punktströmmar, snarare än hårdvarujustering. Det här bygger på den erfarenheten.
{% endhint %}

#### **Varifrån siffrorna kommer**

Termer som ”30K” och ”50K” är förkortningar som bygger på hur scannrar utvärderas med ILDA-testmönstret vid dessa punkthastigheter under specifika förhållanden.

När en scanner anges som till exempel: _30Kpps @ 8°_ betyder det egentligen:

> ”Den här scannern kan återge ILDA-testmönstret vid 30 000 punkter/sekund med en skanningsvinkel på 8°, när den är korrekt intrimmad.”

Det är inte ett heltäckande eller fullt standardiserat mått på prestanda i verklig användning. Faktum är att det från början inte var avsett som ett riktmärke alls – det användes för en **intrimningsprocedur**. Du kör ett känt mönster med en fast punkthastighet (t.ex. 30 000 punkter/sekund) och justerar dämpning och gain tills det ser korrekt ut.

Men det är fortfarande den mest använda referensen vi har, och den kan ge en bra bild av scannrarnas kvalitet, åtminstone hos seriösa tillverkare. Hos _mindre seriösa_ tillverkare däremot...

#### Om du vill testa scannrarna enligt deras angivna specifikation

{% hint style="danger" %}
**Det här är en avancerad teknik och du kan skada dina scannrar om du inte är försiktig. Rekommenderas inte om du inte vet vad du gör.**
{% endhint %}

Du behöver hitta mjukvara som kan mata ut [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) – jag tror att LaserShowGen kanske kan göra det – och justera utmatningsstorleken så att den motsvarar den angivna skanningsvinkeln (t.ex. 8°). Se ILDA-dokumentationen för råd om hur du analyserar utsignalen.

#### Varför det kanske inte är ett bra riktmärke

För det första kan ditt testmönster visas fel även om dina scannrar är bra, eftersom de inte är intrimmade på ett sätt som är optimerat för just det.

Det kan vara en användbar allmän vägledning för ”bra” kontra ”dåliga” scannrar, men tillverkare kan ibland vara ganska fria i hur de använder de här specifikationerna.

#### Så hur väljer jag en bra scanner?

Jag skulle säga: se bara till att de är gjorda av en välrenommerad tillverkare. Dyra high-end-tillverkare av scannrar som Cambridge Technology (CT), Eye Magic (EMS) och ScannerMAX (ett dotterbolag till Pangolin) är alltid bra och du kan inte välja fel där. Men när ett par scannrar kostar runt 1000 dollar är det, för många av oss som precis börjar, dyrare än våra lasrar!

Så jag har mest använt kinesiska tillverkare. Dragon Tiger (DT)-scannrar är helt okej och prisvärda, och jag tror att LightSpace använder dem. Många andra tillverkare (inklusive OPT och Able i vissa modeller) använder också DT-baserade system.

Phenix Technology (PT) ligger generellt på en lägre nivå, men ärligt talat är de förmodligen tillräckligt bra för det mesta.

**Om dina scannrar saknar varumärke är det förmodligen då du bör börja oroa dig för kvaliteten!**

#### Hur Liberation hjälper

För det första: för det mesta behöver du inte riktigt dyra scannrar! Prisvärda 30kpps DT, eller till och med PT, fungerar bra. Standardinställningarna för scannrar är avsiktligt konservativa och i de flesta fall _ska du inte behöva justera dem_ (förutom _Scanner sync_).

Även om du har bättre scannrar finns det ingen poäng med att driva dem hårdare än nödvändigt. Det förlänger deras livslängd avsevärt.

#### Vad är en ”point stream”?

Du har säkert hört den här termen tidigare – det är så vi styr scannrarnas rörelsebana.

En punktström är en lista med X/Y-positioner, där varje position har en färg. För att rita till exempel en vit linje skickar du en sekvens av punkter längs den linjen, alla inställda på vitt. Scannrarna flyttar sig sedan från punkt till punkt med en fast hastighet – punkter per sekund (PPS) – och strålen ritar upp formen.

#### Hur det fungerar i traditionell lasermjukvara

Traditionell lasermjukvara lagrar en punktström för varje cue. För animerade cues innebär det vanligtvis en separat punktström för varje bildruta. Det viktiga är att allt är helt förutbestämt. Därför gör en högre punkthastighet att scannrarna rör sig snabbare genom samma fördefinierade data.

{% hint style="info" %}
För äldre mjukvara var det här arbetssättet nödvändigt – datorer var helt enkelt inte snabba nog för att generera punktströmmar i realtid. Det är därför det oftast finns en separat cue editor, som används för att förgenerera data för varje bildruta i en animation.

Det förklarar också varför innehåll kan ta upp flera gigabyte utrymme. Du lagrar i praktiken stora, okomprimerade vågformer med ganska höga samplingsfrekvenser.
{% endhint %}

#### Varför ”point rate” är mindre meningsfullt i Liberation

Liberation genererar punktströmmen i realtid, vilket ger oss väldigt stor flexibilitet. Lägg märke till inställningen "Scanner speed" i panelen Laser Settings. Den låter oss öka och minska scannrarnas hastighet, men det viktiga är att den **inte** ändrar den underliggande punkthastigheten (PPS).

#### Vänta, va? Hur då?

Jag vet, det låter konstigt i början.

Eftersom Liberation genererar punktströmmen i realtid kan det justera den punktströmmen. Ju mer utspridda punkterna är, desto snabbare rör sig scannrarna. Ju tätare de ligger, desto långsammare rör sig scannrarna.

{% hint style="info" %}
I nyare versioner av Liberation påverkar den faktiska _point rate_ (i avancerade inställningar) inte scannrarnas hastighet alls. I stället justerar renderaren punktfördelningen så att den matchar den valda punkthastigheten, samtidigt som scannrarnas rörelse hålls oförändrad.

Det påverkar punktbanans ”upplösning”, men det gör främst skillnad för grafik (och kan hjälpa till med finare justering av inställningen _scanner sync_).
{% endhint %}

#### Bra! Så vad betyder allt det här i praktiken?

Bra fråga. Här är mina tips:

* Undvik scannrar utan varumärke. Om du kan få snabbare scannrar, gör det – minst 30KPPS.
* I de flesta fall fungerar DT30-scannrar bra, och PT30-scannrar är förmodligen okej i billigare lasrar.
* Om du arbetar med grafik är fler lasrar i de flesta fall bättre än snabbare scannrar.
* När du kommer upp till mer avancerade system fungerar vilket som helst av de etablerade high-end-märkena bra.
* Om du bara kan få tag på de billigaste omärkta scannrarna är Liberations standardinställningar ganska konservativa, och du får förmodligen okej resultat för grundläggande beam-arbete. Om systemet får problem, sänk inställningen **Speed** (men ändra inte punkthastigheten!).

#### Och ILDA Test Pattern?

…är fortfarande mycket användbart som kalibrerings- och referensverktyg, men det var aldrig avsett som ett heltäckande riktmärke och kan missbrukas eller tolkas löst av tillverkare.
