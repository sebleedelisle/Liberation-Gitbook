---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip settings

### Clip settings -paneeli

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip settings -paneeli</p></figcaption></figure>

Muuta clipin ulostulon kokoa asetuksilla _Scale X_ ja _Scale Y_. Ne on lukittu yhteen, ellet paina _SHIFT_-näppäintä.

Muuta clipin vaaka- ja pystysijaintia asetuksilla _Shift X_ ja _Shift Y_.

_Zone Delay/Chase_ on niin hauska ominaisuus, että sille on oma osionsa. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Parameters-paneeli

Clip Deckin oikealla puolella oleva paneeli näyttää kahdeksan kontekstikohtaista parametria. Kun Clip on valittuna, ensimmäiset säätimet ovat valitun Clipin _Shift X_, _Shift Y_ ja _Zone Delay_, ja niiden jälkeen tulevat yleiset _Spin_- ja _Scale_-säätimet.

Samat parametrit peilataan tuetuille MIDI-ohjaimille. Jos Clip ei ole valittuna, Clip-kohtaiset paikat ovat tyhjiä. Jos pidät ryhmäpainiketta painettuna, kaksi ensimmäistä säädintä vaihtuvat kyseisen ryhmän sisään- ja ulosfeidauksen ajoiksi.

### Clipien lukitseminen

Jos clip on lukittu, sitä ei voi siirtää tai poistaa. Lukitse clip oikean painikkeen valikon _Locked_-valintaruudulla. Clip settings -paneelissa saat käyttöön muutamia lisäasetuksia.

* _UNLOCK ALL -_ avaa kaikkien Clip Deckin clipien lukituksen.
* _AUTO-LOCK_ - kun _Auto-Lock_ on käytössä, kaikki automaattisesti toistetut clipit (joko aikajanalla tai MIDI-tallennus-/toistojärjestelmällä) lukitaan. Tästä on hyötyä, jos olet ohjelmoinut shown Logic Prossa (tai vastaavassa) etkä halua muokata shown käyttämiä clipejä vahingossa.
* _LOCKED CLIPS ZONES_ - jos tämä on käytössä, lukittujen clipien zoneja ei voi muuttaa.
* _LOCKED CLIPS PARAMS_ - jos tämä on käytössä, lukittujen clipien parametreja (scale, shift jne.) ei voi muuttaa.

### Oikean painikkeen valikko

Kun napsautat Clipiä oikealla painikkeella, näkyviin tulee valikko, jossa on kyseisen Clipin asetuksia. Katso lisätietoja valikon ensimmäisistä kohdista: [Johdanto Clip Editoriin](../clip-editor/clip-editor-intro.md "mention"), [Clip settings](clip-settings.md "mention") ja [Clip-ryhmät](groups.md "mention").

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Clipit on oletusarvoisesti asetettu tilaan _retrigger_. Tämä tarkoittaa, että riippumatta siitä, milloin painat clipiä, se alkaa toistua siitä hetkestä. Jos käynnistät sen myöhässä, clipin animaatio on hieman myöhässä eikä osu aikaan.

{% hint style="info" %}
Jos käytät _Tap Tempo_ -toimintoa retrigger-tilassa olevan clipin toistuessa, järjestelmä "kvantisoi" clipin aikaan, vaikka et käynnistänyt sitä täsmälleen iskulle.
{% endhint %}

Jos _Retrigger_ ei ole käytössä, clip on aina ajassa — aivan kuin se olisi käynnistetty kellon alusta. Tämä sopii tilanteisiin, joissa olet synkronoitu täydellisesti musiikkiin ulkoisen kellosignaalin kautta.

{% hint style="info" %}
Clipit on usein suunniteltu looppamaan loputtomasti, mutta voit suunnitella ne myös niin, että ne toistuvat vain kerran tai muutaman kierroksen. Varmista, että tällaisissa clipeissä _retrigger_ on käytössä, muuten ne eivät käynnisty uudelleen!
{% endhint %}

### Sisään-/ulos-siirtymän aika (fade)

Clipille voidaan määrittää sisään- ja ulosfeidaus, jonka kesto mitataan sekunteina. Oletusarvoisesti fade-aika periytyy ryhmän asetuksista (ja sitä voi muuttaa napsauttamalla ryhmäpainiketta oikealla painikkeella).

Jos haluat clipille eri fade-keston kuin sen ryhmällä, poista ensin _USE GROUP DEFAULT_ -painike käytöstä ja säädä sitten clipin _In time_- ja _Out time_ -liukusäätimiä.
