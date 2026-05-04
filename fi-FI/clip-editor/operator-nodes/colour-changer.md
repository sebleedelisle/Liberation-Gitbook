---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Muuttaa kaiken sisään tulevan sisällön värejä. Voit joko asettaa kiinteät HSB-arvot tai vaihtaa gradienttijärjestelmään ja poimia värit mukautetusta gradientista.

* **hue, saturation, brightness** - väriarvot, katso [Väriasetukset ja HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - sävyä ei muuteta
  * FIXED - elementtien sävy asetetaan hue-arvoon
  * SHIFT - elementtien sävyä siirretään annetulla arvolla, joten eriväriset elementit pysyvät edelleen erivärisinä, mutta niiden sävy siirtyy hue-arvon mukaisesti.
* **saturation mode** -
  * OFF - kylläisyyttä ei muuteta
  * FIXED - kylläisyys lukitaan määritettyyn arvoon.
* **brightness mode** -
  * OFF - kirkkautta ei muuteta
  * FIXED - elementtien kirkkaus asetetaan brightness-arvoon
  * MULTIPLY - elementtien kirkkaus yhdistetään brightness-arvoon, joten jos ne vilkkuvat, ne vilkkuvat edelleen, mutta enintään tässä määritettyyn kirkkauteen asti.
* **gradient mode** - vaihtaa kiinteistä HSB-liukusäätimistä gradienttieditoriin. node poimii gradientista yhden värin ja käyttää sitä yllä olevien sävy-, kylläisyys- ja kirkkaustilojen mukaisesti.
* **gradient position** - valitsee, mistä kohdasta gradienttia väri poimitaan. Animoi tätä arvosta 0 % arvoon 100 % Sawtooth Oscillator -toiminnolla, jotta gradientti kiertää ajan kuluessa.
* **blend** - kuinka voimakkaasti Colour change otetaan käyttöön. 0 % ei vaikuta lainkaan, 100 % käyttää vaikutusta kokonaan, ja 50 % on yhdistelmä nykyistä väriä ja uusia arvoja.

{% hint style="info" %}
Colour Change node poimii gradientista yhden värin koko syötteelle. Jos haluat gradientin kulkevan muodon yli sijainnin mukaan, käytä sen sijaan kohtaa [sijaintiin perustuvat muuttajat](position-based-changers.md "mention").
{% endhint %}

### Gradienttieditori

Kun **gradient mode** on käytössä, gradienttieditori näkyy pääsäätimien alapuolella.

* Lisää väripysähdys napsauttamalla gradienttipalkkia.
* Valitse pysähdys napsauttamalla sitä hiiren vasemmalla painikkeella ja siirrä sitä vetämällä sivusuunnassa.
* Poista valittu pysähdys vetämällä se alas pois palkista tai painamalla Delete/Backspace. Gradientissa säilyy aina vähintään kaksi pysähdystä.
* Muokkaa pysähdystä värivalitsimella napsauttamalla sitä hiiren oikealla painikkeella.
* Muokkaa valittua pysähdystä tarkasti asetuksilla **Position**, **Hue**, **Saturation** ja **Brightness**.
* **interpolation** valitsee, miten värit sekoittuvat pysähdysten välillä:
* **HSB** - sekoittaa sävyn, kylläisyyden ja kirkkauden. Tämä sopii parhaiten sulavaan sateenkaarimaiseen liikkeeseen väriympyrän ympäri.
* **RGB** - sekoittaa punaisen, vihreän ja sinisen arvot suoraan. Tämä tuntuu usein enemmän näytön tai valopöydän väriliu'ulta.
* **NONE** - hyppää pysähdyksestä seuraavaan ilman sekoitusta.
* **hue direction** on käytettävissä HSB-interpoloinnissa:
* **AUTO** - käyttää lyhintä reittiä sävyympyrän ympäri.
* **FORWARDS** - kulkee aina eteenpäin sävyarvojen läpi.
* **BACKWARDS** - kulkee aina taaksepäin sävyarvojen läpi.
