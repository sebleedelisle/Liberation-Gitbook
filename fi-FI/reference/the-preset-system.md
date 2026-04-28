---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Preset-järjestelmä

Liberation käyttää Preset-järjestelmää eri paikoissa silloin, kun useita valittavia asetuksia täytyy tallentaa _presets_-luettelosta valittaviksi.

Järjestelmää käytetään tällä hetkellä seuraaviin:

* Scanner-asetukset
* Värikalibroinnin asetukset
* 3D Visualiser -kameran asetukset
* 3D Visualiser -laserien asetukset
* DMX-profiilit

Jos siis säädät scanner-asetukset uusille hienoille CT6210-scannereillesi, voit tallentaa ne presetiksi, nimetä sen "CT6210", ja se on jatkossa käytettävissä preset-luettelossa aina kun tarvitset sitä sekä valittavissa pudotusvalikosta.

Kaikki presetit tallennetaan projektisi (tai laserasetustesi) mukana riippumatta siitä, käytätkö niitä vai et. Aina kun lataat jonkin näistä tiedostoista, kaikki sen sisältämät presetit lisätään olemassa oleviin presetteihisi. Jos ladatulla presetillä on sama nimi kuin jollakin olemassa olevalla presetilläsi, se korvaa olemassa olevan presetin.

Voit lisäksi tuoda ja viedä preset-tiedostoja preset-pudotusvalikon vieressä olevalla load/save-painikkeella (levykekuvake). Tämä avaa ponnahdusikkunan, jossa on import/export-painikkeet sekä mahdollisuus poistaa yksi tai useampi preseteistäsi.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Ponnahdusvalikko, joka avautuu, kun napsautat load/save-kuvaketta</p></figcaption></figure>

Jos muokkaat preset-asetusta, esimerkiksi scanner-asetusta nimeltä _Default_, huomaa, että muut laserit eivät päivity automaattisesti. Sen sijaan kunkin laserin scanner-asetusten nimeksi tulee nyt _Default(edited)_. Päivitä asetus uuteen _Default_-presetiin valitsemalla se uudelleen pudotusvalikosta.

{% hint style="info" %}
Jos sinulla on paljon lasereita ja haluat päivittää kaikkien scanner-asetukset, käytä _COPY LASER SETTINGS_ -järjestelmää. Katso [copy-laser-settings.md](../setting-up/copy-laser-settings.md)
{% endhint %}

Jos poistat presetin, jota käytetään muualla, et menetä asetusta, vaan näet sen merkinnällä _(deleted)._
