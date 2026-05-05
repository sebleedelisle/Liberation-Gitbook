# ✅ Flýtileiðbeiningar

## Inngangur

Velkomin í **Liberation** - næstu kynslóð hugbúnaðar fyrir leysissýningar.

Liberation er öflugur og flókinn nútímahugbúnaður; hann byggir á notagildi og áreiðanleika til að gefa þér frelsi til að tjá sköpunargáfuna. Hann er hraður, skilvirkur og þægilegur í notkun; fylgdu þessum _flýtileiðbeiningum_ til að komast af stað á örskömmum tíma!

### Umsjón með leysum

Liberation er nógu sveigjanlegt til að þú getir sett upp leysa og séð þá fyrir þér án þess að nokkrir raunverulegir leysar séu tengdir. Þegar komið er að því að keyra sýninguna geturðu úthlutað hverju output til laser controller án vandræða.

{% hint style="info" %}
Þú getur sett upp og séð fyrir þér eins marga leysa og þú vilt í Liberation. Leyfisþrepin (Hobbyist, Pro o.s.frv.) takmarka aðeins fjölda leysa sem þú getur sett í _arm._ Þetta þýðir að þú getur hannað leysissýningar með 100 leysum jafnvel með ókeypis leyfi. Þú þarft aðeins að uppfæra þegar kemur að því að keyra sýninguna á raunverulegum leysum.
{% endhint %}

