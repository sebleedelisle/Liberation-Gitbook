---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Flýtihandbók

## Inngangur

Velkomin í **Liberation** — næstu kynslóð hugbúnaðar fyrir leysisýningar.

Liberation er öflugur og fjölhæfur nútímahugbúnaður. Hann byggir á notendavænni og áreiðanleika til að gefa þér frelsi til að tjá sköpunargáfuna. Hann er hraður, skilvirkur og hnökralaus. Fylgdu þessari _flýtihandbók_ til að komast hratt af stað!

### Umsjón með leysum

Liberation er nógu sveigjanlegt til að þú getir sett upp leysa og séð þá fyrir þér án þess að nokkur raunverulegur leysir sé tengdur. Þegar komið er að því að keyra sýninguna geturðu síðan úthlutað hverju Output til laser controller án vandræða.

{% hint style="info" %}
Þú getur sett upp og myndgert eins marga leysa og þú vilt í Liberation. Leyfisþrepin (Hobbyist, Pro o.s.frv.) takmarka aðeins fjölda leysa sem þú getur sett í _armed_ stöðu. Þetta þýðir að þú getur hannað leysisýningar með 100 leysum jafnvel með ókeypis leyfi. Þú þarft aðeins að uppfæra þegar kemur að því að keyra sýninguna á raunverulegum leysum.
{% endhint %}

Sjálfgefin uppsetning er með 8 leysum dreifðum lárétt, en þú getur breytt þessu eins og þú vilt. Líklega er best að halda þessari sjálfgefnu uppsetningu á meðan þú kynnist hugbúnaðinum og stilla hana síðar til að passa við búnaðinn þinn. (Sjá [Uppsetning verkefnisins](setting-up/setting-up-your-project.md))

{% hint style="warning" %}
Mikilvægt: Áður en þú setur nokkra leysa í armed stöðu skaltu ganga úr skugga um að þú skiljir áhættuna og fara vandlega yfir kaflann [Uppsetning leysa](setting-up/setting-up-lasers.md).
{% endhint %}

## Yfirlit yfir hugbúnaðinn

### Öryggisstöðvun

Alltaf þegar þú keyrir leysa þarftu að hafa **neyðarstöðvunarhnapp í vélbúnaði** við höndina (sjá [Neyðarstöðvun / öryggislæsingar](hardware/emergency-stop-interlocks.md)). Ef þú vilt disarm allt án þess að um bráðatilvik sé að ræða geturðu notað _**DISARM ALL**_ hnappinn eða `Escape` lykilinn (eða _**SESSION**_ lykilinn á APC40). Þú getur líka lækkað Global Brightness með sleðanum á skjánum eða aðal-fader á APC40.

### Sleðar og stýringar

Í Liberation eru ýmsir sleðar og stýringar.

{% hint style="info" %}
`Cmd / Ctrl`-smelltu á sleða til að slá inn nýtt gildi ef þú þarft meiri nákvæmni en sleðinn býður upp á.
{% endhint %}

### Flýtilyklar

Heildarlista yfir flýtilykla má finna hér: [Flýtilyklar](reference/keyboard-shortcuts.md)

### Skjáuppsetning

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Ertu ekki viss hvað ákveðinn hnappur gerir? Færðu músina yfir hann til að sjá lýsingu!
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Í valmyndinni finnurðu alla valkosti fyrir innflutning og útflutning skráa, ásamt því að opna panels. Þar finnurðu einnig möguleikann á að heimila tölvuna með áskriftinni þinni (í _Liberation -> Authorise/Deauthorise this computer_).

#### Icon bar

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Hér finnurðu algeng verkefni, svo sem að arm/disarm alla leysa, Global Brightness, test pattern og að skipta á milli 3D view, Canvas view og Output view.

### Views

