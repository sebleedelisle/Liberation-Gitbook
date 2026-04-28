---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempó / samstilling

Samstilling við tónlist er grunnþáttur í Liberation; þegar tempó og slög passa við tónlistina geturðu verið viss um að allt sé samstillt. Ef þú ert svo heppin(n) að fá MIDI clock (eða Ableton Link) þarftu alls ekki að hafa áhyggjur af handvirkri samstillingu. Ef ekki, hafðu engar áhyggjur — þú getur stillt þetta handvirkt með _Live_ tempo-eiginleikanum.

Ef þú hefur reynslu af tónlistar- eða ljósahugbúnaði ætti þetta ferli að vera kunnuglegt. Ef ekki er þess virði að gefa sér tíma til að kynnast kerfinu og æfa sig heima áður en þú mætir á lifandi sýningu.

## Tempo-spjaldið

_Tempo_-spjaldið er alltaf sýnilegt á skjánum og inniheldur allar samstillingarstillingar. Efst sérðu núverandi takt-/slagteljara og stjórnstiku með play/pause og rewind/fastforward hnöppum.

Fyrir neðan það sérðu slagmerkið; fjóra ferninga sem „púlsa“ í takt við slagið. Þetta _beat marker_ er mjög gagnleg sjónræn vísbending og þú munt nota það stöðugt þegar þú vinnur með _Live_ tempo-kerfið.

### Að stilla tempó

Þú hefur nokkrar leiðir til að stilla tempóið:

* Smelltu og dragðu _Tempo_ sleðann
* Shift-smelltu og dragðu _Tempo_ sleðann til að breyta tempóinu í 0.1 skrefum
* Tvísmelltu á _Tempo_ sleðann og sláðu töluna inn handvirkt
* Notaðu _Tempo_ snúningshnappinn á APC40 (ýttu á shift fyrir 0.1 skref)
* Tap Tempo

{% hint style="info" %}
Tempó er skilgreint í „slögum á mínútu“ og hefðbundið sjálfgefið gildi er yfirleitt 120.
{% endhint %}

## Tap Tempo

Stilltu tempóið sjálfkrafa með því að smella á _TAP_ hnappinn í takt við slagið. Stilltu upphaf taktsins með _RESET_ hnappinum.

{% hint style="info" %}
Tap Tempo-kerfið er nógu snjallt til að vita hvort þú hafir gert hlé á töppun í smá stund eða misst úr nokkur slög. Ef þú byrjar að tappa á tvöföldum hraða skilur það að þú viljir tvöfalda tempóið; það sama á við ef þú tappar á hálfum hraða.

Það er líka nógu snjallt til að átta sig á því ef tveir einstaklingar eru að tappa tempó á sama tíma (þ.e. einn á lyklaborðinu og einn á APC40). Liberation tekur meðaltal af tvöföldu töppunum.
{% endhint %}

#### Lyklaborðsskipanir:

T - tap tempo\
R - reset the bar\
Y - námunda tempóið að næsta heila slagi á mínútu.

{% hint style="info" %}
Þar sem flest tónlist í dag er búin til stafrænt er líklegt að tempóið sé heil tala. Ef tempóið sem þú tappar virðist vera nálægt, notaðu þá Y lykilinn (eða hreyfðu APC40 tempo-snúningshnappinn um eitt „tick“) til að námunda það að heilli tölu
{% endhint %}

#### APC40-stýringar:

APC40 er með sérstakan _TAP TEMPO_ hnapp, eða þú getur líka notað tengdan fótrofa til að tappa með fætinum!

Notaðu _TEMPO_ snúningshnappinn til að stilla. Haltu _SHIFT_ inni á meðan þú notar _TEMPO_ snúningshnappinn fyrir fínstillingar.

Notaðu _METRONOME_ hnappinn til að **endurstilla taktinn**. (Athugaðu að _METRONOME_ hnappurinn lýsir líka í takt við slagið)

Snúðu _TEMPO_ snúningshnappinum um eitt „tick“ til hægri eða vinstri til að **námunda tempóið** upp eða niður að heilli BPM tölu.

Sjá einnig [apc40-reference.md](reference/apc40-reference.md)

### Nudge tempo

Ef þú ert viss um að þú sért nógu nálægt raunverulegu tempói en finnur að þú ert að reka úr takti, notaðu þá _NUDGE_ hnappana til að leiðrétta.

Ef Liberation-tempóið fer fram úr tónlistinni skaltu halda _NUDGE -_ inni til að hægja tímabundið á því þar til það samstillist aftur.

Ef Liberation-tempóið dregst aftur úr tónlistinni skaltu halda _NUDGE +_ inni til að hraða tímabundið á því þar til það samstillist aftur.

{% hint style="info" %}
Þú getur annaðhvort notað NUDGE hnappana á skjánum eða sérstöku hnappana á APC40.
{% endhint %}

### Half time / double time

Notaðu _÷2_ og _x2_ hnappana til að helminga eða tvöfalda tempóið varanlega. Ólíkt tempo multiplier er þetta varanleg breyting á núverandi tempói.

## Tempo Multiplier

_Tempo Multiplier_ kerfið gerir þér kleift að breyta tempóinu tímabundið áður en það fer aftur í fyrra gildi.

Kveiktu eða slökktu á _Tempo Multiplier_ með því að ýta á _TEMPO MULTIPLIER_ hnappinn eða _BANK_ hnappinn á APC40. Stilltu með sleðanum á skjánum eða með APC40 A-B sleðanum. Þú getur líka notað _25%, 50%, 100% 200%_ forstillingarhnappana.

## Ytri tempóuppsprettur

### MIDI Clock

Til að samstilla við ytra MIDI clock merki skaltu velja _MIDI CLOCK_ valhnappinn og velja MIDI tækið úr fellivalmyndinni. Athugaðu litaða stöðuljósið við hliðina á fellivalmyndunum:

* Grænt - tekur á móti MIDI clock merki
* Appelsínugult - getur tengst MIDI tækinu en ekkert clock merki er til staðar eins og er
* Rautt - getur ekki tengst MIDI tækinu

{% hint style="info" %}
MIDI Clock sendir út röð ramma (24 á hvern fjórðungsnótu), en engin staðsetningargögn eru í skilaboðunum. Þetta þýðir að það hjálpar til við að halda takti, en þú gætir samt þurft að endurstilla taktinn.

Liberation MIDI Clock tempóuppsprettan bregst einnig við **MIDI Machine Control (MMC)** skilaboðum, þannig að ef clock-uppsprettan þín sendir þau þarftu ekki að endurstilla taktinn handvirkt.
{% endhint %}



### Timeline

Hver timeline hefur sitt eigið tempó, sem getur verið fast gildi eða _Tempo Map_. _Tempo Map_ gerir þér kleift að stilla tempóið á tilteknum tímapunktum innan timeline.

Timeline-tempóið verður notað þegar _TIMELINE_ er valið sem tempóuppspretta.

{% hint style="info" %}
Þú getur keyrt timeline með _hvaða_ tempóuppsprettu sem er! Ef þú ert til dæmis með lifandi hljómsveit sem spilar ekki eftir click, geturðu ræst timeline handvirkt og haldið henni samstilltri með _LIVE_ tempóuppsprettunni. Eða ef þú ert með MIDI clock merki geturðu notað það!
{% endhint %}
