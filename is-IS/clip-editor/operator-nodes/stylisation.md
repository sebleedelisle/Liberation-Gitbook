---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stylisation-hnútar

## &#x20;Randomise

Býr til dreifð afrit af innkomandi einindum með samhangandi suðsviði. Með öðrum orðum afritar hnúturinn form og punkta og færir þau til á stýrðan, „suðkenndan“ hátt. Í stað þess að allt sitji snyrtilega á einum stað færðu mörg afbrigði sem færast og dreifast, eins og agnir sem hreyfast í flæði.

* **count** – fjöldi afrita fyrir hvert innkomandi einindi (1–20). Með 1 færðu eina örlítið hliðraða útgáfu af hverju einindi. Hærri gildi búa til mörg dreifð afrit.
* **noise offset** – fer í gegnum suðsviðið (0–100%). Það lykkjast hnökralaust, þannig að ef þú hreyfir þetta með Oscillator Node færðu mjúka, samfellda hreyfingu á öllum afritum saman.
* **noise jitter** – stýrir áferðarkvarða suðsins. Lægri gildi gefa breiða og mjúka breytileika. Hærri gildi gefa þéttari og óreglulegri staðsetningu. Þetta breytir mynstrinu, ekki styrknum.
* **change between points** – stýrir hversu ólíkt hvert afrit er því fyrra. Lág gildi halda afritum þétt saman og svipuðum. Há gildi dreifa þeim meira með meiri breytileika.
* **face direction** – snýr hverju afriti þannig að það vísi í hreyfistefnuna í suðsviðinu, sem býr til örvar/agnir sem raða sér eftir flæðinu.
* **amount** – heildarstyrkur áhrifanna (0–100%). Kvarðar bæði hliðrunina og snúninginn frá Face direction.

{% hint style="info" %}
Randomise-hnúturinn er kjarninn í Randomise-áhrifunum!
{% endhint %}

## &#x20;Trails

Býr til bergmál af efninu þínu og skilur eftir dofnandi eða sköluð afrit á eftir upprunalega efninu þegar það hreyfist.

* **change render profile for trail** – ef kveikt er á þessu nota öll trail-afrit valið **render profile**. _Sjá_ [render-profile.md](../fundamentals/render-profile.md).
* **render profile** – sniðið sem er notað fyrir trail-afrit þegar rofinn hér fyrir ofan er á. Þetta er oft notað þegar aðalefnið er stillt á **DETAIL** en bergmálin eru teiknuð sem **FAST**. Þannig færðu skýr smáatriði í aðalformunum en trails eru teiknuð á skilvirkari hátt.
* **delay** – stillir bilið á milli trail-afrita í tónfræðilegum tíma, mælt í **1/64-nótu skrefum**.\
  Til viðmiðunar:
  * 16 = 1/16 úr takti (sextándapartsnóta)
  * 32 = 1/8 úr takti (áttundapartsnóta)
  * 64 = 1/4 úr takti (fjórðapartsnóta)
  * 128 = 1/2 úr takti (hálfnóta)
  * 256 = 1 taktur
* **trail size** – hversu mörg trail-afrit eru teiknuð á eftir lifandi efninu.
* **freeze trails** – breytir mjúkum flæðandi trails í röð af frystum skyndimyndum. Gagnlegt til að búa til staccato, taktsamstillt trail-áhrif.
* **brightness start / brightness end** – beitir birtu yfir trail frá nýjasta afritinu (**start**) til elsta afritsins (**end**). Yfirleitt er **brightness start** stillt á 100% og **brightness end** á 0% svo bergmálin dofni út.
* **scale start / scale end** – beitir skölun yfir trail frá nýjasta afritinu (start) til elsta afritsins (end). Fyrir trails sem minnka niður í ekkert skaltu stilla **scale start** á 100% og **scale end** á 0%.

## &#x20;Shimmer

Bætir tindrandi birtubreytingu við efnið þitt, allt frá mildum glampa til öflugs strobe-bliks.

* **speed** – hversu hratt shimmer breytist með tímanum. Hærri gildi blikka hraðar; 0 setur áhrifin í bið.
* **separation** – hversu ólíkir nálægir punktar/einindi eru hver öðrum.
  * 0: allt tindrar saman.
  * \>0: nálægir punktar fá smám saman ólíka fasa, þannig að shimmer breytist yfir formið.
  * <0: sama og hér fyrir ofan, en fasaframvindan fer í hina áttina.
* **threshold** – í stað þess að dofna mjúklega blikka punktar nú alveg kveikt eða slökkt eftir birtu sinni. Bjartari einindi kvikna oftar, en athugaðu að einindi með 100% birtu eru alltaf kveikt og einindi með 0% birtu eru alltaf slökkt. Gagnlegt fyrir skýran glitra- eða stjörnuljósaáhrif.

{% hint style="info" %}
Að kveikja á **threshold** er einn af þessum frábæru földu eiginleikum sem geta virkilega lífgað upp á agnirnar þínar eða efnið. Í stað þess að dofna eru punktar kveiktir og slökktir hratt út frá birtu þeirra. Þar sem færri punktar eru teiknaðir á hverjum tíma verður úttakið bjartara og hreyfingin mýkri.

