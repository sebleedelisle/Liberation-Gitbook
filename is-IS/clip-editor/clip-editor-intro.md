---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Kynning á Clip Editor

Clip Editor er fjölhæf leið til að búa til laser-efni og er kjarninn í Liberation. Það er auðvelt að gera einfalda hluti, en ritillinn er samt nógu sveigjanlegur til að búa til mjög þróaðar og flóknar effecta.

{% hint style="info" %}
Hnútabundni ritillinn var fyrsti hlutinn í Liberation sem var búinn til! Hugmyndin kviknaði í samtali við Rob Stanley á laser-hittingi í Bretlandi árið 2018 um hvernig „hlutbundinn“ hönnuður fyrir laser-efni gæti litið út.

Þótt þetta virðist einfalt er þetta nokkuð flókið kerfi í smíðum, en í byrjun árs 2019 var ég kominn með virkt sýnidæmi sem sannaði hugmyndina — og þar með hófst allt þetta ferðalag!
{% endhint %}

Þetta er hnútabundinn myndrænn ritill (eða [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) sem þú kannast líklega við ef þú hefur notað forrit eins og TouchDesigner, MaxMSP eða VVVV. Clip Editor er þó aðeins öðruvísi og nokkuð einfaldari, þar sem hann er hannaður sérstaklega fyrir vigurgrafík.

Þú getur opnað Clip Editor með því að hægrismella á clip-hnappinn og velja _EDIT CLIP_. Þú getur líka hægrismellt á tóman clip-hnapp og valið _CREATE AND EDIT CLIP_.

### Yfirlit

Í Clip Editor sérðu:

* **Creator** og **Operator node buttons** efst
* **Oscillator node buttons** vinstra megin
* Forskoðun á efninu í spjaldi hægra megin, og ef þú smellir á hnút sérðu aðra forskoðun sem sýnir efnið við hnútinn sjálfan.
* Alla hnúta og tengingar fyrir það Clip sem þú ert að breyta (ef þetta er nýtt Clip verður þetta tómt)
* Clip Editor-spjaldið með ýmsum valkostum

Á meðan þú ert að breyta sérðu líka hvernig Clip lítur út í 3D Visualiser í bakgrunni.

{% hint style="info" %}
Ef þú sérð ekkert output í 3D Visualiser gætirðu þurft að nota zone-hnappana til að kveikja á þeim zones sem þú vilt nota. Þú þarft líka að ganga úr skugga um að _Preview to lasers_ sé virkt; sjá [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel) hér fyrir neðan.
{% endhint %}

### Að byggja Clip

Yfirleitt byrjarðu með einum eða fleiri [Creator-hnútum](creator-nodes.md) og tengir [Operator-hnúta](operator-nodes/) frá vinstri til hægri sem vinna úr efninu. Þegar þú færir Creator og/eða Operator saman sérðu að þeir tengjast sjálfkrafa. Þú getur svo dregið þá í sundur til að aftengja þá aftur.

### Að bæta hnútum við Clip

Smelltu og dragðu frá einum af node-hnöppunum efst eða vinstra megin inn á autt svæði í Clip Editor.

### Að stilla hnút

Smelltu á tannhjólstáknið (efst til hægri á hnútnum) til að opna properties-spjaldið fyrir þann hnút.

### Að virkja og slökkva á hnút

Smelltu á power-táknið (efst til vinstri á hnútnum) til að virkja eða slökkva á hnútnum. Hnúturinn dofnar til að sýna að hann sé ekki virkur eins og er. Athugaðu að efni fer áfram í gegnum Operator þótt slökkt sé á honum, en hnúturinn hefur þá engin áhrif á efnið.

### Að tengja hnúta saman

Efni er búið til með Creator-hnút og fer áfram eftir hnútum frá vinstri til hægri; hver Operator hefur einhver áhrif á efnið og sendir það áfram til næsta Operator. Það sem stendur eftir við enda leiðarinnar verður efni Clip. Creator og Operator tengjast sjálfkrafa þegar þú færir þá nálægt hvor öðrum. Til að aðskilja þá dregurðu þá aftur í sundur.

{% hint style="info" %}
Þú getur tengt fleiri en einn hnút inn í input næsta hnúts. Þetta er gagnlegt til að sameina mörg efnisatriði.
{% endhint %}

### Properties og sockets hnúta

Hver hnútur er með röð af sockets neðst og hvert þeirra táknar property innan hnútsins, svo sem brightness, position, scale, rotation o.s.frv.

Hægt er að tengja [Oscillator-hnúta](oscillators/) við þessi sockets neðan frá og nota þá til að hreyfa þessar stillingar. Oscillator-hnútar eru með output efst; smelltu og dragðu til að draga út tenginguna og slepptu henni í eitt af property sockets annarra hnúta.

### Oscillator-hnútar

Oscillator-hnútar eru notaðir til að breyta properties yfir tíma. Þeir tákna yfirleitt bylgjulögun eins og sawtooth eða sine wave, en sumir Oscillator-hnútar nota ytri input (til dæmis styrk úr microphone input) sem uppsprettu.

{% hint style="info" %}
Ef þú hefur einhvern tíma notað analog synth þekkirðu líklega hugmyndina um oscillators, sem eru oft notaðir til að búa til bylgjulögun eða breyta hljóðinu yfir tíma. Oscillators í Liberation gera svipaða hluti.

**Skemmtileg staðreynd:** nafnið _Liberation_ var innblásið af Moog Liberation, „keytar“-hljóðgervli sem kom út árið 1980 og varð frægur í höndum Herbie Hancock, Jean-Michel Jarre og jafnvel James Brown!
{% endhint %}

Oscillators eru alltaf með _range_ stillingar sem stjórna lágmarks- og hámarksgildi þess property sem á að breyta. _Wave Oscillators_ eru líka alltaf með _duration_ stillingu sem ákvarðar hversu hratt oscillatorinn breytir gildinu. Sjá [wave-oscillators.md](oscillators/wave-oscillators.md) fyrir frekari upplýsingar.

### Clip Editor-spjaldið

* Timer - efst á spjaldinu sérðu núverandi tíma Clip þegar það keyrir áfram
* _RETRIGGER_ - endurræsir Clip frá byrjun; sérstaklega gagnlegt ef Clip lykkjast ekki
* _Preview to lasers_ - þegar hakað er við þetta uppfærist 3D Visualiser á meðan þú breytir þessu Clip. Ef þú slekkur á þessu sérðu þau Clips sem eru í gangi utan ritilsins. Þetta er global stilling, ekki stilling fyrir hvert Clip.
* _UNDO/REDO_ - fyrir Clip Editor sjálfan. Einnig tengt við `Cmd / Ctrl + Z` og `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ - vistar breytingarnar þínar en varar þig við yfirskrift
* _SAVE AS A COPY_ - vistar Clip í næsta lausa reit í Clip Deck. Þetta verður nýja staðsetningin fyrir Clip og allar síðari vistanir fara á þennan nýja stað.
* _EXIT EDITOR_ - lokar Clip Editor. Ef þú ert með óvistaðar breytingar færðu staðfestingarspjald.
