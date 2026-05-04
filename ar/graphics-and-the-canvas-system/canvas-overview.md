---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 نظرة عامة على Canvas

نظام Canvas في Liberation بسيط نسبيًا، لكنه قد يكون مربكًا في البداية. إليك نظرة مفاهيمية عامة لتبدأ.

{% hint style="info" %}
**مهلًا، هل أحتاج إلى نظام Canvas؟**

ربما لا! إذا كنت تعرض رسمًا واحدًا فقط على ليزر واحد، فيمكنك فعل ذلك بسهولة باستخدام beam zone (مع أن محتوى beam zone يُقلب أفقيًا افتراضيًا، لذلك ستحتاج إلى تطبيق X flip على Clip).

لكن إذا أردت توزيع محتوى رسومي على أكثر من ليزر، أو تقسيمه إلى أقسام مختلفة لمواءمته مع عناصر معمارية، فإن نظام Canvas يوفّر لك ما تحتاجه!
{% endhint %}

### Canvas

أولًا، هناك Canvas نفسه. هذا ما تراه في عرض _CANVAS_، ويمثّل مساحة كبيرة — Canvas بالمعنى الحرفي تقريبًا — يمكنك رسم المحتوى في أي مكان داخلها.

### مناطق هدف Canvas

تظهر هذه المناطق كمستطيلات زرقاء الحدود في Canvas view، وهي مناطق يمكنك إرسال المحتوى إليها. ترسل محتوى Clip إلى منطقة هدف Canvas بالطريقة نفسها التي ترسل بها Clip إلى beam zone. سترى أزرار مناطق هدف Canvas إلى يمين أزرار beam zone في Clip Deck.

{% hint style="info" %}
إذا لم تتمكن من رؤية أزرار Canvas في Clip Deck، فجرّب تمرير أزرار beam zone باستخدام `Shift + Left / Right Arrow`. ينبغي أن ترى زرًا لكل منطقة هدف Canvas مع تسمية مثل _CANVAS 1, CANVAS 2_ وما إلى ذلك.
{% endhint %}

### Canvas zones

Canvas zones هي مناطق داخل Canvas تختار إرسالها إلى ليزر. تُعرض كمستطيلات وردية الحدود في Canvas view. يمكنك النقر بزر الماوس الأيمن على كل zone واختيار أجهزة الليزر التي تريد إسنادها إليها. إذا انتقلت الآن إلى عرض _OUTPUT_ لذلك الليزر، فسترى ظهور zone جديدة.

{% hint style="danger" %}
تحذير - إذا كانت حالة الليزر هي armed، فقد يبدأ فجأة في عرض محتوى ضمن Canvas zone افتراضية. من الأفضل تغيير حالة الليزر إلى disarmed قبل إسناد Canvas zones إليه.
{% endhint %}

{% hint style="info" %}
يمكنك أيضًا إسناد Canvas zone إلى ليزر بالنقر على زر _add canvas zone_ في عرض _OUTPUT_. راجع [zones](../output-view/zones.md "mention").
{% endhint %}

### صور الإرشاد

يمكنك إضافة صورة إرشادية إلى Canvas واستخدامها كقالب لرسوماتك. يُنصح بتعديل تلوين الصورة الإرشادية (من قائمة النقر بزر الماوس الأيمن) وتعتيمها لتتمكن من رؤية محتواك فوقها بسهولة أكبر.

{% hint style="info" %}
بالنسبة للمواءمة المعمارية، وجدت أنه من المفيد إنشاء تصور «مفكوك» للمبنى يمثّل جميع أسطحه كصورة مسطحة غير مشوهة. يمكن تنفيذ تصحيح المنظور للأقسام المختلفة باستخدام Canvas zone في عرض _OUTPUT_.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>صورة إرشادية «مفلطحة» لـ Saltwell Hall في Gateshead بالمملكة المتحدة</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Canvas zones في نسخة مبكرة جدًا من Liberation (حوالي 2017!) لاحظ أن المستطيلات الوردية تختار الجزء الذي سيُعرض من Canvas، ثم توضّح عروض الإخراج أدناه الجزء الذي ستذهب إليه تلك zones في كل ليزر.</p></figcaption></figure>

### Canvas في عارض 3D

من المحتمل أن تكون إعادة إنشاء نظام عرض معقد متعدد الليزر داخل عارض 3D أمرًا شاقًا للغاية، على أقل تقدير! لذلك، بدلًا من ذلك، لديك خيار وضع Canvas داخل مساحة 3D. فعّل مربع الاختيار _Show canvas_ في لوحة _3D visualiser settings_. (ستظهر أيضًا أي صور إرشادية لديك في Canvas داخل العارض.)

{% hint style="info" %}
لاحظ أن العارض سيظل يعرض إسقاطات Canvas كمؤثرات جوية صادرة من أجهزة الليزر. يمكنك ببساطة نقلها خارج المشهد، أو إذا أردت ضبطًا أدق، يمكنك محاذاتها مع Canvas!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>قد يكون الأمر مُرضيًا جدًا عندما تُحاذي الأشعة الصادرة من الليزر مع صورة Canvas داخل عارض 3D!</p></figcaption></figure>
