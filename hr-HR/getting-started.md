---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Vodič za brzi početak

## Uvod

Dobro došli u **Liberation** - novu generaciju softvera za laserske showove.

Liberation je moćan i složen moderan softver; izgrađen je na temeljima upotrebljivosti i pouzdanosti kako bi vam dao slobodu da izrazite svoju kreativnost. Brz je, učinkovit i radi glatko; slijedite ovaj _Vodič za brzi početak_ i bit ćete spremni za rad u vrlo kratkom vremenu!

### Upravljanje laserima

Liberation je dovoljno fleksibilan da možete postaviti lasere i vizualizirati ih čak i bez spojenih stvarnih lasera. A zatim, kada ste spremni za rad, svaki output možete jednostavno dodijeliti laserskom kontroleru.

{% hint style="info" %}
Unutar Liberation možete postaviti i vizualizirati koliko god lasera želite; razine licence (Hobbyist, Pro itd.) ograničavaju samo broj lasera koje možete _aktivirati za izlaz._ To znači da možete dizajnirati laserske showove sa 100 lasera čak i s besplatnom licencom. Nadogradnja vam treba tek kada show zaista želite pokrenuti na stvarnim laserima.
{% endhint %}

Zadana postavka ima 8 lasera raspoređenih vodoravno, ali to možete prilagoditi kako god želite. Vjerojatno je najbolje zadržati ovu zadanu postavku dok se upoznajete sa softverom, a kasnije je možete prilagoditi svojoj hardverskoj konfiguraciji. (Pogledajte [Postavljanje projekta](setting-up/setting-up-your-project.md))

{% hint style="warning" %}
Važno: prije nego što aktivirate bilo koji laser za izlaz, provjerite razumijete li povezane rizike i pažljivo prođite kroz poglavlje [Postavljanje lasera](setting-up/setting-up-lasers.md).
{% endhint %}

## Pregled softvera

### Sigurnosno isključivanje

Kad god koristite lasere, morate imati pri ruci **hardversku tipku za zaustavljanje u nuždi** (pogledajte [Zaustavljanje u nuždi i sigurnosne blokade](hardware/emergency-stop-interlocks.md)), ali ako sve želite deaktivirati bez hitnog zaustavljanja, možete upotrijebiti tipku _**DISARM ALL**_ ili tipku `Escape` (ili tipku _**SESSION**_ na APC40). Global Brightness možete smanjiti i pomoću klizača na zaslonu ili glavnog fadera na APC40.

### Klizači

Kroz Liberation nalaze se razni klizači i kontrole.

{% hint style="info" %}
Kliknite klizač uz `Cmd / Ctrl` kako biste upisali novu vrijednost ako vam treba preciznija kontrola nego što je klizač može pružiti.
{% endhint %}

### Tipkovni prečaci

Cijeli popis tipkovnih prečaca nalazi se ovdje: [Tipkovni prečaci](reference/keyboard-shortcuts.md)

### Raspored zaslona

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Niste sigurni čemu služi određena tipka? Zadržite pokazivač miša iznad nje i dobit ćete opis!
{% endhint %}

#### Izbornik

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

U izborniku ćete pronaći sve opcije za uvoz i izvoz datoteka te za otvaranje panela. Ovdje ćete pronaći i opciju za autorizaciju računala s vašom pretplatom (u _Liberation -> Authorise/Deauthorise this computer_).

#### Traka s ikonama

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Ovdje se nalaze uobičajeni zadaci, kao što su aktiviranje/deaktiviranje svih lasera za izlaz, Global Brightness, Test Pattern te prebacivanje između prikaza 3D, Canvas i Output

### Prikazi

Veliko područje u gornjem lijevom dijelu zaslona može prikazivati jedan od 3 glavna prikaza: **3D**, **CANVAS** i **OUTPUT.** Između njih se prebacujete tipkama na traci s ikonama (ili tipkom `Tab` za prebacivanje između prikaza 3D i OUTPUT, a zatim nastavite pritiskati Tab kako biste redom prošli kroz svaki laser output).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view prikazuje kako će vaši laseri izgledati i može se konfigurirati tako da odgovara vašoj vlastitoj postavi lasera. Kliknite i povucite za rotiranje kamere, a kotačićem miša pomičite se naprijed i natrag. Mnoge druge opcije nalaze se u panelu _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Pogledajte [3D Visualiser](setting-up/3d-visualiser.md).

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view koristi se za konfiguriranje zone i mask za svaki laser. (Obratite pozornost na veliki broj u gornjem lijevom kutu kako biste lako vidjeli na kojem se laseru nalazite!)

