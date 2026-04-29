---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Lataaminen ja tallentaminen

Liberation tallentaa tilansa jatkuvasti levylle, joten sähkökatkon tai järjestelmäongelman jälkeen se käynnistyy siitä kohdasta, johon se jäi. Vyöhykkeet, aikajanat ja muu sisältö eivät normaalisti katoa.

Voit kuitenkin viedä kokoonpanosi varmuuskopioksi tai siirtää sen toiseen tietokoneeseen.

### Projektin tuonti/vienti

Projektitiedosto tallentaa lähes kaiken nykyisestä kokoonpanostasi, mukaan lukien:

* Kaikki, mitä on kuvattu kohdassa [Lataaminen ja tallentaminen](loading-and-saving.md#laser-settings-import-export) alla
* Clips, efektit ja ryhmäasetukset
* Kaikki aikajanasi (ei sisällä ääni- ja videomediaa)
* Art-Net-kokoonpano
* MIDI-lähetys- ja vastaanottoasetukset
* Tempo- ja synkronointiasetukset

Se ei tällä hetkellä tallenna eikä lataa:

* Ääni- ja MIDI-syöteasetuksia, joita käytetään MIDI notes -nodessa ja Sound Input Oscillatorissa (se _tallentaa_ kuitenkin MIDI-lähetys- ja vastaanottoasetukset sekä timecode-äänisyötteen)
* Käyttöliittymän skaalausta
* Canvas-opaskuvien mediaa
* Aikajanojen ääni- ja videomediaa
* Text-nodessa käytettyjä fontteja

{% hint style="danger" %}
Aikajanan ääni- ja videotiedostoja ei tallenneta projektitiedostojen mukana, joten tallenna ne erikseen, jos haluat siirtää ne toiseen tietokoneeseen. Katso [Lataaminen ja tallentaminen](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Laserasetusten tuonti/vienti

* Jokaisen laserin laserasetukset
* Sädealueet
* Canvas-kohdealueet
* DMX-alueet
* Laserohjainten määritys (sekä aliakset kaikille ohjaimille, jotka olet nimennyt uudelleen)
* Laserskannerin ja värikalibroinnin asetukset ja presetit
* 3D visualiser -asetukset ja presetit

### Clip Deckin tuonti/vienti

* Kaikki Clips ja niiden aluemääritykset, asetukset ja parametrit
* Kaikki ryhmäasetukset, flash mode, fade in/out -ajat jne.

Se ei tällä hetkellä tallenna eikä lataa:

* Kaikkia efektejä ja niiden parametreja ja asetuksia

{% hint style="info" %}
**Lataa Clips projektitiedostosta lataamatta koko projektia**

Jos haluat tuoda projektista vain Clips, valitse _**Clips->Import Clip Deck**_ ja valitse Clip Deck -tiedoston (.cpdk) sijaan projektitiedosto.
{% endhint %}

### Clip Deckin lisääminen

Voit lisätä Clips viedystä Clip Deck -tiedostosta nykyiseen projektiisi käyttämällä _Append Clip Deck_ -toimintoa. Clips lisätään nykyisen Clip Deckin loppuun, mutta tiedoston efektejä ja ryhmäasetuksia ei tuoda.

### Valittujen Clips vienti

Kaikki tällä hetkellä valitut Clips viedään tiedostoon. Ryhmäasetuksia ja efektejä ei tallenneta, vain Clips. Huomaa, että parhaillaan käynnissä olevia aktiivisia Clips ei viedä, elleivät ne ole myös valittuina.

{% hint style="info" %}
Valitse Clips käyttämällä Option/Alt–Shift–napsautusta (tai lasso-valintaa). Valitut Clips tunnistaa niiden ympärillä olevasta paksusta valkoisesta reunuksesta. Katso [Clipien käynnistäminen ja pysäyttäminen](clips/starting-stopping-clips.md)
{% endhint %}

### Efektien tuonti/vienti

Lataa ja tallentaa kaikki efektit sekä niiden ryhmäasetukset ja parametrit.

{% hint style="info" %}
**Lataa efektit projektitiedostosta lataamatta koko projektia**

Jos haluat tuoda projektista vain efektit, valitse _**Effects->Import Effects**_ ja valitse efektitiedoston (.efts) sijaan projektitiedosto.
{% endhint %}

### Aikajanan vienti

Vie aikajanatiedoston, jossa on yksi tai useampi aikajana. Huomaa, että Clip Deck sisällytetään aina vietyihin aikajanatiedostoihin (voit kuitenkin valita, mitkä Clips tuot takaisin, katso [Lataaminen ja tallentaminen](loading-and-saving.md#timeline-import) alla).

Jos projektitiedostossasi on useampi kuin yksi aikajana, avautuu paneeli, jossa voit valita vietävät aikajanat.

{% hint style="danger" %}
Aikajanan ääni- ja videotiedostoja ei tallenneta aikajanatiedostojen mukana, joten tallenna ne erikseen, jos haluat siirtää sisältösi toiseen tietokoneeseen. Katso [Lataaminen ja tallentaminen](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Aikajanan tuonti

Tuo yksi tai useampi aikajana yhdestä aikajanatiedostosta. Kun olet valinnut aikajanatiedoston, avautuu paneeli, jossa on useita tuontiasetuksia.

Jos aikajanatiedostossa on useampi kuin yksi aikajana, ne kaikki näytetään luettelossa. Valitse mukaan otettavat aikajanat.

* Replace existing timelines\
  Poistaa kaikki nykyiset aikajanasi ja korvaa ne tuoduilla aikajanoilla
* Import used clips only\
  Tuo vain käytetyt Clips ja järjestää ne ryhmiin, yksi ryhmä kutakin aikajanaa varten. Jos tätä asetusta ei ole valittu, aikajanatiedoston koko Clip Deck lisätään olemassa olevien Clips perään.
* Replace existing clip deck\
  Korvaa nykyisen Clip Deckin aikajanatiedoston Clips. Käytettävissä vain, jos _Replace existing timelines_ on valittu.

{% hint style="info" %}
**Lataa aikajanat projektitiedostosta lataamatta koko projektia**

Jos haluat tuoda projektista vain aikajanat, valitse _**Timeline->Import Timeline(s)**_ ja valitse aikajanatiedoston (.ltml) sijaan projektitiedosto.
{% endhint %}

### DMX / Art-Net -tuonti/vienti

Tallentaa ja lataa Art-Net-nodet sekä niiden IP-osoitteet. Sisältää myös DMX-alueet ja kaikki DMX-presetisi.

### Tärkeä huomautus aikajanan mediatiedostoista

Ääni- ja videotiedostoja **ei** tällä hetkellä viedä aikajanatiedoston mukana. Jos sinun täytyy siirtää sisältöä toiseen tietokoneeseen, varmista, että sisällytät myös nämä tiedostot.

{% hint style="info" %}
**Miten aikajana etsii mediatiedostoja**

Kun aikajana ladataan, se etsii tiedostoja samasta kansiosta kuin aikajana- tai projektitiedosto sekä sen alikansioista. Kun tiedostot ovat samassa kansiossa tai alikansiossa (kuten _/videos_ tai _/sound_), ne löytyvät latauksen yhteydessä.
{% endhint %}
