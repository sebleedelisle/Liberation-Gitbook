---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stylisation-nodit

## &#x20;Randomise

Luo sisääntulevista elementeistä hajautettuja kopioita koherentin kohinakentän avulla. Toisin sanoen se kopioi ja siirtää muotoja ja pisteitä hallitulla, “kohinaisella” tavalla. Sen sijaan, että kaikki olisi siististi yhdessä paikassa, saat useita versioita, jotka liikkuvat ja leviävät kuin virtauksessa kulkevat partikkelit.

* **count** – kopioiden määrä jokaista sisääntulevaa elementtiä kohti (1–20). Arvolla 1 saat jokaisesta elementistä yhden hieman siirretyn version. Suuremmat arvot luovat useita hajautettuja kopioita.
* **noise offset** – kiertää kohinakentän läpi (0–100%). Se looppaantuu saumattomasti, joten tämän animointi Oscillator Node -nodilla tuottaa kaikkien kopioiden yhteisen, tasaisen ja jatkuvan liikkeen.
* **noise jitter** – säätää kohinan tekstuurin mittakaavaa. Pienemmät arvot tuottavat laajaa ja pehmeää vaihtelua. Suuremmat arvot tuottavat tiiviimpää ja arvaamattomampaa sijoittelua. Tämä muuttaa kuviota, ei vaikutuksen voimakkuutta.
* **change between points** – säätää, kuinka paljon kukin kopio poikkeaa edellisestä. Pienet arvot pitävät kopiot ryhmittyneinä ja samankaltaisina. Suuret arvot levittävät niitä laajemmalle ja lisäävät vaihtelua.
* **face direction** – kiertää jokaista kopiota niin, että se osoittaa kohinakentän liikesuuntaan. Tämä tuottaa nuolia/partikkeleita, jotka kohdistuvat virtauksen mukaan.
* **amount** – efektin kokonaisvoimakkuus (0–100%). Skaalaa sekä siirtymää että Face direction -asetuksesta tulevaa kiertoa.

{% hint style="info" %}
Randomise-nodi on Randomise-efektin ytimessä!
{% endhint %}

## &#x20;Trails

Luo sisällöstä kaikuja, eli jättää alkuperäisen liikkuessa sen perään himmeneviä tai skaalautuvia kopioita.

* **change render profile for trail** – jos käytössä, kaikki trail-kopiot käyttävät valittua **render profile** -asetusta. _Katso_ [render-profile.md](../fundamentals/render-profile.md).
* **render profile** – profiili, jota käytetään trail-kopioille, kun yllä oleva kytkin on käytössä. Tätä käytetään usein, kun pääsisältö on asetettu tilaan **DETAIL**, mutta kaiut renderöidään tilassa **FAST**. Näin päämuodoissa säilyy selkeä yksityiskohtaisuus ja trail-kopiot renderöityvät tehokkaammin.
* **delay** – asettaa trail-kopioiden välisen etäisyyden musiikillisessa ajassa, mitattuna **1/64-nuotin askelina**.\
  Vertailuksi:
  * 16 = 1/16 tahtia (kuudestoistaosanuotti)
  * 32 = 1/8 tahtia (kahdeksasosanuotti)
  * 64 = 1/4 tahtia (neljäsosanuotti)
  * 128 = 1/2 tahtia (puolinuotti)
  * 256 = 1 tahti
* **trail size** – kuinka monta trail-kopiota piirretään live-sisällön perään.
* **freeze trails** – muuttaa pehmeästi virtaavat trailit sarjaksi pysäytettyjä hetkikuvia. Hyödyllinen staccato-tyylisten, biittiin synkronoitujen trail-efektien luomiseen.
* **brightness start / brightness end** – asettaa kirkkauden trailin matkalle uusimmasta kopiosta (**start**) vanhimpaan kopioon (**end**). Yleensä **brightness start** asetetaan arvoon 100% ja **brightness end** arvoon 0%, jolloin kaiut häipyvät pois.
* **scale start / scale end** – asettaa skaalauksen trailin matkalle uusimmasta kopiosta (start) vanhimpaan kopioon (end). Jos haluat trailien kutistuvan pois, aseta **scale start** arvoon 100% ja **scale end** arvoon 0%.

