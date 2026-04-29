---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Úthlutun laser controller

Þegar þú hefur sett leysana upp í Liberation geturðu úthlutað hverjum þeirra á laser controller í raunheimum. (Sjá [Samhæfir leysar og controllers (DACs)](../hardware/compatible-lasers-and-controllers-dacs.md) til að kanna hvaða vélbúnað þú getur notað.) Controllers eru annaðhvort tengdir með USB eða í gegnum net.

* Opnaðu _Controller Assignment_ panel í valmyndinni _View -> Controller Assignment_. (Þú getur líka notað hnappinn _ASSIGN LASER CONTROLLERS_ í _Laser Overview_ panel.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment panel"><figcaption></figcaption></figure>

* Panel skiptist í tvennt: listi yfir leysa er vinstra megin og listi yfir tiltæka controllers er hægra megin. Ef þú sérð ekki laser controller á listanum skaltu ýta á _REFRESH_. Ef vandamálið heldur áfram skaltu skoða [úrræðaleit](../troubleshooting/).
* Til að úthluta controller á leysi skaltu smella og draga frá hægri yfir í laust leysihólf vinstra megin. Þetta segir Liberation hvaða controller á að nota fyrir hvaða leysi. (Ef þú skiptir um skoðun geturðu dregið controllers frjálslega upp og niður frá einum leysi til annars.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Listi yfir controllers" width="375"><figcaption></figcaption></figure>

* Ef þú sérð grænan ferning við hliðina á controller þýðir það að Liberation hefur tengst honum með góðum árangri.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Ether Dream og Helios DAC sem hefur verið úthlutað á leysi 2 og 3</p></figcaption></figure>

{% hint style="info" %}
Athugaðu að í hvert skipti sem þú tengist controller verður laserinn sjálfkrafa disarmed.
{% endhint %}

* Appelsínugulur ferningur 🟧 þýðir að controller er að lenda í slitróttum tengivandamálum. Þetta stafar yfirleitt af netvandamáli; sjá [úrræðaleit](../troubleshooting/).
* Rauður ferningur 🟥 þýðir að ekki næst samband við controller; sjá [úrræðaleit](../troubleshooting/).
* _Hnappurinn til að aftengja_ (X) aftengir controller en hreinsar hann ekki úr úthlutun leysisins. Þú getur síðan notað _hnappinn til að endurtengja_ (refresh-örvatákn) til að tengja hann aftur, eða smellt aftur á _hnappinn til að aftengja_ til að hreinsa úthlutunina.
* _Ítarlegur eiginleiki:_ Opnaðu greiningarspjald controller með því að smella á hnappinn sem lítur út eins og graf. Þetta er ítarlegur eiginleiki sem sýnir nákvæmar upplýsingar um gagnastrauminn og getur hjálpað við úrræðaleit. (Þessi valkostur er hugsanlega ekki í boði fyrir sumar gerðir controllers.)
* Þú getur notað _hnappinn til að endurnefna_ (blýantur) til að gefa þessum controller hvaða nafn sem þú vilt. Best er að velja nafn sem auðveldar að tengja hann við tiltekinn vélbúnað. Ef hann er innbyggður í leysi getur verið gagnlegt að nefna hann í samræmi við það, t.d. _LaserCube Ultra #1_ eða _Triton T5 #3._ Þessi nöfn vistast með Liberation uppsetningunni þinni og birtast héðan í frá; það getur verið mjög gagnlegt þegar þú þarft að bera kennsl á leysana þína fljótt.

{% hint style="info" %}
Gott ráð – **tvísmelltu** á controller hægra megin til að úthluta honum sjálfkrafa á næsta lausa leysi vinstra megin. Þetta getur sparað mikinn tíma ef þú þarft að úthluta mörgum leysum!
{% endhint %}

Þú getur notað hnappana _DISCONNECT ALL_ og _RECONNECT ALL_ til að endurstilla allar tengingar fljótt. Þetta er gagnlegt ef þú ert að lenda í netvandamálum.
