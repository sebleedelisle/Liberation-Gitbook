---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Inngangur

Liberation inniheldur sveigjanlegt og öflugt DMX-kerfi sem gerir þér kleift að búa til ljósáhrif og stjórna DMX-samhæfum leysum yfir Art-Net. Kerfið er hannað þannig að auðvelt sé að halda ljósunum samstilltum við lasersýninguna — án þess að þurfa sérstakt ljósaborð.

{% hint style="info" %}
**Hvað er Art-Net og hvernig tengist það DMX?**

**DMX** er kerfi sem hefur verið notað í mörg ár til að stjórna ljósum, leysum, reykvélum og öðrum sviðsáhrifum. Það sendir stýrimerki um sérstaka kapla, yfirleitt með XLR-tengjum, og hvert tæki hlustar á tiltekið sett af rásum til að vita hvað það á að gera.

**Art-Net** er nýrri leið til að senda sömu DMX-gögn yfir venjulegt tölvunet. Í stað þess að nota sérstaka kapla sendir það allt yfir Ethernet, rétt eins og internet- eða staðarnetsumferð.

Í Liberation er allt DMX-úttak sent með Art-Net. Þú getur notað það til að stjórna Art-Net-samhæfum tækjum beint, eða tengt **Art-Net node** — lítinn kassa sem breytir Art-Net aftur yfir í hefðbundið DMX. Þannig geturðu enn stjórnað hefðbundnum DMX-ljósum og áhrifum, jafnvel þótt þau styðji ekki Art-Net sjálf.
{% endhint %}

Þú getur líka notað kerfið til að stjórna alls kyns sviðsbúnaði, til dæmis reykvélum, móðuvélum, CO₂-sprautum, köldum neistavélum og fleiru. Ef búnaðurinn styður DMX geturðu sett hann upp sem DMX zone og ræst hann beint úr Liberation, samhliða laser-efninu þínu.

DMX-búnaði er bætt við sem **DMX zones**, sem birtast í listanum yfir zones ásamt laser beam zones og marksvæðum á Canvas. Hvert DMX zone notar **DMX preset**, sem segir Liberation hvernig eigi að varpa eiginleikum úr laser Clips — eins og staðsetningu, lit og birtu — yfir í DMX-rásargildi.

Þegar þú sendir Clip í DMX zone skoðar Liberation fyrsta elementið í Clip og breytir eiginleikum þess samkvæmt forstillingunni. Þetta gerir einfalt að stýra ljósum og DMX-áhrifum beint úr sömu Clips og þú notar nú þegar fyrir leysana.

#### Liberation á Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Fyrsta raunverulega prófunin á DMX-kerfinu í Liberation fór fram á Glastonbury 2023, þar sem Reach Lasers setti upp alls 90 beam sources sem hluta af Arcadia „spider“-sviðinu.

18 leysum var stjórnað með innbyggðum Ether Dreams og 12 til viðbótar, hver með 6 hausa beam bars, var stjórnað með Art-Net og DMX.
