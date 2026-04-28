---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Tilldela kontroller

När du har ställt in lasrarna i Liberation kan du tilldela var och en av dem till en laserkontroller i den verkliga världen. (Se [compatible-lasers-and-controllers-dacs.md](../hardware/compatible-lasers-and-controllers-dacs.md "mention") för att kontrollera vilken hårdvara du kan använda). Kontrollerna ansluts antingen via USB eller över nätverket.

* Öppna panelen _Controller Assignment_ via menyalternativet _View -> Controller Assignment_. (Alternativt kan du använda knappen _ASSIGN LASER CONTROLLERS_ i panelen _Laser Overview_.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment-panel"><figcaption></figcaption></figure>

* Panelen är uppdelad i två delar, med en lista över lasrar till vänster och en lista över tillgängliga kontroller till höger. Om du inte ser din laserkontroller i listan trycker du på knappen _REFRESH_. Om du fortfarande har problem, se [troubleshooting](../troubleshooting/ "mention").
* För att tilldela en kontroller till en laser klickar du och drar från höger till en ledig laserplats till vänster. Detta talar om för Liberation vilken kontroller som ska användas för vilken laser. (Om du ändrar dig kan du fritt dra kontrollerna upp och ner från en laser till en annan.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Lista över kontroller" width="375"><figcaption></figcaption></figure>

* Om du ser en grön fyrkant bredvid kontrollern betyder det att Liberation har anslutit till den.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>En Ether Dream och en Helios DAC tilldelade till laser 2 respektive 3</p></figcaption></figure>

{% hint style="info" %}
Observera att när du ansluter till en kontroller avarmeras lasern automatiskt.
{% endhint %}

* En orange fyrkant 🟧 betyder att kontrollern har tillfälliga anslutningsproblem. Det beror vanligtvis på ett nätverksproblem, se [troubleshooting](../troubleshooting/ "mention").
* En röd fyrkant 🟥 betyder att kontrollern inte kan nås, se [troubleshooting](../troubleshooting/ "mention").
* _disconnect button_ (X) kopplar från kontrollern men tar inte bort den från lasertilldelningen. Du kan sedan använda _reconnect button_ (ikonen med uppdateringspil) för att ansluta den igen, eller klicka på _disconnect button_ igen för att ta bort tilldelningen.
* _Avancerad funktion:_ Öppna analys-panelen för kontrollern genom att klicka på knappen som ser ut som ett diagram. Detta är en avancerad funktion som ger dig detaljerad information om dataströmmen och kan hjälpa dig att felsöka problem. (Det här alternativet kanske inte är tillgängligt för vissa kontrollertyper.)
* Du kan använda _rename button_ (pennan) för att byta namn på den här kontrollern till vad du vill. Det är klokt att namnge den på ett sätt som gör det enkelt att koppla den till en viss hårdvara. Om den är inbyggd i en laser kan du namnge den därefter, till exempel _LaserCube Ultra #1_ eller _Triton T5 #3._ Dessa namn sparas med din Liberation-installation och visas framöver. Det kan vara till stor hjälp när du snabbt behöver identifiera dina lasrar.

{% hint style="info" %}
Proffstips – **dubbelklicka** på en kontroller till höger för att automatiskt tilldela den till nästa tillgängliga laser till vänster. Det kan spara mycket tid om du har många lasrar att tilldela!
{% endhint %}

Du kan använda knapparna _DISCONNECT ALL_ och _RECONNECT ALL_ för att snabbt återställa alla anslutningar. Det är användbart om du har nätverksproblem.
