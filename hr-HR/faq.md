---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Česta pitanja

## Hardver

#### **Radi li Liberation na Windowsima?**

Da - Liberation u potpunosti podržava **Windows 10 i 11 (64-bit)**, s potpuno istim značajkama kao verzija za Mac. Svako izdanje izlazi istovremeno za obje platforme.

#### **Radi li Liberation na Macu**

Da - Liberation u potpunosti podržava **Mac (macOS 12 Monterey i noviji)**, s istim skupom značajki kao verzija za Windows. Sva ažuriranja objavljuju se zajedno.

#### **Koja je minimalna potrebna konfiguracija računala?**

Ovisi o tome koliko lasera želite upravljati. Ako koristite samo nekoliko lasera, bit će dovoljno i slabije računalo. Svaki Apple Silicon Mac radi vrlo dobro i trebao bi moći upravljati s do 100 lasera. Ako radite složene nastupe u kojima je pouzdanost posebno važna, preporučujemo najbolje računalo koje si možete priuštiti.

#### **Koliko lasera mogu upravljati pomoću Liberation?**

Liberation može pokretati mnogo lasera s jednog računala; testiran je s više od 100 laserskih kontrolera, pa odgovor ovisi o:

* procesoru vašeg računala
* brzini mreže
* razini vaše licence

#### **Koje MIDI kontrolere mogu koristiti?**

Liberation je osmišljen i optimiziran za popularni APC40 Mk2 MIDI kontroler. Radi i s APC40 Mk1. Pogledajte [Live MIDI kontroleri](midi-control/live-control-with-the-apc40.md "mention")

Liberation podržava i APC Mini te MIDI Fighter Twister. APC40 Mk2 i dalje je najpotpuniji referentni kontroler.

Postoji i sustav MIDI Send/Receive, koji nudi dodatno MIDI upravljanje. Pogledajte [MIDI Send/Receive](midi-control/midi-send-receive.md "mention")

Za više informacija pogledajte [MIDI upravljanje](midi-control/ "mention").

#### **Mogu li ga koristiti s bilo kojim MIDI kontrolerom?**