Stóra svæðið efst til vinstri á skjánum getur verið eitt af 3 aðal-views: **3D**, **CANVAS** og **OUTPUT.** Skiptu á milli þeirra með hnöppunum á icon bar (eða notaðu `Tab` lykilinn til að skipta á milli 3D view og OUTPUT view og haltu síðan áfram að fletta í gegnum hvert laser Output fyrir sig).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view sýnir hvernig leysarnir munu líta út og hægt er að stilla það til að passa við þína eigin uppsetningu. Smelltu og dragðu til að snúa myndavélinni og notaðu músarhjólið til að færa þig fram og til baka. Þú finnur marga aðra valkosti í _3D Visualiser settings_ panel (_View -> 3D Visualiser Settings_). Sjá [3D Visualiser](setting-up/3d-visualiser.md).

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view er notað til að stilla zones og masks fyrir hvern leysi. (Taktu eftir stóra númerinu efst í vinstra horninu svo þú sjáir auðveldlega hvaða leysi þú ert að vinna með!)

Þetta view sýnir allt Output þessa leysis og hvar hvert zone er staðsett innan þess. Sjálfgefið er aðeins eitt zone á hvern leysi, en þú getur bætt við eins mörgum zones og er raunhæft, og þau birtast öll í þessu view.

{% hint style="info" %}
**Hvað er zone?**

Zone er rými innan Output leysis sem þú getur beint laser-efni inn í. Þú getur haft fleiri en eitt zone á hverjum leysi. Einfaldasta gerðin er _beam_ zone, en einnig eru til _canvas_ zones og _DMX_ zones. Í þessari handbók einbeitum við okkur aðallega að beam zones, sem eru yfirleitt notuð til að búa til geislaáhrif í loftinu.
{% endhint %}

Þú getur valið leysinn sem þú vilt breyta með einni af þessum leiðum:

* númeruðu hnöppunum á stikunni efst
* því að ýta á númeralykilinn fyrir leysinn sem þú vilt _(lyklarnir 1–9)_
* `Tab` lyklinum til að fara í gegnum þá einn af öðrum

Bættu nýjum leysi við uppsetninguna með því að ýta á _+_ hnappinn. (Það er líka _ADD LASER_ hnappur í _Laser Overview_ panel)

Eyddu leysi úr uppsetningunni með því að ýta á rauða ⊖ hnappinn í _Laser Overview_ panel.

Þú getur súmmað inn og út með músarhjólinu og smellt og dregið hvar sem ekki er zone til að færa view.

Smelltu á zone til að velja það og stilltu síðan hornpunktana með músinni. Haltu `Alt / Option` niðri á meðan þú dregur horn til að gera breytinguna ójafna. Hægrismelltu á zone til að sjá fleiri valkosti, þar á meðal að breyta gerð þess.

Vinstra megin er stika með röð af táknhnöppum. Færðu músina yfir hvaða hnapp sem er til að fá lýsingu á því hvað hann gerir. Hnapparnir hér leyfa þér að bæta við beam zones, canvas zones og masks. Þar eru líka valkostir til að stilla test pattern aðeins fyrir þennan leysi, ásamt stillingum fyrir grid og snapping.

Nánari upplýsingar eru í [Output-sýn](output-view/).

#### Canvas

Canvas kerfið er aðallega notað fyrir grafík og arkitektúr-mapping. Þú getur dreift flóknum myndum yfir marga leysa og leiðrétt sjónarhorn fyrir hvern hluta. Sjá [Grafík og Canvas kerfið](graphics-and-the-canvas-system/).

### APC40 MIDI controller

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Þótt hægt sé að stjórna Liberation með mús og lyklaborði er mun betra að nota APC40 MIDI controller (Mark 2 er best, en Mark 1 virkar líka).

Sjá einnig: [APC40 tilvísun](reference/apc40-reference.md)

Við höfum nú einnig innleitt stuðning við APC Mini Mark 2 og MIDI Fighter Twister og fleiri tæki eru í þróun. APC40 Mark 2 er þó besti kosturinn í flestum tilvikum.

