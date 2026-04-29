---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Efektit

Liberationin efektijärjestelmä on hauska ja monipuolinen tapa muuttaa klipin ulostuloa reaaliajassa. Efektit ovat täysin joustavia: voit saada kaiken vilkkumaan päälle ja pois, pyörimään, vaihtamaan väriä tai vaikka liikkumaan satunnaisesti ympäriinsä!

Kaikkea, mitä voit tehdä klippieditorissa, voi käyttää efektinä. Itse asiassa efektejä muokataan täsmälleen samalla node-editorilla kuin klippejä! Katso [Efektit](effects.md#editing-effects). Luovat mahdollisuudet ovat käytännössä rajattomat.

Oletusarvoiset efektipainikkeet 1–8 ovat zone-painikkeiden alla, ja efektit 9–24 ovat alareunan pienet painikkeet.

#### Efektin käyttäminen

Paina efektipainiketta kytkeäksesi efektin päälle tai pois. Vielä parempi tapa on käyttää APC40-liukusäätimiä 1–8 efektien häivyttämiseen sisään ja ulos. Jos käytössäsi ei ole APC40:tä, häivytä efekti sisään klikkaamalla painiketta ja vetämällä ylös tai alas. Voit myös klikata efektipainiketta hiiren oikealla painikkeella ja säätää level-liukusäädintä.

{% hint style="warning" %}
Efektipainikkeen painaminen aktivoi kyseisen efektin heti. Huomaa kuitenkin, että jos taso on nollassa, mitään ei tapahdu! Muuta tasoa klikkaamalla ja vetämällä painiketta, klikkaamalla hiiren oikealla ja käyttämällä _level_-liukusäädintä tai käyttämällä APC40:n fadereita.
{% endhint %}

#### Efektit ja klipin zone delay

Efektit perivät jokaisen parhaillaan käynnissä olevan klipin zone delay -asetuksen. Jos klipissäsi on esimerkiksi viive, joka liikkuu vasemmalta oikealle, ja lisäät vilkkuefektin, myös välähdys viivästyy vasemmalta oikealle.

{% hint style="info" %}
Sitä, miten klipin zone delay periytyy efekteihin, on erittäin vaikea selittää, mutta se on ilmeistä, kun kokeilet sitä!

Väittäisin, että se on yksi Liberationin hauskimmista ja luovimmista sisäänrakennetuista työkaluista. Kokeile, niin näet mitä tarkoitan!
{% endhint %}

#### Efektin parametrit

Lisää efektiin parametri _Parameter node_ -nodella. Parameter-järjestelmän avulla voit säätää useita efektin sisäisiä asetuksia ulkopuolelta. Katso lisätietoja: [Parameter Control](clip-editor/oscillators/parameter-control.md).

Säädä kunkin efektin _parameter_-arvoa rotary controller -säätimillä 1–8. Voit myös klikata efektipainiketta hiiren oikealla painikkeella ja säätää parameter-liukusäädintä tai -säätimiä. Parametrin muutos tekee eri asioita sen mukaan, miten efekti on rakennettu. Alla olevassa luettelossa kerrotaan oletusefektit ja mitä niiden parametrit tekevät.

{% hint style="info" %}
Rotary controllers 1-8 ovat APC40 Mk2:n yläreunassa ja Mk1:ssä oikeassa yläkulmassa. Katso myös: [APC40-viite](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
Efektipainikkeissa näkyvät pienet numerot viittaavat efektin _level_- ja _parameter_-arvoihin. _level_-arvoa ohjataan APC40:n faderilla, tai voit klikata ja vetää painiketta. Parameter-arvoa säädetään APC40:n rotary-säätimillä, tai voit klikata hiiren oikealla ja säätää sitä hiirellä.
{% endhint %}

#### Oletusefektit

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Lisää klipin ulostuloon kaoottista liikettä. Parametri säätää kaaoksen määrää/nopeutta.
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
   Muuttaa kaiken sävyä ja myös kyllästää värin täysin (eli kaikki valkoinen muuttuu kyseiseksi väriksi). Parametri säätää sävyä.
8. **Flash** :\
   Vilkuttaa kaiken kirkkautta toistuvasti täydestä nollaan. Parametri säätää vilkkumisnopeutta.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Alarivillä on lisäksi 16 väriefektiä, joilla voit käyttää valmiiksi asetettuja hue- ja saturation-arvoja.

Huomaa, että nämä ovat oletusefektejä, mutta niitä voi muokata tekemään lähes mitä tahansa haluat!

### Apply to groups

Voit valita, mihin ryhmiin efekti vaikuttaa. Klikkaa hiiren oikealla ja kytke päälle tai pois ryhmien valintaruudut, joiden nimi on _Apply to groups._

Käytän tätä asetusta itse pääasiassa silloin, kun käsittelen Canvas-grafiikkaa ja lasersäteitä erikseen. Määritän kaikki Canvas-klipit ryhmään 5 ja jätän tämän ryhmän pois efekteistä, joiden en halua vaikuttavan näihin graafisiin klippeihin.

Voit käyttää tätä myös live-tilanteessa kahden eri värimuutoksen käyttämiseen kahdelle laseriryhmälle samaan aikaan. Luo kaksi värinvaihtoefektiä ja valitse, mihin klippiryhmiin kumpaakin käytetään.

### MX group

_Mutually Exclusive_ -lyhenne. Tällä tavalla voit ryhmitellä efektejä niin, että vain yksi ryhmän efekti voi olla aktiivinen kerrallaan. Huomaa, että vain yksi oletusarvoisista väriä vaihtavista efekteistä voi olla aktiivinen kerrallaan. Tämä johtuu siitä, että ne kaikki ovat MX Group 1 -ryhmässä.

Tämä toiminto ei ole käytössä, jos _MX Group_ -asetus on 0.

### Efektien muokkaaminen

Klikkaa mitä tahansa efektiä hiiren oikealla painikkeella ja avaa efektieditori klikkaamalla _EDIT EFFECT_ -painiketta. Huomaa, että tämä editori on identtinen klippieditorin kanssa!

Muokkaa efektiä samalla tavalla kuin mitä tahansa klippiä. Katso [clip-editor](clip-editor/).

Efektissä täytyy olla vähintään yksi creator-node. Se voi olla mikä tahansa (viiva, ympyrä, muoto, jopa teksti!), mutta yleensä kannattaa valita jokin, joka näyttää efektipainikkeen esikatselussa järkevältä.

Kun efektejä käytetään, kaikki efektin creator-nodet korvataan parhaillaan käynnissä olevien klippien ulostulolla.

{% hint style="warning" %}
Erittäin puuduttavista teknisistä syistä "trails"-nodet eivät ole käytössä efektin sisällä. Sama koskee pattern-nodejen "delay"-asetusta (ne käyttävät samaa järjestelmää). Tämä korjataan tulevissa versioissa.
{% endhint %}
