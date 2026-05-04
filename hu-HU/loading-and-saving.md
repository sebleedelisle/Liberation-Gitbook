---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Betöltés és mentés

A Liberation folyamatosan menti az állapotát a lemezre, így áramkimaradás vagy rendszerhiba esetén is onnan indul újra, ahol abbahagyta. A zónák, timeline-ok és egyéb tartalmak normál esetben nem vesznek el.

Ettől függetlenül exportálhatod a beállításaidat biztonsági mentéshez, vagy ha egy másik számítógépre szeretnéd áthelyezni őket.

### Projekt importálása/exportálása

A Project fájl a jelenlegi beállítások szinte minden elemét tárolja, többek között:

* Mindent, ami az alábbi részben szerepel: [Betöltés és mentés](loading-and-saving.md#laser-settings-import-export "mention")
* Klipeket, effekteket és csoportbeállításokat
* Az összes timeline-t, az audio- és videomédia kivételével
* Art-Net-beállításokat
* MIDI küldési/fogadási beállításokat
* Tempó- és szinkronizációs beállításokat

Jelenleg nem menti és tölti be:

* A Sound és MIDI bemeneti beállításokat, amelyeket a MIDI notes node és a Sound Input Oscillator használ (_a_ MIDI küldési/fogadási beállításokat, valamint a timecode hangbemenetet viszont menti)
* A felület méretezését
* A Canvas segédképeihez tartozó médiafájlokat
* A timeline-okhoz tartozó hang- és videomédiát
* A Text node által használt betűtípusokat

{% hint style="danger" %}
A timeline-ban lévő hang- és videofájlok nem kerülnek mentésre a projektfájlokkal, ezért ha másik számítógépre szeretné áthelyezni őket, mindenképpen mentse el külön ezeket is. Lásd: [Betöltés és mentés](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Laser settings importálása/exportálása

* Laser settings minden lézerhez
* Beam zones
* Canvas target areas
* DMX zones
* Lézervezérlő-hozzárendelés, valamint az átnevezett vezérlők aliasai
* Lézerszkenner- és színkalibrációs beállítások és presetek
* 3D visualiser beállítások és presetek

### Clip Deck importálása/exportálása

* Az összes klip és a hozzájuk tartozó zónahozzárendelések, beállítások és paraméterek
* Az összes csoportbeállítás, flash mode, fade in/out idők stb.

Jelenleg nem menti és tölti be:

* Az összes effektet, valamint azok paramétereit és beállításait

{% hint style="info" %}
**Klipek betöltése projektfájlból a teljes projekt betöltése nélkül**

Ha csak a klipeket szeretné importálni egy projektből, válassza a _**Clips->Import Clip Deck**_ lehetőséget, majd clip deck fájl (.cpdk) helyett válasszon egy projektfájlt.
{% endhint %}

### Clip deck hozzáfűzése

Az _Append Clip Deck_ használatával egy exportált clip deck fájlból klipeket adhat hozzá a jelenlegi projekthez. A klipek a jelenlegi clip deck végére kerülnek, de a fájlban lévő effektek és csoportbeállítások nem kerülnek importálásra.

### Kijelölt klipek exportálása

A jelenleg kijelölt klipek egy fájlba lesznek exportálva. A csoportbeállítások és effektek nem kerülnek mentésre, csak a klipek. Fontos, hogy az éppen futó aktív klipek nem kerülnek exportálásra, hacsak nincsenek kijelölve.

{% hint style="info" %}
A klipek kijelöléséhez használja az Option/Alt - shift - click műveletet, vagy a lasszót. A kijelölt klipeket a körülöttük látható vastag fehér körvonal jelzi. Lásd: [Clipek indítása / leállítása](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Effektek importálása/exportálása

Betölti és menti az összes effektet a hozzájuk tartozó csoportbeállításokkal és paraméterekkel együtt.

{% hint style="info" %}
**Effektek betöltése projektfájlból a teljes projekt betöltése nélkül**

Ha csak az effekteket szeretné importálni egy projektből, válassza az _**Effects->Import Effects**_ lehetőséget, majd effect fájl (.efts) helyett válasszon egy projektfájlt.
{% endhint %}

### Timeline exportálása

Egy vagy több timeline-t tartalmazó timeline fájl exportálása. Fontos, hogy a Clip Deck mindig bekerül az exportált timeline fájlokba, bár az importáláskor kiválaszthatod, mely Clip elemeket szeretnéd visszaimportálni. Lásd: [Betöltés és mentés](loading-and-saving.md#timeline-import "mention") alább.

Ha a projektfájlban egynél több timeline található, megnyílik egy panel, ahol kiválaszthatja, mely timeline-okat szeretné exportálni.

{% hint style="danger" %}
A timeline-ban lévő hang- és videofájlok nem kerülnek mentésre a timeline fájlokkal, ezért ha a tartalmat másik számítógépre szeretné áthelyezni, mindenképpen mentse el külön ezeket is. Lásd: [Betöltés és mentés](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Timeline importálása

Egy vagy több timeline importálása egyetlen timeline fájlból. Miután kiválasztotta a timeline fájlt, megnyílik egy panel több importálási beállítással.

Ha a timeline fájl egynél több timeline-t tartalmaz, mindegyik megjelenik a listában. Jelölje be azokat, amelyeket be szeretne vonni.

* Replace existing timelines\
  Törli az összes jelenlegi timeline-t, és az importáltakra cseréli őket
* Import used clips only\
  Csak a használt klipeket importálja, és a klipeket csoportokba rendezi, timeline-onként egy csoportba. Ha ez az opció nincs kiválasztva, a timeline fájl teljes clip deckje hozzáfűződik a meglévő klipekhez.
* Replace existing clip deck\
  A jelenlegi clip decket lecseréli a timeline fájlban lévő klipekre. Csak akkor érhető el, ha a _Replace existing timelines_ ki van választva.

{% hint style="info" %}
**Timeline-ok betöltése projektfájlból a teljes projekt betöltése nélkül**

Ha csak a timeline-okat szeretné importálni egy projektből, válassza a _**Timeline->Import Timeline(s)**_ lehetőséget, majd timeline fájl (.ltml) helyett válasszon egy projektfájlt.
{% endhint %}

### DMX / Art-Net importálása/exportálása

Menti és betölti az Art-Net node-okat az IP-címeikkel együtt. Tartalmazza a DMX zones elemeket és az összes DMX presetet is.

### Fontos megjegyzés a timeline médiafájljairól

A hang- és videofájlok jelenleg **nem** kerülnek exportálásra a timeline fájllal, ezért ha a tartalmat másik számítógépre kell áthelyeznie, ezeket is mellékelje.

{% hint style="info" %}
**Hogyan keresi a timeline a médiafájlokat**

A timeline betöltésekor a program a timeline- vagy projektfájllal azonos mappában keres, valamint annak almappáiban. Így ha a fájlok ugyanabban a mappában vagy egy almappában vannak, például _/videos_ vagy _/sound_, a betöltéskor meg fogja találni őket.
{% endhint %}
