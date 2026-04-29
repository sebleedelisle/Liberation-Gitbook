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

* **range min / range max** - ákvarðar gildasvið eiginleikans sem sveifillinn stjórnar. Eiginleikinn er stilltur á _range min_ þegar bylgjulögunin er neðst og á _range max_ þegar bylgjulögunin er efst.

{% hint style="info" %}
Til dæmis, ef þú vilt láta punkt hreyfast til vinstri og hægri á milli -100 og 100, tengirðu sveifilinn við _x property socket_, stillir _min range_ á -100 og _max range_ á 100.
{% endhint %}

* **duration** - tíminn sem tekur að ljúka einum heilum ferli (eða _loop_). Þetta er miðað við taktinn í töktum. Þannig er ¼ einn sláttur. 1 er einn heill taktur, o.s.frv.
* **duration multiplier** - margfaldar grunntímalengdina með völdum stuðli. Til dæmis, ef duration er stillt á fjórðapartsnótu og margfaldarinn er 3, varir sveifillinn í þrjár fjórðapartsnótur (punkteruð hálfnóta). Brotastuðlar eru líka studdir — haltu _SHIFT_ inni á meðan þú dregur sleðann til að stilla gildi sem eru ekki heilar tölur. Þetta er gagnlegt fyrir fösunaráhrif eða til að búa til fíngerðar tímabreytingar.
* **offset** - upphafshliðrun bylgjunnar sem hlutfall af duration. Ef þú vilt að bylgjan byrji fjórðung af leiðinni inn í ferlið skaltu stilla þetta á 25%.
* **repeat count** - fjöldi skipta sem lykkjan keyrir áður en hún stöðvast. Sjálfgefið er _FOREVER_, en þú getur breytt því ef þú vilt ekki að sveifillinn keyri endalaust. Þegar hann stöðvast er eiginleikinn stilltur á gildið við enda bylgjunnar.
* **delay count** - töf í slögum áður en sveifillinn byrjar að keyra. Áður en hann byrjar að keyra er eiginleikinn stilltur á gildið við upphaf bylgjunnar.

{% hint style="info" %}
Með vandaðri notkun á _repeat count_ og _delay count_ geturðu búið til mjög flóknar hreyfimyndir, næstum eins og sérstaka tímalínu!
{% endhint %}

## Sameiginlegar stillingar

* **steps** - skiptir hreyfingunni niður í tiltekinn fjölda aðgreindra þrepa. Þetta hentar vel þegar þú vilt að eiginleikar „stökkvi“ á milli gilda í stað þess að hreyfast mjúklega.

{% hint style="info" %}
Athugaðu að þrepin eru skipt eftir tíma, ekki gildi. Þannig breytist eiginleikinn samstundis við hvern slátt ef bylgja er skipt í 4 þrep og duration er 1 taktur.
{% endhint %}

* **clamp min / clamp max -** eykur skala bylgjunnar út fyrir lágmarks- eða hámarksgildi hennar og klemmir niðurstöðuna.

{% hint style="info" %}
Hugtakið _clamp_ er frekar erfitt að útskýra, en ímyndaðu þér að bylgjulögunin fari upp fyrir eða niður fyrir grafið og sé síðan klemmd við brúnirnar. Ég mæli með að þú prófir þig áfram með þetta! Þetta er mjög gagnlegt ef þú vilt láta sagtennta bylgju byrja seint eða enda snemma.
{% endhint %}

* **ease function** - sagtennta bylgjan og þríhyrningsbylgjan hafa einnig mýkingarfall sem breytir hreyfikúrfunni á fíngerðan hátt og getur gert hreyfimyndirnar mun tjáningarríkari!
  * **LINEAR** - sjálfgefið, engin mýking; hreyfist einfaldlega línulega á milli lágmarks- og hámarksgilda.
  * **EASE OUT** - byrjar hratt og hægir síðan á sér þegar komið er að endanum. Mjög gott til að líkja eftir eðlisfræði, t.d. að hægja á sér þar til stöðvast.
  * **EASE IN** - byrjar hægt og eykur hraðann smám saman. Hentar vel til að líkja eftir vaxandi skriðþunga.
  * **EASE IN/OUT** - blanda af báðu, með mjög lífrænni hreyfingu.

{% hint style="warning" %}
**Easing -** Ég myndi forðast sjálfgefnu línulegu hreyfinguna þegar þú getur, nema þú viljir sérstaklega fá eitthvað sem lítur vélrænt út. Easing getur gert hreyfimyndirnar miklu flæðandi og lífrænni!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sagtennt bylgja

Er stundum einnig kölluð _ramp waveform_ vegna þess að hún rís upp á við og fellur síðan skarpt niður við enda ferilsins. Þetta er líklega algengasti bylgjusveifillinn, þar sem hann býr til lykkju fyrir eiginleika sem eiga að fara í hring, eins og _hue_ eða _rotation._

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

