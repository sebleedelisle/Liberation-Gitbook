---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Nodes fyrir stílfærslu

## &#x20;Randomise

Býr til dreifð afrit af innkomandi einingum með samfelldu noise-sviði. Með öðrum orðum afritar það formin þín og punkta og færir þau til á stýrðan, „noisy“ hátt. Í stað þess að allt liggi snyrtilega á einum stað færðu margar útgáfur sem hreyfast og dreifast, líkt og agnir sem flæða áfram.

* **count** – fjöldi afrita fyrir hverja innkomandi einingu (1–20). Með 1 færðu eina hristta útgáfu af hverri einingu. Hærri gildi búa til mörg dreifð afrit.
* **noise offset** – fer í gegnum noise-sviðið (0–100%). Það lykkjast óaðfinnanlega, þannig að ef þú hreyfir þetta með Oscillator Node færðu mjúka, samfellda hreyfingu á öllum afritunum saman.
* **noise jitter** – stjórnar áferðarkvarða noise. Lægri gildi gefa breiða og mjúka breytileika. Hærri gildi gefa þéttari og óreglulegri staðsetningu. Þetta breytir mynstrinu, ekki styrknum.
* **change between points** – stjórnar því hversu ólíkt hvert afrit er frá því fyrra. Lág gildi halda afritum saman í þyrpingu og svipuðum. Há gildi dreifa þeim meira og auka breytileika.
* **face direction** – snýr hverju afriti þannig að það snúi í ferðastefnu innan noise-sviðsins, sem skapar örvar/agnir sem fylgja flæðinu.
* **amount** – heildarstyrkur áhrifanna (0–100%). Skalar bæði færslu og snúning frá **face direction**.

{% hint style="info" %}
Randomise node er kjarninn í Randomise-áhrifunum!
{% endhint %}

## &#x20;Trails

Býr til bergmál af efninu þínu og skilur eftir dofnandi eða stækkandi/minnkandi afrit fyrir aftan upprunalega efnið þegar það hreyfist.

* **change render profile for trail** – ef þetta er kveikt nota öll trail-afrit valið **render profile**. _Sjá_ [render-profile.md](../fundamentals/render-profile.md).
* **render profile** – sniðið sem er notað fyrir trail-afrit þegar rofinn hér fyrir ofan er kveiktur. Þetta er oft notað þegar aðalefnið er stillt á **DETAIL** en bergmálin eru teiknuð sem **FAST**. Þannig færðu skýr smáatriði í aðalformunum en trails eru teiknuð á skilvirkari hátt.
* **delay** – stillir bilið milli trail-afrita í tónlistarlegum tíma, mælt í **1/64-nótu skrefum**.\
  Til viðmiðunar:
  * 16 = 1/16 úr takti (sextándapartsnóta)
  * 32 = 1/8 úr takti (áttundapartsnóta)
  * 64 = 1/4 úr takti (fjórðapartsnóta)
  * 128 = 1/2 úr takti (hálfnóta)
  * 256 = 1 taktur
* **trail size** – hversu mörg trail-afrit eru teiknuð á eftir lifandi efninu.
* **freeze trails** – breytir mjúklega flæðandi trails í röð frosinna skyndimynda. Gagnlegt til að búa til stutt, taktsamstillt trail-áhrif.
* **brightness start / brightness end** – beitir birtu yfir trail frá nýjasta afritinu (**start**) til elsta afritsins (**end**). Yfirleitt er **brightness start** stillt á 100% og **brightness end** á 0%, þannig að bergmálin dofni út.
* **scale start / scale end** – beitir skölun yfir trail frá nýjasta afritinu (start) til elsta afritsins (end). Fyrir trails sem minnka niður í ekki neitt skaltu stilla **scale start** á 100% og **scale end** á 0%.

## &#x20;Shimmer

Bætir tindrandi birtubreytingu við efnið þitt, allt frá mildum glampa til kröftugs strobe-áhrifs.

* **speed** – hversu hratt shimmer breytist með tímanum. Hærri gildi blikka hraðar; 0 setur áhrifin í bið.
* **separation** – hversu ólíkir nálægir punktar/einingar eru hver frá annarri.
  * 0: allt shimmer hreyfist saman.
  * \>0: nálægir punktar fá smám saman ólíka fasa, þannig að shimmer breytist yfir formið.
  * <0: sama og hér fyrir ofan, en fasaframvindan fer í gagnstæða átt.
* **threshold** – í stað þess að dofna mjúklega blikka punktar nú annaðhvort alveg kveiktir eða slökktir eftir birtu. Bjartari einingar kvikna oftar, en athugaðu að einingar í 100% birtu eru alltaf kveiktar og einingar í 0% birtu eru alltaf slökktar. Gagnlegt fyrir skýran glitra- eða stjörnuljóma.

{% hint style="info" %}
Að kveikja á **threshold** er einn af þessum frábæru földu eiginleikum sem geta virkilega lífgað upp á agnir eða efni. Í stað þess að dofna eru punktar kveiktir og slökktir hratt út frá birtu þeirra. Þar sem færri punktar eru teiknaðir á hverju augnabliki verður úttakið bjartara og hreyfingin mýkri.

