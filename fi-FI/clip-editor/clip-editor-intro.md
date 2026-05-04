---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Johdanto Clip Editoriin

Clip editor on monipuolinen tapa luoda lasersisältöä, ja se on Liberationin ytimessä. Yksinkertaisten asioiden tekeminen on helppoa, mutta editori on silti riittävän joustava myös erittäin hienostuneiden ja monimutkaisten efektien rakentamiseen.

{% hint style="info" %}
Solmupohjainen editori oli ensimmäinen osa Liberationia, joka tehtiin! Se sai alkunsa keskustelusta Rob Stanleyn kanssa UK laser meet up -tapaamisessa vuonna 2018 siitä, miltä "oliopohjainen" lasersisällön suunnittelutyökalu voisi näyttää.

Vaikka se vaikuttaa yksinkertaiselta, kyseessä on melko monimutkainen järjestelmä rakentaa. Vuoden 2019 alkuun mennessä minulla oli kuitenkin toimiva demo, joka todisti idean toimivaksi – ja siitä koko matka alkoi!
{% endhint %}

Se on solmupohjainen visuaalinen editori (eli [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)), joka tuntuu tutulta, jos olet käyttänyt esimerkiksi TouchDesigneria, MaxMSP:tä tai VVVV:tä. Clip editor on kuitenkin hieman erilainen ja jonkin verran yksinkertaisempi, koska se on suunniteltu nimenomaan vektorigrafiikkaa varten.

Voit avata Clip Editorin napsauttamalla Clip-painiketta hiiren oikealla painikkeella ja valitsemalla _EDIT CLIP_. Voit myös napsauttaa tyhjää Clip-painiketta hiiren oikealla painikkeella ja valita _CREATE AND EDIT CLIP_.

### Yleiskuva

Clip editorissa näet seuraavat asiat:

* Yläreunassa olevat **Creator**- ja **Operator**-solmupainikkeet
* Vasemmassa reunassa olevat **Oscillator**-solmupainikkeet
* Oikealla olevassa paneelissa sisällön esikatselun. Jos napsautat solmua, näet myös toisen esikatselun, joka näyttää sisällön kyseisen solmun kohdalla.
* Kaikki muokattavan clipin solmut ja yhteydet. Jos kyseessä on uusi clip, alue on tyhjä.
* Clip Editor -paneelin eri asetuksineen

Muokkauksen aikana näet myös taustalla 3D visualiserissa, miltä clip näyttää.

