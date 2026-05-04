---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Bevezetés a Clip Editor használatába

A clip editor sokoldalú eszköz lézeres tartalmak készítéséhez, és a Liberation egyik központi része. Egyszerű elemeket könnyen létrehozhatsz vele, ugyanakkor elég rugalmas ahhoz is, hogy nagyon kifinomult és összetett effekteket készíts.

{% hint style="info" %}
A csomópont-alapú editor volt a Liberation elsőként elkészült része! Egy 2018-as brit lézeres találkozón, Rob Stanleyvel folytatott beszélgetésből született az ötlet, hogy milyen lenne egy „objektumorientált” lézeres tartalomtervező.

Bár egyszerűnek tűnik, valójában meglehetősen összetett rendszer megépíteni, de 2019 elejére már volt egy működő demóm, amely igazolta a koncepciót – és ezzel indult el ez az egész út!
{% endhint %}

Ez egy csomópont-alapú vizuális editor (vagy [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)), amely ismerős lehet, ha használtál már olyan termékeket, mint a TouchDesigner, a MaxMSP vagy a VVVV. A clip editor azonban kicsit más, és valamivel egyszerűbb is, mivel kifejezetten vektorgrafikához készült.

A Clip Editor megnyitásához kattints jobb gombbal a Clip gombra, és válaszd az _EDIT CLIP_ lehetőséget. Vagy kattints jobb gombbal egy üres Clip gombra, és válaszd a _CREATE AND EDIT CLIP_ lehetőséget.

### Áttekintés

A clip editorban a következőket látod:

* A **Creator** és **Operator node buttons** felül
* Az **Oscillator node buttons** bal oldalt
* A tartalom előnézete egy jobb oldali panelen, és ha egy node-ra kattintasz, megjelenik egy második előnézet is, amely magánál a node-nál mutatja a tartalmat.
* Az éppen szerkesztett clip összes node-ja és kapcsolata (új clip esetén ez üres lesz)
* A Clip Editor panel különféle beállításokkal

Szerkesztés közben a háttérben a 3D visualiser nézetben is látod, hogyan néz ki a clip.

{% hint style="info" %}
Ha nem látsz kimenetet a 3D visualiser nézetben, lehet, hogy a zone gombokkal be kell kapcsolnod a kívánt zónákat. Emellett győződj meg róla, hogy a _Preview to lasers_ engedélyezve van; lásd lent: [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel "mention").
{% endhint %}

### Clip készítése

Általában egy vagy több [creator node](creator-nodes.md) elemmel kezdesz, majd balról jobbra [Operátor csomópontok](operator-nodes/) elemeket kapcsolsz hozzájuk, amelyek feldolgozzák a tartalmat. Amikor a creatorokat és/vagy operatorokat egymáshoz közel mozgatod, észreveszed, hogy automatikusan összekapcsolódnak. Ha ismét szét szeretnéd választani őket, húzd őket távolabb egymástól.

### Node-ok hozzáadása a cliphez

Kattints és húzd be az egyik felül vagy bal oldalt található node gombról az elemet a clip editor egy üres területére.

### Egy node beállításainak módosítása

Kattints a fogaskerék ikon gombra (a node jobb felső sarkában), hogy megnyisd az adott node tulajdonságpaneljét.

### Egy node engedélyezése és letiltása

Kattints a bekapcsoló ikon gombra (a node bal felső sarkában) a node engedélyezéséhez vagy letiltásához. A node elhalványul, jelezve, hogy jelenleg nem aktív. Fontos: a tartalom akkor is áthalad egy operatoron, ha az le van tiltva, de a node ilyenkor nem módosítja a tartalmat.

### Node-ok összekapcsolása

A tartalom egy creator node-dal jön létre, majd balról jobbra halad tovább a node-okon; minden operator valamilyen módon módosítja a tartalmat, majd továbbadja a következő operatornak. Ami az útvonal végén megmarad, az lesz a clip tartalma. A Creator és Operator elemek automatikusan összekapcsolódnak, amikor közel mozgatod őket egymáshoz. Szétválasztáshoz húzd őket ismét távolabb egymástól.

{% hint style="info" %}
Egynél több node-ot is csatlakoztathatsz a következő node bemenetére. Ez akkor hasznos, ha több tartalomelemet szeretnél kombinálni.
{% endhint %}

### Node tulajdonságok és socketek

Minden node alján socketek sora található, és mindegyik a node egy-egy tulajdonságát jelöli, például fényerőt, pozíciót, skálázást, forgatást stb.

Az [Oscillator node-ok](oscillators/) alulról csatlakoztathatók ezekhez a socketekhez, és ezekkel animálhatók a beállítások. Az Oscillator node-ok kimenete felül található; kattints és húzd ki a kapcsolatot, majd engedd rá valamelyik másik node tulajdonság-socketjére.

### Oscillator node-ok

Az Oscillator node-ok tulajdonságok időbeli változtatására szolgálnak. Általában hullámformákat, például fűrészfogat vagy szinuszhullámot képviselnek, de egyes Oscillator node-ok külső bemeneteket használnak forrásként, például a mikrofon bemeneti szintjét.

{% hint style="info" %}
Ha használtál már analóg szintetizátort, ismerős lesz az oszcillátorok fogalma: ezeket gyakran hullámformák létrehozására vagy a hang időbeli módosítására használják. A Liberation oszcillátorai hasonló feladatot látnak el.

**Érdekesség:** a _Liberation_ név a Moog Liberation szintetizátorról kapta az ihletet. Ez egy 1980-ban megjelent „keytar” volt, amelyet Herbie Hancock, Jean-Michel Jarre, sőt James Brown is ismertté tett!
{% endhint %}

Az Oscillatoroknak mindig vannak _range_ beállításaik, amelyek a módosítandó tulajdonság minimális és maximális értékét szabályozzák. A _Wave Oscillators_ elemeknek pedig mindig van _duration_ beállításuk, amely meghatározza, milyen gyorsan változtatja az oscillator az értéket. További információ: [Hullámoszcillátorok](oscillators/wave-oscillators.md "mention").

### Clip editor panel

* Timer - a panel tetején a clip aktuális idejét látod, ahogy az lejátszás közben halad
* _RETRIGGER_ - újraindítja a clipet az elejétől; különösen hasznos, ha a clip nem loopol
* _Preview to lasers_ - ha be van jelölve, a 3D visualiser frissül, miközben ezt a clipet szerkeszted. Ha kikapcsolod, az editoron kívül futó clipeket fogod látni. Ez globális beállítás, nem clipenkénti.
* _UNDO/REDO_ - magára a clip editorra vonatkozik. A `Cmd / Ctrl + Z` és `Cmd / Ctrl + Shift + Z` billentyűparancsokra is le van képezve.
* _SAVE CLIP_ - menti a módosításokat, de figyelmeztet a felülírásra
* _SAVE AS A COPY_ - elmenti a clipet a clip deck következő szabad helyére. Ez lesz a clip új pozíciója, és minden későbbi mentés erre az új helyre kerül.
* _EXIT EDITOR_ - bezárja a clip editort. Ha vannak nem mentett módosításaid, megjelenik egy megerősítő panel.
