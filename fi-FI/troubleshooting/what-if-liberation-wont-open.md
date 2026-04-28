---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Mitä jos Liberation ei avaudu?

Tämä on harvinaista, mutta joskus Liberation ei ehkä käynnisty tai se kaatuu heti avaamisen jälkeen. Tämä johtuu lähes aina siitä, että jokin paikallinen määritystiedosto on vioittunut – yleensä järjestelmän kaatumisen tai muun tietokoneella tapahtuneen odottamattoman tilanteen jälkeen.

Onneksi ongelma on helppo korjata nollaamalla paikalliset asetukset. Näin teet sen macOS- ja Windows-järjestelmissä.

> **Tärkeää**
>
> * Sulje Liberation ennen kuin teet mitään.
> * Nämä vaiheet vaikuttavat vain paikallisiin asetuksiin, lokeihin ja välimuisteihin. Lisenssisi ja tilisi ovat turvassa.

***

#### Mistä työkansio löytyy

Jokaisella Liberation-versiolla on oma työkansionsa. Jos käytössäsi on esimerkiksi versio 1.0.0, kansion nimi on 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Kansion avaaminen nopeasti**

**macOS**

1. Paina Finderissa **Shift + Cmd + G**.
2.  Liitä tämä polku ja paina **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Avaa kansio, joka vastaa versionumeroasi, esimerkiksi `1.0.0`.

**Windows**

1.  Paina **Win + R**, liitä tämä ja paina **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Avaa kansio, joka vastaa versionumeroasi, esimerkiksi `1.0.0`.

> **Vinkki Windowsille**: Jos selaat kansioon File Explorerin kautta, ota piilotetut kohteet käyttöön: **View > Show > Hidden items**.

***

#### Vaihe 1 – Nollaa asetustiedosto turvallisesti

Avaa versiokansiosi sisältä:

```
data/liberation/
```

liberation-kansiosta pitäisi löytyä tiedosto nimeltä se`ttings.json`. Poista tämä tiedosto.

* **macOS-esimerkki**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows-esimerkki**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Yritä nyt käynnistää Liberation. Jos se avautuu, olet valmis.

***

#### Vaihe 2 – Tarkista, onko jokin Clip ongelmallinen

Jos Liberation kaatui, kun muokkasit Clip-tiedostoa, ongelma voi johtua kyseisestä Clip-tiedostosta.

Samasta kansiosta kuin settings.json-tiedosto pitäisi löytyä tiedosto nimeltä clipEdit`.json`

Varmuuskopioi tämä tiedosto turvalliseen paikkaan (esimerkiksi Desktop-kansioon) ja poista se sitten Liberationin työkansiosta.

Yritä käynnistää Liberation uudelleen. Jos se avautuu nyt normaalisti, lähetä varmuuskopioitu tiedosto sähköpostitse osoitteeseen [**info@liberationlaser.com**](mailto:info@liberationlaser.com), jotta voimme selvittää ongelman syyn.

***

#### Vaihe 3 - Varmuuskopioi ja poista sitten koko työkansio

Jos Vaihe 1 ja Vaihe 2 eivät auttaneet:

1. **Varmuuskopioi** koko versiokansio:
   * macOS: Napsauta `1.0.0`-kansiota hiiren oikealla painikkeella ja valitse **Compress** luodaksesi zip-tiedoston, tai kopioi kansio turvalliseen paikkaan, kuten Desktop-kansioon.
   * Windows: Napsauta `1.0.0`-kansiota hiiren oikealla painikkeella ja valitse **Send to > Compressed (zipped) folder**, tai kopioi kansio turvalliseen paikkaan, kuten Desktop-kansioon.
2. Kun varmuuskopio on tehty, **poista** alkuperäinen `1.0.0`-kansio Liberationin työkansion sijainnista.
3. Käynnistä Liberation uudelleen. Se luo uuden puhtaan työkansion.

Jos Liberation avautuu nyt, siirry Vaiheeseen 4.

***

#### Vaihe 4 - Lähetä varmuuskopio meille

Tämä auttaa meitä tunnistamaan ongelman syyn, jotta voimme estää sen tulevissa versioissa.

Pakkaa Vaiheessa 3 luotu **varmuuskopio** zip-tiedostoksi, jos et tehnyt sitä jo, ja lähetä se sitten sähköpostitse, jotta voimme selvittää syyn.

* **Vastaanottaja**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Aihe**: Liberationin käynnistyskorjaus - työkansion varmuuskopio
* **Viesti**: Sisällytä mukaan:
  * Käyttöjärjestelmä ja versio (esim. macOS 14.6 tai Windows 11 23H2)
  * Liberation-versio (esim. 1.0.0)
  * Mikä vaihe korjasi ongelman, jos jokin (Vaihe 1, Vaihe 2 tai Vaihe 3)
  * Lyhyt kuvaus siitä, mitä tapahtui ennen ongelman alkamista
* **Liite**: zip-pakattu varmuuskopio `1.0.0`-työkansiostasi.

> Jos zip-tiedosto on liian suuri sähköpostiin, lataa se pilvitallennuspalveluun ja jaa linkki.

***

#### Eikö Liberation vieläkään käynnisty Vaiheen 3 jälkeen?

Jos Liberation ei vieläkään avaudu työkansion poistamisen jälkeen:

* Käynnistä tietokone uudelleen ja yritä uudestaan.
* Poista väliaikaisesti käytöstä virustorjunta- tai suojaustyökalut, jotka saattavat estää uusien kansioiden luomisen, ja yritä sitten käynnistää Liberation.
* Asenna uusin Liberation-koontiversio nykyisen asennuksen päälle.
* Jos mikään yllä olevista ei auta, ota yhteyttä tukeen osoitteessa [**info@liberationlaser.com**](mailto:info@liberationlaser.com) ja liitä mukaan tiedot sekä mahdolliset kaatumislokit `logs`-alikansiosta, jos sellaisia on.

***

#### Yhteenveto

1. Poista `data/liberation/settings.json` versioidusta työkansiostasi.
2. Jos muokkasit Clip-tiedostoa, varmuuskopioi ja poista sitten `data/liberation/clipEdit.json`.
3. Jos Liberation ei vieläkään avaudu, varmuuskopioi ja poista sitten koko `1.0.0`-kansio (tai oman versiosi kansio).
4. Jos Vaihe 3 korjaa ongelman (tai vaikka se ei korjaisi), pakkaa varmuuskopio zip-tiedostoksi ja lähetä se osoitteeseen [**info@liberationlaser.com**](mailto:info@liberationlaser.com) yhdessä käyttöjärjestelmäsi ja Liberation-version kanssa.
