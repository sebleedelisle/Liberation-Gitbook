---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Česta pitanja

## Hardver

#### **Radi li Liberation na Windowsu?**

Da - Liberation u potpunosti podržava **Windows 10 i 11 (64-bit)**, s potpuno istim značajkama kao verzija za Mac. Svako izdanje objavljuje se istovremeno za obje platforme.

#### **Radi li Liberation na Macu**

Da - Liberation u potpunosti podržava **Mac (macOS 12 Monterey i noviji)**, s potpunom usklađenošću značajki s verzijom za Windows. Sva ažuriranja objavljuju se zajedno.

#### **Koje su minimalne specifikacije računala?**

Ovisi o tome koliko lasera želite kontrolirati. Ako koristite samo nekoliko lasera, bit će dovoljno računalo skromnijih specifikacija. Svaki Apple Silicon Mac radi vrlo dobro i trebao bi moći kontrolirati do 100 lasera. Ako izvodite složene predstave u kojima je pouzdanost kritična, preporučujemo najbolje računalo koje si možete priuštiti.

#### **Koliko lasera mogu kontrolirati s Liberation?**

Liberation može pokretati vrlo velik broj lasera na jednom računalu; testiran je s više od 100 lasera, pa odgovor ovisi o:

* procesoru vašeg računala
* brzini mreže
* razini vaše licence

#### **Koje MIDI kontrolere mogu koristiti?**

Liberation je dizajniran i optimiziran oko popularnog MIDI kontrolera APC40 Mk2. Radi i s APC40 Mk1. Pogledajte [Live MIDI kontroleri](midi-control/live-control-with-the-apc40.md)

Liberation podržava i APC Mini te MIDI Fighter Twister. APC40 Mk2 i dalje je najpotpuniji referentni kontroler.

Tu je i sustav MIDI Send/Receive koji omogućuje dodatnu MIDI kontrolu. Pogledajte [MIDI Send/Receive](midi-control/midi-send-receive.md)

Za više informacija pogledajte [MIDI kontrola](midi-control/).

#### **Mogu li ga koristiti s bilo kojim MIDI kontrolerom?**

