# ✅ Pika-aloitusopas

## Johdanto

Tervetuloa käyttämään **Liberation**-ohjelmistoa – uuden sukupolven lasershow-ohjelmistoa.

Liberation on tehokas ja monipuolinen moderni ohjelmisto. Se perustuu käytettävyyteen ja luotettavuuteen, jotta voit toteuttaa luovuuttasi vapaasti. Se on nopea, tehokas ja sujuva. Tämän _pika-aloitusoppaan_ avulla pääset alkuun nopeasti!

### Lasereiden hallinta

Liberation on niin joustava, että voit määrittää lasereita ja visualisoida niitä ilman, että yhtään oikeaa laseria on kytketty. Kun olet valmis käyttämään oikeita lasereita, voit määrittää jokaisen Output-kanavan laser controller -laitteelle sujuvasti.

{% hint style="info" %}
Voit määrittää ja visualisoida Liberationissa niin monta laseria kuin haluat. Lisenssitasot (Hobbyist, Pro jne.) rajoittavat vain sitä, kuinka monta laseria voi olla _armed_-tilassa. Tämä tarkoittaa, että voit suunnitella lasershow’n 100 laserilla myös ilmaisella lisenssillä. Päivitystä tarvitaan vasta, kun show ajetaan oikeilla lasereilla.
{% endhint %}

