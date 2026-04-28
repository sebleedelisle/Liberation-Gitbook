---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Sijaintiin perustuvat muuttajat

Tämä solmuryhmä muokkaa sisältöä sijainnin mukaan. Oletuksena efekti kohdistuu vaakasuuntaiselle akselille (vasemmalta oikealle), mutta voit kiertää akselin mihin tahansa kulmaan. Jokaisessa solmussa on myös _radial_-tila, jossa efekti määräytyy kunkin pisteen kulman mukaan suhteessa keskikohtaan.

* **Colour Changer by Position** – siirtää värejä valitulla akselilla tai radial-kulman ympäri.\
  \&#xNAN;_Esimerkki: Luo viivan yli pyyhkäisevä sateenkaarigradientti tai käytä radial-tilaa ympyrässä väripyöräefektin luomiseen._
* **Wave Shift by Position** – käyttää siniaaltoon perustuvaa vääristymää ja siirtää sisältöä pystysuunnassa (tai kohtisuoraan valittuun akseliin nähden).\
  \&#xNAN;_Esimerkki: Tee viivasta veden lailla väreilevä tai käytä radial-tilaa, jotta ympyrä sykkii ulospäin keskikohdasta._
* **Noise Shift by Position** – käyttää simplex-kohinaan perustuvaa vääristymää ja siirtää sisältöä pystysuunnassa (tai kohtisuoraan valittuun akseliin nähden).\
  \&#xNAN;_Esimerkki: katso Wave Shift -esimerkki, mutta lopputulos on orgaanisempi ja satunnaisempi. Sopii hyvin luonnollisen vaihtelun lisäämiseen._

## &#x20;Värin muutos sijainnin mukaan

Tämä solmu muuttaa sisällön värejä sijainnin perusteella. Oletuksena akseli on vaakasuuntainen (0°), mutta voit kiertää sitä tai vaihtaa radial-tilaan.

* **wavelength** – määrittää toistuvan värisyklin koon.
  * _Linear mode:_ arvolla 100% yksi täysi sykli kattaa sisällön koko leveyden.
  * _Radial mode:_ arvolla 100% yksi täysi sykli kattaa koko ympyrän (360°). Arvot ovat prosentteja ympyrästä: esim. 50% = puoli ympyrää (180°).
* **offset** – siirtää värisyklin aloituskohtaa prosenttiosuutena wavelength-arvosta. Voit moduloida tätä (esim. sawtooth-oskillaattorilla), jotta värit vaihtuvat sulavasti.
* **repeat** – kun käytössä, sykli toistuu sisällön yli. Jos se on pois käytöstä, gradientti käytetään vain kerran: kaikki ennen alkua on aloitusväriä ja kaikki lopun jälkeen on lopetusväriä.
* **pingpong** – kun käytössä, jokainen toisto vaihtaa suuntaa ja luo peilatun efektin. Jos _Repeat_ on pois käytöstä, gradientti kulkee kerran eteenpäin ja sitten takaisin. _Huomautus: Pingpong-tilassa wavelength kattaa sekä eteenpäin kulkevan että palaavan pyyhkäisyn._
* **linear angle** – kiertää efektin akselia. 0° = vaakasuuntainen.
* **radial** – vaihtaa radial-tilaan, jossa värit määräytyvät keskikohdasta mitatun kulman mukaan.
* **radial smooth loop** – säätää wavelength-arvon automaattisesti niin, että se jakautuu tasan 100%:iin ympyrästä. Tämä estää näkyvän sauman kohdassa, jossa sykli kiertyy ympäri.

**Colour Modes**

Nämä määrittävät, mitkä värisäätöjen osa-alueet käytetään sisältöön. Katso myös: [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md).

* **hue mode**
  * _OFF_ – hue ei muutu.
  * _FIXED_ – hue pakotetaan kiinteään arvoon.
  * _SHIFTED_ – hue siirtyy määritetyllä määrällä (eri väriset elementit pysyvät erillisinä, mutta siirtyvät yhdessä väripyörällä).
* **saturation mode**
  * _OFF_ – saturation ei muutu.
  * _FIXED_ – saturation asetetaan määritettyyn arvoon.
* **brightness mode**
  * _OFF_ – brightness ei muutu.
  * _FIXED_ – brightness asetetaan määritettyyn arvoon.
  * _MULTIPLY_ – brightness skaalataan määritetyllä arvolla. Tämä säilyttää dynamiikan (esim. vilkkuvat elementit vilkkuvat edelleen, mutta rajatulla kirkkausalueella).

**Start / End Values**

Nämä liukusäätimet määrittävät valitulle akselille (tai radial-pyyhkäisylle) käytettävän värialueen.

* **start hue** – hue gradientin alussa.
* **end hue** – hue gradientin lopussa.
* **start saturation** – saturation alussa.
* **end saturation** – saturation lopussa.
* **start brightness** – brightness alussa.
* **end brightness** – brightness lopussa.
* **blend** – sekoittaa värimuutoksen alkuperäisiin väreihin. Arvolla 100% efekti korvaa alkuperäiset värit kokonaan.

**Esimerkki 1: Liukuva sateenkaarigradientti**

Aloita oletusasetuksista:

1. Jätä solmu **Linear**-tilaan (0° kulma = vaakasuuntainen).
2. Jätä **wavelength** arvoon 100% (kattaa koko leveyden ja pitäisi olla oletus).
3. Jätä alku- ja loppuarvot oletuksiin.
4. Ota **repeat** käyttöön.
5. Lisää **Sawtooth Oscillator** **offset**-asetukseen niin, että se kulkee arvosta 0% arvoon 100%.

***

**Esimerkki 2: Musta–valkoinen–musta-gradientti (Pingpong)**

Aloita oletusasetuksista:

1. Jätä solmu **Linear**-tilaan (0° kulma = vaakasuuntainen).
2. Jätä **wavelength** arvoon 100% (kattaa koko leveyden ja pitäisi olla oletus).
3. Kytke **repeat** pois käytöstä.
4. Aseta **start brightness** arvoon 0 (musta).
5. Aseta **end brightness** arvoon 100 (valkoinen).
6. Aseta **start saturation** ja **end saturation** arvoon 0 (muuntaa harmaasävyksi).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Ota **pingpong** käyttöön.

_Lopputulos: gradientti häivyttää leveydellä mustasta valkoiseen ja takaisin mustaan._\
Huomaa, että jos haluat sisällön säilyttävän hue- ja saturation-arvonsa, kytke Saturation mode pois päältä. \\

***

**Esimerkki 3: Pyörivä sateenkaaripyörä (Radial)**

1. Ota **radial**-tila käyttöön.
2. Aseta **wavelength** arvoon 100% (täysi 360° pyyhkäisy).
3. Kytke **repeat** päälle.
4. Lisää **Sawtooth Oscillator** **offset**-asetukseen niin, että se kulkee arvosta 0% arvoon 100%.

_Lopputulos: saumaton väripyörä, joka pyörii jatkuvasti ympyrän ympäri._

## &#x20;Aaltosiirto sijainnin mukaan

Tämä solmu käyttää sisältöön aaltovääristymää ja siirtää pisteitä kohtisuoraan valittuun akseliin nähden (tai säteittäisesti keskikohdasta).

* **Wavelength** – määrittää aaltosyklin pituuden.
  * _Linear mode:_ arvolla 100% yksi täysi sykli kattaa sisällön koko leveyden.
  * _Radial mode:_ arvolla 100% yksi täysi sykli kattaa koko 360°. (Arvot ovat prosentteja ympyrästä: 50% = puoli kierrosta, 25% = neljänneskierros jne.)
* **Size** – säätää aallon amplitudia (kuinka kauas sisältö siirtyy).
* **Offset** – siirtää aaltoa akselin suuntaisesti (tai ympyrän ympäri radial-tilassa). Tämä on prosenttiosuus wavelength-arvosta, joten voit animoida sen **Oscillator Node** -solmulla ja saada aallon liikkumaan.
* **Radial** – vaihtaa linear-tilasta radial-tilaan, jolloin siirtymä perustuu keskikohdasta mitattuun kulmaan.
* **Radial Smooth Loop** – säätää wavelength-arvon niin, että se jakautuu tasan 100%:iin ympyrästä. Tämä estää näkyvät saumat kiertymäkohdassa.
* **Triangle** – muuttaa aaltomuodon sinistä kolmioksi.
* **Absolute** – ottaa aallon itseisarvon ja luo vain ylöspäin suuntautuvia siirtymiä (taittaa negatiivisen puolen positiivisen päälle).
* **Angle** – kiertää aallon akselia. 0° = vaakasuuntainen.

## &#x20;Kohinasiirto sijainnin mukaan

Tämä solmu vääristää sisältöä kohinakentän avulla (turbulenssin tapaan) ja siirtää pisteitä kohtisuoraan valittuun akseliin nähden (tai säteittäisesti keskikohdasta). Verrattuna _Wave Shift_ -solmuun lopputulos on orgaanisempi ja satunnaisempi.

* **Detail** – säätää kohinan hienojakoisuutta. Suuremmat arvot = terävämpää ja yksityiskohtaisempaa vaihtelua. Pienemmät arvot = pehmeämpää vaihtelua.
* **Wavelength** – määrittää kohinakuvion mittakaavan.
  * _Linear mode:_ arvolla 100% yksi täysi kohinasykli kattaa sisällön leveyden.
  * _Radial mode:_ arvolla 100% yksi täysi sykli kattaa koko 360°.
* **Size** – säätää siirtymän määrää (kohinavääristymän amplitudia).
* **Offset** – siirtää kohinakuviota akselin suuntaisesti (tai ympyrän ympäri). Tämä on prosenttiosuus wavelength-arvosta, joten voit animoida sen **Oscillator Node** -solmulla ja saada kohinan “virtaamaan.”
* **Depth Offset** – liikkuu 3D-kohinakentän läpi ja luo vaihtelua ajan myötä. Tämä toimii erityisen hyvin, kun se animoidaan Oscillator Node -solmulla.
* **Depth Detail** – säätää, kuinka yksityiskohtaista vaihtelu on syvyysulottuvuudessa.
* **Absolute** – ottaa kohinan itseisarvon ja taittaa negatiiviset arvot positiivisiksi (tuottaa vain yksipuolisen siirtymän).
* **Radial** – vaihtaa linear-tilasta radial-tilaan, jolloin siirtymä perustuu keskikohdasta mitattuun kulmaan.
* **Radial Smooth Loop** – säätää wavelength-arvon niin, että se jakautuu tasan 100%:iin ympyrästä. Tämä estää näkyvät saumat radial-tilassa.