* **cycle range compensation** - tiltækt þegar **steps** er stillt og hentar vel fyrir gildi sem eiga að fara í hring, til dæmis rotation frá 0 til 360. Þegar þetta er ekki virkt verða upphafs- og lokagildin eins, sem getur valdið því að hreyfingin festist við upphafspunktinn (þar sem 0 og 360 eru sama hornið). Kveiktu á þessu og hámarkssviðið verður minnkað til að leiðrétta stöðu þrepanna.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Þríhyrningsbylgja

Ólíkt _sagtenntri bylgju_, sem hoppar aftur á byrjunina í hverjum ferli, hreyfist _þríhyrningsbylgja_ línulega áfram og síðan aftur til baka.

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

Mýksta bylgjulögunin! Sveiflast mjúklega á milli tveggja gilda eins og pendúll.

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

Einfaldasta bylgjulögunin - hún skiptir einfaldlega á milli tveggja gilda, fram og til baka!

Sjá kaflana hér að ofan fyrir :

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Sérstakt fyrir ferhyrningsbylgju :

* **pulse width** - tíminn sem bylgjan er á hámarksgildi sínu miðað við heildar duration. 50% er sjálfgefið, sem þýðir nákvæmlega helmingur og helmingur. Ef þú vilt aðeins hafa hana „kveikta“ í fjórðung tímans skaltu stilla þetta á 25%. Þú getur stillt hvenær þessi púls gerist með _offset_ gildinu.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Suð

Einn af styrkleikum Liberation er að það getur búið til tilviljanakennd áhrif sem eru samt endurtakanleg. _Suð_-sveifilinn má nota til að búa til lífræna, endurtekna tilviljanahreyfingu með eins miklum smáatriðum eða skjálfta og þú vilt.

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
  * **SIMPLEX** - sjálfgefið, sveiflukennt gildi sem rís og hnígur og endurtekur sig í lykkju.
  * **RANDOM** - notar hefðbundnara slembitölureiknirit; algjörlega suðkennt og óreiðukennt.

{% hint style="info" %}
**Simplex noise** var hannað af Ken Perlin árið 2001 sem endurbót á „Perlin noise“ reikniritinu hans, sem hann þróaði árið 1983 sem hluta af vinnu sinni við kvikmyndina _Tron_ (sem hann fékk Óskarsverðlaun fyrir!)

Þetta svokallaða „gradient“-suð varð til út frá gremju hans með fyrri tölvugerða myndgerð sem honum fannst of „vélræn“. Í CGI-heiminum hentar það sérstaklega vel til að teikna ský, vatnsyfirborð eða jafnvel hæðarkort fyrir raunhæft landslag.

Í Liberation er það hins vegar gagnlegt fyrir hreyfingu sem virðist óútreiknanleg en er samt mjúk og lífræn.
{% endhint %}

* **seed** - gildið sem er notað til að búa til suðið. Ef þér líkar ekki útlit suðbylgjunnar skaltu prófa að breyta þessu gildi.

{% hint style="info" %}
Skemmtileg nördastaðreynd! Til að fá simplex noise sem lykkjast fullkomlega fer ég í hring á tvívíðu suðplani. Og þegar seed-gildinu er breytt færist þetta plan í gegnum þriðju víddina!
{% endhint %}

* **simplex detail** - breytir því hversu ítarlegt eða skjálfandi suðið er. Ef þú vilt að endurtekna mynstrið sé síður augljóst skaltu hækka duration og auka þetta gildi.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Sérsniðinn sveifill

Býr til alveg sérsniðna bylgjulögun. Þetta er mjög gagnlegt til að búa til flóknar hreyfimyndir.

Sjá kaflana hér að ofan fyrir :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Fyrir neðan þetta er listi yfir stöður og gildi. Duration er skipt í 64 þrep og þú getur sett gildi á hvaða punkt sem er.

Hvert þrep hefur eftirfarandi stillingar :

* **Step** - tímaþrepið innan duration. 0 er við upphafið og 64 er við endann.
* **Level** - styrkur bylgjunnar á þessu tímaþrepi. Level er á bilinu 0 til 1.
* **Animation type** - fellivalmyndin leyfir þér að velja hvernig þú vilt hreyfast í átt að þessu Level frá fyrra þrepi.
  * **None** - engin yfirfærsla, hoppar beint á þetta Level á tilteknum tíma.
  * **Linear** - alveg línuleg hreyfing frá fyrra Level yfir í þetta.
  * **Ease in / Ease out / Ease in/out** - mýkir hreyfinguna frá fyrra Level yfir í þetta. Sjá _ease function_ hér að ofan fyrir lýsingu á gerðum hreyfinga.

***