Za druge kontrolere upotrijebite sustav MIDI Send/Receive ili MIDI prevoditelj koji može slati zadane MIDI poruke za Liberation. Potražite savjete za takvu konfiguraciju na [forumu](https://forum.liberationlaser.com), ali realno je APC40 Mk2 i dalje najbolja opcija za većinu nastupa uživo.

## Laserski kontroleri

#### **Koji su laserski kontroleri kompatibilni s Liberation?**

* [Ether Dream (preporučeno)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (možda ćete morati ažurirati firmware)
* LaserCube USB (i LaserDock)
* LaserCube mrežni protokol (uz žičanu vezu)
* AVB, kako ga koriste [LASollinger laseri](https://laseranimation.com/en/) (trenutačno samo macOS, u testiranju)

Za više informacija pogledajte [Kompatibilni laseri i kontroleri (DAC-ovi)](hardware/compatible-lasers-and-controllers-dacs.md "mention")

#### **Zašto ne podržavate laserski kontroler \[drugog proizvođača]?**

Kako bi se potaknula veća interoperabilnost softvera i hardvera, Liberation će podržavati samo one DAC-ove koji imaju objavljen komunikacijski protokol. Vjerujem da je to najbolji smjer za lasersku industriju.

#### **Kako mogu znati može li se moj laser koristiti s Liberation?**

Ako vaš laser ima nešto od sljedećeg, možete ga koristiti s Liberation:

* Vanjski **ILDA ulaz** – 25-pin D konektor, koji se koristi s kompatibilnim vanjskim kontrolerom.
* Interno ugrađeni **Ether Dream**.
* Bilo koji **LaserCube** (radi i s USB i s Wi-Fi LaserCube uređajima).
* **X-Laser uređaj s ugrađenim Mercury sustavom** (u načinu rada Ether Dream).
* **LaserAnimation Sollinger projektor s ugrađenim AVB-om** (samo macOS, zahtijeva mrežne uređaje kompatibilne s AVB-om, trenutačno u testiranju).

Za više informacija pogledajte [Kompatibilni laseri i kontroleri (DAC-ovi)](hardware/compatible-lasers-and-controllers-dacs.md "mention")

#### **Mogu li koristiti Liberation sa svojim LaserCube uređajem?**

Da, Liberation radi izravno s bilo kojim LaserCube uređajem. Pogledajte [LaserCube](hardware/lasercube.md "mention")

## Licence

#### **Koja je cijena licence?**

Trenutačne cijene pogledajte na stranici [trgovina](https://liberationlaser.com/shop).

#### **Koja su ograničenja između razina licence?**

Trenutačne opcije licenci pogledajte na stranici [trgovina](https://liberationlaser.com/shop).

Napomena: na **svakoj** razini, čak i besplatnoj, možete postavljati, pregledavati i dizajnirati nastupe s koliko god lasera želite. Nema drugih ograničenja osim broja lasera koje možete aktivirati za izlaz. Sve ostale značajke u Liberation dostupne su svima.

#### **Mogu li nadograditi na višu razinu?**

U bilo kojem trenutku možete nadograditi na višu razinu. Dobit ćete djelomični povrat za preostalo vrijeme u trenutačnom plaćenom razdoblju, a nova razina licence počet će odmah. Pogledajte [Nadogradnja / vraćanje licence na nižu razinu](installation/upgrade-downgrade-your-license.md "mention")

#### **Mogu li vratiti licencu na nižu razinu?**

Licencu možete vratiti na nižu razinu u bilo kojem trenutku, ali promjena će stupiti na snagu na kraju trenutačnog plaćenog razdoblja. Pogledajte [Nadogradnja / vraćanje licence na nižu razinu](installation/upgrade-downgrade-your-license.md "mention")

#### **Mogu li pauzirati plaćanja za licencu?**

Da. Licenca se može pauzirati na sljedeći datum pretplate i ponovno pokrenuti u bilo kojem trenutku. To je korisno ako Liberation koristite povremeno, a ne morate ponovno unositi podatke kartice. Pogledajte [Pauziranje ili otkazivanje plaćanja](installation/cancel-your-subscription.md "mention")

#### **Kako mogu trajno otkazati licencu?**

Svoju ponavljajuću licencu možete otkazati u bilo kojem trenutku, a automatski će se deaktivirati na kraju trenutačnog plaćenog razdoblja. Pogledajte [Pauziranje ili otkazivanje plaćanja](installation/cancel-your-subscription.md "mention")

#### **Kako autorizirati računalo svojom licencom?**

Nakon što kupite licencu, računalo možete autorizirati unutar samog softvera Liberation. Na zaslonu _About_ vidjet ćete gumb _Authorise_, koji će vas zatražiti da se prijavite na web-mjesto. Slijedite upute na zaslonu kako biste dovršili postupak autorizacije. Pogledajte [Autorizacija i uklanjanje autorizacije](installation/authorising-and-de-authorising.md "mention")

#### **Koliko često moram povezati računalo s internetom?**

Svaki put kada se ponavljajuća plaćena licenca uspješno obnovi, morat ćete povezati Liberation s internetom kako bi se ažurirala njegova interna licenca. Dakle, za mjesečnu licencu s automatskom obnovom morat ćete se povezati svaki mjesec.

#### **Što se događa ako nakon sljedeće uplate ne mogu povezati računalo s internetom?**

Za mjesečne ponavljajuće plaćene licence Liberation obično daje razdoblje odgode od 7 dana nakon obnove plaćene licence, kako biste se povezali s internetom i ažurirali internu licencu. Nakon tog razdoblja Liberation će se vratiti u način rada _Free_.

#### **Što se događa ako mi istekne kreditna kartica?**

Dobit ćete obavijest e-poštom od našeg pružatelja usluga plaćanja i morat ćete ažurirati podatke kartice. Prijavite se na web-mjesto i upotrijebite _UPDATE CARD DETAILS_ na stranici licence ili _Update_ pod _Billing and payments_. To morate učiniti unutar razdoblja odgode kako biste izbjegli gubitak pristupa plaćenim značajkama.

#### **Na koliko računala mogu instalirati Liberation?**

Liberation možete instalirati na koliko god računala želite. Autorizacije licence potrebne su samo za omogućavanje laserskog / DMX izlaza, a razina vaše licence određuje koliko računala može istovremeno biti autorizirano za izlaz. Pogledajte [Kako funkcionira licenciranje](installation/how-licensing-works.md "mention")

#### **Kako premjestiti licencu s jednog računala na drugo?**

* Otvorite Liberation na računalu koje više ne želite koristiti
* Provjerite jeste li povezani s internetom i kliknite gumb _De-authorise this computer_ na zaslonu _About_
* Zatim otvorite Liberation na novom računalu
* Kliknite gumb _Authorise this computer_ na zaslonu _About_.
* Otvorit će se web-mjesto; prijavite se i slijedite upute na zaslonu kako biste dovršili autorizaciju

Također možete daljinski ukloniti autorizaciju računala kojem više nemate pristup (uz određena ograničenja). Pogledajte [Autorizacija i uklanjanje autorizacije](installation/authorising-and-de-authorising.md "mention")

#### **Mogu li ukloniti autorizaciju za Liberation na računalu koje je izgubljeno ili ukradeno?**

Autorizaciju računala možete ukloniti putem web-mjesta. Ako instalacija Liberation nije bila na mreži od posljednjeg osvježavanja licence, to se može učiniti odmah.

Ako nije, uklanjanje autorizacije stupit će na snagu pri sljedećem osvježavanju licence ili kada se računalo poveže s internetom, što god nastupi prije. Ako hitno trebate ponovno autorizirati novo računalo, obratite se podršci.

### Korištenje Liberation

#### Zadana konfiguracija ima 8 lasera - kako to mogu promijeniti?

Pogledajte [Postavljanje projekta](setting-up/setting-up-your-project.md "mention") i [Dodavanje / uklanjanje lasera](setting-up/adding-removing-lasers.md "mention")

#### Mogu li kopirati postavke za zone s jednog lasera na druge?

Da! Pogledajte [Kopiranje zone između lasera](output-view/copy-zones-between-lasers.md "mention")

#### Mogu li upisati broj umjesto korištenja klizača?

Da. Kliknite klizač uz `Cmd / Ctrl` i možete unijeti vrijednost pomoću tipkovnice.

#### **Kako sinkronizirati Liberation s glazbom?**

Ima inteligentan sustav "tap tempo" koji radi onako kako biste očekivali, ali možete koristiti i vanjski MIDI clock ili Ableton Link. Pogledajte [Tempo / sinkronizacija](tempo-synchronisation.md "mention"). Timeline se može sinkronizirati s dolaznim LTC/SMPTE vremenskim kodom putem bilo kojeg audio sučelja. Pogledajte [Vremenski kod](timecode.md "mention").

#### Koje postavke trebam prilagoditi za najbolji izlaz iz lasera?

Glavna postavka je _Scanner Sync_, koja kompenzira malo kašnjenje između pomicanja zrcala i promjene svjetline lasera. Ako laserske točke/snopovi imaju male "repove", trebate prilagoditi ovu postavku. (Primjer "repova" pogledajte na fotografijama na stranici [Ploča s postavkama laserskog izlaza](setting-up/laser-settings.md "mention"))

Možete pokušati promijeniti i brzinu skenera: sporije ako su vaši skeneri osnovni, ili brže ako su kvalitetni. Ali **budite oprezni jer skenere možete oštetiti ako ih opteretite previše.**

Postoje i neke unaprijed definirane postavke skenera. Zadana opcija je konzervativna i dobra za većinu zahtjeva laserskih snopova. No postoje i druge unaprijed definirane postavke za bolje skenere, kao i postavke podešene za grafiku.

Za više informacija pogledajte [Ploča s postavkama laserskog izlaza](setting-up/laser-settings.md "mention"), a za informacije o izradi vlastitih unaprijed definiranih postavki pogledajte [◼️ Unaprijed definirane postavke skenera i profili renderiranja](advanced/scanner-presets.md "mention") (napredno, u izradi)

Ravnotežu boja možete ispraviti i pomoću postavki _Colour calibration_. Pogledajte [Kalibracija boja](advanced/colour-calibration.md "mention") (napredna tehnika)

#### Što radi postavka _Latency(ms)_?

To je latencija okvira, odnosno najveće vrijeme između generiranja okvira i njegova naknadnog slanja laseru. Ne biste je trebali morati prilagođavati, ali ako imate problema s mrežom, možete je pokušati povećati. Za više pojedinosti pogledajte [Postavka latencije](setting-up/latency-setting.md "mention").

### Clips

#### Kako prilagoditi zone i postavke za Clip bez njegova pokretanja?

Kliknite uz `Alt / Option` kako bi postao _trenutačno odabrani Clip_, ali bez aktiviranja. Pogledajte i [Pokretanje / zaustavljanje Clips](clips/starting-stopping-clips.md "mention")

#### Kako kopirati Clips?

Kliknite i povucite držeći tipku `Alt / Option`. Pogledajte i [Organiziranje Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Kako izbrisati Clips?

Kliknite ih i povucite izvan Clip Deck. Pogledajte i [Organiziranje Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Kako odabrati više stavki, izbrisati ih, kombinirati Clip Deck i slično?

Pogledajte [Organiziranje Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Što označavaju mali simbol mikrofona i druge ikone na Clip?

One pokazuju da Clip prima zvučni ili MIDI ulaz, a tri točke pokazuju da postoji kašnjenje zone. Pogledajte [Što znače male ikone na gumbima Clip?](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
