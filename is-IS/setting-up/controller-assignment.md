---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Úthlutun stýringa

Þegar þú hefur sett upp laserana í Liberation geturðu úthlutað hverjum þeirra til laserstýringar í raunheimum. (Sjá [compatible-lasers-and-controllers-dacs.md](../hardware/compatible-lasers-and-controllers-dacs.md) til að athuga hvaða vélbúnað þú getur notað). Stýringarnar eru annaðhvort tengdar með USB eða yfir netið.

* Opnaðu _Controller Assignment_ spjaldið í gegnum valmyndina _View -> Controller Assignment_. (Þú getur líka notað hnappinn _ASSIGN LASER CONTROLLERS_ í _Laser Overview_ spjaldinu.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment-spjaldið"><figcaption></figcaption></figure>

* Spjaldið skiptist í tvennt: listi yfir lasera er vinstra megin og listi yfir tiltækar stýringar hægra megin. Ef þú sérð ekki laserstýringuna þína á listanum skaltu ýta á _REFRESH_ hnappinn. Ef vandamálið heldur áfram skaltu skoða [troubleshooting](../troubleshooting/).
* Til að úthluta stýringu til lasers skaltu smella og draga frá hægri yfir í laust lasersæti vinstra megin. Þetta segir Liberation hvaða stýringu á að nota fyrir hvaða laser. (Ef þú skiptir um skoðun geturðu dregið stýringarnar frjálst upp og niður frá einum laser yfir á annan.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Listi yfir stýringar" width="375"><figcaption></figcaption></figure>

* Ef þú sérð grænan ferning við hliðina á stýringunni þýðir það að Liberation hefur tengst henni með góðum árangri.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Ether Dream og Helios DAC úthlutað til lasers 2 og 3</p></figcaption></figure>

{% hint style="info" %}
Athugaðu að í hvert skipti sem þú tengist stýringu er laserinn sjálfkrafa gerður óvopnaður.
{% endhint %}

* Appelsínugulur ferningur 🟧 þýðir að stýringin á í tímabundnum tengingarvandræðum. Þetta stafar yfirleitt af netvandamáli; sjá [troubleshooting](../troubleshooting/).
* Rauður ferningur 🟥 þýðir að ekki næst samband við stýringuna; sjá [troubleshooting](../troubleshooting/).
* _disconnect button_ (X) aftengir stýringuna en hreinsar hana ekki úr úthlutun lasersins. Þú getur þá notað _reconnect button_ (refresh arrow icon) til að tengjast henni aftur, eða smellt aftur á _disconnect button_ til að hreinsa úthlutunina.
* _Ítarleg virkni:_ Opnaðu greiningarspjald stýringarinnar með því að smella á hnappinn sem lítur út eins og graf. Þetta er ítarleg virkni sem gefur þér nákvæmar upplýsingar um gagnastreymið og getur hjálpað við bilanagreiningu. (Þessi valkostur er mögulega ekki tiltækur fyrir sumar gerðir stýringa.)
* Þú getur notað _rename button_ (pencil) til að endurnefna þessa stýringu í hvað sem þú vilt. Það er skynsamlegt að gefa henni nafn sem auðvelt er að tengja við tiltekinn vélbúnað. Ef hún er innbyggð í laser gætirðu viljað nefna hana í samræmi við það, t.d. _LaserCube Ultra #1_ eða _Triton T5 #3._ Þessi nöfn vistast með Liberation uppsetningunni þinni og birtast héðan í frá; þetta getur hjálpað þér mikið við að bera kennsl á laserana þína fljótt.

{% hint style="info" %}
Pro tip - **tvísmelltu** á stýringu hægra megin til að úthluta henni sjálfkrafa á næsta lausa laser vinstra megin. Þetta getur sparað mikinn tíma ef þú þarft að úthluta mörgum laserum!
{% endhint %}

Þú getur notað hnappana _DISCONNECT ALL_ og _RECONNECT ALL_ til að endurstilla allar tengingar fljótt. Þetta er gagnlegt ef þú ert að glíma við netvandamál.
