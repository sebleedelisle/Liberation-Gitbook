---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Postavke boje i HSB

Boja se u Liberation definira kao HSB, a ne kao RGB. To vam možda neće biti poznato, ali smatram da je to mnogo intuitivniji sustav kad se na njega naviknete.

{% hint style="info" %}
Ako radije koristite RGB, možete kliknuti kvadratić boje u bilo kojoj postavci boje. Time se otvara panel uređivača boje, koji vam daje opcije za RGB i HSB.
{% endhint %}

### HSB – Hue, Saturation i Brightness

#### Hue

Hue boje kreće se od 0 do 255. 0 je crvena, a kako povećavate vrijednost, prolazite kroz sve nijanse duge: narančastu, žutu, zelenu, cijan, plavu, ljubičastu, magentu, a zatim se na 255 vraćate na crvenu.

Budući da je to petlja, možete koristiti trokutasti val za kruženje kroz sve boje.

#### Saturation

Ova postavka podešava zasićenost ili živost boje. Drugim riječima, koliko je boja _šarena_, a raspon je od 0 do 255. Postavite Saturation na 0 za sive tonove, a na 255 za pune dugine boje. Vrijednosti negdje u sredini dat će vam pastelne, isprane boje.

{% hint style="info" %}
Isprike mojim prijateljima iz SAD-a zbog dodatnog samoglasnika u riječi colour. Liberation se izrađuje u Engleskoj, pa je britanski engleski zadani jezik. U budućnosti se nadam ponuditi prijevode na francuski, španjolski, njemački, talijanski, pojednostavljeni kineski i, da, čak i američki engleski. :innocent:
{% endhint %}

#### Brightness

Vjerojatno najjednostavnije za razumjeti: 0 je potpuno crno, 255 je puna svjetlina.

### Primjer upotrebe

#### Ciklus duginih boja:

Postavite _Brightness_ i _Saturation_ na 255. Spojite oscilator _Sawtooth_ na priključak _Hue_ i podesite mu raspon od 0 do 255.

#### Pulsirajuća svjetlina:

Spojite oscilator _Sawtooth_ na priključak _Brightness_ i podesite mu raspon od 255 do 0. Zatim možete dodatno podesiti clamp min i max kako biste kontrolirali trajanje promjene. Nakon toga upotrijebite easing funkcije za dodatno fino podešavanje animacije.

#### Oštar bljesak / strobe:

Odaberite boju pomoću _Hue_ i _Saturation_ ili klikom na birač boje. Spojite oscilator _Square Wave_ na priključak _Brightness_ i podesite mu raspon od 255 do 0.

#### Ciklus kroz prilagođeni raspon nijansi:

Postavite _Brightness_ i _Saturation_ na 255. Spojite oscilator _Triangle Wave_ na priključak _Hue_ i podesite mu raspon:

* za plavu do cijan koristite raspon od 70 do 128
* za crvenu do žutu koristite raspon od 0 do 40
* za crvenu do magente koristite raspon od 255 do 220
