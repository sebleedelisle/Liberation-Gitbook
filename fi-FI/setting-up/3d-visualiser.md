---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Johdanto

Liberationin 3D visualiser on erittäin hyödyllinen ominaisuus: voit suunnitella ja viimeistellä esityksiä ilman yhtäkään laseria. Se on osoittautunut minulle korvaamattomaksi työkaluksi erityisesti monimutkaisissa kokoonpanoissa, joissa on paljon lasereita.

### 3D-tilassa liikkuminen

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>3D Visualiser -näkymä</p></figcaption></figure>

* Kierrä näkymää kiertopisteen ympäri napsauttamalla ja vetämällä.
* Siirry lähemmäs kiertopistettä tai kauemmas siitä hiiren rullalla.
* Siirrä kameraa sivusuunnassa (strafe) vasemmalle, oikealle, ylös ja alas XY-tasossa napsauttamalla ja vetämällä samalla, kun pidät Shift-näppäintä painettuna.
* Palauta kameran sijainti kaksoisnapsauttamalla missä tahansa visualiserin alueella.

### Asetukset

Avaa _3D Visualiser Settings_ -paneeli _Window_-valikosta.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings -paneeli</p></figcaption></figure>

* **Visualiser size** - muuttaa visualiserin kokoa suhteessa muuhun sovellukseen.
* **Brightness Adjustment** - muuttaa sitä, kuinka kirkkaina laserit näkyvät.
* **Show laser numbers** - näyttää kunkin laserin numeron sen yläpuolella.
* **Show zone names** - näyttää kunkin laserin alla siihen liittyvien zonejen nimet.

### Kameran asetukset

Nämä asetukset liittyvät pääasiassa 3D-tilan virtuaalikameraan. Näet pudotusvalikon, jossa on näiden asetusten esiasetuksia. Voit tallentaa ja ladata niitä uudelleen.

* **Camera distance -** Kamera osoittaa aina _Orbit point_ -pisteeseen. Camera distance määrittää, kuinka kaukana kamera on tästä pisteestä. Voit säätää tätä asetusta myös hiiren rullalla.
* **FOV -** Field of view eli näkökenttä määrittää, kuinka laajakulmainen tai zoomattu kameran näkymä on.
* **Orbit position** - kuvaa nykyistä kiertoa kiertopisteen ympäri. Ensimmäinen arvo on kierto X-akselin ympäri (pitch) ja toinen arvo kierto Y-akselin ympäri (yaw).
* **Orbit centre point** - kiertopisteen sijainti 3D-tilassa: x, y, z.
* **Grid height** - ruudukon korkeus "maasta" (eli kohdasta, jossa y = 0).

### Sisällön asetukset

Nämä asetukset määrittävät, mihin laserit (ja Canvas) sijoitetaan 3D-ympäristössä. Näet pudotusvalikon, jossa on näiden asetusten esiasetuksia. Voit tallentaa ja ladata niitä uudelleen.

#### Lasers

Jokaisella laserilla on oma asetusryhmänsä, jonka voit avata pienellä valkoisella kolmiolla.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>3D visualiserin laser-asetukset</p></figcaption></figure>

* **3D Position** - laserin x-, y- ja z-sijainti.
* **3D Orientation** - laserin kierto x-, y- ja z-akselien ympäri.
* **Flip X / Flip Y** - kääntää laserin virtuaalisen Outputin. HUOMAA, että tämän ei pitäisi olla tarpeen: on parempi korjata laitteiston mahdolliset epäjohdonmukaisuudet laserin flip-/orientation-asetuksilla.
* **Output Range horizontal / vertical** - liittyy laserin skannerien enimmäis- ja vähimmäiskulmiin. 60º on vakio, mutta voit säätää tätä, jos laserisi poikkeavat siitä.

#### Canvas

Jos käytät canvas-järjestelmää, voit myös sisällyttää canvas-kuvan 3D-näkymään. Ota valintaruutu käyttöön, jotta canvas renderöidään näkymään, ja määritä sen ulkoasu 3D-näkymässä position-, orientation- ja scale-asetuksilla.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>3D visualiserin canvas-asetukset</p></figcaption></figure>

{% hint style="info" %}
Näetkö "haamulase­reita"? 3D Visualiser toimii jossain määrin erillään laserikokoonpanosta, ja visualiserissa voi olla enemmän lasereita kuin Liberationissa. Kun lisäät laserin projektiin, visualiseriin lisätään myös uusi laserobjekti. Jos kuitenkin poistat laserin, visualiseriin jää edelleen "haamulaser"-objekti.

Poista kaikki haamulaserit napsauttamalla _Remove extra 3D laser objects_ -painiketta (3D Visualiser -asetuspaneelin alareunassa).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
