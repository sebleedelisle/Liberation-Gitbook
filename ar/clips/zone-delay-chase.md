---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 تأخير zones / تأثير chase

نتفق جميعًا على أن زيادة عدد أجهزة الليزر تعني متعة أكبر، لكن إذا كانت كلها تفعل الشيء نفسه تمامًا، فستفوتك الكثير من الإمكانات الإبداعية.

نظام تأخير zones طريقة بسيطة وفعّالة لإضافة تنوّع بين zones، ويمكنه الاستفادة فعليًا من إعداد يحتوي على عدة أجهزة ليزر. ويمكن استخدامه أيضًا لإنشاء تأثير chase تقليدي أكثر.

#### كيف يعمل

يضيف _Zone delay_ تأخيرًا إلى توقيت Clip عبر كل zone، مما ينشئ نوعًا من الحركة المتتابعة عبر zones.

يكون تأثيره فعّالًا جدًا عند إضافة Zone delay إلى Clip قيد التشغيل بالفعل؛ استخدم عنصر التحكم المناسب على APC40 لضبط المستوى والنمط. (راجع [مرجع APC40](../reference/apc40-reference.md)). أو يمكنك استخدام لوحة _Clip Settings_.

إعدادات Zone delay:

* **Zone delay** - يتحكم في مقدار زمن التأخير المطبّق على كل zone، ويُقاس بوحدات النوتة من فئة 64.
* **Pattern** - اختر ترتيب zones
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
يعتمد النمط على أرقام zones ويفترض أن zones لديك مرتبة من اليسار إلى اليمين. يعامل Zone delay كلًا من canvas zones و DMX zones كمجموعات منفصلة عند حساب الأنماط.
{% endhint %}

* **Delay mode**
  1. No delay - استخدم هذا في وضع chase
  2. Delay - الوضع الافتراضي، يؤخر توقيت كل zone
  3. Delay with re-trigger - يعيد Clip إلى البداية في كل مرة عبر النمط. يكون هذا مفيدًا مع _Chase mode_.
* **Chase mode** - عند تشغيل chase mode، يتم تشغيل كل zone وإيقافها مثل تأثير chase التقليدي. اضبط مظهر chase باستخدام إعدادات _Fade in, Hold,_ و _Fade out_. تُضبط هذه الإعدادات كنسبة من قيمة Zone delay، لذا فإن القيمة 1 تعني الزمن نفسه المحدد في قيمة _Zone delay_. يصعب شرح ذلك قليلًا، لذا أنصحك بتجربته بنفسك.

{% hint style="info" %}
يُطبّق Zone delay أيضًا على أي مؤثرات نشطة. على سبيل المثال، سيتم تأخير تأثير الوميض عبر zones، بالإضافة إلى الحركة داخل Clip نفسه.
{% endhint %}

عندما يحتوي Clip على أي نوع من _Zone delay_، سترى أيقونة من ثلاث نقاط في أعلى يمين Clip. تتحرك هذه النقاط لتوضح لك نمط _Zone delay_ لذلك Clip. راجع [ما الأيقونات الصغيرة على أزرار Clip؟](what-are-the-small-icons-on-the-clip-buttons.md) لمزيد من التفاصيل.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>رمز النقاط الثلاث الذي يشير إلى أن Clip يحتوي على Zone delay ويوضح وضعه</p></figcaption></figure>

{% hint style="info" %}
Zone delay إعداد يخص كل Clip، وليس إعدادًا عامًا؛ فهو جزء من التصميم الإبداعي للـ Clip.
{% endhint %}
