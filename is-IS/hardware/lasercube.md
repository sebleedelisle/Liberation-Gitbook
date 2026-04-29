---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Kynningarmynd fyrir LaserCube, með leyfi Wicked Lasers</p></figcaption></figure>

[LaserCube](https://www.laseros.com/lasercube/) frá Wicked Lasers er mjög fyrirferðarlítið, rafhlöðuknúið lasertæki sem fæst í nokkrum aflútfærslum. Það er vinsælt meðal áhugafólks vegna snjallsímaappsins sem er auðvelt í notkun, en nýlegar gerðir eru nógu öflugar til að nota í atvinnusýningum.

Símaappið, sem heitir LaserOS og er einnig til fyrir borðtölvur, er ókeypis og skemmtilegt að prófa, og dugar vel fyrir flesta notendur. En ef þú ert að keyra stærri sýningar með mörgum leysum þarftu sérhæfðara og öflugra verkfæri — og þar kemur Liberation til sögunnar.

### Að tengjast LaserCube

Eldri LaserCube-tæki eru stýrð með USB, en núverandi gerðir eru allar með innbyggðan network controller. Þessi nettengdu tæki eru kölluð „LaserCube Wifi“. Liberation styður báðar gerðir LaserCube\*, hvort sem tengt er með USB eða yfir netkerfi.

\*(Stuðningur við LaserCube network protocol var kynntur í útgáfu 0.7.3)

### USB LaserCube

Tengdu LaserCube við tölvuna með micro USB-snúru og leitaðu síðan að því í _Controller Assignment_ spjaldinu (sjá [Úthlutun laser controller](../setting-up/controller-assignment.md)). Ef það birtist ekki sjálfkrafa skaltu ýta á _REFRESH_ hnappinn.

### Network LaserCube „Wifi“

{% hint style="danger" %}
Þótt „Wifi“ tækin séu hönnuð til notkunar yfir þráðlaust net er ekki mælt með því, þar sem þú munt líklega fá rof og hnökra. Notaðu frekar RJ45-tengið til að tengja LaserCube við vírað net, alveg eins og þú myndir gera með Ether Dream.
{% endhint %}

Tengdu LaserCube við víraða netkerfið þitt.

Settu LaserCube í „LAN Client“ ham og gakktu úr skugga um að router sé á netkerfinu. LaserCube fær þá IP-tölu frá routernum og ætti síðan að birtast í _Controller Assignment_ spjaldinu. (Sjá [Úthlutun laser controller](../setting-up/controller-assignment.md)).

{% hint style="info" %}
Það er hægt að setja upp netkerfi án routers og gefa öllum tækjum fastar IP-tölur, og það er mjög algengt í viðburðageiranum. Persónulega kýs ég að bæta router við netkerfið og mæli með þeirri leið fyrir alla sem hafa minni reynslu af netkerfum.

Routerinn úthlutar IP-tölum sjálfkrafa á allt sem tengist, og mér finnst það einfaldara og síður líklegt til að valda villum.
{% endhint %}

{% hint style="danger" %}
Ólíkt Ether Dream þá _**SLÖKKVA LaserCube EKKI Á LASERGEISLANUM**_ ef þau lenda í buffer under-run, glötuðum pakka eða öðrum skemmdum/röngum gögnum.

Í staðinn halda þau bara áfram frá þeim stað þar sem þau voru, og í sumum tilvikum getur það valdið því að virkur geisli fari yfir svæði sem eru ekki innan zones, og það sem verra er, hann getur farið í gegnum software masks.

Ég er í samtali við hönnuði/forritara LaserCube og vona að þeir lagi þetta í framtíðinni með firmware-uppfærslu. Þangað til verður þú að tryggja að þú setjir líkamlegar afmarkanir þar sem þú vilt ekki að laser fari.

Til að vera sanngjörn ættirðu líklega alltaf að gera þetta, en ég nota sjálfur software masks til að verja myndavélar og skjávarpa. Hafðu því í huga að þetta er hættulegra þegar LaserCube network protocol er notað en með Ether Dream, sem fer í öryggisstöðvun um leið og villa kemur upp eða gögn vantar.

Og ég er búinn að segja þetta áður, en **notaðu víraða tengingu við LaserCube**. Wifi dugar ekki og gerir þetta vandamál enn verra.
{% endhint %}
