---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Česta pitanja

## Hardver

#### **Radi li Liberation na Windows?**

Da - Liberation u potpunosti podržava **Windows 10 i 11 (64-bit)**, s potpuno istim značajkama kao verzija za Mac. Svako izdanje izlazi istodobno za obje platforme.

#### **Radi li Liberation na Mac računalima?**

Da - Liberation u potpunosti podržava **Mac (macOS 12 Monterey i noviji)**, uz potpunu jednakost značajki s verzijom za Windows. Sva ažuriranja objavljuju se zajedno.

#### **Koje su minimalne specifikacije računala?**

Ovisi o tome koliko lasera želite kontrolirati. Ako koristite samo nekoliko lasera, bit će dovoljno i slabije računalo. Svaki Mac s Apple Silicon procesorom radi vrlo dobro i trebao bi moći kontrolirati do 100 lasera. Ako izvodite složene showove u kojima je pouzdanost kritična, preporučujemo najbolje računalo koje si možete priuštiti.

#### **Koliko lasera mogu kontrolirati s Liberation?**

Liberation može pokretati mnogo lasera na jednom računalu. Testiran je s više od 100 laserskih kontrolera, pa odgovor ovisi o:

* CPU-u vašeg računala
* brzini mreže
* vrsti vaše pretplate

#### **Koje MIDI kontrolere mogu koristiti?**

Liberation je osmišljen i optimiziran za popularni MIDI kontroler APC40 Mk2. Radi i s APC40 Mk1. Pogledajte [Upravljanje uživo s APC40](midi-control/live-control-with-the-apc40.md)

Postupno dodajemo podršku za dodatne MIDI kontrolere, a trenutačno podržavamo i APC Mini Mk2 te MIDI Fighter Twister.

Postoji i sustav MIDI Send/Receive koji omogućuje dodatno MIDI upravljanje. Pogledajte [MIDI Send/Receive sustav](midi-control/midi-send-receive.md)

Za više informacija pogledajte [MIDI upravljanje](midi-control/).

#### **Mogu li ga koristiti s bilo kojim MIDI kontrolerom?**

