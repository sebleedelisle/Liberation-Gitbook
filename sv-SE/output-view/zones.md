---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

Den huvudsakliga typen av zon som du kommer att använda i de flesta projekt är _Beam zone_. Det är en zon som är utformad för atmosfäriska beam-effekter genom luften. Den andra typen av zon är en _Canvas zone_ (se [Grafik och Canvas-systemet](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**VARNING – Var extremt försiktig när du flyttar zoner medan lasern är igång** och sänk ljusstyrkan så mycket det går. Se [Översikt över hur du konfigurerar lasrar](../setting-up/setting-up-lasers.md "mention") för en komplett guide om hur du aktiverar och zonindelar lasrar på ett säkert sätt
{% endhint %}

Du kan klicka och dra zonerna med musen. Slå på ett testmönster för att se vart zonen hamnar.

{% hint style="info" %}
Använd piltangenterna för att **finjustera** den zon eller punkt som är markerad. Håll ned `Shift` för att flytta i större steg.
{% endhint %}

{% hint style="info" %}
Tips: du kan snabbt kopiera zoninställningar mellan flera lasrar! Se [Kopiera inställningar mellan lasrar](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Lägga till en ny beam-zon

Klicka på knappen _Add a new beam zone_ högst upp i verktygsfältet så visas en ny zon. Observera att beam-zoner sorteras i den ordning du lägger till dem, men du kan ändra ordningen. Se [Ändra ordning på beam zones](re-ordering-beam-zones.md "mention")

### Lägga till en befintlig canvas-zon

Klicka på knappen _Add existing canvas zone_ så visas en lista över tillgängliga canvas-zoner, och du kan slå på eller av dem för den här lasern. Se [Grafik och Canvas-systemet](../graphics-and-the-canvas-system/ "mention")

### Zonformtyper

Det finns 3 zonformtyper:

* **Quad** – standardformen för en rektangulär zon, som kan vara rak (axeljusterad) eller förvrängd. Passar bäst för större rektangulära zoner eller canvas-zoner som kräver perspektivkorrigering.
* **Line/Curve** – en zon som definieras av 2 eller fler punkter och en tjocklek. Idealisk för smala zoner eller för avgränsning mot balkonger, broar eller andra böjda former.
* **Segmented** – en zon som kan delas upp i mindre quads. Idealisk för arkitektonisk mapping.

Högerklicka på en zone för att öppna dess inställningar. I den här högerklicksmenyn kan du:

* Byta namn på zonen (det kan vara praktiskt för att identifiera den i Clip Deck, särskilt om du har många zoner!)
* Aktivera/inaktivera zonen
* Låsa dess position
* Ändra dess formtyp
* Återställa den till standardpositionen
* Komma åt inställningar som är specifika för formtypen
* Ta bort den
* Lägga till en _Alt Zone_ (se [Alt zone-system](alt-zone-system.md "mention"))

{% hint style="danger" %}
**VARNING –** var mycket försiktig när du ändrar zontyp medan lasern är aktiv. Zonen återgår till den senaste positionen/storleken för den formen, så output kan ändras plötsligt. Det är bäst att stänga av lasern innan du ändrar zontyp.
{% endhint %}

### Quad-zonform

Du kan flytta varje hörn i quaden med musen. `Alt / Option`-klicka på ett hörn för att flytta det oberoende av de andra och förvränga quaden. När quaden väl är förvrängd kan alla hörn flyttas fritt.

Du kan ta bort förvrängningen och återställa den till en axeljusterad rektangel med knappen _REMOVE DISTORTION_ i högerklicksmenyn.

#### Perspektivkorrigering

Det här alternativet kan ställas in med växlingsknappen i högerklicksmenyn och avgör vilken förvrängningsmetod som används. Det är bäst att ha detta avstängt för beams, men om denna zone projicerar grafik på ett plant underlag kan du slå på det så perspektivkorrigeras outputen.

{% hint style="info" %}
Om _Perspective correction_ är avstängt förvrängs innehållet med _bilinjär interpolering_. Med andra ord fördelas innehållet jämnt över quaden. Det är därför det passar bäst för beams.

När perspektivkorrigering är påslagen förvrängs innehållet med perspektivwarping, vilket kompenserar för förkortning i perspektiv. Om du till exempel projicerar grafik på en vägg i sned vinkel kan du använda detta för att räta upp outputen och korrigera projektionsförvrängningen.
{% endhint %}

### Line / Curve-zonform

Zonformen Line / Curve har blivit mitt standardval i senare shower, och man skulle kunna hävda att den borde vara standard för beam-zoner.

Ofta behöver mina zoner vara smala för att passa in i besvärliga, smala utrymmen på spelplatser eller mellan fönster på byggnader, och jag märkte att det kunde vara riktigt pilligt att justera fyra hörn på en quad när de ligger så nära varandra. Så föddes Line / Curve-zonen!

För raka linjer behöver du bara två punkter och justerar sedan _Zone thickness_ i högerklicksmenyn. Det är det snabbaste sättet att skapa enkla zones.

`Alt / Option`-klicka på linjen för att skapa fler punkter. Dessa punkter jämnas automatiskt ut för att skapa en flytande form, och du kan justera _Smooth level_ för att släta ut eventuella knyckar.

`Alt / Option`-klicka på en punkt för att ta bort den.

Om du är van vid vektorgrafikprogram (Inkscape, Illustrator osv.) kan du också använda alternativet _Manually adjust bezier curves_ för att finjustera alla kontrollpunkter.

### Segmented-zonform

Den här uppdelade zonen låter dig göra mycket detaljerade korrigeringar och är användbar när du mappar mot komplexa former. Du kan lägga till eller ta bort uppdelningar med knapparna + och - i högerklicksmenyn.

### Så redigerar du en zon som är helt täckt av en annan zon

Högerklicka på zonen ovanpå och klicka på hänglåsknappen för att låsa den. Nu bör du kunna redigera och justera zonen under.

<br>

{% hint style="info" %}
När du har lagt till en Beam zone i din output kan den läggas till i ett clip i Clip Deck.
{% endhint %}
