---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / synkronointi

Musiikin synkronointi on Liberationin keskeinen osa. Kun tempo ja iskut on sovitettu musiikkiin, voit luottaa siihen, että kaikki pysyy synkassa. Jos saat käyttöösi MIDI clockin tai Ableton Linkin, manuaalisesta synkronoinnista ei tarvitse huolehtia lainkaan. Jos et, ei hätää – voit sovittaa tempon käsin _Live_-tempotoiminnolla.

Jos sinulla on kokemusta musiikki- tai valo-ohjelmistoista, tämä prosessi on todennäköisesti tuttu. Jos ei, järjestelmään kannattaa tutustua rauhassa ja harjoitella kotona ennen live-keikkaa.

## Tempo-paneeli

_Tempo_-paneeli on aina näkyvissä ja sisältää kaikki synkronointiasetukset. Yläosassa näkyy nykyinen tahti-/iskulaskuri sekä transport-ohjaimet, joissa on play/pause- ja rewind/fast-forward-painikkeet.

Sen alapuolella näkyy iskumerkki: neljä neliötä, jotka “sykkivät” iskun mukana. Tämä _beat marker_ on erittäin hyödyllinen visuaalinen apu, ja siihen tulee viitattua jatkuvasti _Live_-tempotoimintoa käytettäessä.

### Tempon asettaminen

Voit asettaa tempon usealla tavalla:

* Napsauta ja vedä _Tempo_-liukusäädintä
* Shift-napsauta ja vedä _Tempo_-liukusäädintä muuttaaksesi tempoa 0,1:n askelin
* Kaksoisnapsauta _Tempo_-liukusäädintä ja kirjoita arvo käsin
* Käytä APC40:n _Tempo_-nuppia (paina Shift, jos haluat 0,1:n askelia)
* Käytä Tap Tempoa

{% hint style="info" %}
Tempo määritetään iskuina minuutissa, ja perinteinen oletusarvo on yleensä 120.
{% endhint %}

## Tap Tempo

Aseta tempo automaattisesti napsauttamalla _TAP_-painiketta iskun tahdissa. Aseta tahdin alku _RESET_-painikkeella.

{% hint style="info" %}
Tap Tempo -järjestelmä tunnistaa, jos pidät hetken taukoa naputtamisesta tai jos muutama isku jää välistä. Jos alat naputtaa kaksinkertaisessa tempossa, se ymmärtää, että haluat kaksinkertaistaa tempon. Sama pätee, jos naputat puolitempossa.

Se osaa myös päätellä, jos kaksi henkilöä naputtaa tempoa samaan aikaan (esimerkiksi toinen näppäimistöllä ja toinen APC40:llä). Liberation laskee kaksoisnaputuksista keskiarvon.
{% endhint %}

#### Näppäinkomennot:

T - tap tempo\
R - reset the bar\
Y - round the tempo to the nearest beat per minute.

{% hint style="info" %}
Koska suurin osa nykyisestä musiikista tehdään digitaalisesti, tempo on yleensä pyöristetty kokonaisluku. Jos naputettu tempo vaikuttaa olevan lähellä oikeaa, käytä Y-näppäintä (tai siirrä APC40:n tempo-nuppia yhden “pykälän”) pyöristääksesi sen kokonaislukuun.
{% endhint %}

#### APC40-ohjaimet:

APC40:ssä on erillinen _TAP TEMPO_ -painike. Voit myös käyttää liitettyä jalkakytkintä ja naputtaa tempon jalalla.

Säädä tempoa _TEMPO_-nupilla. Paina _SHIFT_-painiketta käyttäessäsi _TEMPO_-nuppia, jos haluat tehdä hienosäätöä.

Käytä _METRONOME_-painiketta **tahdin nollaamiseen**. (Huomaa, että _METRONOME_-painike myös vilkkuu iskun tahdissa.)

Käännä _TEMPO_-nuppia yhden “pykälän” oikealle tai vasemmalle, jos haluat **pyöristää tempon** ylös- tai alaspäin kokonaiseksi BPM-arvoksi.