En hafðu í huga að ef efnið þitt er þegar í 100% birtu gerist ekkert!
{% endhint %}

* **use whole shape** – beitir einu shimmer-gildi jafnt á allt formið. Þegar slökkt er á þessu skiptir hnúturinn formum niður svo mismunandi hlutar geti tindrað sjálfstætt og myndað flekkótt útlit.

## &#x20;Particles

Þetta er tilraunaáhrif sem býr til og hreyfir agnir út frá efninu þínu. Öll punktamiðuð einindi sem fara inn eru meðhöndluð sem emitter-staðsetningar. Þar sem ferlar agnanna eru reiknaðir fyrirfram gætirðu þurft að endurhlaða/endur­reikna agnirnar ef inntaksefnið breytist (breyttu bara einhverri stillingu).

**General**

* **keep original** – ef kveikt er á þessu er upprunalega efninu haldið og agnir eru lagðar ofan á. Gagnlegt þegar þú vilt að emitter-punktarnir haldist sýnilegir.
* **number of particles** – hversu margar agnir eru búnar til í hverri losun. Hærri gildi gera áhrifin þéttari, lægri gildi halda þeim einfaldari.
* **emission period** – lengd lykkjunnar (í töktum) sem agnir eru losaðar yfir. Við 100% dreifast þær jafnt yfir lykkjuna; minni gildi safna þeim saman í gusur.
* **loop length** – hversu lengi agnalykkjan varir, mælt í tónfræðilegum töktum.
* **loop count** – hversu oft lykkjan endurtekur sig áður en hún endurstillist. Ef þetta er stillt á 1 fylgja agnirnar alltaf nákvæmlega sömu hermun í hvert skipti, sem gerir hana fullkomlega endurtakanlega. Hærri gildi bæta við meiri breytileika áður en hringrásin endurstillist.
* **delay** – hliðrar upphafstíma losunar um tiltekinn fjölda 1/64-nóta fyrir tímasetningaráhrif.

**Motion**

* **speed** – hversu hratt agnirnar hreyfast frá emitternum.
* **speed variation** – bætir við tilviljun svo agnir hreyfist ekki allar á sama hraða. Býr til náttúrulegri dreifingu.
* **direction** – stillir grunnstefnuna sem agnir eru skotnar í, skilgreinda með **x, y, z angles**. Þessi horn snúa skotvektornum í 3D-rými, þannig að þú getur beint ögnunum beint upp, til hliðar eða á hvaða ská sem er. Sameinaðu þetta með **spread** fyrir breiðari keilur eða óreiðukenndari gusur.

{% hint style="info" %}
**Euler angles**\
Liberation notar **Euler angles** til að lýsa stefnu í 3D-rými. Þetta eru einfaldlega snúningar um þrjá meginása:

* **X** – halla fram/aftur (eins og að kinka kolli)
* **Y** – snúa til vinstri/hægri (eins og að hrista höfuðið til að segja „nei“)
* **Z** – velta réttsælis/rangsælis (eins og að halla höfðinu til hliðar)

Með því að stilla þessi þrjú gildi geturðu beint ögnum í hvaða átt sem er.
{% endhint %}

* **direction variation** – bætir við tilviljanakenndri dreifingu í kringum þá stefnu. Gagnlegt til að búa til keilur, úða eða sprengingar.
* **drag** – hægir á ögnum með tímanum. Hærri gildi láta þær virka þyngri og tregari.
* **gravity** – togar agnir niður (jákvætt) eða ýtir þeim upp (neikvætt).
* **gravity variation** – bætir við breytileika í þyngdarafli fyrir hverja ögn, sem gerir hreyfinguna óreiðukenndari.

**Life**

* **life duration** – hversu lengi agnir eru til (mælt í 1/64-nótu einingum). Með styttri gildum hverfa agnir hratt, en með lengri gildum haldast þær sýnilegar í lengri tíma.
* **life variation** – bætir tilviljun við líftíma agna svo þær hverfi ekki allar í einu.
* **start delay / start delay variation** – seinkar því hvenær hver ögn verður sýnileg (í 1/64-note-skrefum). Ögnin er þegar búin að birtast og er á hreyfingu á þessum tíma, en birtunni er haldið í 0, þannig að hún helst ósýnileg þar til seinkunin er liðin. Þetta er gagnlegt ef þú vilt að seinkaðir flugelda-„glampar“ birtist.

**Colour & brightness**

* **hue start** – upphafslitur agna.
* **hue variation** – bætir við tilviljun svo agnir byrji ekki allar með sama lit.
* **hue change** – hliðrar litblæ yfir líftíma agnarinnar og býr til litbreytandi trails.
* **brightness start / brightness end** – beitir birtu yfir líftíma agnarinnar. Yfirleitt er brightness start stillt hátt og brightness end lágt svo þær dofni eðlilega út.
* **brightness variation** – slembir upphafsbirtu fyrir líflegra útlit.
* **saturation start / saturation end** – stillir hversu skær liturinn er í upphafi og lokum.
* **saturation variation** – slembir mettun til að fá breytileika milli agna.

**Simulation**

* **time adjustment** – hraðar eða hægir á allri agnahermuninni. Gagnlegt til að samstilla við mismunandi tempó eða ýkja hreyfingu.
