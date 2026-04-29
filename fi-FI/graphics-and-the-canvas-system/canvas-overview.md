---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas-yleiskatsaus

Liberationin Canvas-järjestelmä on melko yksinkertainen, mutta se voi aluksi tuntua hämmentävältä. Tässä on käsitteellinen yleiskatsaus, jolla pääset alkuun.

{% hint style="info" %}
**Hetkinen, tarvitsenko Canvas-järjestelmää?**

Et välttämättä! Jos projisoit vain yhden grafiikan yhdelle laserille, voit tehdä sen helposti beam zone -alueella. Oletuksena beam zone -sisältö kuitenkin peilataan vaakasuunnassa, joten Clipille täytyy tehdä X flip.

Jos taas haluat jakaa graafista sisältöä useammalle laserille tai pilkkoa sen eri osiin esimerkiksi arkkitehtuurimappausta varten, Canvas-järjestelmä hoitaa sen.
{% endhint %}

### Canvas

Ensimmäisenä on itse Canvas. Se näkyy _CANVAS_-näkymässä ja edustaa suurta, no, canvasta, jonka alueelle voit piirtää sisältöä mihin tahansa.

### Canvas-kohdealueet

Nämä näkyvät Canvas-näkymässä sinisinä ääriviivasuorakulmioina. Ne ovat alueita, joille voit lähettää sisältöä. Lähetät Clipin sisällön Canvas-kohdealueelle samalla tavalla kuin lähettäisit Clipin beam zone -alueelle. Canvas-kohdealueiden painikkeet näkyvät Clip Deckissä beam zone -painikkeiden oikealla puolella.

{% hint style="info" %}
Jos et näe Canvas-painikkeita Clip Deckissä, kokeile vierittää beam zone -painikkeita näppäinyhdistelmällä `Shift + Left / Right Arrow`. Jokaiselle Canvas-kohdealueelle pitäisi näkyä painike, jonka nimi on _CANVAS 1, CANVAS 2_ jne.
{% endhint %}

### Canvas-alueet

Canvas-alueet ovat Canvasin sisällä olevia alueita, jotka valitset lähetettäviksi laserille. Ne esitetään Canvas-näkymässä vaaleanpunaisina ääriviivasuorakulmioina. Voit napsauttaa kutakin aluetta hiiren oikealla painikkeella ja valita laserit, joille haluat määrittää sen. Jos vaihdat nyt kyseisen laserin _OUTPUT_-näkymään, näet, että uusi alue on ilmestynyt.

{% hint style="danger" %}
VAROITUS – jos laser on armed-tilassa, saatat yhtäkkiä alkaa projisoida sisältöä oletusarvoiselle Canvas-alueelle. Laser kannattaa poistaa armed-tilasta ennen Canvas-alueiden määrittämistä sille.
{% endhint %}

{% hint style="info" %}
Voit myös määrittää Canvas-alueen laserille napsauttamalla _add canvas zone_ -painiketta _OUTPUT_-näkymässä. Katso [Vyöhykkeet](../output-view/zones.md).
{% endhint %}

### Opaskuvat

Voit lisätä Canvasille opaskuvan ja käyttää sitä grafiikan mallipohjana. Opaskuvan värisävyä kannattaa säätää (hiiren oikean painikkeen valikosta) ja tummentaa kuvaa, jotta näet oman sisältösi sen päällä helpommin.

{% hint style="info" %}
Arkkitehtuurimappauksessa olen kokenut hyödylliseksi tehdä rakennuksesta ”auki levitetyn” visualisoinnin, jossa kaikki rakennuksen pinnat esitetään litteänä ja vääristymättömänä kuvana. Eri osien perspektiivikorjauksen voi tehdä Canvas-alueella _OUTPUT_-näkymässä.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>”Litteäksi” tehty opaskuva Saltwell Hallista Gatesheadissa, Isossa-Britanniassa</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Canvas-alueet Liberationin hyvin varhaisessa versiossa (noin 2017!) Huomaa, että vaaleanpunaiset suorakulmiot valitsevat, mikä osa Canvasista näytetään, ja niiden alla olevat Output-näkymät näyttävät, mihin kohtaan kunkin laserin kuvaa nämä alueet kohdistuvat.</p></figcaption></figure>

### Canvas 3D Visualiserissa

Monimutkaisen monilaserisen projisointijärjestelmän uudelleenluonti 3D Visualiserissa olisi todennäköisesti vähintäänkin hankalaa. Sen sijaan voit sijoittaa Canvasin 3D-tilaan. Ota _3D visualiser settings_ -paneelissa käyttöön _Show canvas_ -valintaruutu. (Myös Canvasilla olevat opaskuvat näkyvät visualiserissa.)

{% hint style="info" %}
Huomaa, että visualiser näyttää Canvas-projisoinnit edelleen lasereista tulevina ilmakehäefekteinä. Voit joko siirtää ne pois näkymästä tai, jos haluat hienosäätää, kohdistaa ne Canvasin kanssa.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>On erittäin palkitsevaa, kun saat laserin säteet kohdistettua Canvas-kuvan kanssa 3D Visualiserissa!</p></figcaption></figure>
