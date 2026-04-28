---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Inngangur

Liberation inniheldur sveigjanlegt og öflugt DMX-kerfi sem gerir þér kleift að búa til ljósáhrif og stjórna DMX-samhæfum leysum yfir Art-Net. Það er hannað til að auðvelda þér að halda lýsingunni samstilltri við leysisýninguna — án þess að þurfa sérstakt ljósaborð.

{% hint style="info" %}
**Hvað er Art-Net og hvernig tengist það DMX?**

**DMX** er kerfi sem hefur verið notað í mörg ár til að stjórna ljósum, leysum, reykvélum og öðrum sviðsáhrifum. Það sendir stjórnsignöl um sérstaka kapla, yfirleitt með XLR-tengjum, og hvert tæki hlustar á ákveðið sett rása til að vita hvað það á að gera.

**Art-Net** er nýrri leið til að senda sömu DMX-gögn yfir venjulegt tölvunet. Í stað þess að nota sérstaka kapla sendir það allt yfir Ethernet, rétt eins og netumferð á interneti eða staðarneti.

Í Liberation er allt DMX-úttak sent með Art-Net. Þú getur notað það til að stjórna Art-Net-samhæfum tækjum beint, eða tengt **Art-Net node** — lítinn kassa sem breytir Art-Net aftur í hefðbundið DMX. Þetta þýðir að þú getur áfram stjórnað hefðbundnum DMX-ljósum og áhrifum, jafnvel þótt þau styðji ekki Art-Net sjálf.
{% endhint %}

Þú getur líka notað kerfið til að stjórna alls kyns sviðsbúnaði, svo sem reykvélum, haze-vélum, CO₂-þotum, cold spark-vélum og fleiru. Ef búnaðurinn styður DMX geturðu sett hann upp sem DMX-svæði og ræst hann beint úr Liberation, samhliða leysiefninu þínu.

DMX-tækjum er bætt við sem **DMX-svæðum**, sem birtast í svæðalistanum ásamt leysigeislasvæðum og Canvas-marksvæðum. Hvert DMX-svæði notar **DMX-forstillingu**, sem segir Liberation hvernig eigi að varpa eiginleikum úr leysiklippunum þínum — eins og staðsetningu, lit og birtustigi — yfir í DMX-rásargildi.

Þegar þú sendir klippu á DMX-svæði skoðar Liberation fyrsta stakið í klippunni og breytir eiginleikum þess út frá forstillingunni. Þetta gerir einfalt að stjórna ljósum og DMX-áhrifum beint úr sömu klippum og þú notar nú þegar fyrir leysa.

#### Liberation á Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Fyrsta alvöru prófunin á DMX-kerfi Liberation var á Glastonbury 2023, þar sem Reach Lasers setti upp samtals 90 geislagjafa sem hluta af Arcadia „spider“-sviðinu.

18 leysum var stjórnað með innbyggðum Ether Dreams og 12 geislabörum til viðbótar, hverjum með 6 geislahausum, var stjórnað með Art-Net og DMX.
