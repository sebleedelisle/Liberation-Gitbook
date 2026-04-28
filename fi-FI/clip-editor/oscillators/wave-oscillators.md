---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Wave-oskillaattorit

## Tällä sivulla:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Sawtooth wave](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Triangle wave](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sine wave](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Square wave](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Wave-oskillaattorien asetukset

Kaikilla Wave-oskillaattoreilla on seuraavat asetukset:

* **range min / range max** - määrittää arvoalueen ominaisuudelle, jota oskillaattori ohjaa. Ominaisuus asetetaan arvoon _range min_, kun aaltomuoto on alhaalla, ja arvoon _range max_, kun aaltomuoto on ylhäällä.

{% hint style="info" %}
Jos esimerkiksi haluat pisteen liikkuvan vasemmalle ja oikealle välillä -100 ja 100, yhdistä oskillaattori _x property socket_ -liitäntään, aseta _min range_ arvoon -100 ja _max range_ arvoon 100.
{% endhint %}

* **duration** - aika, joka yhdeltä täydeltä jaksolta (eli _loopilta_) kestää valmistua. Tämä suhteutetaan tempoon tahteina. Siksi ¼ on yksi isku. 1 on kokonainen tahti jne.
* **duration multiplier** - skaalaa peruskeston valitulla kertoimella. Jos esimerkiksi duration on asetettu neljäsosanuottiin ja kerroin on 3, oskillaattori kestää kolme neljäsosanuottia (pisteellinen puolinuotti). Myös murtolukukertoimet ovat tuettuja — pidä _SHIFT_ painettuna liukusäädintä vetäessäsi, jos haluat asettaa muita kuin kokonaislukuja. Tämä on hyödyllistä vaiheistusvaikutuksiin tai hienovaraisiin ajoituksen muutoksiin.
* **offset** - aallon aloitussiirtymä prosentteina kestosta. Jos haluat aallon alkavan neljäsosan kohdalta, aseta arvoksi 25%.
* **repeat count** - kuinka monta kertaa looppi toistuu ennen pysähtymistä. Oletus on _FOREVER_, mutta voit muuttaa sitä, jos et halua oskillaattorin jatkuvan loputtomasti. Kun oskillaattori pysähtyy, ominaisuus asetetaan aallon lopussa olevaan arvoon.
* **delay count** - viive iskuina ennen kuin oskillaattori alkaa käydä. Ennen käynnistymistä ominaisuus asetetaan aallon alun arvoon.

{% hint style="info" %}
Kun käytät _repeat count_ ja _delay count_ -asetuksia harkitusti, voit luoda hyvin monimutkaisia animaatioita — melkein kuin niillä olisi oma aikajanansa!
{% endhint %}

## Yleiset asetukset

* **steps** - jakaa liikkeen tiettyyn määrään erillisiä askelia. Hyvä silloin, kun haluat ominaisuuksien "hyppäävän" arvoihin sen sijaan, että ne liikkuisivat pehmeästi.

{% hint style="info" %}
Huomaa, että askeleet jaetaan ajan, ei arvon perusteella. Jos aalto jaetaan 4 askeleeseen ja sen kesto on 1 tahti, ominaisuus muuttuu välittömästi jokaisella iskulla.
{% endhint %}

* **clamp min / clamp max -** kasvattaa aallon skaalaa sen minimi- tai maksimiarvojen yli ja rajoittaa lopputuloksen.

{% hint style="info" %}
_clamp_-käsitettä on melko vaikea selittää, mutta ajattele aaltomuotoa, joka menee kuvaajan ylä- tai alareunan yli ja leikataan sitten reunoihin. Suosittelen kokeilemaan näitä asetuksia! Ne ovat erittäin hyödyllisiä, jos haluat sawtooth-aallon alkavan myöhässä tai päättyvän aikaisin.
{% endhint %}

* **ease function** - Sawtooth- ja Triangle-aalloissa on myös ease function, joka muuttaa animaatiokäyrää hienovaraisesti ja voi tehdä animaatioistasi paljon ilmaisuvoimaisempia.
  * **LINEAR** - oletus, ei easingia, vaan liikkuu lineaarisesti minimi- ja maksimiarvojen välillä.
  * **EASE OUT** - alkaa nopeasti ja hidastuu loppua kohti. Erittäin hyvä fysiikan simulointiin, esimerkiksi pysähdykseen hidastumiseen.
  * **EASE IN** - alkaa hitaasti ja nopeutuu vähitellen. Hyvä kasvavan liike-energian simulointiin.
  * **EASE IN/OUT** - näiden yhdistelmä, joka tuottaa hyvin orgaanisen liikkeen.

{% hint style="warning" %}
**Easing -** Suosittelen välttämään oletuksena olevaa lineaarista animaatiota aina kun mahdollista, ellet nimenomaan halua robottimaiselta näyttävää liikettä. Easing voi tehdä animaatioista paljon sulavampia ja orgaanisempia!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sawtooth wave