Ovaj prikaz predstavlja cijeli output tog lasera i pokazuje gdje se svaka zone nalazi unutar njega. Zadano postoji samo jedna zone po laseru, ali možete dodati onoliko zone koliko je razumno praktično, a sve ćete ih vidjeti u ovom prikazu.

{% hint style="info" %}
**Što je zone?**

Zone je prostor unutar izlaza lasera u koji možete usmjeriti laserski sadržaj. Na jednom laseru možete imati više od jedne zone. Najjednostavnija vrsta zone je _beam_ zone, ali postoje i _canvas_ zone te _DMX_ zone. U ovom ćemo se vodiču uglavnom usredotočiti na beam zone, koje se obično koriste za stvaranje atmosferskih beam efekata u zraku.
{% endhint %}

Laser koji želite uređivati možete odabrati na jedan od sljedećih načina:

* numeriranim tipkama u traci na vrhu
* pritiskom brojčane tipke za željeni laser _(tipke 1-9_)\_
* tipkom `Tab` za kružno prelaženje s jednog lasera na sljedeći

Dodajte novi laser u postavu pritiskom na tipku _+_. (U panelu _Laser Overview_ nalazi se i tipka _ADD LASER_)

Laser uklonite iz postave pritiskom na crvenu tipku ⊖ u panelu _Laser Overview_.

Zumirati možete kotačićem miša, a prikaz pomičete klikom i povlačenjem na bilo kojem mjestu na kojem nema zone.

Kliknite na zone da biste je odabrali, a zatim mišem prilagodite njezine kutne točke. Tijekom povlačenja kuta držite tipku `Alt / Option` kako biste ga prilagodili neujednačeno. Desnim klikom na zone otvorit ćete dodatne opcije, uključujući promjenu vrste zone.

S lijeve strane nalazi se traka s nizom tipki s ikonama; zadržite pokazivač iznad bilo koje tipke kako biste dobili opis njezine funkcije. Tipke ovdje omogućuju dodavanje beam zone, canvas zone i mask. Tu su i opcije za postavljanje testnog uzorka samo za ovaj laser, zajedno s postavkama mreže i prianjanja.

Za više pojedinosti pogledajte [Output view](output-view/).

#### Canvas

Sustav Canvas koristi se uglavnom za grafiku i arhitektonsko mapiranje. Složene slike možete rasporediti preko više lasera i perspektivno korigirati svaki dio. Pogledajte [Grafika i sustav Canvas](graphics-and-the-canvas-system/).

### APC40 MIDI kontroler

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Iako je Liberation moguće kontrolirati mišem i tipkovnicom, mnogo je bolje koristiti APC40 MIDI kontrolersko sučelje (Mark 2 je najbolji izbor, ali Mark 1 također radi).

Pogledajte i: [APC40 referenca](reference/apc40-reference.md)

Sada smo implementirali i podršku za APC Mini Mark 2 i MIDI Fighter Twister, a u razvoju su i dodatni kontroleri. Ipak, APC40 Mark 2 najbolja je opcija za većinu slučajeva.

### Clips i efekti

{% hint style="info" %}
**Što je Clip?**

Clip je spremnik za bilo koji laserski sadržaj unutar Liberation. Clip može sadržavati beam elemente ili grafičke animacije i obično se izvodi kao ponavljajuća petlja. Može se usmjeriti u bilo koju zone (ili _Canvas target area_) i pokreće se tipkama za Clip unutar Clip Deck.
{% endhint %}

#### Pregled Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Ova mreža naziva se _Clip Deck_ i u njoj su pohranjeni svi laserski Clips. Osmišljena je tako da se izravno preslikava na mrežu tipki 8 x 5 na vašem APC40.

**Navigacija kroz Clip Deck.**

Clip Deck možete pomicati lijevo i desno na sljedeće načine:

* tipkama sa strelicama lijevo i desno. Dodajte `Cmd / Ctrl` za pomicanje za cijelu stranicu odjednom.
* trackpadom: prijeđite prstom
* mišem: ako vaš miš ima bočno pomicanje, možete ga koristiti dok je pokazivač iznad Clip Deck
* kotačićem za pomicanje na APC40
* tipkama APC40 _<- DEVICE ->_

Kako biste se lakše snašli, uz vrh se nalazi mini vizualizator za Clip Deck. Pogledajte i [Clips i Clip Deck](clips/)

#### Pokretanje i zaustavljanje Clips

Pritisnite tipku za Clip (mišem ili na APC40) kako biste pokrenuli Clip. Pritisnite je ponovno za zaustavljanje. Kada pokrenete Clip, svi drugi Clips iste boje automatski će se zaustaviti osim ako držite _shift_.

