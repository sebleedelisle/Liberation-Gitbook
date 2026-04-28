---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator-nodet

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Tekee yksittäisen pisteen / säteen.

* **Render profile** - katso [render-profile.md](fundamentals/render-profile.md)
* **Colour** - pisteen väri. Katso [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x**- ja **y**-sijainti - katso [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Tekee viivan / tason.

* **Render profile** - katso [render-profile.md](fundamentals/render-profile.md)
* **Size** - viivan pituus
* **Colour** - viivan väri. Katso [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x**- ja **y**-sijainti - katso [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - viivan kulma asteina
* **resolution** - katso [resolution.md](fundamentals/resolution.md)
* **alignment** - _LEFT / CENTRE / RIGHT -_ määrittää viivan aloituspisteen ja kierron keskipisteen
* _MOVE TO FRONT / MOVE TO BACK_ - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Tekee ympyrän / kartion.

* **Render profile** - katso [render-profile.md](fundamentals/render-profile.md)
* **radius** - ympyrän säde
* **Colour** - ympyrän väri. Katso [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x**- ja **y**-sijainti - katso [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **resolution** - katso [resolution.md](fundamentals/resolution.md)
* **Fill state** - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Tekee säännöllisen monikulmion, kuten kolmion, neliön tai viisikulmion.

* **Render profile** - katso [render-profile.md](fundamentals/render-profile.md)
* **size** - etäisyys keskeltä kuhunkin kulmaan
* **Colour** - monikulmion väri. Katso [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x**- ja **y**-sijainti - katso [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - muodon kiertokulma asteina
* **resolution** - katso [resolution.md](fundamentals/resolution.md)
* **Fill state** - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Lataa SVG-tiedoston omia muotoja varten.

{% hint style="warning" %}
Liberation on yhteensopiva _SVGTiny_-muodon kanssa. InkScapea suositellaan, mutta useimmat vektorigrafiikkasovellukset osaavat viedä tähän muotoon. Muunna kaikki teksti muodoiksi ennen vientiä. Liberation renderöi viivat ja voi haluttaessa käyttää täyttöjä maskeina. Varmista, etteivät viivat ole mustia, muuten ne eivät näy ilman värimuokkainta!
{% endhint %}

* **Import SVG** - lataa SVG-tiedosto levyltä.

{% hint style="info" %}
Kun SVG on ladattu, sisältö muunnetaan ja tallennetaan clipin sisään. Siksi tiedostoviittausta ei tarvitse säilyttää, ellet myöhemmin halua muuttaa maskiasetuksia.
{% endhint %}

* **Use fills as masks** - käsittelee kaikki täytetyt muodot maskeina, eli mustalla täytettyinä. Tämä asetetaan automaattisesti, jos SVG:ssä on täytettyjä muotoja. Jos täytettyjä muotoja ei ole, asetus poistetaan käytöstä. Katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - jos SVG:n muodoissa ei ole ääriviivaa, niitä ei voida piirtää! Tämä asetus lisää ääriviivan (eli _stroke_) kaikkiin täytettyihin muotoihin. Jos SVG:ssä ei ole lainkaan viivallisia muotoja, asetus otetaan käyttöön automaattisesti. Jos siinä ei ole täytettyjä muotoja, asetus poistetaan käytöstä.
* **Invert black lines** - jos kaikki SVG:n viivat ovat mustia, niitä ei näy! Tämä asetus muuttaa ne valkoisiksi. Asetus otetaan käyttöön automaattisesti, jos SVG:ssä on vain mustia muotoja, mutta se poistetaan käytöstä, jos mustia muotoja ei ole.
* **Render profile** - katso [render-profile.md](fundamentals/render-profile.md)
* **scale** - säätää SVG:n kokoa. Tämä lasketaan automaattisesti, kun SVG ladataan (jotta kuva varmasti näkyy), mutta arvoa voi myöhemmin muokata käsin.
* **x**- ja **y**-sijainti - katso [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - kuvan kiertokulma asteina
* **resolution** - katso [resolution.md](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Luo animaation SVG-tiedostojen sarjasta.

* **Import SVG Sequence** - valitse kansio, jossa kaikki SVG-tiedostot ovat. Huomaa, että tiedostot ladataan aakkosnumeerisessa järjestyksessä.

{% hint style="info" %}
Kun SVG-sarja on ladattu, sisältö muunnetaan ja tallennetaan clipin sisään. Siksi tiedostoviittauksia ei tarvitse säilyttää, ellet myöhemmin halua muuttaa maskiasetuksia.
{% endhint %}

* **Use fills as masks** - käsittelee kaikki täytetyt muodot maskeina, eli mustalla täytettyinä. Tämä asetetaan automaattisesti, jos jossakin SVG:ssä on täytettyjä muotoja. Jos missään ei ole täytettyjä muotoja, asetus poistetaan käytöstä. Katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - jos SVG:iden muodoissa ei ole ääriviivoja, niitä ei voida piirtää! Tämä asetus lisää ääriviivan (eli _stroke_) kaikkiin täytettyihin muotoihin. Jos SVG:issä ei ole lainkaan viivallisia muotoja, asetus otetaan käyttöön automaattisesti. Jos yhdessäkään ei ole täytettyjä muotoja, asetus poistetaan käytöstä.
* **Invert black lines** - jos kaikki SVG:iden viivat ovat mustia, niitä ei näy! Tämä asetus muuttaa ne valkoisiksi. Asetus otetaan käyttöön automaattisesti, jos SVG:issä on vain mustia muotoja, mutta se poistetaan käytöstä, jos mustia muotoja ei ole.
* **Render profile** - katso [render-profile.md](fundamentals/render-profile.md)
* **scale** - säätää kuvan kokoa.
* **x**- ja **y**-sijainti - katso [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - kuvan kiertokulma asteina
* **resolution** - katso [resolution.md](fundamentals/resolution.md)
* **speed** - koko animaation kesto tahteina.
* **time per frame** - jos tämä on käytössä, kesto koskee jokaista ruutua eikä koko animaation pituutta. Jos _speed_-arvoksi on asetettu ¼, jokainen ruutu kestää 1 iskun.
* **animation direction** -
  * _FORWARDS_ - animaatio etenee eteenpäin ja palaa sitten silmukassa alkuun
  * _BACKWARDS_ - animaatio etenee taaksepäin ja palaa sitten silmukassa loppuun
  * _PINGPONG_ - animaatio etenee eteenpäin ja sitten taaksepäin silmukassa
  * _MANUAL_ - nykyinen ruutu asetetaan _position manual_ -asetuksella
* **position manual** - aseta nykyinen ruutu: 0 % on ensimmäinen ruutu ja 100 % viimeinen ruutu. Tämän voi asettaa käsin tai ulkoisella oskillaattorilla.
* _MOVE TO FRONT / MOVE TO BACK_ - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Luo tekstiä TrueType- tai OpenType-fontilla.

* **Text** - kirjoita haluamasi teksti tähän
* **Font** - valitse haluamasi fontti

{% hint style="info" %}
Voit lisätä Liberationiin fontteja kopioimalla .ttf- tai .otf-tiedostot data/resources/fonts-kansioon.
{% endhint %}

* **Render profile** - katso [render-profile.md](fundamentals/render-profile.md)
* **horizontal alignment** - valitse tekstin tasaus: _LEFT_, _CENTRE_ tai _RIGHT_.
* **Fill state** - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* **size** - tekstin koko
* **colour -** katso [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x**- ja **y**-sijainti - katso [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - kuvan kiertokulma asteina
* **resolution** - katso [resolution.md](fundamentals/resolution.md)
* **reveal** - käytä tätä tekstin asteittaiseen paljastamiseen merkki kerrallaan. Kun arvo on välillä 0–50 %, teksti ilmestyy vähitellen vasemmalta oikealle. Kun arvo on välillä 50–100 %, teksti katoaa vasemmalta oikealle. Voit liittää tähän liitäntään oskillaattorin animaatioita varten.
* **reveal by word** - kun tämä on käytössä, _reveal_ toimii sana kerrallaan eikä merkki kerrallaan.
* **countdown** - nopeasti toteutettu lähtölaskentajärjestelmä. Arvo muuttuu 2 iskun välein, joten jos haluat sekunteja, varmista että tempo on 120 bpm.
* **countdown start** - numero, josta haluat lähtölaskennan alkavan
* _MOVE TO FRONT / MOVE TO BACK_ - katso [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
