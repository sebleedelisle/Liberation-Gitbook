---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Pika-aloitusopas

## Johdanto

Tervetuloa käyttämään **Liberationia** – seuraavan sukupolven laser-show-ohjelmistoa.

Liberation on tehokas ja monipuolinen moderni ohjelmisto. Se perustuu käytettävyyteen ja luotettavuuteen, jotta voit toteuttaa luovuuttasi vapaasti. Se on nopea, tehokas ja sujuva. Seuraa tätä _pika-aloitusopasta_, niin pääset alkuun hetkessä!

### Lasereiden hallinta

Liberation on niin joustava, että voit määrittää ja visualisoida lasereita ilman, että yhtään oikeaa laseria on kytketty. Kun olet valmis, voit liittää jokaisen lähdön saumattomasti laserohjaimeen.

{% hint style="info" %}
Voit määrittää ja visualisoida Liberationissa niin monta laseria kuin haluat. Lisenssitasot (Hobbyist, Pro jne.) rajoittavat vain sitä, montako laseria voit _aktivoida käyttöön._ Tämä tarkoittaa, että voit suunnitella 100 laserin esityksiä myös ilmaisella lisenssillä. Päivitys tarvitaan vasta, kun esitys ajetaan oikeilla lasereilla.
{% endhint %}

Oletuksena käytössä on 8 laseria vaakasuunnassa, mutta voit muokata tämän haluamaksesi. Alkuun on yleensä parasta pitää oletusasetukset käytössä, kun tutustut ohjelmistoon. Myöhemmin voit säätää ne vastaamaan omaa laitteistoasi. (Katso [Projektin määrittäminen](setting-up/setting-up-your-project.md))

{% hint style="warning" %}
Tärkeää: Ennen kuin aktivoit yhtään laseria, varmista että ymmärrät niihin liittyvät riskit ja käy huolellisesti läpi luku [Lasereiden käyttöönoton prosessin yleiskatsaus](setting-up/setting-up-lasers.md).
{% endhint %}

## Ohjelmiston yleiskuva

### Turvakatkaisu

Aina kun käytät lasereita, sinulla on oltava käytettävissä **fyysinen hätäpysäytyspainike** (katso [Hätäpysäytys / interlockit](hardware/emergency-stop-interlocks.md)). Jos haluat poistaa kaiken käytöstä vähemmän kiireellisesti, voit käyttää _**DISARM ALL**_ -painiketta tai `Escape`-näppäintä (tai APC40:n _**SESSION**_-näppäintä). Voit myös vähentää yleistä kirkkautta näytön liukusäätimellä tai APC40:n pääliukusäätimellä.

### Liukusäätimet

Liberationissa on eri puolilla erilaisia liukusäätimiä ja ohjaimia.

{% hint style="info" %}
`Cmd / Ctrl`-klikkaa liukusäädintä, jos haluat kirjoittaa arvon käsin ja tarvitset tarkempaa säätöä kuin liukusäädin tarjoaa.
{% endhint %}

### Pikanäppäimet

Täydellinen pikanäppäinluettelo löytyy täältä: [Pikanäppäimet](reference/keyboard-shortcuts.md)

### Näytön asettelu

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Etkö ole varma, mitä jokin painike tekee? Vie hiiri painikkeen päälle, niin näet kuvauksen!
{% endhint %}

#### Valikko

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Valikosta löydät kaikki tiedostojen tuonti- ja vientitoiminnot sekä paneelien avaamisen. Täältä löytyy myös tietokoneen valtuutus tilauksellesi (_Liberation -> Authorise/Deauthorise this computer_).

#### Kuvakepalkki

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Täältä löytyvät yleiset toiminnot, kuten kaikkien lasereiden aktivointi ja poiskytkentä, yleinen kirkkaus, testikuvio sekä 3D-, Canvas- ja Output-näkymien välillä vaihtaminen.

### Näkymät