Neki Clips bit će u načinu _Flash mode_ (zadano su to crveni), pa će se zaustaviti čim otpustite tipku za Clip.

Tipka _STOP_ zaustavlja sve trenutno pokrenute Clips.

#### Postavljanje izlaznih zona za Clip

Ispod tipki za Clip vidjet ćete tipke za zone, zadano beam zone od 1 do 8 (_BEAM 1_, _BEAM 2_ itd.). Tipke za zone svijetle kako bi pokazale koje su zone dodijeljene trenutno odabranom Clip.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Dva reda ispod tipki za zone nalaze se tipke za X/Y flip; uključite ih ili isključite kako biste Clip zrcalili vodoravno i okomito.

{% hint style="info" %}
Imajte na umu da su ove dodjele zone i postavke X/Y flip povezane sa samim Clip; zadržavaju se sljedeći put kada pokrenete taj Clip. Nisu globalna postavka.
{% endhint %}

Desnim klikom na Clip možete urediti više njegovih postavki. Pogledajte i [Postavke Clip](clips/clip-settings.md)

### Grupe

Primijetit ćete da svaki Clip ima obojeni obrub, a ta boja označava kojoj _grupi_ pripada. Tipke za Clip na APC40 također svijetle tom bojom.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Grupa 1</td><td>Cijan</td></tr><tr><td>Grupa 2</td><td>Narančasta</td></tr><tr><td>Grupa 3</td><td>Crvena</td></tr><tr><td>Grupa 4</td><td>Indigo</td></tr><tr><td>Grupa 5</td><td>Zelena</td></tr></tbody></table>

Sustav grupa vrlo je fleksibilan i omogućuje vam da:

* zadržite rad Clips u jednoj grupi dok uključujete i isključujete grupe u drugoj
* brzo dodijelite zone i X/Y flip svim Clips unutar grupe
* postavite _Flash mode_ za Clip (Grupa 3 zadano je postavljena na _Flash mode_)

Grupe imaju i postavke za prijelaz pri ulazu/izlazu koje mogu naslijediti njihovi Clips ili se mogu nadjačati.

Grupu za Clip možete dodijeliti tipkama u izborniku desnog klika ili, na APC40, možete pritisnuti tipku grupe i _dok je još držite pritisnutom,_ pritisnuti tipke za Clip.

Promjena postavki zone za sve Clips unutar grupe

Na APC40 pritisnite tipku grupe, zatim _dok je još držite pritisnutom,_ koristite tipke za zone i X/Y kako biste uključivali ili isključivali postavke zone za sve Clips unutar te grupe.

Pogledajte i [Clip grupe](clips/groups.md)

### Efekti

Sustav efekata u Liberation moćan je i svestran način mijenjanja izlaza Clip u stvarnom vremenu. Zadane tipke efekata 1-8 nalaze se ispod tipki za zone.

#### Primjena efekta

Pritisnite tipku efekta kako biste ga uključili ili isključili, ili još bolje, koristite klizače 1-8 na APC40 za postupno pojačavanje i smanjivanje efekata.

#### Parametri efekta

Rotacijskim kontrolerima 1-8\* prilagodite _parametar_ za svaki efekt. (Ili možete desnim klikom miša prilagoditi razinu i parametar). Promjena parametra radi različite stvari ovisno o tome kako je efekt postavljen. Popis u nastavku prikazuje zadane efekte.

{% hint style="info" %}
Mali brojevi koje vidite na tipkama efekata odnose se na _razinu_ i _parametar_ efekta. _Razinom_ upravlja fader na APC40 ili je možete prilagoditi klikom i povlačenjem po tipki. Parametar se podešava rotacijskim kontrolerima na APC40 ili desnim klikom miša.
{% endhint %}

_\*Rotacijski kontroleri 1-8 nalaze se uz vrh APC40 Mk2, a na Mk1 u gornjem desnom dijelu. Pogledajte i:_ [APC40 referenca](reference/apc40-reference.md)

#### Zadani efekti

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Primjenjuje kaotično kretanje na izlaz Clip. Parametar prilagođava količinu/brzinu kaosa.
2. **Sine wave** :\
   Izobličuje sav sadržaj preko pomičnog sinusnog vala. Parametar prilagođava valnu duljinu.
3. **Rotation** :\
   Vrti sve oko središta. Parametar prilagođava brzinu vrtnje.
4. **Horizontal flip** :\
   Vodoravno sabija i rasteže sve. Parametar prilagođava brzinu.
5. **Scale** :\
   Ponavljano skalira sve od pune veličine do nule. Parametar prilagođava brzinu.
