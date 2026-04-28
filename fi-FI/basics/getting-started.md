# ✅ Pika-aloitusopas

## Johdanto

Tervetuloa **Liberationiin** – seuraavan sukupolven laser show -ohjelmistoon.

Liberation on tehokas ja monipuolinen nykyaikainen ohjelmisto. Se on rakennettu käytettävyyden ja luotettavuuden perusperiaatteiden varaan, jotta voit ilmaista luovuuttasi vapaasti. Se on nopea, tehokas ja sujuva; tämän _pika-aloitusoppaan_ avulla pääset alkuun nopeasti!

### Laserien hallinta

Liberation on niin joustava, että voit määrittää lasereita ja visualisoida niitä ilman, että yhtään oikeaa laseria on kytketty. Kun olet valmis, voit liittää jokaisen ulostulon saumattomasti laserohjaimeen.

{% hint style="info" %}
Voit määrittää ja visualisoida Liberationissa niin monta laseria kuin haluat. Lisenssitasot (Hobbyist, Pro jne.) rajoittavat vain niiden laserien määrää, jotka voit _aktivoida_. Tämä tarkoittaa, että voit suunnitella 100 laserin laser shown jopa ilmaisella lisenssillä. Päivitys tarvitaan vasta, kun haluat ajaa shown oikeilla lasereilla.
{% endhint %}

