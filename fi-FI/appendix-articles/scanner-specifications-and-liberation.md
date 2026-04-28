---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Skannerien tekniset tiedot ja Liberation

### Skannerien teknisten tietojen sekava todellisuus

Pisteenopeudet ja skannerien tekniset tiedot voivat olla hieman hämmentäviä. Näet usein tietoja kuten 30kpps @ 8º tai 50kpps @ 4º, mutta aina ei ole selvää, mitä nämä luvut oikeastaan tarkoittavat.

{% hint style="info" %}
Huomautus – en ole skannerilaitteiston asiantuntija, mutta minulla on vuosien käytännön kokemus siitä, miten hyvin eritasoiset skannerit saadaan näyttämään hyvältä ohjelmiston ja pistevirran muodostuksen avulla, ilman laitteiston säätämistä. Tämä perustuu siihen kokemukseen.
{% endhint %}

#### **Mistä nämä luvut tulevat**

Termit kuten “30K” ja “50K” ovat lyhenteitä, jotka perustuvat siihen, miten skannereita arvioidaan ILDA-testikuviolla näillä pisteenopeuksilla tietyissä olosuhteissa.

Kun skannerin tiedoissa lukee esimerkiksi: _30Kpps @ 8°_ se tarkoittaa käytännössä:

> “Tämä skanneri pystyy toistamaan ILDA-testikuvion 30 000 pisteen sekuntinopeudella 8° skannauskulmassa, kun se on säädetty oikein.”

Se ei ole kattava tai täysin standardoitu mittari todellisesta suorituskyvystä. Itse asiassa sitä ei alun perin suunniteltu vertailuarvoksi lainkaan, vaan sitä käytettiin **säätömenettelyssä**. Ajetaan tunnettua kuviota kiinteällä pisteenopeudella (esim. 30 000 pistettä/s) ja säädetään vaimennusta ja vahvistusta, kunnes kuvio näyttää oikealta.

Se on kuitenkin edelleen yleisimmin käytetty vertailukohta, ja se voi antaa hyvän käsityksen skannerien laadusta, ainakin hyvämaineisten valmistajien kohdalla. _Vähemmän hyvämaineisten_ kohdalla taas...

#### Jos haluat testata skannerit niiden ilmoitetuilla arvoilla

{% hint style="danger" %}
**Tämä on edistynyt tekniikka, ja voit vahingoittaa skannereitasi, jos et ole varovainen. Ei suositella, ellet tiedä mitä teet.**
{% endhint %}

Tarvitset ohjelmiston, joka pystyy tuottamaan [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) -kuvion – käsittääkseni LaserShowGen saattaa osata tehdä tämän – ja sinun on säädettävä ulostulon koko vastaamaan ilmoitettua skannauskulmaa (esim. 8°). Katso ILDA-dokumentaatiosta ohjeet ulostulon analysointiin.

#### Miksi se ei välttämättä ole hyvä vertailuarvo

Ensinnäkin testikuviosi voi näkyä väärin, vaikka skannerisi olisivat hyvät, jos niitä ei ole säädetty juuri tätä varten optimaalisella tavalla.

Se voi olla hyödyllinen yleisohje “hyvien” ja “huonojen” skannerien erottamiseen, mutta valmistajat voivat joskus suhtautua näihin teknisiin tietoihin melko vapaasti.

#### Miten valitsen hyvän skannerin?

Mielestäni kannattaa varmistaa, että skannerit ovat hyvämaineisen valmistajan tekemiä. Kalliit huippuluokan skannerivalmistajat kuten Cambridge Technology (CT), Eye Magic (EMS) ja ScannerMAX (Pangolinin tytäryhtiö) ovat aina hyviä, eikä niiden kanssa juuri voi mennä pieleen. Mutta kun skanneripari maksaa noin 1000 dollaria, monelle aloittelevalle se on kalliimpi kuin itse laserit!

Olen siis käyttänyt enimmäkseen kiinalaisia valmistajia. Dragon Tiger (DT) -skannerit ovat asiallisia ja edullisia, ja käsittääkseni LightSpace käyttää niitä. Myös monet muut valmistajat (mukaan lukien OPT ja Able joissakin malleissa) käyttävät DT-pohjaisia järjestelmiä.

Phenix Technology (PT) on yleensä alempaa tasoa, mutta rehellisesti sanottuna ne ovat luultavasti useimpiin käyttötarkoituksiin aivan riittäviä.

**Jos skannereissasi ei ole brändiä, silloin laadusta kannattaa todennäköisesti olla huolissaan!**

#### Miten Liberation auttaa

Ensinnäkin useimpiin asioihin et tarvitse todella kalliita skannereita! Edulliset 30kpps DT -skannerit tai jopa PT-skannerit riittävät hyvin. Skannerien oletusasetukset ovat tarkoituksella varovaisia, eikä niitä useimmiten _tarvitse säätää_ (paitsi _Scanner sync_).

