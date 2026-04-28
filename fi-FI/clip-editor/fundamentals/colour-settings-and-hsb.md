---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Väriasetukset ja HSB

Liberationissa väri määritellään HSB:nä, ei RGB:nä. Tämä voi tuntua aluksi vieraalta, mutta kun siihen tottuu, se on mielestäni paljon intuitiivisempi järjestelmä.

{% hint style="info" %}
Jos käytät mieluummin RGB:tä, voit napsauttaa värineliötä missä tahansa väriasetuksessa. Tämä avaa värinmuokkauspaneelin, jossa on vaihtoehdot RGB:lle ja HSB:lle.
{% endhint %}

### HSB - Hue, Saturation ja Brightness

#### Hue

Värin Hue-arvo on välillä 0–255. 0 on punainen, ja kun kasvatat arvoa, käyt läpi kaikki sateenkaaren sävyt: oranssin, keltaisen, vihreän, syaanin, sinisen, violetin, magentan ja lopulta takaisin punaiseen arvossa 255.

Koska tämä muodostaa silmukan, voit käyttää kolmioaaltoa käydäksesi läpi kaikki värit.

#### Saturation

Tämä asetus säätää värin kylläisyyttä eli voimakkuutta. Toisin sanoen sitä, kuinka _värikäs_ väri on. Arvoalue on 0–255. Aseta Saturation arvoon 0 harmaasävyjä varten ja arvoon 255 täysiä sateenkaarivärejä varten. Keskialueen arvot tuottavat pastellisia, haalistuneita värejä.

{% hint style="info" %}
Pahoittelut yhdysvaltalaisille ystävilleni ylimääräisestä vokaalista sanassa colour. Liberation tehdään Englannissa, joten brittiläinen englanti on oletus. Tulevaisuudessa toivon voivani tarjota käännökset ranskaksi, espanjaksi, saksaksi, italiaksi, yksinkertaistetuksi kiinaksi ja kyllä, jopa yhdysvaltainenglanniksi. :innocent:
{% endhint %}

#### Brightness

Tämä on luultavasti helpoin ymmärtää: 0 on täysin musta ja 255 on täysi kirkkaus.

### Käyttöesimerkkejä

#### Rainbow cycle :

Aseta _Brightness_ ja _Saturation_ arvoon 255. Kytke _Sawtooth_-oskillaattori _Hue_-liitäntään ja säädä sen alueeksi 0–255.

#### Pulsing brightness :

Kytke _Sawtooth_-oskillaattori _Brightness_-liitäntään ja säädä sen alueeksi 255–0. Voit lisäksi säätää clamp min- ja max-arvoja muuttaaksesi muutoksen kestoa. Sen jälkeen voit hienosäätää animaatiota easing-toiminnoilla.

#### Hard flash / strobe :

Valitse väri käyttämällä _Hue_- ja _Saturation_-asetuksia tai napsauttamalla värivalitsinta. Kytke _Square Wave_-oskillaattori _Brightness_-liitäntään ja säädä sen alueeksi 255–0.

#### Cycle across custom range of hues :

Aseta _Brightness_ ja _Saturation_ arvoon 255. Kytke _Triangle Wave_-oskillaattori _Hue_-liitäntään ja säädä sen alue:

* sinisestä syaaniin käytä aluetta 70–128
* punaisesta keltaiseen käytä aluetta 0–40
* punaisesta magentaan käytä aluetta 255–220