Trenutačno radimo na podesivom MIDI sustavu koji će to omogućiti u budućnosti. U međuvremenu su neki korisnici uspješno koristili MIDI interpreter koji može pretvoriti bilo koje MIDI poruke za sustav MIDI Send/Receive, ali to je zahtjevan i napredan postupak. Potražite savjete za takvo postavljanje na [forumu](https://forum.liberationlaser.com), ali realno je APC40 najbolja opcija.

## Laserski kontroleri

#### **Koji su laserski kontroleri kompatibilni s Liberation?**

* [Ether Dream (preporučeno)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (možda ćete morati ažurirati firmware)
* LaserCube USB (i LaserDock)
* mrežni protokol LaserCube (uz žičanu vezu)
* AVB kakav koriste [LASollinger laseri](https://laseranimation.com/en/) (trenutačno samo macOS, u fazi testiranja)

Za više informacija pogledajte [Kompatibilni laseri i kontroleri (DAC-ovi)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Zašto ne podržavate laserski kontroler \[drugog proizvođača]?**

Kako bismo potaknuli bolju interoperabilnost između softvera i hardvera, Liberation će podržavati samo DAC uređaje koji imaju javno objavljen komunikacijski protokol. Vjerujem da je to najbolji smjer za lasersku industriju.

#### **Kako mogu znati može li se moj laser koristiti s Liberation?**

Ako vaš laser ima nešto od navedenog, možete ga koristiti s Liberation:

* Vanjski **ILDA ulaz** – 25-pinski D konektor, za upotrebu s kompatibilnim vanjskim kontrolerom.
* Interno ugrađen **Ether Dream**.
* Bilo koji **LaserCube** (radi i s USB i s Wi-Fi LaserCube).
* **X-Laser uređaj s ugrađenim sustavom Mercury** (u načinu Ether Dream).
* **LaserAnimation Sollinger projektor s ugrađenim AVB-om** (samo macOS, zahtijeva AVB-kompatibilne mrežne uređaje, trenutačno u fazi testiranja).

Za više informacija pogledajte [Kompatibilni laseri i kontroleri (DAC-ovi)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Mogu li koristiti Liberation sa svojim LaserCube?**

Da, Liberation radi izravno s bilo kojim LaserCube. Pogledajte [LaserCube](hardware/lasercube.md)

## Licence

#### **Koja je cijena licence?**

Trenutačne cijene pogledajte na stranici [trgovine](https://liberationlaser.com/shop).

#### **Koja su ograničenja između licencijskih razina?**

Trenutačne opcije licenci pogledajte na stranici [trgovine](https://liberationlaser.com/shop).

Imajte na umu da na **svakoj** razini, čak i besplatnoj, možete postavljati, pregledavati i dizajnirati showove s koliko god lasera želite. Nema nikakvih drugih ograničenja osim broja lasera na kojima možete pokrenuti radnju _arm_. Sve ostale značajke Liberation dostupne su svima.

#### **Mogu li nadograditi licencu na novu razinu?**

U bilo kojem trenutku možete prijeći na višu razinu. Dobit ćete djelomični povrat za preostalo vrijeme svoje trenutačne licence, a novi plan počinje odmah. Pogledajte [Nadogradnja i snižavanje licence](installation/upgrade-downgrade-your-license.md)

#### **Mogu li sniziti razinu svoje licence?**

Razinu možete sniziti u bilo kojem trenutku, ali promjena će stupiti na snagu na kraju trenutačnog licencijskog razdoblja. Pogledajte [Nadogradnja i snižavanje licence](installation/upgrade-downgrade-your-license.md)

#### **Kako autorizirati računalo za svoju licencu?**

Nakon kupnje licence računalo možete autorizirati izravno u softveru Liberation. Na zaslonu _About_ vidjet ćete gumb _Authorise_ koji će vas uputiti da se prijavite na web-mjesto. Slijedite upute na zaslonu kako biste dovršili postupak autorizacije. Pogledajte [Autorizacija i deautorizacija](installation/authorising-and-de-authorising.md)

#### **Koliko često moram povezati računalo s internetom?**

Svaki put kada se licenca obnovi, morat ćete povezati Liberation s internetom kako bi ažurirao svoju internu licencu. Ako plaćate mjesečnu pretplatu, povezivanje je potrebno svaki mjesec.

#### **Što se događa ako nakon obnove ne mogu povezati računalo s internetom?**

Liberation vam daje poček od 7 dana nakon obnove licence da se povežete s internetom i ažurirate internu licencu. Nakon tog razdoblja Liberation se vraća u način _Free_.

#### **Što se događa ako moja kreditna kartica istekne?**

Dobit ćete obavijest e-poštom od našeg pružatelja usluge plaćanja i morat ćete ažurirati podatke za plaćanje. Prijavite se na web-mjesto i na stranici pretplata upotrijebite poveznicu _Update payment details_.

#### **Kako mogu otkazati pretplatničku licencu?**

Prijavite se na web-mjesto, otvorite stranicu _Your subscriptions_, odaberite pretplatu koju želite otkazati, zatim kliknite poveznicu _Cancel Subscription_. Liberation možete nastaviti koristiti do kraja licencijskog razdoblja.

#### **Na koliko računala mogu instalirati Liberation?**

Liberation možete instalirati na koliko god računala želite. Autorizacije licence potrebne su samo za omogućavanje izlaza lasera / DMX-a, a vaša licencijska razina određuje koliko računala može istodobno biti autorizirano za izlaz. Pogledajte [Kako funkcionira licenciranje](installation/how-licensing-works.md)

#### **Kako premjestiti licencu s jednog računala na drugo?**

* Otvorite Liberation na računalu koje više ne želite koristiti
* Provjerite jeste li povezani s internetom i kliknite gumb _De-authorise this computer_ na zaslonu _About_
* Sada otvorite Liberation na novom računalu
* Kliknite gumb _Authorise this computer_ na zaslonu _About_.
* Otvorit će se web-mjesto; prijavite se i slijedite upute na zaslonu kako biste dovršili autorizaciju

Možete i daljinski deautorizirati računalo kojem više nemate pristup (uz određena ograničenja). Pogledajte [Autorizacija i deautorizacija](installation/authorising-and-de-authorising.md)

#### **Mogu li deautorizirati Liberation na računalu koje je izgubljeno ili ukradeno?**

Računalo možete deautorizirati putem web-mjesta. Ako instalacija Liberation nije bila online od vaše posljednje obnove, to se može napraviti odmah.

Ako nije tako, deautorizacija će stupiti na snagu kada se pretplata obnovi ili kada se računalo poveže s internetom, ovisno o tome što se dogodi prvo. Ako hitno morate ponovno autorizirati novo računalo, obratite se podršci.

### Korištenje Liberation

#### Zadana postavka ima 8 lasera - kako to promijeniti?

Pogledajte [Postavljanje projekta](setting-up/setting-up-your-project.md) i [Dodavanje i uklanjanje lasera](setting-up/adding-removing-lasers.md)

#### Mogu li kopirati postavke za zone s jednog lasera na ostale?

Da! Pogledajte [Kopiranje postavki za zone između lasera](output-view/copy-zones-between-lasers.md)

#### Mogu li upisati broj umjesto korištenja klizača?

Da. Kliknite klizač uz `Cmd / Ctrl` i možete unijeti vrijednost tipkovnicom.

#### **Kako sinkronizirati Liberation s glazbom?**

Ima inteligentan sustav "tap tempo" koji radi kako biste očekivali, ali možete koristiti i vanjski MIDI clock ili Ableton Link. Pogledajte [Sinkronizacija tempa](tempo-synchronisation.md). Timeline se može sinkronizirati s dolaznim LTC/SMPTE vremenskim kodom putem bilo kojeg audio sučelja. Pogledajte [Vremenski kod (timecode)](timecode.md).

#### Koje postavke trebam prilagoditi za najbolji izlaz iz lasera?

Glavna postavka je _Colour Shift,_ koja kompenzira malo kašnjenje između pomicanja zrcala i promjene svjetline lasera. Ako točke/snopovi vašeg lasera imaju male 'repove', to trebate prilagoditi. (Primjer 'repova' pogledajte na fotografijama na stranici [Laser Settings](setting-up/laser-settings.md))

Možete pokušati promijeniti i brzinu skenera: sporije ako su vaši skeneri osnovni, ili brže ako su kvalitetni. Ali **koristite s oprezom jer možete oštetiti skenere ako ih previše opteretite.**

Postoje i neke unaprijed definirane postavke skenera. Zadana opcija je konzervativna i prikladna za većinu zahtjeva za laserske snopove. No postoje i drugi preseti za bolje skenere, kao i preseti podešeni za grafiku.

Za više informacija pogledajte [Laser Settings](setting-up/laser-settings.md), a za informacije o stvaranju vlastitih preseta pogledajte [Preseti skenera](advanced/scanner-presets.md) (napredno, u izradi)

Ravnotežu boja možete ispraviti i pomoću postavki _Colour calibration_. Pogledajte [Kalibracija boje](advanced/colour-calibration.md)(napredna tehnika)

#### Što radi postavka _Latency(ms)_?

To je latencija framea, odnosno najveće vrijeme između generiranja framea i njegova slanja laseru. Ne biste je trebali morati podešavati, ali ako imate problema s mrežom, možete je pokušati povećati. Za više pojedinosti pogledajte [Postavka Latency(ms)](setting-up/latency-setting.md).

### Clips

#### Kako prilagoditi zone i postavke za Clip bez njegova pokretanja?

Kliknite uz `Alt / Option` kako bi postao _trenutačno odabrani Clip_, ali bez aktiviranja. Pogledajte i [Pokretanje i zaustavljanje Clips](clips/starting-stopping-clips.md)

#### Kako kopirati Clips?

Kliknite i povucite držeći tipku `Alt / Option`. Pogledajte i [Organiziranje Clip Deck](clips/organising-your-clip-deck.md)

#### Kako izbrisati Clips?

Kliknite ih i povucite izvan Clip Deck. Pogledajte i [Organiziranje Clip Deck](clips/organising-your-clip-deck.md)

#### Kako napraviti višestruki odabir, brisanje, kombiniranje Clip Deck itd.?

Pogledajte [Organiziranje Clip Deck](clips/organising-your-clip-deck.md)

#### Što označavaju mali simbol mikrofona i druge ikone na gumbu za Clip?

One vam pokazuju da Clip koristi zvučni ili MIDI ulaz, a 3 točkice pokazuju da postoji kašnjenje za zone. Pogledajte [Što znače male ikone na gumbima Clip?](clips/what-are-the-small-icons-on-the-clip-buttons.md)
