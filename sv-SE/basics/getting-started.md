# ✅ Snabbstartsguide

## Introduktion

Välkommen till **Liberation** – nästa generations programvara för lasershower.

Liberation är en kraftfull och avancerad modern programvara. Den bygger på grundläggande principer för användbarhet och tillförlitlighet, så att du får frihet att uttrycka din kreativitet. Den är snabb, effektiv och smidig. Följ den här _snabbstartsguiden_ så kommer du igång på nolltid!

### Hantera lasrar

Liberation är tillräckligt flexibelt för att du ska kunna konfigurera lasrar och visualisera dem utan att några fysiska lasrar är anslutna. När du sedan är redo kan du smidigt tilldela varje output till en laser controller.

{% hint style="info" %}
Du kan konfigurera och visualisera så många lasrar du vill i Liberation. Licensnivåerna (Hobbyist, Pro osv.) begränsar bara hur många lasrar du kan _arm._ Det betyder att du kan designa lasershower med 100 lasrar även med en gratislicens. Du behöver bara uppgradera när du faktiskt ska köra showen på riktiga lasrar.
{% endhint %}

Som standard finns 8 lasrar utspridda horisontellt, men du kan anpassa detta precis som du vill. Det är förmodligen bäst att behålla standardinställningen medan du lär känna programmet, och senare justera den så att den matchar din hårdvaruuppsättning. (Se [Konfigurera ditt projekt](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Viktigt: Innan du sätter några lasrar i _armed_-läge måste du förstå riskerna och noggrant gå igenom kapitlet [Konfigurera lasrar](../setting-up/setting-up-lasers.md).
{% endhint %}

## Översikt över programvaran

### Säkerhetsavstängning

När du kör lasrar måste du alltid ha en **fysisk nödstoppknapp** till hands (se [Nödstopp och interlocks](../hardware/emergency-stop-interlocks.md)). Om du vill disarm allt utan samma akuta behov kan du använda knappen _**DISARM ALL**_, tangenten `Escape` eller tangenten _**SESSION**_ på APC40. Du kan också sänka Global Brightness med reglaget på skärmen eller huvudfadern på APC40.

### Reglage

I Liberation finns olika reglage och kontroller.

{% hint style="info" %}
`Cmd / Ctrl`-klicka på ett reglage för att skriva in ett nytt värde om du behöver mer precision än reglaget ger.
{% endhint %}

### Kortkommandon

En fullständig lista över kortkommandon finns här: [Kortkommandon](../reference/keyboard-shortcuts.md)

### Skärmlayout

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Osäker på vad en viss knapp gör? Håll muspekaren över den för att visa en beskrivning!
{% endhint %}

#### Meny

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

I menyn hittar du alla alternativ för import och export av filer, samt öppnar paneler. Här hittar du också alternativet för att auktorisera datorn med din prenumeration (i _Liberation -> Authorise/Deauthorise this computer_).

#### Ikonrad

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Här finns vanliga uppgifter, till exempel att sätta alla lasrar i _armed_- eller _disarmed_-läge, Global Brightness, test pattern och växling mellan 3D view, Canvas view och Output view.

### Vyer

Det stora området längst upp till vänster på skärmen kan visa en av tre huvudvyer: **3D**, **CANVAS** och **OUTPUT.** Växla mellan dem med knapparna i ikonraden, eller använd tangenten `Tab` för att växla mellan 3D och Output view och fortsätt sedan att tabba genom varje laser-output i tur och ordning.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view visar hur dina lasrar kommer att se ut och kan konfigureras så att den matchar din egen laseruppsättning. Klicka och dra för att rotera kameran, och använd mushjulet för att röra dig framåt och bakåt. Du hittar många fler alternativ i panelen _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Se [3D Visualiser](../setting-up/3d-visualiser.md).

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view används för att konfigurera zones och masks för varje laser. (Lägg märke till det stora numret i övre vänstra hörnet, så att du lätt ser vilken laser du arbetar med!)

Den här vyn representerar hela output från den här lasern och visar var varje zone ligger inom den. Som standard finns bara en zone per laser, men du kan lägga till så många zones som är rimligt praktiskt, och du ser dem alla i den här vyn.

{% hint style="info" %}
**Vad är en zone?**

En zone är ett område inom en lasers output dit du kan skicka laserinnehåll. Du kan ha fler än en zone per laser. Den enklaste typen av zone är en _beam_ zone, men det finns också _canvas_ zones och _DMX_ zones. I den här guiden fokuserar vi främst på beam zones, som vanligtvis används för att skapa atmosfäriska stråleffekter genom luften.
{% endhint %}

Du kan välja vilken laser du vill redigera på något av följande sätt:

* de numrerade knapparna i raden längst upp
* tryck på siffertangenten för den laser du vill välja _(tangenterna 1-9\_)\_
* tangenten `Tab` för att gå från en laser till nästa

Lägg till en ny laser i uppsättningen genom att trycka på knappen _+_. (Det finns också en knapp _ADD LASER_ i panelen _Laser Overview_.)

Ta bort en laser från uppsättningen genom att trycka på den röda knappen ⊖ i panelen _Laser Overview_.

Du kan zooma in och ut med mushjulet, och klicka och dra där det inte finns någon zone för att flytta vyn.

Klicka på en zone för att välja den och justera sedan hörnpunkterna med musen. Håll ned `Alt / Option` medan du drar i ett hörn för att göra ändringen icke-uniform. Högerklicka på zone för att se fler alternativ, inklusive att ändra typ av zone.

Till vänster finns en rad med ikonknappar. Håll muspekaren över en knapp för att visa en beskrivning av vad den gör. Knapparna här låter dig lägga till beam zones, canvas zones och masks. Det finns också alternativ för att ställa in ett test pattern endast för den här lasern, samt inställningar för rutnät och snapping.

Mer information finns i [Output view](../output-view/).

#### Canvas

Canvas-systemet används främst för grafik och arkitektonisk mapping. Du kan fördela komplexa bilder över flera lasrar och perspektivkorrigera varje del. Se [Grafik och Canvas-systemet](../graphics-and-the-canvas-system/).

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Även om det går att styra Liberation med mus och tangentbord är det mycket bättre att använda ett APC40 MIDI-kontrollinterface (Mark 2 är bäst, men Mark 1 fungerar också).

Se även: [APC40-referens](../reference/apc40-reference.md)

Vi har nu också lagt till stöd för APC Mini Mark 2 och MIDI Fighter Twister, och fler är under utveckling. APC40 Mark 2 är dock det bästa alternativet i de flesta fall.&#x20;

### Clips och effekter

{% hint style="info" %}
**Vad är en clip?**

En clip är en behållare för laserinnehåll i Liberation. Clips kan innehålla beams eller grafiska animationer och är vanligtvis en loopande sekvens. De kan riktas till valfri zone eller _Canvas target area_ och triggas med clip-knapparna i Clip Deck.
{% endhint %}

#### Översikt över Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Det här rutnätet kallas _Clip Deck_ och det är här alla laser-Clips lagras. Det är utformat för att mappa direkt mot rutnätet med 8 x 5 knappar på din APC40.

**Navigera i Clip Deck.**

Du kan scrolla Clip Deck åt vänster och höger med:

* vänster- och högerpiltangenterna. Lägg till `Cmd / Ctrl` för att scrolla en hel sida åt gången.
* styrplatta: svep
* mus: om din mus har horisontell scroll kan du använda den när pekaren är över Clip Deck
* scrollratten på APC40
* knapparna _<- DEVICE ->_ på APC40

För att hjälpa dig att orientera dig finns en minivisualisering av Clip Deck längst upp. Se även [Clips](../clips/)

#### Starta och stoppa Clips

Tryck på en clip-knapp, antingen med musen eller med APC40, för att starta en Clip. Tryck igen för att stoppa den. När du startar en Clip stoppas alla andra Clips med samma färg automatiskt, om du inte håller ned _shift_.

Vissa Clips är i _Flash mode_ (som standard de röda), och då stoppas de så fort du släpper clip-knappen.

Knappen _STOP_ stoppar alla Clips som körs just nu.

#### Ställa in output zones för Clip

Under clip-knapparna ser du zone-knapparna, som standard beam zones 1 till 8 (_BEAM 1_, _BEAM 2_ osv.). Zone-knapparna lyser för att visa vilka zones som är tilldelade till den Clip som är vald just nu.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Två rader under zone-knapparna ser du X/Y flip-knapparna. Växla dem för att vända Clip horisontellt och vertikalt.

{% hint style="info" %}
Observera att dessa zone-tilldelningar och X/Y flip-inställningar är kopplade till själva Clip. De sparas till nästa gång du kör den Clip. De är inte en global inställning.
{% endhint %}

Högerklicka på en Clip för att redigera fler inställningar för den. Se även [Clip Settings](../clips/clip-settings.md)

### Groups

Du kommer att märka att varje Clip har en färgad kontur, och den färgen visar vilken _group_ den tillhör. Clip-knapparna på APC40 lyser också i den färgen.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyan</td></tr><tr><td>Group 2</td><td>Orange</td></tr><tr><td>Group 3</td><td>Röd</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Grön</td></tr></tbody></table>

Systemet med Groups är mycket flexibelt och låter dig:

* låta Clips i en group fortsätta, medan du växlar Groups i en annan
* snabbt tilldela zones och X/Y flips till alla Clips i en group
* ställa in _Flash mode_ för en Clip (Group 3 är inställd på _Flash mode_ som standard)

Groups har också inställningar för transition in/out som kan ärvas av Clips eller åsidosättas.

Du kan tilldela en Clip till en group med knapparna i högerklicksmenyn. Med APC40 kan du också trycka på group-knappen och, _medan den fortfarande hålls ned_, trycka på clip-knapparna.

Ändra zone-inställningar för alla Clips i en group

Med APC40: tryck på group-knappen och använd sedan, _medan den fortfarande hålls ned_, zone- och X/Y-knapparna för att växla zone-inställningar för alla Clips i den group.

Se även [Groups](../clips/groups.md)

### Effekter

Effektsystemet i Liberation är ett kraftfullt och flexibelt sätt att ändra Clip output i realtid. Standardknapparna för effekter 1–8 finns under zone-knapparna.

#### Använda en effekt

Tryck på en effektknapp för att slå på eller av effekten. Ännu bättre är att använda reglarna 1–8 på APC40 för att tona effekter in och ut.

#### Effektparametrar

Använd rotary controllers 1–8\* för att justera _parameter_ för varje effekt. (Du kan också högerklicka med musen för att justera level och parameter.) Parameterändringen gör olika saker beroende på hur effekten är konfigurerad. Se listan nedan för standardeffekterna.

{% hint style="info" %}
De små siffrorna du ser på effektknapparna avser effektens _level_ och _parameter_. _Level_ styrs med fadern på APC40, eller genom att klicka och dra på knappen. Parameter justeras med rattarna på APC40, eller genom att högerklicka och justera med musen.
{% endhint %}

_\*Rotary controllers 1–8 sitter längst upp på en APC40 Mk2 och längst upp till höger på Mk1. Se även:_ [APC40-referens](../reference/apc40-reference.md)

#### Standardeffekterna

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Lägger till en kaotisk rörelse på Clip output. Parametern justerar mängden/hastigheten på kaoset.
2. **Sine wave** :\
   Förvränger allt innehåll över en rörlig sinusvåg. Parametern justerar våglängden.
3. **Rotation** :\
   Snurrar allt runt. Parametern justerar rotationshastigheten.
4. **Horizontal flip** :\
   Trycker ihop och sträcker allt horisontellt. Parametern justerar hastigheten.
5. **Scale** :\
   Skalar upprepade gånger allt från fullt till noll. Parametern justerar hastigheten.
6. **Hue** :\
   Ändrar nyansen på allt, men ändrar inte mättnaden (dvs. allt som är vitt förblir vitt). Parametern justerar nyansen.
7. **Saturation and hue** :\
   Ändrar nyansen på allt och mättar också färgen helt (dvs. allt som är vitt ändras till färgen). Parametern justerar nyansen.
8. **Flash** :\
   Blinkar upprepade gånger ljusstyrkan för allt från fullt till noll. Parametern justerar blinkhastigheten.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Det finns ytterligare 16 färgeffekter längs den nedre raden, som använder förinställda värden för nyans och mättnad.

Observera att detta är standardeffekterna, men de kan redigeras så att de gör nästan vad du vill!

#### Vad är _det Clip som är valt just nu_?

När du startar en Clip lyser den för att visa att den är aktiv. Den har också en vit kontur runt sig, vilket visar att detta är det Clip som är valt just nu. När du växlar zone-knappar eller justerar clip-inställningar tillämpas de på _det Clip som är valt just nu_.

{% hint style="info" %}
För att välja en Clip utan att trigga den trycker du på `Alt / Option` innan du trycker på clip-knappen. Det är ett bra sätt att justera dess zones och andra inställningar utan att köra den.
{% endhint %}

### Panelen Clip Settings

Använd panelen _Clip Settings_ för att redigera skalning, X/Y-position och komma åt det kraftfulla systemet för zone delay.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panelen Global Settings

I panelen _Global Settings_ kan du justera globala output-inställningar som påverkar all output över alla zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Slå på AUTO RESET för att automatiskt återställa alla _Global settings_ när inga Clips spelas.&#x20;

### Timing

Nästan alla laserföreställningar har någon form av musikalisk ljudläggning, så timingsystemet i Liberation bygger på ett tempo i slag per minut. I _Tempo Panel_ kan du se en representation av tiden. Varje ruta motsvarar ett slag och du kan se rutorna blinka i takt.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Det finns flera synkroniseringsalternativ, inklusive MIDI clock och Ableton Link. Om du känner till musikens tempo kan du justera det manuellt med reglaget på skärmen eller Tempo-ratten på APC40, men du kan också hålla takten med musiken med _Tap Tempo_-systemet\_.\_

#### Tap Tempo

_Tap Tempo_ är en term som ofta används i musikappar. Den låter dig knacka in takten för att ställa in tempot medan musiken spelas. Du kan använda knappen på skärmen, men det rekommenderas att använda tangenten _T_ eller knappen _Tap Tempo_ på APC40, eller till och med en fotpedal om du föredrar det.

Tryck på tangenten _R_ eller knappen _Metronome_ (APC40) för att återställa tempot till början av takten.

Tryck på tangenten _Y_ eller vrid på _Tempo_-ratten (APC40) för att avrunda tempot till ett heltal. Det kan vara användbart för elektronisk musik, som ofta har ett helt antal slag per minut.

### Organisera ditt Clip Deck

För att flytta en Clip i Clip Deck klickar du på den och drar den till en ny position. Medan du drar kan du använda piltangenterna, eller scrollhjulet/knapparna på APC40, för att scrolla åt vänster och höger.

Håll ned `Alt / Option` medan du drar för att göra en kopia.

`Alt / Option`-klicka på en Clip för att välja den utan att starta den.

`Alt / Option + Shift`-klicka på en Clip för att välja flera, eller klicka och dra utanför en Clip för att välja med ”lasso”.&#x20;

Klicka och dra flyttar ALLA valda Clips.

För att ta bort en eller flera Clips kan du antingen dra dem bort från Clip Deck (en papperskorgsikon visas) eller använda knappen DELETE i högerklicksmenyn för Clip.

### Panelen Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panelen _Laser Overview_ ger dig en snabb överblick över statusen för de lasrar som körs just nu. Den gröna rutan till höger visar att laser controller fungerar som den ska. Om den blir orange har du tillfälliga avbrott, och om den blir röd har anslutningen brutits. Om den är grå är den inte ansluten till någon controller alls.&#x20;

Grafen i mitten visar historik över bildrutornas längd, och siffran till höger är den aktuella bildfrekvensen. Ju mer komplicerat innehållet är, desto lägre blir bildfrekvensen (dvs. mer flimmer). Allt under ungefär 25 fps börjar se lite flimrigt ut.&#x20;

### Ansluta till lasrar – panelen Controller Assignment

Klicka på knappen _Assign Laser Controllers_ för att öppna panelen _Controller Assignment_. (Den här panelen kan också öppnas via _View -> Controller Assignment_ i menyraden.)

Här kan du välja vilka laser-outputs som ska gå till vilka laser controllers. Dra och släpp controllers från listan till höger till platserna till vänster. Du kan byta namn på dina controllers så att de matchar vilken laser de är kopplade till (använd knappen med pennikonen).

Läs kapitlet [Controller Assignment](../setting-up/controller-assignment.md) för mer information.

{% hint style="danger" %}
Innan du sätter några lasrar i _armed_-läge måste du gå igenom kapitlet [Konfigurera lasrar](../setting-up/setting-up-lasers.md).
{% endhint %}

### Panelen Laser Settings

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Den här panelen visar inställningarna för den _currently selected laser_, som anges av numret längst upp. Ändra vilken laser som är vald med tangenten _tab_, genom att trycka på en siffertangent, klicka på ett lasernummer i panelen _Laser Overview_ eller i _output view._

* **Number button** sätter lasern i _armed_- eller _disarmed_-läge. Om den är röd är lasern _armed_.
* **Brightness** justerar laserns ljusstyrka oberoende av de andra lasrarna. Den kombineras med inställningen _global brightness_ – dvs. om båda står på 50 % blir din laser 25 %.
* **Test Pattern** slår på ett test pattern endast för den här lasern (åsidosätter den globala test pattern-inställningen)
* **Orientation** korrigerar för lasrar som är riggade på sidan eller upp och ned.
* **Flip Horizontal and Flip Vertical** vänder laserns output. Användbart för output-korrigering på lasrar med inkonsekvent kabeldragning.
* **Copy Laser Settings** öppnar en panel där du kan kopiera olika inställningar från den här lasern till andra.

### Scanner-inställningar

Displaylasrar fungerar genom att flytta en enda laserstråle extremt snabbt och slå på och av den för att rita former i luften. Det du ser som linjer, former och bilder är i själva verket strålen som följer banor snabbare än dina ögon hinner uppfatta.

En point stream är den data som talar om för lasern vart den ska flytta härnäst och när strålen ska vara på eller av. I Liberation omvandlas Clips till denna point stream i realtid när de skickas till lasrarna.

Liberation ger dig detaljerad kontroll över hur denna point stream genereras, så att du kan balansera jämnhet, ljusstyrka och prestanda för varje laser.

{% hint style="info" %}
Om du är van vid äldre laserprogramvara som bygger på förberäknade point streams kan detta arbetssätt kännas annorlunda i början. Men generering av punkter i realtid gör att samma innehåll kan optimeras olika för varje laser. Det gör det enklare att arbeta med flera lasrar som har olika scanner-hastigheter eller kvalitet, utan att duplicera eller bygga om innehåll. Det håller också clip-filer mycket små, vilket är anledningen till att hela standarduppsättningen i Liberation Clip Deck bara är några få megabyte i stället för gigabyte.
{% endhint %}

De grundläggande scanner-inställningarna är:

* **Speed** är scanner-hastigheten, dvs. hur snabbt lasern rör sig för att rita former. Det motsvarar att justera point rate i traditionell laserprogramvara, men i Liberation kan du ändra hur snabbt lasern rör sig _oberoende av point rate._ Du ska normalt inte behöva justera detta.
* **Scanner sync** (kallas ibland _blank shift_, tidigare Colour Shift) Scanners flyttar laserstrålen mycket snabbt, men förändringen av ljusstyrka och färg är vanligtvis inte synkroniserad med rörelsen. Det syns som små flimrande ”svansar” av ljus i kanten av beams och linjer. Använd den här justeringen för att få rörelse och färg i synk med varandra. Se [Laser Settings](../setting-up/laser-settings/)

De övriga avancerade scanner-inställningarna behandlas i kapitlet [Avancerat](../advanced/).

### Zoning

En fullständig guide till att konfigurera och skapa zones för lasrar finns här: [Konfigurera lasrar](../setting-up/setting-up-lasers.md)