Näytön vasemman yläosan suuri alue voi olla jokin kolmesta päänäkymästä: **3D**, **CANVAS** tai **OUTPUT.** Vaihda näkymää kuvakepalkin painikkeilla (tai vaihda 3D- ja OUTPUT-näkymien välillä `Tab`-näppäimellä ja jatka sen jälkeen välilehtien tapaan kunkin laserulostulon läpi).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D-näkymä

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D-näkymä näyttää, miltä laserisi näyttävät, ja sen voi määrittää vastaamaan omaa laserjärjestelmääsi. Kierrä kameraa klikkaamalla ja vetämällä. Siirry eteen- ja taaksepäin hiiren rullalla. Lisää asetuksia löytyy _3D Visualiser settings_ -paneelista (_View -> 3D Visualiser Settings_). Katso [3D Visualiser](setting-up/3d-visualiser.md).

#### Output-näkymä

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output-näkymää käytetään kunkin laserin alueiden ja maskien määrittämiseen. (Huomaa vasemman yläkulman suuri numero, josta näet helposti, mitä laseria käsittelet!)

Tämä näkymä esittää kyseisen laserin koko ulostulon ja sen, missä kukin alue sijaitsee sen sisällä. Oletuksena laseria kohti on vain yksi alue, mutta voit lisätä alueita niin monta kuin käytännössä on järkevää. Näet ne kaikki tässä näkymässä.

{% hint style="info" %}
**Mikä on alue?**

Alue on laserin ulostulon sisällä oleva tila, johon voit ohjata lasersisältöä. Yhdellä laserilla voi olla useita alueita. Yksinkertaisin aluetyyppi on _beam_-alue, mutta käytössä on myös _canvas_-alueita ja _DMX_-alueita. Tässä oppaassa keskitymme pääasiassa beam-alueisiin, joita käytetään yleensä ilmassa näkyvien tunnelmallisten säde-efektien luomiseen.
{% endhint %}

Voit valita muokattavan laserin jollakin seuraavista tavoista:

* yläpalkin numeroiduilla painikkeilla
* painamalla haluamasi laserin numeronäppäintä _(1–9)_
* selaamalla lasereita `Tab`-näppäimellä

Lisää uusi laser järjestelmään painamalla _+_-painiketta. (_Laser Overview_ -paneelissa on myös _ADD LASER_ -painike.)

Poista laser järjestelmästä painamalla punaista ⊖-painiketta _Laser Overview_ -paneelissa.

Voit lähentää ja loitontaa hiiren rullalla. Siirrä näkymää klikkaamalla ja vetämällä kohdasta, jossa ei ole aluetta.

Valitse alue klikkaamalla sitä ja säädä sitten sen kulmapisteitä hiirellä. Pidä `Alt / Option`-näppäintä painettuna kulmaa vetäessäsi, jos haluat tehdä muutoksesta epäyhtenäisen. Avaa lisäasetukset, kuten aluetyypin vaihtaminen, klikkaamalla aluetta hiiren oikealla painikkeella.

Vasemmassa reunassa on palkki, jossa on sarja kuvakepainikkeita. Vie hiiri minkä tahansa painikkeen päälle nähdäksesi, mitä se tekee. Näillä painikkeilla voit lisätä beam-alueita, canvas-alueita ja maskeja. Lisäksi käytettävissä on asetuksia, joilla voit määrittää testikuvion vain tälle laserille sekä säätää ruudukkoa ja kohdistumista.

Lisätietoja: [Output-näkymä](output-view/).

#### Canvas

Canvas-järjestelmää käytetään pääasiassa grafiikkaan ja arkkitehtoniseen mappaukseen. Voit jakaa monimutkaisia kuvia useille lasereille ja perspektiivikorjata jokaisen osan. Katso [Grafiikka ja Canvas-järjestelmä](graphics-and-the-canvas-system/).

### APC40 MIDI -ohjain

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Liberationia voi ohjata hiirellä ja näppäimistöllä, mutta APC40 MIDI -ohjain tekee käytöstä huomattavasti parempaa (Mark 2 on paras vaihtoehto, mutta myös Mark 1 toimii).

Katso myös: [APC40-viite](reference/apc40-reference.md)

Olemme nyt lisänneet tuen myös APC Mini Mark 2:lle ja MIDI Fighter Twisterille, ja lisää ohjaimia on kehitteillä. APC40 Mark 2 on kuitenkin useimmissa tilanteissa paras vaihtoehto.

### Clipit ja efektit

{% hint style="info" %}
**Mikä on clip?**

