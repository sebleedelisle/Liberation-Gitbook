---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Johdanto

Liberation sisältää joustavan ja tehokkaan DMX-järjestelmän, jolla voit luoda valotehosteita ja ohjata DMX-yhteensopivia lasereita Art-Netin kautta. Sen tarkoitus on helpottaa valojen pitämistä synkronissa lasershow’n kanssa – erillistä valopöytää ei tarvita.

{% hint style="info" %}
**Mikä Art-Net on, ja miten se liittyy DMX:ään?**

**DMX** on järjestelmä, jota on käytetty jo vuosia valojen, laserien, savukoneiden ja muiden lavaefektien ohjaamiseen. Se lähettää ohjaussignaaleja erityisiä kaapeleita pitkin (yleensä XLR-liittimillä), ja jokainen laite kuuntelee tiettyä kanava-aluetta tietääkseen, mitä sen pitää tehdä.

**Art-Net** on uudempi tapa lähettää samaa DMX-dataa tavallisen tietokoneverkon kautta. Erikoiskaapeleiden sijaan kaikki lähetetään Ethernetin yli, aivan kuten internet- tai lähiverkkoliikenne.

Liberationissa kaikki DMX-lähtö lähetetään Art-Netillä. Voit ohjata sillä suoraan Art-Net-yhteensopivia laitteita, tai voit liittää järjestelmään **Art-Net-noden** – pienen laitteen, joka muuntaa Art-Netin takaisin tavalliseksi DMX:ksi. Näin voit ohjata myös perinteisiä DMX-valoja ja -efektejä, vaikka ne eivät itse tukisi Art-Netiä.
{% endhint %}

Voit käyttää sitä myös monenlaisten muiden lavalaitteiden ohjaamiseen, kuten savukoneiden, hazerien, CO₂-tykkien, kylmäkipinäkoneiden ja muiden vastaavien laitteiden kanssa. Jos laite tukee DMX:ää, voit määrittää sen DMX-alueeksi ja käynnistää sen suoraan Liberationista laserisisällön rinnalla.

DMX-laitteet lisätään **DMX-alueina**, jotka näkyvät alueluettelossa laser beam -alueiden ja Canvas-kohdealueiden rinnalla. Jokainen DMX-alue käyttää **DMX-esiasetusta**, joka kertoo Liberationille, miten laser-clipeistä tulevat ominaisuudet – kuten sijainti, väri ja kirkkaus – muunnetaan DMX-kanava-arvoiksi.

Kun lähetät clipin DMX-alueelle, Liberation tarkistaa clipin ensimmäisen elementin ja muuntaa sen ominaisuudet esiasetuksen perusteella. Näin valojen ja DMX-efektien ohjaaminen onnistuu helposti samoista clipeistä, joita käytät jo lasereille.

#### Liberation Glastonburyssa

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Liberationin DMX-järjestelmän ensimmäinen todellinen testi oli Glastonbury 2023 -tapahtumassa, jossa Reach Lasers asensi yhteensä 90 sädelähdettä osaksi Arcadia “spider” -lavaa.

18 laseria ohjattiin sisäisillä Ether Dream -ohjaimilla, ja lisäksi 12 kuusipäistä beam bar -laitetta ohjattiin Art-Netin ja DMX:n kautta.