Vaikka sinulla olisi paremmat skannerit, niitä ei kannata ajaa kovempaa kuin on tarpeen. Tämä pidentää niiden käyttöikää merkittävästi.

#### Mikä on "point stream"?

Olet luultavasti kuullut tämän termin aiemmin – sillä ohjataan skannerien liikerataa.

Pistevirta on luettelo X/Y-sijainneista, joista jokaisella on väri. Jos haluat piirtää esimerkiksi valkoisen viivan, lähetät sarjan pisteitä viivaa pitkin, kaikki valkoisiksi asetettuina. Skannerit liikkuvat sitten pisteestä toiseen kiinteällä nopeudella – pisteitä sekunnissa -nopeudella (PPS) – ja säde piirtää muodon.

#### Miten tämä toimii perinteisissä laserojelmistoissa

Perinteinen laserohjelmisto tallentaa pistevirran jokaiselle cue-kohdalle. Animoiduissa cue-kohdissa tämä tarkoittaa yleensä erillistä pistevirtaa jokaiselle framelle. Keskeistä on, että kaikki on täysin ennalta määritettyä. Tämän seurauksena pisteenopeuden kasvattaminen saa skannerit liikkumaan nopeammin saman ennalta määritetyn datan läpi.

{% hint style="info" %}
Vanhemmissa ohjelmistoissa tämä lähestymistapa oli välttämätön – tietokoneet eivät yksinkertaisesti olleet riittävän nopeita muodostamaan pistevirtoja reaaliajassa. Siksi niissä on yleensä erillinen cue-editori, jolla animoitujen framejen data esigeneroidaan.

Tämä selittää myös, miksi sisältö voi viedä gigatavuja tilaa. Käytännössä tallennat suuria, pakkaamattomia aaltomuotoja melko korkeilla näytteenottotaajuuksilla.
{% endhint %}

#### Miksi "point rate" on Liberationissa vähemmän merkityksellinen

Liberation muodostaa pistevirran reaaliajassa, mikä antaa meille valtavasti joustavuutta. Huomaa "Scanner speed" -asetus Laser Settings -paneelissa. Sen avulla voimme nopeuttaa ja hidastaa skannereita, mutta tärkeää on, että se **ei** muuta taustalla olevaa pisteenopeutta (PPS).

#### Hetkinen, mitä? Miten?

Tiedän, se kuulostaa aluksi oudolta.

Koska Liberation muodostaa pistevirran reaaliajassa, se voi säätää tätä pistevirtaa. Mitä kauempana pisteet ovat toisistaan, sitä nopeammin skannerit liikkuvat. Mitä lähempänä ne ovat toisiaan, sitä hitaammin skannerit liikkuvat.

{% hint style="info" %}
Liberationin uudemmissa versioissa varsinainen _point rate_ (lisäasetuksissa) ei vaikuta skannerin nopeuteen lainkaan. Sen sijaan renderer säätää pisteiden jakaumaa valitun pisteenopeuden mukaiseksi ja pitää samalla skannerien liikkeen muuttumattomana.

Tämä vaikuttaa pistepolun “resoluutioon”, mutta sillä on merkitystä lähinnä grafiikassa (ja se voi auttaa _scanner sync_ -asetuksen tarkemmassa säädössä).
{% endhint %}

#### Hienoa! Mitä tämä kaikki siis käytännössä tarkoittaa?

Hyvä kysymys. Tässä vinkkini:

* Vältä brändäämättömiä skannereita. Jos saat nopeammat skannerit, valitse ne – vähintään 30KPPS.
* Useimmissa tapauksissa DT30-skannerit riittävät hyvin, ja PT30-skannerit ovat todennäköisesti OK edullisemmissa lasereissa.
* Jos teet grafiikkaa, useimmissa tapauksissa useampi laser on parempi kuin nopeammat skannerit.
* Kun siirryt korkeatasoisempiin kokoonpanoihin, mikä tahansa vakiintuneista huippumerkeistä toimii hyvin.
* Jos saat käyttöösi vain halvimmat brändäämättömät skannerit, Liberationin oletusasetukset ovat melko varovaisia ja saat todennäköisesti OK-tuloksia peruskeilatyöskentelyyn. Jos skannerit eivät pysy mukana, pienennä **Speed**-asetusta (mutta älä muuta pisteenopeutta!).

#### Entä ILDA Test Pattern?

…on edelleen erittäin hyödyllinen kalibrointi- ja vertailutyökalu, mutta sitä ei koskaan suunniteltu kattavaksi vertailuarvoksi, ja valmistajat voivat käyttää tai tulkita sitä väljästi.
