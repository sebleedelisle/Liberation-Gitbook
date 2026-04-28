---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Flýtileiðarvísir

## Inngangur

Velkomin(n) í **Liberation** - næstu kynslóð hugbúnaðar fyrir lasersýningar.

Liberation er öflugur og flókinn nútímahugbúnaður; hann er byggður á notendavænni hönnun og áreiðanleika til að gefa þér frelsi til að tjá sköpunargáfuna. Hann er hraður, skilvirkur og hnökralaus; fylgdu þessum _flýtileiðarvísi_ til að komast hratt af stað!

### Umsjón með leysum

Liberation er nógu sveigjanlegt til að þú getir sett upp leysa og séð þá í sjónhermi án þess að raunverulegir leysar séu tengdir. Þegar þú ert síðan tilbúin(n) geturðu úthlutað hverju úttaki hnökralaust á laser controller.

{% hint style="info" %}
Þú getur sett upp og séð eins marga leysa og þú vilt innan Liberation. Leyfisstigin (Hobbyist, Pro o.s.frv.) takmarka aðeins fjölda leysa sem þú getur _virkjað_. Þetta þýðir að þú getur hannað lasersýningar með 100 leysum jafnvel með ókeypis leyfi. Þú þarft aðeins að uppfæra þegar kemur að því að keyra sýninguna á raunverulegum leysum.
{% endhint %}

Sjálfgefna uppsetningin er með 8 leysa sem raðast lárétt, en þú getur sérsniðið þetta eins og þú vilt. Líklega er best að halda þessari sjálfgefnu uppsetningu meðan þú ert að kynnast hugbúnaðinum, og stilla hana svo síðar til að passa við þinn búnað. (Sjá [setting-up-your-project.md](setting-up/setting-up-your-project.md))

{% hint style="warning" %}
Mikilvægt: Áður en þú virkjar einhverja leysa skaltu ganga úr skugga um að þú skiljir áhættuna og fara vandlega í gegnum kaflann [setting-up-lasers.md](setting-up/setting-up-lasers.md).
{% endhint %}

## Yfirlit yfir hugbúnaðinn

### Neyðarstöðvun

Alltaf þegar þú keyrir leysa þarftu að hafa **líkamlegan neyðarstöðvunarhnapp** við höndina (sjá [emergency-stop-interlocks.md](hardware/emergency-stop-interlocks.md)), en ef þú vilt afvirkja allt án jafn mikillar neyðar geturðu notað hnappinn _**DISARM ALL**_, eða `Escape`-lykilinn (eða _**SESSION**_-lykilinn á APC40). Þú getur líka lækkað heildarbirtustigið með rennistikunni á skjánum eða aðalfadernum á APC40.

### Rennistikur og stýringar

Í Liberation eru ýmsar rennistikur og stýringar.

{% hint style="info" %}
`Cmd / Ctrl`-smelltu á rennistiku til að slá inn nýtt gildi ef þú þarft meiri nákvæmni en rennistikan býður upp á.
{% endhint %}

### Flýtilyklar

Heildarlista yfir flýtilykla má finna hér: [keyboard-shortcuts.md](reference/keyboard-shortcuts.md)

### Uppsetning skjásins

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Ertu ekki viss hvað ákveðinn hnappur gerir? Færðu músina yfir hann til að fá lýsingu!
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Í valmyndinni finnurðu alla valkosti fyrir innflutning og útflutning skráa, og til að opna spjöld. Hér finnurðu líka valkostinn til að heimila tölvuna með áskriftinni þinni (í _Liberation -> Authorise/Deauthorise this computer_).

#### Icon bar

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Hér finnurðu algeng verkefni, eins og að virkja/afvirkja alla leysa, heildarbirtustig, prófunarmynstur og að skipta á milli 3D, Canvas og Output sýna.

### Sýnir

