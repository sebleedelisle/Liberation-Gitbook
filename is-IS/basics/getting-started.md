# ✅ Flýtileiðbeiningar til að byrja

## Inngangur

Velkomin(n) í **Liberation** - næstu kynslóð hugbúnaðar fyrir lasersýningar.

Liberation er öflugur og flókinn nútímahugbúnaður; hann er byggður á traustum grunni nothæfis og áreiðanleika til að gefa þér frelsi til að tjá sköpunargáfuna. Hann er hraður, skilvirkur og hnökralaus; fylgdu þessum _flýtileiðbeiningum_ til að komast fljótt af stað!

### Umsjón með laserum

Liberation er nógu sveigjanlegt til að þú getir sett upp lasera og séð þá fyrir þér án þess að nokkrir raunverulegir laserar séu tengdir. Þegar þú ert svo tilbúin(n) geturðu úthlutað hverju Output hnökralaust á laserstýringu.

{% hint style="info" %}
Þú getur sett upp og myndgert eins marga lasera og þú vilt í Liberation. Leyfisþrepin (Hobbyist, Pro o.s.frv.) takmarka aðeins fjölda lasera sem þú getur _arm._ Þetta þýðir að þú getur hannað lasersýningar með 100 laserum jafnvel með ókeypis leyfi. Þú þarft aðeins að uppfæra þegar kemur að því að keyra sýninguna á raunverulegum laserum.
{% endhint %}

