---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Usein kysytyt kysymykset

## Laitteisto

#### **Toimiiko Liberation Windowsissa?**

Kyllä – Liberation tukee täysin **Windows 10:tä ja 11:tä (64-bittinen)**, ja ominaisuudet ovat samat kuin Mac-versiossa. Jokainen julkaisu toimitetaan samanaikaisesti molemmille alustoille.

#### **Toimiiko Liberation Macilla?**

Kyllä – Liberation tukee täysin **Macia (macOS 12 Monterey ja uudemmat)**, ja ominaisuudet vastaavat Windows-versiota. Kaikki päivitykset julkaistaan yhtä aikaa.

#### **Millainen kone vaaditaan vähintään?**

Se riippuu siitä, kuinka monta laseria haluat ohjata. Jos käytät vain muutamaa laseria, myös vaatimaton kone riittää hyvin. Kaikki Apple Silicon -Macit toimivat erittäin hyvin, ja niiden pitäisi pystyä ohjaamaan jopa 100 laseria. Jos teet monimutkaisia ja kriittisiä esityksiä, suosittelemme hankkimaan parhaan koneen, johon budjettisi riittää.

#### **Kuinka montaa laseria voin ohjata Liberationilla?**

Liberation voi käyttää useita lasereita yhdellä tietokoneella. Sitä on testattu yli 100 laserohjaimella, joten vastaus riippuu seuraavista:

* tietokoneesi suoritin
* verkon nopeus
* tilauksesi tyyppi

#### **Mitä MIDI-ohjaimia voin käyttää?**

Liberation on suunniteltu ja optimoitu suositun APC40 Mk2 MIDI -ohjaimen ympärille. Se toimii myös APC40 Mk1:n kanssa. Katso [Live-ohjaus APC40](midi-control/live-control-with-the-apc40.md)

Lisäämme vähitellen tukea muille MIDI-ohjaimille, ja tällä hetkellä tuemme myös APC Mini Mk2:ta ja MIDI Fighter Twisteriä.

Lisäksi käytettävissä on MIDI Send/Receive -järjestelmä, joka tarjoaa lisää MIDI-ohjausmahdollisuuksia. Katso [MIDI Send/Receive](midi-control/midi-send-receive.md)

Katso lisätietoja kohdasta [MIDI-ohjaus](midi-control/).

#### **Voinko käyttää mitä tahansa MIDI-ohjainta?**