### Clips og effect-ar

{% hint style="info" %}
**Hvað er Clip?**

Clip er ílát fyrir hvers konar laser-efni innan Liberation. Clips geta innihaldið geisla eða grafískar hreyfimyndir og eru yfirleitt lykkja sem endurtekur sig. Hægt er að beina þeim inn í hvaða zone sem er (eða _Canvas target area_) og þau eru ræst með Clip hnöppunum inni í Clip Deck.
{% endhint %}

#### Yfirlit yfir Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Þetta grid kallast _Clip Deck_ og þar eru öll laser Clips geymd. Það er hannað til að samsvara beint 8 x 5 hnappagrindinni á APC40.

**Fletting í Clip Deck.**

Þú getur skrunað Clip Deck til vinstri og hægri með:

* Vinstri og hægri örvalyklum. Bættu við `Cmd / Ctrl` til að skruna heila síðu í einu.
* Snertiplatta: Strjúka
* Mús: ef músin þín styður hliðarskrun geturðu notað það þegar bendillinn er yfir Clip Deck
* APC40 scroll knob
* APC40 _<- DEVICE ->_ hnöppunum

Til að auðvelda þér að átta þig er lítið visualiser af Clip Deck efst. Sjá einnig [Clips og Clip Deck](clips/)

#### Að ræsa og stöðva Clips

Ýttu á Clip hnapp (annaðhvort með músinni eða APC40) til að ræsa Clip. Ýttu aftur til að stöðva það. Þegar þú ræsir Clip stöðvast öll önnur Clips í sama lit sjálfkrafa nema þú haldir _shift_ niðri.

Sum Clips eru í _Flash mode_ (sjálfgefið þau rauðu), og þá stöðvast þau um leið og þú sleppir Clip hnappnum.

_STOP_ hnappurinn stöðvar öll Clips sem eru í gangi.

#### Að stilla Output zones fyrir Clip

Undir Clip hnöppunum sérðu zone hnappana, beam zones 1 til 8 sjálfgefið (_BEAM 1_, _BEAM 2_ o.s.frv.). Zone hnapparnir lýsast upp til að sýna hvaða zones eru tengd við Clip sem er valið hverju sinni.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Tveimur röðum fyrir neðan zone hnappana sérðu X/Y flip hnappana. Kveiktu eða slökktu á þeim til að spegla Clip lárétt og lóðrétt.

{% hint style="info" %}
Athugaðu að þessar zone úthlutanir og X/Y flip stillingar tengjast Clip sjálfu. Þær haldast næst þegar þú keyrir það Clip. Þetta er ekki global stilling.
{% endhint %}

Hægrismelltu á Clip til að breyta fleiri stillingum fyrir það. Sjá einnig [Clip stillingar](clips/clip-settings.md)

### Groups

Þú tekur eftir því að hvert Clip hefur litaða útlínu og liturinn sýnir í hvaða _group_ það er. Clip hnapparnir á APC40 lýsast einnig í þessum lit.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Blágrænt</td></tr><tr><td>Group 2</td><td>Appelsínugult</td></tr><tr><td>Group 3</td><td>Rautt</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Grænt</td></tr></tbody></table>

Group kerfið er mjög sveigjanlegt og gerir þér kleift að:

* Láta Clips í einum group halda áfram á meðan þú kveikir og slekkur á groups í öðrum
* Úthluta zones og X/Y flips hratt á öll Clips innan group
* Stilla _Flash mode_ fyrir Clip (Group 3 er sjálfgefið í _Flash mode_)

Groups hafa einnig stillingar fyrir transition inn/út sem Clips geta erft eða yfirskrifað.

Þú getur úthlutað group fyrir Clip með hnöppunum í hægrismellsvalmyndinni. Með APC40 geturðu líka ýtt á group hnappinn og, _á meðan honum er enn haldið niðri,_ ýtt á Clip hnappana.

Breyta zone stillingum fyrir öll Clips innan group