Sjálfgefið eru 8 laserar raðaðir lárétt, en þú getur sérsniðið þetta eins og þú vilt. Líklega er best að halda þessari sjálfgefnu uppsetningu á meðan þú kynnist hugbúnaðinum og laga hana síðar að vélbúnaðaruppsetningunni þinni. (Sjá [setting-up-your-project.md](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Mikilvægt: Áður en þú arm nokkra lasera skaltu ganga úr skugga um að þú skiljir áhættuna og fara vandlega yfir kaflann [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

## Yfirlit yfir hugbúnaðinn

### Öryggisstöðvun

Alltaf þegar þú keyrir lasera verður þú að hafa **hardware emergency stop button** við höndina (sjá [emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md)), en ef þú vilt disarm allt án jafn mikillar neyðar geturðu notað _**DISARM ALL**_ hnappinn eða `Escape` takkann (eða _**SESSION**_ takkann á APC40). Þú getur líka lækkað heildarbirtu með sleðanum á skjánum eða aðal fader á APC40.

### Sleðar og stýringar

Í Liberation eru ýmsir sleðar og stýringar.

{% hint style="info" %}
`Cmd / Ctrl`-smelltu á sleða til að slá inn nýtt gildi ef þú þarft meiri nákvæmni en sleðinn býður upp á.
{% endhint %}

### Flýtilyklar

Heildarlisti yfir flýtilykla er hér: [keyboard-shortcuts.md](../reference/keyboard-shortcuts.md)

### Skjáuppsetning

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Ertu ekki viss hvað tiltekinn hnappur gerir? Haltu músinni yfir honum til að fá lýsingu!
{% endhint %}

#### Valmynd

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Í valmyndinni finnur þú alla valkosti fyrir innflutning og útflutning skráa, auk þess að opna panels. Hér finnur þú líka valkostinn til að heimila tölvuna með áskriftinni þinni (í _Liberation -> Authorise/Deauthorise this computer_).

#### Táknstika

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Hér finnur þú algeng verk, eins og að arming/disarming alla lasera, global brightness, test pattern og að skipta á milli 3D, Canvas og Output views

### Views

Stóra svæðið efst til vinstri á skjánum getur verið eitt af 3 megin views; **3D**, **CANVAS** og **OUTPUT.** Skiptu á milli þeirra með hnöppunum á táknstikunni (eða notaðu `Tab` takkann til að skipta á milli 3D og OUTPUT views og haltu svo áfram að fletta með tab í gegnum hvert laser output fyrir sig).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view sýnir hvernig laserarnir þínir munu líta út og hægt er að stilla það þannig að það passi við þína eigin laseruppsetningu. Smelltu og dragðu til að snúa myndavélinni, notaðu músarhjólið til að færa þig fram og til baka. Þú finnur marga aðra valkosti í _3D Visualiser settings_ panel (_View -> 3D Visualiser Settings_). Sjá [3d-visualiser.md](../setting-up/3d-visualiser.md).

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view er notað til að stilla zones og masks fyrir hvern laser. (Taktu eftir risastóra númerinu efst í vinstra horninu svo þú sjáir auðveldlega á hvaða laser þú ert!)

Þetta view er framsetning á öllu output þessa lasers og hvar hver zone er staðsett innan þess. Sjálfgefið er aðeins ein zone á hvern laser, en þú getur bætt við eins mörgum zones og er raunhæft, og þú sérð þær allar í þessu view.

{% hint style="info" %}
**Hvað er zone?**

Zone er svæði innan output lasers sem þú getur beint laser content inn á. Þú getur líka haft fleiri en eina zone á hvern laser. Einfaldasta gerð zone er _beam_ zone, en einnig eru til _canvas_ zones og _DMX_ zones. Í þessum leiðbeiningum einbeitum við okkur aðallega að beam zones, sem eru yfirleitt notaðar til að búa til andrúmslofts beam effects í loftinu.
{% endhint %}

Þú getur valið laserinn sem þú vilt breyta með því að nota annaðhvort:

* númeruðu hnappana á stikunni efst
* ýta á númeratakkann fyrir laserinn sem þú vilt _(1-9_ keys\_)\_
* `Tab` takkann til að fletta frá einum yfir í þann næsta

Bættu nýjum laser við uppsetninguna með því að ýta á _+_ hnappinn. (Það er líka _ADD LASER_ hnappur í _Laser Overview_ panel)

Eyddu laser úr uppsetningunni með því að ýta á rauða ⊖ hnappinn í _Laser Overview_ panel.

Þú getur stækkað og minnkað með skrunhjóli músarinnar og smellt og dregið hvar sem engin zone er til að færa view.

Smelltu á zone til að velja hana og stilltu svo hornpunktana með músinni. Notaðu `Alt / Option` takkann á meðan þú dregur horn til að gera það ójafnt. Hægrismelltu á zone til að sjá fleiri valkosti, þar á meðal að breyta gerð zone.

Vinstra megin er stika með röð táknhnappa; haltu músinni yfir hvaða hnappi sem er til að fá lýsingu á því hvað hann gerir. Hnapparnir hér leyfa þér að bæta við beam zones, canvas zones og masks. Einnig eru valkostir til að stilla test pattern aðeins fyrir þennan laser, ásamt grid og snapping stillingum.

Nánari upplýsingar eru í [output-view](../output-view/).

#### Canvas

Canvas kerfið er aðallega notað fyrir grafík og architectural mapping. Þú getur dreift flóknum myndum yfir marga lasera og leiðrétt sjónarhorn hvers hluta. Sjá [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/).

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Þótt hægt sé að stjórna Liberation með mús og lyklaborði er miklu betra að nota APC40 MIDI control interface (Mark 2 er best, en Mark 1 virkar líka).

Sjá einnig: [apc40-reference.md](../reference/apc40-reference.md)

Við höfum nú líka innleitt stuðning við APC Mini Mark 2 og MIDI Fighter Twister, og fleiri eru í þróun. APC40 Mark 2 er þó besti kosturinn í flestum tilfellum.&#x20;

### Clips og effects

{% hint style="info" %}
**Hvað er clip?**

Clip er ílát fyrir hvaða laser content sem er innan Liberation. Clips geta innihaldið beams eða grafískar animations og eru yfirleitt lykkja sem endurtekur sig. Hægt er að beina þeim inn í hvaða zone sem er (eða _Canvas target area_) og þau eru ræst með clip hnöppunum inni í Clip Deck.
{% endhint %}

#### Yfirlit yfir Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Þetta grid kallast _Clip Deck_ og þar eru öll laser clips geymd. Það er hannað til að samsvara beint 8 x 5 hnappagridinu á APC40.

**Að fletta um Clip Deck.**

Þú getur flett Clip Deck til vinstri og hægri með:

* Vinstri og hægri örvatökkum. Bættu við `Cmd / Ctrl` til að fletta heilli síðu í einu.
* Trackpad: Strjúktu
* Mús: ef músin þín styður hliðarskrun geturðu notað það þegar bendillinn er yfir Clip Deck
* APC40 scroll knob
* APC40 _<- DEVICE ->_ hnappar

Til að hjálpa þér að átta þig er lítið visualiser af Clip Deck meðfram efri brúninni. Sjá einnig [clips](../clips/)

#### Að ræsa og stöðva clips

Ýttu á clip hnapp (annaðhvort með músinni eða APC40) til að ræsa clip. Ýttu aftur til að stöðva það. Þegar þú ræsir clip stöðvast öll önnur clips í sama lit sjálfkrafa nema þú haldir _shift_ inni.

Sum clips eru í _Flash mode_ (sjálfgefið þau rauðu), og þá stöðvast þau um leið og þú sleppir clip hnappinum.

_STOP_ hnappurinn stöðvar öll clips sem eru í gangi.

#### Að stilla output zones fyrir clip

Undir clip hnöppunum sérðu zone hnappana, beam zones 1 til 8 sjálfgefið (_BEAM 1_, _BEAM 2_ o.s.frv.). Zone hnapparnir lýsast til að sýna hvaða zones eru úthlutaðar á clip sem er valið núna.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Tveimur röðum fyrir neðan zone hnappana sérðu X/Y flip hnappana; kveiktu eða slökktu á þeim til að spegla clip lárétt og lóðrétt.

{% hint style="info" %}
Athugaðu að þessar zone úthlutanir og X/Y flip stillingar tengjast clip sjálfu; þær haldast næst þegar þú keyrir þetta clip. Þær eru ekki global setting.
{% endhint %}

Hægrismelltu á clip til að breyta fleiri stillingum fyrir clip. Sjá einnig [clip-settings.md](../clips/clip-settings.md)

### Groups

Þú tekur eftir að hvert clip er með litaðan ramma, og liturinn sýnir í hvaða _group_ það er. APC40 clip hnapparnir lýsast líka í þessum lit.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Blágrænn</td></tr><tr><td>Group 2</td><td>Appelsínugulur</td></tr><tr><td>Group 3</td><td>Rauður</td></tr><tr><td>Group 4</td><td>Indígó</td></tr><tr><td>Group 5</td><td>Grænn</td></tr></tbody></table>

Group kerfið er mjög sveigjanlegt og gerir þér kleift að:

* Halda clips í einum group í gangi á meðan þú kveikir og slekkur á groups í öðrum
* Úthluta zones og X/Y flips fljótt á öll clips innan group
* Stilla _Flash mode_ fyrir clip (Group 3 er sjálfgefið stillt á _Flash mode_)

Groups hafa líka stillingar fyrir transition in/out sem clips geta erft eða yfirskrifað.

Þú getur úthlutað group fyrir clip með hnöppunum í hægrismellsvalmyndinni, eða með APC40 með því að ýta á group hnappinn og, _á meðan honum er enn haldið niðri,_ ýta á clip hnappana.

Breyttu zone stillingum fyrir öll clips innan group

Með APC40 ýtirðu á group hnappinn og notar svo, _á meðan honum er enn haldið niðri,_ zone og X/Y hnappana til að kveikja og slökkva á zone stillingum fyrir öll clips innan þess group.

Sjá einnig [groups.md](../clips/groups.md)

### Effects

Effects kerfið í Liberation er öflug og fjölhæf leið til að breyta clip output í rauntíma. Sjálfgefnu effects hnapparnir 1-8 eru undir zone hnöppunum.

#### Að beita effect

Ýttu á effect hnapp til að kveikja eða slökkva á effect, eða enn betra, notaðu APC40 sliders 1-8 til að fade effects inn og út.

#### Effect parameters

Notaðu rotary controllers 1-8\* til að stilla _parameter_ fyrir hvern effect. (Eða þú getur hægrismellt með músinni til að stilla level og parameter). Parameter breytingin gerir mismunandi hluti eftir því hvernig effect er settur upp. Sjá listann hér fyrir neðan yfir sjálfgefnu effects.

{% hint style="info" %}
Litlu tölurnar sem þú sérð á effect hnöppunum vísa til _level_ og _parameter_ effectsins. _Level_ er stjórnað með fader á APC40, eða þú getur smellt og dregið á hnappinum. Parameter er stillt með rotaries á APC40, eða þú getur hægrismellt til að stilla með músinni.
{% endhint %}

_\*Rotary controllers 1-8 eru meðfram efri brún APC40 Mk2 og efst til hægri á Mk1. Sjá einnig:_ [apc40-reference.md](../reference/apc40-reference.md)

#### Sjálfgefin effects

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Bætir óreiðukenndri hreyfingu við clip output. Parameter stillir magn/hraða óreiðunnar.
2. **Sine wave** :\
   Sveigir allt content eftir hreyfanlegri sínusbylgju. Parameter stillir bylgjulengdina.
3. **Rotation** :\
   Snýr öllu í hring. Parameter stillir snúningshraðann.
4. **Horizontal flip** :\
   Þjappar og teygir allt lárétt. Parameter stillir hraðann.
5. **Scale** :\
   Skalar allt endurtekið frá fullri stærð niður í núll. Parameter stillir hraðann.
6. **Hue** :\
   Breytir hue á öllu, en breytir ekki saturation (þ.e. allt sem er hvítt helst hvítt). Parameter stillir hue.
7. **Saturation and hue** :\
   Breytir hue á öllu og saturates litinn að fullu (þ.e. allt sem er hvítt breytist í litinn). Parameter stillir hue.
8. **Flash** :\
   Lætur birtu alls blikka endurtekið frá fullri birtu niður í núll. Parameter stillir flash hraðann.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Það eru 16 colour effects til viðbótar í neðstu röðinni til að beita fyrirfram stilltum hue og saturation gildum.

Athugaðu að þetta eru sjálfgefin effects, en hægt er að breyta þeim þannig að þau geri nánast hvað sem þú vilt!

#### Hvað er _„currently selected clip“_?

Þegar þú ræsir clip lýsist það til að sýna að það sé virkt. Það fær líka hvítan ramma sem sýnir að þetta er clip sem er _selected_ núna. Alltaf þegar þú kveikir eða slekkur á zone hnöppum eða breytir clip stillingum eru þær breytingar settar á _currently selected clip._

{% hint style="info" %}
Til að velja clip án þess að ræsa það skaltu ýta á `Alt / Option` takkann áður en þú ýtir á clip hnappinn. Þetta er góð leið til að stilla zones þess og aðrar stillingar án þess að keyra það.
{% endhint %}

### Clip Settings panel

Notaðu _Clip Settings_ panel til að breyta scaling, X/Y position og fá aðgang að öfluga zone delay kerfinu.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings panel

Finndu _Global Settings_ panel til að stilla global output settings sem hafa áhrif á allt output yfir allar zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Kveiktu á AUTO RESET til að endurstilla allar _Global settings_ sjálfkrafa þegar engin clips eru í spilun.&#x20;

### Timing

Nánast allar lasersýningar hafa einhvers konar tónlist, þannig að timing kerfið í Liberation byggir á tempo í slögum á mínútu. Í _Tempo Panel_ sérðu framsetningu á tímanum; hver ferningur táknar einn slag og þú sérð þá blikka í takt.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Það eru margir samstillingarvalkostir, þar á meðal MIDI clock og Ableton Link. Ef þú þekkir tempo tónlistarinnar geturðu stillt það handvirkt með sleðanum á skjánum eða APC40 Tempo knob, en þú getur líka haldið takti við tónlistina með _Tap Tempo_ kerfinu\_.\_

#### Tap Tempo

_Tap Tempo_ er hugtak sem er algengt í tónlistarforritum og gerir þér kleift að slá inn taktinn í rauntíma til að stilla tempo á meðan tónlistin spilar. Þú getur notað hnappinn á skjánum, en mælt er með að nota _T_ takkann eða _Tap Tempo_ hnappinn á APC40 (eða jafnvel fótpedala ef þú vilt).

Ýttu á _R_ takkann eða _Metronome_ hnappinn (APC40) til að endurstilla tempo á byrjun takts.

Ýttu á _Y_ takkann eða snúðu _Tempo_ knob(APC40) til að rúnna tempo í heila tölu. Þetta getur verið gagnlegt fyrir raftónlist, þar sem slög á mínútu eru oft heil tala.

### Að skipuleggja Clip Deck

Til að færa clip á Clip Deck smellirðu á það og dregur það á nýjan stað. Á meðan þú dregur geturðu notað bendiltakkana (eða scroll wheel/buttons á APC40) til að fletta til vinstri og hægri.

Ýttu á `Alt / Option` takkann á meðan þú dregur til að búa til afrit.

`Alt / Option`-smelltu á clip til að velja það án þess að ræsa það.

`Alt / Option + Shift`-smelltu á clip til að velja mörg, eða smelltu og dragðu utan við clip til að velja með „lasso“.&#x20;

Smella og draga mun draga ÖLL valin clips.

Til að eyða einu eða fleiri clips skaltu annaðhvort draga þau af Clip Deck (ruslatunnutákn birtist) eða nota DELETE hnappinn í hægrismellsvalmynd clip.

### Laser Overview panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser overview panel_ gefur þér fljótt yfirlit yfir stöðu laseranna sem eru í gangi. Græni ferningurinn hægra megin sýnir að laserstýringin sé í lagi. Ef hann verður appelsínugulur eru stöku drop-outs, og ef hann verður rauður hefur hún aftengst. Ef hann er grár er hún alls ekki tengd við controller.&#x20;

Grafið í miðjunni sýnir sögu frame lengths og talan hægra megin er núverandi frame rate. Því flóknara sem content er, því lægra verður frame rate (þ.e. meiri flökt). Allt undir um það bil 25fps fer að líta svolítið flöktandi út.&#x20;

### Að tengjast laserum - Controller Assignment panel

Smelltu á _Assign Laser Controllers_ hnappinn til að opna _Controller Assignment_ panel. (Þetta panel er líka aðgengilegt í valmyndastikunni í gegnum _View -> Controller Assignment_).

Hér geturðu valið hvaða laser outputs fara í hvaða laser controllers. Dragðu controllers úr listanum hægra megin yfir í raufarnar vinstra megin. Þú getur endurnefnt controllers þannig að þeir passi við laserinn sem þeir eru paraðir við (notaðu pennatáknhnappinn).

Lestu kaflann [controller-assignment.md](../setting-up/controller-assignment.md) fyrir frekari upplýsingar.

{% hint style="danger" %}
Áður en þú arm nokkra lasera skaltu ganga úr skugga um að fara yfir kaflann [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

### Laser Output panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Þetta panel sýnir stillingar fyrir _currently selected laser_ (sýndan með númerinu efst). Breyttu hvaða laser er currently selected með _tab_ takkanum, með því að ýta á númeratakka, smella á lasernúmer í _Laser Overview_ panel eða í _output view._

* **Number button** arm og disarm laserinn; ef hann er rauður er laserinn armed.
* **Brightness** stillir birtu lasers óháð öðrum laserum (og hún sameinast _global brightness_ stillingunni - þ.e. ef báðar eru í 50% verður laserinn þinn í 25%).
* **Test Pattern** kveikir á test pattern aðeins fyrir þennan laser (yfirskrifar global test pattern stillinguna)
* **Orientation** leiðréttir fyrir lasera sem eru hengdir upp á hlið eða á hvolfi.
* **Flip Horizontal and Flip Vertical** snýr output lasersins við. Gagnlegt til að leiðrétta output á laserum með ósamræmda vírun.
* **Copy Laser Settings** opnar panel sem leyfir þér að afrita ýmsar stillingar frá þessum laser yfir á aðra.

### Scanner settings

Sýningarlaserar virka þannig að einn lasergeisli er hreyfður gríðarlega hratt og kveikt og slökkt á honum til að teikna form í loftinu. Það sem þú sérð sem línur, form og myndir er í raun geislinn sem rekur ferla hraðar en augun þín ná að fylgja.

Point stream er gögnin sem segja laserinum hvert hann á að fara næst og hvenær geislinn á að vera kveiktur eða slökktur. Í Liberation eru clips umbreytt í þennan point stream í rauntíma á meðan þau eru send til laseranna.

Liberation gefur þér nákvæma stjórn á því hvernig þessi point stream er búinn til, svo þú getir jafnað smoothness, brightness og performance fyrir hvern laser.

{% hint style="info" %}
Ef þú ert vön/vanur eldri laserhugbúnaði sem byggir á fyrirfram reiknuðum point streams getur þessi nálgun fyrst virst öðruvísi. Rauntíma point generation gerir þó kleift að optimize sama content á mismunandi hátt fyrir hvern laser. Þetta auðveldar vinnu með marga lasera sem hafa mismunandi scanner speeds eða gæði, án þess að afrita eða endurbyggja content. Þetta heldur clip skrám líka mjög litlum, sem er ástæðan fyrir því að allt sjálfgefna Liberation Clip Deck er aðeins nokkur megabæti frekar en gígabæti.
{% endhint %}

Grunnstillingar scanner eru:

* **Speed** er scanner speed, þ.e. hversu hratt laserinn hreyfist til að teikna form. Þetta jafngildir því að stilla point rate í hefðbundnum laserhugbúnaði, en í Liberation geturðu breytt því hversu hratt laserinn hreyfist _óháð point rate._ Þú ættir ekki að þurfa að breyta þessu.
* **Scanner sync** (stundum kallað _blank shift, previously Colour Shift_) Scanners færa laserinn mjög hratt til, en yfirleitt er breytingin á birtu og lit ekki í sync við hreyfinguna. Þetta birtist sem litlir flöktandi „halar“ af ljósi á brúnum beams og lína. Notaðu þessa stillingu til að samstilla hreyfingu og lit. Sjá [laser-settings](../setting-up/laser-settings/)

Fjallað er um aðrar advanced scanner settings í kaflanum [advanced](../advanced/).

### Zoning

Fyrir heildarleiðbeiningar um að setja upp og zoning lasera, sjá: [setting-up-lasers.md](../setting-up/setting-up-lasers.md)
