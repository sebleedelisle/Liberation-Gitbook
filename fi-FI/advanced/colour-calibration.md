---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Värikalibrointi

Värikalibrointi varmistaa, että projektorin punainen, vihreä ja sininen laser tuottavat valoa tasaisesti ja ennustettavasti kaikilla kirkkaustasoilla. Eri projektoreissa voi olla epälineaarisia kirkkauskäyriä, jolloin esimerkiksi 50 % punainen voi näyttää paljon kirkkaammalta tai himmeämmältä kuin puolet 100 % punaisen voimakkuudesta. Kalibrointi korjaa tämän, jotta värit sekoittuvat siististi, liukuvärit näyttävät tasaisilta ja valkoinen on tasapainossa.

#### Projektorin lämmittäminen

Laserdiodien toiminta muuttuu niiden lämmetessä. Anna projektorin aina vakautua ennen kalibrointia:

* Heijasta kirkas kuvio, kuten **White rectangle test pattern (11)**, vähintään **15–20 minuutin** ajan.
* Näin varmistat, että asettamasi väritasapaino pysyy yhtenäisenä esityksen aikana.

#### Kalibrointitestin toiminta

Käytä kalibrointiin testikuvioita (katso [test-patterns.md](../output-view/test-patterns.md))

* **5** – Punainen
* **6** – Vihreä
* **7** – Sininen
* **8** – Valkoinen

Jokainen näistä näyttää neljä liikkuvaa viivaa:

* **Ylin viiva** – 100 % kirkkaus täydellä nopeudella
* **Toinen viiva** – 75 % kirkkaus 75 % nopeudella
* **Kolmas viiva** – 50 % kirkkaus 50 % nopeudella
* **Neljäs viiva** – 25 % kirkkaus 25 % nopeudella

Koska sekä kirkkautta _että nopeutta_ skaalataan yhdessä, kaikkien viivojen pitäisi näyttää yhtä kirkkailta. Jos jokin viiva näyttää vaaleammalta tai tummemmalta, säädä vastaavaa liukusäädintä, kunnes viivat vastaavat toisiaan.

Jokaisessa testikuviossa on myös viides viiva **0 % kirkkaudella**, eikä sen pitäisi näkyä. Tätä käytetään korjaamaan lasereita, jotka eivät tuota lainkaan valoa hyvin matalilla tasoilla. Jos laser pysyy näkymättömänä matalalla kirkkaudella, nosta **0% setting** -arvoa vähitellen, kunnes viiva juuri tulee näkyviin, ja pienennä sitä sitten hieman, kunnes viiva katoaa uudelleen. Tavoitteena on löytää kynnys, jossa laser alkaa syttyä, ja pysyä juuri sen alapuolella – näin häivytykset alkavat luonnollisesti ilman, että alin säätöalue leikkautuu pois.

#### Colour Calibration -paneelin käyttö

Paneelissa on erilliset säätimet kullekin kanavalle (punainen, vihreä, sininen) tasoilla 100, 75, 50, 25 ja 0 %.

1. **Valitse testikuvio** (aloita punaisesta).
2. **Säädä liukusäätimiä** niin, että 100, 75, 50 ja 25 % viivat näyttävät yhtä kirkkailta.
3. **Hienosäädä 0 % -liukusäädintä**, jos “off”-viiva näkyy edelleen heikosti.
4. **Toista vihreälle ja siniselle.**
5. Vaihda **White test pattern (8)** -testikuvioon. Kaikkien neljän viivan pitäisi näyttää yhtä kirkkailta, ja valkoisen pitäisi olla neutraali (ei sävyttynyt).

#### Valkotasapainon säätäminen

Voit käyttää samaa järjestelmää myös **valkotasapainon** säätämiseen. Kun olet kalibroinut jokaisen kanavan erikseen, vaihda **White test pattern (8)** -testikuvioon. Jos lähtö näyttää sävyttyneeltä (esimerkiksi liian vihreältä tai liian siniseltä), säädä punaisen, vihreän ja sinisen kanavan suhteellisia tasoja, kunnes viivat näyttävät neutraalin valkoisilta. Vaikka laserien tehot poikkeaisivat toisistaan paljon, kalibrointi auttaa silti tuomaan ne lähemmäs toisiaan ja tuottamaan puhtaamman, tasapainoisemman värisekoituksen.

#### Kalibroinnin tallentaminen

* Korvaa nykyinen esiasetus valitsemalla **Store**.
* Luo uusi esiasetus valitsemalla **Store As** (hyödyllistä, jos käytät useita lasereita).