En hafðu í huga að ef efnið þitt er þegar í 100% birtu gerist ekkert!
{% endhint %}

* **use whole shape** – beitir einu shimmer-gildi jafnt á allt formið. Þegar slökkt er á þessu skiptir node formum niður þannig að ólíkir hlutar geti tindrað sjálfstætt og gefið flekkótt yfirbragð.

## &#x20;Particles

Þetta eru tilraunaáhrif sem búa til og hreyfa agnir út frá efninu þínu. Allar punktabyggðar einingar sem fara inn eru meðhöndlaðar sem staðsetningar fyrir emitters. Þar sem ferlar agna eru forreiknaðir gætirðu þurft að endurnýja/endurreikna til að uppfæra agnirnar ef inntaksefnið breytist (breyttu bara einhverri stillingu).

**Almennt**

* **keep original** – ef þetta er kveikt er upprunalega efninu haldið og ögnum bætt ofan á. Gagnlegt þegar þú vilt að emitter-punktar haldist sýnilegir.
* **number of particles** – hversu margar agnir eru búnar til í hverri losun. Hærri gildi gera áhrifin þéttari, lægri gildi gera þau einfaldari.
* **emission period** – lengd lykkjunnar (í töktum) sem agnir eru losaðar yfir. Við 100% dreifast þær jafnt yfir lykkjuna; minni gildi safna þeim saman í gusur.
* **loop length** – hversu lengi agnalykkjan varir, mælt í tónlistartöktum.
* **loop count** – hversu oft lykkjan endurtekur sig áður en hún endurstillist. Ef gildið er 1 fylgja agnirnar alltaf nákvæmlega sömu hermun í hvert skipti, þannig að niðurstaðan er fullkomlega endurtekanleg. Hærri gildi bæta við meiri breytileika áður en hringrásin endurstillist.
* **delay** – hliðrar upphafstíma losunar um fjölda 1/64-nótna fyrir tímasetningaráhrif.

**Hreyfing**

* **speed** – hversu hratt agnirnar hreyfast frá emitter.
* **speed variation** – bætir við slembni þannig að agnirnar hreyfast ekki allar á sama hraða. Þetta skapar náttúrulegri dreifingu.
* **direction** – stillir grunnstefnuna sem agnirnar skjótast í, skilgreinda með **x, y, z angles**. Þessi horn snúa skotvektornum í 3D-rými, þannig að þú getur beint ögnunum beint upp, til hliðar eða á hvaða ská sem er. Sameinaðu þetta við **spread** til að fá breiðari keilur eða óreiðukenndari gusur.

{% hint style="info" %}
**Euler angles**\
Liberation notar **Euler angles** til að lýsa stefnu í 3D-rými. Þetta eru einfaldlega snúningar um aðalásana þrjá:

* **X** – halla fram/aftur (eins og að kinka kolli)
* **Y** – snúa til vinstri/hægri (eins og að hrista höfuðið „nei“)
* **Z** – velta réttsælis/rangsælis (eins og að halla höfðinu til hliðar)

Með því að stilla þessi þrjú gildi geturðu beint ögnum í hvaða átt sem er.
{% endhint %}

* **direction variation** – bætir við slembinni dreifingu í kringum þessa stefnu. Gagnlegt til að búa til keilur, úða eða sprengingar.
* **drag** – hægir á ögnum með tímanum. Hærri gildi láta þær virka þyngri og tregari.
* **gravity** – togar agnir niður (jákvætt) eða ýtir þeim upp (neikvætt).
* **gravity variation** – bætir við breytileika í þyngdarafli fyrir hverja ögn og gerir hreyfinguna óreiðukenndari.

**Líftími**

* **life duration** – hversu lengi agnir eru til (mælt í 1/64-nótu einingum). Með styttri gildum hverfa agnir hratt, en með lengri gildum haldast þær sýnilegar í lengri tíma.
* **life variation** – bætir við slembni í líftíma agna þannig að þær hverfa ekki allar í einu.
* **start delay / start delay variation** – seinkar því hvenær hver ögn verður sýnileg (í 1/64-nótu skrefum). Ögnin er þegar búin að myndast og er á hreyfingu á þessum tíma, en birtan er haldið í 0, þannig að hún er ósýnileg þar til seinkunin er liðin. Þetta er gagnlegt ef þú vilt að seinkuð „sparkles“ í flugeldastíl birtist.

**Litur og birta**

* **hue start** – upphafslitur agna.
* **hue variation** – bætir við slembni þannig að agnir byrja ekki allar með sama lit.
* **hue change** – hliðrar hue yfir líftíma agnarinnar og skapar trails sem skipta um lit.
* **brightness start / brightness end** – beitir birtu yfir líftíma agnarinnar. Yfirleitt er brightness start stillt hátt og brightness end lágt svo agnirnar dofni náttúrulega út.
* **brightness variation** – slembir upphafsbirtu til að fá líflegra yfirbragð.
* **saturation start / saturation end** – stillir hversu skær liturinn er í upphafi og lokum.
* **saturation variation** – slembir litmettun til að fá breytileika milli agna.

**Hermun**

* **time adjustment** – hraðar á eða hægir á allri agnahermuninni. Gagnlegt til að samstilla við mismunandi tempó eða ýkja hreyfingu.