Kehitämme parhaillaan määritettävää MIDI-järjestelmää, joka mahdollistaa tämän tulevaisuudessa. Sillä välin osa käyttäjistä on onnistunut käyttämään MIDI-tulkkia, joka voi muuntaa mitä tahansa MIDI-viestejä MIDI Send/Receive -järjestelmää varten, mutta tämä on hankala ja edistynyt prosessi. Etsi neuvoja tästä määrityksestä [foorumilta](https://forum.liberationlaser.com), mutta käytännössä APC40 on paras vaihtoehto.

## Laserohjaimet

#### **Mitkä laserohjaimet ovat yhteensopivia Liberationin kanssa?**

* [Ether Dream (suositeltu)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (laiteohjelmisto on ehkä päivitettävä)
* LaserCube USB (ja LaserDock)
* LaserCube-verkkoprotokolla (langallisella yhteydellä)
* AVB, jota [LASollinger lasers](https://laseranimation.com/en/) käyttää (tällä hetkellä vain macOS, testauksessa)

Katso lisätietoja kohdasta [Yhteensopivat laserit ja ohjaimet (DACit)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Miksi ette tue \[muun merkkistä] laserohjainta?**

Jotta ohjelmistojen ja laitteistojen yhteentoimivuutta voitaisiin parantaa, Liberation tukee vain DAC-laitteita, joilla on julkaistu viestintäprotokolla. Uskon, että tämä on laseralan kannalta paras suunta.

#### **Mistä tiedän, voiko laseriani käyttää Liberationin kanssa?**

Jos laserissasi on jokin seuraavista, voit käyttää sitä Liberationin kanssa:

* Ulkoinen **ILDA input** – 25-nastainen D-liitin, jota käytetään yhteensopivan ulkoisen ohjaimen kanssa.
* Sisäisesti asennettu **Ether Dream**.
* Mikä tahansa **LaserCube** (toimii sekä USB- että Wi-Fi LaserCube -laitteiden kanssa).
* **X-Laser-laite, jossa on sisäänrakennettu Mercury-järjestelmä** (Ether Dream mode -tilassa).
* **LaserAnimation Sollinger -projektori, jossa on sisäänrakennettu AVB** (vain macOS, vaatii AVB-yhteensopivat verkkolaitteet, tällä hetkellä testauksessa).

Katso lisätietoja kohdasta [Yhteensopivat laserit ja ohjaimet (DACit)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Voinko käyttää Liberationia LaserCubeni kanssa?**

Kyllä, Liberation toimii suoraan minkä tahansa LaserCuben kanssa. Katso [LaserCube](hardware/lasercube.md)

## Lisenssit

#### **Mikä lisenssin hinta on?**

Katso ajantasaiset hinnat [shop](https://liberationlaser.com/shop)-sivulta.

#### **Mitä rajoituksia lisenssitasojen välillä on?**

Katso nykyiset lisenssivaihtoehdot [shop](https://liberationlaser.com/shop)-sivulta.

Huomaa, että voit määrittää, esikatsella ja suunnitella esityksiä niin monella laserilla kuin haluat **jokaisella** tasolla, myös ilmaisella. Muita rajoituksia ei ole lainkaan lukuun ottamatta sitä, kuinka monta laseria voit asettaa _arm_-tilaan. Kaikki muut Liberationin ominaisuudet ovat kaikkien käytettävissä.

#### **Voinko päivittää ylemmälle tasolle?**

Voit päivittää ylemmälle tasolle milloin tahansa. Saat osittaisen hyvityksen nykyisen lisenssisi jäljellä olevasta ajasta, ja uusi tilauksesi alkaa heti. Katso [Päivitä / alenna lisenssisi tasoa](installation/upgrade-downgrade-your-license.md)

#### **Voinko siirtyä alemmalle lisenssitasolle?**

Voit siirtyä alemmalle tasolle milloin tahansa, mutta muutos tulee voimaan nykyisen lisenssikauden lopussa. Katso [Päivitä / alenna lisenssisi tasoa](installation/upgrade-downgrade-your-license.md)

#### **Miten valtuutan tietokoneeni lisenssilläni?**

Kun olet ostanut lisenssin, voit valtuuttaa tietokoneen suoraan Liberation-ohjelmistossa. _About_-näytössä näkyy _Authorise_-painike, joka pyytää sinua kirjautumaan verkkosivustolle. Viimeistele valtuutus noudattamalla näytön ohjeita. Katso [Valtuutus ja valtuutuksen poistaminen](installation/authorising-and-de-authorising.md)

#### **Kuinka usein tietokone on yhdistettävä internetiin?**

Aina kun lisenssi uusiutuu, Liberation on yhdistettävä internetiin, jotta sen sisäinen lisenssi voidaan päivittää. Kuukausittain uusiutuvalla maksulla yhteys tarvitaan joka kuukausi.

#### **Mitä tapahtuu, jos en voi yhdistää tietokonetta internetiin uusimisen jälkeen?**

Liberation antaa 7 päivän lisäajan lisenssin uusiutumisen jälkeen, jotta voit yhdistää internetiin ja päivittää sen sisäisen lisenssin. Tämän jälkeen Liberation palaa _Free_-tilaan.

#### **Mitä tapahtuu, jos luottokorttini vanhenee?**

Saat sähköposti-ilmoituksen maksupalveluntarjoajaltamme, ja sinun täytyy päivittää maksutapasi. Kirjaudu verkkosivustolle ja käytä tilaussivun _Update payment details_ -linkkiä.

#### **Miten peruutan uusiutuvan lisenssini?**

Kirjaudu verkkosivustolle, avaa _Your subscriptions_ -sivu, valitse peruutettava tilaus ja napsauta sitten _Cancel Subscription_ -linkkiä. Voit jatkaa Liberationin käyttöä lisenssikauden loppuun asti.

#### **Kuinka monelle tietokoneelle voin asentaa Liberationin?**

Voit asentaa Liberationin niin monelle tietokoneelle kuin haluat. Lisenssivaltuutuksia tarvitaan vain laser-/DMX-ulostulon käyttöön, ja lisenssitasosi määrittää, kuinka monta tietokonetta voidaan valtuuttaa ulostuloa varten samanaikaisesti. Katso [Miten lisensointi toimii](installation/how-licensing-works.md)

#### **Miten siirrän lisenssini tietokoneelta toiselle?**

* Avaa Liberation tietokoneella, jota et enää halua käyttää
* Varmista, että olet yhteydessä internetiin, ja napsauta _About_-näytön _De-authorise this computer_ -painiketta
* Avaa nyt Liberation uudella tietokoneella
* Napsauta _About_-näytön _Authorise this computer_ -painiketta.
* Verkkosivusto avautuu. Kirjaudu sisään ja viimeistele valtuutus noudattamalla näytön ohjeita

Voit myös poistaa valtuutuksen etänä tietokoneelta, johon sinulla ei enää ole pääsyä (tietyin rajoituksin). Katso [Valtuutus ja valtuutuksen poistaminen](installation/authorising-and-de-authorising.md)

#### **Voinko poistaa Liberationin valtuutuksen tietokoneelta, joka on kadonnut tai varastettu?**

Voit poistaa tietokoneen valtuutuksen verkkosivuston kautta. Jos kyseinen Liberation-asennus ei ole ollut verkossa viimeisimmän uusimisen jälkeen, tämä voidaan tehdä heti.

Muussa tapauksessa valtuutuksen poisto tulee voimaan, kun tilaus uusiutuu tai kun tietokone muodostaa yhteyden internetiin, sen mukaan kumpi tapahtuu ensin. Jos sinun täytyy kiireellisesti valtuuttaa uusi tietokone uudelleen, ota yhteyttä tukeen.

### Liberationin käyttö

#### Oletusmäärityksessä on 8 laseria – miten muutan tämän?

Katso [Projektin määrittäminen](setting-up/setting-up-your-project.md) ja [Lasereiden lisääminen / poistaminen](setting-up/adding-removing-lasers.md)

#### Voinko kopioida zone-asetukset yhdeltä laserilta muille?

Kyllä. Katso [Kopioi alueita lasereiden välillä](output-view/copy-zones-between-lasers.md)

#### Voinko kirjoittaa numeron liukusäätimen käyttämisen sijaan?

Kyllä. `Cmd / Ctrl`-napsauta liukusäädintä, niin voit syöttää arvon näppäimistöllä.

#### **Miten synkronoin Liberationin musiikkiin?**

Siinä on älykäs "tap tempo" -järjestelmä, joka toimii odotetulla tavalla, mutta voit käyttää myös ulkoista MIDI-kelloa tai Ableton Linkiä. Katso [Tempo / synkronointi](tempo-synchronisation.md). Timeline voidaan synkronoida sisääntulevaan LTC/SMPTE-aikakoodiin minkä tahansa audioliitännän kautta. Katso [Timecode](timecode.md).

#### Mitä asetuksia minun täytyy säätää, jotta saan laserista parhaan ulostulon?

Tärkein asetus on _Colour Shift_, joka kompensoi pientä viivettä peilien liikkeen ja laserien kirkkauden muutosten välillä. Jos laserpisteissä tai -sädeissä näkyy pieniä “häntiä”, tätä asetusta täytyy säätää. (Katso esimerkki “hännistä” [Laser output -asetuspaneeli](setting-up/laser-settings.md) -sivun kuvista)

Voit myös kokeilla scanner-nopeuden muuttamista: hitaampi, jos scannerit ovat perustasoa, tai nopeampi, jos ne ovat hyvät. **Käytä kuitenkin varoen, sillä voit vahingoittaa scannereita, jos ajat niitä liian kovaa.**

Käytettävissä on myös valmiita scanner-asetuksia. Oletusasetus on varovainen ja sopii useimpiin lasersädevaatimuksiin. Jos sinulla on paremmat scannerit, käytettävissä on muita esiasetuksia, ja lisäksi on grafiikkaa varten viritettyjä esiasetuksia.

Lisätietoja on kohdassa [Laser output -asetuspaneeli](setting-up/laser-settings.md), ja ohjeet omien esiasetusten luomiseen ovat kohdassa [◼️ Skanneriesiasetukset ja renderöintiprofiilit](advanced/scanner-presets.md) (edistynyt, työn alla)

Voit myös korjata väritasapainoa _Colour calibration_ -asetuksilla. Katso [Värikalibrointi](advanced/colour-calibration.md) (edistynyt tekniikka)

#### Mitä _Latency(ms)_-asetus tekee?

Tämä on kuvaviive eli suurin aika kuvan luomisen ja sen laseriin lähettämisen välillä. Sitä ei yleensä tarvitse säätää, mutta jos sinulla on verkko-ongelmia, voit kokeilla sen kasvattamista. Katso lisätietoja kohdasta [Latenssiasetus](setting-up/latency-setting.md).

### Clips

#### Miten säädän clipin zoneja ja asetuksia käynnistämättä sitä?

`Alt / Option`-napsauta, jotta siitä tulee _tällä hetkellä valittu Clip_, mutta sitä ei aktivoida. Katso myös [Clipien käynnistäminen ja pysäyttäminen](clips/starting-stopping-clips.md)

#### Miten kopioin clippejä?

Napsauta ja vedä samalla, kun pidät `Alt / Option`-näppäintä painettuna. Katso myös [Clip Deckin järjestäminen](clips/organising-your-clip-deck.md)

#### Miten poistan clippejä?

Napsauta ja vedä ne pois clip deckiltä. Katso myös [Clip Deckin järjestäminen](clips/organising-your-clip-deck.md)

#### Miten teen monivalinnan, poistan, yhdistän clip deckejä jne.?

Katso [Clip Deckin järjestäminen](clips/organising-your-clip-deck.md)

#### Mitä clipissä oleva pieni mikrofonisymboli ja muut kuvakkeet tarkoittavat?

Ne osoittavat, että clip käyttää ääni- tai MIDI-syötettä, ja kolme pistettä osoittavat, että käytössä on zone-viive. Katso [Mitä clip-painikkeiden pienet kuvakkeet tarkoittavat?](clips/what-are-the-small-icons-on-the-clip-buttons.md)
