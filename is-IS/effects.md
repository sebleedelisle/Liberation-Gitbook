---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Áhrif

Áhrifakerfið í Liberation er skemmtileg og fjölhæf leið til að breyta úttaki frá Clip í rauntíma. Áhrif eru fullkomlega sveigjanleg og má nota til að láta allt blikka, snúast, skipta um lit eða jafnvel fljúga tilviljanakennt um!

Allt sem þú getur gert í Clip Editor má nota sem áhrif. Í raun eru áhrif breytt með nákvæmlega sama node editor og Clips! Sjá [Breyta áhrifum](effects.md#editing-effects "mention"). Sköpunarmöguleikarnir eru nánast endalausir.

Sjálfgefnu áhrifahnapparnir 1–8 eru undir zone-hnöppunum og áhrif 9–24 eru litlu hnapparnir neðst.

#### Virkja áhrif

Ýttu á áhrifahnapp til að kveikja eða slökkva á áhrifinu, eða enn betra, notaðu APC40 sleðana 1–8 til að blanda áhrifum inn og út. Til að blanda áhrif inn án APC40 skaltu smella á hnappinn og draga upp og niður. Þú getur líka hægrismellt á áhrifahnappinn og stillt level-sleðann.

{% hint style="warning" %}
Þegar þú ýtir á áhrifahnappinn virkjar það áhrifin strax. Athugaðu þó að ef level er stillt á núll gerist ekkert! Smelltu og dragðu á hnappinn til að breyta level, eða hægrismelltu og notaðu _level_-sleðann, eða notaðu APC40 faders.
{% endhint %}

#### Áhrif og zone delay í Clip

Áhrif nota zone delay stillinguna fyrir hvert Clip sem er í gangi. Ef Clip er til dæmis með delay sem færist frá vinstri til hægri og þú bætir við blikkandi áhrifum, þá tefst blikkið líka frá vinstri til hægri.

{% hint style="info" %}
Það er mjög erfitt að lýsa því hvernig zone delay í Clip erfist yfir í áhrif, en það verður augljóst þegar þú prófar!

Ég myndi segja að þetta sé eitt skemmtilegasta og skapandi verkfærið sem er innbyggt í Liberation. Prófaðu og þú sérð hvað ég á við!
{% endhint %}

#### Færibreytur áhrifa

Bættu færibreytu við áhrifin með _Parameter node._ Parameter-kerfið er leið til að stilla margar stillingar inni í áhrifinu utan frá. Sjá [Parameter-stýring](clip-editor/oscillators/parameter-control.md "mention") fyrir nánari upplýsingar.

Notaðu snúningsstýringar 1–8 til að stilla _parameter_ fyrir hvert áhrif. Þú getur líka hægrismellt á áhrifahnappinn og stillt parameter-sleðann eða sleðana. Breyting á parameter gerir mismunandi hluti eftir því hvernig áhrifin eru sett upp. Sjá listann hér fyrir neðan yfir sjálfgefnu áhrifin og hvað færibreytur þeirra gera.

{% hint style="info" %}
Snúningsstýringar 1–8 eru efst á APC40 Mk2 og efst til hægri á Mk1. Sjá einnig: [APC40 tilvísun](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
Litlu tölurnar sem þú sérð á áhrifahnöppunum vísa til _level_ og _parameter_ fyrir áhrifin. _level_ er stjórnað með fader á APC40, eða með því að smella og draga á hnappinn. Parameter er stillt með snúningsstýringunum á APC40, eða með því að hægrismella og stilla með músinni.
{% endhint %}

#### Sjálfgefin áhrif

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Setur óreiðukennda hreyfingu á úttakið frá Clip. Færibreytan stillir magn/hraða óreiðunnar.
2. **Sine wave** :\
   Sveigir allt efnið eftir hreyfanlegri sínusbylgju. Færibreytan stillir bylgjulengdina.
3. **Rotation** :\
   Lætur allt snúast. Færibreytan stillir snúningshraðann.
4. **Horizontal flip** :\
   Kremur og teygir allt lárétt. Færibreytan stillir hraðann.
5. **Scale** :\
   Skalar allt endurtekið frá fullri stærð niður í núll. Færibreytan stillir hraðann.
6. **Hue** :\
Breytir litblæ alls, en breytir ekki litmettuninni (þ.e. allt sem er hvítt helst hvítt). Færibreytan stillir litblæinn.
7. **Saturation and hue** :\
Breytir litblæ alls og mettar litinn líka að fullu (þ.e. allt sem er hvítt breytist í litinn). Færibreytan stillir litblæinn.
8. **Flash** :\
   Lætur birtu alls blikka endurtekið frá fullri birtu niður í núll. Færibreytan stillir blikkhraðann.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Í neðstu röðinni eru 16 litáhrif til viðbótar sem nota fyrirfram stillt gildi fyrir litblæ og litmettun.

Athugaðu að þetta eru sjálfgefnu áhrifin, en þú getur breytt þeim þannig að þau geri nánast hvað sem þú vilt!

### Apply to groups

Þú getur valið hvaða hópar verða fyrir áhrifunum. Hægrismelltu og kveiktu eða slökktu á gátreitunum fyrir hópa sem eru merktir _Apply to groups._

Ég nota þessa uppsetningu aðallega þegar ég vinn með Canvas grafík og leysigeisla sitt í hvoru lagi. Ég set öll Canvas Clips í hóp 5 og útiloka svo þennan hóp frá áhrifum sem ég vil ekki að hafi áhrif á þessi grafísku Clips.

Þú gætir líka notað þetta til að beita tveimur mismunandi litabreytingum á tvo hópa leysa í einu, í beinni. Búðu til tvö litabreytingaráhrif og veldu á hvaða Clip hópa hvort þeirra á að virka.

### MX group

MX er stytting á _Mutually Exclusive_. Þetta er leið til að hópa áhrif saman þannig að aðeins eitt áhrif í hópnum geti verið virkt í einu. Taktu eftir að aðeins eitt af sjálfgefnu litabreytingaráhrifunum getur verið virkt í einu. Þetta er vegna þess að þau eru öll í MX Group 1.

Þessi virkni er óvirk ef _MX Group_ stillingin er 0.

### Breyta áhrifum

Hægrismelltu á hvaða áhrif sem er og smelltu á _EDIT EFFECT_ hnappinn til að opna effect editor. Athugaðu að þessi editor er eins og Clip Editor!

Breyttu áhrifunum á sama hátt og þú myndir breyta hvaða Clip sem er. Sjá [Clip Editor](clip-editor/ "mention").

Þú þarft að hafa að minnsta kosti einn Creator node; það getur verið hvað sem er (lína, hringur, shape, jafnvel texti!), en þú ættir líklega að velja eitthvað sem birtist á skýran hátt í forskoðuninni á áhrifahnappnum.

Þegar áhrif eru virkjuð er öllum nodes af gerðinni Creator í áhrifinu skipt út fyrir úttak þeirra Clips sem eru í gangi hverju sinni.

{% hint style="warning" %}
Af afar leiðinlegum tæknilegum ástæðum eru "trails" nodes ekki virk þegar þau eru inni í áhrifum. Sama á við um "delay" stillinguna inni í pattern nodes (þau nota sama kerfi). Þetta verður lagað í síðari útgáfum.
{% endhint %}
