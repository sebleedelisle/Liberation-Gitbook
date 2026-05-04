---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Laser output -asetuspaneeli

Avaa _Laser output_ -asetuspaneeli valikosta _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Tämä näyttää parhaillaan valitun laserin asetukset, joita voit vaihtaa:

* laserin numeropainikkeella _Laser overview_ -paneelissa
* näppäimistön numeronäppäimillä: näppäimet 1–0 avaavat laserit 1–10
* `Tab`-näppäimellä, jolla voit selata lasereita (`Shift + Tab` siirtyy taaksepäin).

Paneelin yläosassa näet:

* numeropainikkeen – klikkaa sitä armataksesi tai poistaaksesi tämän laserin armauksen. Painike on punainen, kun laser on armattu.
* _Brightness_-liukusäätimen vain tälle laserille. Huomaa, että tämä yhdistetään yleiseen kirkkauteen.
* _Test Pattern_ -kytkimen ja kuviovalitsimen. Näillä voit valita tietyn testikuvion vain tälle laserille. (Samat ohjaimet näkyvät myös Output-näkymän työkalupalkissa.)

### Output orientation / mirroring correction

Seuraavilla asetuksilla korjataan laserin asennus niin, että se toimii Liberationissa johdonmukaisesti.

* **Flip horizontal / vertical** – näillä asetuksilla voit korjata laserin ulostuloa

{% hint style="info" %}
Sinun ei pitäisi joutua muuttamaan horizontal / vertical flip -asetuksia, ellei laseria ole kytketty väärin tai sen takana olevat X/Y flip -painikkeet ole väärässä asennossa. Jos haluat kääntää tietyn clipin ulostulon, tee se suoraan clipissä.
{% endhint %}

* **Orientation** – jos laser on ripustettu kyljelleen tai ylösalaisin, voit korjata kierron tällä asetuksella.
* **Fine position adjustments** – voidaan käyttää hyvin pienten siirtymien tai kiertymien korjaamiseen. Tarkoitettu korjaamaan pientä elämistä tai asettumista, jos laser on ollut paikallaan yön yli tai pitkän ajan.

{% hint style="info" %}
Huomaa, että orientation / mirroring -korjaukset eivät muuta mitään 3D Visualiserissa. Niitä käytetään varsinaisen laserin ulostulon korjaamiseen niin, että se vastaa 3D Visualiserissa näkyvää näkymää.
{% endhint %}

### Laserasetusten kopiointi

Katso [Laser output -asetuspaneeli](laser-settings.md#copy-laser-settings "mention").

### Scanner settings

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed-asetus määrittää, kuinka nopeasti skannerit liikkuvat.

{% hint style="danger" %}
Vaikka oletusasetukset ovat melko varovaiset, voit silti vahingoittaa skannereita, jos ajat niitä liian nopeasti. Ole varovainen, erityisesti kun nostat nopeutta.
{% endhint %}

{% hint style="info" %}
Tämä Speed-asetus ei muuta pisteiden lähetysnopeutta, vaan säätää sitä, kuinka harvassa tai tiheässä pisteet ovat. Lisätietoja: [◼️ Miten Liberation luo lasersisältöä](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Säde vaihtaa väriä sekä kytkeytyy päälle ja pois, kun skannerit liikuttavat sitä. Nämä kaksi asiaa eivät yleensä ole täysin synkronissa keskenään. Säädä tätä asetusta, jotta ajoitus saadaan kohdalleen.

{% hint style="info" %}
Tätä kutsutaan joskus nimellä _blank shift_, mutta itse pidän termistä _scanner sync_ – se on hieman tarkempi, koska asetus säätää kaikkien värimuutosten ajoitusta suhteessa skannerien liikkeeseen.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laserin ”hännät” – Colour shift ei ole oikein säädetty</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Ei laserin ”häntiä”! Colour shift on kohdallaan!</p></figcaption></figure></div>

Jos laserin ulostulossa näkyy pieniä ”häntiä”, scanner sync vaatii todennäköisesti säätöä. Jos hännät näkyvät edelleen asetuksesta riippumatta, ajat skannereita tai laserin ohjaimia todennäköisesti nopeammin kuin ne kestävät. Kokeile laskea skannerien nopeutta.

#### Scanner presets

Tällä valitaan valmis skanneriasetus. Oletusvaihtoehto on yleensä sopiva, joten tätä asetusta ei pitäisi tarvita muuttaa, elleivät skannerisi ole erityisen huonot (tai hyvät). Jos haluat perehtyä tarkemmin, katso [◼️ Skanneriesiasetukset ja renderöintiprofiilit](../advanced/scanner-presets.md "mention")

#### Colour calibration

Tällä järjestelmällä voit korjata laserin kirkkauskäyrää ja valkotasapainoa. Katso [Värikalibrointi](../advanced/colour-calibration.md "mention")

#### Advanced settings

Näihin ei yleensä tarvitse koskea, mutta jos olet kiinnostunut, katso [◼️ Laserin lisäasetukset](../advanced/advanced-laser-settings.md "mention")
