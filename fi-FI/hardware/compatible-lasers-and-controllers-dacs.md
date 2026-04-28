---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Yhteensopivat laserit ja ohjaimet (DACit)

### Mitkä laserit ovat yhteensopivia Liberationin kanssa?

Jos laserissasi on tavallinen ILDA-tulo, voit käyttää sitä Liberationin kanssa yhteensopivan laserohjaimen, kuten Ether Dreamin tai Helios DACin, kautta – [katso koko luettelo alta](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC – edullisin vaihtoehto kotikäyttöön</p></figcaption></figure>

Et tarvitse ulkoista ohjainta tai ILDA-tuloa, jos:

* laserissasi on sisäänrakennettu Ether Dream, tai
* sinulla on Wicked Lasersin LaserCube, tai
* sinulla on X-Laser-laite, jossa on sisäänrakennettu Mercury, tai
* sinulla on Laser Animation Sollinger -laser, jossa on sisäänrakennettu AVB-ohjain (tällä hetkellä testauksessa vain macOS:llä)

{% hint style="info" %}
**Mikä laserohjain on?**

Laserohjain (tai DAC) on laite, joka ottaa Liberationin digitaalisen datan ja muuntaa sen analogisiksi signaaleiksi, joita tarvitaan laserin skannerien ja lähdön ohjaamiseen. (Tästä nimi DAC: Digital to Analog Converter.)

Ohjain liitetään tietokoneeseen USB:llä tai tavallisen tietokoneverkon kautta. Se voi olla joko ulkoinen laite tai laserin sisään asennettu ohjain.

Jos ohjain on ulkoinen, liität sen laseriin ILDA-liitännällä. ILDA on alan standardi, joka käyttää vanhanmallista 25-napaista D-liitintä. Hanki ILDA-kaapeli, liitä toinen pää ohjaimeen ja toinen laseriin.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>ILDA-lähtö ulkoisessa Ether Dreamissa</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Laserin takapaneeli ja sen eri liitännät, mukaan lukien ILDA-tulo</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Tavallinen ILDA-kaapeli</p></figcaption></figure>

### Mikä ohjain sopii minulle parhaiten?

Jos olet kotikäyttäjä tai ajat pieniä esityksiä enintään neljällä laserilla, jotka ovat lähellä tietokonetta, USB-ohjaimet, kuten **Helios DAC**, ovat **edullisin** vaihtoehto.

Verkkopohjaiset DACit, kuten **Ether Dream**, ovat **paras vaihtoehto ammattilaisille**, jotka osaavat ja haluavat rakentaa verkon ja ajaa suurta määrää lasereita. Kaikki suuret Liberation-esitykset on tähän mennessä ajettu Ether Dreameilla.

Jos sinulla on **LaserCube**, et tarvitse erillistä laserohjainta lainkaan – Liberation on yhteensopiva kaikkien LaserCube-mallien kanssa. Vanhemmat mallit liitetään USB-kaapelilla, ja uudemmat mallit liitetään verkon kautta.

Jos olet ammattilainen ja haluat helpoimman vaihtoehdon, harkitse X-Laser-yksiköitä, joissa on sisäänrakennettu Mercury, tai AVB:tä käyttäviä Laser Animation Sollinger -lasereita.

### Yhteensopivat laserohjaimet

#### Ether Dream (verkko)

[Ether Dream](https://ether-dream.com) on ollut markkinoilla yli kymmenen vuotta, ja sen nykyinen versio on 4 (Liberation toimii kuitenkin myös Ether Dream -versioiden 1, 2 ja 3 kanssa). Ne ovat erittäin luotettavia.

Niihin muodostetaan yhteys tavallisen verkon kautta. Niitä voi ostaa erillisinä yksikköinä, mutta vielä parempi ratkaisu on asentaa ne laserien sisään.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) on paras vaihtoehto aloittelijoille. Se on Ether Dreamia edullisempi, mutta koska se käyttää USB-yhteyttä, sitä ei suositella pitkiin kaapelivetoihin. Lisäksi USB-datan ja ajurien kanssa voi tulla ongelmia, kun liität yli neljä laitetta, erityisesti Windowsissa.

Jos haluat kuitenkin ajaa vain paria laseria kotona, se on halvin ja yksinkertaisin vaihtoehto.

#### Mercury (sisäänrakennettu X-Laser-yksiköihin)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) on X-Laserin tehokas DMX-laserohjausjärjestelmä, joka on suunniteltu valosuunnittelijoille, jotka haluavat ajaa lasereita suoraan perinteisestä valopöydästä. Uusimman laiteohjelmistopäivityksen myötä Mercury sisältää myös **Ether Dream -emuloinnin**, joten se toimii nyt sujuvasti Liberationin kanssa – sekä minkä tahansa muun Ether Dreamia tukevan ohjelmiston kanssa.

#### AVB (sisäänrakennettu Laser Animation Sollinger -yksiköihin)

**AVB** on avoin verkkopohjainen protokolla tehokkaaseen ja pieniviiveiseen ääni- ja datavirran siirtoon. Monissa LaserAnimation Sollinger -projektoreissa AVB-tuki on sisäänrakennettuna laitteistoon, jolloin Liberation voi muodostaa niihin yhteyden verkon kautta ilman ulkoisia DACeja. Liberationin AVB-tuki on tällä hetkellä **vain macOS:lle ja testausvaiheessa**, ja se edellyttää **yhteensopivia AVB-tuettuja verkkolaitteita**. Oikein määritettynä se tarjoaa ammattiesityksiin yksinkertaisemman työnkulun, vähemmän ulkoisia laitteita ja hyvän toimintavarmuuden. I

#### Ohjaimet, joita tuetaan tulevaisuudessa:

* [IDN](http://www.ilda-digital.com) (ILDAn avoin verkkoprotokolla, jonka kuka tahansa valmistaja voi toteuttaa)

### Kaapelointisuositukset

Parhaan suorituskyvyn saavuttamiseksi pidä USB-DACit lähellä tietokonetta ja liitä ne lasereihin pidemmillä ILDA-kaapeleilla. (Ole kuitenkin varovainen: ILDA-kaapelit voivat toimia purun aikana kuin tarttumakoukku!)

Jos käytät Ether Dreameja, voit pitää ne edelleen yhdessä paikassa ja liittää ne lasereihin pitkillä ILDA-kaapeleilla. Vaihtoehtoisesti voit ripustaa tai sijoittaa ne lähelle lasereita ja käyttää pidempiä verkkokaapeleita.

Ihanteellinen ratkaisu on, että Ether Dreamit (tai muut ohjaimet) asennetaan suoraan laserien sisään. Isossa-Britanniassa Rob Stanwax Laserilta voi tehdä tämän puolestasi.
