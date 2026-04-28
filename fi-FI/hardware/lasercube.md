---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube-mainoskuva Wicked Lasersin luvalla</p></figcaption></figure>

Wicked Lasersin [LaserCube](https://www.laseros.com/lasercube/) on erittäin kompakti akkukäyttöinen laseryksikkö, jota on saatavilla useina eri tehoversioina. Se on suosittu harrastajien keskuudessa helppokäyttöisen älypuhelinsovelluksen ansiosta, mutta uusimmat mallit ovat riittävän suorituskykyisiä myös ammattiesityksiin.

Puhelinsovellus (nimeltään LaserOS, saatavilla myös työpöytäversiona) on ladattavissa ilmaiseksi. Sillä on hauska leikkiä, ja se riittää hyvin useimmille käyttäjille. Jos kuitenkin ajat suurempia esityksiä useilla lasereilla, tarvitset erikoistuneemman ja tehokkaamman ratkaisun – tässä kohtaa Liberation tulee mukaan.

### LaserCuben liittäminen

Varhaisia LaserCube-malleja ohjataan USB:n kautta, mutta nykyisissä malleissa on sisäänrakennettu verkkokontrolleri. Näitä verkon kautta ohjattavia kuutioita kutsutaan nimellä "LaserCube Wifi". Liberation tukee molempia LaserCube-tyyppejä\*, oli yhteys sitten USB:n kautta tai verkossa.

\*(LaserCube-verkkoprotokollan tuki lisättiin versiossa 0.7.3)

### USB LaserCube

Liitä LaserCube tietokoneeseen micro USB -kaapelilla ja etsi se sitten _Controller Assignment_ -paneelista (katso [controller-assignment.md](../setting-up/controller-assignment.md)). Jos se ei tule näkyviin automaattisesti, paina _REFRESH_-painiketta.

### Network LaserCube "Wifi"

{% hint style="danger" %}
Vaikka "Wifi"-kuutiot on suunniteltu käytettäviksi langattomassa verkossa, sitä ei suositella. Yhteyteen tulee todennäköisesti katkoksia ja häiriöitä. Käytä sen sijaan RJ45-liitäntää ja yhdistä LaserCube langalliseen verkkoon, aivan kuten Ether Dreamien kanssa.
{% endhint %}

Liitä LaserCube langalliseen verkkoon.

Aseta LaserCube "LAN Client" -tilaan ja varmista, että verkossa on reititin. LaserCube saa IP-osoitteen reitittimeltä, minkä jälkeen sen pitäisi näkyä _Controller Assignment_ -paneelissa. (Katso [controller-assignment.md](../setting-up/controller-assignment.md)).

{% hint style="info" %}
Verkon voi määrittää myös ilman reititintä antamalla kaikille laitteille kiinteät IP-osoitteet, ja tämä on hyvin yleistä tapahtuma-alalla. Itse lisään mieluummin verkkoon reitittimen ja suosittelen tätä vaihtoehtoa kaikille, joilla on vähemmän verkkokokemusta.

Reititin jakaa IP-osoitteet kaikille laitteille dynaamisesti. Minusta se on yksinkertaisempaa ja vähentää virheiden mahdollisuutta.
{% endhint %}

{% hint style="danger" %}
Toisin kuin Ether Dream, _**LaserCubet EIVÄT SAMMUTA LASERSÄDETTÄ**_, jos niissä tapahtuu puskurin alivuoto, paketin menetys tai muuta vioittunutta / virheellistä dataa.

Sen sijaan ne jatkavat siitä, mihin jäivät. Joissakin tapauksissa tämä voi aiheuttaa sen, että aktiivinen säde kulkee alueiden läpi, jotka eivät ole zone-alueiden sisällä, ja mikä vielä pahempaa, leikkaa ohjelmistomaskien läpi.

Olen yhteydessä LaserCuben suunnittelijoihin/kehittäjiin, ja toivon, että tämä korjataan tulevaisuudessa laiteohjelmistopäivityksellä. Siihen asti sinun on kuitenkin varmistettava, että maskaat fyysisesti kaikki alueet, joihin et halua laserin osuvan.

Rehellisesti sanottuna tämä kannattaa luultavasti tehdä joka tapauksessa, mutta itse käytän ohjelmistomaskeja kameroiden ja projektorien suojaamiseen. Huomioi siis, että tämä on LaserCuben verkkoprotokollaa käytettäessä vaarallisempaa kuin Ether Dreamin kanssa, koska Ether Dream siirtyy turvapysäytystilaan heti, kun tapahtuu mikä tahansa virhe tai dataa puuttuu.

Lisäksi olen sanonut tämän jo aiemmin, mutta **käytä langallista yhteyttä LaserCubeen**. Wifi ei yksinkertaisesti riitä, ja se pahentaa tätä ongelmaa entisestään.
{% endhint %}
