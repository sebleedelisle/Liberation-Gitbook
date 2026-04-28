---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Kleurinstellingen en HSB

Kleur wordt in Liberation gedefinieerd als HSB in plaats van RGB. Dat is misschien even wennen, maar zodra je eraan gewend bent, vind ik het een veel intuïtiever systeem.

{% hint style="info" %}
Als je liever RGB gebruikt, kun je in elke kleurinstelling op het kleurvak klikken. Hiermee open je het kleur-editorpaneel, waar je opties hebt voor RGB en HSB.
{% endhint %}

### HSB - Hue, Saturation en Brightness

#### Hue

De kleurtoon loopt van 0 tot 255. 0 is rood, en terwijl je de waarde verhoogt, ga je langs elke kleur van de regenboog: oranje, geel, groen, cyaan, blauw, paars, magenta en daarna weer terug naar rood bij 255.

Omdat dit een lus is, kun je een triangle wave gebruiken om door alle kleuren te lopen.

#### Saturation

Deze instelling past de verzadiging of levendigheid van je kleur aan. Met andere woorden: hoe _kleurrijk_ de kleur is. De waarde loopt van 0 tot 255. Zet de saturation op 0 voor grijstinten en op 255 voor volledige regenboogkleuren. Ergens in het midden krijg je pastelkleurige, wat fletsere kleuren.

{% hint style="info" %}
Excuses aan mijn Amerikaanse vrienden voor de extra klinker in het woord colour. Liberation wordt in Engeland gemaakt, dus Brits Engels is de standaard. In de toekomst hoop ik vertalingen aan te bieden naar Frans, Spaans, Duits, Italiaans, Vereenvoudigd Chinees en ja, zelfs Amerikaans Engels. :innocent:
{% endhint %}

#### Brightness

Waarschijnlijk het eenvoudigst te begrijpen: 0 is volledig zwart, 255 is volledige helderheid.

### Voorbeeldgebruik

#### Regenboogcyclus :

Zet _Brightness_ en _Saturation_ op 255. Verbind een _Sawtooth_-oscillator met je _Hue_-socket en stel het bereik in van 0 tot 255.

#### Pulserende helderheid :

Verbind een _Sawtooth_-oscillator met je _Brightness_-socket en stel het bereik in van 255 tot 0. Je kunt de clamp min en max verder aanpassen om de duur van de verandering te bepalen. Gebruik daarna de easing functions om de animatie verder te verfijnen.

#### Harde flits / strobe :

Selecteer een kleur met _Hue_ en _Saturation_ of door op de colour picker te klikken. Verbind een _Square Wave_-oscillator met je _Brightness_-socket en stel het bereik in van 255 tot 0.

#### Door een aangepast bereik van kleurtonen lopen :

Zet _Brightness_ en _Saturation_ op 255. Verbind een _Triangle Wave_-oscillator met je _Hue_-socket en stel het bereik in :

* gebruik voor blauw naar cyaan een bereik van 70 tot 128
* gebruik voor rood naar geel een bereik van 0 tot 40
* gebruik voor rood naar magenta een bereik van 255 tot 220
