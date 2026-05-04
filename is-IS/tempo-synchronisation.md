---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / samstilling

Samstilling við tónlist er grundvallaratriði í Liberation. Þegar tempo og slög passa við tónlistina geturðu treyst því að allt sé í sync. Ef þú ert svo heppin að fá MIDI clock (eða Ableton Link) þarftu ekkert að hafa áhyggjur af handvirkri samstillingu. Ef ekki, þá er það ekkert mál — þú getur stillt þetta handvirkt með _Live_ tempo-eiginleikanum.

Ef þú hefur reynslu af tónlistar- eða ljósahugbúnaði ætti þetta ferli að vera kunnuglegt. Ef ekki er vel þess virði að gefa þér tíma til að kynnast kerfinu og æfa þig heima áður en þú ferð á lifandi sýningu.

## Spjaldið _Tempo_

Spjaldið _Tempo_ er alltaf sýnilegt á skjánum og inniheldur allar stillingar fyrir samstillingu. Efst sérðu núverandi takta-/slagteljara og transport með hnöppum fyrir play/pause og rewind/fast-forward.

Fyrir neðan það sérðu beat marker; fjóra ferninga sem „púlsa“ í takt við slögin. Þessi _beat marker_ er mjög gagnleg sjónræn vísbending og þú munt nota hana stöðugt þegar þú vinnur með _Live_ tempo-kerfið.

### Stilla tempo

Þú hefur nokkra valkosti til að stilla tempo:

* Smelltu og dragðu _Tempo_ slider
* Shift-smelltu og dragðu _Tempo_ slider til að breyta tempo í 0,1 skrefum
* Tvísmelltu á _Tempo_ slider og sláðu töluna inn handvirkt
* Notaðu _Tempo_ knob á APC40 (ýttu á shift fyrir 0,1 skref)
* Tap Tempo

{% hint style="info" %}
Tempo er skilgreint sem „slög á mínútu“ og hefðbundið sjálfgefið gildi er yfirleitt 120.
{% endhint %}

## Tap Tempo

Stilltu tempo sjálfkrafa með því að smella á _TAP_ hnappinn í takt við slögin. Stilltu upphaf taktsins með _RESET_ hnappinum.

{% hint style="info" %}
Tap Tempo-kerfið er nógu snjallt til að vita hvort þú hafir hætt að tappa í smá stund eða misst af nokkrum slögum. Ef þú byrjar að tappa í tvöföldum hraða skilur það að þú viljir tvöfalda tempo, og það sama gildir ef þú tappar á hálfum hraða.

Það er líka nógu snjallt til að átta sig á því ef tveir einstaklingar eru að tappa tempo á sama tíma (þ.e. annar á lyklaborði og hinn á APC40). Liberation tekur meðaltal af tvöföldu töppunum.
{% endhint %}

#### Lyklaborðsskipanir:

T - tap tempo\
R - endurstilla taktinn\
Y - námunda tempo að næsta slagi á mínútu.

{% hint style="info" %}
Þar sem mest tónlist í dag er búin til stafrænt er líklegt að tempo sé heil tala. Ef tappað tempo virðist vera nálægt réttu gildi skaltu því nota Y lykilinn (eða færa APC40 tempo knob um eitt „tick“) til að námunda það að heilli tölu.
{% endhint %}

#### Stýringar á APC40:

APC40 er með sérstakan _TAP TEMPO_ hnapp, en þú getur líka notað tengdan footswitch til að tappa með fætinum!

Notaðu _TEMPO_ knob til að stilla. Haltu _SHIFT_ inni á meðan þú notar _TEMPO_ knob til að fínstilla.

Notaðu _METRONOME_ hnappinn til að **endurstilla taktinn**. (Athugaðu að _METRONOME_ hnappurinn lýsir líka í takt við slögin)

Snúðu _TEMPO_ knob um eitt „tick“ til hægri eða vinstri til að **námunda tempo** upp eða niður að heilli BPM-tölu.

