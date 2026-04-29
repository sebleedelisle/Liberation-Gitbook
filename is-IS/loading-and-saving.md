---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Hlaða inn og vista

Liberation vistar stöðuna sína stöðugt á disk. Þannig geturðu treyst því að ef rafmagn fer af eða kerfisvandamál kemur upp, þá ræsist forritið aftur þar sem frá var horfið. Þú ættir ekki að tapa zones, tímalínu eða öðru efni.

Þú getur þó flutt uppsetninguna þína út til að taka öryggisafrit eða færa hana yfir á aðra tölvu.

### Innflutningur / útflutningur verkefnis

Verkefnisskráin geymir nánast allt í núverandi uppsetningu, þar á meðal:

* Allt sem er lýst í [Innflutningur / útflutningur á Laser Settings](loading-and-saving.md#laser-settings-import-export) hér að neðan
* Clips, áhrif og hópstillingar
* Allar tímalínurnar þínar (ekki hljóð- og myndmiðlun)
* Uppsetning fyrir ArtNet
* Stillingar fyrir MIDI sendingu/móttöku
* Stillingar fyrir tempó / samstillingu

Hún vistar og hleður sem stendur ekki:

* Stillingar fyrir hljóð- og MIDI-inntak eins og þær eru notaðar í MIDI notes node og Sound Input Oscillator (hún _vistar_ stillingar fyrir MIDI sendingu/móttöku ásamt hljóðinntaki fyrir tímakóða)
* Stærðarkvarða viðmóts
* Miðlun fyrir leiðbeiningarmyndir í Canvas
* Hljóð- og myndmiðlun fyrir tímalínur
* Leturgerðir sem Text node notar

{% hint style="danger" %}
Hljóð- og myndskrár á tímalínunni eru ekki vistaðar með verkefnisskrám, svo vistaðu þær sérstaklega ef þú vilt færa þær yfir á aðra tölvu. Sjá [Mikilvæg athugasemd um miðlunarskrár í tímalínum](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Innflutningur / útflutningur á Laser Settings

* Laser Settings fyrir hvern laser
* Beam zones
* Marksvæði fyrir Canvas
* DMX zones
* Hvaða laser controller er úthlutað hverjum laser (og samnefni fyrir controller sem þú hefur endurnefnt)
* Stillingar og forstillingar fyrir leysiskanna og litakvörðun
* Stillingar og forstillingar fyrir 3D-sýn

### Innflutningur / útflutningur á Clip Deck

* Öll Clips og hvaða zones þau eru tengd við, auk stillinga og færibreyta
* Allar hópstillingar, flash mode, tímar fyrir fade in/out o.s.frv.

Það vistar og hleður sem stendur ekki:

* Öll áhrif og færibreytur þeirra og stillingar

{% hint style="info" %}
**Hlaða Clips úr verkefnisskrá án þess að hlaða inn öllu verkefninu**

Til að flytja aðeins inn Clips úr verkefni skaltu velja _**Clips->Import Clip Deck**_ og velja verkefnisskrá í stað skráar fyrir Clip Deck (.cpdk).
{% endhint %}

### Bæta Clip Deck við

Þú getur bætt Clips úr útfluttri skrá fyrir Clip Deck við núverandi verkefni með _Append Clip Deck_. Clips er bætt við aftast í núverandi Clip Deck, en áhrif og hópstillingar í skránni eru ekki flutt inn.

### Flytja út valin Clips

Öll Clips sem eru valin verða flutt út í skrá. Hópstillingar og áhrif verða ekki vistuð, aðeins Clips. Athugaðu að virk Clips sem eru í gangi eru ekki flutt út nema þau séu líka valin.

{% hint style="info" %}
Haltu inni Option/Alt - shift og smelltu á Clips til að velja þau (eða notaðu lasso). Þú sérð hvaða Clips eru valin á þykkri hvítri útlínu í kringum þau. Sjá [Ræsa og stöðva Clips](clips/starting-stopping-clips.md)
{% endhint %}

### Innflutningur / útflutningur á áhrifum

Hleður inn og vistar öll áhrif ásamt hópstillingum þeirra og færibreytum.

{% hint style="info" %}
**Hlaða áhrifum úr verkefnisskrá án þess að hlaða inn öllu verkefninu**

Til að flytja aðeins inn áhrif úr verkefni skaltu velja _**Effects->Import Effects**_ og velja verkefnisskrá í stað áhrifaskrár (.efts).
{% endhint %}

### Útflutningur tímalínu

Flyttu út tímalínuskrá með einni eða fleiri tímalínum. Athugaðu að Clip Deck fylgir alltaf með útfluttum tímalínuskrám (þó þú getir valið hvaða Clips þú flytur aftur inn, sjá [Innflutningur tímalína](loading-and-saving.md#timeline-import) hér að neðan).

Ef verkefnisskráin þín inniheldur fleiri en eina tímalínu opnast panel þar sem þú getur valið hvaða tímalínur þú vilt flytja út.

{% hint style="danger" %}
Hljóð- og myndskrár á tímalínunni eru ekki vistaðar með tímalínuskrám, svo vistaðu þær sérstaklega ef þú vilt færa efnið þitt yfir á aðra tölvu. Sjá [Mikilvæg athugasemd um miðlunarskrár í tímalínum](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Innflutningur tímalína

Flyttu inn eina eða fleiri tímalínur úr einni tímalínuskrá. Þegar þú hefur valið tímalínuskrána opnast panel með nokkrum innflutningsvalkostum.

Ef tímalínuskráin inniheldur fleiri en eina tímalínu birtast þær allar á lista. Hakaðu við þær sem þú vilt taka með.

* Replace existing timelines\
  Eyðir öllum núverandi tímalínum og setur þær innfluttu í staðinn
* Import used clips only\
  Flytur aðeins inn þau Clips sem eru notuð og raðar þeim í hópa, einn fyrir hverja tímalínu. Ef þessi valkostur er ekki valinn verður öllu Clip Deck úr tímalínuskránni bætt við núverandi Clips.
* Replace existing clip deck\
  Skiptir út núverandi Clip Deck fyrir Clips í tímalínuskránni. Aðeins í boði ef _Replace existing timelines_ er valið.

{% hint style="info" %}
**Hlaða tímalínum úr verkefnisskrá án þess að hlaða inn öllu verkefninu**

Til að flytja aðeins inn tímalínur úr verkefni skaltu velja _**Timeline->Import Timeline(s)**_ og velja verkefnisskrá í stað tímalínuskrár (.ltml).
{% endhint %}

### Innflutningur / útflutningur á DMX / ArtNet

Vistar og hleður inn ArtNet nodes ásamt IP-tölum þeirra. Inniheldur einnig DMX zones og allar DMX-forstillingarnar þínar.

### Mikilvæg athugasemd um miðlunarskrár í tímalínum

Hljóð- og myndskrár eru **ekki** fluttar út með tímalínuskránni eins og er. Ef þú þarft að færa efni yfir á aðra tölvu skaltu því ganga úr skugga um að þessar skrár fylgi með.

{% hint style="info" %}
**Hvernig tímalína leitar að miðlunarskrám**

Þegar tímalína er hlaðin inn leitar hún í sömu möppu og tímalínuskráin (eða verkefnisskráin) er í, ásamt undirmöppum. Svo lengi sem skrárnar eru í sömu möppu eða undirmöppu (eins og _/videos_ eða _/sound_) finnur hún þær þegar hún hleður.
{% endhint %}