Za druge kontrolere upotrijebite sustav MIDI Send/Receive ili MIDI prevoditelj koji može slati zadane MIDI poruke za Liberation. Potražite savjete za takvo postavljanje na [forumu](https://forum.liberationlaser.com), ali realno je APC40 Mk2 i dalje najbolja opcija za većinu live predstava.

## Laserski kontroleri

#### **Koji su laserski kontroleri kompatibilni s Liberation?**

* [Ether Dream (preporučeno)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (možda ćete morati ažurirati firmware)
* LaserCube USB (i LaserDock)
* LaserCube mrežni protokol (putem žične veze)
* AVB kakav koriste [LASollinger laseri](https://laseranimation.com/en/) (trenutačno samo macOS, u testiranju)

Za više informacija pogledajte [Kompatibilni laseri i kontroleri (DAC-ovi)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Zašto ne podržavate laserski kontroler \[druge marke]?**

Kako bi se potaknula veća interoperabilnost između softvera i hardvera, Liberation će podržavati samo DAC-ove koji imaju objavljen komunikacijski protokol. Smatram da je to najbolji put naprijed za lasersku industriju.

#### **Kako mogu znati može li se moj laser koristiti s Liberation?**

Ako vaš laser ima nešto od sljedećeg, možete ga koristiti s Liberation:

* Vanjski **ILDA ulaz** – 25-pinski D priključak, koji se koristi s kompatibilnim vanjskim kontrolerom.
* Interno ugrađen **Ether Dream**.
* Bilo koji **LaserCube** (radi i s USB i s Wi-Fi LaserCube uređajima).
* **X-Laser uređaj s ugrađenim Mercury sustavom** (u Ether Dream načinu rada).
* **LaserAnimation Sollinger projektor s ugrađenim AVB-om** (samo macOS, zahtijeva AVB-kompatibilne mrežne uređaje, trenutačno u testiranju).

Za više informacija pogledajte [Kompatibilni laseri i kontroleri (DAC-ovi)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Mogu li koristiti Liberation sa svojim LaserCube uređajem?**

Da, Liberation radi izravno s bilo kojim LaserCube uređajem. Pogledajte [LaserCube](hardware/lasercube.md)

## Licence

#### **Koja je cijena licence?**

Trenutačne cijene pogledajte na stranici [trgovina](https://liberationlaser.com/shop).

#### **Koja su ograničenja između razina licence?**

Trenutačne opcije licence pogledajte na stranici [trgovina](https://liberationlaser.com/shop).

Imajte na umu da na **svakoj** razini, čak i besplatnoj, možete postavljati, pregledavati i dizajnirati predstave s koliko god lasera želite. Nema drugih ograničenja osim broja lasera koje možete _aktivirati za izlaz_. Sve ostale značajke u Liberation dostupne su svima.

#### **Mogu li prijeći na novu razinu?**

U bilo kojem trenutku možete prijeći na višu razinu. Dobit ćete djelomični povrat za preostalo vrijeme u trenutačnom plaćenom razdoblju, a nova razina licence počet će odmah. Pogledajte [Nadogradnja / vraćanje licence na nižu razinu](installation/upgrade-downgrade-your-license.md)

#### **Mogu li vratiti licencu na nižu razinu?**

Licencu možete vratiti na nižu razinu u bilo kojem trenutku, ali promjena će stupiti na snagu na kraju trenutačnog plaćenog razdoblja. Pogledajte [Nadogradnja / vraćanje licence na nižu razinu](installation/upgrade-downgrade-your-license.md)

#### **Mogu li pauzirati plaćanja za licencu?**

Da. Licenca se može pauzirati na sljedeći datum pretplate i ponovno pokrenuti u bilo kojem trenutku. To je korisno ako povremeno počinjete i prestajete koristiti softver, a pritom ne morate ponovno unositi podatke o kartici. Pogledajte [Pauziranje ili otkazivanje plaćanja](installation/cancel-your-subscription.md)

#### **Kako mogu trajno otkazati licencu?**

Svoju ponavljajuću licencu možete otkazati u bilo kojem trenutku, a automatski će se deaktivirati na kraju trenutačnog plaćenog razdoblja. Pogledajte [Pauziranje ili otkazivanje plaćanja](installation/cancel-your-subscription.md)

#### **Zašto je Liberation pretplata?**

Kratak odgovor je da to održava Liberation održivim, aktivno razvijanim i pravednim, a istovremeno svima omogućuje otvaranje, uređivanje, spremanje, vježbanje i pregled predstava bez plaćanja.

Više o razlozima napisao sam ovdje: [Zašto Liberation koristi pretplatu](https://liberationlaser.com/articles/why-a-subscription).

#### **Mogu li dobiti trajnu ili dugoročnu licencu za svoju instalaciju / turnejsku produkciju?**

Godišnje (ili čak višegodišnje) unaprijed plaćene licence dostupne su za stalne instalacije i turnejske produkcije. Ako je želite postaviti, pošaljite e-poštu na [billing@liberationlaser.com](mailto:billing@liberationlaser.com).

Trajne licence trenutačno nisu dostupne. Za više konteksta pogledajte [Zašto Liberation koristi pretplatu](https://liberationlaser.com/articles/why-a-subscription).

#### **Kako ovlastiti računalo svojom licencom?**

Nakon kupnje licence možete ovlastiti računalo izravno u softveru Liberation. Na zaslonu _About_ vidjet ćete gumb _Authorise_ koji će vas zatražiti da se prijavite na web-mjesto. Slijedite upute na zaslonu kako biste dovršili postupak autorizacije. Pogledajte [Autorizacija i uklanjanje autorizacije](installation/authorising-and-de-authorising.md)

#### **Koliko često moram povezati računalo s internetom?**

Svaki put kada se ponavljajuća plaćena licenca uspješno obnovi, morat ćete povezati Liberation s internetom kako bi ažurirao internu licencu. Dakle, za mjesečnu licencu s automatskom obnovom morat ćete se povezati svaki mjesec.

#### **Što se događa ako nakon sljedećeg plaćanja ne mogu povezati računalo s internetom?**

Za mjesečne ponavljajuće plaćene licence Liberation vam obično daje grace period od 7 dana nakon obnove plaćene licence da se povežete s internetom i ažurirate internu licencu. Nakon tog razdoblja Liberation će se vratiti u način rada _Free_.

#### **Što se događa ako mi kreditna kartica istekne?**

Dobit ćete obavijest e-poštom od našeg pružatelja usluga plaćanja i morat ćete ažurirati podatke o kartici. Prijavite se na web-mjesto i upotrijebite _UPDATE CARD DETAILS_ na stranici licence ili _Update_ pod _Billing and payments_. To morate učiniti unutar grace perioda kako ne biste izgubili pristup plaćenim značajkama.

#### **Na koliko računala mogu instalirati Liberation?**

Liberation možete instalirati na koliko god računala želite. Autorizacije licence potrebne su samo za omogućavanje laserskog / DMX izlaza, a razina vaše licence određuje koliko računala može istovremeno biti autorizirano za izlaz. Pogledajte [Kako funkcionira licenciranje](installation/how-licensing-works.md)

#### **Kako premjestiti licencu s jednog računala na drugo?**

* Otvorite Liberation na računalu koje više ne želite koristiti
* Provjerite jeste li povezani s internetom i kliknite gumb _De-authorise this computer_ na zaslonu _About_
* Sada otvorite Liberation na novom računalu
* Kliknite gumb _Authorise this computer_ na zaslonu _About_.
* Otvorit će se web-mjesto; prijavite se i slijedite upute na zaslonu kako biste dovršili autorizaciju

Možete i daljinski ukloniti autorizaciju s računala kojem više nemate pristup (uz određena ograničenja). Pogledajte [Autorizacija i uklanjanje autorizacije](installation/authorising-and-de-authorising.md)

#### **Mogu li ukloniti autorizaciju za Liberation na računalu koje je izgubljeno ili ukradeno?**

Autorizaciju računala možete ukloniti putem web-mjesta. Ako instalacija Liberation nije bila na mreži od posljednjeg osvježavanja licence, to se može učiniti odmah.

Ako jest bila, uklanjanje autorizacije stupit će na snagu pri sljedećem osvježavanju licence ili kada se računalo poveže s internetom, što god nastupi prije. Ako hitno trebate ponovno autorizirati novo računalo, obratite se podršci.

### Korištenje Liberation

#### Zadano postavljanje ima 8 lasera - kako to promijeniti?

Pogledajte [Postavljanje projekta](setting-up/setting-up-your-project.md) i [Dodavanje / uklanjanje lasera](setting-up/adding-removing-lasers.md)

#### Mogu li kopirati postavke zone s jednog lasera na druge?

Da! Pogledajte [Kopiranje zones između lasera](output-view/copy-zones-between-lasers.md)

#### Mogu li upisati broj umjesto korištenja klizača?

Da. Kliknite klizač uz `Cmd / Ctrl` i vrijednost možete unijeti pomoću tipkovnice.

#### **Kako sinkronizirati Liberation s glazbom?**

Ima inteligentan sustav "tap tempo" koji radi kako biste očekivali, ali možete koristiti i vanjski MIDI clock ili Ableton Link. Pogledajte [Tempo / sinkronizacija](tempo-synchronisation.md). Timeline se može sinkronizirati s dolaznim LTC/SMPTE timecode signalom putem bilo kojeg audio sučelja. Pogledajte [Vremenski kod (timecode)](timecode.md).

#### Koje postavke trebam prilagoditi za najbolji izlaz iz lasera?

Glavna postavka je _Scanner Sync,_ koja kompenzira malo kašnjenje između pomicanja zrcala i promjene svjetline lasera. Ako laserske točke/snopovi imaju male „repove”, trebate prilagoditi tu postavku. (Primjer „repova” pogledajte na fotografijama na stranici [Panel postavki laserskog izlaza](setting-up/laser-settings.md))

Možete pokušati promijeniti i brzinu skenera: sporije ako su vaši skeneri osnovni, ili brže ako su kvalitetni. Ali **budite oprezni jer možete oštetiti skenere ako ih previše opteretite.**

Postoje i neke unaprijed zadane postavke skenera. Zadana opcija je konzervativna i dobra za većinu zahtjeva za laserske snopove. No postoje i druge unaprijed zadane postavke ako imate bolje skenere, kao i postavke podešene za grafiku.

Za više informacija pogledajte [Panel postavki laserskog izlaza](setting-up/laser-settings.md), a za informacije o izradi vlastitih unaprijed zadanih postavki pogledajte [◼️ Unaprijed zadane postavke skenera i profili renderiranja](advanced/scanner-presets.md) (napredno, u izradi)

Ravnotežu boja možete korigirati i pomoću postavki _Colour calibration_. Pogledajte [Kalibracija boja](advanced/colour-calibration.md) (napredna tehnika)

#### Što radi postavka _Latency(ms)_?

To je latencija okvira, odnosno maksimalno vrijeme između generiranja okvira i njegova naknadnog slanja laseru. Ne biste je trebali morati prilagođavati, ali ako imate problema s mrežom, možete je pokušati povećati. Za više detalja pogledajte [Postavka latencije](setting-up/latency-setting.md).

### Clips

#### Kako prilagoditi zone i postavke za Clip bez pokretanja?

Kliknite uz `Alt / Option` kako biste ga postavili kao _trenutačno odabrani Clip_, ali bez aktiviranja. Pogledajte i [Pokretanje / zaustavljanje Clips](clips/starting-stopping-clips.md)

#### Kako kopirati Clips?

Kliknite i povucite dok držite tipku `Alt / Option`. Pogledajte i [Organiziranje Clip Deck](clips/organising-your-clip-deck.md)

#### Kako izbrisati Clips?

Kliknite ih i povucite izvan Clip Deck. Pogledajte i [Organiziranje Clip Deck](clips/organising-your-clip-deck.md)

#### Kako višestruko odabrati, izbrisati, kombinirati Clip Deck itd.?

Pogledajte [Organiziranje Clip Deck](clips/organising-your-clip-deck.md)

#### Što označavaju mali simbol mikrofona i druge ikone na Clip?

Tu su kako bi pokazale da Clip prima zvuk ili MIDI ulaz, a tri točke pokazuju da postoji kašnjenje zone. Pogledajte [Što znače male ikone na gumbima za Clip?](clips/what-are-the-small-icons-on-the-clip-buttons.md)