Clip on Liberationissa säiliö mille tahansa lasersisällölle. Clipit voivat sisältää säteitä tai graafisia animaatioita, ja ne ovat yleensä luuppaavia jaksoja. Ne voidaan ohjata mille tahansa alueelle (tai _Canvas target area_ -kohdealueelle), ja ne käynnistetään clip deckin clip-painikkeilla.
{% endhint %}

#### Clip deckin yleiskuva

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Tämä ruudukko tunnetaan nimellä _clip deck_, ja siihen tallennetaan kaikki laser-clipit. Se on suunniteltu vastaamaan suoraan APC40:n 8 x 5 -painikeruudukkoa.

**Clip deckissä liikkuminen.**

Voit vierittää clip deckiä vasemmalle ja oikealle seuraavilla tavoilla:

* Vasen ja oikea nuolinäppäin. Lisää `Cmd / Ctrl`, jos haluat vierittää kokonaisen sivun kerrallaan.
* Ohjauslevy: pyyhkäisy
* Hiiri: jos hiiressäsi on sivuttaisvieritys, voit käyttää sitä, kun osoitin on clip deckin päällä
* APC40:n vieritysnuppi
* APC40:n _<- DEVICE ->_ -painikkeet

Suuntaamisen helpottamiseksi yläreunassa on clip deckin pieni visualisointi. Katso myös [Clips ja Clip Deck](clips/)

#### Clippien käynnistäminen ja pysäyttäminen

Käynnistä clip painamalla clip-painiketta joko hiirellä tai APC40:llä. Paina painiketta uudelleen pysäyttääksesi clipin. Kun käynnistät clipin, kaikki muut samanväriset clipit pysähtyvät automaattisesti, ellet pidä _shift_-näppäintä painettuna.

Osa clipeistä on _Flash mode_ -tilassa (oletuksena punaiset), jolloin ne pysähtyvät heti, kun vapautat clip-painikkeen.

_STOP_-painike pysäyttää kaikki parhaillaan käynnissä olevat clipit.

#### Clipin ulostuloalueiden määrittäminen

Clip-painikkeiden alla näet aluepainikkeet, oletuksena beam-alueet 1–8 (_BEAM 1_, _BEAM 2_ jne.). Aluepainikkeet syttyvät osoittamaan, mitkä alueet on määritetty valittuna olevalle clipille.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Kaksi riviä aluepainikkeiden alapuolella näet X/Y-kääntöpainikkeet. Niillä voit kääntää clipin vaaka- ja pystysuunnassa.

{% hint style="info" %}
Huomaa, että nämä aluemääritykset ja X/Y-kääntöasetukset liittyvät itse clipiin. Ne säilyvät seuraavan kerran, kun ajat kyseisen clipin. Ne eivät ole globaali asetus.
{% endhint %}

Muokkaa clipin lisäasetuksia klikkaamalla clipiä hiiren oikealla painikkeella. Katso myös [Clip settings](clips/clip-settings.md)

### Ryhmät

Huomaat, että jokaisella clipillä on värillinen reunus, ja tämä väri kertoo, mihin _ryhmään_ clip kuuluu. Myös APC40:n clip-painikkeet syttyvät tällä värillä.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Syaani</td></tr><tr><td>Group 2</td><td>Oranssi</td></tr><tr><td>Group 3</td><td>Punainen</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Vihreä</td></tr></tbody></table>

Ryhmäjärjestelmä on erittäin joustava, ja sen avulla voit:

* pitää yhden ryhmän clipit käynnissä samalla, kun vaihdat toisen ryhmän clippejä
* määrittää alueet ja X/Y-käännöt nopeasti kaikille ryhmän clipeille
* määrittää clipille _Flash mode_ -tilan (Group 3 on oletuksena _Flash mode_ -tilassa)

Ryhmillä on myös siirtymän sisään- ja ulostuloasetukset, jotka clipit voivat periä tai ohittaa.

Voit määrittää clipin ryhmän hiiren oikean painikkeen valikon painikkeilla. APC40:llä voit painaa ryhmäpainiketta ja _sen ollessa edelleen painettuna_ painaa clip-painikkeita.

Muuta alueasetuksia kaikille ryhmän clipeille

Paina APC40:llä ryhmäpainiketta ja _sen ollessa edelleen painettuna_ muuta kaikkien kyseisen ryhmän clippien alueasetuksia zone- ja X/Y-painikkeilla.