Með APC40 ýtirðu á group hnappinn og notar síðan, _á meðan honum er enn haldið niðri,_ zone og X/Y hnappana til að kveikja eða slökkva á zone stillingum fyrir öll Clips í þeim group.

Sjá einnig [Hópar fyrir Clips](clips/groups.md)

### Effects

Effects kerfið í Liberation er öflug og fjölhæf leið til að breyta Output frá Clip í rauntíma. Sjálfgefnu effect hnapparnir 1–8 eru undir zone hnöppunum.

#### Að beita effect

Ýttu á effect hnapp til að kveikja eða slökkva á effect, eða enn betra, notaðu APC40 sleðana 1–8 til að fade-a effects inn og út.

#### Effect parameters

Notaðu rotary controllers 1–8\* til að stilla _parameter_ fyrir hvert effect. (Eða þú getur hægrismellt með músinni til að stilla level og parameter). Breyting á parameter gerir mismunandi hluti eftir því hvernig effect er sett upp. Sjá listann hér fyrir neðan yfir sjálfgefin effects.

{% hint style="info" %}
Litlu tölurnar sem þú sérð á effect hnöppunum vísa til _level_ og _parameter_ fyrir effect. _Level_ er stýrt með fader á APC40 eða með því að smella og draga á hnappnum. Parameter er stillt með rotary hnöppunum á APC40 eða með því að hægrismella og stilla með músinni.
{% endhint %}

_\*Rotary controllers 1–8 eru efst á APC40 Mk2 og efst til hægri á Mk1. Sjá einnig:_ [APC40 tilvísun](reference/apc40-reference.md)

#### Sjálfgefin effects

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Bætir óreiðukenndri hreyfingu við Output frá Clip. Parameter stillir magn/hraða óreiðunnar.
2. **Sine wave** :\
   Aflagar allt efnið eftir hreyfanlegri sínusbylgju. Parameter stillir bylgjulengdina.
3. **Rotation** :\
   Snýr öllu í hring. Parameter stillir snúningshraðann.
4. **Horizontal flip** :\
   Kremur og teygir allt lárétt. Parameter stillir hraðann.
5. **Scale** :\
   Skalar allt endurtekið frá fullri stærð niður í núll. Parameter stillir hraðann.
6. **Hue** :\
   Breytir litblæ alls, en breytir ekki mettuninni (þ.e. allt sem er hvítt helst hvítt). Parameter stillir litblæinn.
7. **Saturation and hue** :\
   Breytir litblæ alls og mettar litinn að fullu (þ.e. allt sem er hvítt breytist í litinn). Parameter stillir litblæinn.
8. **Flash** :\
   Lætur birtu alls blikka endurtekið frá fullri birtu niður í núll. Parameter stillir blikkhraðann.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Að auki eru 16 colour effects í neðstu röðinni til að beita fyrirfram stilltum gildum fyrir hue og saturation.

Athugaðu að þetta eru sjálfgefin effects, en hægt er að breyta þeim til að gera nánast hvað sem þú vilt!

#### Hvað er _Clip sem er valið núna_?

Þegar þú ræsir Clip lýsist það upp til að sýna að það sé virkt. Það hefur einnig hvíta útlínu sem sýnir að þetta er Clip sem er valið núna. Alltaf þegar þú kveikir eða slekkur á zone hnöppum eða breytir Clip stillingum eru þær breytingar notaðar á _Clip sem er valið núna_.

{% hint style="info" %}
Til að velja Clip án þess að ræsa það skaltu halda `Alt / Option` niðri áður en þú ýtir á Clip hnappinn. Þetta er góð leið til að stilla zones og aðrar stillingar án þess að keyra það.
{% endhint %}

### Clip Settings panel

Notaðu _Clip Settings_ panel til að breyta scaling, X/Y position og fá aðgang að öfluga zone delay kerfinu.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings panel

