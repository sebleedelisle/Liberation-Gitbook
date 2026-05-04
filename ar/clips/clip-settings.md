---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ إعدادات Clip

### لوحة إعدادات Clip

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>لوحة إعدادات Clip</p></figcaption></figure>

غيّر حجم خرج Clip باستخدام _Scale X_ و _Scale Y_. يكونان مرتبطين معًا ما لم تضغط على مفتاح _SHIFT_.

غيّر الموضع الأفقي والعمودي للـ Clip باستخدام _Shift X_ و _Shift Y_.

تُعد _Zone Delay/Chase_ ميزة ممتعة بما يكفي لتستحق قسمًا خاصًا بها. [Zone Delay/Chase](zone-delay-chase.md "mention")

### لوحة Parameters

تعرض اللوحة الموجودة إلى يمين Clip Deck ثمانية معاملات سياقية. عند تحديد Clip، تكون عناصر التحكم الأولى هي _Shift X_ و_Shift Y_ و_Zone Delay_ الخاصة بالـ Clip المحدد، ثم عناصر التحكم العامة _Spin_ و_Scale_.

تُعكس هذه المعاملات نفسها على وحدات تحكم MIDI المدعومة. إذا لم يكن هناك Clip محدد، تبقى الخانات الخاصة بالـ Clip فارغة. إذا ضغطت باستمرار على زر مجموعة، يتغير أول عنصري تحكم إلى زمنَي fade in وfade out لتلك المجموعة.

### قفل Clips

إذا كان Clip مقفلاً، فلا يمكن نقله أو حذفه. لقفل Clip، استخدم خانة الاختيار _Locked_ في قائمة النقر بزر الماوس الأيمن. في لوحة إعدادات Clip ستحصل على بعض الخيارات الإضافية.

* _UNLOCK ALL -_ يفتح قفل كل Clip في Clip Deck.
* _AUTO-LOCK_ - عند تفعيل _Auto-Lock_، سيتم قفل أي Clip يتم تشغيله تلقائيًا (سواء عبر المخطط الزمني أو نظام تسجيل/تشغيل MIDI). يكون هذا مفيدًا إذا كنت قد برمجت عرضًا في Logic Pro (أو برنامج مشابه) ولا تريد تعديل Clips المستخدمة في العرض عن طريق الخطأ.
* _LOCKED CLIPS ZONES_ - إذا كان هذا الخيار مفعلاً، فلن تتمكن من تغيير zones لأي Clip مقفل.
* _LOCKED CLIPS PARAMS_ - إذا كان هذا الخيار مفعلاً، فلن تتمكن من تغيير المعلمات (مثل scale و shift وما إلى ذلك) لأي Clip مقفل.

### قائمة النقر بزر الماوس الأيمن

إذا نقرت بزر الماوس الأيمن على Clip، ستظهر قائمة تحتوي على بعض الخيارات الخاصة بذلك Clip. راجع [مقدمة إلى Clip Editor](../clip-editor/clip-editor-intro.md "mention")، و[إعدادات Clip](clip-settings.md "mention")، و[المجموعات](groups.md "mention")لمزيد من المعلومات عن العناصر الأولى في هذه القائمة.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

يتم ضبط Clips افتراضيًا على _retrigger_. يعني ذلك أنه بغض النظر عن وقت الضغط عليه، سيبدأ Clip التشغيل من تلك اللحظة. لذلك إذا بدأته متأخرًا، فسيكون تحريك Clip متأخرًا قليلًا وخارج التوقيت.

{% hint style="info" %}
إذا استخدمت _Tap Tempo_ أثناء تشغيل Clip مضبوط على retrigger، فسيقوم النظام بضبط توقيت Clip ليصبح متزامنًا، حتى إذا لم تبدأه تمامًا على الإيقاع.
{% endhint %}

إذا لم يكن _Retrigger_ مفعلاً، فسيظل Clip دائمًا ضمن التوقيت — كما لو أن Clip بدأ من بداية الساعة تمامًا. هذا مناسب عندما تكون متزامنًا تمامًا مع الموسيقى عبر إشارة توقيت خارجية.

{% hint style="info" %}
غالبًا ما تكون Clips مصممة للتكرار إلى ما لا نهاية، لكن يمكنك تصميمها بحيث تعمل مرة واحدة فقط أو عدة مرات محدودة. تأكد من إبقائها مضبوطة على _retrigger_، وإلا فلن تُعاد من البداية!
{% endhint %}

### زمن الدخول/الخروج الانتقالي (fade)

يمكن ضبط Clips لتظهر وتختفي تدريجيًا بمدة تُقاس بالثواني. افتراضيًا، سيتم توريث زمن fade من إعدادات المجموعة الخاصة بها (ويمكن تغييره بالنقر بزر الماوس الأيمن على زر المجموعة).

إذا كنت تريد مدة fade مختلفة عن مدة مجموعة Clip، فأوقف أولاً زر _USE GROUP DEFAULT_، ثم اضبط منزلقَي _In time_ و _Out time_ الخاصين بالـ Clip.