## &#x20;Shimmer

Lisää sisältöön tuikkivaa kirkkauden vaihtelua, joka voi olla kevyttä kimallusta tai voimakasta strobemaisuutta.

* **speed** – kuinka nopeasti shimmer muuttuu ajan myötä. Suuremmat arvot välkkyvät nopeammin; 0 pysäyttää efektin.
* **separation** – kuinka paljon vierekkäiset pisteet/elementit poikkeavat toisistaan.
  * 0: kaikki shimmeröi yhdessä.
  * \>0: läheiset pisteet saavat asteittain eri vaiheita, joten shimmer vaihtelee muodon eri kohdissa.
  * <0: sama kuin yllä, mutta vaiheen etenemissuunta on päinvastainen.
* **threshold** – pehmeän häipymisen sijaan pisteet välähtävät nyt täysin päälle tai pois kirkkaudestaan riippuen. Kirkkaammat elementit syttyvät useammin, mutta huomaa, että 100% kirkkaudella olevat elementit ovat aina päällä ja 0% kirkkaudella olevat elementit aina pois päältä. Hyödyllinen teräviin glitter- tai tähtivaloefekteihin.

{% hint style="info" %}
**threshold**-asetuksen käyttöönotto on yksi niistä hienoista piilossa olevista ominaisuuksista, jotka voivat todella herättää partikkelit tai sisällön eloon. Häipymisen sijaan pisteet kytkeytyvät nopeasti päälle ja pois kirkkauden perusteella. Koska kerralla piirretään vähemmän pisteitä, lopputuloksena on kirkkaampi ulostulo ja sulavampi animaatio.

Muista kuitenkin, että jos sisältösi on jo 100% kirkkaudella, asetus ei tee mitään!
{% endhint %}

* **use whole shape** – käyttää yhtä shimmer-arvoa tasaisesti koko muodolle. Kun asetus ei ole käytössä, nodi jakaa muodot osiin, jolloin eri osat voivat tuikkia itsenäisesti ja lopputuloksesta tulee rakeisempi.

## &#x20;Particles

Tämä on kokeellinen efekti, joka luo ja animoi partikkeleita sisältösi perusteella. Kaikki sisääntulevat pistepohjaiset elementit käsitellään emitterien sijainteina. Koska partikkelien polut lasketaan etukäteen, syötesisällön muuttuessa partikkelit täytyy ehkä päivittää tai laskea uudelleen (muuta mitä tahansa asetusta).

**General**

* **keep original** – jos käytössä, alkuperäinen sisältö säilytetään ja partikkelit lisätään sen päälle. Hyödyllinen, kun haluat emitteripisteiden pysyvän näkyvissä.
* **number of particles** – kuinka monta partikkelia luodaan per emissio. Suuremmat arvot tekevät efektistä tiheämmän, pienemmät arvot minimalistisemman.
* **emission period** – loopin jakso (tahteina), jonka aikana partikkelit emittoidaan. Arvolla 100% ne jakautuvat tasaisesti koko loopille; pienemmät arvot kasaavat ne yhteen purskahduksiksi.
* **loop length** – kuinka pitkään partikkelilooppi kestää, mitattuna musiikillisina tahteina.
* **loop count** – kuinka monta kertaa looppi toistuu ennen nollausta. Jos arvoksi asetetaan 1, partikkelit seuraavat aina täsmälleen samaa simulaatiota joka kerta, joten lopputulos on täysin toistettava. Suuremmat arvot tuovat lisää vaihtelua ennen syklin nollausta.
* **delay** – siirtää emission aloitusaikaa tietyn määrän 1/64-nuotteja ajoitusefektejä varten.

