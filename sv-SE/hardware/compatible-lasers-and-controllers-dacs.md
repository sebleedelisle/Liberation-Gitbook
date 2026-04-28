---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Kompatibla lasrar och styrenheter (DAC:ar)

### Vilka lasrar är kompatibla med Liberation?

Om din laser har en standard ILDA-ingång kan du använda den med Liberation (tillsammans med en kompatibel laserstyrenhet som Ether Dream eller Helios DAC – [se hela listan nedan](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC – det billigaste alternativet för hemmabruk</p></figcaption></figure>

Du behöver ingen extern styrenhet eller ILDA-ingång om:

* Din laser har Ether Dream installerad internt, eller;
* Du har en LaserCube från Wicked Lasers, eller;
* Du har en X-Laser-armatur med inbyggd Mercury, eller;
* Du har en Laser Animation Sollinger-laser med inbyggd AVB-styrenhet (för närvarande under testning endast på macOS)

{% hint style="info" %}
**Vad är en laserstyrenhet?**

En laserstyrenhet (eller DAC) är en hårdvaruenhet som tar den digitala datan från Liberation och omvandlar den till de analoga signaler som krävs för att styra skannrarna och utmatningen från din laser. (Därav DAC: Digital to Analog Converter.)

Styrenheten ansluts till din dator via USB eller över ett vanligt datornätverk. Den kan antingen vara en extern enhet eller vara installerad inuti lasern.

Om den är extern ansluter du den till din laser via ILDA-anslutningen. ILDA är en branschstandard som använder en klassisk 25-polig D-kontakt. Skaffa en ILDA-kabel, anslut ena änden till styrenheten och den andra till lasern.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>ILDA-utgången på en extern Ether Dream</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Bakpanelen på en laser som visar de olika anslutningarna, inklusive ILDA-ingången</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>En standard ILDA-kabel</p></figcaption></figure>

### Vilken styrenhet passar mig bäst?

Om du är hemanvändare, eller kör mindre shower med högst 4 lasrar som står nära datorn, är USB-styrenheter som **Helios DAC** det **mest prisvärda** alternativet.

Nätverks-DAC:ar som **Ether Dream** är det **bästa alternativet för professionella** laseroperatörer som gärna sätter upp ett nätverk och vill köra ett stort antal lasrar. Alla större Liberation-shower hittills har körts med Ether Dreams.

Om du har en **LaserCube** behöver du ingen separat laserstyrenhet alls – Liberation är kompatibelt med alla LaserCubes. De tidigare modellerna ansluts med USB-kabel, och de nyare modellerna ansluts över ett nätverk.

Om du är professionell och vill ha det enklaste alternativet kan du överväga X-Laser-enheter med inbyggd Mercury eller Laser Animation Sollinger-lasrar som använder AVB.

### Kompatibla laserstyrenheter

#### Ether Dream (Network)

[Ether Dream](https://ether-dream.com) har funnits i över tio år och är för närvarande på version 4 (även om Liberation också fungerar med Ether Dream version 1, 2 och 3). De är extremt tillförlitliga.

Du ansluter till dem över ett vanligt nätverk. De kan köpas som fristående enheter, eller ännu bättre, monteras inuti lasrar.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) är det bästa alternativet för nybörjare och är billigare än Ether Dreams, men eftersom de ansluts via USB rekommenderas de inte för långa kabeldragningar. Du kan också få problem med USB-data och drivrutiner när du ansluter fler än 4 (särskilt på Windows).

Men om du bara vill köra ett par lasrar hemma är det det billigaste och enklaste alternativet.

#### Mercury (inbyggt i X-Laser-enheter)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) är X-Lasers kraftfulla DMX-baserade laserstyrsystem, utformat för ljusdesigners som vill köra lasrar direkt från ett traditionellt ljusbord. Med den senaste firmwareuppdateringen har Mercury även **Ether Dream-emulering**, vilket innebär att det nu fungerar sömlöst med Liberation – och med all annan programvara som stöder Ether Dream.

#### AVB (inbyggt i Laser Animation Sollinger-enheter)

**AVB** är ett öppet nätverksbaserat protokoll för högpresterande ljud- och dataströmning med låg latens. Många LaserAnimation Sollinger-projektorer har AVB-stöd direkt i hårdvaran, vilket gör att Liberation kan ansluta till dem över nätverket utan externa DAC:ar. AVB-stödet i Liberation är för närvarande **endast för macOS och under testning**, och det kräver **kompatibla nätverksenheter med AVB-stöd**. När det är korrekt konfigurerat ger det ett enklare arbetsflöde, färre externa enheter och hög driftsäkerhet för professionella shower.

#### Styrenheter som kommer att stödjas i framtiden:

* [IDN](http://www.ilda-digital.com) (ett öppet nätverksprotokoll från ILDA, kan implementeras av valfri tillverkare)

### Kabelrekommendationer

För bästa prestanda bör du hålla USB-DAC:ar nära datorn och ansluta dem till lasrarna med längre ILDA-kablar. (Var dock försiktig, eftersom ILDA-kablar kan fungera som en änterhake vid nedriggning!)

Om du använder Ether Dreams kan du fortfarande hålla dem samlade och ansluta till lasrarna med långa ILDA-kablar, eller så kan du rigga dem nära lasrarna och använda längre nätverkskablar.

Den idealiska lösningen är att ha Ether Dreams (eller andra styrenheter) installerade direkt inuti dina lasrar (Rob på Stanwax Laser kan göra detta åt dig i Storbritannien)
