---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Við erum öll sammála um að fleiri leysar þýði meiri skemmtun, en ef þeir gera allir nákvæmlega það sama ertu að missa af skapandi möguleikum.

Zone delay-kerfið er einföld en áhrifarík leið til að skapa fjölbreytni milli svæða og nýtir fjölleysisuppsetningu mjög vel. Það má líka nota til að búa til hefðbundnari chase-áhrif.

#### Hvernig þetta virkar

_Zone delay_ bætir töf við tímasetningu Clip fyrir hvert svæði og býr þannig til eins konar sveip yfir svæðin.

Það er mjög áhrifaríkt að bæta Zone delay við Clip sem er þegar í gangi og nota viðeigandi stýringu á APC40 til að stilla styrk og mynstur. (Sjá [apc40-reference.md](../reference/apc40-reference.md)). Þú getur líka notað _Clip Settings_ panel.

Zone delay-stillingar:

* **Zone delay** - stýrir lengd tafarinnar sem er beitt á hvert svæði, mælt í 1/64 nótum.
* **Pattern** - veldu röð svæðanna
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Mynstrið byggir á svæðisnúmerunum og gerir ráð fyrir að svæðin séu í röð frá vinstri til hægri. Zone delay meðhöndlar Canvas-svæði og DMX-svæði sem aðskilda hópa þegar mynstrin eru reiknuð.
{% endhint %}

* **Delay mode**
  1. No delay - notaðu þetta í chase mode
  2. Delay - sjálfgefni hamurinn, seinkar tímasetningu hvers svæðis
  3. Delay with re-trigger - Endurstillir Clip aftur á byrjun í hvert skipti yfir mynstrið. Þetta hentar vel með _Chase mode_.
* **Chase mode** - þegar chase mode er kveikt er kveikt og slökkt á hverju svæði eins og í hefðbundnum chase-áhrifum. Stilltu útlit chase með _Fade in, Hold,_ og _Fade out_ stillingunum. Þessar stillingar eru hlutfall af Zone delay-gildinu, þannig að gildið 1 samsvarar sama tíma og tilgreindur er í _Zone delay_. Þetta er svolítið erfitt að útskýra, svo mitt ráð er að prófa þetta sjálf/ur.

{% hint style="info" %}
Zone delay er líka beitt á öll virk effects. Til dæmis seinkar blikkandi effect yfir svæðin, rétt eins og hreyfimyndin inni í sjálfu Clip.
{% endhint %}

Þegar Clip er með einhvers konar _Zone delay_ sérðu tákn með þremur punktum efst til hægri á Clip. Punktarnir eru hreyfðir til að sýna þér gerð _Zone delay_ fyrir viðkomandi Clip. Sjá [what-are-the-small-icons-on-the-clip-buttons.md](what-are-the-small-icons-on-the-clip-buttons.md) fyrir nánari upplýsingar.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Tákn með þremur punktum sem gefur til kynna að Clip sé með Zone delay og sýnir haminn</p></figcaption></figure>

{% hint style="info" %}
Zone delay er stilling sem tilheyrir hverju Clip; hún er ekki global, heldur hluti af skapandi hönnun Clip.
{% endhint %}
