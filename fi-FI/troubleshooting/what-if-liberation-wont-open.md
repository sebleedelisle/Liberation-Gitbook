---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Mitä jos Liberation ei avaudu?

Tämä on harvinaista, mutta joskus Liberation ei käynnisty tai kaatuu heti avaamisen jälkeen. Syy on lähes aina se, että jokin paikallinen määritystiedosto on vioittunut – yleensä järjestelmän kaatumisen tai muun tietokoneessa tapahtuneen odottamattoman tilanteen jälkeen.

Onneksi ongelma on helppo korjata nollaamalla paikalliset asetukset. Näin teet sen macOS- ja Windows-järjestelmissä.

> **Tärkeää**
>
> * Sulje Liberation ennen kuin teet mitään.
> * Nämä vaiheet vaikuttavat vain paikallisiin asetuksiin, lokitiedostoihin ja välimuisteihin. Lisenssisi ja tilisi ovat turvassa.

***

#### Mistä työkansio löytyy

Jokaisella Liberation-versiolla on oma työkansionsa. Jos käytössäsi on esimerkiksi versio 1.0.3, kansion nimi on 1.0.3.

* **macOS**: `~/Library/Application Support/Liberation/1.0.3`
* **Windows**: `AppData\Local\Liberation\1.0.3`

**Kansion avaaminen nopeasti**

**macOS**

1. Paina Finderissa **Shift + Cmd + G**.
2.  Liitä tämä polku ja paina **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Avaa kansio, joka vastaa versionumeroasi, esimerkiksi `1.0.3`.

**Windows**

1.  Paina **Win + R**, liitä tämä ja paina **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Avaa kansio, joka vastaa versionumeroasi, esimerkiksi `1.0.3`.

> **Vinkki Windowsiin**: Jos selaat kansioon File Explorerin kautta, ota piilotetut kohteet käyttöön: **View > Show > Hidden items**.

***

#### Vaihe 1 – Nollaa asetustiedosto turvallisesti

Avaa versiokansiosi sisältä:

```
data/liberation/
```

Liberation-kansiosta pitäisi löytyä tiedosto nimeltä `settings.json`. Poista tämä tiedosto.

* **macOS-esimerkki**: `~/Library/Application Support/Liberation/1.0.3/data/liberation/settings.json`
* **Windows-esimerkki**: `%LOCALAPPDATA%\Liberation\1.0.3\data\liberation\settings.json`

Yritä nyt käynnistää Liberation. Jos se avautuu, olet valmis.

***

#### Vaihe 2 – Tarkista, aiheuttaako Clip ongelman

Jos Liberation kaatui, kun muokkasit Clip-kohdetta, on mahdollista, että jokin kyseiseen Clip-kohteeseen liittyvässä tiedostossa aiheuttaa ongelman.

Samasta kansiosta kuin `settings.json`-tiedosto pitäisi löytyä tiedosto nimeltä `clipEdit.json`.

Tee tästä tiedostosta varmuuskopio turvalliseen paikkaan (esimerkiksi Desktop-kansioon) ja poista se sitten Liberation-työkansiosta.

Yritä käynnistää Liberation uudelleen. Jos se avautuu nyt normaalisti, lähetä varmuuskopioitu tiedosto sähköpostilla osoitteeseen [**info@liberationlaser.com**](mailto:info@liberationlaser.com), jotta voimme selvittää, mikä aiheutti ongelman.

***

#### Vaihe 3 – Varmuuskopioi ja poista sitten koko työkansio

Jos vaihe 1 ja vaihe 2 eivät auttaneet:

1. **Varmuuskopioi** koko versiokansio:
* macOS: Napsauta `1.0.3`-kansiota hiiren oikealla painikkeella ja valitse **Compress** luodaksesi zip-tiedoston, tai kopioi kansio turvalliseen paikkaan, kuten Desktop-kansioon.
* Windows: Napsauta `1.0.3`-kansiota hiiren oikealla painikkeella ja valitse **Send to > Compressed (zipped) folder**, tai kopioi kansio turvalliseen paikkaan, kuten Desktop-kansioon.
2. Kun varmuuskopio on tehty, **poista** alkuperäinen `1.0.3`-kansio Liberationin työkansion sijainnista.
3. Käynnistä Liberation uudelleen. Se luo uuden puhtaan työkansion.

Jos Liberation avautuu nyt, jatka vaiheeseen 4.

***

#### Vaihe 4 – Lähetä varmuuskopio meille

Tämä auttaa meitä selvittämään, mikä aiheutti ongelman, jotta voimme estää sen tulevissa versioissa.

Pakkaa vaiheen 3 **varmuuskopio** zip-tiedostoksi, jos et tehnyt sitä jo, ja lähetä se sitten meille sähköpostilla, jotta voimme diagnosoida syyn.

* **To**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Subject**: Liberation start-up fix - working folder backup
* **Body**: Sisällytä viestiin:
  * Käyttöjärjestelmä ja versio (esim. macOS 14.6 tai Windows 11 23H2)
* Liberation-versio (esim. 1.0.3)
  * Mikä vaihe korjasi ongelman, jos jokin (vaihe 1, vaihe 2 tai vaihe 3)
  * Lyhyt kuvaus siitä, mitä tapahtui ennen ongelman alkamista
* **Attachment**: zip-pakattu varmuuskopio `1.0.3`-työkansiostasi.

> Jos zip-tiedosto on liian suuri sähköpostiin, lataa se pilvipalveluun ja jaa linkki.

***

#### Eikö Liberation vieläkään käynnisty vaiheen 3 jälkeen?

Jos Liberation ei vieläkään avaudu työkansion poistamisen jälkeen:

* Käynnistä tietokone uudelleen ja yritä uudelleen.
* Poista väliaikaisesti käytöstä virustorjunta- tai suojaustyökalut, jotka saattavat estää uusien kansioiden luomisen, ja yritä sitten käynnistää uudelleen.
* Asenna uusin Liberation-versio nykyisen asennuksesi päälle.
* Jos mikään yllä olevista ei auta, ota yhteyttä tukeen osoitteessa [**info@liberationlaser.com**](mailto:info@liberationlaser.com) ja liitä mukaan tiedot sekä mahdolliset kaatumislokit `logs`-alikansiosta, jos sellaisia on.

***

#### Yhteenveto

1. Poista `data/liberation/settings.json` versiokohtaisesta työkansiostasi.
2. Jos muokkasit Clip-kohdetta, varmuuskopioi ja poista sitten `data/liberation/clipEdit.json`.
3. Jos Liberation ei vieläkään avaudu, varmuuskopioi ja poista sitten koko `1.0.3`-kansio (tai oman versiosi kansio).
4. Jos vaihe 3 korjaa ongelman (tai vaikka ei korjaisi), pakkaa varmuuskopio zip-tiedostoksi ja lähetä se osoitteeseen [**info@liberationlaser.com**](mailto:info@liberationlaser.com) yhdessä käyttöjärjestelmäsi ja Liberation-version kanssa.