{% hint style="info" %}
Jos et näe 3D visualiserissa mitään ulostuloa, sinun täytyy ehkä ottaa haluamasi zonet käyttöön zone-painikkeilla. Varmista myös, että _Preview to lasers_ on käytössä. Katso alempaa [Johdanto Clip Editoriin](clip-editor-intro.md#clip-editor-panel "mention").
{% endhint %}

### Clipin rakentaminen

Yleensä aloitat yhdellä tai useammalla [Creator-nodet](creator-nodes.md) ja yhdistät vasemmalta oikealle [Operaattorisolmut](operator-nodes/), jotka käsittelevät sisältöä. Kun siirrät creator- ja/tai operator-solmuja lähelle toisiaan, huomaat, että ne yhdistyvät automaattisesti. Voit irrottaa ne toisistaan vetämällä ne jälleen erilleen.

### Solmujen lisääminen clipiin

Napsauta ja vedä jokin ylä- tai vasemman reunan solmupainikkeista tyhjään kohtaan clip editorissa.

### Solmun asetusten säätäminen

Avaa solmun ominaisuuspaneeli napsauttamalla hammasrataskuvaketta solmun oikeasta yläkulmasta.

### Solmun käyttöönotto ja poistaminen käytöstä

Ota solmu käyttöön tai poista se käytöstä napsauttamalla virtakuvaketta solmun vasemmasta yläkulmasta. Solmu himmenee osoittaakseen, ettei se ole parhaillaan aktiivinen. Huomaa, että sisältö kulkee edelleen operator-solmun läpi, vaikka solmu olisi poistettu käytöstä, mutta solmu ei vaikuta sisältöön.

### Solmujen yhdistäminen

Sisältö luodaan creator-solmulla, ja se kulkee solmujen läpi vasemmalta oikealle. Jokainen operator vaikuttaa sisältöön jollakin tavalla ja välittää sen seuraavalle operatorille. Polun loppuun jäävä sisältö on clipin sisältö. Creator- ja Operator-solmut yhdistyvät automaattisesti, kun siirrät ne lähelle toisiaan. Voit erottaa ne vetämällä ne jälleen erilleen.

{% hint style="info" %}
Voit yhdistää useamman kuin yhden solmun seuraavan solmun tuloon. Tämä on hyödyllistä, kun haluat yhdistää useita sisältöosia.
{% endhint %}

### Solmun ominaisuudet ja liitännät

Jokaisen solmun alareunassa on joukko liitäntöjä, joista jokainen vastaa solmun ominaisuutta, kuten kirkkautta, sijaintia, skaalaa tai kiertoa.

[Oscillaattorisolmut](oscillators/) voidaan yhdistää näihin liitäntöihin alapuolelta ja käyttää niiden asetusten animointiin. Oscillator-solmuissa on ulostulo yläreunassa. Napsauta ja vedä siitä yhteys ja pudota se jonkin toisen solmun ominaisuusliitäntään.

### Oscillator-solmut

Oscillator-solmuilla muutetaan ominaisuuksia ajan kuluessa. Ne edustavat yleensä aaltomuotoja, kuten sahalaita- tai siniaaltoa, mutta osa oscillator-solmuista käyttää lähteenään ulkoisia syötteitä, kuten mikrofonin tulotasoa.

{% hint style="info" %}
Jos olet joskus käyttänyt analogista syntetisaattoria, oskillaattorien käsite on sinulle tuttu: niitä käytetään yleisesti aaltomuotojen luomiseen tai äänen muuttamiseen ajan kuluessa. Liberationin oscillator-solmut tekevät samankaltaista työtä.

**Hauska fakta:** nimi _Liberation_ sai inspiraationsa Moog Liberationista, vuonna 1980 julkaistusta "keytar"-syntetisaattorista, jonka tekivät tunnetuksi Herbie Hancock, Jean-Michel Jarre ja jopa James Brown!
{% endhint %}

Oscillator-solmuilla on aina _range_-asetukset, joilla määritetään säädettävän ominaisuuden minimi- ja maksimiarvo. _Wave Oscillators_ -solmuilla on lisäksi aina _duration_-asetus, joka määrittää, kuinka nopeasti oscillator muuttaa arvoa. Lisätietoja on kohdassa [Wave-oskillaattorit](oscillators/wave-oscillators.md "mention").

### Clip editor -paneeli

* Timer – paneelin yläreunassa näet clipin nykyisen ajan sen edetessä
* _RETRIGGER_ – käynnistää clipin uudelleen alusta; erityisen hyödyllinen, jos clip ei looppaudu
* _Preview to lasers_ – kun tämä on valittuna, 3D visualiser päivittyy samalla kun muokkaat tätä clipiä. Jos poistat sen käytöstä, näet editorin ulkopuolella käynnissä olevat clipit. Tämä on yleinen asetus, ei clip-kohtainen.
* _UNDO/REDO_ – koskee itse clip editoria. Toiminnot on myös määritetty pikanäppäimille `Cmd / Ctrl + Z` ja `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ – tallentaa muokkaukset, mutta varoittaa ylikirjoittamisesta
* _SAVE AS A COPY_ – tallentaa clipin seuraavaan vapaaseen paikkaan clip deckissä. Tästä tulee clipin uusi sijainti, ja kaikki myöhemmät tallennukset tehdään tähän uuteen paikkaan.
* _EXIT EDITOR_ – sulkee clip editorin. Jos sinulla on tallentamattomia muutoksia, näet vahvistuspaneelin.