Stóra svæðið efst til vinstri á skjánum getur verið ein af 3 aðalsýnum; **3D**, **CANVAS** og **OUTPUT.** Skiptu á milli þeirra með hnöppunum á icon bar (eða notaðu `Tab`-lykilinn til að skipta á milli 3D og OUTPUT sýna, og haltu svo áfram að flakka með Tab í gegnum hvert laser output fyrir sig).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D-sýnin sýnir þér hvernig leysarnir munu líta út og hægt er að stilla hana þannig að hún passi við þína eigin laseruppsetningu. Smelltu og dragðu til að snúa myndavélinni, notaðu músarhjólið til að færa þig fram og til baka. Þú finnur marga aðra valkosti í spjaldinu _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Sjá [3d-visualiser.md](setting-up/3d-visualiser.md).

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output View er notað til að stilla svæði og grímur fyrir hvern leysi. (Taktu eftir risastóru tölunni efst í vinstra horninu svo þú sjáir auðveldlega á hvaða leysi þú ert!)

Þessi sýn er framsetning á öllu úttaki þessa leysis og hvar hvert svæði liggur innan þess. Sjálfgefið er aðeins eitt svæði á hvern leysi, en þú getur bætt við eins mörgum svæðum og er raunhæft, og þú sérð þau öll í þessari sýn.

{% hint style="info" %}
**Hvað er svæði?**

Svæði er rými innan úttaks leysis sem þú getur beint laser content inn í. Þú getur haft fleiri en eitt svæði á hverjum leysi. Einfaldasta gerð svæðis er _beam_ zone, en það eru líka _canvas_ zones og _DMX_ zones. Í þessum leiðarvísi einbeitum við okkur aðallega að beam zones, sem eru yfirleitt notuð til að búa til geislaáhrif í loftinu.
{% endhint %}

Þú getur valið leysinn sem þú vilt breyta með því að nota annaðhvort:

* tölusettu hnappana á stikunni efst
* ýta á talnalykilinn fyrir leysinn sem þú vilt _(1-9_ keys\_)\_
* `Tab`-lykilinn til að fara í röð frá einum til næsta

Bættu nýjum leysi við uppsetninguna með því að ýta á _+_ hnappinn. (Það er líka _ADD LASER_ hnappur í spjaldinu _Laser Overview_)

Eyddu leysi úr uppsetningunni með því að ýta á rauða ⊖ hnappinn í spjaldinu _Laser Overview_.

Þú getur þysjað inn og út með músarhjólinu og smellt og dregið hvar sem er þar sem ekkert svæði er til að færa sýnina.

Smelltu á svæði til að velja það og stilltu síðan hornpunkta þess með músinni. Notaðu `Alt / Option`-lykilinn á meðan þú dregur horn til að gera það ójafnt. Hægrismelltu á svæðið til að sjá fleiri valkosti, þar á meðal að breyta gerð svæðisins.

Vinstra megin er stika með röð af táknhnöppum; færðu músina yfir hvaða hnapp sem er til að fá lýsingu á því hvað hann gerir. Hnapparnir hér leyfa þér að bæta við beam zones, canvas zones og grímum. Þar eru líka valkostir til að stilla prófunarmynstur aðeins fyrir þennan leysi, ásamt stillingum fyrir hnitakerfi og snapping.

Nánari upplýsingar eru í [output-view](output-view/).

#### Canvas

Canvas-kerfið er aðallega notað fyrir grafík og arkitektúr-möppun. Þú getur dreift flóknum myndum yfir marga leysa og leiðrétt sjónarhorn fyrir hvern hluta. Sjá [graphics-and-the-canvas-system](graphics-and-the-canvas-system/).

### APC40 MIDI controller

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Þó það sé hægt að stjórna Liberation með mús og lyklaborði er mun betra að nota APC40 MIDI control interface (Mark 2 er best, en Mark 1 virkar líka).

Sjá einnig: [apc40-reference.md](reference/apc40-reference.md)

Við höfum nú einnig innleitt stuðning við APC Mini Mark 2 og MIDI Fighter Twister, og fleiri tæki eru í þróun. APC40 Mark 2 er þó besti kosturinn í flestum tilvikum.

