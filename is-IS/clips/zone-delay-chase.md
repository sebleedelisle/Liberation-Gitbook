---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Við erum líklega öll sammála um að fleiri leysar þýði meiri skemmtun, en ef þeir gera allir nákvæmlega það sama ertu að missa af skapandi möguleikum.

Zone delay kerfið er einföld en áhrifarík leið til að skapa fjölbreytni milli zones og nýta uppsetningu með mörgum leysum betur. Það má líka nota til að búa til hefðbundnari chase-áhrif.

#### Hvernig þetta virkar

_Zone delay_ bætir seinkun við tímasetningu Clip fyrir hvert zone og skapar þannig eins konar sveip yfir zones.

Það er mjög áhrifaríkt að bæta zone delay við Clip sem er þegar í gangi og nota viðeigandi stjórnun á APC40 til að stilla styrk og mynstur. (Sjá [APC40 tilvísun](../reference/apc40-reference.md)). Einnig geturðu notað _Clip Settings_ panel.

Zone delay stillingar:

* **Zone delay** - stjórnar hversu mikil seinkun er sett á hvert zone, mælt í 1/64-nótum.
* **Pattern** - veldu röð zones
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Mynstrið byggir á númerum zones og gerir ráð fyrir að zones séu í röð frá vinstri til hægri. Zone delay meðhöndlar canvas zones og DMX zones sem aðskilda hópa þegar mynstrin eru reiknuð.
{% endhint %}

* **Delay mode**
  1. No delay - notaðu þetta í chase mode
  2. Delay - sjálfgefni hamurinn; seinkar tímasetningu fyrir hvert zone
  3. Delay with re-trigger - endurstillir Clip aftur á byrjun í hvert skipti sem farið er í gegnum mynstrið. Þetta hentar vel með _Chase mode_.
* **Chase mode** - þegar chase mode er virkt er kveikt og slökkt á hverju zone eins og í hefðbundnum chase-áhrifum. Stilltu útlitið á chase með stillingunum _Fade in, Hold,_ og _Fade out_. Þessar stillingar eru hlutfall af gildinu í Zone delay, þannig að gildið 1 samsvarar sama tíma og er tilgreindur í _Zone delay_. Þetta er svolítið erfitt að útskýra, þannig að besta ráðið er að prófa sjálf/ur.

{% hint style="info" %}
Zone delay er einnig beitt á öll virk effects. Til dæmis seinkar blikkandi effect líka milli zones, rétt eins og animation innan Clip.
{% endhint %}

Þegar Clip er með einhvers konar _Zone delay_ sérðu tákn með þremur punktum efst til hægri á Clip. Punktarnir hreyfast til að sýna hvaða gerð af _Zone delay_ er notuð fyrir viðkomandi Clip. Sjá [Hvað merkja litlu táknin á Clip-hnöppunum?](what-are-the-small-icons-on-the-clip-buttons.md) fyrir nánari upplýsingar.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Tákn með þremur punktum sem sýnir að Clip er með zone delay og hvaða hamur er notaður</p></figcaption></figure>

{% hint style="info" %}
Zone delay er stilling sem tilheyrir hverju Clip; hún er ekki global. Hún er hluti af skapandi hönnun Clip.
{% endhint %}