Finndu _Global Settings_ panel til að stilla global Output stillingar sem hafa áhrif á allt Output yfir öll zones.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Kveiktu á AUTO RESET til að endurstilla allar _Global settings_ sjálfkrafa þegar engin Clips eru í spilun.

### Timing

Næstum allar leysisýningar eru með einhvers konar tónlist, þannig að timing kerfið í Liberation byggir á tempo í slögum á mínútu. Í _Tempo Panel_ sérðu framsetningu á tímanum; hver ferningur táknar einn slag og þú sérð þá blikka í takt.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Það eru margir möguleikar fyrir samstillingu, þar á meðal MIDI clock og Ableton Link. Ef þú veist tempo tónlistarinnar geturðu stillt það handvirkt með sleðanum á skjánum eða APC40 Tempo hnappnum, en þú getur líka haldið takt við tónlistina með _Tap Tempo_ kerfinu.

#### Tap Tempo

_Tap Tempo_ er hugtak sem er algengt í tónlistarforritum og gerir þér kleift að slá inn taktinn til að stilla tempo á meðan tónlistin spilar. Þú getur notað hnappinn á skjánum, en mælt er með því að nota _T_ lykilinn eða _Tap Tempo_ hnappinn á APC40 (eða jafnvel fótrofa ef þú vilt).

Ýttu á _R_ lykilinn eða _Metronome_ hnappinn (APC40) til að endurstilla tempo að byrjun taktsins.

Ýttu á _Y_ lykilinn eða snúðu _Tempo_ hnappnum(APC40) til að rúnna tempo í heila tölu. Þetta getur verið gagnlegt fyrir raftónlist, þar sem slög á mínútu eru oft heil tala.

### Að skipuleggja Clip Deck

Til að færa Clip á Clip Deck skaltu smella á það og draga á nýjan stað. Á meðan þú dregur geturðu notað örvalyklana (eða scroll wheel/buttons á APC40) til að skruna til vinstri og hægri.

Haltu `Alt / Option` niðri á meðan þú dregur til að búa til afrit.

`Alt / Option`-smelltu á Clip til að velja það án þess að ræsa það.

`Alt / Option + Shift`-smelltu á Clip til að velja fleiri en eitt, eða smelltu og dragðu utan við Clip til að velja með „lasso“.

Smelltu og dragðu til að draga ÖLL valin Clips.

Til að eyða einu eða fleiri Clips geturðu annaðhvort dregið þau út af Clip Deck (ruslatunnutákn birtist) eða notað DELETE hnappinn í hægrismellsvalmynd Clip.

### Laser Overview panel

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser Overview panel_ gefur þér fljótlegt yfirlit yfir stöðu leysanna sem eru í gangi. Græni ferningurinn hægra megin sýnir að laser controller sé í lagi. Ef hann verður appelsínugulur eru einstaka drop-outs, og ef hann verður rauður hefur hann aftengst. Ef hann er grár er hann alls ekki tengdur við controller.

Grafið í miðjunni sýnir sögu rammalengda og talan hægra megin er núverandi frame rate. Því flóknara sem efnið er, því hægari verður frame rate (þ.e. meira flökt). Allt undir um það bil 25fps byrjar að líta dálítið flöktandi út.

### Að tengjast leysum — Controller Assignment panel

Smelltu á _Assign Laser Controllers_ hnappinn til að opna _Controller Assignment_ panel. (Þetta panel er einnig aðgengilegt í valmyndastikunni undir _View -> Controller Assignment_).

Hér geturðu valið hvaða laser Outputs fara til hvaða laser controllers. Dragðu controllers úr listanum hægra megin yfir í reitina vinstra megin. Þú getur endurnefnt controllers til að passa við leysinn sem þeir eru paraðir við (notaðu pennatákn-hnappinn).

Lestu kaflann [Úthlutun laser controller](setting-up/controller-assignment.md) fyrir nánari upplýsingar.

