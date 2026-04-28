---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Hleðsla og vistun

Liberation vistar stöðu sína stöðugt á disk. Þannig geturðu treyst því að ef rafmagn fer af eða kerfisvandamál kemur upp, ræsist forritið aftur þar sem það var statt. Þú ættir því ekki að missa svæði, tímalínur eða annað efni.

Þú getur þó flutt uppsetninguna út til öryggisafritunar eða til að færa hana yfir á aðra tölvu.

### Innflutningur / útflutningur á verkefni

Verkefnisskráin geymir nánast allt í núverandi uppsetningu, þar á meðal:

* Allt sem er nánar lýst í [#laser-settings-import-export](loading-and-saving.md#laser-settings-import-export) hér fyrir neðan
* Clip, áhrif og hópstillingar
* Allar tímalínurnar þínar (án hljóð- og myndmiðla)
* ArtNet-uppsetningu
* MIDI send/receive stillingar
* Tempo / samstillingarstillingar

Sem stendur vistar og hleður hún ekki:

* Sound og Midi input settings eins og þær eru notaðar í MIDI notes node og Sound Input Oscillator (hún _vistar_ þó MIDI send/receive stillingar ásamt timecode sound input)
* Interface scaling
* Miðla fyrir Canvas guide images
* Hljóð- og myndmiðla fyrir tímalínur
* Leturgerðir sem eru notaðar í Text node

{% hint style="danger" %}
Hljóð- og myndskrár á tímalínunni eru ekki vistaðar með verkefnisskrám, svo vertu viss um að vista þær sérstaklega ef þú vilt færa efnið yfir á aðra tölvu. Sjá [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Innflutningur / útflutningur á Laser settings

* Laser settings fyrir hvern laser
* Beam zones
* Canvas target areas
* DMX zones
* Úthlutun laser controller (og alias fyrir controller-a sem þú hefur endurnefnt)
* Laser scanner og colour calibration settings og presets
* 3D Visualiser stillingar og presets

### Innflutningur / útflutningur á Clip Deck

* Öll Clip og zone assignments þeirra, stillingar og breytur
* Allar group settings, flash mode, fade in/out times o.s.frv.

Sem stendur vistar og hleður það ekki:

* Öllum effects og breytum þeirra og stillingum

{% hint style="info" %}
**Hlaða Clip úr verkefnisskrá án þess að hlaða allt verkefnið**

Til að flytja aðeins Clip úr verkefni inn skaltu velja _**Clips->Import Clip Deck**_ og velja verkefnisskrá í stað þess að velja clip deck skrá (.cpdk).
{% endhint %}

### Append Clip Deck

Þú getur bætt Clip úr útfluttri clip deck skrá við núverandi verkefni með _Append Clip Deck_. Clip bætast við í lok núverandi Clip Deck, en effects og group settings í skránni eru ekki flutt inn.

### Export Selected Clips

Öll Clip sem eru valin í augnablikinu verða flutt út í skrá. Group settings og effects vistast ekki, aðeins Clip. Athugaðu að virk Clip sem eru í keyrslu eru ekki flutt út nema þau séu einnig valin.

{% hint style="info" %}
Notaðu Option/Alt - shift - click á Clip til að velja þau (eða notaðu lasso). Þú sérð hvaða Clip eru valin á þykku hvítu útlínunni utan um þau. Sjá [starting-stopping-clips.md](clips/starting-stopping-clips.md)
{% endhint %}

### Innflutningur / útflutningur á Effects

Hleður og vistar öll effects ásamt group settings og breytum þeirra.

{% hint style="info" %}
**Hlaða effects úr verkefnisskrá án þess að hlaða allt verkefnið**

Til að flytja aðeins effects úr verkefni inn skaltu velja _**Effects->Import Effects**_ og velja verkefnisskrá í stað þess að velja effects skrá (.efts).
{% endhint %}

### Útflutningur á tímalínu

Flyttu út tímalínuskrá með einni eða fleiri tímalínum. Athugaðu að Clip Deck fylgir alltaf með útfluttum tímalínuskrám (þó þú getir valið hvaða Clip þú flytur aftur inn, sjá [#timeline-import](loading-and-saving.md#timeline-import) hér fyrir neðan).

Ef fleiri en ein tímalína er í verkefnisskránni opnast panel þar sem þú getur valið hvaða tímalínur þú vilt flytja út.

{% hint style="danger" %}
Hljóð- og myndskrár á tímalínunni eru ekki vistaðar með tímalínuskrám, svo vertu viss um að vista þær sérstaklega ef þú vilt færa efnið yfir á aðra tölvu. Sjá [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Innflutningur á tímalínu

Flyttu inn eina eða fleiri tímalínur úr einni tímalínuskrá. Eftir að þú hefur valið tímalínuskrána opnast panel með nokkrum innflutningsvalkostum.

Ef tímalínuskráin inniheldur fleiri en eina tímalínu birtast þær allar á lista. Hakaðu við þær sem þú vilt hafa með.

* Replace existing timelines\
  Eyðir öllum núverandi tímalínum og setur þær innfluttu í staðinn
* Import used clips only\
  Flytur aðeins inn Clip sem eru notuð og raðar þeim í hópa, einn hóp fyrir hverja tímalínu. Ef þessi valkostur er ekki valinn verður öllu Clip Deck úr tímalínuskránni bætt við núverandi Clip.
* Replace existing clip deck\
  Skiptir núverandi Clip Deck út fyrir Clip í tímalínuskránni. Aðeins í boði ef _Replace existing timelines_ er valið.

{% hint style="info" %}
**Hlaða tímalínum úr verkefnisskrá án þess að hlaða allt verkefnið**

Til að flytja aðeins tímalínurnar úr verkefni inn skaltu velja _**Timeline->Import Timeline(s)**_ og velja verkefnisskrá í stað þess að velja tímalínuskrá (.ltml).
{% endhint %}

### Innflutningur / útflutningur á DMX / ArtNet

Vistar og hleður ArtNet nodes ásamt IP-vistföngum þeirra. Inniheldur einnig DMX zones og öll DMX presets.

### Mikilvæg athugasemd um miðlaskrár á tímalínu

Hljóð- og myndskrár eru **ekki** fluttar út með tímalínuskránni sem stendur, svo ef þú þarft að færa efni yfir á aðra tölvu skaltu ganga úr skugga um að þær fylgi með.

{% hint style="info" %}
**Hvernig tímalína leitar að miðlaskrám**

Þegar tímalínunni er hlaðið leitar hún í sömu möppu og tímalínuskráin (eða verkefnisskráin) er í, og leitar innan hennar og allra undirmappa. Svo lengi sem skrárnar eru í sömu möppu eða undirmöppu (til dæmis _/videos_ eða _/sound_) finnur hún þær við hleðslu.
{% endhint %}