6. **Hue** :\
   Mijenja nijansu svega, ali ne mijenja zasićenost (tj. sve što je bijelo ostaje bijelo). Parametar prilagođava nijansu.
7. **Saturation and hue** :\
   Mijenja nijansu svega i ujedno potpuno zasićuje boju (tj. sve što je bijelo mijenja se u boju). Parametar prilagođava nijansu.
8. **Flash** :\
   Ponavljano treperi svjetlinom svega od pune vrijednosti do nule. Parametar prilagođava brzinu treperenja.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

U donjem redu nalazi se još 16 efekata boje za primjenu unaprijed postavljenih vrijednosti nijanse i zasićenosti.

Imajte na umu da su ovo zadani efekti, ali mogu se urediti tako da rade gotovo što god želite!

#### Što je _"trenutno odabrani Clip"_?

Kada pokrenete Clip, on zasvijetli kako bi pokazao da je aktivan. Oko njega se pojavljuje i bijeli obrub koji označava da je to trenutno _odabrani_ Clip. Kad god uključujete ili isključujete tipke zone ili prilagođavate postavke Clip, promjene se primjenjuju na _trenutno odabrani Clip._

{% hint style="info" %}
Da biste odabrali Clip bez njegova pokretanja, pritisnite tipku `Alt / Option` prije nego što pritisnete tipku za Clip. To je dobar način za prilagodbu njegovih zone i drugih postavki bez pokretanja.
{% endhint %}

### Panel Clip settings

Panel _Clip Settings_ koristite za uređivanje skaliranja, X/Y položaja i pristup moćnom sustavu odgode po zone.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global settings

Panel _Global Settings_ pronađite za prilagodbu globalnih postavki izlaza koje utječu na sav output kroz sve zone.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Uključite AUTO RESET kako bi se sve _Global settings_ automatski resetirale kad god se ne izvodi nijedan Clip.

### Timing

Gotovo svi laserski prikazi imaju neku vrstu glazbene podloge, pa je sustav Timing u Liberation temeljen na tempu u otkucajima u minuti. U panelu _Tempo Panel_ možete vidjeti prikaz vremena; svaki kvadrat predstavlja jedan otkucaj i možete vidjeti kako bljeskaju u ritmu.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Postoji više opcija sinkronizacije, uključujući MIDI clock i Ableton Link. Ako znate tempo glazbe, možete ga ručno prilagoditi pomoću klizača na zaslonu ili kotačića APC40 Tempo, ali možete ostati u ritmu s glazbom i pomoću sustava _Tap Tempo_\_.\_

#### Tap Tempo

_Tap Tempo_ je izraz koji se često koristi u glazbenim aplikacijama i omogućuje vam da tapkanjem u ritmu postavite tempo dok glazba svira. Možete koristiti tipku na zaslonu, iako se preporučuje tipka _T_ ili tipka _Tap Tempo_ na APC40 (ili čak nožni prekidač ako vam tako više odgovara).

Pritisnite tipku _R_ ili tipku _Metronome_ (APC40) kako biste tempo vratili na početak takta.

Pritisnite tipku _Y_ ili okrenite kotačić _Tempo_ (APC40) kako biste tempo zaokružili na cijeli broj. To može biti korisno za elektroničku glazbu, koja obično ima cijeli broj otkucaja u minuti.

### Organiziranje Clip Deck

Da biste premjestili Clip u Clip Deck, kliknite ga i povucite na novu poziciju. Tijekom povlačenja možete koristiti tipke pokazivača (ili kotačić/tipke za pomicanje na APC40) za pomicanje lijevo i desno.

Tijekom povlačenja držite tipku `Alt / Option` kako biste napravili kopiju.

Kliknite Clip uz `Alt / Option` da biste ga odabrali bez pokretanja.

Kliknite Clip uz `Alt / Option + Shift` za višestruki odabir ili kliknite i povucite izvan Clip kako biste odabrali metodom "laso".

Klik i povlačenje pomaknut će SVE odabrane Clips.

Da biste izbrisali jedan ili više Clips, odvucite ih izvan Clip Deck (pojavit će se ikona kante za smeće) ili upotrijebite tipku DELETE iz izbornika desnog klika za Clip.

### Panel Laser overview

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panel _Laser overview_ daje vam brz uvid u status lasera koji se trenutno izvode. Zeleni kvadrat s desne strane pokazuje da je laserski kontroler u redu. Ako postane narančast, imate povremene prekide, a ako postane crven, veza je prekinuta. Ako je siv, tada uopće nije povezan s kontrolerom.

