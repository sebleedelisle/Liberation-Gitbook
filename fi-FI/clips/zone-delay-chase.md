---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Olemme varmasti samaa mieltä siitä, että useampi laser tarkoittaa enemmän hauskuutta. Jos kaikki laserit tekevät täsmälleen samaa asiaa, luovia mahdollisuuksia jää kuitenkin käyttämättä.

Zone delay -järjestelmä on yksinkertainen mutta tehokas tapa tuoda vaihtelua eri zoneihin ja hyödyntää monilaser-kokoonpanoa paremmin. Sitä voi käyttää myös perinteisemmän chase-efektin tekemiseen.

#### Toimintaperiaate

_Zone delay_ lisää viiveen clipin ajoitukseen eri zoneissa ja luo eräänlaisen pyyhkäisyn zonejen yli.

Zone delay toimii erityisen hyvin, kun lisäät sen jo käynnissä olevaan clipiin. Säädä määrää ja patternia APC40:n vastaavalla ohjaimella. (Katso [APC40-viite](../reference/apc40-reference.md "mention")). Voit käyttää myös _Clip Settings_ -paneelia.

Zone delay -asetukset:

* **Zone delay** - säätää kuhunkin zoneen lisättävän viiveen määrää. Arvo mitataan 64-osanuotteina.
* **Pattern** - valitse zonejen järjestys
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern toimii zone-numeroiden perusteella ja olettaa, että zonet ovat järjestyksessä vasemmalta oikealle. Zone delay käsittelee Canvas-zonet ja DMX-zonet erillisinä ryhminä patterneja laskettaessa.
{% endhint %}

* **Delay mode**
  1. No delay - käytä tätä chase-tilassa
  2. Delay - oletustila, viivästää kunkin zonen ajoitusta
  3. Delay with re-trigger - palauttaa clipin alkuun joka kerta patternin edetessä. Tämä toimii hyvin _Chase mode_ -tilan kanssa.
* **Chase mode** - kun chase mode on käytössä, kukin zone kytketään päälle ja pois perinteisen chase-efektin tapaan. Säädä chase-efektin ulkoasua asetuksilla _Fade in, Hold,_ ja _Fade out_. Nämä asetukset määritetään suhteessa Zone delay -arvoon, joten arvo 1 vastaa samaa aikaa kuin _Zone delay_ -arvossa määritetty aika. Tätä on hieman vaikea selittää, joten suosittelen kokeilemaan itse.

{% hint style="info" %}
Zone delay vaikuttaa myös kaikkiin aktiivisiin efekteihin. Esimerkiksi vilkkuva efekti viivästyy zonejen välillä samalla tavalla kuin clipin oma animaatio.
{% endhint %}

Kun clipissä on käytössä jonkinlainen _Zone delay_, clipin oikeassa yläkulmassa näkyy kolmen pisteen kuvake. Pisteet animoidaan niin, että ne näyttävät kyseisen clipin _Zone delay_ -tyylin. Lisätietoja: [Mitä clip-painikkeiden pienet kuvakkeet tarkoittavat?](what-are-the-small-icons-on-the-clip-buttons.md "mention").

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Kolmen pisteen symboli ilmaisee, että clipissä on zone delay ja näyttää sen tilan</p></figcaption></figure>

{% hint style="info" %}
Zone delay on clip-kohtainen asetus, ei globaali asetus. Se on osa clipin luovaa suunnittelua.
{% endhint %}
