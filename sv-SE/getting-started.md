---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Snabbstartsguide

## Introduktion

Välkommen till **Liberation** – nästa generation av programvara för lasershower.

Liberation är en kraftfull och komplex modern programvara. Den bygger på grundprinciper för användbarhet och tillförlitlighet, så att du får friheten att uttrycka din kreativitet. Den är snabb, effektiv och smidig. Följ den här _snabbstartsguiden_ så kommer du igång på nolltid!

### Hantera lasrar

Liberation är tillräckligt flexibelt för att du ska kunna konfigurera lasrar och visualisera dem utan att ha några faktiska lasrar anslutna alls. När du sedan är redo kan du enkelt tilldela varje output till en laser controller.

{% hint style="info" %}
Du kan konfigurera och visualisera så många lasrar du vill i Liberation. Licensnivåerna (Hobbyist, Pro osv.) begränsar bara antalet lasrar du kan _armera_. Det betyder att du kan designa lasershower med 100 lasrar även med en gratislicens. Du behöver bara uppgradera när du faktiskt ska köra showen på riktiga lasrar.
{% endhint %}

Standardinställningen har 8 lasrar placerade horisontellt, men du kan anpassa detta hur du vill. Det är troligen bäst att behålla standardinställningen medan du lär känna programmet, och senare justera den så att den matchar din hårdvarukonfiguration. (Se [Ställa in ditt projekt](setting-up/setting-up-your-project.md "mention"))

