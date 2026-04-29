---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Specifikacije skenera i Liberation

### Neuredna stvarnost specifikacija skenera

Brzine točaka i specifikacije skenera mogu biti pomalo zbunjujuće. Često ćete vidjeti specifikacije poput 30kpps @ 8º ili 50kpps @ 4º, ali nije uvijek očito što ti brojevi zapravo znače.

{% hint style="info" %}
Napomena — nisam stručnjak za hardver skenera, ali imam višegodišnje praktično iskustvo u tome kako postići da skeneri vrlo različite kvalitete izgledaju dobro putem softvera i generiranja toka točaka, umjesto podešavanjem hardvera. Ovo se temelji na tom iskustvu.
{% endhint %}

#### **Odakle dolaze ti brojevi**

Pojmovi poput “30K” i “50K” skraćenice su temeljene na načinu na koji se skeneri procjenjuju pomoću ILDA testnog uzorka pri tim brzinama točaka i pod određenim uvjetima.

Kada se za skener navede nešto poput: _30Kpps @ 8°_, to zapravo znači:

> “Ovaj skener može reproducirati ILDA testni uzorak pri 30.000 točaka/s pod kutom skeniranja od 8°, kada je pravilno podešen.”

To nije sveobuhvatno ni potpuno standardizirano mjerenje stvarnih performansi. Zapravo, izvorno uopće nije zamišljeno kao mjerilo performansi — koristilo se za **postupak podešavanja**. Pokrenete poznati uzorak pri fiksnoj brzini točaka (npr. 30.000 točaka/s) i podešavate prigušenje i pojačanje dok prikaz ne izgleda ispravno.

Ali to je i dalje najraširenija referenca koju imamo i može vam dati dobru predodžbu o kvaliteti skenera, barem kod pouzdanih proizvođača. Kod _manje pouzdanih_ proizvođača, međutim...

#### Ako želite testirati skenere prema njihovoj deklaraciji

{% hint style="danger" %}
**Ovo je napredna tehnika i možete oštetiti skenere ako niste oprezni. Ne preporučuje se osim ako znate što radite.**
{% endhint %}

