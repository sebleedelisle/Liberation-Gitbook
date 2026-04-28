---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Bylgjusveiflar

## Á þessari síðu :

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Sagtennt bylgja](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Þríhyrningsbylgja](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sínusbylgja](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Ferhyrningsbylgja](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Suð](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Sérsniðinn sveifill](wave-oscillators.md#custom-oscillator-1)

## Stillingar fyrir bylgjusveifla

Allir bylgjusveiflar hafa eftirfarandi stillingar :

* **range min / range max** - ákvarðar gildasviðið fyrir eigindið sem sveifillinn stjórnar. Eigindið er stillt á _range min_ þegar bylgjuformið er neðst, og á _range max_ þegar bylgjuformið er efst.

{% hint style="info" %}
Til dæmis, ef þú vilt láta punkt hreyfast til vinstri og hægri á milli -100 og 100, tengir þú sveiflinn við _x property socket_, stillir _min range_ á -100 og _max range_ á 100.
{% endhint %}

* **duration** - tíminn sem tekur að klára einn heilan hring (eða _loop_). Þetta er miðað við tempóið í taktbilum. Þannig er ¼ einn slagur. 1 er heilt taktbil o.s.frv.
* **duration multiplier** - margfaldar grunnlengdina með völdum stuðli. Til dæmis, ef duration er stillt á fjórðapartsnótu og margfaldarinn er 3, varir sveifillinn í þrjár fjórðapartsnótur (punktuð hálfnóta). Brotastuðlar eru líka studdir — haltu _SHIFT_ inni á meðan þú dregur sleðann til að stilla tölur sem eru ekki heilar. Þetta er gagnlegt fyrir fösunaráhrif eða til að búa til fínlegar tímabreytingar.
* **offset** - upphafshliðrun bylgjunnar sem hlutfall af duration. Ef þú vilt að bylgjan byrji fjórðung inn í ferlið, stillir þú þetta á 25%.
* **repeat count** - hversu oft loop keyrir áður en hann stöðvast. Sjálfgefið er _FOREVER_, en þú getur breytt því ef þú vilt ekki að sveifillinn keyri endalaust. Þegar hann stöðvast er eigindið stillt á gildið við enda bylgjunnar.
* **delay count** - seinkun í slögum áður en sveifillinn byrjar að keyra. Áður en hann byrjar að keyra er eigindið stillt á gildið við upphaf bylgjunnar.

{% hint style="info" %}
Með vandaðri notkun á _repeat count_ og _delay count_ getur þú búið til mjög flóknar hreyfingar, næstum eins og sérstaka tímalínu!
{% endhint %}

## Algengar stillingar

* **steps** - skiptir hreyfingunni í tiltekinn fjölda af aðskildum skrefum. Gott þegar þú vilt að eigindi „hoppi“ á milli gilda í stað þess að hreyfast mjúklega.

{% hint style="info" %}
Athugaðu að skrefunum er skipt eftir tíma, ekki eftir gildi. Þannig breytist eigindið samstundis í hverjum slagi fyrir bylgju sem er skipt í 4 skref og hefur duration upp á 1 taktbil.
{% endhint %}

* **clamp min / clamp max -** eykur skala bylgjunnar út fyrir lágmarks- eða hámarksgildi hennar og klemmir niðurstöðuna.

{% hint style="info" %}
Hugtakið _clamp_ getur verið svolítið erfitt að útskýra, en ímyndaðu þér að bylgjuformið fari upp fyrir eða niður fyrir grafið og sé síðan klemmt að jöðrunum. Ég mæli með að þú prófir þig áfram með þetta! Þetta er mjög gagnlegt ef þú vilt láta sagtennta bylgju byrja seint eða enda snemma.
{% endhint %}

* **ease function** - Sawtooth og Triangle bylgjurnar hafa líka ease function sem breytir hreyfikúrfunni lítillega og getur gert hreyfingarnar mun tjáningarmeiri!
  * **LINEAR** - sjálfgefið, engin mýking, hreyfist bara línulega á milli min og max gilda.
  * **EASE OUT** - byrjar hratt og hægir síðan á sér þegar nálgast endann. Mjög gott til að líkja eftir eðlisfræði, t.d. þegar eitthvað hægir á sér þar til það stöðvast.
  * **EASE IN** - byrjar hægt og eykur hraðann smám saman. Gott til að líkja eftir uppbyggingu skriðþunga.
  * **EASE IN/OUT** - sambland af hvoru tveggja og gefur mjög lífræna hreyfingu.

{% hint style="warning" %}
**Easing -** Ég myndi forðast sjálfgefna línulega hreyfingu þegar þú getur, nema þú viljir sérstaklega fá eitthvað sem lítur út fyrir að vera vélrænt. Easing getur gert hreyfingarnar miklu flæðandi og lífrænni!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sagtennt bylgja

Er líka stundum kölluð _ramp waveform_, þar sem hún hækkar jafnt og fellur síðan snöggt í lok hverrar lotu. Þetta er líklega algengasti bylgjusveifillinn, því hann býr til loop fyrir hringrásareigindi eins og _hue_ eða _rotation._

Sjá kaflana hér að ofan fyrir :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Sérstakt fyrir sagtennta bylgju :

* **cycle range compensation** - í boði þegar **steps** er stillt, og hentar vel til að láta gildi ganga í hring, til dæmis rotation frá 0 til 360. Þegar þetta er ekki virkt verða upphafs- og lokagildin eins, sem getur valdið því að hreyfingin festist við upphafspunktinn (þar sem 0 og 360 eru sami vinkillinn). Kveiktu á þessu og hámarkssviðið minnkar til að leiðrétta staðsetningu skrefanna.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Þríhyrningsbylgja

Ólíkt _sawtooth wave_, sem hoppar aftur í byrjun í hverri lotu, hreyfist _triangle wave_ línulega áfram og síðan aftur til baka.

Sjá kaflana hér að ofan fyrir :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sínusbylgja

Mýksta bylgjuformið! Sveiflast mjúklega á milli tveggja gilda, eins og pendúll.

Sjá kaflana hér að ofan fyrir :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Ferhyrningsbylgja

Einfaldasta bylgjuformið - hún skiptir bara á milli tveggja gilda, fram og til baka!

Sjá kaflana hér að ofan fyrir :

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Sérstakt fyrir ferhyrningsbylgju :

* **pulse width** - hversu lengi bylgjan er í hámarksgildi miðað við heildarlengdina. 50% er sjálfgefið, sem er nákvæmlega helmingur og helmingur. Ef þú vilt aðeins hafa hana „kveikta“ í fjórðung tímans, stillir þú þetta á 25%. Þú getur stillt hvenær þessi púls gerist með _offset_ gildinu.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Suð

Einn af styrkleikum Liberation er að það getur búið til handahófskennd áhrif sem eru samt endurtekningarhæf. _noise_ sveifillinn er hægt að nota til að búa til lífræna, lykkjandi handahófshreyfingu með eins miklum smáatriðum eða titringi og þú vilt.

Sjá kaflana hér að ofan fyrir :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Sérstakt fyrir suð :

* **noise type** - reikniritið sem er notað til að búa til suðið.
  * **SIMPLEX** - sjálfgefið, bylgjandi gildi sem rís og hnígur og endurtekur sig í loop.
  * **RANDOM** - notar hefðbundnara slembitölureiknirit, algjörlega suðkennt og óreiðukennt.

{% hint style="info" %}
**Simplex noise** var hannað af Ken Perlin árið 2001 sem endurbót á „Perlin noise“ reikniritinu hans, sem hann þróaði árið 1983 sem hluta af vinnu sinni við kvikmyndina _Tron_ (sem hann fékk Óskar fyrir!)

Þetta svokallaða „gradient“ suð varð til vegna óánægju hans með tölvugerðar myndir sem litu áður of „vélrænt“ út. Í CGI-heiminum hentar það sérstaklega vel til að teikna ský, vatnsyfirborð eða jafnvel hæðarkort fyrir raunhæft landslag.

Í Liberation er það hins vegar gott fyrir hreyfingu sem virðist ófyrirsjáanleg en er samt mjúk og lífræn.
{% endhint %}

* **seed** - gildið sem er notað til að búa til suðið. Ef þér líkar ekki útlitið á noise wave sem þú ert með, prófaðu að breyta þessu gildi.

{% hint style="info" %}
Skemmtileg nördaleg staðreynd! Til að fá simplex noise sem myndar fullkominn loop fer ég í hring á tvívíðum suðfleti. Og þegar seed gildinu er breytt færist þessi flötur í gegnum þriðju víddina!
{% endhint %}

* **simplex detail** - breytir því hversu ítarlegt eða titrandi suðið er. Ef þú vilt að endurtekningarmynstrið sé minna áberandi skaltu lengja duration og hækka þetta gildi.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Sérsniðinn sveifill

Býr til alveg sérsniðið bylgjuform. Þetta er mjög gagnlegt til að búa til flóknar hreyfingar.

Sjá kaflana hér að ofan fyrir :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Fyrir neðan þetta er listi yfir stöður og gildi. Duration er skipt í 64 skref og þú getur sett gildi á hvaða punkt sem er.

Hvert skref hefur eftirfarandi stillingar :

* **Step** - tímaskrefið innan duration. 0 er í byrjun og 64 er í lokin.
* **Level** - stig bylgjunnar á því tímaskrefi. Level er á bilinu 0 til 1.
* **Animation type** - fellivalmyndin gerir þér kleift að velja hvernig þú vilt færa þig að þessu stigi frá fyrra skrefi.
  * **None** - engin umbreyting, hoppar beint á þetta stig á tilgreindum tíma.
  * **Linear** - alveg línuleg hreyfing frá fyrra stigi að þessu.
  * **Ease in / Ease out / Ease in/out** - mýkir hreyfinguna frá fyrra stigi að þessu. Sjá _ease function_ hér að ofan fyrir lýsingu á hreyfingargerðunum.

***