### Clips og áhrif

{% hint style="info" %}
**Hvað er clip?**

Clip er ílát fyrir allt laser content innan Liberation. Clips geta innihaldið geisla eða grafískar hreyfimyndir og eru yfirleitt lykkja sem endurtekur sig. Hægt er að beina þeim í hvaða svæði sem er (eða _Canvas target area_) og þau eru ræst með clip-hnöppunum inni í Clip Deck.
{% endhint %}

#### Yfirlit yfir Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Þetta hnitanet kallast _Clip Deck_ og þar eru öll laser clips geymd. Það er hannað til að samsvara beint 8 x 5 hnappanetinu á APC40.

**Að rata um Clip Deck.**

Þú getur skrunað Clip Deck til vinstri og hægri með því að nota:

* Vinstri og hægri örvalykla. Bættu við `Cmd / Ctrl` til að skruna heila síðu í einu.
* Snertiflöt: Strjúktu
* Mús: ef músin þín er með hliðarskrun geturðu notað það þegar bendillinn er yfir Clip Deck
* APC40 scroll knob
* APC40 _<- DEVICE ->_ hnappar

Til að hjálpa þér að átta þig er lítill sjónhermir af Clip Deck efst. Sjá einnig [clips](clips/)

#### Að ræsa og stöðva clips

Ýttu á clip-hnapp (annaðhvort með músinni eða APC40) til að ræsa clip. Ýttu aftur til að stöðva það. Þegar þú ræsir clip stöðvast öll önnur clips í sama lit sjálfkrafa nema þú haldir inni _shift_.

Sum clips eru í _Flash mode_ (sjálfgefið þau rauðu), og þá stöðvast þau um leið og þú sleppir clip-hnappinum.

_STOP_ hnappurinn stöðvar öll clips sem eru í gangi.

#### Að stilla úttakssvæði fyrir clip

Undir clip-hnöppunum sérðu svæðishnappana, sjálfgefið beam zones 1 til 8 (_BEAM 1_, _BEAM 2_ o.s.frv.). Svæðishnapparnir lýsast upp til að sýna hvaða svæðum er úthlutað á það clip sem er valið hverju sinni.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Tveimur röðum neðan við svæðishnappana sérðu X/Y flip-hnappana; kveiktu eða slökktu á þeim til að spegla clip lárétt og lóðrétt.

{% hint style="info" %}
Athugaðu að þessar svæðisúthlutanir og X/Y flip stillingar tengjast sjálfu clip-inu; þær haldast næst þegar þú keyrir það clip. Þetta er ekki almenn stilling.
{% endhint %}

Hægrismelltu á clip til að breyta fleiri stillingum fyrir það. Sjá einnig [clip-settings.md](clips/clip-settings.md)

### Groups

Þú tekur eftir því að hvert clip er með litaða útlínu, og þessi litur sýnir í hvaða _group_ það er. APC40 clip-hnapparnir lýsast líka upp í þessum lit.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Blágrænn</td></tr><tr><td>Group 2</td><td>Appelsínugulur</td></tr><tr><td>Group 3</td><td>Rauður</td></tr><tr><td>Group 4</td><td>Indígó</td></tr><tr><td>Group 5</td><td>Grænn</td></tr></tbody></table>

Group-kerfið er mjög sveigjanlegt og gerir þér kleift að:

* Halda clips í einum group gangandi á meðan þú kveikir og slekkur á groups í öðrum
* Úthluta svæðum og X/Y flip fljótt á öll clips innan sama group
* Stilla _Flash mode_ fyrir clip (Group 3 er sjálfgefið stillt á _Flash mode_)

Groups hafa líka stillingar fyrir transition inn/út sem clips geta erft eða yfirskrifað.

Þú getur úthlutað group fyrir clip með hnöppunum í hægrismellsvalmyndinni, eða með APC40 með því að ýta á group-hnappinn og, _á meðan honum er enn haldið inni,_ ýta á clip-hnappana.

Breyta svæðisstillingum fyrir öll clips innan group

