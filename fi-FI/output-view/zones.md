---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Vyöhykkeet

Useimmissa projekteissa käytät pääasiassa _Beam zone_ -vyöhykkeitä. Tämä vyöhyke on tarkoitettu ilmassa näkyville säde-efekteille. Toinen vyöhyketyyppi on _Canvas zone_ (katso [Grafiikka ja Canvas-järjestelmä](../graphics-and-the-canvas-system/)).

{% hint style="danger" %}
**VAROITUS - Ole erittäin varovainen, kun siirrät vyöhykkeitä laserin ollessa käynnissä**, ja laske kirkkaus mahdollisimman alas. Katso kattava opas laserien turvalliseen aktivointiin ja vyöhykkeiden määrittämiseen kohdasta [Lasereiden käyttöönoton prosessin yleiskatsaus](../setting-up/setting-up-lasers.md)
{% endhint %}

Voit siirtää vyöhykkeitä napsauttamalla ja vetämällä niitä hiirellä. Ota testikuvio käyttöön, jotta näet, mihin vyöhyke osuu.

{% hint style="info" %}
Käytä nuolinäppäimiä valittuna olevan vyöhykkeen/pisteen hienosäätöön. Paina `Shift`-näppäintä, jos haluat siirtää suuremmissa askelissa.
{% endhint %}

{% hint style="info" %}
Vinkki: voit kopioida vyöhykeasetuksia nopeasti useille lasereille! Katso [Kopioi asetukset lasereiden välillä](../setting-up/copy-laser-settings.md)
{% endhint %}

### Uuden beam zone -vyöhykkeen lisääminen

Napsauta työkalupalkin yläosassa olevaa _Add a new beam zone_ -painiketta, jolloin uusi vyöhyke tulee näkyviin. Huomaa, että beam zone -vyöhykkeet lajitellaan lisäysjärjestyksen mukaan, mutta voit muuttaa niiden järjestystä. Katso [Sädealueiden järjestyksen muuttaminen](re-ordering-beam-zones.md)

### Olemassa olevan canvas zone -vyöhykkeen lisääminen

Napsauta _Add existing canvas zone_ -painiketta. Näet luettelon käytettävissä olevista canvas zone -vyöhykkeistä, ja voit ottaa niitä käyttöön tai poistaa käytöstä tälle laserille. Katso [Grafiikka ja Canvas-järjestelmä](../graphics-and-the-canvas-system/)

### Vyöhykkeen muototyypit

Vyöhykkeillä on 3 muototyyppiä:

* **Quad** - oletusarvoinen suorakulmainen vyöhykemuoto, joka voi olla tasasuuntainen (akselien suuntainen) tai vääristetty. Paras suuremmille suorakulmaisille vyöhykkeille tai Canvas-vyöhykkeille, jotka vaativat perspektiivikorjausta.
* **Line/Curve** - vyöhyke, joka määritetään vähintään 2 pisteellä ja paksuudella. Sopii erinomaisesti kapeille vyöhykkeille tai rajaukseen parvekkeisiin, siltoihin tai muihin kaareviin muotoihin.
* **Segmented** - vyöhyke, joka voidaan jakaa pienempiin nelikulmioihin. Sopii erinomaisesti arkkitehtoniseen mappaukseen.

Avaa vyöhykkeen asetukset napsauttamalla mitä tahansa vyöhykettä hiiren oikealla painikkeella. Tästä oikean painikkeen valikosta voit:

* Nimetä vyöhykkeen uudelleen (tästä voi olla apua sen tunnistamisessa Clip Deckissä, varsinkin jos vyöhykkeitä on paljon!)
* Ottaa vyöhykkeen käyttöön tai poistaa sen käytöstä
* Lukita sen sijainnin
* Vaihtaa sen muototyyppiä
* Palauttaa sen oletussijaintiin
* Käyttää muototyyppikohtaisia asetuksia
* Poistaa sen
* Lisätä _Alt Zone_ -vyöhykkeen (katso [Alt-vyöhykejärjestelmä](alt-zone-system.md))

