---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Ohjaimen määritys

Kun olet määrittänyt laserit Liberationissa, voit liittää jokaisen niistä fyysiseen laserohjaimeen. (Katso kohdasta [Yhteensopivat laserit ja ohjaimet (DACit)](../hardware/compatible-lasers-and-controllers-dacs.md "mention"), mitä laitteistoa voit käyttää.) Ohjaimet yhdistetään joko USB:n kautta tai verkon yli.

* Avaa _Controller Assignment_ -paneeli valikosta _View -> Controller Assignment_. (Vaihtoehtoisesti voit käyttää _Laser Overview_ -paneelin _ASSIGN LASER CONTROLLERS_ -painiketta.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment -paneeli"><figcaption></figcaption></figure>

* Paneeli on jaettu kahteen osaan: vasemmalla on laserien luettelo ja oikealla käytettävissä olevien ohjaimien luettelo. Jos laserohjaimesi ei näy luettelossa, paina _REFRESH_ -painiketta. Jos ongelma jatkuu, katso [Vianmääritys](../troubleshooting/ "mention").
* Määritä ohjain laserille napsauttamalla ja vetämällä ohjain oikealta vasemmalla olevaan vapaaseen laserpaikkaan. Näin kerrot Liberationille, mitä ohjainta sen tulee käyttää kullekin laserille. (Jos muutat mielesi, voit vapaasti vetää ohjaimia ylös ja alas laserilta toiselle.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Ohjaimien luettelo" width="375"><figcaption></figcaption></figure>

* Jos ohjaimen vieressä näkyy vihreä neliö, Liberation on muodostanut siihen yhteyden onnistuneesti.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Ether Dream ja Helios DAC määritettyinä lasereille 2 ja 3</p></figcaption></figure>

{% hint style="info" %}
Huomaa, että aina kun muodostat yhteyden ohjaimeen, laser asetetaan automaattisesti disarmed-tilaan.
{% endhint %}

* Oranssi neliö 🟧 tarkoittaa, että ohjaimella on ajoittaisia yhteysongelmia. Tämä johtuu yleensä verkko-ongelmasta; katso [Vianmääritys](../troubleshooting/ "mention").
* Punainen neliö 🟥 tarkoittaa, ettei ohjaimeen saada yhteyttä; katso [Vianmääritys](../troubleshooting/ "mention").
* _disconnect button_ (X) katkaisee yhteyden ohjaimeen, mutta ei poista sitä laserin määrityksestä. Voit sen jälkeen käyttää _reconnect button_ -painiketta (päivitysnuolikuvake) yhdistääksesi sen uudelleen, tai napsauttaa _disconnect button_ -painiketta uudelleen poistaaksesi määrityksen.
* _Lisäominaisuus:_ Avaa ohjaimen analytiikkapaneeli napsauttamalla painiketta, joka näyttää kaaviolta. Tämä on lisäominaisuus, joka näyttää yksityiskohtaisia tietoja datavirrasta ja voi auttaa ongelmien vianmäärityksessä. (Tämä vaihtoehto ei välttämättä ole käytettävissä kaikilla ohjaintyypeillä.)
* Voit nimetä tämän ohjaimen haluamallasi tavalla _rename button_ -painikkeella (kynä). Ohjain kannattaa nimetä niin, että se on helppo yhdistää tiettyyn laitteistoon. Jos ohjain on sisäänrakennettu laseriin, voit nimetä sen sen mukaisesti, esimerkiksi _LaserCube Ultra #1_ tai _Triton T5 #3._ Nämä nimet tallennetaan Liberation-asennukseesi ja näkyvät jatkossa; ne voivat auttaa tunnistamaan laserisi nopeasti.

{% hint style="info" %}
Vinkki – **kaksoisnapsauta** oikealla olevaa ohjainta, niin se määritetään automaattisesti seuraavalle vapaalle laserille vasemmalla. Tämä voi säästää paljon aikaa, jos määritettäviä lasereita on paljon!
{% endhint %}

Voit nollata kaikki yhteydet nopeasti _DISCONNECT ALL_ ja _RECONNECT ALL_ -painikkeilla. Tämä on hyödyllistä, jos sinulla on verkko-ongelmia.
