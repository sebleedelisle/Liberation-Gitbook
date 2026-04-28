# ✅ Snabbstartsguide

## Introduktion

Välkommen till **Liberation** – nästa generation av lasershowprogramvara.

Liberation är en kraftfull och avancerad modern programvara. Den bygger på grundläggande principer om användbarhet och tillförlitlighet, så att du får frihet att uttrycka din kreativitet. Den är snabb, effektiv och sömlös. Följ den här _snabbstartsguiden_ så kommer du igång på nolltid!

### Hantera lasrar

Liberation är tillräckligt flexibelt för att du ska kunna konfigurera och visualisera lasrar utan att några fysiska lasrar alls är anslutna. När du sedan är redo kan du smidigt tilldela varje utgång till en laserkontroller.

{% hint style="info" %}
Du kan konfigurera och visualisera hur många lasrar du vill i Liberation. Licensnivåerna (Hobbyist, Pro osv.) begränsar bara hur många lasrar du kan _arma._ Det betyder att du kan designa lasershower med 100 lasrar även med en gratislicens. Du behöver bara uppgradera när det är dags att faktiskt köra showen på riktiga lasrar.
{% endhint %}

Standardinställningen har 8 lasrar utspridda horisontellt, men du kan anpassa detta precis som du vill. Det är troligen bäst att behålla standardinställningen medan du lär känna programvaran, och senare justera den så att den matchar din hårdvaruuppsättning. (Se [setting-up-your-project.md](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Viktigt: Innan du armar några lasrar ska du se till att du förstår riskerna och noggrant gå igenom kapitlet [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Översikt över programvaran

### Säkerhetsavstängning

När du kör lasrar måste du alltid ha en **fysisk nödstoppsknapp** nära till hands (se [emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md "mention")). Om du vill disarma allt utan samma brådska kan du använda knappen _**DISARM ALL**_, eller `Escape`-tangenten (eller _**SESSION**_-tangenten på APC40). Du kan också minska den globala ljusstyrkan med reglaget på skärmen eller huvudfadern på APC40.

### Reglage

I Liberation finns olika reglage och kontroller.

{% hint style="info" %}
`Cmd / Ctrl`-klicka på ett reglage för att skriva in ett nytt värde om du behöver mer exakt kontroll än reglaget ger.
{% endhint %}

### Kortkommandon

En komplett lista över kortkommandon finns här: [keyboard-shortcuts.md](../reference/keyboard-shortcuts.md "mention")

### Skärmlayout

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Osäker på vad en viss knapp gör? Håll muspekaren över den så får du en beskrivning!
{% endhint %}

#### Meny

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

I menyn hittar du alla alternativ för filimport och filexport, samt paneler som kan öppnas. Här hittar du också alternativet för att auktorisera datorn med din prenumeration (i _Liberation -> Authorise/Deauthorise this computer_).

#### Ikonrad

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Här finns vanliga funktioner, till exempel att arma/disarma alla lasrar, global ljusstyrka, testmönster och växling mellan vyerna 3D, Canvas och Output.

### Vyer

Det stora området längst upp till vänster på skärmen kan visa en av tre huvudvyer: **3D**, **CANVAS** och **OUTPUT.** Växla mellan dem med knapparna i ikonraden (eller använd `Tab`-tangenten för att växla mellan vyerna 3D och OUTPUT, och fortsätt sedan tabba igenom varje laserutgång i tur och ordning).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D-vy

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D-vyn visar hur dina lasrar kommer att se ut och kan konfigureras så att den matchar din egen laseruppsättning. Klicka och dra för att rotera kameran, och använd mushjulet för att förflytta dig framåt och bakåt. Du hittar många fler alternativ i panelen _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Se [3d-visualiser.md](../setting-up/3d-visualiser.md "mention").

#### Output-vy

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output-vyn används för att konfigurera zoner och masker för varje laser. (Observera den stora siffran i övre vänstra hörnet, så att du enkelt ser vilken laser du arbetar med!)

Den här vyn är en representation av hela utgången för den här lasern, och var varje zon ligger inom den. Som standard finns det bara en zon per laser, men du kan lägga till så många zoner som är rimligt praktiskt, och du ser dem alla i den här vyn.

{% hint style="info" %}
**Vad är en zon?**

En zon är ett område inom en lasers utgång dit du kan styra laserinnehåll. Du kan ha mer än en zon per laser. Den enklaste typen av zon är en _beam_-zon, men det finns också _canvas_-zoner och _DMX_-zoner. I den här guiden fokuserar vi mest på beam-zoner, som vanligtvis används för att skapa atmosfäriska stråleffekter i luften.
{% endhint %}

Du kan välja vilken laser du vill redigera med något av följande:

* de numrerade knapparna i raden högst upp
* tryck på siffertangenten för den laser du vill välja _(1-9_-tangenter\_)\_
* `Tab`-tangenten för att bläddra från en laser till nästa

Lägg till en ny laser i uppsättningen genom att trycka på knappen _+_. (Det finns också en _ADD LASER_-knapp i panelen _Laser Overview_)

Ta bort en laser från uppsättningen genom att trycka på den röda ⊖-knappen i panelen _Laser Overview_.

Du kan zooma in och ut med musens rullhjul, och klicka och dra var som helst där det inte finns en zon för att flytta vyn.

Klicka på en zon för att markera den och justera sedan dess hörnpunkter med musen. Använd `Alt / Option`-tangenten medan du drar i ett hörn för att göra justeringen icke-uniform. Högerklicka på zonen för att se fler alternativ, inklusive att ändra zontyp.

Till vänster finns en rad med ikonknappar. Håll muspekaren över valfri knapp för att få en beskrivning av vad den gör. Knapparna här låter dig lägga till beam-zoner, canvas-zoner och masker. Det finns också alternativ för att ange ett testmönster enbart för den här lasern, samt inställningar för rutnät och snäppning.

Mer information finns i [output-view](../output-view/ "mention").

#### Canvas

Canvas-systemet används främst för grafik och arkitektonisk mapping. Du kan fördela komplexa bilder över flera lasrar och perspektivkorrigera varje sektion. Se [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention").

### APC40 MIDI-kontroller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Det går att styra Liberation med mus och tangentbord, men det är mycket bättre att använda ett APC40 MIDI-kontrollgränssnitt (Mark 2 är bäst, men Mark 1 fungerar också).

Se även: [apc40-reference.md](../reference/apc40-reference.md "mention")

Vi har nu också implementerat stöd för APC Mini Mark 2 och MIDI Fighter Twister, och fler är under utveckling. Men APC40 Mark 2 är det bästa alternativet i de flesta fall.&#x20;

### Clips och effekter

{% hint style="info" %}
**Vad är ett clip?**

Ett clip är en behållare för laserinnehåll i Liberation. Clips kan innehålla strålar eller grafiska animationer, och de är vanligtvis en loopande cykel. De kan styras till valfri zon (eller _Canvas target area_) och triggas med clip-knapparna i clip deck.
{% endhint %}

#### Översikt över clip deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Det här rutnätet kallas _clip deck_ och det är där alla laser-clips lagras. Det är utformat för att mappa direkt till knappmatrisen 8 x 5 på din APC40.

**Navigera i clip deck.**

Du kan rulla clip deck åt vänster och höger med:

* Vänster- och högerpiltangenterna. Lägg till `Cmd / Ctrl` för att rulla en hel sida i taget.
* Styrplatta: svep
* Mus: om din mus har sidledes rullning kan du använda den när muspekaren är över clip deck
* APC40 scroll knob
* APC40 _<- DEVICE ->_-knappar

För att hjälpa dig att orientera dig finns en minivisualisering av clip deck längst upp. Se även [clips](../clips/ "mention")

#### Starta och stoppa clips

Tryck på en clip-knapp (antingen med musen eller med APC40) för att starta ett clip. Tryck på den igen för att stoppa det. När du startar ett clip stoppas alla andra clips med samma färg automatiskt, om du inte håller ned _shift_.

Vissa clips är i _Flash mode_ (som standard de röda), och då stoppas de så snart du släpper clip-knappen.

Knappen _STOP_ stoppar alla clips som körs för tillfället.

#### Ange output-zoner för clipet

Under clip-knapparna ser du zonknapparna, som standard beam-zoner 1 till 8 (_BEAM 1_, _BEAM 2_ osv.). Zonknapparna lyser för att visa vilka zoner som är tilldelade det clip som är markerat just nu.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Två rader under zonknapparna ser du X/Y flip-knapparna. Växla dessa för att spegelvända clipet horisontellt och vertikalt.

{% hint style="info" %}
Observera att dessa zontilldelningar och X/Y flip-inställningar är kopplade till själva clipet. De sparas till nästa gång du kör det clipet. De är inte en global inställning.
{% endhint %}

Högerklicka på ett clip för att redigera fler inställningar för clipet. Se även [clip-settings.md](../clips/clip-settings.md "mention")

### Grupper

Du märker att varje clip har en färgad kontur, och den färgen visar vilken _grupp_ det tillhör. Clip-knapparna på APC40 lyser också i den färgen.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyan</td></tr><tr><td>Group 2</td><td>Orange</td></tr><tr><td>Group 3</td><td>Röd</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Grön</td></tr></tbody></table>

Gruppsystemet är mycket flexibelt och gör att du kan:

* Låta clips i en grupp fortsätta spela medan du växlar grupper i en annan
* Snabbt tilldela zoner och X/Y flips till alla clips i en grupp
* Ställa in _Flash mode_ för ett clip (Group 3 är inställd på _Flash mode_ som standard)

Grupper har också inställningar för in- och uttoning som kan ärvas av deras clips, eller åsidosättas.

Du kan tilldela clipets grupp med knapparna i högerklicksmenyn, eller med APC40 genom att trycka på gruppknappen och, _medan den fortfarande hålls ned,_ trycka på clip-knapparna.

Ändra zoninställningar för alla clips i en grupp

Med APC40 trycker du på gruppknappen och använder sedan, _medan den fortfarande hålls ned,_ zon- och X/Y-knapparna för att växla zoninställningar för alla clips i den gruppen.

Se även [groups.md](../clips/groups.md "mention")

### Effekter

Effektsystemet i Liberation är ett kraftfullt och mångsidigt sätt att ändra clip-output i realtid. Standardknapparna för effekter 1–8 finns under zonknapparna.

#### Använda en effekt

Tryck på en effektknapp för att slå på eller av effekten, eller ännu bättre: använd APC40-reglagen 1–8 för att tona effekter in och ut.

#### Effektparametrar

Använd rotary controllers 1–8\* för att justera _parameter_ för varje effekt. (Du kan också högerklicka med musen för att justera nivå och parameter). Parameterändringen gör olika saker beroende på hur effekten är konfigurerad. Se listan nedan för standardeffekterna.

{% hint style="info" %}
De små siffrorna du ser på effektknapparna avser effektens _level_ och _parameter_. _Level_ styrs av fadern på APC40, eller så kan du klicka och dra på knappen. Parametern justeras med rotary controllers på APC40, eller så kan du högerklicka för att justera med musen.
{% endhint %}

_\*Rotary controllers 1–8 sitter längst upp på en APC40 Mk2 och uppe till höger på Mk1. Se även:_ [apc40-reference.md](../reference/apc40-reference.md "mention")

#### Standardeffekterna

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Lägger till en kaotisk rörelse på clipets output. Parametern justerar mängden/hastigheten på kaoset.
2. **Sine wave** :\
   Förvränger allt innehåll över en rörlig sinusvåg. Parametern justerar våglängden.
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

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Det finns ytterligare 16 färgeffekter längs den nedersta raden för att använda förinställda värden för nyans och mättnad.

Observera att detta är standardeffekterna, men de kan redigeras så att de gör nästan vad du vill!

#### Vad är det _"currently selected clip"_?

När du startar ett clip lyser det upp för att visa att det är aktivt. Det har också en vit kontur runt sig som visar att det är det clip som är _markerat_ just nu. När du växlar zonknappar eller justerar clip-inställningarna tillämpas dessa på det _currently selected clip._

{% hint style="info" %}
För att välja ett clip utan att trigga det, tryck på `Alt / Option`-tangenten innan du trycker på clip-knappen. Det är ett bra sätt att justera dess zoner och andra inställningar utan att köra det.
{% endhint %}

### Panelen Clip Settings

Använd panelen _Clip Settings_ för att redigera skalning, X/Y-position och komma åt det kraftfulla systemet för zonfördröjning.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panelen Global Settings

Öppna panelen _Global Settings_ för att justera globala output-inställningar som påverkar all output över alla zoner.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Slå på AUTO RESET för att automatiskt återställa alla _Global settings_ när inga clips spelas.&#x20;

### Timing

Nästan alla laservisningar har någon form av musikaliskt soundtrack, så timingsystemet i Liberation bygger på ett tempo i slag per minut. I _Tempo Panel_ kan du se en representation av tiden. Varje ruta motsvarar ett slag och du kan se dem blinka i takt.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Det finns flera synkroniseringsalternativ, inklusive MIDI clock och Ableton Link. Om du känner till musikens tempo kan du justera det manuellt med reglaget på skärmen eller APC40 Tempo-ratten, men du kan också hålla takten med musiken med hjälp av _Tap Tempo_-systemet\_.\_

#### Tap Tempo

_Tap Tempo_ är ett begrepp som ofta används i musikappar, och det låter dig knacka i takt med beatet för att ange tempot medan musiken spelas. Du kan använda knappen på skärmen, men det rekommenderas att använda _T_-tangenten eller _Tap Tempo_-knappen på APC40 (eller till och med en fotpedal om du föredrar det).

Tryck på _R_-tangenten eller knappen _Metronome_ (APC40) för att återställa tempot till början av takten.

Tryck på _Y_-tangenten eller vrid på _Tempo_-ratten (APC40) för att avrunda tempot till ett heltal. Det kan vara användbart för elektronisk musik, som ofta har ett jämnt antal slag per minut.

### Organisera ditt clip deck

För att flytta ett clip på ditt clip deck klickar du och drar det till en ny position. Medan du drar kan du använda piltangenterna (eller rullhjulet/knapparna på din APC40) för att rulla åt vänster och höger.

Tryck på `Alt / Option`-tangenten medan du drar för att skapa en kopia.

`Alt / Option`-klicka på ett clip för att välja det utan att starta det.

`Alt / Option + Shift`-klicka på ett clip för att flermarkera, eller klicka och dra utanför ett clip för att markera med "lasso".&#x20;

Klicka och dra drar ALLA markerade clips.

För att ta bort ett eller flera clips kan du antingen dra dem bort från clip deck (en papperskorgsikon visas) eller använda knappen DELETE i clipets högerklicksmeny.

### Panelen Laser overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panelen _Laser overview panel_ ger dig en snabb överblick över statusen för de lasrar som körs just nu. Den gröna rutan till höger visar att laserkontrollern mår bra. Om den blir orange har du tillfälliga bortfall, och om den blir röd har den kopplats från. Om den är grå är den inte ansluten till någon kontroller alls.&#x20;

Grafen i mitten visar historiken för bildrutornas längd, och siffran till höger är aktuell bildfrekvens. Ju mer komplicerat innehållet är, desto lägre blir bildfrekvensen (dvs. mer flimmer). Allt under ungefär 25 fps börjar se lite flimrigt ut.&#x20;

### Ansluta till lasrar – panelen Controller Assignment

Klicka på knappen _Assign Laser Controllers_ för att öppna panelen _Controller Assignment_. (Den här panelen kan också nås via _View -> Controller Assignment_ i menyraden).

Här kan du välja vilka laserutgångar som ska gå till vilka laserkontrollers. Dra och släpp kontrollers från listan till höger till platserna till vänster. Du kan byta namn på dina kontrollers så att de matchar den laser de är kopplade till (använd pennikonen).

Läs kapitlet [controller-assignment.md](../setting-up/controller-assignment.md "mention") för mer information.

{% hint style="danger" %}
Innan du armar några lasrar ska du gå igenom kapitlet [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Panelen Laser output

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Den här panelen visar inställningarna för den _currently selected laser_ (representerad av siffran högst upp). Ändra vilken laser som är markerad genom att använda _tab_-tangenten, trycka på en siffertangent, klicka på ett lasernummer i panelen _Laser Overview_ eller i _output view._

* **Number button** armar och disarmar lasern. Om den är röd är lasern armad.
* **Brightness** justerar laserns ljusstyrka oberoende av de andra lasrarna (och kombineras med inställningen _global brightness_ – dvs. om båda är på 50 % blir din laser 25 %).
* **Test Pattern** slår på ett testmönster endast för den här lasern (åsidosätter den globala testmönsterinställningen)
* **Orientation** korrigerar för lasrar som är riggade på sidan eller upp och ned.
* **Flip Horizontal and Flip Vertical** vänder laserns output. Användbart för output-korrigering på lasrar med inkonsekvent kabeldragning.
* **Copy Laser Settings** öppnar en panel där du kan kopiera olika inställningar från den här lasern till andra.

### Scanner-inställningar

Displaylasrar fungerar genom att flytta en enda laserstråle extremt snabbt och slå på och av den för att rita former i luften. Det du ser som linjer, former och bilder är i själva verket strålen som spårar banor snabbare än dina ögon hinner uppfatta.

En punktström är den data som talar om för lasern vart den ska flytta sig härnäst och när strålen ska vara på eller av. I Liberation konverteras clips till den här punktströmmen i realtid när de skickas till lasrarna.

Liberation ger dig detaljerad kontroll över hur den här punktströmmen genereras, så att du kan balansera mjukhet, ljusstyrka och prestanda för varje laser.

{% hint style="info" %}
Om du är van vid äldre laserprogramvara som bygger på förberäknade punktströmmar kan det här arbetssättet kännas annorlunda i början. Punktgenerering i realtid gör dock att samma innehåll kan optimeras på olika sätt för varje laser. Det gör det lättare att arbeta med flera lasrar som har olika scannerhastigheter eller kvalitet, utan att duplicera eller bygga om innehåll. Det håller också clip-filerna mycket små, vilket är anledningen till att hela standarduppsättningen i Liberation clip deck bara är några få megabyte i stället för gigabyte.
{% endhint %}

De grundläggande scanner-inställningarna är:

* **Speed** är scannerhastigheten, dvs. hur snabbt lasern rör sig runt för att rita former. Detta motsvarar att justera punktfrekvensen i traditionell laserprogramvara, men i Liberation kan du ändra hur snabbt lasern rör sig _oberoende av punktfrekvensen._ Du bör inte behöva justera detta.
* **Scanner sync** (kallas ibland _blank shift, tidigare Colour Shift_) Scannrarna flyttar lasern mycket snabbt, men oftast är förändringen av ljusstyrka och färg inte synkroniserad med rörelsen. Det visar sig som små flimrande "svansar" av ljus i kanten på strålar och linjer. Använd den här justeringen för att få rörelse och färg att synka med varandra. Se [laser-settings](../setting-up/laser-settings/ "mention")

De andra avancerade scanner-inställningarna beskrivs i kapitlet [advanced](../advanced/ "mention").

### Zoning

En komplett guide till att konfigurera och zonavgränsa lasrar finns här: [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention")
