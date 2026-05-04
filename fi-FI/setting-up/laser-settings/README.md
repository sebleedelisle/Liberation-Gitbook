# ✅ Laser output -asetuspaneeli

Avaa _Laser output_ -asetuspaneeli valikosta _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Tämä näyttää parhaillaan valitun laserin asetukset. Voit vaihtaa valittua laseria:

* sen numeropainikkeella _Laser overview_ -paneelissa
* näppäimistön numeronäppäimellä; näppäimet 1–0 avaavat laserit 1–10
* `Tab`-näppäimellä, joka käy laserit läpi järjestyksessä (`Shift + Tab` siirtyy taaksepäin).

Paneelin yläreunassa näet:

* numeropainikkeen – napsauta sitä kytkeäksesi tämän laserin käyttövalmiiksi tai pois käyttövalmiudesta. Painike on punainen, kun laser on käyttövalmiina.
* _Brightness_-liukusäätimen vain tälle laserille. Huomaa, että tämä yhdistetään yleiseen kirkkauteen.
* _Test Pattern_ -kytkimen ja kuviovalitsimen. Niillä voit valita tietyn testikuvion vain tälle laserille. (Samat säätimet näkyvät myös Output-näkymän työkalurivillä.)

### Output orientation / mirroring correction

Seuraavilla asetuksilla korjataan laserin asetukset niin, että se toimii Liberationissa johdonmukaisesti.

* **Flip horizontal / vertical** – näillä asetuksilla voit korjata laserin ulostuloa

{% hint style="info" %}
Horizontal / vertical flip -asetuksia ei yleensä tarvitse muuttaa, ellei laseria ole johdotettu väärin tai sen takapaneelissa olevat X/Y flip -painikkeet ole väärässä asennossa. Jos haluat kääntää ulostulon vain tietyssä klipissä, tee se itse klipissä.
{% endhint %}

* **Orientation** – jos laser on asennettu kyljelleen tai ylösalaisin, voit korjata kierron tällä asetuksella.
* **Fine position adjustments** – näillä voit korjata hyvin pieniä siirtymiä tai kiertymiä. Tarkoitettu korjaamaan ryömintää tai asettumista, jos laser on ollut paikallaan yön yli tai pitkiä aikoja.

{% hint style="info" %}
Huomaa, että orientation / mirroring -korjaukset eivät muuta mitään 3D Visualiserissa. Niitä käytetään todellisen laserin ulostulon korjaamiseen niin, että se vastaa 3D Visualiserissa näkyvää!
{% endhint %}

### Copy laser settings

Katso [#copy-laser-settings](./#copy-laser-settings "mention").

### Scanner settings

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed-asetus määrittää, kuinka nopeasti skannerit liikkuvat.

{% hint style="danger" %}
Vaikka oletusasetukset ovat melko varovaiset, voit silti vahingoittaa skannereita, jos ajat niitä liian nopeasti. Ole varovainen, erityisesti kun kasvatat nopeutta.
{% endhint %}

{% hint style="info" %}
Tämä Speed-asetus ei muuta pisteiden määrää sekunnissa, vaan säätää sitä, kuinka laajalle pisteet jakautuvat. Lisätietoja on kohdassa [◼️ Miten Liberation luo lasersisältöä](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Säde vaihtaa väriä sekä kytkeytyy päälle ja pois skannereiden liikuttaessa sitä, eivätkä nämä yleensä ole täydellisesti synkronissa keskenään. Säädä tällä asetuksella ajoitus takaisin kohdalleen.

{% hint style="info" %}
Tästä käytetään joskus nimeä _blank shift_, mutta itse pidän enemmän termistä _scanner sync_ – se on hieman tarkempi, koska asetus säätää kaikkien värimuutosten ajoitusta suhteessa skannerin liikkeeseen.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laserin ”hännät” – Colour shift ei ole oikein asetettu</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Ei laserin ”häntiä”! Colour shift on kunnossa!</p></figcaption></figure></div>

Jos laserin ulostulossa näkyy pieniä ”häntiä”, Scanner sync tarvitsee todennäköisesti säätöä. Jos hännät näkyvät edelleen asetuksesta riippumatta, ajat todennäköisesti skannereita tai laserohjaimia nopeammin kuin ne kestävät. Kokeile laskea skannerinopeutta.

#### Scanner presets

Tällä valitaan valmiiksi suunniteltu skanneriasetus. Oletusasetus on yleensä sopiva, joten tätä ei pitäisi tarvita muuttaa, elleivät skannerisi ole poikkeuksellisen huonot (tai hyvät). Jos haluat perehtyä tarkemmin, katso [◼️ Skanneriesiasetukset ja renderöintiprofiilit](../../advanced/scanner-presets.md "mention")

#### Colour calibration

Tällä järjestelmällä voit korjata laserin kirkkauskäyrää ja valkotasapainoa. Katso [Värikalibrointi](../../advanced/colour-calibration.md "mention")

#### Advanced settings

Näihin ei yleensä tarvitse koskea, mutta jos olet utelias, katso [◼️ Laserin lisäasetukset](../../advanced/advanced-laser-settings.md "mention")
