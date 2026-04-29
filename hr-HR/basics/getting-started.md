# ✅ Vodič za brzi početak

## Uvod

Dobro došli u **Liberation** — novu generaciju softvera za laserske predstave.

Liberation je snažan i složen moderan softver; izgrađen je na temeljima upotrebljivosti i pouzdanosti kako bi vam dao slobodu da izrazite svoju kreativnost. Brz je, učinkovit i ugodan za rad; slijedite ovaj _Vodič za brzi početak_ i bit ćete spremni za rad u vrlo kratkom vremenu!

### Upravljanje laserima

Liberation je dovoljno fleksibilan da možete postaviti lasere i vizualizirati ih čak i bez ijednog stvarnog lasera spojenog na sustav. Zatim, kada budete spremni za rad, svaki izlaz možete jednostavno dodijeliti laserskom kontroleru.

{% hint style="info" %}
U Liberation možete postaviti i vizualizirati koliko god lasera želite; licencne razine (Hobbyist, Pro itd.) ograničavaju samo broj lasera koje možete _aktivirati za izlaz_. To znači da laserske predstave sa 100 lasera možete dizajnirati čak i s besplatnom licencom. Nadogradnja vam treba tek kada ih stvarno želite pokrenuti na pravim laserima.
{% endhint %}

