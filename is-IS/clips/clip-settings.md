---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip settings

### Clip settings-spjald

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip settings-spjaldið</p></figcaption></figure>

Breyttu úttaksstærð Clip með _Scale X_ og _Scale Y_. Þær eru læstar saman nema þú haldir _SHIFT_ inni.

Breyttu láréttri og lóðréttri staðsetningu Clip með _Shift X_ og _Shift Y_.

_Zone Delay/Chase_ er svo skemmtilegur eiginleiki að hann fær sinn eigin kafla. [zone-delay-chase.md](zone-delay-chase.md)

### Að læsa Clip

Ef Clip er læst er ekki hægt að færa það eða eyða því. Til að læsa Clip notarðu gátreitinn _Locked_ í hægrismellsvalmyndinni. Í Clip settings-spjaldinu færðu nokkra valkosti til viðbótar.

* _UNLOCK ALL -_ aflæsir öllum Clip í Clip Deck.
* _AUTO-LOCK_ - þegar _Auto-Lock_ er virkt læsist hvert Clip sem er spilað sjálfkrafa, annaðhvort með tímalínunni eða MIDI-upptöku/spilunarkerfinu. Þetta er gagnlegt ef þú hefur forritað sýningu í Logic Pro (eða sambærilegu) og vilt ekki breyta óvart Clip sem eru notuð í sýningunni.
* _LOCKED CLIPS ZONES_ - ef þetta er virkt geturðu ekki breytt svæðum fyrir nein læst Clip
* _LOCKED CLIPS PARAMS_ - ef þetta er virkt geturðu ekki breytt færibreytum (scale, shift o.s.frv.) fyrir nein læst Clip.

### Hægrismellsvalmynd

Ef þú hægrismellir á Clip birtist valmynd með nokkrum valkostum fyrir það Clip. Sjá [clip-editor-intro.md](../clip-editor/clip-editor-intro.md), [clip-settings.md](clip-settings.md) og [groups.md](groups.md) fyrir meira um fyrstu atriðin í þessari valmynd.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>Hægrismellsvalmynd Clip settings</p></figcaption></figure>

### Retrigger

Sjálfgefið er að Clip séu stillt á _retrigger_. Það þýðir að sama hvenær þú ýtir á það byrjar Clip að keyra frá þeirri stundu. Ef þú ræsir það seint verður hreyfingin í Clip því aðeins sein og úr takt.

{% hint style="info" %}
Ef þú notar _Tap Tempo_ á meðan Clip með retrigger er í gangi mun kerfið „quantise“ Clip þannig að það sé í takt, jafnvel þótt þú hafir ekki ræst það nákvæmlega á slagi.
{% endhint %}

Ef _Retrigger_ er ekki virkt verður Clip alltaf í takt — það er eins og Clip hafi verið ræst alveg í upphafi klukkunnar. Þetta hentar vel þegar þú ert fullkomlega samstilltur við tónlistina með ytra klukkumerki.

{% hint style="info" %}
Clip eru oft hönnuð til að lykkjast endalaust, en þú getur hannað þau þannig að þau keyri aðeins einu sinni eða nokkrar umferðir. Gakktu úr skugga um að hafa slík Clip stillt á _retrigger_, annars endurræsast þau ekki!
{% endhint %}

### Transition in/out time (fade)

Hægt er að stilla Clip til að dofna inn og út með tímalengd mældri í sekúndum. Sjálfgefið erfir Clip dofnunartímann frá hópstillingunum sínum (og hægt er að breyta honum með því að hægrismella á hóphnappinn).

Ef þú vilt annan dofnunartíma en er stilltur fyrir hóp Clip skaltu fyrst slökkva á _USE GROUP DEFAULT_ hnappnum og síðan stilla rennurnar _In time_ og _Out time_ fyrir Clip.