Katso myös [Clip-ryhmät](clips/groups.md)

### Efektit

Liberationin efektijärjestelmä on tehokas ja monipuolinen tapa muuttaa clipin ulostuloa reaaliajassa. Oletusefektipainikkeet 1–8 sijaitsevat aluepainikkeiden alla.

#### Efektin käyttäminen

Kytke efekti päälle tai pois painamalla efektipainiketta. Vielä parempi tapa on käyttää APC40:n liukusäätimiä 1–8 efektien häivyttämiseen sisään ja ulos.

#### Efektiparametrit

Säädä kunkin efektin _parametria_ kiertosäätimillä 1–8\*. (Voit myös säätää tasoa ja parametria hiiren oikealla painikkeella.) Parametrin muutos tekee eri asioita sen mukaan, miten efekti on määritetty. Katso alla oleva oletusefektien luettelo.

{% hint style="info" %}
Efektipainikkeissa näkyvät pienet numerot viittaavat efektin _level_- ja _parameter_-arvoihin. _Level_-arvoa ohjataan APC40:n liukusäätimellä, tai sitä voi säätää klikkaamalla ja vetämällä painiketta. Parametria säädetään APC40:n kiertosäätimillä, tai sitä voi säätää hiirellä klikkaamalla oikealla painikkeella.
{% endhint %}

_\*Kiertosäätimet 1–8 ovat APC40 Mk2:n yläreunassa ja Mk1:n oikeassa yläkulmassa. Katso myös:_ [APC40-viite](reference/apc40-reference.md)

#### Oletusefektit

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Lisää clipin ulostuloon kaoottista liikettä. Parametri säätää kaaoksen määrää/nopeutta.
2. **Sine wave** :\
   Vääristää kaiken sisällön liikkuvan siniaallon yli. Parametri säätää aallonpituutta.
3. **Rotation** :\
   Pyörittää kaikkea. Parametri säätää pyörimisnopeutta.
4. **Horizontal flip** :\
   Litistää ja venyttää kaikkea vaakasuunnassa. Parametri säätää nopeutta.
5. **Scale** :\
   Skaalaa kaiken toistuvasti täydestä koosta nollaan. Parametri säätää nopeutta.
6. **Hue** :\
   Muuttaa kaiken sävyä, mutta ei muuta kylläisyyttä (eli kaikki valkoinen pysyy valkoisena). Parametri säätää sävyä.
7. **Saturation and hue** :\
   Muuttaa kaiken sävyä ja kyllästää värin täysin (eli kaikki valkoinen muuttuu värilliseksi). Parametri säätää sävyä.
8. **Flash** :\
   Väläyttää kaiken kirkkauden toistuvasti täydestä nollaan. Parametri säätää välähdysnopeutta.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Alarivillä on lisäksi 16 väritehostetta, joilla käytetään valmiita sävy- ja kylläisyysarvoja.

Huomaa, että nämä ovat oletusefektejä, mutta niitä voi muokata tekemään lähes mitä tahansa haluat!

#### Mikä on _tällä hetkellä valittu Clip_?

Kun käynnistät clipin, se syttyy osoittamaan, että se on aktiivinen. Sen ympärillä on myös valkoinen reunus, joka osoittaa, että kyseessä on tällä hetkellä _valittu_ clip. Kun vaihdat aluepainikkeita tai säädät clipin asetuksia, muutokset kohdistuvat _tällä hetkellä valittuun clipiin._

{% hint style="info" %}
Valitse clip käynnistämättä sitä painamalla `Alt / Option`-näppäintä ennen clip-painikkeen painamista. Tämä on hyvä tapa säätää sen alueita ja muita asetuksia ilman, että clip ajetaan.
{% endhint %}

### Clip Settings -paneeli

Käytä _Clip Settings_ -paneelia skaalauksen ja X/Y-sijainnin muokkaamiseen sekä tehokkaan zone delay -järjestelmän käyttämiseen.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings -paneeli

_Global Settings_ -paneelissa voit säätää globaaleja ulostuloasetuksia, jotka vaikuttavat kaikkeen ulostuloon kaikilla alueilla.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Ota AUTO RESET käyttöön, jos haluat nollata kaikki _Global settings_ -asetukset automaattisesti aina, kun yhtään clipiä ei ole käynnissä.

