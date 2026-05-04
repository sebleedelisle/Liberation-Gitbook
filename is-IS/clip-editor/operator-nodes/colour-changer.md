---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Litabreyting

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Litabreyting

Breytir litum alls efnis sem kemur inn. Þú getur annaðhvort stillt föst HSB-gildi eða skipt yfir í gradient-kerfið og tekið liti úr sérsniðnum gradient.

* **hue, saturation, brightness** - litagildin, sjá [Litastillingar og HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - litblænum er ekki breytt
  * FIXED - litblær eininga er stilltur á gildið sem er valið fyrir hue
  * SHIFT - litblær eininga færist um gildið, þannig að einingar í mismunandi litum halda áfram að vera mismunandi, en færast bara eftir hue-gildinu.
* **saturation mode** -
  * OFF - mettun er ekki breytt
  * FIXED - mettun er föst á tilgreinda gildinu.
* **brightness mode** -
  * OFF - birtustigi er ekki breytt
  * FIXED - birtustig eininga er stillt á gildið sem er valið fyrir brightness
  * MULTIPLY - birtustig eininga er sameinað gildinu fyrir brightness, þannig að ef þær blikka halda þær áfram að blikka, en aðeins upp að birtustiginu sem er tilgreint hér.
* **gradient mode** - skiptir úr föstu HSB-rennunum yfir í gradient-ritilinn. Þetta node tekur einn lit úr gradient og beitir honum síðan með hue-, saturation- og brightness-hömunum hér fyrir ofan.
* **gradient position** - velur hvaða punktur í gradient er notaður. Hreyfðu þetta frá 0% til 100% með Sawtooth Oscillator til að fara í gegnum gradient með tímanum.
* **blend** - hversu sterkt litabreytingin er notuð; 0% þýðir ekkert, 100% er full virkni og 50% er blanda af núverandi lit og nýju gildunum.

{% hint style="info" %}
Colour Change node tekur einn lit úr gradient fyrir allt inntakið. Ef þú vilt að gradient liggi yfir formið eftir staðsetningu skaltu nota [breytingar eftir staðsetningu](position-based-changers.md "mention") í staðinn.
{% endhint %}

### Gradient-ritill

Þegar **gradient mode** er virkt birtist gradient-ritillinn fyrir neðan aðalstýringarnar.

* Smelltu á gradient-stikuna til að bæta við litastoppi.
* Vinstrismelltu á stopp til að velja það og dragðu það síðan til hliðar til að færa það.
* Dragðu valið stopp niður frá stikunni, eða ýttu á Delete/Backspace, til að fjarlægja það. Gradient heldur alltaf að minnsta kosti tveimur stoppum.
* Hægrismelltu á stopp til að breyta því með litavalinu.
* Notaðu **Position**, **Hue**, **Saturation** og **Brightness** til að breyta völdu stoppi nákvæmlega.
* **interpolation** velur hvernig litum er blandað á milli stoppa:
* **HSB** - blandar hue, saturation og brightness. Þetta hentar best fyrir mjúka regnbogahreyfingu um litahringinn.
* **RGB** - blandar rauðum, grænum og bláum gildum beint. Þetta minnir oft meira á litaflökt á skjá eða ljósaborði.
* **NONE** - hoppar frá einu stoppi yfir í það næsta án blöndunar.
* **hue direction** er í boði við HSB interpolation:
* **AUTO** - fer stystu leið um hue-hringinn.
* **FORWARDS** - fer alltaf áfram í gegnum hue-gildi.
* **BACKWARDS** - fer alltaf aftur á bak í gegnum hue-gildi.
