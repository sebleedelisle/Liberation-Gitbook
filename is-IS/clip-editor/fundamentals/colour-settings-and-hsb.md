---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Litastillingar og HSB

Litir í Liberation eru skilgreindir sem HSB frekar en RGB. Þetta kann að vera óvant í fyrstu, en þegar þú venst því er þetta mun innsæislegra kerfi.

{% hint style="info" %}
Ef þú vilt frekar nota RGB geturðu smellt á litareitinn í hvaða litastillingu sem er. Þá opnast litavinnsluspjald þar sem þú færð valkosti fyrir RGB og HSB.
{% endhint %}

### HSB - Hue, Saturation og Brightness

#### Hue

Litblærinn nær frá 0 til 255. 0 er rautt og eftir því sem þú hækkar gildið ferðu í gegnum alla litina í regnboganum: appelsínugult, gult, grænt, blágrænt, blátt, fjólublátt, bleikfjólublátt og svo aftur í rautt við 255.

Þar sem þetta er lykkja geturðu notað triangle wave til að fara í hring í gegnum alla litina.

#### Saturation

Þessi stilling stjórnar litmettuninni eða hversu skær liturinn er. Með öðrum orðum hversu _litríkur_ hann er, á bilinu 0 til 255. Stilltu Saturation á 0 fyrir gráa tóna og 255 fyrir fulla regnbogaliti. Einhvers staðar í miðjunni færðu pastelkennda, útþvegna liti.

{% hint style="info" %}
Afsakið við bandaríska vini mína fyrir aukasérhljóðann í orðinu colour. Liberation er þróað í Englandi, þannig að bresk enska er sjálfgefið mál. Í framtíðinni vonast ég til að geta boðið upp á þýðingar á frönsku, spænsku, þýsku, ítölsku, einfaldaðri kínversku og já, jafnvel bandarískri ensku. :innocent:
{% endhint %}

#### Brightness

Sennilega einfaldasta stillingin að skilja: 0 er alveg svart og 255 er full birta.

### Dæmi um notkun

#### Regnbogahringrás :

Stilltu _Brightness_ og _Saturation_ á 255. Tengdu _Sawtooth_ oscillator við _Hue_ tengið og stilltu sviðið hans frá 0 til 255.

#### Púlsandi birta :

Tengdu _Sawtooth_ oscillator við _Brightness_ tengið og stilltu sviðið hans frá 255 til 0. Þú getur svo stillt clamp min og max til að stjórna lengd breytingarinnar. Notaðu síðan easing functions til að fínstilla hreyfinguna enn frekar.

#### Skarpur blikkur / strobe :

Veldu lit með _Hue_ og _Saturation_ eða með því að smella á litaveljarann. Tengdu _Square Wave_ oscillator við _Brightness_ tengið og stilltu sviðið hans frá 255 til 0.

#### Hringrás yfir sérvalið svið litblæja :

Stilltu _Brightness_ og _Saturation_ á 255. Tengdu _Triangle Wave_ oscillator við _Hue_ tengið og stilltu sviðið :

* fyrir blátt yfir í blágrænt skaltu nota sviðið 70 til 128
* fyrir rautt yfir í gult skaltu nota sviðið 0 til 40
* fyrir rautt yfir í bleikfjólublátt skaltu nota sviðið 255 til 220
