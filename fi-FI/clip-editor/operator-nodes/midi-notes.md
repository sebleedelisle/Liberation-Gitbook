---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Luo “laserharppu”-tyylisiä efektejä, joissa saapuvat MIDI-nuotit laukaisevat säteitä tai muotoja määritetyllä alueella. Node käyttää kullekin nuotille _lähteenä_ sitä sisältöä, jonka syötät siihen: syötä piste, niin saat rivin pisteitä. Syötä muoto, kuten ympyrä, niin saat rivin ympyröitä. Myös monimutkaisemmat muodot kopioidaan samalla tavalla.

Voit valita, mitä MIDI-liitäntää Liberation kuuntelee kohdassa **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – mitä MIDI-kanavaa kuunnellaan (0 = kaikki kanavat, 1–16 = tietty kanava)
* **width** – kokonaisleveys, jolle nuotit levittyvät.
* **MIDI note min / max** – alueen alin ja ylin MIDI-nuottiarvo.
* **ignore out of range notes** – suodattaa pois nuotit, jotka ovat asetetun alueen ulkopuolella. Jos tämä ei ole käytössä, alueen ulkopuoliset nuotit “rajoitetaan” lähimpään käytettävissä olevaan nuottiin (korkeat nuotit laukaisevat alueen yläreunan, matalat nuotit alareunan).
* **auto extend range** – laajentaa aluetta automaattisesti, jos soitetaan sen ulkopuolisia nuotteja.

{% hint style="info" %}
Etkö ole varma, mitä nuottialuetta saat? Ota **auto extend range** käyttöön, aseta **MIDI note min** hyvin korkeaksi ja **MIDI note max** hyvin matalaksi, ja soita sitten nuottisi läpi. Järjestelmä tunnistaa ne kaikki ja laajentaa alueen puolestasi. Kun kaikki on mukana, poista **auto extend range** käytöstä lukitaksesi alueen.
{% endhint %}

* **leave all notes visible** – luo säteet tai muodot kaikille alueen nuoteille riippumatta siitä, soivatko ne, jolloin syntyy “laserharppu”-efekti.
* **hit colour** – väri, joka näkyy, kun nuotti laukaistaan.
* **hit colour hold time** – kuinka kauan hit colour pysyy täydellä kirkkaudella ennen häipymistä. Arvo annetaan sekunteina (0–1). _100 % = 1 sekunti._
* **hit colour decay time** – kuinka kauan hit colour -värin häipyminen takaisin kestää pitoajan jälkeen. Arvo annetaan sekunteina (0–1). _100 % = 1 sekunti._

{% hint style="info" %}
Jos sisältösi on jo puhtaan valkoista, hit colour -värin asettaminen valkoiseksi ei muuta mitään. Parhaan tuloksen saat käyttämällä sisällössä kylläistä väriä ja asettamalla hit colour -väriksi valkoisen – näin saat erittäin toimivan välähdysefektin, kun nuotit laukaistaan.
{% endhint %}

* **note off fade out time** – kuinka kauan nuotin häipyminen kestää, kun se vapautetaan. Arvo annetaan sekunteina (0–1). _100 % = 1 sekunti._
* **hit scale factor** – kuinka paljon nuotti suurenee, kun se laukaistaan (esim. 2 = kaksinkertainen koko).
* **hit scale hold time** – kuinka kauan nuotti pysyy suurennettuna ennen kuin se pienenee takaisin. Arvo annetaan sekunteina (0–1). _100 % = 1 sekunti._
* **hit scale decay time** – kuinka kauan nuotin palaaminen alkuperäiseen kokoonsa kestää. Arvo annetaan sekunteina (0–1). _100 % = 1 sekunti._
* **note off shrink time** – kuinka kauan alkuperäiseen kokoon kutistuminen kestää sen jälkeen, kun nuotti on vapautettu. Arvo annetaan sekunteina (0–1). _100 % = 1 sekunti._ (Ei vaikuta, kun **leave all notes visible** on käytössä.)

{% hint style="info" %}
Skaalaus – Huomaa, että jos sisältösi on yksittäinen piste, skaalaus ei vaikuta siihen!
{% endhint %}