### Ajoitus

Lähes kaikissa laser-esityksissä on jonkinlainen musiikkiraita, joten Liberationin ajoitusjärjestelmä perustuu tempoon iskuina minuutissa. _Tempo Panel_ -paneelissa näet ajan esityksen: jokainen neliö vastaa yhtä iskua, ja näet niiden välkkyvän tahdissa.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Käytettävissä on useita synkronointivaihtoehtoja, kuten MIDI clock ja Ableton Link. Jos tiedät musiikin tempon, voit säätää sitä käsin näytön liukusäätimellä tai APC40:n Tempo-nupilla. Voit myös pysyä musiikin tahdissa _Tap Tempo_ -järjestelmällä\_.\_

#### Tap Tempo

_Tap Tempo_ on musiikkisovelluksissa yleisesti käytetty termi. Sen avulla voit naputtaa tempon musiikin soidessa rytmin mukana. Voit käyttää näytöllä olevaa painiketta, mutta suositeltavaa on käyttää _T_-näppäintä tai APC40:n _Tap Tempo_ -painiketta (tai halutessasi vaikka jalkakytkintä).

Palauta tempo tahdin alkuun painamalla _R_-näppäintä tai _Metronome_-painiketta (APC40).

Pyöristä tempo kokonaisluvuksi painamalla _Y_-näppäintä tai kääntämällä _Tempo_-nuppia (APC40). Tämä voi olla hyödyllistä elektronisessa musiikissa, jossa tempo on usein tasaluku iskuina minuutissa.

### Clip deckin järjestäminen

Siirrä clipiä clip deckissä klikkaamalla ja vetämällä se uuteen paikkaan. Vedon aikana voit vierittää vasemmalle ja oikealle nuolinäppäimillä (tai APC40:n vieritysrullalla/painikkeilla).

Pidä `Alt / Option`-näppäintä painettuna vetämisen aikana, jos haluat tehdä kopion.

Valitse clip käynnistämättä sitä `Alt / Option`-klikkaamalla.

Monivalitse clippejä `Alt / Option + Shift`-klikkaamalla tai tee "lasso"-valinta klikkaamalla ja vetämällä clipin ulkopuolelta.

Klikkaus ja veto siirtää KAIKKI valitut clipit.

Poista yksi tai useampi clip joko vetämällä ne pois clip deckistä (roskakorikuvake tulee näkyviin) tai käyttämällä DELETE-painiketta clipin hiiren oikean painikkeen valikosta.

### Laser Overview -paneeli

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser overview panel_ näyttää nopeasti parhaillaan käytössä olevien lasereiden tilan. Oikean reunan vihreä neliö kertoo, että laserohjain toimii normaalisti. Jos se muuttuu oranssiksi, yhteydessä on satunnaisia katkoksia. Jos se on punainen, yhteys on katkennut. Jos se on harmaa, sitä ei ole yhdistetty ohjaimeen lainkaan.

Keskellä oleva kuvaaja näyttää ruutujen keston historian, ja oikealla oleva numero on nykyinen kuvataajuus. Mitä monimutkaisempaa sisältö on, sitä hitaampi kuvataajuus on (eli sitä enemmän se voi välkkyä). Alle noin 25 fps alkaa yleensä näyttää hieman välkkyvältä.

### Lasereihin yhdistäminen – Controller Assignment -paneeli

Avaa _Controller Assignment_ -paneeli klikkaamalla _Assign Laser Controllers_ -painiketta. (Paneeliin pääsee myös valikkoriviltä kohdasta _View -> Controller Assignment_.)

Tässä voit valita, mitkä laserulostulot lähetetään millekin laserohjaimelle. Vedä ja pudota ohjaimet oikean reunan luettelosta vasemman reunan paikkoihin. Voit nimetä ohjaimet uudelleen vastaamaan laseria, jonka kanssa ne on yhdistetty (käytä kynäkuvakkeen painiketta).

Lue lisätiedot luvusta [Ohjaimen määritys](setting-up/controller-assignment.md).

{% hint style="danger" %}
Ennen kuin aktivoit yhtään laseria, käy läpi luku [Lasereiden käyttöönoton prosessin yleiskatsaus](setting-up/setting-up-lasers.md).
{% endhint %}

