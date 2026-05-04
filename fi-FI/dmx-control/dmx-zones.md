---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ DMX-alueet

DMX zone on Liberationin Output zone, joka lähettää Art-Net/DMX-dataa laserpisteiden sijaan. Ne näkyvät beam zone- ja canvas zone -kohteiden rinnalla, joten Clips voidaan määrittää niihin samalla zone-valinnan työnkululla.

Hallinnoi niitä avaamalla valikosta **DMX Zones** tai käyttämällä Laser Overview -näkymän DMX-osiota.

* **ADD DMX ZONE** - luo uuden DMX zone -kohteen.
* **ARM** - ottaa DMX-lähdön käyttöön kyseiselle zone-kohteelle. Kun DMX zone ei ole valmiustilassa, sen määritetyt kanavat tyhjennetään nollaan.
* **Node** - valitsee Art-Net-node-numeron.
* **Universe** - valitsee Art-Net-universumin. Näytettävä arvo alkaa luvusta 1, joten Universe 1 on ensimmäinen universumi.
* **Address** - asettaa valaisimen aloitusosoitteen. Myös näytettävä arvo alkaa luvusta 1.
* **Preset** - valitsee DMX-esiasetuksen, joka kohdistaa Clip-sisällön DMX-kanaviin.
* **Edit DMX zone settings** (kynäkuvake) - avaa zone-asetukset, kuten manuaalisen zone-välityksen ja valaisimen suunnan.
* **Edit DMX profile/channel mapping** (liukusäädinkuvake) - avaa DMX-esiasetusten ja kanavien editorin.
* **Delete** - poistaa DMX zone -kohteen.

### Valmiustilan rajoitukset

Samanaikaisesti valmiustilaan asetettavien DMX zone -kohteiden määrä riippuu lisenssitasostasi. Jos tasosi ei salli DMX-lähtöä tai olet jo asettanut valmiustilaan enimmäismäärän DMX zone -kohteita, lisävyöhykkeiden **ARM**-painike poistetaan käytöstä ja näyttää kielletty-kuvakkeen, kun osoitin viedään sen päälle.

Poista toinen DMX zone valmiustilasta tai käytä lisenssitasoa, jossa DMX-raja on suurempi, ennen kuin asetat lisää zone-kohteita valmiustilaan.