Með APC40 ýtirðu á group-hnappinn og notar svo, _á meðan honum er enn haldið inni,_ svæðis- og X/Y-hnappana til að kveikja eða slökkva á svæðisstillingum fyrir öll clips innan þess group.

Sjá einnig [groups.md](clips/groups.md)

### Áhrif

Áhrifakerfið í Liberation er öflug og fjölhæf leið til að breyta clip-úttaki í rauntíma. Sjálfgefnu áhrifahnapparnir 1-8 eru undir svæðishnöppunum.

#### Að beita áhrifum

Ýttu á áhrifahnapp til að kveikja eða slökkva á áhrifinu, eða enn betra, notaðu APC40 sleðana 1-8 til að fade-a áhrif inn og út.

#### Færibreytur áhrifa

Notaðu snúningsstýringar 1-8\* til að stilla _parameter_ fyrir hvert áhrif. (Eða þú getur hægrismellt með músinni til að stilla level og parameter). Breyting á parameter gerir mismunandi hluti eftir því hvernig áhrifin eru sett upp. Sjá listann hér fyrir neðan yfir sjálfgefnu áhrifin.

{% hint style="info" %}
Litlu tölurnar sem þú sérð á áhrifahnöppunum vísa til _level_ og _parameter_ áhrifanna. _Level_ er stjórnað með fadernum á APC40 eða með því að smella og draga á hnappinum. Parameter er stillt með snúningsstýringunum á APC40 eða með því að hægrismella og stilla með músinni.
{% endhint %}

_\*Snúningsstýringar 1-8 eru efst á APC40 Mk2 og efst til hægri á Mk1. Sjá einnig:_ [apc40-reference.md](reference/apc40-reference.md)

#### Sjálfgefnu áhrifin

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Bætir óreiðukenndri hreyfingu við clip-úttakið. Parameter stillir magn/hraða óreiðunnar.
2. **Sine wave** :\
   Sveigir allt efni eftir hreyfanlegri sínusbylgju. Parameter stillir bylgjulengdina.
3. **Rotation** :\
   Snýr öllu í hring. Parameter stillir snúningshraðann.
4. **Horizontal flip** :\
   Þjappar og teygir allt lárétt. Parameter stillir hraðann.
5. **Scale** :\
   Skalar allt endurtekið frá fullri stærð niður í núll. Parameter stillir hraðann.
6. **Hue** :\
   Breytir hue á öllu, en breytir ekki mettuninni (þ.e. allt sem er hvítt helst hvítt). Parameter stillir hue.
7. **Saturation and hue** :\
   Breytir hue á öllu og mettar litinn líka að fullu (þ.e. allt sem er hvítt breytist í litinn). Parameter stillir hue.
8. **Flash** :\
   Blikkar birtustigi alls endurtekið frá fullu niður í núll. Parameter stillir blikkhraðann.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Það eru 16 litáhrif til viðbótar í neðstu röðinni til að beita fyrirfram stilltum hue- og mettunargildum.

Athugaðu að þetta eru sjálfgefnu áhrifin, en hægt er að breyta þeim til að gera nánast hvað sem þú vilt!

#### Hvað er _„currently selected clip“_?

Þegar þú ræsir clip lýsist það upp til að sýna að það sé virkt. Það er líka með hvíta útlínu í kringum sig sem sýnir að þetta er clip-ið sem er _selected_ hverju sinni. Þegar þú kveikir eða slekkur á svæðishnöppum eða stillir clip-stillingar, þá eru þær breytingar notaðar á _currently selected clip._

{% hint style="info" %}
Til að velja clip án þess að ræsa það skaltu ýta á `Alt / Option`-lykilinn áður en þú ýtir á clip-hnappinn. Þetta er góð leið til að stilla svæði þess og aðrar stillingar án þess að keyra það.
{% endhint %}

### Clip Settings panel

Notaðu _Clip Settings_ spjaldið til að breyta skölun, X/Y staðsetningu og fá aðgang að öfluga zone delay kerfinu.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings panel