{% hint style="danger" %}
**VAROITUS -** ole erittäin varovainen, kun vaihdat vyöhyketyyppiä laserin ollessa aktiivinen. Vyöhyke palaa kyseisen muodon viimeiseen sijaintiin/kokoon, joten ulostulo voi muuttua äkillisesti. Laser kannattaa sammuttaa ennen vyöhyketyypin vaihtamista.
{% endhint %}

### Quad-vyöhykemuoto

Voit siirtää quad-muodon jokaista kulmaa hiirellä. Siirrä kulmaa muista riippumatta ja vääristä quad napsauttamalla kulmaa `Alt / Option` -näppäin painettuna. Kun quad on vääristetty, kaikkia kulmia voi siirtää vapaasti.

Voit poistaa vääristymän ja palauttaa muodon akselien suuntaiseksi suorakulmioksi oikean painikkeen valikon _REMOVE DISTORTION_ -painikkeella.

#### Perspektiivikorjaus

Tämä asetus voidaan määrittää oikean painikkeen valikon vaihtopainikkeella, ja se määrittää vääristysmenetelmän. Beam-sisällössä tämä kannattaa yleensä pitää pois päältä, mutta jos tämä vyöhyke projisoi grafiikkaa tasaiselle pinnalle, ota se käyttöön, jolloin ulostuloon tehdään perspektiivikorjaus.

{% hint style="info" %}
Jos _Perspective correction_ on pois päältä, sisältö vääristetään _bi-linear interpolation_ -menetelmällä. Toisin sanoen sisältö sijoittuu tasaisesti koko quad-muodon alueelle. Siksi se sopii parhaiten säteille.

Kun perspektiivikorjaus on käytössä, sisältö vääristetään perspektiivimuunnoksella, joka kompensoi lyhenemää. Jos siis projisoit grafiikkaa seinälle vinosta kulmasta, voit käyttää tätä ulostulon oikaisemiseen ja projektion vääristymän korjaamiseen.
{% endhint %}

### Line / Curve -vyöhykemuoto

Line / Curve -vyöhykemuodosta on tullut oma vakio valintani viimeaikaisissa show’issa, ja voisi hyvin väittää, että sen pitäisi olla beam zone -vyöhykkeiden oletus.

Usein vyöhykkeideni täytyy olla kapeita, jotta ne mahtuvat hankaliin kapeisiin kohtiin tapahtumapaikoissa tai rakennusten ikkunoiden väliin. Huomasin, että quad-muodon neljän kulman säätäminen voi olla todella hankalaa, kun kulmat ovat hyvin lähellä toisiaan. Näin syntyi Line / Curve -vyöhyke!

Suoriin linjoihin tarvitset vain kaksi pistettä. Säädä sen jälkeen _Zone thickness_ oikean painikkeen valikosta. Tämä on nopein tapa luoda yksinkertaisia vyöhykkeitä.

Luo lisää pisteitä napsauttamalla linjaa `Alt / Option` -näppäin painettuna. Nämä pisteet pehmennetään automaattisesti sulavan muodon luomiseksi, ja voit säätää _Smooth level_ -arvoa mahdollisten mutkien tasoittamiseksi.

Poista piste napsauttamalla sitä `Alt / Option` -näppäin painettuna.

Jos sinulla on kokemusta vektorigrafiikkasovelluksista (Inkscape, Illustrator jne.), voit käyttää _Manually adjust bezier curves_ -asetusta ja hienosäätää kaikkia ohjauspisteitä.

### Segmented-vyöhykemuoto

Tämän jaetun vyöhykkeen avulla voit tehdä erittäin tarkkoja korjauksia, ja se on hyödyllinen, kun mappaat monimutkaisiin muotoihin. Voit lisätä tai poistaa jakoja oikean painikkeen valikon + ja - -painikkeilla.

### Kokonaan toisen vyöhykkeen peittämän vyöhykkeen muokkaaminen

Napsauta päällä olevaa vyöhykettä hiiren oikealla painikkeella ja lukitse se napsauttamalla lukkopainiketta. Tämän jälkeen voit muokata ja säätää alla olevaa vyöhykettä.

<br>

{% hint style="info" %}
Kun lisäät Beam zone -vyöhykkeen ulostuloosi, voit lisätä sen klippiin Clip Deckissä.
{% endhint %}
