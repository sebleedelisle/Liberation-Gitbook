---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 nodes الخاصة بـ Creator

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

ينشئ نقطة / شعاعًا واحدًا.

* **Render profile** - راجع [ملف تعريف العرض](fundamentals/render-profile.md)
* **Colour** - لون النقطة. راجع [إعدادات اللون و HSB](fundamentals/colour-settings-and-hsb.md)
* موضع **x** و **y** - راجع [نظام الإحداثيات](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

ينشئ خطًا / سطحًا.

* **Render profile** - راجع [ملف تعريف العرض](fundamentals/render-profile.md)
* **Size** - طول الخط
* **Colour** - لون الخط. راجع [إعدادات اللون و HSB](fundamentals/colour-settings-and-hsb.md)
* موضع **x** و **y** - راجع [نظام الإحداثيات](fundamentals/co-ordinate-system.md)
* **rotation** - زاوية الخط بالدرجات
* **resolution** - راجع [الدقة](fundamentals/resolution.md)
* **alignment** - _LEFT / CENTRE / RIGHT -_ يحدد نقطة بداية الخط ومركز دورانه
* _MOVE TO FRONT / MOVE TO BACK_ - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

ينشئ دائرة / مخروطًا.

* **Render profile** - راجع [ملف تعريف العرض](fundamentals/render-profile.md)
* **radius** - نصف قطر الدائرة
* **Colour** - لون الدائرة. راجع [إعدادات اللون و HSB](fundamentals/colour-settings-and-hsb.md)
* موضع **x** و **y** - راجع [نظام الإحداثيات](fundamentals/co-ordinate-system.md)
* **resolution** - راجع [الدقة](fundamentals/resolution.md)
* **Fill state** - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

ينشئ مضلعًا متساوي الأضلاع، مثلثًا أو مربعًا أو خماسيًا وغير ذلك.

* **Render profile** - راجع [ملف تعريف العرض](fundamentals/render-profile.md)
* **size** - المسافة من المركز إلى كل زاوية
* **Colour** - لون المضلع. راجع [إعدادات اللون و HSB](fundamentals/colour-settings-and-hsb.md)
* موضع **x** و **y** - راجع [نظام الإحداثيات](fundamentals/co-ordinate-system.md)
* **rotation** - زاوية دوران الشكل بالدرجات
* **resolution** - راجع [الدقة](fundamentals/resolution.md)
* **Fill state** - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

يحمّل ملف SVG لإنشاء أشكال مخصصة.

{% hint style="warning" %}
Liberation متوافق مع تنسيق _SVGTiny_. يُوصى باستخدام InkScape، لكن معظم تطبيقات الرسومات المتجهة يمكنها التصدير بهذا التنسيق. تأكد من تحويل أي نص إلى أشكال قبل التصدير. سيعرض Liberation الحدود الخطية، ويمكنه اختياريًا استخدام التعبئات كـ masks. تأكد من أن خطوطك ليست سوداء، وإلا فلن تظهر من دون معدّل لون!
{% endhint %}

* **Import SVG** - حمّل ملف SVG من القرص.

{% hint style="info" %}
بعد تحميل SVG، يتم تحويل المحتوى وحفظه داخل clip، لذلك لا تحتاج إلى الاحتفاظ بمرجع إلى الملف، إلا إذا أردت لاحقًا تغيير إعدادات mask.
{% endhint %}

* **Use fills as masks** - يعالج أي شكل ممتلئ باعتباره mask، أي مملوءًا بالأسود. سيتم ضبط هذا تلقائيًا إذا كان ملف SVG يحتوي على أي أشكال ممتلئة. إذا لم يحتوِ على أشكال ممتلئة، فسيتم تعطيله. راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - إذا لم تكن الأشكال في ملف SVG تحتوي على حد خارجي، فلن نتمكن من رسمها! يضيف هذا الخيار حدًا خارجيًا (أو _stroke_) إلى أي شكل ممتلئ. إذا لم يكن ملف SVG يحتوي على أي أشكال ذات stroke، فسيتم ضبطه تلقائيًا. وإذا لم يحتوِ على أي أشكال ممتلئة، فسيتم تعطيله.
* **Invert black lines** - إذا كانت كل الخطوط في ملف SVG سوداء فلن تتمكن من رؤيتها! يحولها هذا الخيار إلى اللون الأبيض. يتم ضبطه تلقائيًا إذا كان ملف SVG يحتوي على أشكال سوداء فقط، لكنه يُعطّل إذا لم تكن لديك أي أشكال سوداء.
* **Render profile** - راجع [ملف تعريف العرض](fundamentals/render-profile.md)
* **scale** - يضبط حجم SVG. يتم حساب هذا تلقائيًا عند تحميل SVG (للتأكد من أن الصورة مرئية)، لكن يمكن تعديله يدويًا بعد ذلك.
* موضع **x** و **y** - راجع [نظام الإحداثيات](fundamentals/co-ordinate-system.md)
* **rotation** - زاوية دوران الصورة بالدرجات
* **resolution** - راجع [الدقة](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

ينشئ حركة من تسلسل ملفات SVG.

* **Import SVG Sequence** - اختر المجلد الذي يحتوي على كل ملفات SVG. لاحظ أنه يتم تحميلها بالترتيب الأبجدي الرقمي.

{% hint style="info" %}
بعد تحميل تسلسل SVG، يتم تحويل المحتوى وحفظه داخل clip، لذلك لا تحتاج إلى الاحتفاظ بمرجع إلى الملفات، إلا إذا أردت لاحقًا تغيير إعدادات mask.
{% endhint %}

* **Use fills as masks** - يعالج أي شكل ممتلئ باعتباره mask، أي مملوءًا بالأسود. سيتم ضبط هذا تلقائيًا إذا كان أي من ملفات SVG لديك يحتوي على أشكال ممتلئة. إذا لم يحتوِ أي منها على أشكال ممتلئة، فسيتم تعطيله. راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - إذا لم تكن الأشكال في ملفات SVG لديك تحتوي على أي حدود خارجية، فلن نتمكن من رسمها! يضيف هذا الخيار حدًا خارجيًا (أو _stroke_) إلى أي شكل ممتلئ. إذا لم تكن ملفات SVG لديك تحتوي على أي أشكال ذات stroke، فسيتم ضبطه تلقائيًا. وإذا لم يحتوِ أي منها على أشكال ممتلئة، فسيتم تعطيله.
* **Invert black lines** - إذا كانت كل الخطوط في ملفات SVG لديك سوداء فلن تتمكن من رؤيتها! يحولها هذا الخيار إلى اللون الأبيض. يتم ضبطه تلقائيًا إذا كانت ملفات SVG لديك تحتوي على أشكال سوداء فقط، لكنه يُعطّل إذا لم تكن لديك أي أشكال سوداء.
* **Render profile** - راجع [ملف تعريف العرض](fundamentals/render-profile.md)
* **scale** - يضبط حجم الصورة.
* موضع **x** و **y** - راجع [نظام الإحداثيات](fundamentals/co-ordinate-system.md)
* **rotation** - زاوية دوران الصورة بالدرجات
* **resolution** - راجع [الدقة](fundamentals/resolution.md)
* **speed** - مدة الحركة كاملةً، بالموازير.
* **time per frame** - إذا تم ضبط هذا الخيار، فستكون المدة لكل إطار بدلًا من الطول الكامل للحركة. لذلك إذا تم ضبط _speed_ على ¼، فسيكون كل إطار بمقدار ضربة واحدة.
* **animation direction** -
  * _FORWARDS_ - تعمل الحركة إلى الأمام ثم تعود في حلقة إلى البداية
  * _BACKWARDS_ - تعمل الحركة إلى الخلف ثم تعود في حلقة إلى النهاية
  * _PINGPONG_ - تعمل الحركة إلى الأمام ثم إلى الخلف في حلقة
  * _MANUAL_ - يتم ضبط الإطار الحالي باستخدام إعداد _position manual_
* **position manual** - اضبط الإطار الحالي، حيث 0% هو الإطار الأول و 100% هو الإطار الأخير. يمكن ضبط ذلك يدويًا أو باستخدام مذبذب خارجي.
* _MOVE TO FRONT / MOVE TO BACK_ - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

ينشئ نصًا باستخدام خط TrueType أو OpenType.

* **Text** - اكتب النص الذي تريده هنا
* **Font** - اختر الخط الذي تريده

{% hint style="info" %}
لإضافة المزيد من الخطوط إلى Liberation، انسخ ملفات .ttf أو .otf إلى المجلد data/resources/fonts.
{% endhint %}

* **Render profile** - راجع [ملف تعريف العرض](fundamentals/render-profile.md)
* **horizontal alignment** - اختر _LEFT_ أو _CENTRE_ أو _RIGHT_ لتحديد محاذاة النص.
* **Fill state** - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)
* **size** - حجم النص
* **colour -** راجع [إعدادات اللون و HSB](fundamentals/colour-settings-and-hsb.md)
* موضع **x** و **y** - راجع [نظام الإحداثيات](fundamentals/co-ordinate-system.md)
* **rotation** - زاوية دوران الصورة بالدرجات
* **resolution** - راجع [الدقة](fundamentals/resolution.md)
* **reveal** - استخدم هذا لإظهار النص تدريجيًا، حرفًا واحدًا في كل مرة. عندما تكون هذه القيمة بين 0 و 50% سيظهر النص تدريجيًا من اليسار إلى اليمين. وعندما تكون بين 50% و 100% سيختفي النص من اليسار إلى اليمين. يمكنك توصيل مذبذب بهذا المقبس لإنشاء حركات.
* **reveal by word** - عند ضبطه، سيعمل _reveal_ على أساس كلمة بكلمة بدلًا من حرف بحرف.
* **countdown** - نظام عدّ تنازلي (تم تنفيذه على عجل!). سيتغير كل ضربتين، لذلك إذا أردت الثواني فتأكد من أنك على 120bpm.
* **countdown start** - الرقم الذي تريد أن يبدأ منه العدّ التنازلي
* _MOVE TO FRONT / MOVE TO BACK_ - راجع [التعبئات و masks وترتيب العمق](fundamentals/fills-masks-and-depth-sorting.md)
