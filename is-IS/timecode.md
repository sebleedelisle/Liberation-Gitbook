---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Tímakóði

Liberation styður samstillingu við ytra SMPTE/LTC-tímakóðamerki, sem er oft notað á tónleikum til að halda ljósum, flugeldabrellum, myndbandi og undirspili í takt.

{% hint style="info" %}
Hvað er SMPTE/LTC?

SMPTE er staðall fyrir tímakóða og LTC er þessi tímakóði umbreyttur í hljóðmerki. Ef þú hlustar á þetta hljóð hljómar það eins og hræðilegt, hátíðni ískur, en fyrir tölvur eru þetta nákvæmar tímasetningarupplýsingar.

**Nördastaðreyndir!**

Sögulega hefur SMPTE verið notað til að halda myndbandi og hljóði samstilltu. Þegar samstillt var við hliðræna segulbandsspólu var tímakóðahljóðið stundum tekið upp á eina rás, sem var kallað að „strípa“ bandið. Þú gast notað þessa tímakóðarás til að halda mörgum segulbandstækjum samstilltum, eða til að halda MIDI-raðara í takt við bandið. (Þannig þurftirðu ekki að taka MIDI-hljóðfæri upp á band; raðarinn gat einfaldlega spilað þau í beinni á meðan þú varst að mixa!)

SMPTE stendur fyrir Society of Motion Picture and Television Engineers, sem skilgreindu staðalinn. LTC stendur fyrir _Linear TimeCode._
{% endhint %}

Þú getur tekið á móti LTC-tímakóðamerki í gegnum hvaða hljóðviðmót sem er á tölvunni þinni, en mælt er með að nota faglegt viðmót með að minnsta kosti einu stillanlegu XLR-inntaki og möguleika á hlustun.

Ég hef góða reynslu af [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), þar sem það er með heyrnartólshlustun, 2 XLR-inntök og þarf enga sérstaka rekla (að minnsta kosti á macOS). Ef þú ætlar aðeins að nota það fyrir tímakóða geturðu keypt aðeins ódýrara [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (sem er aðeins með eitt inntak og ekkert MIDI), en í hreinskilni sagt ætti hvaða sæmilegt hljóðviðmót sem er að virka.

{% hint style="info" %}
LTC-tímakóðamerki eru yfirleitt send um jafnvægis-XLR-kapla, þar sem þeir eru nógu traustir til að flytja lágstyrks hljóðmerki yfir langar vegalengdir. (XLR er hólklaga tengið sem er venjulega notað með hljóðnemum)
{% endhint %}

### Vélbúnaðartengingar

Tengdu XLR-kapal tímakóðamerkisins við hljóðviðmótið þitt og gakktu úr skugga um að merkið sé gott. Stilltu styrkinn á hljóðviðmótinu þar til merkið er sterkt en ekki að bjagast. Ef hljóðviðmótið er með heyrnartólstengi geturðu hlustað á tímakóðann og gengið úr skugga um að hann detti ekki út og sé ekki með of mikinn suð eða truflanir.

{% hint style="info" %}
Fræðilega er hægt að taka á móti merkinu í gegnum jack-tengið á MacBook, en það krefðist sérsmíðaðs kapals. Þessi tengi eru yfirleitt 4 póla TRRS-mini jack-tengi, og ég er satt að segja ekki viss hvaða tengi er hægt að nota sem hljóðinntak. Ég er heldur ekki viss hvaða spennustig það þolir (ég hef lesið einhvers staðar að það sé +/-1V, en notaðu þetta á eigin ábyrgð!)

Ég held að það sé betra fyrir þig að útvega þér ódýrt USB-hljóðviðmót frekar en að reyna þetta.
{% endhint %}

Ef hljóðviðmótið þitt er ekki með neina inntakshlustun geturðu athugað í kerfisstillingum macOS (undir _Sound_) að þú sért að fá merki. (Í Windows skaltu nota _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS sýnir inntaksstyrk fyrir hvaða hljóðviðmót sem er í Sound-kerfisstillingaspjaldinu</p></figcaption></figure>

### Uppsetning í Liberation

1. Veldu hljóðviðmótið þitt og rétta inntaksrás í Timecode settings Window.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Athugaðu að það eru aðskildir valkostir í fellivalmyndinni fyrir hverja inntaksrás í hljóðviðmótinu þínu

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Taktu eftir ferningnum vinstra megin. Ef þú ert að taka á móti gildu tímakóðamerki verður hann grænn. Ef ekki verður hann rauður.

2. Veldu réttan rammahraða fyrir tímakóðann sem kemur inn. Sá sem útvegar þér tímakóðann ætti að geta sagt þér hver rammahraðinn er. (Ef þú velur rangt mun samstillingin samt virka, en þú munt taka eftir litlu „hoppi“ á hverri sekúndu)
3. Opnaðu tímakóðastillingar Timeline með litla klukkutákninu á timeline-stikunni og veldu SMPTE(LTC) valkostinn.

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Stilltu upphafshliðrunina (í klukkustundum, mínútum, sekúndum, römmum) þannig að hún passi við upphaf lagsins. Ef þú ert með mörg Timeline þarftu að stilla þessa valkosti sérstaklega fyrir hvert þeirra.

{% hint style="info" %}
Í tónleikaferðabransanum er algeng venja að láta hvert lag byrja á annarri klukkustund, t.d. 01:00:00:00 fyrir fyrsta lagið, 02:00:00:00 fyrir annað lagið og svo framvegis.

Liberation skiptir sjálfkrafa yfir í rétt Timeline eftir tímakóðanum, svo þú þarft aldrei að skipta handvirkt um Timeline á meðan á sýningu stendur.
{% endhint %}

Athugaðu að ólíkt MIDI Clock og Ableton Link er SMPTE _algilt_ tímakerfi, mælt í klukkustundum, mínútum, sekúndum og römmum. Grunntímakerfi Liberation byggir á slögum og töktum, þannig að þegar þú tekur á móti tímakóða notar það tempóið sem er stillt í Timeline. Þú þarft að ganga úr skugga um að þetta tempó sé samstillt við þá tónlist sem er einnig samstillt við tímakóðann.