Graf u sredini prikazuje povijest duljina frameova, a broj s desne strane trenutačnu brzinu frameova. Što je sadržaj složeniji, brzina frameova bit će sporija (tj. prikaz će više titrati). Sve ispod otprilike 25 fps počet će izgledati pomalo titravo.

### Povezivanje s laserima - panel Controller Assignment

Kliknite tipku _Assign Laser Controllers_ kako biste otvorili panel _Controller Assignment_. (Ovom panelu možete pristupiti i putem _View -> Controller Assignment_ u traci izbornika).

Ovdje možete odabrati koji laser output ide na koji laserski kontroler. Povucite i ispustite kontrolere s popisa s desne strane u utore s lijeve strane. Kontrolere možete preimenovati tako da odgovaraju laseru s kojim su upareni (upotrijebite tipku s ikonom olovke).

Za više pojedinosti pročitajte poglavlje [Dodjela kontrolera](setting-up/controller-assignment.md).

{% hint style="danger" %}
Prije nego što aktivirate bilo koji laser za izlaz, obavezno prođite kroz poglavlje [Postavljanje lasera](setting-up/setting-up-lasers.md).
{% endhint %}

### Panel Laser output

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Ovaj panel prikazuje postavke za _trenutno odabrani laser_ (predstavljen brojem na vrhu). Trenutno odabrani laser promijenite tipkom _tab_, pritiskom brojčane tipke, klikom na broj lasera u panelu _Laser Overview_ ili u _output view._

* **Number button** aktivira i deaktivira laser za izlaz; ako je crven, laser je aktiviran.
* **Brightness** prilagođava svjetlinu lasera neovisno o drugim laserima (i kombinira se s postavkom _global brightness_ - tj. ako su obje na 50%, vaš laser bit će na 25%).
* **Test Pattern** uključuje testni uzorak samo za ovaj laser (nadjačava globalnu postavku testnog uzorka)
* **Orientation** korigira lasere montirane bočno ili naopako.
* **Flip Horizontal and Flip Vertical** obrće izlaz lasera. Korisno za korekciju izlaza na laserima koji nisu dosljedno ožičeni.
* **Copy Laser Settings** otvara panel koji vam omogućuje kopiranje raznih postavki s ovog lasera na druge.

### Postavke skenera

Laseri za prikaz rade tako da jedan laserski snop pomiču iznimno brzo i uključuju ga i isključuju kako bi crtali oblike u zraku. Ono što vidite kao linije, oblike i slike zapravo je snop koji iscrtava putanje brže nego što ih vaše oči mogu pratiti.

Tok točaka su podaci koji laseru govore kamo se treba sljedeće pomaknuti i kada snop treba biti uključen ili isključen. U Liberation se Clips u stvarnom vremenu pretvaraju u taj tok točaka dok se šalju laserima.

Liberation vam daje detaljnu kontrolu nad načinom na koji se taj tok točaka generira, što vam omogućuje balansiranje glatkoće, svjetline i performansi za svaki laser.

{% hint style="info" %}
Ako ste navikli na stariji laserski softver koji se oslanja na unaprijed izračunate tokove točaka, ovaj pristup u početku može djelovati drukčije. Međutim, generiranje točaka u stvarnom vremenu omogućuje da se isti sadržaj različito optimizira za svaki laser. To olakšava rad s više lasera koji imaju različite brzine ili kvalitetu skenera, bez dupliciranja ili ponovne izrade sadržaja. Također održava datoteke Clip vrlo malima, zbog čega cijeli zadani Liberation Clip Deck zauzima samo nekoliko megabajta umjesto gigabajta.
{% endhint %}

Osnovne postavke skenera su:

* **Speed** je brzina skenera, tj. koliko se brzo laser kreće kako bi crtao oblike. To je ekvivalent podešavanju brzine točaka u tradicionalnom laserskom softveru, ali u Liberation možete mijenjati brzinu kretanja lasera _neovisno o brzini točaka._ Ovu postavku ne biste trebali morati podešavati.
* **Scanner sync** (ponekad poznato kao _blank shift, prethodno Colour Shift_) Skeneri pomiču laser vrlo brzo, ali promjena svjetline i boje obično nije sinkronizirana s kretanjem. To se vidi kao mali treperavi "repovi" svjetla na rubu beam elemenata i linija. Ovom prilagodbom uskladite kretanje i boju. Pogledajte [Laser Settings](setting-up/laser-settings.md)

Ostale napredne postavke skenera obrađene su u poglavlju [Napredno](advanced/).

### Zoning

Cijeli vodič za postavljanje lasera i zoning potražite ovdje: [Postavljanje lasera](setting-up/setting-up-lasers.md)