Sjá einnig [Tilvísun fyrir APC40](reference/apc40-reference.md "mention")

### Hnika tempo

Ef þú ert viss um að þú sért nógu nálægt raunverulegu tempo, en sérð að þú ert að reka úr takti, skaltu nota _NUDGE_ hnappana til að leiðrétta.

Ef Liberation tempo fer á undan tónlistinni skaltu halda _NUDGE -_ inni til að hægja tímabundið á þar til það passar aftur.

Ef Liberation tempo dregst aftur úr tónlistinni skaltu halda _NUDGE +_ inni til að hraða tímabundið þar til það passar aftur.

{% hint style="info" %}
Þú getur annaðhvort notað NUDGE hnappana á skjánum eða sérstöku hnappana á APC40.
{% endhint %}

### Hálfur hraði / tvöfaldur hraði

Notaðu _÷2_ og _x2_ hnappana til að helminga eða tvöfalda tempo varanlega. Ólíkt tempo multiplier er þetta varanleg breyting á núverandi tempo.

## Tempo Multiplier

_Tempo Multiplier_ kerfið gerir þér kleift að breyta tempo tímabundið áður en það fer aftur í fyrra gildi.

Kveiktu eða slökktu á _Tempo Multiplier_ með því að ýta á _TEMPO MULTIPLIER_ hnappinn eða _BANK_ hnappinn á APC40. Stilltu með slider á skjánum eða með APC40 A-B slider. Þú getur líka notað forstillingarhnappana _25%, 50%, 100% 200%_.

## Ytri tempo-gjafar

### MIDI Clock

Til að samstilla við ytra MIDI clock merki skaltu velja _MIDI CLOCK_ radio button og velja MIDI tækið úr fellivalmyndinni. Athugaðu litaða stöðuljósið við hliðina á fellivalmyndunum:

* Grænt - MIDI clock merki berst
* Appelsínugult - hægt er að tengjast MIDI tækinu en ekkert clock merki berst eins og er
* Rautt - ekki hægt að tengjast MIDI tækinu

{% hint style="info" %}
MIDI Clock sendir út röð ramma (24 á hvern fjórðapartsnótu), en skilaboðin innihalda engin staðsetningargögn. Þetta þýðir að það hjálpar til við að halda takti, en þú gætir samt þurft að endurstilla taktinn.

Liberation MIDI Clock tempo-gjafinn bregst einnig við **MIDI Machine Control (MMC)** skilaboðum, þannig að ef clock-gjafinn þinn sendir þau þarftu ekki að endurstilla taktinn handvirkt.
{% endhint %}



### Ableton Link

Til að samstilla við Ableton Link skaltu velja _ABLETON LINK_ sem tempo-gjafa. Liberation tengist Link-lotunni á staðarnetinu þínu og fylgir sameiginlegu tempo og slagfasa frá öðrum öppum sem styðja Link.

Ableton Link notar ekki MIDI tengi og flytur ekki nákvæma staðsetningu í lagi. Notaðu stýringar fyrir endurstillingu takta ef þú þarft að upphaf takts í Liberation falli að tilteknu augnabliki í sýningunni.

### Timeline

Hver timeline hefur sitt eigið tempo, sem getur verið fast gildi eða _Tempo Map_. _Tempo Map_ gerir þér kleift að stilla tempo á tilteknum tímapunktum innan timeline.

Tempo fyrir timeline er notað þegar _TIMELINE_ er valið sem tempo-gjafi.

{% hint style="info" %}
Þú getur keyrt timeline með _hvaða_ tempo-gjafa sem er! Ef þú ert til dæmis með lifandi hljómsveit sem spilar ekki eftir click geturðu ræst timeline handvirkt og haldið því í sync með _LIVE_ tempo-gjafanum. Eða ef þú ert með MIDI clock merki geturðu notað það!
{% endhint %}
