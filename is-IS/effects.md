---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Áhrif

Áhrifakerfið í Liberation er skemmtileg og fjölhæf leið til að breyta clip-úttaki í rauntíma. Áhrif eru mjög sveigjanleg og má nota til að láta allt blikka af og á, snúast, skipta um liti eða jafnvel fljúga um af handahófi!

Allt sem þú getur gert í clip-ritlinum má nota sem áhrif. Reyndar eru áhrif breytt í nákvæmlega sama node-ritli og clip! Sjá [#editing-effects](effects.md#editing-effects). Sköpunarmöguleikarnir eru nánast endalausir.

Sjálfgefnu áhrifahnapparnir 1-8 eru fyrir neðan zone-hnappana, og áhrif 9-24 eru litlu hnapparnir neðst.

#### Að virkja áhrif

Ýttu á áhrifahnapp til að kveikja eða slökkva á áhrifinu, eða enn betra, notaðu APC40-rennana 1-8 til að fasa áhrifin inn og út. Til að fasa inn áhrif án APC40 skaltu smella á hnappinn og draga upp og niður. Þú getur líka hægrismellt á áhrifahnappinn og stillt level-rennann.

{% hint style="warning" %}
Ef þú ýtir á áhrifahnappinn virkjast áhrifin strax. Athugaðu þó að ef level er stillt á núll gerist ekkert! Smelltu og dragðu hnappinn til að breyta level, eða hægrismelltu og notaðu _level_-rennann, eða notaðu APC40-faderana.
{% endhint %}

#### Áhrif og zone delay í clip

Áhrif taka við zone delay-stillingunni fyrir hvert clip sem er í gangi hverju sinni. Ef clip er til dæmis með töf sem færist frá vinstri til hægri, og þú bætir við blikkandi áhrifinu, seinkar blikkinu líka frá vinstri til hægri.

{% hint style="info" %}
Það er mjög erfitt að lýsa því hvernig zone delay úr clip erfist yfir í áhrif, en þetta verður augljóst þegar þú prófar það!

Ég myndi segja að þetta sé eitt skemmtilegasta og skapandi verkfærið sem er innbyggt í Liberation. Prófaðu og þá sérðu hvað ég á við!
{% endhint %}

#### Færibreytur áhrifa

Bættu færibreytu við áhrifin með _Parameter node._ Parameter-kerfið er leið til að stilla margar stillingar inni í áhrifinu utan frá. Sjá [parameter-control.md](clip-editor/oscillators/parameter-control.md) fyrir nánari upplýsingar.

Notaðu rotary controllers 1-8 til að stilla _parameter_ fyrir hvert áhrif. Einnig geturðu hægrismellt á áhrifahnappinn og stillt parameter-rennann eða rennana. Breyting á parameter gerir mismunandi hluti eftir því hvernig áhrifin eru sett upp. Sjá listann hér fyrir neðan yfir sjálfgefnu áhrifin og hvað færibreytur þeirra gera.

{% hint style="info" %}
Rotary controllers 1-8 eru efst á APC40 Mk2 og efst til hægri á Mk1. Sjá einnig: [apc40-reference.md](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
Litlu tölurnar sem þú sérð á áhrifahnöppunum vísa til _level_ og _parameter_ áhrifsins. _level_ er stjórnað með fader á APC40, eða þú getur smellt og dregið á hnappinum. Parameter er stillt með rotary controls á APC40, eða þú getur hægrismellt og stillt með músinni.
{% endhint %}

#### Sjálfgefnu áhrifin

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Bætir óreiðukenndri hreyfingu við clip-úttakið. Parameter stillir magn/hraða óreiðunnar.
2. **Sine wave** :\
   Bjagar allt efnið yfir hreyfanlega sínusbylgju. Parameter stillir bylgjulengdina.
3. **Rotation** :\
   Lætur allt snúast. Parameter stillir snúningshraðann.
4. **Horizontal flip** :\
   Þjappar og teygir allt lárétt. Parameter stillir hraðann.
5. **Scale** :\
   Skalar allt endurtekið frá fullri stærð niður í núll. Parameter stillir hraðann.
6. **Hue** :\
   Breytir litblæ alls, en breytir ekki litmettuninni (þ.e. allt sem er hvítt helst hvítt). Parameter stillir litblæinn.
7. **Saturation and hue** :\
   Breytir litblæ alls og mettar litinn líka að fullu (þ.e. allt sem er hvítt breytist yfir í litinn). Parameter stillir litblæinn.
8. **Flash** :\
   Lætur birtu alls blikka endurtekið frá fullri birtu niður í núll. Parameter stillir blikkhraðann.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Það eru 16 litáhrif til viðbótar í neðstu röðinni til að beita forstilltum gildum fyrir litblæ og litmettun.

Athugaðu að þetta eru sjálfgefnu áhrifin, en þú getur breytt þeim þannig að þau geri nánast hvað sem þú vilt!

### Beita á hópa

Þú getur valið hvaða hópar verða fyrir áhrifunum. Hægrismelltu og kveiktu eða slökktu á gátreitunum fyrir hópa sem eru merktir _Apply to groups._

Ég nota þessa uppsetningu aðallega þegar ég vinn með canvas-grafík og lasergeisla aðskilið. Ég úthluta öllum canvas-clipum í hóp 5 og útiloka svo þennan hóp frá áhrifum sem ég vil ekki að hafi áhrif á þessi grafísku clip.

Þú gætir líka notað þetta til að beita tveimur mismunandi litabreytingum í beinni á tvo laserhópa í einu. Búðu til tvö litabreytingaráhrif og veldu hvaða clip-hópa hvort þeirra á að hafa áhrif á.

### MX group

Stytting á _Mutually Exclusive_. Þetta er leið til að hópa áhrif saman þannig að aðeins eitt áhrif í hópnum geti verið virkt í einu. Taktu eftir að aðeins eitt af sjálfgefnu litabreytingaráhrifunum getur verið virkt í einu. Það er vegna þess að þau eru öll í MX Group 1.

Þessi virkni er óvirk ef _MX Group_-stillingin er 0.

### Að breyta áhrifum

Hægrismelltu á hvaða áhrif sem er og smelltu á _EDIT EFFECT_ hnappinn til að opna áhrifaritilinn. Athugaðu að þessi ritill er eins og clip-ritillinn!

Breyttu áhrifinu á sama hátt og þú myndir breyta hvaða clip sem er. Sjá [clip-editor](clip-editor/).

Þú þarft að hafa að minnsta kosti einn creator node; þetta getur verið hvað sem er (lína, hringur, form, jafnvel texti!), en þú ættir líklega að velja eitthvað sem kemur best út í forskoðuninni á áhrifahnappinum.

Þegar áhrifum er beitt er öllum creator nodes í áhrifinu skipt út fyrir úttakið frá þeim clipum sem eru í gangi hverju sinni.

{% hint style="warning" %}
Af mjög leiðinlegum tæknilegum ástæðum eru "trails" nodes ekki virkir inni í áhrifum. Sama á við um "delay"-stillinguna inni í pattern nodes (þau nota sama kerfi). Þetta verður lagað í síðari útgáfum.
{% endhint %}
