---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Tímakóði

Liberation styður samstillingu við ytra SMPTE/LTC-tímakóðamerki, sem er algengt í tónleikasýningum til að halda ljósum, pyrotækni, myndbandi og bakröddum eða undirspili í takt.

{% hint style="info" %}
Hvað er SMPTE/LTC?

SMPTE er staðall fyrir tímakóða og LTC er þessi tímakóði umbreyttur í hljóðmerki. Ef þú hlustar á þetta hljóð hljómar það eins og hræðilegt, skerandi hátíðnivein, en fyrir tölvur eru þetta tímasetningarupplýsingar í mikilli upplausn.

**Nörda staðreyndir!**

Sögulega hefur SMPTE verið notað til að halda mynd og hljóði samstilltu. Þegar samstillt var við hliðrænt segulband var ein rás stundum tekin undir tímakóðahljóðið, oft kallað að „strípa“ bandið. Þú gast notað þessa tímakóðarás til að halda mörgum segulbandstækjum í takt hvert við annað, eða til að halda MIDI-sequencer í takt við bandið. (Þá þurftirðu ekki að taka MIDI-hljóðfæri upp á band, heldur gast látið sequencer spila þau beint á meðan þú blandaðir!)

SMPTE stendur fyrir Society of Motion Picture and Television Engineers, sem skilgreindu staðalinn. LTC stendur fyrir _Linear TimeCode._
{% endhint %}

Þú getur tekið á móti LTC-tímakóðamerki í gegnum hvaða hljóðviðmót sem er í tölvunni þinni, en mælt er með faglegu viðmóti með að minnsta kosti einu stillanlegu XLR-inntaki og möguleika á hlustun.

Ég hef góða reynslu af [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), þar sem það er með heyrnartólahlustun, 2 XLR-inntök og þarf enga sérstaka rekla (að minnsta kosti í macOS). Ef þú ætlar eingöngu að nota það fyrir tímakóða geturðu fengið aðeins ódýrara [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (sem er aðeins með eitt inntak og ekkert MIDI), en í hreinskilni sagt ætti hvaða sæmilega hljóðviðmót sem er að virka.

{% hint style="info" %}
LTC-tímakóðamerki eru yfirleitt send um balanced XLR-kapla, þar sem þeir eru nógu traustir til að flytja hljóðmerki á lágum styrk yfir langar vegalengdir. (XLR er sívalningslaga tengið sem er venjulega notað með hljóðnemum)
{% endhint %}

### Vélbúnaðartengingar

Tengdu XLR-kapalinn með tímakóðamerkinu við hljóðviðmótið og gakktu úr skugga um að merkið sé gott. Stilltu styrkinn á hljóðviðmótinu þar til merkið er sterkt en ekki að klippa. Ef hljóðviðmótið er með heyrnartólstengi geturðu hlustað á tímakóðann og gengið úr skugga um að hann hiksti ekki og að það sé ekki of mikill suð eða truflun í merkinu.

{% hint style="info" %}
Fræðilega séð er hægt að taka á móti merkinu í gegnum jack-tengið á MacBook, en það krefst sérsmíðaðs kapals. Þessi tengi eru yfirleitt 4-póla TRRS mini jack-tengi og ég er satt að segja ekki viss hvaða pinnar í þeim er hægt að nota fyrir hljóðinntak. Ég er heldur ekki viss hvaða spennustig þau þola (ég las einhvers staðar að það væri +/-1V, en notaðu þetta á eigin ábyrgð!)

Ég held að það sé mun skynsamlegra að ná þér bara í ódýrt USB-hljóðviðmót frekar en að reyna þetta.
{% endhint %}

Ef hljóðviðmótið þitt býður ekki upp á neina inntakshlustun geturðu athugað í kerfisstillingum macOS (undir _Sound_) hvort merki sé að berast. (Í Windows skaltu nota _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS sýnir inntaksstyrk fyrir hvaða hljóðviðmót sem er í Sound-kerfisstillingaspjaldinu</p></figcaption></figure>

### Uppsetning í Liberation

1. Veldu hljóðviðmótið þitt og rétta inntaksrás í glugganum Timecode settings Window.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Athugaðu að í fellivalmyndinni eru aðskildir valkostir fyrir hverja inntaksrás í hljóðviðmótinu þínu

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Taktu eftir ferningnum til vinstri. Ef gilt tímakóðamerki berst verður hann grænn. Ef ekki verður hann rauður.

2. Veldu réttan rammahraða fyrir tímakóðann sem berst inn. Sá sem útvegar þér tímakóðann ætti að geta sagt þér hver rammahraðinn er. (Ef þú velur rangt samstillist þetta samt, en þú munt taka eftir litlu „hoppi“ á hverri sekúndu)
3. Opnaðu timecode settings fyrir tímalínuna með litla klukkutákninu á tímalínustikunni og veldu valkostinn SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Stilltu upphafshliðrunina (í klukkustundum, mínútum, sekúndum og römmum) þannig að hún passi við upphaf lagsins. Ef þú ert með margar tímalínur þarftu að stilla þessa valkosti sérstaklega fyrir hverja þeirra.

{% hint style="info" %}
Í tónleikaferðabransanum er algengt viðmið að hvert lag byrji á annarri klukkustund, t.d. 01:00:00:00 fyrir fyrsta lagið, 02:00:00:00 fyrir annað lagið og svo framvegis.

Liberation skiptir sjálfkrafa yfir á tímalínuna út frá tímakóðanum, þannig að þú þarft aldrei að skipta handvirkt um tímalínu meðan á sýningu stendur.
{% endhint %}

Athugaðu að ólíkt MIDI Clock og Ableton Link er SMPTE _algilt_ tímakerfi, mælt í klukkustundum, mínútum, sekúndum og römmum. Grunntímakerfi Liberation byggir á slögum og töktum, þannig að þegar þú tekur á móti tímakóða notar Liberation tempóið sem er stillt í tímalínunni. Þú þarft að ganga úr skugga um að þetta tempó sé samstillt við þá tónlist sem er einnig samstillt við tímakóðann.
