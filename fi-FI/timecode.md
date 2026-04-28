---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation tukee synkronointia ulkoisen SMPTE/LTC-timecode-signaalin kanssa. Sitä käytetään yleisesti live-musiikkiesityksissä pitämään valot, pyrotekniikka, video ja taustanauhat synkassa.

{% hint style="info" %}
Mikä on SMPTE/LTC?

SMPTE on timecode-standardi, ja LTC on tämä timecode muunnettuna audiosignaaliksi. Jos kuuntelet tätä ääntä, se kuulostaa hirveältä korkealta vinkumiselta, mutta tietokoneille se on tarkkaa ajoitustietoa.

**Nörttifaktoja!**

Historiallisesti SMPTE:tä on käytetty pitämään video ja ääni synkassa. Analogisen nauhan kanssa synkronoitaessa yhdelle raidalle voitiin tallentaa timecode-ääni, mitä kutsuttiin joskus nauhan "raidoittamiseksi" ("striping"). Tämän timecode-raidan avulla useita nauhureita voitiin pitää keskenään synkassa tai MIDI-sekvensseri voitiin pitää synkassa nauhan kanssa. (Näin MIDI-soittimia ei tarvinnut tallentaa nauhalle, vaan sekvensseri pystyi soittamaan ne livenä miksauksen aikana!)

SMPTE tulee sanoista Society of Motion Picture and Television Engineers, eli standardin määritelleestä organisaatiosta. LTC tulee sanoista _Linear TimeCode._
{% endhint %}

Voit vastaanottaa LTC-timecode-signaalin minkä tahansa tietokoneesi ääniliitännän kautta, mutta suositeltavaa on käyttää ammattilaistason äänikorttia, jossa on vähintään yksi säädettävä XLR-tulo ja monitorointimahdollisuus.

Minulla on hyviä kokemuksia [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) -äänikortista, koska siinä on kuulokemonitorointi, 2 XLR-tuloa eikä se tarvitse erillisiä ajureita (ainakaan macOS:ssä). Jos käytät sitä aina vain timecodeen, voit hankkia hieman edullisemman [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) -mallin (siinä on vain yksi tulo eikä MIDIä), mutta käytännössä mikä tahansa kohtuullisen hyvä äänikortti toimii.

{% hint style="info" %}
LTC-timecode-signaalit jaetaan yleensä balansoituja XLR-kaapeleita pitkin, koska ne ovat riittävän luotettavia siirtämään matalatasoisia audiosignaaleja pitkiä matkoja. (XLR on pyöreä liitin, jota käytetään yleensä mikrofonien kanssa.)
{% endhint %}

### Laitteiston kytkennät

Kytke timecode-signaalin XLR-kaapeli äänikorttiisi ja varmista, että signaali on hyvä. Säädä äänikortin tasoa, kunnes signaali on vahva mutta ei leikkaa. Jos äänikortissa on kuulokeliitäntä, voit kuunnella timecodea ja varmistaa, ettei siinä ole häiriöitä tai liikaa kohinaa.

{% hint style="info" %}
Teoriassa signaali on mahdollista vastaanottaa MacBookin jack-liitännän kautta, mutta se vaatisi erikoiskaapelin. Nämä liitännät ovat yleensä 4-napaisia TRRS-minijack-liittimiä, enkä rehellisesti sanottuna ole varma, mitä näistä liittimistä voi käyttää audiotulona. En myöskään ole varma, millaisen jännitetason se kestää (olen lukenut jostain arvon +/-1V, mutta käytä tätä omalla vastuullasi!).

Luulen, että sinun kannattaa mieluummin hankkia edullinen USB-äänikortti kuin yrittää tätä.
{% endhint %}

Jos äänikortissasi ei ole minkäänlaista tulomonitorointia, voit tarkistaa macOS:n järjestelmäasetuksista (_Sound_-kohdasta), että saat signaalin. (Windowsissa käytä _Sound Control Panel_ -paneelia.)

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS näyttää minkä tahansa äänikortin tulotason Sound-järjestelmäasetuspaneelissa</p></figcaption></figure>

### Asetusten määrittäminen Liberationissa

1. Valitse äänikorttisi ja oikea tulokanava Timecode-asetusikkunassa.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Huomaa, että pudotusvalikossa on erilliset vaihtoehdot äänikorttisi jokaiselle tulokanavalle.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Huomaa vasemmalla oleva neliö. Jos vastaanotat kelvollista timecode-signaalia, se muuttuu vihreäksi. Muussa tapauksessa se on punainen.

2. Valitse saapuvan timecoden oikea kuvataajuus. Timecoden toimittajan pitäisi pystyä kertomaan, mikä frame rate on. (Jos valitset väärän arvon, synkronointi toimii silti, mutta huomaat pienen "hyppäyksen" joka sekunti.)
3. Avaa Timeline-näkymän timecode-asetukset aikajanapalkin pienestä kellokuvakkeesta ja valitse SMPTE(LTC)-vaihtoehto.

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Säädä start offset (tunteina, minuutteina, sekunteina ja frameina) vastaamaan kappaleen alkua. Jos sinulla on useita timelineja, nämä asetukset täytyy määrittää jokaiselle erikseen.

{% hint style="info" %}
Kiertuekäytössä yleinen käytäntö on, että jokainen kappale alkaa eri tunnilta, esimerkiksi 01:00:00:00 ensimmäiselle kappaleelle, 02:00:00:00 toiselle kappaleelle ja niin edelleen.

Liberation vaihtaa automaattisesti timelineen timecoden perusteella, joten timelineja ei tarvitse vaihtaa esityksen aikana käsin.
{% endhint %}

Huomaa, että toisin kuin MIDI Clock ja Ableton Link, SMPTE on _absoluuttinen_ aikajärjestelmä, joka mitataan tunteina, minuutteina, sekunteina ja frameina. Liberationin ydinaikajärjestelmä perustuu iskuihin ja tahteihin, joten timecodea vastaanotettaessa se käyttää timelineen määritettyä tempoa. Varmista, että tämä tempo on synkassa sen musiikin kanssa, joka on myös synkronoitu timecodeen.