{% hint style="danger" %}
Áður en þú setur nokkra leysa í armed stöðu skaltu fara yfir kaflann [Uppsetning leysa](setting-up/setting-up-lasers.md).
{% endhint %}

### Laser Output panel

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Þetta panel sýnir stillingar fyrir _currently selected laser_ (táknað með númerinu efst). Breyttu hvaða leysir er valinn hverju sinni með _tab_ lyklinum, með því að ýta á númeralykil, smella á leysinúmer í _Laser Overview_ panel eða í _Output view._

* **Number button** setur leysinn í arm eða disarm. Ef hnappurinn er rauður er leysirinn armed.
* **Brightness** stillir birtu leysisins óháð öðrum leysum (og hún leggst saman við _Global Brightness_ stillinguna — þ.e. ef báðar eru 50% verður leysirinn á 25%).
* **Test Pattern** kveikir á test pattern aðeins fyrir þennan leysi (yfirskrifar global test pattern stillinguna)
* **Orientation** leiðréttir fyrir leysa sem eru hengdir upp á hlið eða á hvolfi.
* **Flip Horizontal and Flip Vertical** snýr Output leysisins við. Gagnlegt til að leiðrétta Output á leysum sem eru ekki víraðir eins.
* **Copy Laser Settings** opnar panel sem gerir þér kleift að afrita ýmsar stillingar frá þessum leysi yfir á aðra.

### Scanner settings

Sýningaleysarar virka með því að færa einn leysigeisla mjög hratt og kveikja og slökkva á honum til að teikna form í loftinu. Það sem þú sérð sem línur, form og myndir er í raun geislinn að rekja ferla hraðar en augað nær að fylgja.

Point stream er gögnin sem segja leysinum hvert hann á að færa sig næst og hvenær geislinn á að vera kveiktur eða slökktur. Í Liberation er Clips umbreytt í þennan point stream í rauntíma þegar þau eru send til leysanna.

Liberation gefur þér nákvæma stjórn á því hvernig þessi point stream er myndaður, þannig að þú getir jafnað smoothness, brightness og performance fyrir hvern leysi.

{% hint style="info" %}
Ef þú ert vön eldri leysihugbúnaði sem byggir á fyrirfram útreiknuðum point streams gæti þessi nálgun virkað öðruvísi í fyrstu. Rauntímamyndun punkta gerir þó kleift að fínstilla sama efni á mismunandi hátt fyrir hvern leysi. Það auðveldar vinnu með marga leysa sem hafa mismunandi scanner hraða eða gæði, án þess að afrita eða endurbyggja efni. Þetta heldur Clip skrám einnig mjög litlum, sem er ástæðan fyrir því að allt sjálfgefna Liberation Clip Deck er aðeins nokkur megabæt í stað gígabæta.
{% endhint %}

Grunnstillingar fyrir scanner eru:

* **Speed** er scanner hraðinn, þ.e. hversu hratt leysirinn hreyfist til að teikna form. Þetta jafngildir því að stilla point rate í hefðbundnum leysihugbúnaði, en í Liberation geturðu breytt því hversu hratt leysirinn hreyfist _óháð point rate._ Þú ættir ekki að þurfa að breyta þessu.
* **Scanner sync** (stundum kallað _blank shift, áður Colour Shift_) Scanner færir leysigeislann mjög hratt, en yfirleitt eru breytingar á birtu og lit ekki í takt við hreyfinguna. Þetta birtist sem lítil flöktandi „hala“-ljós við jaðar geisla og lína. Notaðu þessa stillingu til að samstilla hreyfingu og lit. Sjá [Laser Settings](setting-up/laser-settings.md)

Aðrar ítarlegar scanner stillingar eru útskýrðar í kaflanum [Ítarlegt](advanced/).

### Zoning

Heildarleiðbeiningar um uppsetningu og zoning fyrir leysa eru hér: [Uppsetning leysa](setting-up/setting-up-lasers.md)