Finndu _Global Settings_ spjaldið til að stilla almennar úttaksstillingar sem hafa áhrif á allt úttak á öllum svæðum.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Kveiktu á AUTO RESET til að endurstilla sjálfkrafa allar _Global settings_ þegar engin clips eru í spilun.

### Tímasetning

Nánast allar lasersýningar hafa einhvers konar tónlistarundirleik, þannig að tímasetningarkerfið í Liberation byggir á tempói í slögum á mínútu. Í _Tempo Panel_ geturðu séð framsetningu tímans; hver ferningur táknar eitt slag og þú sérð þá blikka í takt.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Það eru margir samstillingarvalkostir, þar á meðal MIDI clock og Ableton Link. Ef þú þekkir tempó tónlistarinnar geturðu stillt það handvirkt með rennistikunni á skjánum eða APC40 Tempo knob, en þú getur líka haldið takti við tónlistina með _Tap Tempo_ kerfinu\_.\_

#### Tap Tempo

_Tap Tempo_ er hugtak sem er mikið notað í tónlistarforritum og gerir þér kleift að slá taktinn inn á meðan tónlistin spilar til að stilla tempóið. Þú getur notað hnappinn á skjánum, þó mælt sé með að nota _T_ lykilinn eða _Tap Tempo_ hnappinn á APC40 (eða jafnvel fótpedal ef þú vilt).

Ýttu á _R_ lykilinn eða _Metronome_ hnappinn (APC40) til að endurstilla tempóið á upphaf taktsins.

Ýttu á _Y_ lykilinn eða snúðu _Tempo_ knob(APC40) til að námunda tempóið að heilli tölu. Þetta getur verið gagnlegt fyrir raftónlist, sem er oft með heiltölu í slögum á mínútu.

### Að skipuleggja Clip Deck

Til að færa clip á Clip Deck smellirðu og dregur það á nýjan stað. Á meðan þú dregur geturðu notað örvalyklana (eða scroll wheel/buttons á APC40) til að skruna til vinstri og hægri.

Ýttu á `Alt / Option`-lykilinn á meðan þú dregur til að búa til afrit.

`Alt / Option`-smelltu á clip til að velja það án þess að ræsa það.

`Alt / Option + Shift`-smelltu á clip til að fjölvelja, eða smelltu og dragðu utan við clip til að velja með „lasso“.

Smella og draga dregur ÖLL valin clips.

Til að eyða einu eða fleiri clips geturðu annaðhvort dregið þau út af Clip Deck (ruslatunnutákn birtist) eða notað DELETE hnappinn í hægrismellsvalmynd clip.

### Laser Overview panel

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser Overview panel_ gefur þér fljótlegt yfirlit yfir stöðu leysanna sem eru í gangi. Græni ferningurinn til hægri sýnir að laser controller sé í góðu lagi. Ef hann verður appelsínugulur eru einstaka rof í sendingu, og ef hann verður rauður hefur tengingin rofnað. Ef hann er grár er hann alls ekki tengdur við controller.

Grafið í miðjunni sýnir sögu rammalengda og talan til hægri er núverandi rammatíðni. Því flóknara sem efnið er, því hægari verður rammatíðnin (þ.e. meira flökt). Allt undir um það bil 25fps fer að líta dálítið flöktandi út.

### Að tengjast leysum - Controller Assignment panel

Smelltu á _Assign Laser Controllers_ hnappinn til að opna _Controller Assignment_ spjaldið. (Þetta spjald er líka aðgengilegt í gegnum _View -> Controller Assignment_ í valmyndastikunni).

Hér geturðu valið hvaða laser outputs fara á hvaða laser controllers. Dragðu og slepptu controllers úr listanum til hægri inn í reitina til vinstri. Þú getur endurnefnt controllers til að passa við leysinn sem þeir eru paraðir við (notaðu pennatáknhnappinn).

Lestu kaflann [controller-assignment.md](setting-up/controller-assignment.md) fyrir nánari upplýsingar.