Oletusasetuksessa on 8 laseria vaakasuorassa rivissä, mutta voit muokata tätä haluamallasi tavalla. Aluksi tämä oletus kannattaa todennäköisesti pitää käytössä, kun tutustut ohjelmistoon. Myöhemmin voit säätää sen vastaamaan omaa laitteistoasi. (Katso [Projektin määrittäminen](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Tärkeää: ennen kuin asetat mitään lasereita armed-tilaan, varmista, että ymmärrät riskit, ja käy huolellisesti läpi luku [Lasereiden määrittäminen](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Ohjelmiston yleiskuva

### Turvakatkaisu

Aina kun käytät lasereita, sinulla on oltava käytettävissä **fyysinen hätäpysäytyspainike** (katso [Hätäpysäytys / turvalukitukset](../hardware/emergency-stop-interlocks.md "mention")). Jos haluat poistaa kaikkien lasereiden armed-tilan vähemmän kiireellisesti, käytä _**DISARM ALL**_ -painiketta, `Escape`-näppäintä tai APC40-laitteen _**SESSION**_-näppäintä. Voit myös pienentää Global Brightness -tasoa näytön liukusäätimellä tai APC40:n pääfaderilla.

### Liukusäätimet

Liberationissa on erilaisia liukusäätimiä ja ohjaimia.

{% hint style="info" %}
`Cmd / Ctrl`-klikkaa liukusäädintä, jos haluat syöttää uuden arvon käsin ja tarvitset tarkempaa säätöä kuin liukusäädin antaa.
{% endhint %}

### Pikanäppäimet

Täysi pikanäppäinluettelo löytyy täältä: [Pikanäppäimet](../reference/keyboard-shortcuts.md "mention")

### Näytön asettelu

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Etkö ole varma, mitä jokin painike tekee? Vie hiiri painikkeen päälle, niin näet kuvauksen!
{% endhint %}

#### Valikko

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Valikosta löydät kaikki tiedostojen tuonti- ja vientitoiminnot sekä paneelien avaamisen. Täältä löytyy myös vaihtoehto, jolla tietokone valtuutetaan tilauksellesi (_Liberation -> Authorise/Deauthorise this computer_).

#### Kuvakepalkki

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Täältä löydät yleiset toiminnot, kuten kaikkien lasereiden asettamisen armed- tai disarmed-tilaan, Global Brightness -säädön, test pattern -toiminnon sekä vaihtamisen 3D view-, Canvas view- ja Output view -näkymien välillä.

### Näkymät

Näytön vasemmassa yläkulmassa oleva suuri alue voi näyttää yhden kolmesta päänäkymästä: **3D**, **CANVAS** tai **OUTPUT.** Vaihda niiden välillä kuvakepalkin painikkeilla. Voit myös käyttää `Tab`-näppäintä vaihtaaksesi 3D view- ja OUTPUT view -näkymien välillä ja jatkaa sitten siirtymistä vuorotellen jokaisen laserin Output-kanavan läpi.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view näyttää, miltä laserit näyttävät, ja sen voi määrittää vastaamaan omaa laseriasetustasi. Klikkaa ja vedä kiertääksesi kameraa. Käytä hiiren rullaa siirtyäksesi eteen- ja taaksepäin. Lisää asetuksia löytyy _3D Visualiser settings_ -paneelista (_View -> 3D Visualiser Settings_). Katso [3D Visualiser](../setting-up/3d-visualiser.md "mention").

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view -näkymässä määritetään kunkin laserin zones ja masks. Huomaa vasemman yläkulman suuri numero, josta näet helposti, mitä laseria käsittelet.

Tämä näkymä kuvaa laserin koko Output-aluetta ja sitä, missä kukin zone sijaitsee sen sisällä. Oletuksena jokaisella laserilla on vain yksi zone, mutta voit lisätä niin monta zone-kohdetta kuin käytännössä on järkevää, ja näet ne kaikki tässä näkymässä.

{% hint style="info" %}
**Mikä on zone?**

Zone on laserin Output-alueen sisällä oleva tila, johon voit ohjata lasersisältöä. Yhdellä laserilla voi olla useampi kuin yksi zone. Yksinkertaisin zone-tyyppi on _beam_ zone, mutta käytettävissä on myös _canvas_ zones ja _DMX_ zones. Tässä oppaassa keskitymme enimmäkseen beam zones -kohteisiin, joita käytetään yleensä ilmassa näkyvien säde-efektien luomiseen.
{% endhint %}

Voit valita muokattavan laserin jollakin näistä tavoista:

* yläreunan palkin numeropainikkeilla
* painamalla haluamasi laserin numeronäppäintä (_1-9 keys_)
* siirtymällä laserista toiseen `Tab`-näppäimellä

Lisää uusi laser asetukseen painamalla _+_-painiketta. (_Laser Overview_ -paneelissa on myös _ADD LASER_ -painike.)

Poista laser asetuksesta painamalla punaista ⊖-painiketta _Laser Overview_ -paneelissa.

Voit lähentää ja loitontaa hiiren rullalla. Voit siirtää näkymää klikkaamalla ja vetämällä kohdassa, jossa ei ole zone-kohdetta.

Valitse zone klikkaamalla sitä ja säädä sen kulmapisteitä hiirellä. Pidä `Alt / Option`-näppäin painettuna kulmaa vetäessäsi, jos haluat tehdä säädöstä epäyhtenäisen. Avaa lisää vaihtoehtoja klikkaamalla zone-kohdetta hiiren oikealla painikkeella; vaihtoehtoihin kuuluu myös zone-tyypin vaihtaminen.

Vasemmalla on palkki, jossa on useita kuvakepainikkeita. Vie hiiri minkä tahansa painikkeen päälle, niin näet kuvauksen sen toiminnosta. Näillä painikkeilla voit lisätä beam zones, canvas zones ja masks. Lisäksi käytettävissä on asetuksia, joilla test pattern asetetaan vain tälle laserille, sekä ruudukko- ja tartunta-asetuksia.

Lisätietoja: [Output-näkymä](../output-view/ "mention").

#### Canvas

Canvas-järjestelmää käytetään pääasiassa grafiikkaan ja arkkitehtoniseen mappingiin. Voit jakaa monimutkaisia kuvia useille lasereille ja korjata jokaisen osan perspektiivin. Katso [Grafiikka ja Canvas-järjestelmä](../graphics-and-the-canvas-system/ "mention").

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Liberationia voi ohjata hiirellä ja näppäimistöllä, mutta APC40 MIDI control interface tekee käytöstä huomattavasti paremman. Mark 2 on paras vaihtoehto, mutta myös Mark 1 toimii.

Katso myös: [APC40-viite](../reference/apc40-reference.md "mention")

Liberation tukee myös APC Mini- ja MIDI Fighter Twister -laitteita. APC40 Mark 2 on edelleen useimmissa tapauksissa paras vaihtoehto.&#x20;

### Clips ja tehosteet

{% hint style="info" %}
**Mikä on Clip?**

Clip on säiliö mille tahansa lasersisällölle Liberationissa. Clips voivat sisältää säteitä tai graafisia animaatioita, ja ne ovat yleensä toistuvia silmukoita. Ne voidaan ohjata mihin tahansa zone-kohteeseen tai _Canvas target area_ -alueelle, ja ne käynnistetään Clip Deck -alueen Clip-painikkeilla.
{% endhint %}

#### Clip Deckin yleiskuva

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Tämä ruudukko tunnetaan nimellä _Clip Deck_, ja siihen tallennetaan kaikki laserin Clips. Se on suunniteltu vastaamaan suoraan APC40-laitteen 8 x 5 -painikeruudukkoa.

**Clip Deckissä liikkuminen.**

Voit vierittää Clip Deck -aluetta vasemmalle ja oikealle seuraavilla tavoilla:

* Vasen ja oikea nuolinäppäin. Lisää `Cmd / Ctrl`, jos haluat vierittää kokonaisen sivun kerrallaan.
* Ohjauslevy: pyyhkäisy
* Hiiri: jos hiiressäsi on vaakavieritys, voit käyttää sitä, kun osoitin on Clip Deck -alueen päällä
* APC40:n vieritysnuppi
* APC40:n _<- DEVICE ->_ -painikkeet

Yläreunassa oleva Clip Deck -alueen pienoisvisualisointi auttaa hahmottamaan sijaintisi. Katso myös [Clips ja Clip Deck](../clips/ "mention")

#### Clips käynnistäminen ja pysäyttäminen

Käynnistä Clip painamalla Clip-painiketta joko hiirellä tai APC40-laitteella. Pysäytä se painamalla painiketta uudelleen. Kun käynnistät Clip-sisällön, kaikki muut samanväriset Clips pysähtyvät automaattisesti, ellet pidä _shift_-näppäintä painettuna.

Osa Clips-sisällöistä on _Flash mode_ -tilassa (oletuksena punaiset). Tällöin ne pysähtyvät heti, kun vapautat Clip-painikkeen.

_STOP_-painike pysäyttää kaikki parhaillaan käynnissä olevat Clips.

#### Output zones -määritys Clip-sisällölle

Clip-painikkeiden alapuolella näkyvät zone-painikkeet, oletuksena beam zones 1–8 (_BEAM 1_, _BEAM 2_ jne.). Zone-painikkeet syttyvät osoittamaan, mitkä zones on määritetty valitulle Clip-sisällölle.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Kaksi riviä zone-painikkeiden alapuolella näkyvät X/Y flip -painikkeet. Niillä voit kääntää Clip-sisällön vaaka- ja pystysuunnassa.

{% hint style="info" %}
Huomaa, että nämä zone-määritykset ja X/Y flip -asetukset liittyvät itse Clip-sisältöön. Ne säilyvät seuraavaan kertaan, kun käynnistät kyseisen Clip-sisällön. Ne eivät ole globaaleja asetuksia.
{% endhint %}

Muokkaa Clip-sisällön lisäasetuksia klikkaamalla Clip-kohdetta hiiren oikealla painikkeella. Katso myös [Clip settings](../clips/clip-settings.md "mention")

### Ryhmät

Huomaat, että jokaisella Clip-kohteella on värillinen reunus, ja tämä väri kertoo, mihin _ryhmään_ se kuuluu. Myös APC40:n Clip-painikkeet syttyvät tällä värillä.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Ryhmä 1</td><td>Syaani</td></tr><tr><td>Ryhmä 2</td><td>Oranssi</td></tr><tr><td>Ryhmä 3</td><td>Punainen</td></tr><tr><td>Ryhmä 4</td><td>Indigo</td></tr><tr><td>Ryhmä 5</td><td>Vihreä</td></tr></tbody></table>

Ryhmäjärjestelmä on hyvin joustava, ja sen avulla voit:

* pitää yhden ryhmän Clips käynnissä samalla, kun kytket toisen ryhmän sisältöjä päälle ja pois
* määrittää zones ja X/Y flip -asetukset nopeasti kaikille ryhmän Clips-sisällöille
* asettaa Clip-sisällön _Flash mode_ -tilaan (Ryhmä 3 on oletuksena _Flash mode_ -tilassa)

Ryhmillä on myös siirtymäasetukset sisään- ja ulosmenolle. Ryhmän Clips voivat periä nämä asetukset tai ohittaa ne.

Voit määrittää Clip-sisällön ryhmän hiiren oikean painikkeen valikon painikkeilla. APC40-laitteella voit painaa ryhmäpainiketta ja _sen ollessa edelleen painettuna_ painaa Clip-painikkeita.

Muuta zone-asetuksia kaikille ryhmän Clips-sisällöille

APC40-laitteella paina ryhmäpainiketta ja käytä sitten zone- ja X/Y-painikkeita _sen ollessa edelleen painettuna_, jotta voit vaihtaa zone-asetuksia kaikille kyseisen ryhmän Clips-sisällöille.

Katso myös [Ryhmät](../clips/groups.md "mention")

### Tehosteet

Liberationin tehostejärjestelmä on tehokas ja monipuolinen tapa muuttaa Clip-sisällön Output-signaalia reaaliajassa. Oletustehostepainikkeet 1–8 ovat zone-painikkeiden alla.

#### Tehosteen käyttäminen

Kytke tehoste päälle tai pois painamalla tehostepainiketta. Vielä parempi tapa on käyttää APC40:n liukusäätimiä 1–8 tehosteiden häivyttämiseen sisään ja ulos.

#### Tehosteparametrit

Säädä kunkin tehosteen _parameter_-arvoa kiertosäätimillä 1–8\*. Voit säätää tasoa ja parametria myös klikkaamalla hiiren oikealla painikkeella. Parametrin muutos tekee eri asioita sen mukaan, miten tehoste on määritetty. Alla on luettelo oletustehosteista.

{% hint style="info" %}
Tehostepainikkeissa näkyvät pienet numerot viittaavat tehosteen _level_- ja _parameter_-arvoihin. _Level_-arvoa ohjataan APC40:n faderilla, tai voit klikata painiketta ja vetää. Parameter-arvoa säädetään APC40:n kiertosäätimillä, tai voit säätää sitä hiirellä klikkaamalla oikealla painikkeella.
{% endhint %}

_\*Kiertosäätimet 1–8 ovat APC40 Mk2:n yläreunassa ja Mk1:n oikeassa yläkulmassa. Katso myös:_ [APC40-viite](../reference/apc40-reference.md "mention")

#### Oletustehosteet

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Lisää kaoottista liikettä Clip-sisällön Output-signaaliin. Parameter säätää kaaoksen määrää/nopeutta.
2. **Sine wave** :\
   Vääristää kaiken sisällön liikkuvan siniaallon mukaan. Parameter säätää aallonpituutta.
3. **Rotation** :\
   Pyörittää kaikkea. Parameter säätää pyörimisnopeutta.
4. **Horizontal flip** :\
   Litistää ja venyttää kaikkea vaakasuunnassa. Parameter säätää nopeutta.
5. **Scale** :\
   Skaalaa kaiken toistuvasti täydestä koosta nollaan. Parameter säätää nopeutta.
6. **Hue** :\
Muuttaa kaiken sävyä, mutta ei muuta kylläisyyttä (eli valkoinen pysyy valkoisena). Parameter säätää sävyä.
7. **Saturation and hue** :\
Muuttaa kaiken sävyä ja kyllästää värin täysin (eli valkoinen muuttuu väriksi). Parameter säätää sävyä.
8. **Flash** :\
   Väläyttää kaiken kirkkauden toistuvasti täydestä nollaan. Parameter säätää välähdysnopeutta.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Alarivillä on lisäksi 16 väritehostetta, joilla voi käyttää valmiita sävy- ja kylläisyysarvoja.

Huomaa, että nämä ovat oletustehosteita, mutta niitä voi muokata tekemään lähes mitä tahansa!

#### Mikä on _tällä hetkellä valittu Clip_?

Kun käynnistät Clip-sisällön, se syttyy osoittamaan, että se on aktiivinen. Sen ympärillä on myös valkoinen reunus, joka kertoo, että tämä on tällä hetkellä valittu Clip. Aina kun vaihdat zone-painikkeita tai säädät Clip-asetuksia, muutokset kohdistuvat _tällä hetkellä valittuun Clip-kohteeseen_.

{% hint style="info" %}
Jos haluat valita Clip-kohteen käynnistämättä sitä, paina `Alt / Option`-näppäintä ennen Clip-painikkeen painamista. Tämä on hyvä tapa säätää zones ja muita asetuksia ilman, että Clip käynnistyy.
{% endhint %}

### Clip Settings -paneeli

Käytä _Clip Settings_ -paneelia skaalauksen ja X/Y-sijainnin muokkaamiseen sekä tehokkaan zone delay -järjestelmän käyttöön.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings -paneeli

_Global Settings_ -paneelissa voit säätää globaaleja Output-asetuksia, jotka vaikuttavat kaikkeen Output-signaaliin kaikissa zones-kohteissa.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Ota AUTO RESET käyttöön, jos haluat palauttaa kaikki _Global settings_ -asetukset automaattisesti aina, kun yhtään Clip-sisältöä ei ole käynnissä.&#x20;

### Ajoitus

Lähes kaikissa lasershow’ssa on jonkinlainen musiikkiraita, joten Liberationin ajoitusjärjestelmä perustuu tempoon iskuina minuutissa. _Tempo Panel_ -paneelissa näet ajan esityksen: jokainen neliö vastaa yhtä iskua, ja näet niiden välähtävän tahdissa.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Käytettävissä on useita synkronointivaihtoehtoja, kuten MIDI clock ja Ableton Link. Jos tiedät musiikin tempon, voit säätää sitä käsin näytön liukusäätimellä tai APC40:n Tempo-nupilla. Voit myös pysyä musiikin tahdissa _Tap Tempo_ -järjestelmän avulla.

#### Tap Tempo

_Tap Tempo_ on musiikkisovelluksissa yleisesti käytetty termi. Sen avulla voit naputtaa tahdin musiikin soidessa ja asettaa tempon sen mukaan. Voit käyttää näytön painiketta, mutta suositeltavaa on käyttää _T_-näppäintä tai APC40:n _Tap Tempo_ -painiketta. Voit halutessasi käyttää myös jalkakytkintä.

Paina _R_-näppäintä tai APC40:n _Metronome_-painiketta palauttaaksesi tempon tahdin alkuun.

Paina _Y_-näppäintä tai käännä APC40:n _Tempo_-nuppia pyöristääksesi tempon kokonaisluvuksi. Tästä voi olla hyötyä elektronisessa musiikissa, jossa iskujen määrä minuutissa on usein kokonaisluku.

### Clip Deckin järjestäminen

Siirrä Clip uuteen paikkaan Clip Deck -alueella klikkaamalla ja vetämällä. Vedon aikana voit vierittää vasemmalle ja oikealle nuolinäppäimillä tai APC40:n vieritysrullalla/painikkeilla.

Pidä `Alt / Option`-näppäin painettuna vedon aikana, jos haluat tehdä kopion.

`Alt / Option`-klikkaa Clip-kohdetta valitaksesi sen käynnistämättä sitä.

`Alt / Option + Shift`-klikkaa Clip-kohdetta monivalintaa varten, tai klikkaa ja vedä Clip-kohteen ulkopuolelta tehdäksesi “lasso”-valinnan.&#x20;

Klikkaus ja veto siirtää KAIKKI valitut Clips.

Voit poistaa yhden tai useamman Clip-kohteen joko vetämällä ne pois Clip Deck -alueelta (roskakorikuvake tulee näkyviin) tai käyttämällä DELETE-painiketta Clip-kohteen hiiren oikean painikkeen valikossa.

### Laser Overview -paneeli

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser overview panel_ antaa nopean katsauksen parhaillaan käytössä olevien lasereiden tilaan. Oikealla oleva vihreä neliö kertoo, että laser controller toimii hyvin. Jos se muuttuu oranssiksi, esiintyy satunnaisia katkoksia. Jos se on punainen, yhteys on katkennut. Jos se on harmaa, laseria ei ole kytketty controller-laitteeseen lainkaan.&#x20;

Keskellä oleva kaavio näyttää kuvapituuksien historian, ja oikealla oleva numero on nykyinen kuvataajuus. Mitä monimutkaisempaa sisältö on, sitä hitaampi kuvataajuus on (eli sitä enemmän välkkymistä näkyy). Alle noin 25 fps alkaa näyttää hieman välkkyvältä.&#x20;

### Lasereihin yhdistäminen – Controller Assignment -paneeli

Avaa _Controller Assignment_ -paneeli klikkaamalla _Assign Laser Controllers_ -painiketta. Paneelin voi avata myös valikkoriviltä kohdasta _View -> Controller Assignment_.

Tässä voit valita, mitkä laserin Output-kanavat lähetetään millekin laser controller -laitteelle. Vedä ja pudota controller-laitteita oikeanpuoleisesta luettelosta vasemmanpuoleisiin paikkoihin. Voit nimetä controller-laitteet uudelleen sen mukaan, minkä laserin parina ne ovat. Käytä kynäkuvakkeen painiketta.

Lue lisätietoja luvusta [Ohjaimen määritys](../setting-up/controller-assignment.md "mention").

{% hint style="danger" %}
Ennen kuin asetat mitään lasereita armed-tilaan, käy läpi luku [Lasereiden määrittäminen](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Laser Output -paneeli

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Tämä paneeli näyttää _currently selected laser_ -kohteen asetukset. Valittu laser näkyy yläreunan numerona. Vaihda valittua laseria _tab_-näppäimellä, painamalla numeronäppäintä, klikkaamalla laserin numeroa _Laser Overview_ -paneelissa tai _Output view_ -näkymässä.

* **Number button** asettaa laserin armed- tai disarmed-tilaan. Jos painike on punainen, laser on armed-tilassa.
* **Brightness** säätää laserin kirkkautta muista lasereista riippumatta. Se yhdistetään _global brightness_ -asetukseen: jos molemmat ovat 50 %, laserin teho on 25 %.
* **Test Pattern** ottaa test pattern -kuvion käyttöön vain tälle laserille ja ohittaa globaalin test pattern -asetuksen.
* **Orientation** korjaa sivuttain tai ylösalaisin ripustetut laserit.
* **Flip Horizontal and Flip Vertical** kääntää laserin Output-signaalin. Tästä on hyötyä Output-korjauksessa, jos lasereiden johdotus ei ole yhdenmukainen.
* **Copy Laser Settings** avaa paneelin, jonka avulla voit kopioida erilaisia asetuksia tästä laserista muihin.

### Scanner-asetukset

Näyttölaserien toiminta perustuu siihen, että yksittäistä lasersädettä liikutetaan erittäin nopeasti ja se kytketään päälle ja pois, jotta ilmaan voidaan piirtää muotoja. Viivoina, muotoina ja kuvina näkemäsi sisältö on todellisuudessa säde, joka seuraa reittejä nopeammin kuin silmä ehtii havaita.

Point stream on data, joka kertoo laserille, minne sen pitää siirtyä seuraavaksi ja milloin säteen pitää olla päällä tai pois päältä. Liberationissa Clips muunnetaan tähän point stream -muotoon reaaliajassa, kun ne lähetetään lasereille.

Liberation antaa tarkan hallinnan siihen, miten tämä point stream luodaan. Näin voit tasapainottaa tasaisuuden, kirkkauden ja suorituskyvyn jokaiselle laserille erikseen.

{% hint style="info" %}
Jos olet tottunut vanhempaan lasero-ohjelmistoon, joka perustuu ennalta laskettuihin point stream -tietoihin, tämä lähestymistapa voi aluksi tuntua erilaiselta. Reaaliaikainen pisteiden luonti kuitenkin mahdollistaa saman sisällön optimoinnin eri tavalla jokaiselle laserille. Tämä helpottaa työskentelyä useiden lasereiden kanssa, joilla on eri scanner-nopeudet tai -laatu, ilman että sisältöä tarvitsee monistaa tai rakentaa uudelleen. Se pitää myös Clip-tiedostot hyvin pieninä, minkä vuoksi koko Liberationin oletus-Clip Deck vie vain muutamia megatavuja eikä gigatavuja.
{% endhint %}

Scanner-perusasetukset ovat:

* **Speed** on scanner-nopeus, eli se kuinka nopeasti laser liikkuu piirtäessään muotoja. Tämä vastaa perinteisessä laserohjelmistossa point rate -arvon säätöä, mutta Liberationissa voit muuttaa laserin liikkumisnopeutta _point rate -arvosta riippumatta._ Tätä ei yleensä tarvitse säätää.
* **Scanner sync** (tunnetaan joskus nimellä _blank shift, aiemmin Colour Shift_) Scanner liikuttaa laseria todella nopeasti, mutta kirkkauden ja värin muutos ei yleensä ole synkronissa liikkeen kanssa. Tämä näkyy pieninä välkkyvinä valon “häntinä” säteiden ja viivojen reunoilla. Tällä säädöllä saat liikkeen ja värin synkroniin keskenään. Katso [Laser Settings](../setting-up/laser-settings/ "mention")

Muut edistyneet scanner-asetukset käsitellään luvussa [Lisäasetukset](../advanced/ "mention").

### Zoning

Täysi opas lasereiden määrittämiseen ja zoning-asetusten tekemiseen: [Lasereiden määrittäminen](../setting-up/setting-up-lasers.md "mention")
