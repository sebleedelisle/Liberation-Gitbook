---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip stillingar

### Clip settings-spjaldið

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip settings-spjaldið</p></figcaption></figure>

Breyttu úttaksstærð Clip með _Scale X_ og _Scale Y_. Þessar stillingar eru læstar saman nema þú haldir inni _SHIFT_.

Breyttu láréttri og lóðréttri staðsetningu Clip með _Shift X_ og _Shift Y_.

_Zone Delay/Chase_ er svo skemmtilegur eiginleiki að hann fær eigin kafla. [Zone Delay/Chase](zone-delay-chase.md)

### Að læsa Clips

Ef Clip er læst er ekki hægt að færa það eða eyða því. Til að læsa Clip skaltu nota gátreitinn _Locked_ í hægrismellsvalmyndinni. Í Clip settings-spjaldinu færðu nokkra valkosti til viðbótar.

* _UNLOCK ALL -_ aflæsir öllum Clips í Clip Deck.
* _AUTO-LOCK_ - þegar _Auto-Lock_ er virkt læsist hvert Clip sem er spilað sjálfkrafa, annaðhvort með tímalínunni eða MIDI upptöku-/spilunarkerfinu. Þetta er gagnlegt ef þú hefur forritað sýningu í Logic Pro eða sambærilegu forriti og vilt ekki breyta óvart þeim Clips sem eru notuð í sýningunni.
* _LOCKED CLIPS ZONES_ - ef þetta er virkt geturðu ekki breytt zones fyrir neitt læst Clip.
* _LOCKED CLIPS PARAMS_ - ef þetta er virkt geturðu ekki breytt færibreytum, svo sem scale, shift o.s.frv., fyrir neitt læst Clip.

### Hægrismellsvalmynd

Ef þú hægrismellir á Clip birtist valmynd með nokkrum valkostum fyrir það Clip. Sjá [Kynning á Clip Editor](../clip-editor/clip-editor-intro.md), [Clip stillingar](clip-settings.md) og [Hópar](groups.md) til að fá nánari upplýsingar um fyrstu atriðin í þessari valmynd.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>Hægrismellsvalmynd fyrir Clip stillingar</p></figcaption></figure>

### Retrigger

Sjálfgefið er að Clips séu stillt á _retrigger_. Það þýðir að sama hvenær þú ýtir á Clip byrjar það að keyra frá þeirri stundu. Ef þú ræsir það seint verður hreyfingin í Clip því aðeins sein og úr takti.

{% hint style="info" %}
Ef þú notar _Tap Tempo_ á meðan Clip með _retrigger_ er í gangi „quantise“-ar kerfið Clip þannig að það fari í takt, jafnvel þótt þú hafir ekki ræst það nákvæmlega á slagi.
{% endhint %}

Ef _Retrigger_ er ekki virkt verður Clip alltaf í takt — eins og Clip hafi verið ræst alveg í upphafi klukkunnar. Þetta hentar vel þegar þú ert fullkomlega samstillt við tónlistina með ytra klukkumerki.

{% hint style="info" %}
Clips eru oft hönnuð til að lykkjast endalaust, en þú getur líka hannað þau þannig að þau keyri aðeins einu sinni eða nokkrum sinnum í gegn. Gættu þess að hafa slík Clips áfram stillt á _retrigger_, annars endurræsast þau ekki!
{% endhint %}

### Transition in/out time (fade)

Hægt er að stilla Clips þannig að þau dofni inn og út á tíma sem er mældur í sekúndum. Sjálfgefið erfir Clip dofnunartímann frá stillingum hópsins, og þeim er hægt að breyta með því að hægrismella á hóphnappinn.

Ef þú vilt nota annan dofnunartíma en hópur Clip notar skaltu fyrst slökkva á _USE GROUP DEFAULT_ og stilla síðan sleðana _In time_ og _Out time_ fyrir Clip.