Katso myös [APC40-viite](reference/apc40-reference.md "mention")

### Tempon nudge-säätö

Jos olet varma, että tempo on riittävän lähellä oikeaa, mutta huomaat sen alkavan ajelehtia pois tahdista, korjaa ajoitusta _NUDGE_-painikkeilla.

Jos Liberationin tempo alkaa edistää musiikkiin nähden, pidä _NUDGE -_ -painiketta painettuna hidastaaksesi tilapäisesti, kunnes tempo kohdistuu uudelleen.

Jos Liberationin tempo jää jälkeen musiikista, pidä _NUDGE +_ -painiketta painettuna nopeuttaaksesi tilapäisesti, kunnes tempo kohdistuu uudelleen.

{% hint style="info" %}
Voit käyttää joko näytöllä näkyviä NUDGE-painikkeita tai APC40:n erillisiä painikkeita.
{% endhint %}

### Half time / double time

Käytä _÷2_- ja _x2_-painikkeita tempon puolittamiseen tai kaksinkertaistamiseen pysyvästi. Toisin kuin tempo multiplier, tämä muuttaa nykyistä tempoa pysyvästi.

## Tempo Multiplier

_Tempo Multiplier_ -järjestelmällä voit säätää tempoa tilapäisesti ja palata sen jälkeen aiempaan tempoon.

Kytke _Tempo Multiplier_ päälle tai pois painamalla _TEMPO MULTIPLIER_ -painiketta tai APC40:n _BANK_-painiketta. Säädä sitä näytön liukusäätimellä tai APC40:n A-B-liukusäätimellä. Voit myös käyttää _25%, 50%, 100% 200%_ -esiasetuspainikkeita.

## Ulkoiset tempolähteet

### MIDI Clock

Jos haluat synkronoida ulkoiseen MIDI clock -signaaliin, valitse _MIDI CLOCK_ -valintapainike ja valitse MIDI-laite pudotusvalikosta. Huomioi pudotusvalikoiden vieressä oleva värillinen tilavalo:

* Vihreä - MIDI clock -signaalia vastaanotetaan
* Oranssi - MIDI-laitteeseen voidaan muodostaa yhteys, mutta clock-signaalia ei tällä hetkellä ole
* Punainen - MIDI-laitteeseen ei voida muodostaa yhteyttä

{% hint style="info" %}
MIDI Clock lähettää sarjan frameja (24 neljäsosanuottia kohti), mutta viestit eivät sisällä sijaintitietoa. Tämä tarkoittaa, että se auttaa pysymään tempossa, mutta tahti voi silti olla tarpeen nollata.

Liberationin MIDI Clock -tempolähde reagoi myös **MIDI Machine Control (MMC)** -viesteihin, joten jos clock-lähteesi lähettää niitä, tahtia ei tarvitse nollata käsin.
{% endhint %}



### Ableton Link

Jos haluat synkronoida Ableton Linkin kanssa, valitse tempolähteeksi _ABLETON LINK_. Liberation liittyy paikallisverkkosi Link-istuntoon ja seuraa muiden Link-yhteensopivien sovellusten yhteistä tempoa ja iskukohtaa.

Ableton Link ei käytä MIDI-porttia eikä välitä absoluuttista kappalepositiota. Käytä tahdin nollausohjaimia, jos Liberationin tahdin alun pitää osua tiettyyn hetkeen esityksessä.

### Timeline

Jokaisella timelinella on oma tempo, joka voi olla kiinteä arvo tai _Tempo Map_. _Tempo Map_ mahdollistaa tempon säätämisen tietyissä kohdissa timelinen sisällä.

Timelinen tempoa käytetään, kun tempolähteeksi on valittu _TIMELINE_.

{% hint style="info" %}
Voit ajaa timelinea minkä tahansa tempolähteen kanssa. Jos sinulla on livebändi, joka ei soita klikkiin, voit käynnistää timelinen käsin ja pitää sen synkassa _LIVE_-tempolähteellä. Tai jos käytössäsi on MIDI clock -signaali, voit käyttää sitä.
{% endhint %}