Oletuksena käytössä on 8 laseria vaakasuoraan levitettynä, mutta voit mukauttaa tämän haluamallasi tavalla. Aluksi on luultavasti parasta pitää tämä oletus, kun tutustut ohjelmistoon. Myöhemmin voit säätää sen vastaamaan omaa laitteistoasi. (Katso [setting-up-your-project.md](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Tärkeää: ennen kuin aktivoit yhtään laseria, varmista että ymmärrät niihin liittyvät riskit ja käy huolellisesti läpi luku [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

## Ohjelmiston yleiskuva

### Turvakatkaisu

Aina kun käytät lasereita, sinulla täytyy olla käsillä **laitteistopohjainen hätäpysäytyspainike** (katso [emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md)). Jos haluat poistaa kaiken käytöstä vähemmän kiireellisesti, voit käyttää _**DISARM ALL**_ -painiketta tai `Escape`-näppäintä (tai APC40:n _**SESSION**_-näppäintä). Voit myös pienentää yleiskirkkautta näytön liukusäätimellä tai APC40:n pääfaderilla.

### Liukusäätimet

Liberationissa on useita liukusäätimiä ja ohjaimia.

{% hint style="info" %}
`Cmd / Ctrl`-klikkaa liukusäädintä, jos haluat kirjoittaa uuden arvon tarkempaa säätöä varten.
{% endhint %}

### Pikanäppäimet

Täydellinen pikanäppäinluettelo löytyy täältä: [keyboard-shortcuts.md](../reference/keyboard-shortcuts.md)

### Näytön asettelu

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Etkö ole varma, mitä jokin painike tekee? Vie hiiri sen päälle, niin näet kuvauksen!
{% endhint %}

#### Valikko

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Valikosta löydät kaikki tiedostojen tuonti- ja vientitoiminnot sekä paneelien avaamisen. Täältä löytyy myös toiminto, jolla voit valtuuttaa tietokoneen tilauksellesi (_Liberation -> Authorise/Deauthorise this computer_).

#### Kuvakepalkki

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Täältä löytyvät yleiset toiminnot, kuten kaikkien laserien aktivointi ja käytöstä poisto, yleiskirkkaus, testikuvio sekä 3D-, Canvas- ja Output-näkymien välillä vaihtaminen.

### Näkymät

Näytön vasemmassa yläkulmassa oleva suuri alue voi näyttää jonkin kolmesta päänäkymästä: **3D**, **CANVAS** tai **OUTPUT.** Vaihda niiden välillä kuvakepalkin painikkeilla (tai käytä `Tab`-näppäintä vaihtaaksesi 3D- ja OUTPUT-näkymien välillä ja jatka sitten sarkaimella laserulostulosta toiseen).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D-näkymä näyttää, miltä laserit näyttävät, ja sen voi määrittää vastaamaan omaa laserkokoonpanoasi. Kierrä kameraa klikkaamalla ja vetämällä. Liiku eteen- ja taaksepäin hiiren rullalla. Lisää asetuksia löytyy _3D Visualiser settings_ -paneelista (_View -> 3D Visualiser Settings_). Katso [3d-visualiser.md](../setting-up/3d-visualiser.md).

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output-näkymää käytetään kunkin laserin alueiden ja maskien määrittämiseen. (Huomaa vasemman yläkulman suuri numero, josta näet helposti, mitä laseria käsittelet!)

Tämä näkymä kuvaa kyseisen laserin koko ulostuloa ja sitä, missä kukin alue sijaitsee sen sisällä. Oletuksena jokaisella laserilla on vain yksi alue, mutta voit lisätä niin monta aluetta kuin on käytännössä järkevää. Kaikki alueet näkyvät tässä näkymässä.

{% hint style="info" %}
**Mikä on alue?**

Alue on laserin ulostulossa oleva tila, johon voit ohjata lasersisältöä. Yhdellä laserilla voi olla useampi kuin yksi alue. Yksinkertaisin aluetyyppi on _beam_-alue, mutta käytössä on myös _canvas_-alueita ja _DMX_-alueita. Tässä oppaassa keskitymme pääasiassa beam-alueisiin, joita käytetään yleensä ilmakehään piirtyvien säde-efektien luomiseen.
{% endhint %}

Voit valita muokattavan laserin jollakin näistä tavoista:

* yläpalkin numeroiduilla painikkeilla
* painamalla haluamasi laserin numeronäppäintä _(1-9_ keys\_)\_
* `Tab`-näppäimellä, jolla siirryt laserista seuraavaan

Lisää uusi laser kokoonpanoon painamalla _+_-painiketta. (Myös _Laser Overview_ -paneelissa on _ADD LASER_ -painike)

Poista laser kokoonpanosta painamalla punaista ⊖-painiketta _Laser Overview_ -paneelissa.

Voit lähentää ja loitontaa hiiren vieritysrullalla. Siirrä näkymää klikkaamalla ja vetämällä kohtaa, jossa ei ole aluetta.

Valitse alue klikkaamalla sitä ja säädä sen kulmapisteitä hiirellä. Kun vedät kulmaa, käytä `Alt / Option`-näppäintä, jos haluat tehdä säädöstä epäsuhteisen. Näet lisää asetuksia, kuten aluetyypin vaihtamisen, klikkaamalla aluetta hiiren oikealla painikkeella.

Vasemmalla on palkki, jossa on joukko kuvakepainikkeita. Vie hiiri minkä tahansa painikkeen päälle, niin näet kuvauksen sen toiminnosta. Näillä painikkeilla voit lisätä beam-alueita, canvas-alueita ja maskeja. Lisäksi voit määrittää testikuvion vain tälle laserille sekä säätää ruudukko- ja tartunta-asetuksia.

Lisätietoja on kohdassa [output-view](../output-view/).

#### Canvas

Canvas-järjestelmää käytetään pääasiassa grafiikkaan ja arkkitehtoniseen mappaukseen. Voit jakaa monimutkaisia kuvia useille lasereille ja tehdä perspektiivikorjauksen jokaiselle osalle. Katso [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/).

### APC40 MIDI -ohjain

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Liberationia voi ohjata hiirellä ja näppäimistöllä, mutta paljon parempi tapa on käyttää APC40 MIDI -ohjainta (Mark 2 on paras vaihtoehto, mutta myös Mark 1 toimii).

Katso myös: [apc40-reference.md](../reference/apc40-reference.md)

Olemme nyt toteuttaneet tuen myös APC Mini Mark 2:lle ja MIDI Fighter Twisterille, ja lisää ohjaimia on kehitteillä. APC40 Mark 2 on kuitenkin useimmissa tapauksissa paras vaihtoehto.&#x20;

### Clipit ja efektit

{% hint style="info" %}
**Mikä on clip?**

Clip on säiliö mille tahansa lasersisällölle Liberationissa. Clipit voivat sisältää säteitä tai graafisia animaatioita, ja ne ovat yleensä toistuvia silmukoita. Ne voidaan ohjata mille tahansa alueelle (tai _Canvas target area_ -kohdealueelle), ja ne käynnistetään Clip Deckin clip-painikkeilla.
{% endhint %}

#### Clip deckin yleiskuva

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Tätä ruudukkoa kutsutaan _clip deckiksi_, ja siihen tallennetaan kaikki laserclipit. Se on suunniteltu vastaamaan suoraan APC40:n 8 x 5 -painikeruudukkoa.

**Clip deckissä liikkuminen.**

Voit vierittää clip deckiä vasemmalle ja oikealle seuraavilla tavoilla:

* Vasen ja oikea nuolinäppäin. Lisää `Cmd / Ctrl`, jos haluat vierittää kokonaisen sivun kerrallaan.
* Ohjauslevy: pyyhkäise
* Hiiri: jos hiiressäsi on sivusuuntainen vieritys, voit käyttää sitä, kun osoitin on clip deckin päällä
* APC40:n vieritysnuppi
* APC40:n _<- DEVICE ->_ -painikkeet

Jotta hahmotat sijaintisi paremmin, yläreunassa on clip deckin minivisualisointi. Katso myös [clips](../clips/)

#### Clippien käynnistäminen ja pysäyttäminen

Käynnistä clip painamalla clip-painiketta joko hiirellä tai APC40:llä. Pysäytä se painamalla painiketta uudelleen. Kun käynnistät clipin, kaikki muut samanväriset clipit pysähtyvät automaattisesti, ellet pidä _shift_-näppäintä pohjassa.

Jotkin clipit ovat _Flash mode_ -tilassa (oletuksena punaiset), jolloin ne pysähtyvät heti, kun vapautat clip-painikkeen.

_STOP_-painike pysäyttää kaikki tällä hetkellä käynnissä olevat clipit.

#### Clipin ulostuloalueiden määrittäminen

Clip-painikkeiden alla näet aluepainikkeet, oletuksena beam-alueet 1–8 (_BEAM 1_, _BEAM 2_ jne.). Aluepainikkeet syttyvät osoittamaan, mitkä alueet on määritetty valittuna olevalle clipille.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Kaksi riviä aluepainikkeiden alapuolella näet X/Y-kääntöpainikkeet. Niillä voit kääntää clipin vaaka- ja pystysuunnassa.

{% hint style="info" %}
Huomaa, että nämä aluekohdistukset ja X/Y-kääntöasetukset liittyvät itse clipiin. Ne säilyvät seuraavalla kerralla, kun ajat kyseisen clipin. Ne eivät ole yleisiä asetuksia.
{% endhint %}

Muokkaa clipin muita asetuksia klikkaamalla clipiä hiiren oikealla painikkeella. Katso myös [clip-settings.md](../clips/clip-settings.md)

### Ryhmät

Huomaat, että jokaisella clipillä on värillinen reunus, ja tämä väri kertoo, mihin _ryhmään_ se kuuluu. Myös APC40:n clip-painikkeet syttyvät tällä värillä.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Syaani</td></tr><tr><td>Group 2</td><td>Oranssi</td></tr><tr><td>Group 3</td><td>Punainen</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Vihreä</td></tr></tbody></table>

Ryhmäjärjestelmä on erittäin joustava, ja sen avulla voit:

* Pitää yhden ryhmän clipit käynnissä samalla, kun vaihdat toisen ryhmän tilaa
* Määrittää alueet ja X/Y-käännöt nopeasti kaikille ryhmän clipeille
* Asettaa clipille _Flash mode_ -tilan (Group 3 on oletuksena _Flash mode_ -tilassa)

Ryhmillä on myös sisään- ja ulossiirtymien asetuksia, jotka clipit voivat periä tai ohittaa.

Voit määrittää clipin ryhmän oikean klikkauksen valikon painikkeilla. APC40:llä voit painaa ryhmäpainiketta ja _pitää sen edelleen pohjassa_ samalla, kun painat clip-painikkeita.

Muuta kaikkien ryhmän clippien alueasetuksia

Paina APC40:llä ryhmäpainiketta ja käytä sitten alue- ja X/Y-painikkeita _sen ollessa edelleen pohjassa_ vaihtaaksesi kaikkien kyseisen ryhmän clippien alueasetuksia.

Katso myös [groups.md](../clips/groups.md)

### Efektit

Liberationin efektijärjestelmä on tehokas ja monipuolinen tapa muuttaa clipin ulostuloa reaaliajassa. Oletusefektipainikkeet 1–8 ovat aluepainikkeiden alla.

#### Efektin käyttäminen

Kytke efekti päälle tai pois painamalla efektipainiketta. Vielä parempi tapa on käyttää APC40:n liukusäätimiä 1–8 efektien häivyttämiseen sisään ja ulos.

#### Efektiparametrit

Säädä kunkin efektin _parametria_ kiertosäätimillä 1–8\*. (Voit myös klikata hiiren oikealla painikkeella ja säätää tasoa ja parametria hiirellä.) Parametrin muutos tekee eri asioita sen mukaan, miten efekti on määritetty. Alla on luettelo oletusefekteistä.

{% hint style="info" %}
Efektipainikkeissa näkyvät pienet numerot viittaavat efektin _tasoon_ ja _parametriin_. _Tasoa_ ohjataan APC40:n faderilla, tai voit klikata ja vetää painikkeessa. Parametria säädetään APC40:n kiertosäätimillä, tai voit säätää sitä hiirellä klikkaamalla oikealla painikkeella.
{% endhint %}

_\*Kiertosäätimet 1–8 ovat APC40 Mk2:n yläreunassa ja Mk1:n oikeassa yläkulmassa. Katso myös:_ [apc40-reference.md](../reference/apc40-reference.md)

#### Oletusefektit

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Lisää clipin ulostuloon kaoottista liikettä. Parametri säätää kaaoksen määrää/nopeutta.
2. **Sine wave** :\
   Vääristää kaiken sisällön liikkuvan siniaallon yli. Parametri säätää aallonpituutta.
3. **Rotation** :\
   Pyörittää kaikkea ympäri. Parametri säätää pyörimisnopeutta.
4. **Horizontal flip** :\
   Litistää ja venyttää kaikkea vaakasuunnassa. Parametri säätää nopeutta.
5. **Scale** :\
   Skaalaa kaikkea toistuvasti täydestä koosta nollaan. Parametri säätää nopeutta.
6. **Hue** :\
   Muuttaa kaiken sävyä, mutta ei muuta kylläisyyttä (eli kaikki valkoinen pysyy valkoisena). Parametri säätää sävyä.
7. **Saturation and hue** :\
   Muuttaa kaiken sävyä ja kyllästää värin täysin (eli kaikki valkoinen muuttuu väriksi). Parametri säätää sävyä.
8. **Flash** :\
   Väläyttää kaiken kirkkauden toistuvasti täydestä nollaan. Parametri säätää välähdysnopeutta.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Alarivillä on lisäksi 16 väriefektiä, joilla voi käyttää valmiita sävy- ja kylläisyysarvoja.

Huomaa, että nämä ovat oletusefektejä, mutta niitä voi muokata tekemään lähes mitä tahansa!

#### Mikä on _"currently selected clip"_?

Kun käynnistät clipin, se syttyy osoittamaan, että se on aktiivinen. Sen ympärillä on myös valkoinen reunus, joka kertoo, että tämä on tällä hetkellä _valittu_ clip. Kun vaihdat aluepainikkeita tai säädät clipin asetuksia, muutokset kohdistuvat _currently selected clip_ -clipiin.

{% hint style="info" %}
Jos haluat valita clipin käynnistämättä sitä, paina `Alt / Option`-näppäintä ennen clip-painikkeen painamista. Tämä on hyvä tapa säätää sen alueita ja muita asetuksia ajamatta sitä.
{% endhint %}

### Clip settings -paneeli

Käytä _Clip Settings_ -paneelia skaalauksen ja X/Y-sijainnin muokkaamiseen sekä tehokkaan alueviivejärjestelmän käyttämiseen.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global settings -paneeli

_Global Settings_ -paneelissa voit säätää yleisiä ulostuloasetuksia, jotka vaikuttavat kaikkeen ulostuloon kaikilla alueilla.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Ota AUTO RESET käyttöön, jos haluat palauttaa kaikki _Global settings_ -asetukset automaattisesti aina, kun yksikään clip ei ole käynnissä.&#x20;

### Ajoitus

Lähes kaikissa laseresityksissä on jonkinlainen musiikkiraita, joten Liberationin ajoitusjärjestelmä perustuu tempoon iskuina minuutissa. _Tempo Panel_ -paneelissa näet ajan esityksen: jokainen neliö vastaa yhtä iskua, ja näet niiden vilkkuvan tahdissa.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Käytössä on useita synkronointivaihtoehtoja, kuten MIDI clock ja Ableton Link. Jos tiedät musiikin tempon, voit säätää sitä manuaalisesti näytön liukusäätimellä tai APC40:n Tempo-nupilla. Voit myös pysyä musiikin tahdissa _Tap Tempo_ -järjestelmän avulla\_.\_

#### Tap Tempo

_Tap Tempo_ on musiikkisovelluksissa yleisesti käytetty termi. Sen avulla voit naputtaa tahdin musiikin soidessa ja asettaa tempon sen perusteella. Voit käyttää näytön painiketta, mutta suositeltavaa on käyttää _T_-näppäintä tai APC40:n _Tap Tempo_ -painiketta (tai halutessasi vaikka jalkakytkintä).

Palauta tempo tahdin alkuun painamalla _R_-näppäintä tai _Metronome_-painiketta (APC40).

Pyöristä tempo kokonaisluvuksi painamalla _Y_-näppäintä tai kääntämällä _Tempo_-nuppia (APC40). Tämä voi olla hyödyllistä elektronisessa musiikissa, jossa tempo on usein pyöreä BPM-luku.

### Clip deckin järjestäminen

Siirrä clip clip deckissä klikkaamalla ja vetämällä se uuteen sijaintiin. Vedon aikana voit vierittää vasemmalle ja oikealle nuolinäppäimillä (tai APC40:n vieritysrullalla/painikkeilla).

Pidä `Alt / Option`-näppäintä pohjassa vetämisen aikana, jos haluat tehdä kopion.

`Alt / Option`-klikkaa clipiä valitaksesi sen käynnistämättä sitä.

`Alt / Option + Shift`-klikkaa clipiä monivalintaa varten, tai klikkaa ja vedä clipin ulkopuolelta valitaksesi useita clippejä "lasso"-valinnalla.&#x20;

Klikkaus ja veto vetää KAIKKIA valittuja clippejä.

Poista yksi tai useampi clip joko vetämällä ne pois clip deckistä (roskakorikuvake tulee näkyviin) tai käyttämällä clipin oikean klikkauksen valikon DELETE-painiketta.

### Laser overview -paneeli

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser overview panel_ näyttää nopeasti tällä hetkellä käynnissä olevien laserien tilan. Oikealla oleva vihreä neliö kertoo, että laserohjain toimii normaalisti. Jos se muuttuu oranssiksi, yhteydessä on satunnaisia katkoksia, ja jos se muuttuu punaiseksi, yhteys on katkennut. Jos se on harmaa, laseria ei ole kytketty ohjaimeen lainkaan.&#x20;

Keskellä oleva kuvaaja näyttää ruutupituuksien historian, ja oikealla oleva numero kertoo nykyisen kuvataajuuden. Mitä monimutkaisempaa sisältö on, sitä hitaampi kuvataajuus on (eli sitä enemmän välkkymistä). Noin alle 25 fps alkaa yleensä näyttää hieman välkkyvältä.&#x20;

### Yhdistäminen lasereihin – Controller Assignment -paneeli

Avaa _Controller Assignment_ -paneeli klikkaamalla _Assign Laser Controllers_ -painiketta. (Tähän paneeliin pääsee myös valikkopalkista kohdasta _View -> Controller Assignment_.)

Täällä voit valita, mitkä laserulostulot lähetetään millekin laserohjaimelle. Vedä ja pudota ohjaimia oikeanpuoleisesta luettelosta vasemmanpuoleisiin paikkoihin. Voit nimetä ohjaimet uudelleen sen mukaan, minkä laserin kanssa ne on paritettu (käytä kynäkuvakepainiketta).

Lue lisätietoja luvusta [controller-assignment.md](../setting-up/controller-assignment.md).

{% hint style="danger" %}
Ennen kuin aktivoit yhtään laseria, käy läpi luku [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

### Laser output -paneeli

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Tässä paneelissa näkyvät _currently selected laser_ -laserin asetukset (yläreunan numero osoittaa kyseisen laserin). Vaihda valittua laseria _tab_-näppäimellä, painamalla numeronäppäintä, klikkaamalla laserin numeroa _Laser Overview_ -paneelissa tai _output view_ -näkymässä.

* **Number button** aktivoi laserin ja poistaa sen käytöstä. Jos se on punainen, laser on aktivoitu.
* **Brightness** säätää laserin kirkkautta muista lasereista riippumatta (ja se yhdistetään _global brightness_ -asetukseen – eli jos molemmat ovat 50 %, laserisi on 25 %:ssa).
* **Test Pattern** ottaa testikuvion käyttöön vain tälle laserille (ohittaa yleisen testikuvioasetuksen)
* **Orientation** korjaa sivuttain tai ylösalaisin ripustetut laserit.
* **Flip Horizontal and Flip Vertical** kääntää laserin ulostulon. Hyödyllinen ulostulon korjaamiseen, jos laserien johdotukset poikkeavat toisistaan.
* **Copy Laser Settings** avaa paneelin, jolla voit kopioida erilaisia asetuksia tältä laserilta muille.

### Scanner settings

Näyttölaserit toimivat liikuttamalla yhtä lasersädettä erittäin nopeasti ja kytkemällä sitä päälle ja pois, jotta ilmaan voidaan piirtää muotoja. Se, minkä näet viivoina, muotoina ja kuvina, on todellisuudessa säde, joka seuraa reittejä nopeammin kuin silmäsi ehtivät seurata.

Pistevirta on dataa, joka kertoo laserille, minne sen pitää liikkua seuraavaksi ja milloin säteen pitää olla päällä tai pois päältä. Liberationissa clipit muunnetaan tähän pistevirtaan reaaliajassa samalla, kun ne lähetetään lasereille.

Liberation antaa tarkat säätömahdollisuudet siihen, miten pistevirta luodaan. Näin voit tasapainottaa kunkin laserin pehmeyden, kirkkauden ja suorituskyvyn.

{% hint style="info" %}
Jos olet tottunut vanhempiin laserohjelmistoihin, jotka käyttävät ennalta laskettuja pistevirtoja, tämä toimintatapa voi tuntua aluksi erilaiselta. Reaaliaikainen pisteiden luonti mahdollistaa kuitenkin saman sisällön optimoinnin eri tavoin eri lasereille. Tämä helpottaa työskentelyä useiden laserien kanssa, joilla on erilaiset skannerinopeudet tai laatu, ilman että sisältöä täytyy monistaa tai rakentaa uudelleen. Se myös pitää clip-tiedostot erittäin pieninä, minkä vuoksi koko Liberationin oletus-clip deck on vain muutaman megatavun kokoinen gigatavujen sijaan.
{% endhint %}

Scanner settings -perusasetukset ovat:

* **Speed** on skannerin nopeus eli se, kuinka nopeasti laser liikkuu piirtäessään muotoja. Tämä vastaa perinteisen laserohjelmiston pistearvon säätämistä, mutta Liberationissa voit muuttaa laserin liikkumisnopeutta _pistearvosta riippumatta_. Tätä ei yleensä tarvitse säätää.
* **Scanner sync** (tunnetaan joskus nimellä _blank shift, aiemmin Colour Shift_) Skannerit liikuttavat laseria erittäin nopeasti, mutta kirkkauden ja värin muutos on yleensä epäsynkassa liikkeen kanssa. Tämä näkyy pieninä välkkyvinä valon "häntinä" säteiden ja viivojen reunoilla. Käytä tätä säätöä saadaksesi liikkeen ja värin synkronoitua keskenään. Katso [laser-settings](../setting-up/laser-settings/)

Muut edistyneet Scanner settings -asetukset käsitellään luvussa [advanced](../advanced/).

### Zoning

Täydellinen opas laserien määrittämiseen ja alueiden asettamiseen löytyy täältä: [setting-up-lasers.md](../setting-up/setting-up-lasers.md)
