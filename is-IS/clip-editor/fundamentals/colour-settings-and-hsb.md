---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Litastillingar og HSB

Litur í Liberation er skilgreindur sem HSB frekar en RGB. Þetta kann að vera framandi í fyrstu, en þegar þú venst því er þetta að mínu mati mun innsæiskerfi.

{% hint style="info" %}
Ef þú kýst að nota RGB geturðu smellt á litareitinn í hvaða litastillingu sem er. Þá opnast litastjórnborðið, þar sem þú færð valkosti fyrir bæði RGB og HSB.
{% endhint %}

### HSB - Hue, Saturation og Brightness

#### Hue

Hue-gildið er á bilinu 0 til 255. 0 er rautt og þegar þú hækkar gildið ferðu í gegnum alla liti regnbogans: appelsínugult, gult, grænt, blágrænt, blátt, fjólublátt, magenta og svo aftur í rautt við 255.

Þar sem þetta er hringrás geturðu notað triangle wave til að fara í gegnum alla litina.

#### Saturation

Þessi stilling stjórnar mettun eða skærleika litarins. Með öðrum orðum hversu _litríkur_ hann er, á bilinu 0 til 255. Settu Saturation á 0 fyrir gráa tóna og 255 fyrir fulla regnbogaliti. Gildi einhvers staðar þar á milli gefur þér mjúka, útþvegna pastelliti.

{% hint style="info" %}
Afsakið, bandarísku vinir mínir, auka sérhljóðann í orðinu colour. Liberation er þróað í Englandi, þannig að bresk enska er sjálfgefið mál. Í framtíðinni vonast ég til að geta boðið þýðingar á frönsku, spænsku, þýsku, ítölsku, einfaldaðri kínversku og já, meira að segja bandarískri ensku. :innocent:
{% endhint %}

#### Brightness

Líklega auðveldast að skilja: 0 er alveg svart og 255 er full birta.

### Dæmi um notkun

#### Regnbogahringrás :

Settu _Brightness_ og _Saturation_ á 255. Tengdu _Sawtooth_ oscillator við _Hue_ tengið og stilltu sviðið frá 0 til 255.

#### Púlsandi birta :

Tengdu _Sawtooth_ oscillator við _Brightness_ tengið og stilltu sviðið frá 255 til 0. Þú getur svo stillt clamp min og max til að stjórna tímalengd breytingarinnar. Notaðu síðan easing functions til að fínstilla animation enn frekar.

#### Snöggt flash / strobe :

Veldu lit með _Hue_ og _Saturation_ eða með því að smella á colour picker. Tengdu _Square Wave_ oscillator við _Brightness_ tengið og stilltu sviðið frá 255 til 0.

#### Hringrás yfir sérsniðið Hue-svið :

Settu _Brightness_ og _Saturation_ á 255. Tengdu _Triangle Wave_ oscillator við _Hue_ tengið og stilltu sviðið :

* fyrir blátt yfir í blágrænt skaltu nota svið frá 70 til 128
* fyrir rautt yfir í gult skaltu nota svið frá 0 til 40
* fyrir rautt yfir í magenta skaltu nota svið frá 255 til 220
