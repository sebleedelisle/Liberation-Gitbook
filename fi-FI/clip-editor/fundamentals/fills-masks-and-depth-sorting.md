---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Täytöt, maskit ja syvyyslajittelu

### Viivat, täytöt ja maskit

Joissakin Creator-solmuissa on _Fill state_ -asetus. Voit piirtää ne viivana eli ääriviivana, maskina eli sen alla olevan sisällön peittävänä muotona, tai molempina.

Kun renderöit muodon maskina, se toimii kuin se olisi täytetty mustalla, ja kaikki sen alla oleva peittyy.

{% hint style="info" %}
Viivan eli _stroken_ piirtäminen laserilla on melko yksinkertaista: laser skannataan viivan alusta sen loppuun. Siinä on viivasi!

Täytetyt muodot ovat kuitenkin vaikeampia. Jos haluat täyttää muodon värillä, voisit tehdä sen käsin ristiviivoituksella piirtämällä viivoja ja täyttämällä välin, mutta Liberation ei osaa tehdä sitä automaattisesti (vielä). Ja vaikka osaisimmekin, näkisit silti muut viivat sen alta läpi.

Sen sijaan voimme täyttää muodot _mustalla_. Taustalla Liberation tekee kaikki tarvittavat laskelmat poistaakseen sisällön, joka jää mustalla täytetyn muodon alle. Ja usko pois, se on tarkkaa työtä!

Se toimii kuitenkin erittäin hyvin ja luo vaikutelman mustalla täytetystä muodosta.
{% endhint %}

### Syvyyslajittelu

Koska jotkin muodot voivat _peittää_ muita muotoja, Liberationin on lajiteltava ne syvyyden mukaan. Oletuksena elementit lajitellaan syvyyden mukaan niiden z-sijainnin perusteella. Jos ne ovat samassa z-sijainnissa, ne lajitellaan tasosijainnin mukaan. Tätä voi muuttaa kunkin Creatorin sisällä olevilla _MOVE TO FRONT_ ja _MOVE TO BACK_ -painikkeilla.
