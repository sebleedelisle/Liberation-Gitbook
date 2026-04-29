---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Kynning á Clip Editor

Clip Editor er fjölhæf leið til að búa til laser-efni og er kjarninn í Liberation. Það er auðvelt að búa til einfalda hluti, en tólið er samt nógu sveigjanlegt til að skapa mjög fáguð og flókin áhrif.

{% hint style="info" %}
Node-byggði ritillinn var fyrsti hlutinn af Liberation sem var búinn til! Hugmyndin varð til í samtali við Rob Stanley á laser-samkomu í Bretlandi árið 2018 um hvernig „hlutbundið“ hönnunartól fyrir laser-efni gæti litið út.

Þótt þetta virðist einfalt er þetta frekar flókið kerfi í smíðum, en í byrjun árs 2019 var ég kominn með virkt sýnidæmi sem sannaði hugmyndina — og þar hófst allt þetta ferðalag!
{% endhint %}

Þetta er node-byggður sjónrænn ritill (eða [node graph-arkitektúr](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) sem þú kannast líklega við ef þú hefur notað forrit eins og TouchDesigner, MaxMSP eða VVVV. Clip Editor er þó aðeins öðruvísi og nokkuð einfaldari, þar sem hann er hannaður sérstaklega fyrir vektor-grafík.

Þú opnar Clip Editor með því að hægrismella á clip-hnappinn og velja _EDIT CLIP_. Þú getur líka hægrismellt á tóman clip-hnapp og valið _CREATE AND EDIT CLIP_.

### Yfirlit

Í Clip Editor sérðu:

* **Creator**- og **Operator node buttons** efst
* **Oscillator node buttons** vinstra megin
* Forskoðun á efninu í spjaldi hægra megin. Ef þú smellir á node sérðu einnig aðra forskoðun sem sýnir efnið nákvæmlega á þeim node.
* Öll nodes og tengingar fyrir clip sem þú ert að breyta (ef þetta er nýtt clip er svæðið tómt)
* Clip Editor-spjaldið með ýmsum valkostum

Á meðan þú ert að breyta sérðu einnig hvernig clip lítur út í 3D-sýninni í bakgrunni.

{% hint style="info" %}
Ef þú sérð ekkert Output í 3D-sýninni gætirðu þurft að nota zone-hnappana til að kveikja á þeim zones sem þú vilt nota. Þú þarft líka að ganga úr skugga um að _Preview to lasers_ sé virkt; sjá [Clip Editor-spjaldið](clip-editor-intro.md#clip-editor-panel) hér fyrir neðan.
{% endhint %}

### Að byggja clip

Yfirleitt byrjarðu með einn eða fleiri [Creator nodes](creator-nodes.md) og tengir síðan [Nodes fyrir aðgerðir](operator-nodes/) frá vinstri til hægri til að vinna úr efninu. Þegar þú færir Creator og/eða Operator nær saman sérðu að þau tengjast sjálfkrafa. Þú getur svo dregið þau í sundur aftur til að aftengja þau.

### Að bæta nodes við clip

Smelltu og dragðu frá einum af node-hnöppunum efst eða vinstra megin inn á autt svæði í Clip Editor.

### Að stilla node

Smelltu á tannhjólshnappinn (efst til hægri á node) til að opna properties-spjaldið fyrir þann node.

### Að virkja og óvirkja node

Smelltu á aflhnappinn (efst til vinstri á node) til að virkja eða óvirkja hann. Node dofnar til að sýna að hann sé ekki virkur í augnablikinu. Athugaðu að efni fer áfram í gegnum Operator þótt hann sé óvirkur, en node hefur þá ekki áhrif á efnið.

### Að tengja nodes saman

Efni er búið til með Creator node og fer síðan eftir nodes frá vinstri til hægri. Hver Operator hefur einhver áhrif á efnið og sendir það áfram til næsta Operator. Það sem stendur eftir við enda leiðarinnar er efnið í clip. Creator og Operator tengjast sjálfkrafa þegar þú færir þau nálægt hvort öðru. Til að aðskilja þau dregurðu þau aftur í sundur.

{% hint style="info" %}
Þú getur tengt fleiri en einn node inn í inntak næsta node. Þetta er gagnlegt þegar þú vilt sameina marga hluta af efni.
{% endhint %}

### Node properties og sockets

Hver node hefur röð af sockets neðst og hvert socket táknar property innan node, til dæmis brightness, position, scale, rotation o.s.frv.

[Oscillator nodes](oscillators/) má tengja við þessi sockets neðan frá og nota til að hreyfa þessar stillingar. Oscillator nodes hafa úttak efst; smelltu og dragðu til að draga út tengingu og slepptu henni í eitt af property sockets á öðrum node.

### Oscillator nodes

Oscillator nodes eru notuð til að breyta properties yfir tíma. Yfirleitt tákna þau bylgjuform, eins og sawtooth eða sine wave, en sum Oscillator nodes nota ytri inntak (til dæmis hljóðnemastyrk) sem uppruna.

{% hint style="info" %}
Ef þú hefur einhvern tíma notað analog synth þekkirðu hugmyndina um oscillators, sem eru oft notaðir til að búa til bylgjuform eða breyta hljóði yfir tíma. Oscillators í Liberation gera svipaða hluti.

**Skemmtileg staðreynd:** nafnið _Liberation_ var innblásið af Moog Liberation, „keytar“-hljóðgervli sem kom út árið 1980 og varð frægur í höndum Herbie Hancock, Jean-Michel Jarre og jafnvel James Brown!
{% endhint %}

Oscillators hafa alltaf _range_-stillingar sem stjórna lágmarks- og hámarksgildi þess property sem á að breyta. _Wave Oscillators_ hafa líka alltaf _duration_-stillingu sem ákvarðar hversu hratt oscillator breytir gildinu. Sjá [Bylgjusveiflar](oscillators/wave-oscillators.md) fyrir nánari upplýsingar.

### Clip Editor-spjaldið

* Timer - efst á spjaldinu sérðu núverandi tíma fyrir clip þegar það keyrir áfram
* _RETRIGGER_ - ræsir clip aftur frá byrjun; sérstaklega gagnlegt ef clip fer ekki í loop
* _Preview to lasers_ - þegar þetta er hakað við uppfærist 3D-sýnin á meðan þú breytir þessu clip. Ef þú slekkur á þessu sérðu þau clips sem eru í gangi utan ritilsins. Þetta er global stilling, ekki stilling fyrir hvert clip.
* _UNDO/REDO_ - fyrir Clip Editor sjálfan. Einnig tengt við `Cmd / Ctrl + Z` og `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ - vistar breytingarnar þínar en varar þig við ef verið er að skrifa yfir
* _SAVE AS A COPY_ - vistar clip í næsta lausa reit í Clip Deck. Þetta verður ný staðsetning fyrir clip og allar síðari vistanir fara á þennan nýja stað.
* _EXIT EDITOR_ - lokar Clip Editor. Ef þú ert með óvistaðar breytingar birtist staðfestingarspjald.