Tunnetaan joskus myös nimellä _ramp waveform_, koska se nousee ylöspäin ja putoaa jakson lopussa äkillisesti. Tämä on luultavasti yleisin wave-oskillaattori, koska sillä voi luoda loopin esimerkiksi _hue_- tai _rotation_-ominaisuuksien kierrättämiseen.

Katso yllä olevat osiot:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Sawtooth-kohtaiset asetukset:

* **cycle range compensation** - käytettävissä, kun **steps** on asetettu. Hyvä arvojen kierrättämiseen, esimerkiksi rotation välillä 0–360. Kun tämä ei ole käytössä, alku- ja loppuarvot ovat samat, mikä voi aiheuttaa takertumista alkupisteeseen (koska 0 ja 360 ovat sama kulma). Ota tämä käyttöön, niin enimmäisaluetta pienennetään askelpaikkojen korjaamiseksi.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Triangle wave

Toisin kuin _sawtooth wave_, joka hyppää jokaisen jakson alussa takaisin alkuun, _triangle wave_ liikkuu lineaarisesti eteenpäin ja sitten takaisinpäin.

Katso yllä olevat osiot:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sine wave

Pehmein aaltomuoto! Värähtelee kevyesti kahden arvon välillä kuin heiluri.

Katso yllä olevat osiot:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Square wave

Yksinkertaisin aaltomuoto — se vain vaihtaa kahden arvon välillä edestakaisin!

Katso yllä olevat osiot:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Square wave -kohtaiset asetukset:

* **pulse width** - aika, jonka aalto on maksimiarvossaan suhteessa kokonaiskestoon. Oletus on 50%, eli täsmälleen puolet ja puolet. Jos haluat sen olevan "päällä" vain neljäsosan ajasta, aseta arvoksi 25%. Voit säätää pulssin ajankohtaa _offset_-arvolla.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

Yksi Liberationin vahvuuksista on, että se voi luoda satunnaisia mutta toistettavia efektejä. _noise_-oskillaattorilla voi luoda orgaanisen looppaavan satunnaisliikkeen, jossa voi olla niin paljon yksityiskohtia tai värinää kuin haluat.

Katso yllä olevat osiot:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Noise-kohtaiset asetukset:

* **noise type** - algoritmi, jolla kohina luodaan.
  * **SIMPLEX** - oletus, aaltoileva arvo, joka nousee ja laskee ja toistuu loopissa.
  * **RANDOM** - käyttää perinteisempää satunnaislukualgoritmia; täysin kohiseva ja kaoottinen.

{% hint style="info" %}
**Simplex noise** -algoritmin suunnitteli Ken Perlin vuonna 2001 parannuksena hänen vuonna 1983 kehittämäänsä "Perlin noise" -algoritmiin, joka syntyi hänen työskennellessään _Tron_-elokuvan parissa (josta hän sai Oscarin!).

Tämä niin kutsuttu "gradient"-kohina syntyi turhautumisesta aiempiin, "konemaisiin" tietokoneella luotuihin kuviin. CGI-maailmassa se sopii erityisen hyvin pilvien, vedenpintojen tai jopa realistisen maaston korkeuskarttojen renderöintiin.

Liberationissa se taas sopii näennäisesti arvaamattomaan liikkeeseen, joka on silti pehmeää ja orgaanista.
{% endhint %}

* **seed** - arvo, jota käytetään kohinan luomiseen. Jos et pidä nykyisen noise wave -aallon ulkoasusta, kokeile muuttaa tätä arvoa.

{% hint style="info" %}
Hauska nörttifakta! Jotta saan simplex noise -kohinan looppaamaan täydellisesti, kierrän ympyrää 2D-kohinatasolla. Ja seed-arvon muuttaminen siirtää tätä tasoa kolmannen ulottuvuuden läpi!
{% endhint %}

* **simplex detail** - muuttaa sitä, kuinka yksityiskohtainen tai värisevä kohina on. Jos haluat toistuvan kuvion olevan vähemmän ilmeinen, kasvata duration-arvoa ja lisää tätä arvoa.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Luo täysin mukautettuja aaltomuotoja. Tämä on erittäin hyödyllistä monimutkaisten animaatioiden luomiseen.

Katso yllä olevat osiot:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Tämän alla on luettelo sijainneista ja arvoista. Kesto jaetaan 64 askeleeseen, ja voit sijoittaa arvon mihin tahansa näistä pisteistä.

Jokaisella askeleella on seuraavat asetukset:

* **Step** - aika-askel keston sisällä. 0 on alussa ja 64 lopussa.
* **Level** - aallon taso kyseisessä aika-askeleessa. Taso on välillä 0–1.
* **Animation type** - pudotusvalikosta voit valita, miten tähän tasoon siirrytään edellisestä askeleesta.
  * **None** - ei siirtymää, vaan hyppää suoraan tähän tasoon annetulla ajanhetkellä.
  * **Linear** - täysin lineaarinen liike edelliseltä tasolta tähän tasoon.
  * **Ease in / Ease out / Ease in/out** - käyttää easingia edelliseltä tasolta tähän tasoon siirryttäessä. Katso animaatiotyyppien kuvaus yllä kohdasta _ease function_.

***