Trebat ćete pronaći softver koji može poslati [ILDA testni uzorak](https://ilda.com/technical.htm?r=7950) na izlaz — mislim da bi LaserShowGen to možda mogao — i prilagoditi veličinu izlaza tako da odgovara navedenom kutu skeniranja (npr. 8°). Za savjete o analizi izlaza pogledajte ILDA dokumentaciju.

#### Zašto to možda nije dobro mjerilo

Prije svega, testni uzorak može izgledati neispravno čak i ako su skeneri dobri, jer nisu podešeni na način optimiziran za taj uzorak.

Može biti koristan opći pokazatelj za razlikovanje “dobrih” i “loših” skenera, ali proizvođači se ponekad prilično slobodno odnose prema tim specifikacijama.

#### Kako onda odabrati dobar skener?

Mislim da je najvažnije provjeriti da ih proizvodi pouzdan proizvođač. Skupi vrhunski proizvođači skenera poput Cambridge Technology (CT), Eye Magic (EMS) i ScannerMAX (podružnica Pangolina) uvijek su dobar izbor i s njima nećete pogriješiti. Ali kada par skenera košta oko 1000 USD, mnogima koji tek počinju to je skuplje od samih lasera!

Zato sam uglavnom koristio kineske proizvođače. Skeneri Dragon Tiger (DT) pristojni su i cjenovno pristupačni, a mislim da ih koristi i LightSpace. Mnogi drugi proizvođači (uključujući OPT i Able u nekim modelima) također koriste sustave temeljene na DT skenerima.

Phenix Technology (PT) općenito je niža klasa, ali iskreno, za većinu stvari vjerojatno su sasvim u redu.

**Ako vaši skeneri nemaju oznaku proizvođača, tada biste se vjerojatno trebali zabrinuti za kvalitetu!**

#### Kako Liberation pomaže

Prije svega, za većinu stvari ne trebaju vam stvarno skupi skeneri! Pristupačni DT od 30kpps, pa čak i PT, bit će sasvim u redu. Zadane postavke skenera namjerno su konzervativne i u najvećem dijelu _ne biste ih trebali morati podešavati_ (osim postavke _Scanner sync_).

Čak i ako imate bolje skenere, nema smisla opterećivati ih više nego što je potrebno. Time ćete im znatno produljiti vijek trajanja.

#### Što je “tok točaka”?

Vjerojatno ste već čuli taj pojam — to je način na koji kontroliramo putanju skenera.

Tok točaka popis je X/Y položaja, od kojih svaki ima boju. Da biste nacrtali, primjerice, bijelu liniju, šaljete niz točaka duž te linije, sve postavljene na bijelu boju. Skeneri se zatim pomiču od točke do točke fiksnom brzinom — brzinom točaka u sekundi (PPS) — i zraka iscrtava oblik.

#### Kako to funkcionira u tradicionalnom laserskom softveru

Tradicionalni laserski softver sprema tok točaka za svaki cue. Za animirane cue stavke to obično znači zaseban tok točaka za svaki frame. Ključna je stvar da je sve potpuno unaprijed određeno. Zbog toga povećanje brzine točaka čini da se skeneri brže kreću kroz iste unaprijed definirane podatke.

{% hint style="info" %}
Za stariji softver takav je pristup bio nužan — računala jednostavno nisu bila dovoljno brza da generiraju tokove točaka u stvarnom vremenu. Zato obično postoji zaseban uređivač cueova, koji se koristi za unaprijed generiranje podataka za svaki frame animacije.

To također objašnjava zašto sadržaj može zauzimati gigabajte prostora. U praksi spremate velike, nekomprimirane valne oblike pri prilično visokim brzinama uzorkovanja.
{% endhint %}

#### Zašto je “brzina točaka” manje značajna u Liberation

Liberation generira tok točaka u stvarnom vremenu, što nam daje veliku fleksibilnost. Obratite pozornost na postavku "Scanner speed" u panelu Laser Settings. Ona nam omogućuje ubrzavanje i usporavanje skenera, ali važno je da **ne** mijenja osnovnu brzinu točaka (PPS).

#### Čekaj, što? Kako?

Znam, isprva zvuči čudno.

Budući da Liberation generira tok točaka u stvarnom vremenu, može prilagoditi taj tok točaka. Što su točke više razmaknute, skeneri se kreću brže. Što su bliže jedna drugoj, skeneri se kreću sporije.

{% hint style="info" %}
U novijim verzijama Liberation, stvarna _brzina točaka_ (u naprednim postavkama) uopće ne utječe na brzinu skenera. Umjesto toga, renderer prilagođava raspodjelu točaka tako da odgovara odabranoj brzini točaka, a pritom zadržava nepromijenjeno kretanje skenera.

To utječe na “rezoluciju” putanje točaka, ali to je uglavnom važno za grafiku (i može pomoći pri finijem podešavanju postavke _Scanner sync_).
{% endhint %}

#### Odlično! Što sve to zapravo znači?

Dobro pitanje. Evo mojih savjeta:

* Izbjegavajte skenere bez oznake proizvođača. Ako možete nabaviti brže skenere, učinite to — minimum je 30KPPS.
* U većini slučajeva DT30 skeneri su sasvim u redu, a PT30 skeneri vjerojatno su OK u jeftinijim laserima.
* Ako radite grafiku, u većini slučajeva više lasera bit će bolje od bržih skenera.
* Kada dođete do naprednijih sustava, bilo koji od etabliranih vrhunskih brendova bit će dobar izbor.
* Ako možete nabaviti samo najjeftinije skenere bez oznake proizvođača, zadane postavke u Liberation prilično su konzervativne i vjerojatno ćete dobiti OK rezultate za osnovni rad sa zrakama. Ako sustav ima poteškoća, smanjite postavku **Speed** (ali nemojte mijenjati brzinu točaka!).

#### A ILDA testni uzorak?

…i dalje je vrlo koristan kao alat za kalibraciju i referencu, ali nikada nije bio zamišljen kao sveobuhvatno mjerilo performansi i proizvođači ga mogu zloupotrebljavati ili tumačiti prilično labavo.
