---
description: >-
  Laserit voivat olla vaarallisia, joten hyvien käytäntöjen ja
  turvallisuusohjeiden noudattaminen on tärkeää. Tämä sivu antaa hyödyllisen
  yleiskuvan, joka auttaa lasereiden turvallisessa käyttöönotossa.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/setting-up-lasers
---

# ✅ Lasereiden käyttöönoton prosessin yleiskatsaus

### Yleiskuva lasereiden turvallisesta käynnistämisestä

Tämä opas ei korvaa virallista laserturvallisuuskoulutusta, jota tarvitset ehdottomasti ennen kuin käytät lasereita julkisissa tiloissa tai yleisön edessä. Joillakin alueilla on lisäksi lakisääteisiä vaatimuksia, mutta joka tapauksessa sinun tulee aina noudattaa turvallisuuden ja ammattimaisen toiminnan parhaita käytäntöjä.

PLASA tarjoaa maksutta ladattavan laserturvallisuusoppaan, jota pidetään yleisesti hyvänä käytäntönä: [https://www.plasa.org/guidance-for-display-lasers/](https://www.plasa.org/guidance-for-display-lasers/)

Varmista ennen käyttöä, että ymmärrät lasereihin liittyvät turvallisuusvaikutukset!

#### Johdanto

Tämän sivun tarkoitus on antaa yleiskuva siitä, miten laserit käynnistetään turvallisesti. Kunkin vaiheen tarkemmat ohjeet käsitellään myöhemmin tässä osiossa, mutta tämä sivu auttaa hahmottamaan kokonaisuuden. Voit palata siihen myöhemmin viitteeksi aina, kun otat lasereita käyttöön.

<figure><img src="../.gitbook/assets/laser-aperture.jpg" alt=""><figcaption><p>Tyypillinen laserin sädeaukon suojus</p></figcaption></figure>

### Määritä laitteisto:

1. **Sulje laserin sädeaukon suojus**
2. **Kiinnitä laser turvallisesti** ja suuntaa se oikeaan suuntaan
3. **Liitä pysäytyspainike** laseriin
4. **Liitä laser controller** tietokoneeseen
5. **Kytke laseriin virta**

### Määritä Liberation:

1. **Varmista, että kaikki laserit ovat disarmed-tilassa** ja etsi ja yhdistä controller Liberationissa
2. **Laske&#x20;**_**Global Brightness**_**&#x20;-asetus arvoon 0** (käytä kuvakepalkin liukusäädintä tai APC40:n _Master Fader_ -säädintä)
3. **Aseta laser armed-tilaan** – pidä sädeaukon suojus edelleen suljettuna, varmista ettei mikään Clip ole aktiivinen, ja aseta laser armed-tilaan (käytä _Laser Overview_ -paneelin _Arm_ -painiketta)
4. **Ota test pattern käyttöön** (käytä kuvakepalkin ☒-painiketta ja valitse pattern 1, vihreä neliö jossa on risti)
5. **Säädä output zone** – arvioi turvallisin koko ja sijainti zone-alueelle (esimerkiksi suoraan korkealle kattoon, mutta tämä riippuu omasta ympäristöstäsi)
6. **Varmista, että laser toimii** – nosta kirkkautta hitaasti, kunnes näet valoa sädeaukon ikkunan takana. Laske kirkkaus sen jälkeen takaisin nollaan.
7. **Testaa pysäytyspainike** varmistaaksesi, että kaikki laserin output sammuu, kun painiketta painetaan

### Lasersäteilyn käynnistäminen

1. **Tyhjennä altistusalue** – varmista, ettei kukaan voi altistua laserille, ja ohjeista koko henkilökunta pysymään poissa altistusalueelta lasereiden käyttöönoton aikana. (Varmista myös, että kaikki kamerat ja projektorit on peitetty tai että niiden linssinsuojukset ovat paikallaan!)
2. **Avaa sädeaukon suojus** – seiso sivussa ja poissa output-suunnasta ja liu'uta sädeaukon suojus alas. Jos zones ovat korkealla, voit jättää suojuksen osittain kiinni.
3. **Nosta kirkkautta, kunnes laser juuri ja juuri näkyy** – pidä laser vain niin kirkkaana kuin on tarpeen zone-alueen näkemiseksi
4. **Säädä zone tai zones** – määritä zone-kohteen koko, muoto ja sijainti niin, että se on 3 m lattian yläpuolella kaikista yleisölle avoimista alueista eikä laser ulotu muille yleisölle avoimille alueille
5. **Lisää fyysinen rajaus** – käytä sädeaukon suojusta ja/tai mustaa folioteippiä rajaamaan fyysisesti kaikki halutun zone-alueen ulkopuoliset kohdat. Tämä on erittäin tärkeää, koska mikä tahansa laserlaite tai ohjelmisto voi toimia virheellisesti.
6. **Lisää ohjelmistopohjaiset masks** – Liberationin ohjelmistopohjaisia masks-toimintoja voidaan käyttää kameroiden ja projektorien suojaamiseen, mutta niitä ei pidä **koskaan** käyttää fyysisen rajauksen sijasta ihmisten suojaamiseen. Huomaa, että mikään ohjelmisto tai laitteisto ei ole erehtymätön, joten varmista, että ymmärrät riskit ennen ohjelmistopohjaisten masks-toimintojen käyttöä.

{% hint style="warning" %}
Huomaa, että tämä opas olettaa sisätiloissa tehtävän käyttöönoton. Jos työskentelet ulkona, lentoturvallisuuden varmistamiseksi on tehtävä lisätoimia, mukaan lukien mutta ei rajoittuen seuraaviin:

* Tarvittavien lupien hankkiminen ilmailuviranomaisilta, kuten FAA:lta tai CAA:lta
* Yhteydenpito läheisten lentoasemien ja lentopaikkojen kanssa
* Julkisen lentotutkan tarkistaminen sekä tähystäjän nimeäminen tarkkailemaan ilma-aluksia

Myös selvästi turvallisuusrajan alapuolella olevat laserit voivat aiheuttaa lentäjille vakavia häiriöitä.

Varmista, että sinulla on tarvittavat pätevyydet, lisenssit ja luvat ennen kuin suuntaat mitään lasereita ilmatilaan.
{% endhint %}