**Motion**

* **speed** – kuinka nopeasti partikkelit liikkuvat pois emitteristä.
* **speed variation** – lisää satunnaisuutta, jotta kaikki partikkelit eivät liiku samalla nopeudella. Luo luonnollisemman leviämisen.
* **direction** – asettaa perussuunnan, johon partikkelit laukaistaan, määritettynä **x, y, z angles** -arvoilla. Nämä kulmat kiertävät laukaisuvektoria 3D-tilassa, joten voit suunnata partikkelit suoraan ylös, sivulle tai mihin tahansa viistosuuntaan. Yhdistä **spread**-asetukseen leveämpiä kartioita tai kaoottisempia purskahduksia varten.

{% hint style="info" %}
**Euler angles**\
Liberation käyttää **Euler angles** -kulmia suunnan kuvaamiseen 3D-tilassa. Ne ovat yksinkertaisesti kiertoja kolmen pääakselin ympäri:

* **X** – kallistus eteen/taakse (kuin nyökkäisit)
* **Y** – käännös vasemmalle/oikealle (kuin pudistaisit päätä “ei”)
* **Z** – rullaus myötäpäivään/vastapäivään (kuin kallistaisit päätä sivulle)

Säätämällä näitä kolmea arvoa voit suunnata partikkelit mihin tahansa suuntaan.
{% endhint %}

* **direction variation** – lisää satunnaista hajontaa kyseisen suunnan ympärille. Hyödyllinen kartioiden, suihkujen tai räjähdysten luomiseen.
* **drag** – hidastaa partikkeleita ajan myötä. Suuremmat arvot saavat ne tuntumaan raskaammilta ja verkkaisemmilta.
* **gravity** – vetää partikkeleita alas (positiivinen) tai työntää niitä ylös (negatiivinen).
* **gravity variation** – lisää partikkelikohtaista vaihtelua painovoimaan, mikä tekee liikkeestä kaoottisempaa.

**Life**

* **life duration** – kuinka kauan partikkelit ovat olemassa (mitattuna 1/64-nuotin yksiköissä). Lyhyemmillä arvoilla partikkelit katoavat nopeasti, kun taas pidemmillä arvoilla ne pysyvät näkyvissä pidempään.
* **life variation** – lisää satunnaisuutta partikkelien elinaikaan, jotta ne eivät katoa kaikki kerralla.
* **start delay / start delay variation** – viivästää hetkeä, jolloin kukin partikkeli tulee näkyviin (1/64-nuotin askelina). Partikkeli on jo luotu ja liikkuu tämän jakson aikana, mutta sen kirkkaus pidetään arvossa 0, joten se pysyy näkymättömänä viiveen päättymiseen asti. Tämä on hyödyllistä, jos haluat viivästettyjen ilotulitusmaisten "kipinöiden" ilmestyvän.

**Colour & brightness**

* **hue start** – partikkelien alkuväri.
* **hue variation** – lisää satunnaisuutta, jotta kaikki partikkelit eivät aloita samalla värillä.
* **hue change** – siirtää sävyä partikkelin eliniän aikana ja luo väriä vaihtavia trail-efektejä.
* **brightness start / brightness end** – asettaa kirkkauden partikkelin eliniän matkalle. Yleensä brightness start asetetaan korkeaksi ja brightness end matalaksi, jotta partikkelit häipyvät luonnollisesti.
* **brightness variation** – satunnaistaa alkukirkkautta dynaamisemman ilmeen luomiseksi.
* **saturation start / saturation end** – asettaa, kuinka voimakas väri on alussa ja lopussa.
* **saturation variation** – satunnaistaa saturaatiota, jotta partikkelien välille syntyy vaihtelua.

**Simulation**

* **time adjustment** – nopeuttaa tai hidastaa koko partikkelisimulaatiota. Hyödyllinen eri tempoihin synkronointiin tai liikkeen korostamiseen.
