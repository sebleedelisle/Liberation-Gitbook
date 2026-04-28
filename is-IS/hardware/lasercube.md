---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Kynningarmynd af LaserCube, birt með leyfi Wicked Lasers</p></figcaption></figure>

[LaserCube](https://www.laseros.com/lasercube/) frá Wicked Lasers er mjög fyrirferðarlítið, rafhlöðuknúið laser-tæki sem fæst í nokkrum mismunandi aflútfærslum. Þau eru vinsæl hjá áhugafólki vegna snjallsímaforritsins sem er auðvelt í notkun, en nýrri gerðirnar eru nógu öflugar til að nýtast í atvinnusýningum.

Símaforritið (sem heitir LaserOS og er einnig til fyrir borðtölvur) er ókeypis niðurhal, skemmtilegt að leika sér með og nægir flestum notendum. En ef þú ert að keyra stærri sýningar með mörgum laserum þarftu sérhæfðara og öflugra kerfi — og þar kemur Liberation til sögunnar.

### Tenging við LaserCube

Eldri LaserCube-tæki eru stýrð með USB, en núverandi gerðir eru allar með innbyggðan netstýringu. Þessi netstýrðu tæki eru kölluð „LaserCube Wifi“. Liberation styður báðar gerðir LaserCube\*, hvort sem tengt er með USB eða í gegnum net.

\*(Stuðningur við LaserCube netsamskiptastaðalinn var kynntur í útgáfu 0.7.3)

### USB LaserCube

Tengdu LaserCube við tölvuna með micro USB-snúru og leitaðu svo að tækinu í _Controller Assignment_ spjaldinu (sjá [controller-assignment.md](../setting-up/controller-assignment.md)). Ef það birtist ekki sjálfkrafa skaltu ýta á _REFRESH_ hnappinn.

### Network LaserCube "Wifi"

{% hint style="danger" %}
Þótt „Wifi“ tækin séu hönnuð til að keyra yfir þráðlaust net er ekki mælt með því og þú munt líklega fá rof og hnökra. Notaðu frekar RJ45 tengið til að tengja LaserCube við þráðbundið net, alveg eins og þú myndir gera með Ether Dreams.
{% endhint %}

Tengdu LaserCube við þráðbundna netið þitt.

Settu LaserCube í „LAN Client“ ham og gakktu úr skugga um að beinir sé á netinu. LaserCube fær IP-tölu frá beininum og ætti þá að birtast í _Controller Assignment_ spjaldinu. (Sjá [controller-assignment.md](../setting-up/controller-assignment.md)).

{% hint style="info" %}
Það er hægt að setja upp net án beinis og gefa öllum tækjunum föst IP-vistföng, og það er mjög algengt í viðburðageiranum. Sjálfur kýs ég að bæta beini við netið og mæli með þeirri leið fyrir alla sem hafa minni reynslu af netuppsetningu.

Beinirinn úthlutar IP-tölu sjálfkrafa á allt og mér finnst það einfaldara og síður líklegt til að valda villum.
{% endhint %}

{% hint style="danger" %}
Ólíkt Ether Dream _**SLÖKKVA LaserCube-tæki EKKI Á GEISLANUM (BLANK)**_ ef þau lenda í buffer under-run, týndum pakka eða öðrum skemmdum / röngum gögnum.

Í staðinn halda þau bara áfram þaðan sem þau voru stödd og í sumum tilfellum getur það valdið því að virkur geisli fer yfir svæði sem eru ekki innan skilgreindra svæða, og enn verra, fer í gegnum hugbúnaðargrímur.

Ég er í sambandi við hönnuði/forritara LaserCube og vona að þeir leysi þetta í framtíðinni með firmware-uppfærslu, en þangað til þarftu að tryggja að þú maskir líkamlega alla staði sem þú vilt ekki að laserinn nái til.

Til að gæta sanngirni ættirðu líklega hvort sem er að gera þetta, en ég nota sjálfur hugbúnaðargrímur til að verja myndavélar og skjávarpa. Hafðu því bara í huga að það er hættulegra að gera þetta með LaserCube netsamskiptastaðlinum en með Ether Dream (sem fer í öryggisstopp um leið og villa eða gögn sem vantar koma upp).

Einnig hef ég sagt þetta áður, en **notaðu þráðbundna tengingu við LaserCube**. Wifi dugar ekki og gerir þetta vandamál enn verra.
{% endhint %}