{% hint style="warning" %}
Viktigt: Innan du armerar några lasrar måste du förstå riskerna och noggrant gå igenom kapitlet [Översikt över hur du konfigurerar lasrar](setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Översikt över programvaran

### Säkerhetsavstängning

När du kör lasrar måste du alltid ha en **fysisk nödstoppsknapp** nära till hands (se [Nödstopp / säkerhetsförreglingar](hardware/emergency-stop-interlocks.md "mention")). Om du vill avarmera allt utan samma brådska kan du använda knappen _**DISARM ALL**_, eller tangenten `Escape` (eller tangenten _**SESSION**_ på APC40). Du kan också minska den globala ljusstyrkan med skjutreglaget på skärmen eller huvudreglaget på APC40.

### Skjutreglage och kontroller

I Liberation finns olika skjutreglage och kontroller.

{% hint style="info" %}
`Cmd / Ctrl`-klicka på ett skjutreglage för att skriva in ett nytt värde om du behöver mer precision än reglaget ger.
{% endhint %}

### Kortkommandon

En fullständig lista över kortkommandon finns här: [Tangentbordsgenvägar](reference/keyboard-shortcuts.md "mention")

### Skärmlayout

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Osäker på vad en viss knapp gör? Håll muspekaren över den för att se en beskrivning!
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

I menyn hittar du alla alternativ för import och export av filer samt för att öppna paneler. Här finns också alternativet för att auktorisera datorn med din prenumeration (under _Liberation -> Authorise/Deauthorise this computer_).

#### Icon bar

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Här finns vanliga funktioner, som att armera/avarmera alla lasrar, global ljusstyrka, testmönster och växling mellan vyerna 3D, Canvas och Output.

### Vyer

Det stora området längst upp till vänster på skärmen kan visa en av 3 huvudvyer: **3D**, **CANVAS** och **OUTPUT.** Växla mellan dem med knapparna i icon bar (eller använd tangenten `Tab` för att växla mellan 3D- och OUTPUT-vyerna och fortsätt sedan tabba igenom varje laser output i tur och ordning).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view visar hur dina lasrar kommer att se ut och kan konfigureras så att den matchar din egen laseruppsättning. Klicka och dra för att rotera kameran, och använd mushjulet för att röra dig framåt och bakåt. Du hittar många fler alternativ i panelen _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Se [3D Visualiser](setting-up/3d-visualiser.md "mention").

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output-vyn används för att konfigurera zoner och masker för varje laser. (Lägg märke till det stora numret uppe till vänster så att du enkelt ser vilken laser du arbetar med!)

Den här vyn representerar hela outputen från den här lasern och visar var varje zon ligger inom den. Som standard finns det bara en zon per laser, men du kan lägga till så många zoner som är praktiskt rimligt, och du ser dem alla i den här vyn.

{% hint style="info" %}
**Vad är en zon?**

En zon är ett utrymme inom en lasers output som du kan skicka laserinnehåll till. Du kan ha fler än en zon per laser. Den enklaste typen av zon är en _beam_-zon, men det finns även _canvas_-zoner och _DMX_-zoner. I den här guiden fokuserar vi främst på beam-zoner, som vanligtvis används för att skapa atmosfäriska stråleffekter i luften.
{% endhint %}

Du kan välja vilken laser du vill redigera på något av följande sätt:

* de numrerade knapparna i listen högst upp
* tryck på siffertangenten för den laser du vill använda (_tangenterna 1–9_)
* tangenten `Tab` för att gå igenom dem en i taget

Lägg till en ny laser i uppsättningen genom att trycka på knappen _+_. (Det finns också en _ADD LASER_-knapp i panelen _Laser Overview_)

Ta bort en laser från uppsättningen genom att trycka på den röda ⊖-knappen i panelen _Laser Overview_.

Du kan zooma in och ut med mushjulet, och klicka och dra var som helst där det inte finns en zon för att flytta vyn.

Klicka på en zon för att markera den och justera sedan hörnpunkterna med musen. Håll ned tangenten `Alt / Option` medan du drar ett hörn för att göra justeringen icke-uniform. Högerklicka på zonen för att se fler alternativ, inklusive att ändra zontyp.

Längs vänsterkanten finns en list med ett antal ikonknappar. Håll muspekaren över en knapp för att få en beskrivning av vad den gör. Knapparna här låter dig lägga till beam-zoner, canvas-zoner och masker. Det finns också alternativ för att aktivera ett testmönster endast för den här lasern samt inställningar för rutnät och snapping.

Mer information finns i [Output-vy](output-view/ "mention").

#### Canvas

Canvas-systemet används främst för grafik och arkitektonisk mapping. Du kan fördela komplexa bilder över flera lasrar och perspektivkorrigera varje sektion. Se [Grafik och Canvas-systemet](graphics-and-the-canvas-system/ "mention").

### APC40 MIDI controller

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Även om det går att styra Liberation med mus och tangentbord är det mycket bättre att använda ett APC40 MIDI controller-gränssnitt (Mark 2 är bäst, men Mark 1 fungerar också).

Se även: [APC40-referens](reference/apc40-reference.md "mention")

Liberation har även stöd för APC Mini och MIDI Fighter Twister. APC40 Mark 2 är fortfarande det bästa alternativet i de flesta fall.

### Clips och effekter

{% hint style="info" %}
**Vad är ett Clip?**

Ett Clip är en behållare för laserinnehåll i Liberation. Clips kan innehålla beams eller grafiska animationer och är vanligtvis en loopande cykel. De kan skickas till valfri zon (eller _Canvas target area_) och triggas med clip-knapparna i Clip Deck.
{% endhint %}

#### Översikt över Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Det här rutnätet kallas _Clip Deck_ och är platsen där alla laser-Clips lagras. Det är utformat för att mappas direkt till 8 x 5-rutnätet med knappar på din APC40.

**Navigera i Clip Deck.**

Du kan rulla Clip Deck åt vänster och höger med:

* Vänster- och högerpiltangenterna. Lägg till `Cmd / Ctrl` för att rulla en hel sida i taget.
* Trackpad: Svep
* Mus: om din mus har horisontell rullning kan du använda den när muspekaren är över Clip Deck
* APC40 scroll knob
* APC40 _<- DEVICE ->_-knapparna

För att hjälpa dig orientera dig finns en minivisualisering av Clip Deck längs ovankanten. Se även [Clips och Clip Deck](clips/ "mention")

#### Starta och stoppa Clips

Tryck på en clip-knapp (antingen med musen eller med APC40) för att starta ett Clip. Tryck igen för att stoppa det. När du startar ett Clip stoppas alla andra Clips med samma färg automatiskt, om du inte håller ned _shift_.

Vissa Clips är i _Flash mode_ (som standard de röda), och då stoppas de så snart du släpper clip-knappen.

Knappen _STOP_ stoppar alla Clips som körs för tillfället.

#### Ställa in output-zoner för Clip

Under clip-knapparna ser du zonknapparna, som standard beam-zoner 1 till 8 (_BEAM 1_, _BEAM 2_ osv.). Zonknapparna lyser för att visa vilka zoner som är tilldelade det Clip som är markerat för tillfället.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Två rader under zonknapparna ser du X/Y flip-knapparna. Växla dessa för att spegelvända Clip horisontellt och vertikalt.

{% hint style="info" %}
Observera att dessa zontilldelningar och X/Y flip-inställningar är kopplade till själva Clip. De behålls nästa gång du kör det Clip. De är inte en global inställning.
{% endhint %}

Högerklicka på ett Clip för att redigera fler inställningar för det. Se även [Clip-inställningar](clips/clip-settings.md "mention")

### Grupper

Du ser att varje Clip har en färgad kontur, och den färgen visar vilken _group_ det tillhör. Clip-knapparna på APC40 lyser också i den färgen.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyan</td></tr><tr><td>Group 2</td><td>Orange</td></tr><tr><td>Group 3</td><td>Röd</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Grön</td></tr></tbody></table>

Gruppsystemet är mycket flexibelt och låter dig:

* Låta Clips i en grupp fortsätta köra medan du växlar grupper i en annan
* Snabbt tilldela zoner och X/Y flips till alla Clips inom en grupp
* Ställa in _Flash mode_ för ett Clip (Group 3 är inställd på _Flash mode_ som standard)

Grupper har också inställningar för transition in/out som kan ärvas av gruppens Clips eller åsidosättas.

Du kan tilldela grupp för ett Clip med knapparna i högerklicksmenyn, eller med APC40 genom att trycka på gruppknappen och, _medan den fortfarande hålls nedtryckt_, trycka på clip-knapparna.

Ändra zoninställningar för alla Clips inom en grupp

Med APC40: tryck på gruppknappen och använd sedan, _medan den fortfarande hålls nedtryckt_, zon- och X/Y-knapparna för att växla zoninställningar för alla Clips inom den gruppen.

Se även [Clip groups](clips/groups.md "mention")

### Effekter

Effektsystemet i Liberation är ett kraftfullt och mångsidigt sätt att ändra clip-output i realtid. Standardknapparna för effekter 1–8 finns under zonknapparna.

#### Applicera en effekt

Tryck på en effektknapp för att slå på eller av effekten, eller ännu hellre: använd APC40-reglagen 1–8 för att tona effekter in och ut.

#### Effektparametrar

Använd rotary controllers 1–8\* för att justera _parameter_ för varje effekt. (Du kan också högerklicka med musen för att justera nivå och parameter.) Parameterändringen gör olika saker beroende på hur effekten är konfigurerad. Se listan nedan för standardeffekterna.

{% hint style="info" %}
De små siffrorna du ser på effektknapparna avser effektens _level_ och _parameter_. _Level_ styrs av fadern på APC40, eller så kan du klicka och dra på knappen. Parametern justeras med rattarna på APC40, eller så kan du högerklicka för att justera med musen.
{% endhint %}

_\*Rotary controllers 1–8 sitter längs ovankanten på en APC40 Mk2 och uppe till höger på Mk1. Se även:_ [APC40-referens](reference/apc40-reference.md "mention")

#### Standardeffekterna

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Applicerar en kaotisk rörelse på clip-outputen. Parametern justerar mängden/hastigheten på kaoset.
2. **Sine wave** :\
   Förvränger allt innehåll längs en rörlig sinusvåg. Parametern justerar våglängden.
3. **Rotation** :\
   Snurrar allt runt. Parametern justerar rotationshastigheten.
4. **Horizontal flip** :\
   Trycker ihop och sträcker ut allt horisontellt. Parametern justerar hastigheten.
5. **Scale** :\
   Skalar upprepade gånger allt från fullt till noll. Parametern justerar hastigheten.
6. **Hue** :\
Ändrar nyansen på allt, men ändrar inte mättnaden (dvs. allt som är vitt förblir vitt). Parametern justerar nyansen.
7. **Saturation and hue** :\
Ändrar nyansen på allt och mättar även färgen helt (dvs. allt som är vitt ändras till färgen). Parametern justerar nyansen.
8. **Flash** :\
   Blinkar upprepade gånger ljusstyrkan på allt från fullt till noll. Parametern justerar blinkhastigheten.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Det finns ytterligare 16 färgeffekter längs den nedersta raden för att använda förinställda värden för hue och saturation.

Observera att detta är standardeffekterna, men de kan redigeras för att göra nästan vad du vill!

#### Vad är _det Clip som är valt just nu_?

När du startar ett Clip tänds det för att visa att det är aktivt. Det har också en vit kontur runt sig, vilket visar att detta är det Clip som är valt just nu. När du växlar zonknappar eller justerar clip-inställningarna tillämpas dessa på _det Clip som är valt just nu_.

{% hint style="info" %}
För att välja ett Clip utan att trigga det, tryck på tangenten `Alt / Option` innan du trycker på clip-knappen. Det är ett bra sätt att justera zoner och andra inställningar utan att köra det.
{% endhint %}

### Clip Settings-panel

Använd panelen _Clip Settings_ för att redigera skalning, X/Y-position och få tillgång till det kraftfulla systemet för zone delay.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings-panel

I panelen _Global Settings_ kan du justera globala output-inställningar som påverkar all output i alla zoner.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Slå på AUTO RESET för att automatiskt återställa alla _Global settings_ när inga Clips spelas.

### Timing

Nästan alla laserframträdanden har någon form av musikspår, så timing-systemet i Liberation bygger på ett tempo i slag per minut. I _Tempo Panel_ kan du se en representation av tiden. Varje ruta motsvarar ett slag och du kan se dem blinka i takt.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Det finns flera synkroniseringsalternativ, inklusive MIDI clock och Ableton Link. Om du känner till musikens tempo kan du justera det manuellt med skjutreglaget på skärmen eller APC40 Tempo-ratten, men du kan också hålla takten med musiken med hjälp av _Tap Tempo_-systemet.

#### Tap Tempo

_Tap Tempo_ är en term som ofta används i musikappar och låter dig knacka i takt med beatet för att ställa in tempot medan musiken spelas. Du kan använda knappen på skärmen, men det rekommenderas att du använder tangenten _T_ eller _Tap Tempo_-knappen på APC40 (eller till och med en fotpedal om du föredrar det).

Tryck på tangenten _R_ eller knappen _Metronome_ (APC40) för att återställa tempot till början av takten.

Tryck på tangenten _Y_ eller vrid på _Tempo_-ratten (APC40) för att avrunda tempot till ett heltal. Det kan vara användbart för elektronisk musik, som ofta har ett jämnt antal slag per minut.

### Organisera ditt Clip Deck

För att flytta ett Clip i ditt Clip Deck klickar du och drar det till en ny position. Medan du drar kan du använda piltangenterna (eller scrollhjulet/knapparna på din APC40) för att rulla åt vänster och höger.

Håll ned tangenten `Alt / Option` medan du drar för att skapa en kopia.

`Alt / Option`-klicka på ett Clip för att välja det utan att starta det.

`Alt / Option + Shift`-klicka på ett Clip för att multivälja, eller klicka och dra utanför ett Clip för att markera med "lasso".

Klicka och dra flyttar ALLA markerade Clips.

För att ta bort ett eller flera Clips drar du dem antingen bort från Clip Deck (en papperskorgsikon visas) eller använder knappen DELETE i högerklicksmenyn för Clip.

### Laser Overview-panel

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panelen _Laser Overview_ ger dig en snabb överblick över statusen för de lasrar som körs för tillfället. Den gröna rutan till höger visar att laser controller fungerar som den ska. Om den blir orange har du tillfälliga drop-outs, och om den blir röd har den kopplats från. Om den är grå är den inte ansluten till någon controller alls.

Grafen i mitten visar en historik över bildrutornas längd, och numret till höger är aktuell bildfrekvens. Ju mer komplicerat innehållet är, desto långsammare blir bildfrekvensen (dvs. mer flimmer). Allt under ungefär 25 fps börjar se lite flimrigt ut.

### Ansluta till lasrar – Controller Assignment-panel

Klicka på knappen _Assign Laser Controllers_ för att öppna panelen _Controller Assignment_. (Den här panelen kan också nås via _View -> Controller Assignment_ i menyraden).

Här kan du välja vilka laser outputs som ska gå till vilka laser controllers. Dra och släpp controllers från listan till höger till platserna till vänster. Du kan byta namn på dina controllers så att de matchar den laser de är kopplade till (använd pennikonen).

Läs kapitlet [Tilldela kontroller](setting-up/controller-assignment.md "mention") för mer information.

{% hint style="danger" %}
Innan du armerar några lasrar måste du gå igenom kapitlet [Översikt över hur du konfigurerar lasrar](setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Laser output-panel

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Den här panelen visar inställningarna för den _currently selected laser_ (representerad av numret längst upp). Byt vilken laser som är markerad med tangenten _tab_, genom att trycka på en siffertangent, klicka på ett lasernummer i panelen _Laser Overview_ eller i _output view._

* **Number button** armerar och avarmerar lasern. Om den är röd är lasern armerad.
* **Brightness** justerar laserns ljusstyrka oberoende av de andra lasrarna (och kombineras med inställningen _global brightness_ – dvs. om båda står på 50 % blir din laser 25 %).
* **Test Pattern** aktiverar ett testmönster endast för den här lasern (åsidosätter den globala inställningen för testmönster)
* **Orientation** korrigerar för lasrar som är riggade på sidan eller upp och ned.
* **Flip Horizontal and Flip Vertical** vänder laserns output. Användbart för output-korrigering på lasrar med inkonsekvent kabeldragning.
* **Copy Laser Settings** öppnar en panel där du kan kopiera olika inställningar från den här lasern till andra.

### Scanner settings

Displaylasrar fungerar genom att flytta en enda laserstråle extremt snabbt och slå på och av den för att rita former i luften. Det du ser som linjer, former och bilder är egentligen strålen som följer banor snabbare än ögat hinner uppfatta.

En point stream är den data som talar om för lasern vart den ska flytta sig härnäst och när strålen ska vara på eller av. I Liberation omvandlas Clips till denna point stream i realtid när de skickas till lasrarna.

Liberation ger dig detaljerad kontroll över hur denna point stream genereras, så att du kan balansera mjukhet, ljusstyrka och prestanda för varje laser.

{% hint style="info" %}
Om du är van vid äldre laserprogramvara som bygger på förberäknade point streams kan det här arbetssättet kännas annorlunda i början. Men point-generering i realtid gör att samma innehåll kan optimeras olika för varje laser. Det gör det enklare att arbeta med flera lasrar som har olika scannerhastigheter eller kvalitet, utan att duplicera eller bygga om innehåll. Det håller också clip-filer mycket små, vilket är anledningen till att hela Liberation Clip Deck som följer med som standard bara är några få megabyte i stället för gigabyte.
{% endhint %}

De grundläggande scanner settings är:

* **Speed** är scannerhastigheten, dvs. hur snabbt lasern rör sig för att rita former. Det motsvarar att justera point rate i traditionell laserprogramvara, men i Liberation kan du ändra hur snabbt lasern rör sig _oberoende av point rate._ Du ska normalt inte behöva justera detta.
* **Scanner sync** (kallas ibland _blank shift_, tidigare Colour Shift) Scanners flyttar lasern mycket snabbt, men förändringar i ljusstyrka och färg är oftast inte synkade med rörelsen. Det syns som små flimrande "svansar" av ljus vid kanten av beams och linjer. Använd den här justeringen för att synka rörelse och färg med varandra. Se [Panelen Laser output settings](setting-up/laser-settings.md "mention")

De andra avancerade scanner-inställningarna behandlas i kapitlet [Avancerat](advanced/ "mention").

### Zoning

En fullständig guide till att konfigurera och zona lasrar finns här: [Översikt över hur du konfigurerar lasrar](setting-up/setting-up-lasers.md "mention")
