---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Hårdvara

#### **Fungerar Liberation på Windows?**

Ja – Liberation har fullt stöd för **Windows 10 och 11 (64-bitars)**, med exakt samma funktioner som Mac-versionen. Varje version släpps samtidigt för båda plattformarna.

#### **Fungerar Liberation på Mac?**

Ja – Liberation har fullt stöd för **Mac (macOS 12 Monterey och senare)**, med samma funktioner som Windows-versionen. Alla uppdateringar släpps samtidigt.

#### **Vilken är den lägsta datorspecifikationen som krävs?**

Det beror på hur många lasrar du vill styra. Om du bara kör några få lasrar klarar du dig bra med en enklare dator. Alla Mac-datorer med Apple Silicon fungerar mycket bra och bör kunna styra upp till 100 lasrar. Om du kör komplexa shower med höga krav rekommenderar vi den bästa dator du har råd med.

#### **Hur många lasrar kan jag styra med Liberation?**

Liberation kan köra många lasrar från en dator. Det har testats med över 100 laserkontroller, så svaret beror på:

* datorns CPU
* nätverkshastigheten
* din prenumerationstyp

#### **Vilka MIDI-kontroller kan jag använda?**

Liberation är utformat och optimerat för den populära MIDI-kontrollern APC40 Mk2. Det fungerar även med APC40 Mk1. Se [live-control-with-the-apc40.md](midi-control/live-control-with-the-apc40.md "mention")

Vi lägger gradvis till fler MIDI-kontroller och har för närvarande även stöd för APC Mini Mk2 och MIDI Fighter Twister.

Det finns också systemet MIDI Send/Receive, som ger ytterligare MIDI-kontroll. Se [midi-send-receive.md](midi-control/midi-send-receive.md "mention")

Se [midi-control](midi-control/ "mention") för mer information.

#### **Kan jag använda det med vilken MIDI-kontroller som helst?**