{% hint style="danger" %}
Áður en þú virkjar einhverja leysa skaltu ganga í gegnum kaflann [setting-up-lasers.md](setting-up/setting-up-lasers.md).
{% endhint %}

### Laser Output panel

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Þetta spjald sýnir þér stillingar fyrir _currently selected laser_ (sem er táknaður með tölunni efst). Breyttu hvaða leysir er valinn með _tab_ lyklinum, með því að ýta á talnalykil, smella á leysitölu í _Laser Overview_ spjaldinu eða í _output view._

* **Number button** virkjar og afvirkjar leysinn; ef hann er rauður er leysirinn virkjaður.
* **Brightness** stillir birtustig leysis óháð hinum leysunum (og það er sameinað _global brightness_ stillingunni - þ.e. ef bæði eru í 50%, verður leysirinn þinn í 25%).
* **Test Pattern** kveikir á prófunarmynstri aðeins fyrir þennan leysi (yfirskrifar almenna prófunarmynstursstillingu)
* **Orientation** leiðréttir fyrir leysa sem eru hengdir upp á hlið eða á hvolfi.
* **Flip Horizontal and Flip Vertical** speglar úttak leysisins. Gagnlegt til að leiðrétta úttak á leysum sem eru tengdir með ósamræmdum hætti.
* **Copy Laser Settings** opnar spjald sem gerir þér kleift að afrita ýmsar stillingar frá þessum leysi yfir á aðra.

### Scanner settings

Sýningarleysar virka þannig að einn lasergeisli er hreyfður mjög hratt og kveikt og slökkt á honum til að teikna form í loftið. Það sem þú sérð sem línur, form og myndir er í raun geislinn að rekja slóðir hraðar en augun þín ná að fylgja eftir.

Point stream er gögnin sem segja leysinum hvert hann á að fara næst og hvenær geislinn á að vera kveiktur eða slökktur. Í Liberation er clips umbreytt í þennan point stream í rauntíma þegar þau eru send til leysanna.

Liberation gefur þér nákvæma stjórn á því hvernig þessi point stream er myndaður, svo þú getir jafnað sléttleika, birtustig og afköst fyrir hvern leysi.

{% hint style="info" %}
Ef þú ert vön/vanur eldri laserhugbúnaði sem byggir á fyrirfram útreiknuðum point streams getur þessi nálgun virst öðruvísi í fyrstu. Rauntíma point generation gerir hins vegar kleift að fínstilla sama efni á mismunandi hátt fyrir hvern leysi. Þetta auðveldar vinnu með marga leysa sem hafa mismunandi scanner-hraða eða gæði, án þess að tvírita eða endurbyggja efni. Það heldur líka clip-skrám mjög litlum, sem er ástæðan fyrir því að allt sjálfgefna Liberation Clip Deck er aðeins nokkur megabæti í stað gígabæta.
{% endhint %}

Grunnstillingar scanner eru:

* **Speed** er scanner-hraðinn, þ.e. hversu hratt leysirinn hreyfist til að teikna form. Þetta samsvarar því að stilla point rate í hefðbundnum laserhugbúnaði, en í Liberation geturðu breytt því hversu hratt leysirinn hreyfist _óháð point rate._ Þú ættir ekki að þurfa að breyta þessu.
* **Scanner sync** (stundum þekkt sem _blank shift, áður Colour Shift_) Scanner hreyfa leysinn mjög hratt, en venjulega eru breytingar á birtu og lit ekki í takt við hreyfinguna. Þetta birtist sem litlir flöktandi „halar“ af ljósi við jaðar geisla og lína. Notaðu þessa stillingu til að samstilla hreyfingu og lit. Sjá [laser-settings.md](setting-up/laser-settings.md)

Fjallað er um aðrar ítarlegar scanner-stillingar í kaflanum [advanced](advanced/).

### Svæðaskipting

Fyrir heildarleiðbeiningar um uppsetningu og svæðaskiptingu leysa, sjá: [setting-up-lasers.md](setting-up/setting-up-lasers.md)