### Laser Output -paneeli

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Tämä paneeli näyttää _tällä hetkellä valitun laserin_ asetukset (yläreunan numero kertoo laserin). Vaihda valittua laseria _tab_-näppäimellä, painamalla numeronäppäintä, klikkaamalla laserin numeroa _Laser Overview_ -paneelissa tai _output view_ -näkymässä.

* **Number button** aktivoi laserin tai poistaa sen käytöstä. Jos painike on punainen, laser on aktivoitu.
* **Brightness** säätää laserin kirkkautta muista lasereista riippumatta (ja se yhdistetään _global brightness_ -asetukseen – eli jos molemmat ovat 50 %, laserisi toimii 25 %:n kirkkaudella).
* **Test Pattern** kytkee testikuvion päälle vain tälle laserille (ohittaa globaalin testikuvioasetuksen).
* **Orientation** korjaa sivuttain tai ylösalaisin ripustetut laserit.
* **Flip Horizontal and Flip Vertical** kääntää laserin ulostulon. Hyödyllinen ulostulon korjaukseen, jos lasereiden johdotus ei ole yhdenmukainen.
* **Copy Laser Settings** avaa paneelin, jonka avulla voit kopioida erilaisia asetuksia tästä laserista muihin.

### Skanneriasetukset

Näyttölaserit toimivat liikuttamalla yhtä lasersädettä erittäin nopeasti ja kytkemällä sitä päälle ja pois, jotta ilmassa voidaan piirtää muotoja. Se, minkä näet viivoina, muotoina ja kuvina, on itse asiassa säde, joka seuraa reittejä nopeammin kuin silmäsi ehtivät havaita.

Pistevirta on dataa, joka kertoo laserille, minne sen pitää seuraavaksi siirtyä ja milloin säteen pitää olla päällä tai pois. Liberationissa clipit muunnetaan tähän pistevirtaan reaaliajassa, kun ne lähetetään lasereille.

Liberation antaa tarkan hallinnan siihen, miten tämä pistevirta luodaan. Näin voit tasapainottaa kunkin laserin pehmeyden, kirkkauden ja suorituskyvyn.

{% hint style="info" %}
Jos olet tottunut vanhempiin laserohjelmistoihin, jotka perustuvat ennakkoon laskettuihin pistevirtoihin, tämä lähestymistapa voi tuntua aluksi erilaiselta. Reaaliaikainen pisteiden luonti mahdollistaa kuitenkin saman sisällön optimoinnin eri tavalla kullekin laserille. Tämä helpottaa työskentelyä useiden lasereiden kanssa, joilla on erilaiset skannerinopeudet tai eri laatu, ilman että sisältöä tarvitsee kopioida tai rakentaa uudelleen. Se pitää myös clip-tiedostot hyvin pieninä, minkä vuoksi koko Liberationin oletus-clip deck on vain muutamia megatavuja eikä gigatavuja.
{% endhint %}

Perusskanneriasetukset ovat:

* **Speed** on skannerin nopeus, eli kuinka nopeasti laser liikkuu piirtäessään muotoja. Tämä vastaa pisteennopeuden säätämistä perinteisissä laserohjelmistoissa, mutta Liberationissa voit muuttaa laserin liikkumisnopeutta _pisteennopeudesta riippumatta._ Tätä asetusta ei yleensä tarvitse säätää.
* **Scanner sync** (tunnetaan joskus nimellä _blank shift, aiemmin Colour Shift_) Skannerit liikuttavat laseria todella nopeasti, mutta kirkkauden ja värin muutos ei yleensä ole synkronissa liikkeen kanssa. Tämä näkyy pieninä välkkyvinä valon "häntinä" säteiden ja viivojen reunoissa. Tällä säädöllä saat liikkeen ja värin synkroniin keskenään. Katso [Laser output -asetuspaneeli](setting-up/laser-settings.md)

Muut edistyneet skanneriasetukset käsitellään luvussa [Edistyneet toiminnot](advanced/).

### Alueistus

Täydellinen opas lasereiden määrittämiseen ja alueistukseen löytyy täältä: [Lasereiden käyttöönoton prosessin yleiskatsaus](setting-up/setting-up-lasers.md)