Sjálfgefið eru 8 leysar dreifðir lárétt, en þú getur sérsniðið þetta eins og þú vilt. Það er líklega best að halda þessari sjálfgefnu uppsetningu á meðan þú ert að kynnast hugbúnaðinum, og laga hana síðar að þinni vélbúnaðaruppsetningu. (Sjá [Uppsetning verkefnis](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Mikilvægt: Áður en þú setur einhverja leysa í arm skaltu ganga úr skugga um að þú skiljir áhættuna og fara vandlega yfir kaflann [Uppsetning leysa](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Yfirlit yfir hugbúnaðinn

### Öryggisstöðvun

Í hvert sinn sem þú keyrir leysa verður þú að hafa **vélrænan neyðarstöðvunarhnapp** við höndina (sjá [Neyðarstöðvun / öryggislæsingar](../hardware/emergency-stop-interlocks.md "mention")), en ef þú vilt setja allt í disarm án þess að um bráðatilvik sé að ræða geturðu notað _**DISARM ALL**_ hnappinn eða `Escape` lykilinn (eða _**SESSION**_ lykilinn á APC40). Þú getur líka lækkað Global Brightness með sleðanum á skjánum eða aðal-fader á APC40.

### Sleðar og stýringar

Í Liberation eru ýmsir sleðar og stýringar.

{% hint style="info" %}
`Cmd / Ctrl`-smelltu á sleða til að slá inn nýtt gildi ef þú þarft meiri nákvæmni en sleðinn býður upp á.
{% endhint %}

### Flýtilyklar

Heildarlista yfir flýtilykla má finna hér: [Flýtilyklar](../reference/keyboard-shortcuts.md "mention")

### Skjáuppsetning

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Ertu ekki viss hvað tiltekinn hnappur gerir? Haltu músinni yfir honum til að fá lýsingu!
{% endhint %}

#### Valmynd

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Í valmyndinni finnurðu alla valkosti fyrir innflutning og útflutning skráa, auk þess að opna panel í appinu. Þar finnurðu einnig valkostinn til að heimila tölvuna með áskriftinni þinni (í _Liberation -> Authorise/Deauthorise this computer_).

#### Táknstika

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Hér finnurðu algeng verkefni, eins og að setja alla leysa í arm eða disarm, Global Brightness, test pattern og að skipta á milli 3D, Canvas og Output view

### Views

Stóra svæðið efst til vinstri á skjánum getur sýnt eina af þremur aðalstillingum: **3D**, **CANVAS** og **OUTPUT.** Skiptu á milli þeirra með hnöppunum á táknstikunni (eða notaðu `Tab` lykilinn til að skipta á milli 3D og OUTPUT view, og haltu síðan áfram að fara með tab í gegnum hvert úttak leysis í röð).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view sýnir hvernig leysarnir þínir munu líta út og hægt er að stilla það þannig að það passi við þína eigin leysauppsetningu. Smelltu og dragðu til að snúa myndavélinni, og notaðu skrunhjól músarinnar til að færa þig fram og til baka. Marga aðra valkosti finnurðu í spjaldinu _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Sjá [3D Visualiser](../setting-up/3d-visualiser.md "mention").

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view er notað til að stilla zones og masks fyrir hvern leysi. (Taktu eftir stóra númerinu efst í vinstra horninu svo þú sjáir auðveldlega hvaða leysi þú ert að vinna með!)

Þetta view er framsetning á öllu output frá þessum leysi og sýnir hvar hvert zone liggur innan þess. Sjálfgefið er aðeins eitt zone fyrir hvern leysi, en þú getur bætt við eins mörgum zones og er raunhæft, og þú sérð þau öll í þessu view.

{% hint style="info" %}
**Hvað er zone?**

Zone er svæði innan output frá leysi sem þú getur beint laser efni inn í. Þú getur haft fleiri en eitt zone fyrir hvern leysi. Einfaldasta gerðin er _beam_ zone, en einnig eru til _canvas_ zones og _DMX_ zones. Í þessum leiðbeiningum munum við aðallega fjalla um beam zones, sem eru yfirleitt notuð til að búa til geislaáhrif í loftinu.
{% endhint %}

Þú getur valið leysinn sem þú vilt breyta með því að nota annaðhvort:

* númeruðu hnappana á stikunni efst
* ýta á talnalykilinn fyrir leysinn sem þú vilt (_1-9 lyklar_)
* `Tab` lykilinn til að fara frá einum yfir í næsta

Bættu nýjum leysi við uppsetninguna með því að ýta á _+_ hnappinn. (Það er líka _ADD LASER_ hnappur í _Laser Overview_ spjaldinu)

Eyddu leysi úr uppsetningunni með því að ýta á rauða ⊖ hnappinn í _Laser Overview_ spjaldinu.

Þú getur þysjað inn og út með skrunhjóli músarinnar, og smellt og dregið hvar sem er þar sem ekki er zone til að færa view.

Smelltu á zone til að velja það og stilltu síðan hornpunktana með músinni. Haltu `Alt / Option` lyklinum inni á meðan þú dregur horn til að gera það ójafnt. Hægrismelltu á zone til að sjá fleiri valkosti, þar á meðal að breyta gerð zone.

Vinstra megin er stika með röð táknhnappa; haltu músinni yfir hvaða hnappi sem er til að fá lýsingu á því hvað hann gerir. Hnapparnir hér leyfa þér að bæta við beam zones, canvas zones og masks. Þar eru einnig valkostir til að setja test pattern aðeins fyrir þennan leysi, ásamt stillingum fyrir grid og snapping.

Nánar er fjallað um þetta í [Output-sýn](../output-view/ "mention").

#### Canvas

Canvas kerfið er aðallega notað fyrir grafík og byggingarkortlagningu. Þú getur dreift flóknum myndum yfir marga leysa og leiðrétt sjónarhorn fyrir hvern hluta. Sjá [Grafík og Canvas-kerfið](../graphics-and-the-canvas-system/ "mention").

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Þó að hægt sé að stjórna Liberation með mús og lyklaborði er miklu betra að nota APC40 MIDI control interface (Mark 2 er best, en Mark 1 virkar líka).

Sjá einnig: [APC40 tilvísun](../reference/apc40-reference.md "mention")

Liberation styður einnig APC Mini og MIDI Fighter Twister. APC40 Mark 2 er þó enn besti kosturinn í flestum tilvikum.&#x20;

### Clips og effects

{% hint style="info" %}
**Hvað er Clip?**

Clip er ílát fyrir hvers kyns laser efni í Liberation. Clips geta innihaldið geisla eða grafískar hreyfimyndir og eru yfirleitt lykkja sem endurtekur sig. Hægt er að beina þeim inn í hvaða zone sem er (eða _Canvas target area_) og þau eru ræst með Clip hnöppunum inni í Clip Deck.
{% endhint %}

#### Yfirlit yfir Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Þetta hnitanet kallast _Clip Deck_ og þar eru öll laser Clips geymd. Það er hannað til að samsvara beint 8 x 5 hnappanetinu á APC40.

**Að fara um Clip Deck.**

Þú getur skrunað Clip Deck til vinstri og hægri með:

* Vinstri og hægri örvalyklum. Bættu við `Cmd / Ctrl` til að skruna heila síðu í einu.
* Snertiplatta: Strjúktu
* Mús: ef músin þín styður hliðarskrun geturðu notað það þegar bendillinn er yfir Clip Deck
* APC40 scroll knob
* APC40 _<- DEVICE ->_ hnöppum

Til að hjálpa þér að átta þig er lítill visualiser fyrir Clip Deck efst. Sjá einnig [Clips og Clip Deck](../clips/ "mention")

#### Að ræsa og stöðva Clips

Ýttu á Clip hnapp (annaðhvort með músinni eða með APC40) til að ræsa Clip. Ýttu aftur til að stöðva það. Þegar þú ræsir Clip stöðvast öll önnur Clips í sama lit sjálfkrafa nema þú haldir _shift_ inni.

Sum Clips eru í _Flash mode_ (sjálfgefið þau rauðu), og þá stöðvast þau um leið og þú sleppir Clip hnappnum.

_STOP_ hnappurinn stöðvar öll Clips sem eru í gangi.

#### Að stilla output zones fyrir Clip

Undir Clip hnöppunum sérðu zone hnappana, sjálfgefið beam zones 1 til 8 (_BEAM 1_, _BEAM 2_ o.s.frv.). Zone hnapparnir lýsast upp til að sýna hvaða zones eru úthlutuð til Clip sem er valið núna.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Tveimur röðum fyrir neðan zone hnappana sérðu X/Y flip hnappana; kveiktu eða slökktu á þeim til að spegla Clip lárétt og lóðrétt.

{% hint style="info" %}
Athugaðu að þessar zone úthlutanir og X/Y flip stillingar tengjast Clip sjálfu; þær varðveitast næst þegar þú keyrir þetta Clip. Þetta er ekki global stilling.
{% endhint %}

Hægrismelltu á Clip til að breyta fleiri stillingum fyrir Clip. Sjá einnig [Clip stillingar](../clips/clip-settings.md "mention")

### Hópar

Þú tekur eftir því að hvert Clip hefur litaða útlínu, og liturinn sýnir í hvaða _hópi_ það er. APC40 Clip hnapparnir lýsast einnig upp í þessum lit.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Hópur 1</td><td>Blágrænn</td></tr><tr><td>Hópur 2</td><td>Appelsínugulur</td></tr><tr><td>Hópur 3</td><td>Rauður</td></tr><tr><td>Hópur 4</td><td>Indígóblár</td></tr><tr><td>Hópur 5</td><td>Grænn</td></tr></tbody></table>

Hópakerfið er mjög sveigjanlegt og gerir þér kleift að:

* Halda Clips í einum hópi í gangi á meðan þú kveikir og slekkur á hópum í öðrum
* Úthluta zones og X/Y flips fljótt til allra Clips innan hóps
* Setja _Flash mode_ fyrir Clip (Hópur 3 er sjálfgefið stilltur á _Flash mode_)

Hópar hafa einnig stillingar fyrir transition in/out sem Clips geta erft, eða sem hægt er að yfirskrifa.

Þú getur úthlutað hópi fyrir Clip með hnöppunum í hægrismellsvalmyndinni, eða með APC40 með því að ýta á hóphnappinn og, _á meðan honum er enn haldið inni,_ ýta á Clip hnappana.

Breyta zone stillingum fyrir öll Clips innan hóps

Með APC40 skaltu ýta á hóphnappinn og síðan, _á meðan honum er enn haldið inni,_ nota zone og X/Y hnappana til að kveikja eða slökkva á zone stillingum fyrir öll Clips innan þess hóps.

Sjá einnig [Hópar](../clips/groups.md "mention")

### Effects

Effects kerfið í Liberation er öflug og fjölhæf leið til að breyta output frá Clip í rauntíma. Sjálfgefnu effect hnapparnir 1-8 eru undir zone hnöppunum.

#### Að beita effect

Ýttu á effect hnapp til að kveikja eða slökkva á effect, eða enn betra, notaðu APC40 sleða 1-8 til að fade effects inn og út.

#### Effect parameters

Notaðu rotary controllers 1-8\* til að stilla _parameter_ fyrir hvert effect. (Einnig geturðu hægrismellt með músinni til að stilla level og parameter). Breyting á parameter gerir mismunandi hluti eftir því hvernig effect er sett upp. Sjá listann hér að neðan fyrir sjálfgefnu effects.

{% hint style="info" %}
Litlu tölurnar sem þú sérð á hnöppum fyrir áhrif vísa til _level_ og _parameter_ áhrifanna. _Level_ er stjórnað með fader á APC40 eða með því að smella og draga á hnappnum. Parameter er stillt með snúningshnöppunum á APC40 eða með því að hægrismella og stilla með músinni.
{% endhint %}

_\*Rotary controllers 1-8 eru efst á APC40 Mk2 og efst til hægri á Mk1. Sjá einnig:_ [APC40 tilvísun](../reference/apc40-reference.md "mention")

#### Sjálfgefnu effects

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Bætir óreiðukenndri hreyfingu við output frá Clip. Parameter stillir magn/hraða óreiðunnar.
2. **Sine wave** :\
   Sveigir allt efni yfir hreyfanlega sínusbylgju. Parameter stillir bylgjulengdina.
3. **Rotation** :\
   Snýr öllu í kring. Parameter stillir snúningshraðann.
4. **Horizontal flip** :\
   Þjappar og teygir allt lárétt. Parameter stillir hraðann.
5. **Scale** :\
   Skalar allt endurtekið frá fullri stærð niður í núll. Parameter stillir hraðann.
6. **Hue** :\
Breytir litblæ alls, en breytir ekki mettuninni (þ.e. allt sem er hvítt helst hvítt). Parameter stillir litblæinn.
7. **Saturation and hue** :\
Breytir litblæ alls og mettar litinn líka að fullu (þ.e. allt sem er hvítt breytist í litinn). Parameter stillir litblæinn.
8. **Flash** :\
   Lætur birtustig alls blikka endurtekið frá fullu niður í núll. Parameter stillir blikkhraðann.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Það eru 16 litaáhrif til viðbótar í neðstu röðinni til að beita forstilltum gildum fyrir litblæ og mettun.

Athugaðu að þetta eru sjálfgefnu effects, en hægt er að breyta þeim þannig að þau geri næstum hvað sem þú vilt!

#### Hvað er _Clip sem er valið núna_?

Þegar þú ræsir Clip lýsist það upp til að sýna að það sé virkt. Það hefur einnig hvíta útlínu sem sýnir að þetta er Clip sem er valið núna. Í hvert sinn sem þú kveikir eða slekkur á zone hnöppum eða breytir Clip stillingum eru þær breytingar settar á _Clip sem er valið núna_.

{% hint style="info" %}
Til að velja Clip án þess að ræsa það skaltu ýta á `Alt / Option` lykilinn áður en þú ýtir á Clip hnappinn. Þetta er góð leið til að stilla zones og aðrar stillingar án þess að keyra það.
{% endhint %}

### Clip settings panel

Notaðu _Clip Settings_ panel til að breyta scaling, X/Y position og fá aðgang að öfluga zone delay kerfinu.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global settings panel

Finndu _Global Settings_ panel til að stilla global output stillingar sem hafa áhrif á allt output yfir öll zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Kveiktu á AUTO RESET til að endurstilla allar _Global settings_ sjálfkrafa þegar engin Clips eru í spilun.&#x20;

### Tímasetning

Nánast allar leysissýningar hafa einhvers konar tónlist, svo tímasetningarkerfið í Liberation byggir á tempo í slögum á mínútu. Í _Tempo Panel_ sérðu framsetningu á tímanum; hver ferningur táknar einn slag og þú sérð þá blikka í takt.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Það eru margar samstillingarleiðir, þar á meðal MIDI clock og Ableton Link. Ef þú veist tempo tónlistarinnar geturðu stillt það handvirkt með sleðanum á skjánum eða APC40 Tempo knob, en þú getur líka haldið takti við tónlistina með _Tap Tempo_ kerfinu.

#### Tap Tempo

_Tap Tempo_ er hugtak sem er algengt í tónlistarforritum og gerir þér kleift að slá inn taktinn til að setja tempo á meðan tónlistin spilar. Þú getur notað hnappinn á skjánum, en mælt er með að nota _T_ lykilinn eða _Tap Tempo_ hnappinn á APC40 (eða jafnvel fótrofa ef þú vilt).

Ýttu á _R_ lykilinn eða _Metronome_ hnappinn (APC40) til að endurstilla tempo á byrjun taktsins.

Ýttu á _Y_ lykilinn eða snúðu _Tempo_ knob(APC40) til að rúnna tempo að heilli tölu. Þetta getur verið gagnlegt fyrir raftónlist, þar sem algengt er að slög á mínútu séu heil tala.

### Að skipuleggja Clip Deck

Til að færa Clip á Clip Deck skaltu smella og draga það á nýjan stað. Á meðan þú dregur geturðu notað örvalyklana (eða scroll wheel/buttons á APC40) til að skruna til vinstri og hægri.

Haltu `Alt / Option` lyklinum inni á meðan þú dregur til að búa til afrit.

`Alt / Option`-smelltu á Clip til að velja það án þess að ræsa það.

`Alt / Option + Shift`-smelltu á Clip til að velja mörg, eða smelltu og dragðu utan við Clip til að nota „lasso“ val.&#x20;

Smelltu og dragðu til að draga ÖLL valin Clips.

Til að eyða einu eða fleiri Clips geturðu annaðhvort dregið þau út af Clip Deck (ruslatunnutákn birtist) eða notað DELETE hnappinn í hægrismellsvalmynd Clip.

### Laser Overview panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser Overview panel_ gefur þér fljótlegt yfirlit yfir stöðu leysanna sem eru í gangi. Græni ferningurinn hægra megin sýnir að laser controller sé í lagi. Ef hann verður appelsínugulur eru einstaka truflanir, og ef hann verður rauður hefur sambandið rofnað. Ef hann er grár er hann ekki tengdur við controller.&#x20;

Grafið í miðjunni sýnir sögu rammatíma, og talan hægra megin er núverandi rammatíðni. Því flóknara sem efnið er, því hægari verður rammatíðnin (þ.e. meira flökt). Allt undir um það bil 25fps byrjar að líta svolítið flöktandi út.&#x20;

### Tenging við leysa - Controller Assignment panel

Smelltu á _Assign Laser Controllers_ hnappinn til að opna _Controller Assignment_ panel. (Þú getur líka nálgast þennan panel í gegnum _View -> Controller Assignment_ á valmyndastikunni).

Hér geturðu valið hvaða laser outputs fara í hvaða laser controllers. Dragðu controllers af listanum til hægri og slepptu þeim í reitina til vinstri. Þú getur endurnefnt controllers þannig að nöfnin passi við leysinn sem þeir eru paraðir við (notaðu hnappinn með pennatákninu).

Lestu kaflann [Úthlutun laser controller](../setting-up/controller-assignment.md "mention") fyrir nánari upplýsingar.

{% hint style="danger" %}
Áður en þú setur einhverja leysa í arm skaltu fara yfir kaflann [Uppsetning leysa](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Laser output panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Þessi panel sýnir stillingar fyrir _currently selected laser_ (táknað með númerinu efst). Breyttu því hvaða leysir er valinn með _tab_ lyklinum, með því að ýta á talnalykil, smella á leysinúmer í _Laser Overview_ panel eða í _Output view._

* **Number button** setur leysinn í arm eða disarm; ef hann er rauður er leysirinn armed.
* **Brightness** stillir birtu leysisins óháð hinum leysunum (og sameinast _Global Brightness_ stillingunni - þ.e. ef báðar eru 50% verður leysirinn þinn á 25%).
* **Test Pattern** kveikir á test pattern aðeins fyrir þennan leysi (yfirskrifar global test pattern stillinguna)
* **Orientation** leiðréttir fyrir leysa sem eru hengdir upp á hlið eða á hvolfi.
* **Flip Horizontal and Flip Vertical** snýr output frá leysinum við. Gagnlegt til að leiðrétta output á leysum sem eru ekki víraðir eins.
* **Copy Laser Settings** opnar panel sem gerir þér kleift að afrita ýmsar stillingar frá þessum leysi yfir á aðra.

### Scanner settings

Sýningarleysar virka þannig að einum leysigeisla er hreyft mjög hratt og kveikt og slökkt á honum til að teikna form í loftinu. Það sem þú sérð sem línur, form og myndir er í raun geislinn að rekja slóðir hraðar en augun þín ná að fylgja.

Point stream eru gögnin sem segja leysinum hvert hann á að hreyfast næst og hvenær geislinn á að vera kveiktur eða slökktur. Í Liberation er Clips breytt í þennan point stream í rauntíma þegar þau eru send til leysanna.

Liberation gefur þér nákvæma stjórn á því hvernig þessi point stream er búinn til, svo þú getir jafnað mýkt, birtu og afköst fyrir hvern leysi.

{% hint style="info" %}
Ef þú ert vön eldri leysihugbúnaði sem reiðir sig á fyrirfram útreiknaða point streams gæti þessi nálgun virst öðruvísi í fyrstu. Rauntíma point generation gerir hins vegar kleift að fínstilla sama efni á mismunandi hátt fyrir hvern leysi. Þetta auðveldar vinnu með marga leysa sem hafa mismunandi scanner hraða eða gæði, án þess að afrita eða endurbyggja efni. Þetta heldur Clip skrám líka mjög litlum, og þess vegna er allt sjálfgefna Clip Deck í Liberation aðeins nokkur megabæti í stað gígabæta.
{% endhint %}

Grunnstillingar scanner eru:

* **Speed** er hraði skannanna, þ.e. hversu hratt leysirinn hreyfist til að teikna form. Þetta samsvarar því að stilla point rate í hefðbundnum leysihugbúnaði, en í Liberation geturðu breytt því hversu hratt leysirinn hreyfist _óháð point rate._ Þú ættir ekki að þurfa að breyta þessu.
* **Scanner sync** (stundum kallað _blank shift, áður Colour Shift_) Skannarnir hreyfa leysinn mjög hratt, en yfirleitt er breyting á birtu og lit ekki í takt við hreyfinguna. Þetta birtist sem litlir flöktandi „halar“ af ljósi á jaðri geisla og lína. Notaðu þessa stillingu til að samstilla hreyfingu og lit. Sjá [Laser Settings](../setting-up/laser-settings.md "mention")

Aðrar ítarlegar scanner stillingar eru útskýrðar í kaflanum [Ítarlegt](../advanced/ "mention").

### Zoning

Fyrir heildarleiðbeiningar um uppsetningu og zoning leysa, sjá: [Uppsetning leysa](../setting-up/setting-up-lasers.md "mention")