Vi arbetar just nu med ett konfigurerbart MIDI-system som kommer att göra detta möjligt i framtiden. Under tiden har vissa användare lyckats använda en MIDI-tolk som kan omvandla valfria MIDI-meddelanden för systemet MIDI Send/Receive, men det är en pillig och avancerad process. Sök i [forumet](https://forum.liberationlaser.com) efter råd om den här konfigurationen, men i praktiken är APC40 det bästa alternativet.

## Laserkontroller

#### **Vilka laserkontroller är kompatibla med Liberation?**

* [Ether Dream (rekommenderas)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (du kan behöva uppdatera din firmware)
* LaserCube USB (och LaserDock)
* LaserCube network protocol (med trådbunden anslutning)
* AVB som används av [LASollinger lasers](https://laseranimation.com/en/) (för närvarande endast macOS, under testning)

Se [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention") för mer information

#### **Varför har ni inte stöd för laserkontroller från \[annat märke]?**

För att uppmuntra bättre interoperabilitet mellan mjukvara och hårdvara kommer Liberation endast att stödja DAC:er som har ett publicerat kommunikationsprotokoll. Jag anser att detta är den bästa vägen framåt för laserbranschen.

#### **Hur vet jag om min laser kan användas med Liberation?**

Om din laser har något av följande kan du använda den med Liberation:

* En extern **ILDA input** – en 25-polig D-kontakt som används med en kompatibel extern kontroller.
* En internt installerad **Ether Dream**.
* Valfri **LaserCube** (fungerar med både USB- och Wi‑Fi-LaserCube).
* En **X-Laser-enhet med inbyggt Mercury-system** (i Ether Dream-läge).
* En **LaserAnimation Sollinger-projektor med inbyggt AVB** (endast macOS, kräver AVB-kompatibla nätverksenheter, för närvarande under testning).

Se [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention") för mer information

#### **Kan jag använda Liberation med min LaserCube?**

Ja, Liberation fungerar direkt med valfri LaserCube. Se [lasercube.md](hardware/lasercube.md "mention")

## Licenser

#### **Vad kostar en licens?**

Se sidan [shop](https://liberationlaser.com/shop) för aktuella priser.

#### **Vilka begränsningar finns mellan licensnivåerna?**

Se sidan [shop](https://liberationlaser.com/shop) för aktuella licensalternativ.

Observera att du kan konfigurera, förhandsgranska och designa shower med hur många lasrar du vill på **alla** nivåer, även den kostnadsfria, och det finns inga andra begränsningar alls förutom antalet lasrar som du kan _arm_. Alla andra funktioner i Liberation är tillgängliga för alla.

#### **Kan jag uppgradera till en ny nivå?**

Du kan uppgradera till en högre nivå när som helst. Du får en delvis återbetalning för den återstående tiden på din nuvarande licens, och din nya plan startar direkt. Se [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **Kan jag nedgradera min licens?**

Du kan nedgradera när som helst, men ändringen träder i kraft i slutet av din nuvarande licensperiod. Se [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **Hur auktoriserar jag min dator med min licens?**

När du har köpt en licens kan du auktorisera datorn direkt i Liberation-programmet. Du ser knappen _Authorise_ på skärmen _About_, som uppmanar dig att logga in på webbplatsen. Följ instruktionerna på skärmen för att slutföra auktoriseringen. Se [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **Hur ofta behöver jag ansluta datorn till internet?**

Varje gång licensen förnyas behöver du ansluta Liberation till internet för att uppdatera dess interna licens. För en månadsvis återkommande betalning behöver du ansluta varje månad.

#### **Vad händer om jag inte kan ansluta datorn till internet efter förnyelse?**

Liberation ger dig en respitperiod på 7 dagar efter att licensen har förnyats för att ansluta till internet och uppdatera dess interna licens. Efter den perioden går Liberation tillbaka till _Free_-läge.

#### **Vad händer om mitt kreditkort går ut?**

Du får en e-postavisering från vår betalningsleverantör, och du behöver uppdatera dina betalningsuppgifter. Logga in på webbplatsen och använd länken _Update payment details_ på prenumerationssidan.

#### **Hur säger jag upp min återkommande licens?**

Logga in på webbplatsen, öppna sidan _Your subscriptions_, välj prenumerationen du vill säga upp och klicka sedan på länken _Cancel Subscription_. Du kan fortsätta använda Liberation under resten av licensperioden.

#### **Hur många datorer kan jag installera Liberation på?**

Du kan installera Liberation på hur många datorer du vill. Licensauktorisering krävs bara för att aktivera laser-/DMX-output, och din licensnivå avgör hur många datorer som kan auktoriseras för output samtidigt. Se [how-licensing-works.md](installation/how-licensing-works.md "mention")

#### **Hur flyttar jag min licens från en dator till en annan?**

* Öppna Liberation på datorn du inte längre vill använda
* Kontrollera att du är ansluten till internet och klicka på knappen _De-authorise this computer_ på skärmen _About_
* Öppna nu Liberation på den nya datorn
* Klicka på knappen _Authorise this computer_ på skärmen _About_.
* Webbplatsen öppnas. Logga in och följ instruktionerna på skärmen för att slutföra auktoriseringen

Du kan också fjärravauktorisera en dator som du inte längre har åtkomst till (med vissa begränsningar). Se [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **Kan jag avauktorisera Liberation på en dator som har försvunnit eller blivit stulen?**

Du kan avauktorisera datorn via webbplatsen. Om Liberation-installationen inte har varit online sedan din senaste förnyelse kan detta göras direkt.

Om inte, träder avauktoriseringen i kraft när prenumerationen förnyas eller när datorn ansluter till internet, beroende på vilket som sker först. Om du snabbt behöver auktorisera en ny dator igen, kontakta supporten.

### Använda Liberation

#### Standardkonfigurationen har 8 lasrar – hur ändrar jag detta?

Se [setting-up-your-project.md](setting-up/setting-up-your-project.md "mention") och [adding-removing-lasers.md](setting-up/adding-removing-lasers.md "mention")

#### Kan jag kopiera zoninställningar från en laser till de andra?

Ja! Se [copy-zones-between-lasers.md](output-view/copy-zones-between-lasers.md "mention")

#### Kan jag skriva in ett tal i stället för att använda ett reglage?

Ja. `Cmd / Ctrl`-klicka på reglaget så kan du ange värdet med tangentbordet.

#### **Hur synkar jag Liberation till musik?**

Det har ett intelligent "tap tempo"-system som fungerar som du förväntar dig, men du kan också använda en extern MIDI-klocka eller Ableton Link. Se [tempo-synchronisation.md](tempo-synchronisation.md "mention"). Tidslinjen kan synkas till inkommande LTC/SMPTE-tidskod via valfritt ljudinterface. Se [timecode.md](timecode.md "mention").

#### Vilka inställningar behöver jag justera för att få bästa output från lasern?

Den viktigaste inställningen är _Colour Shift_, som kompenserar för den lilla fördröjningen mellan att speglarna rör sig och att lasrarna ändrar ljusstyrka. Om dina laserpunkter/-strålar har små "svansar" behöver du justera detta. (Se bilderna på sidan [laser-settings.md](setting-up/laser-settings.md "mention") för ett exempel på "svansar")

Du kan också prova att ändra scannerhastigheten: långsammare om dina scanners är enklare, eller snabbare om de är bra. Men **var försiktig, eftersom du kan skada dina scanners om du driver dem för hårt.**

Det finns också några förinställda scannerinställningar. Standardalternativet är konservativt och fungerar bra för de flesta laserstrålebehov. Men det finns andra förinställningar om du har bättre scanners, och det finns förinställningar som är anpassade för grafik.

För mer information, se [laser-settings.md](setting-up/laser-settings.md "mention"), och för information om hur du skapar egna förinställningar, se [scanner-presets.md](advanced/scanner-presets.md "mention") (avancerat, under arbete)

Du kan också korrigera färgbalansen med inställningarna _Colour calibration_. Se [colour-calibration.md](advanced/colour-calibration.md "mention") (avancerad teknik)

#### Vad gör inställningen _Latency(ms)_?

Detta är bildrutelatensen, eller den maximala tiden mellan att en bildruta genereras och sedan skickas till en laser. Du ska normalt inte behöva justera den, men om du har nätverksproblem kan du prova att öka den. Se [latency-setting.md](setting-up/latency-setting.md "mention") för mer information.

### Clips

#### Hur justerar jag zoner och inställningar för en Clip utan att köra den?

`Alt / Option`-klicka för att göra den till _currently selected clip_ utan att aktivera den. Se även [starting-stopping-clips.md](clips/starting-stopping-clips.md "mention")

#### Hur kopierar jag Clips?

Klicka och dra medan du håller ned tangenten `Alt / Option`. Se även [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### Hur tar jag bort Clips?

Klicka och dra dem bort från Clip Deck. Se även [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### Hur markerar jag flera, tar bort, kombinerar Clip Decks osv.?

Se [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### Vad betyder den lilla mikrofonsymbolen och andra ikoner på Clip-knappen?

De visar att en Clip tar emot ljud- eller MIDI-input, och de tre punkterna visar att det finns en zonfördröjning. Se [what-are-the-small-icons-on-the-clip-buttons.md](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