Zadana postavka ima 8 lasera raspoređenih vodoravno, ali to možete prilagoditi kako god želite. Vjerojatno je najbolje zadržati ovu zadanu postavku dok se upoznajete sa softverom, a poslije je možete prilagoditi svojoj hardverskoj konfiguraciji. (Pogledajte [Postavljanje projekta](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Važno: Prije nego što aktivirate bilo koji laser za izlaz, provjerite razumijete li povezane rizike i pažljivo prođite poglavlje [Postavljanje lasera](../setting-up/setting-up-lasers.md).
{% endhint %}

## Pregled softvera

### Sigurnosno isključivanje

Kad god radite s laserima, pri ruci morate imati **hardversko tipkalo za hitno zaustavljanje** (pogledajte [Tipkala za hitno zaustavljanje i sigurnosne blokade](../hardware/emergency-stop-interlocks.md)), ali ako želite manje hitno deaktivirati sve izlaze, možete upotrijebiti gumb _**DISARM ALL**_ ili tipku `Escape` (ili tipku _**SESSION**_ na APC40). Globalnu svjetlinu možete smanjiti i pomoću klizača na zaslonu ili glavnog fadera na APC40.

### Klizači

U cijelom sučelju Liberation postoje razni klizači i kontrole.

{% hint style="info" %}
Kliknite klizač uz `Cmd / Ctrl` ako trebate upisati novu vrijednost i želite precizniju kontrolu od one koju klizač omogućuje.
{% endhint %}

### Tipkovnički prečaci

Cjelovit popis tipkovničkih prečaca nalazi se ovdje: [Tipkovnički prečaci](../reference/keyboard-shortcuts.md)

### Raspored zaslona

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Niste sigurni čemu služi određeni gumb? Zadržite pokazivač miša iznad njega i prikazat će se opis!
{% endhint %}

#### Izbornik

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

U izborniku se nalaze sve opcije za uvoz i izvoz datoteka te otvaranje panela. Ovdje se nalazi i opcija za autorizaciju računala vašom pretplatom (u _Liberation -> Authorise/Deauthorise this computer_).

#### Traka s ikonama

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Ovdje se nalaze uobičajeni zadaci, kao što su aktiviranje i deaktiviranje svih lasera za izlaz, Global Brightness, Test Pattern te prebacivanje između prikaza 3D, Canvas i Output.

### Prikazi

Veliko područje u gornjem lijevom dijelu zaslona može prikazivati jedan od 3 glavna prikaza: **3D**, **CANVAS** i **OUTPUT.** Prebacujte se između njih pomoću gumba na traci s ikonama (ili tipkom `Tab` za prebacivanje između prikaza 3D i Output view, nakon čega možete nastaviti prelaziti redom kroz svaki laserski izlaz).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view prikazuje kako će vaši laseri izgledati i može se konfigurirati tako da odgovara vašoj stvarnoj postavi lasera. Kliknite i povucite za rotiranje kamere, a kotačićem miša pomičite pogled naprijed i natrag. Mnoge druge opcije nalaze se u panelu _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Pogledajte [3D Visualiser](../setting-up/3d-visualiser.md).

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view služi za konfiguriranje zone i masks za svaki laser. (Obratite pozornost na veliki broj u gornjem lijevom kutu kako biste lako vidjeli na kojem ste laseru!)

Ovaj prikaz predstavlja cjelokupan izlaz tog lasera i položaj svake zone unutar njega. Prema zadanim postavkama postoji samo jedan zone po laseru, ali možete dodati onoliko stavki zone koliko je razumno praktično, a sve ćete ih vidjeti u ovom prikazu.

{% hint style="info" %}
**Što je zone?**

Zone je prostor unutar laserskog izlaza u koji možete usmjeriti laserski sadržaj. Na jednom laseru može postojati više takvih prostora. Najjednostavnija vrsta je _beam_ zone, ali postoje i _canvas_ zone te _DMX_ zone. U ovom ćemo se vodiču uglavnom usredotočiti na beam zone, koje se obično upotrebljavaju za stvaranje atmosferskih snopova u zraku.
{% endhint %}

Laser koji želite uređivati možete odabrati na jedan od sljedećih načina:

* numeriranim gumbima na traci pri vrhu
* pritiskom brojčane tipke za željeni laser _(tipke 1–9_ \_)\_
* tipkom `Tab`, za prelazak s jednog lasera na sljedeći

Dodajte novi laser u postavu pritiskom gumba _+_. (U panelu _Laser Overview_ nalazi se i gumb _ADD LASER_)

Izbrišite laser iz postave pritiskom crvenog gumba ⊖ u panelu _Laser Overview_.

Prikaz možete povećavati i smanjivati kotačićem miša, a klikom i povlačenjem na bilo kojem mjestu gdje nema zone možete pomicati prikaz.

Kliknite zone da biste ga odabrali, a zatim mišem prilagodite njegove kutne točke. Dok povlačite kut, držite tipku `Alt / Option` ako želite da promjena ne bude jednolika. Desnom tipkom miša kliknite zone da biste vidjeli dodatne opcije, uključujući promjenu vrste zone.

S lijeve strane nalazi se traka s nizom ikonskih gumba; zadržite pokazivač iznad bilo kojeg gumba da biste vidjeli opis njegove funkcije. Gumbi ovdje omogućuju dodavanje beam zone, canvas zone i masks. Tu su i opcije za postavljanje testnog uzorka samo za ovaj laser, zajedno s postavkama mreže i prianjanja.

Više pojedinosti potražite u odjeljku [Output view](../output-view/).

#### Canvas

Sustav Canvas uglavnom se upotrebljava za grafiku i arhitektonsko mapiranje. Složene slike možete rasporediti preko više lasera i perspektivno ispraviti svaki dio. Pogledajte [Grafika i sustav Canvas](../graphics-and-the-canvas-system/).

### APC40 MIDI kontroler

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Iako je Liberation moguće upravljati mišem i tipkovnicom, mnogo je bolje upotrebljavati APC40 MIDI kontrolno sučelje (Mark 2 je najbolji izbor, ali radi i Mark 1).

Pogledajte i: [Referenca za APC40](../reference/apc40-reference.md)

Sada smo implementirali i podršku za APC Mini Mark 2 i MIDI Fighter Twister, a dodatni kontroleri su u razvoju. Ipak, APC40 Mark 2 najbolja je opcija u većini slučajeva.&#x20;

### Clips i efekti

{% hint style="info" %}
**Što je Clip?**

Clip je spremnik za bilo koji laserski sadržaj u Liberation. Clips mogu sadržavati snopove ili grafičke animacije i obično se izvode u petlji. Mogu se usmjeriti u bilo koji zone (ili _Canvas target area_) i pokreću se pomoću gumba za Clip unutar Clip Deck.
{% endhint %}

#### Pregled Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Ova mreža naziva se _Clip Deck_ i u njoj se pohranjuju svi laserski Clips. Osmišljena je tako da se izravno preslikava na mrežu gumba 8 x 5 na vašem APC40.

**Kretanje kroz Clip Deck.**

Clip Deck možete pomicati ulijevo i udesno na sljedeće načine:

* tipkama sa strelicama lijevo i desno. Dodajte `Cmd / Ctrl` za pomicanje za jednu cijelu stranicu odjednom.
* dodirnom plohom: povlačenjem prstom
* mišem: ako miš podržava vodoravno pomicanje, možete ga upotrijebiti dok je pokazivač iznad Clip Deck
* kotačićem za pomicanje na APC40
* gumbima APC40 _<- DEVICE ->_

Za lakše snalaženje, pri vrhu se nalazi mali vizualni prikaz Clip Deck. Pogledajte i [Clips i Clip Deck](../clips/)

#### Pokretanje i zaustavljanje Clips

Pritisnite gumb za Clip (mišem ili na APC40) da biste pokrenuli Clip. Pritisnite ga ponovno da biste ga zaustavili. Kada pokrenete Clip, svi drugi Clips iste boje automatski će se zaustaviti, osim ako držite _shift_.

Neki Clips bit će u načinu _Flash mode_ (prema zadanim postavkama crveni), pa će se zaustaviti čim otpustite gumb za Clip.

Gumb _STOP_ zaustavlja sve Clips koji se trenutačno izvode.

#### Postavljanje izlaznih zone za Clip

Ispod gumba za Clips vidjet ćete gumbe za zone; prema zadanim postavkama to su beam zone 1 do 8 (_BEAM 1_, _BEAM 2_ itd.). Gumbi za zone svijetle kako bi pokazali koji su zone dodijeljeni trenutačno odabranom Clip.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Dva reda ispod gumba za zone vidjet ćete gumbe za X/Y zrcaljenje; uključite ih ili isključite kako biste Clip zrcalili vodoravno i okomito.

{% hint style="info" %}
Imajte na umu da su ove dodjele zone i postavke X/Y zrcaljenja povezane sa samim Clip; ostat će zapamćene sljedeći put kada pokrenete taj Clip. To nisu globalne postavke.
{% endhint %}

Desnom tipkom miša kliknite Clip da biste uredili dodatne postavke za taj Clip. Pogledajte i [Postavke za Clip](../clips/clip-settings.md)

### Grupe

Primijetit ćete da svaki Clip ima obojeni obrub, a ta boja označava kojoj _grupi_ pripada. Gumbi za Clips na APC40 također svijetle tom bojom.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Grupa 1</td><td>Cijan</td></tr><tr><td>Grupa 2</td><td>Narančasta</td></tr><tr><td>Grupa 3</td><td>Crvena</td></tr><tr><td>Grupa 4</td><td>Indigo</td></tr><tr><td>Grupa 5</td><td>Zelena</td></tr></tbody></table>

Sustav grupa vrlo je fleksibilan i omogućuje vam da:

* zadržite Clips iz jedne grupe aktivnima dok uključujete i isključujete grupe u drugoj
* brzo dodijelite zone i X/Y zrcaljenje svim Clips unutar grupe
* postavite _Flash mode_ za Clip (Grupa 3 prema zadanim je postavkama postavljena na _Flash mode_)

Grupe imaju i postavke za prijelaz na početku i kraju, koje njihovi Clips mogu naslijediti ili nadjačati.

Grupu kojoj Clip pripada možete dodijeliti pomoću gumba u izborniku desnog klika, ili na APC40 tako da pritisnete gumb grupe i, _dok ga još držite pritisnutim_, pritisnete gumbe za Clips.

Promjena postavki zone za sve Clips unutar grupe

Na APC40 pritisnite gumb grupe, zatim _dok ga još držite_, upotrijebite gumbe za zone i X/Y za uključivanje ili isključivanje postavki zone za sve Clips unutar te grupe.

Pogledajte i [Clip grupe](../clips/groups.md)

### Efekti

Sustav efekata u Liberation snažan je i prilagodljiv način za promjenu izlaza iz Clip u stvarnom vremenu. Zadani gumbi efekata 1–8 nalaze se ispod gumba za zone.

#### Primjena efekta

Pritisnite gumb efekta da biste ga uključili ili isključili, ili još bolje, upotrijebite klizače 1–8 na APC40 za postupno uvođenje i smanjivanje efekata.

#### Parametri efekata

Upotrijebite rotacijske kontrolere 1–8\* za podešavanje _parametra_ svakog efekta. (Možete i kliknuti desnom tipkom miša za podešavanje razine i parametra.) Promjena parametra radi različite stvari ovisno o tome kako je efekt postavljen. U nastavku je popis zadanih efekata.

{% hint style="info" %}
Mali brojevi koje vidite na gumbima efekata odnose se na _razinu_ i _parametar_ efekta. _Razinom_ se upravlja faderom na APC40 ili klikom i povlačenjem po gumbu. Parametar se podešava rotacijskim kontrolerima na APC40 ili desnim klikom mišem.
{% endhint %}

_\*Rotacijski kontroleri 1–8 nalaze se uz gornji rub APC40 Mk2 i gore desno na Mk1. Pogledajte i:_ [Referenca za APC40](../reference/apc40-reference.md)

#### Zadani efekti

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Primjenjuje kaotično kretanje na izlaz iz Clip. Parametar podešava količinu/brzinu kaosa.
2. **Sine wave** :\
   Izobličuje sav sadržaj preko pokretnog sinusnog vala. Parametar podešava valnu duljinu.
3. **Rotation** :\
   Okreće sve elemente. Parametar podešava brzinu okretanja.
4. **Horizontal flip** :\
   Vodoravno sabija i rasteže sve elemente. Parametar podešava brzinu.
5. **Scale** :\
   Ponavljano skalira sve elemente od pune veličine do nule. Parametar podešava brzinu.
6. **Hue** :\
   Mijenja nijansu svega, ali ne mijenja zasićenost (tj. sve što je bijelo ostaje bijelo). Parametar podešava nijansu.
7. **Saturation and hue** :\
   Mijenja nijansu svega i ujedno potpuno zasićuje boju (tj. sve što je bijelo mijenja se u tu boju). Parametar podešava nijansu.
8. **Flash** :\
   Ponavljano bljeska svjetlinom svega od pune vrijednosti do nule. Parametar podešava brzinu bljeskanja.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

U donjem redu nalazi se još 16 efekata boje za primjenu unaprijed postavljenih vrijednosti nijanse i zasićenosti.

Imajte na umu da su to zadani efekti, ali mogu se urediti tako da rade gotovo što god želite!

#### Što je _„trenutačno odabrani Clip”_?

Kada pokrenete Clip, on zasvijetli kako bi pokazao da je aktivan. Oko njega se pojavljuje i bijeli obrub, koji označava da je to trenutačno _odabrani_ Clip. Kad god uključujete ili isključujete gumbe za zone ili podešavate postavke za Clip, one se primjenjuju na _trenutačno odabrani Clip._

{% hint style="info" %}
Da biste odabrali Clip bez njegova pokretanja, pritisnite tipku `Alt / Option` prije nego što pritisnete gumb za Clip. To je dobar način za podešavanje njegovih zone i drugih postavki bez pokretanja.
{% endhint %}

### Panel Clip Settings

Upotrijebite panel _Clip Settings_ za uređivanje skaliranja, X/Y položaja i pristup naprednom sustavu kašnjenja za zone.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

Pronađite panel _Global Settings_ da biste podesili globalne postavke izlaza koje utječu na sav izlaz preko svih zone.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Uključite AUTO RESET kako bi se sve _Global settings_ automatski resetirale kad god se ne izvodi nijedan Clip.&#x20;

### Vremenska sinkronizacija

Gotovo svi laserski prikazi imaju neku vrstu glazbene podloge, pa se sustav vremenske sinkronizacije u Liberation temelji na tempu izraženom u otkucajima u minuti. U panelu _Tempo Panel_ možete vidjeti prikaz vremena; svaki kvadrat predstavlja jedan otkucaj i vidjet ćete kako trepere u ritmu.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Dostupno je više opcija sinkronizacije, uključujući MIDI clock i Ableton Link. Ako znate tempo glazbe, možete ga ručno podesiti pomoću klizača na zaslonu ili gumba Tempo na APC40, ali s glazbom se možete uskladiti i pomoću sustava _Tap Tempo_\_.\_

#### Tap Tempo

_Tap Tempo_ je pojam koji se često upotrebljava u glazbenim aplikacijama, a omogućuje vam da kucate u ritmu kako biste postavili tempo dok glazba svira. Možete upotrijebiti gumb na zaslonu, iako se preporučuje tipka _T_ ili gumb _Tap Tempo_ na APC40 (ili čak nožni prekidač, ako vam tako više odgovara).

Pritisnite tipku _R_ ili gumb _Metronome_ (APC40) za resetiranje tempa na početak takta.

Pritisnite tipku _Y_ ili okrenite gumb _Tempo_ (APC40) kako biste tempo zaokružili na cijeli broj. To može biti korisno za elektroničku glazbu, koja često ima cijeli broj otkucaja u minuti.

### Organiziranje Clip Deck

Da biste premjestili Clip u Clip Deck, kliknite ga i povucite na novi položaj. Dok povlačite, možete upotrijebiti tipke sa strelicama (ili kotačić/gumbe za pomicanje na APC40) za pomicanje ulijevo i udesno.

Držite tipku `Alt / Option` dok povlačite kako biste napravili kopiju.

Kliknite Clip uz `Alt / Option` da biste ga odabrali bez pokretanja.

Kliknite Clip uz `Alt / Option + Shift` za višestruki odabir ili kliknite i povucite izvan Clip da biste odabrali više njih „lasom”.&#x20;

Klik i povlačenje povući će SVE odabrane Clips.

Da biste izbrisali jedan ili više Clips, povucite ih izvan Clip Deck (pojavit će se ikona koša za smeće) ili upotrijebite gumb DELETE iz izbornika desnog klika za Clip.

### Panel Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panel _Laser Overview_ daje vam brz uvid u status lasera koji se trenutačno izvode. Zeleni kvadrat s desne strane pokazuje da laserski kontroler radi ispravno. Ako postane narančast, dolazi do povremenih prekida, a ako je crven, veza je prekinuta. Ako je siv, laser uopće nije povezan s kontrolerom.&#x20;

Graf u sredini prikazuje povijest trajanja okvira, a broj s desne strane trenutačnu brzinu okvira. Što je sadržaj složeniji, brzina okvira bit će manja (tj. prikaz će više treperiti). Sve ispod otprilike 25 fps počet će izgledati pomalo treperavo.&#x20;

### Povezivanje s laserima — panel Controller Assignment

Kliknite gumb _Assign Laser Controllers_ da biste otvorili panel _Controller Assignment_. (Tom panelu možete pristupiti i preko _View -> Controller Assignment_ na traci izbornika.)

Ovdje možete odabrati koji laserski izlazi idu na koje laserske kontrolere. Povucite i ispustite kontrolere s popisa s desne strane u utore s lijeve strane. Kontrolere možete preimenovati tako da odgovaraju laseru s kojim su upareni (upotrijebite gumb s ikonom olovke).

Za više pojedinosti pročitajte poglavlje [Dodjela kontrolera](../setting-up/controller-assignment.md).

{% hint style="danger" %}
Prije nego što aktivirate bilo koji laser za izlaz, obavezno prođite poglavlje [Postavljanje lasera](../setting-up/setting-up-lasers.md).
{% endhint %}

### Panel Laser Settings

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Ovaj panel prikazuje postavke za _trenutačno odabrani laser_ (označen brojem pri vrhu). Trenutačno odabrani laser promijenite tipkom _tab_, pritiskom brojčane tipke, klikom na broj lasera u panelu _Laser Overview_ ili u _Output view._

* **Number button** aktivira ili deaktivira laser za izlaz; ako je crven, laser je aktiviran.
* **Brightness** podešava svjetlinu lasera neovisno o drugim laserima (kombinira se s postavkom _global brightness_ — npr. ako su obje vrijednosti 50%, vaš laser bit će na 25%).
* **Test Pattern** uključuje testni uzorak samo za ovaj laser (nadjačava globalnu postavku testnog uzorka)
* **Orientation** ispravlja lasere montirane bočno ili naopako.
* **Flip Horizontal and Flip Vertical** zrcali izlaz lasera. Korisno za korekciju izlaza na laserima s nedosljednim ožičenjem.
* **Copy Laser Settings** otvara panel koji vam omogućuje kopiranje raznih postavki s ovog lasera na druge.

### Postavke skenera

Laseri za prikaz rade tako da jedan laserski snop pomiču iznimno brzo i pale ga i gase kako bi crtali oblike u zraku. Ono što vidite kao linije, oblike i slike zapravo je snop koji iscrtava putanje brže nego što ih vaše oči mogu pratiti.

Tok točaka podaci su koji laseru govore kamo se sljedeće treba pomaknuti i kada snop treba biti uključen ili isključen. U Liberation se Clips pretvaraju u taj tok točaka u stvarnom vremenu dok se šalju laserima.

Liberation vam daje detaljnu kontrolu nad načinom generiranja tog toka točaka, što vam omogućuje da za svaki laser uravnotežite glatkoću, svjetlinu i performanse.

{% hint style="info" %}
Ako ste navikli na stariji laserski softver koji se oslanja na unaprijed izračunate tokove točaka, ovaj pristup u početku može djelovati drukčije. Međutim, generiranje točaka u stvarnom vremenu omogućuje da se isti sadržaj različito optimizira za svaki laser. To olakšava rad s više lasera koji imaju različite brzine ili kvalitetu skenera, bez dupliciranja ili ponovne izrade sadržaja. Također održava datoteke za Clips vrlo malima, zbog čega cijeli zadani Clip Deck u Liberation zauzima samo nekoliko megabajta, a ne gigabajte.
{% endhint %}

Osnovne postavke skenera su:

* **Speed** je brzina skenera, tj. koliko se brzo laser kreće dok crta oblike. To je ekvivalent podešavanju brzine točaka u tradicionalnom laserskom softveru, ali u Liberation možete mijenjati brzinu kretanja lasera _neovisno o brzini točaka._ Ovo obično ne biste trebali podešavati.
* **Scanner sync** (ponekad poznato kao _blank shift_, prije _Colour Shift_) Skeneri pomiču laser vrlo brzo, ali promjena svjetline i boje obično nije sinkronizirana s kretanjem. To se vidi kao mali treperavi „repovi” svjetla na rubovima snopova i linija. Upotrijebite ovu postavku kako biste uskladili kretanje i boju. Pogledajte [Laser Settings](../setting-up/laser-settings/)

Ostale napredne postavke skenera obrađene su u poglavlju [Napredno](../advanced/).

### Zoning

Cjelovit vodič za postavljanje i zoning lasera potražite ovdje: [Postavljanje lasera](../setting-up/setting-up-lasers.md)
