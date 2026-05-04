---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator-nodet

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Tekee yksittäisen pisteen / säteen.

* **Render profile** - katso [Render Profile](fundamentals/render-profile.md "mention")
* **Colour** - pisteen väri. Katso [Väriasetukset ja HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- ja **y**-sijainti - katso [Koordinaatisto](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Tekee viivan / tason.

* **Render profile** - katso [Render Profile](fundamentals/render-profile.md "mention")
* **Size** - viivan pituus
* **Colour** - viivan väri. Katso [Väriasetukset ja HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- ja **y**-sijainti - katso [Koordinaatisto](fundamentals/co-ordinate-system.md "mention")
* **rotation** - viivan kulma asteina
* **resolution** - katso [Resoluutio](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ määrittää viivan aloituspisteen ja kierron keskipisteen
* _MOVE TO FRONT / MOVE TO BACK_ - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Tekee ympyrän / kartion.

* **Render profile** - katso [Render Profile](fundamentals/render-profile.md "mention")
* **radius** - ympyrän säde
* **Colour** - ympyrän väri. Katso [Väriasetukset ja HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- ja **y**-sijainti - katso [Koordinaatisto](fundamentals/co-ordinate-system.md "mention")
* **resolution** - katso [Resoluutio](fundamentals/resolution.md "mention")
* **Fill state** - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Tekee säännöllisen monikulmion, kuten kolmion, neliön tai viisikulmion.

* **Render profile** - katso [Render Profile](fundamentals/render-profile.md "mention")
* **size** - etäisyys keskeltä kuhunkin kulmaan
* **Colour** - monikulmion väri. Katso [Väriasetukset ja HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- ja **y**-sijainti - katso [Koordinaatisto](fundamentals/co-ordinate-system.md "mention")
* **rotation** - muodon kiertokulma asteina
* **resolution** - katso [Resoluutio](fundamentals/resolution.md "mention")
* **Fill state** - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Lataa SVG-tiedoston omia muotoja varten.

{% hint style="warning" %}
Liberation on yhteensopiva _SVGTiny_-muodon kanssa. InkScapea suositellaan, mutta useimmat vektorigrafiikkasovellukset osaavat viedä tähän muotoon. Muunna kaikki teksti muodoiksi ennen vientiä. Liberation renderöi viivat ja voi haluttaessa käyttää täyttöjä maskeina. Varmista, etteivät viivat ole mustia, muuten ne eivät näy ilman värimuokkainta!
{% endhint %}

* **Import SVG** - lataa SVG-tiedosto levyltä.

{% hint style="info" %}
Kun SVG on ladattu, sisältö muunnetaan ja tallennetaan clipin sisään. Siksi tiedostoviittausta ei tarvitse säilyttää, ellet myöhemmin halua muuttaa maskiasetuksia.
{% endhint %}

* **Use fills as masks** - käsittelee kaikki täytetyt muodot maskeina, eli mustalla täytettyinä. Tämä asetetaan automaattisesti, jos SVG:ssä on täytettyjä muotoja. Jos täytettyjä muotoja ei ole, asetus poistetaan käytöstä. Katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - jos SVG:n muodoissa ei ole ääriviivaa, niitä ei voida piirtää! Tämä asetus lisää ääriviivan (eli _stroke_) kaikkiin täytettyihin muotoihin. Jos SVG:ssä ei ole lainkaan viivallisia muotoja, asetus otetaan käyttöön automaattisesti. Jos siinä ei ole täytettyjä muotoja, asetus poistetaan käytöstä.
* **Invert black lines** - jos kaikki SVG:n viivat ovat mustia, niitä ei näy! Tämä asetus muuttaa ne valkoisiksi. Asetus otetaan käyttöön automaattisesti, jos SVG:ssä on vain mustia muotoja, mutta se poistetaan käytöstä, jos mustia muotoja ei ole.
* **Render profile** - katso [Render Profile](fundamentals/render-profile.md "mention")
* **scale** - säätää SVG:n kokoa. Tämä lasketaan automaattisesti, kun SVG ladataan (jotta kuva varmasti näkyy), mutta arvoa voi myöhemmin muokata käsin.
* **x**- ja **y**-sijainti - katso [Koordinaatisto](fundamentals/co-ordinate-system.md "mention")
* **rotation** - kuvan kiertokulma asteina
* **resolution** - katso [Resoluutio](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Luo animaation SVG-tiedostojen sarjasta.

* **Import SVG Sequence** - valitse kansio, jossa kaikki SVG-tiedostot ovat. Huomaa, että tiedostot ladataan aakkosnumeerisessa järjestyksessä.

{% hint style="info" %}
Kun SVG-sarja on ladattu, sisältö muunnetaan ja tallennetaan clipin sisään. Siksi tiedostoviittauksia ei tarvitse säilyttää, ellet myöhemmin halua muuttaa maskiasetuksia.
{% endhint %}

* **Use fills as masks** - käsittelee kaikki täytetyt muodot maskeina, eli mustalla täytettyinä. Tämä asetetaan automaattisesti, jos jossakin SVG:ssä on täytettyjä muotoja. Jos missään ei ole täytettyjä muotoja, asetus poistetaan käytöstä. Katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - jos SVG:iden muodoissa ei ole ääriviivoja, niitä ei voida piirtää! Tämä asetus lisää ääriviivan (eli _stroke_) kaikkiin täytettyihin muotoihin. Jos SVG:issä ei ole lainkaan viivallisia muotoja, asetus otetaan käyttöön automaattisesti. Jos yhdessäkään ei ole täytettyjä muotoja, asetus poistetaan käytöstä.
* **Invert black lines** - jos kaikki SVG:iden viivat ovat mustia, niitä ei näy! Tämä asetus muuttaa ne valkoisiksi. Asetus otetaan käyttöön automaattisesti, jos SVG:issä on vain mustia muotoja, mutta se poistetaan käytöstä, jos mustia muotoja ei ole.
* **Render profile** - katso [Render Profile](fundamentals/render-profile.md "mention")
* **scale** - säätää kuvan kokoa.
* **x**- ja **y**-sijainti - katso [Koordinaatisto](fundamentals/co-ordinate-system.md "mention")
* **rotation** - kuvan kiertokulma asteina
* **resolution** - katso [Resoluutio](fundamentals/resolution.md "mention")
* **speed** - koko animaation kesto tahteina.
* **time per frame** - jos tämä on käytössä, kesto koskee jokaista ruutua eikä koko animaation pituutta. Jos _speed_-arvoksi on asetettu ¼, jokainen ruutu kestää 1 iskun.
* **animation direction** -
  * _FORWARDS_ - animaatio etenee eteenpäin ja palaa sitten silmukassa alkuun
  * _BACKWARDS_ - animaatio etenee taaksepäin ja palaa sitten silmukassa loppuun
  * _PINGPONG_ - animaatio etenee eteenpäin ja sitten taaksepäin silmukassa
  * _MANUAL_ - nykyinen ruutu asetetaan _position manual_ -asetuksella
* **position manual** - aseta nykyinen ruutu: 0 % on ensimmäinen ruutu ja 100 % viimeinen ruutu. Tämän voi asettaa käsin tai ulkoisella oskillaattorilla.
* _MOVE TO FRONT / MOVE TO BACK_ - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Luo tekstiä TrueType- tai OpenType-fontilla.

* **Text** - kirjoita haluamasi teksti tähän
* **Font** - valitse haluamasi fontti

{% hint style="info" %}
Voit lisätä Liberationiin fontteja kopioimalla .ttf- tai .otf-tiedostot Liberation-työkansion sisällä olevaan `data/fonts`-kansioon ja käynnistämällä sitten Liberationin uudelleen.
{% endhint %}

* **Render profile** - katso [Render Profile](fundamentals/render-profile.md "mention")
* **horizontal alignment** - valitse tekstin tasaus: _LEFT_, _CENTRE_ tai _RIGHT_.
* **Fill state** - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - tekstin koko
* **monospace** - piirtää jokaisen merkin samalla leveydellä. Tämä on hyödyllistä ajastimissa ja laskureissa, koska teksti ei hypi sivusuunnassa numeroiden muuttuessa.
* **character spacing** - säätää merkkien välistä etäisyyttä. Suurenna arvoa, jos haluat väljemmän merkkivälistyksen, tai pienennä sitä tiivistääksesi tekstiä.
* **colour -** katso [Väriasetukset ja HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- ja **y**-sijainti - katso [Koordinaatisto](fundamentals/co-ordinate-system.md "mention")
* **rotation** - kuvan kiertokulma asteina
* **resolution** - katso [Resoluutio](fundamentals/resolution.md "mention")
* **reveal** - käytä tätä tekstin asteittaiseen paljastamiseen merkki kerrallaan. Kun arvo on välillä 0–50 %, teksti ilmestyy vähitellen vasemmalta oikealle. Kun arvo on välillä 50–100 %, teksti katoaa vasemmalta oikealle. Voit liittää tähän liitäntään oskillaattorin animaatioita varten.
* **reveal by word** - kun tämä on käytössä, _reveal_ toimii sana kerrallaan eikä merkki kerrallaan.
* **countdown** - korvaa kirjoitetun tekstin lähtölaskennalla. Kun lähtölaskenta saavuttaa nollan, normaali **Text**-arvo näytetään.
* **use seconds** - laskee todellisissa sekunneissa. Kun tämä ei ole käytössä, lähtölaskenta perustuu iskuihin: kaksi iskua vastaa yhtä sekuntia, joten 120 bpm vastaa todellisia sekunteja.
* **show minutes/seconds** - näyttää jäljellä olevan ajan minuutteina ja sekunteina. Jos aikaa on yli tunti, mukana näytetään myös tunnit.
* **countdown to date/time** - laskee aikaa tiettyyn UTC-päivämäärään ja -kellonaikaan sen sijaan, että laskenta alkaisi numerosta.
* **countdown datetime** - asettaa UTC-kohdepäivämäärän ja -kellonajan, kun **countdown to date/time** on käytössä.
* **start number** - aloitusnumero, kun **countdown to date/time** ei ole käytössä.
* _MOVE TO FRONT / MOVE TO BACK_ - katso [Täytöt, maskit ja syvyyslajittelu](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Jos fonttien avattava valikko on auki, ylä- ja alanuolinäppäimillä voi selata käytettävissä olevia fontteja.
{% endhint %}
