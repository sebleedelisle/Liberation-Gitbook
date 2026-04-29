---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 إرسال/استقبال MIDI

نظام إرسال/استقبال MIDI منفصل عن عناصر تحكم APC40، وهو طريقة لإدخال بيانات MIDI إلى Liberation وإخراجها منه. ترتبط وظائف مثل بدء Clips وإيقافها، وضبط الإعدادات العامة، والمؤثرات، ومعلمات Clip، بأمر MIDI خاص بها.

{% hint style="info" %}
تم إنشاء نظام إرسال/استقبال MIDI في البداية قبل أن تتوفر في Liberation أي وظائف Timeline؛ وكان حلاً بديلاً يمكنك استخدامه لتسجيل عرض وتشغيله داخل برامج موسيقية مثل Logic Pro أو Cubase.

يوفر لك تحكمًا مباشرًا في Clips والمؤثرات والإعدادات، بغض النظر عن موضع التمرير في العرض وClip Deck. أما إمكانات التحكم المباشر الأكثر شمولاً مثل tap tempo، وتعيين zones، وarm/disarm، فهي غير مطبقة.
{% endhint %}

### إعدادات MIDI Send/Receive

افتح لوحة _MIDI Send/Receive_ (من القائمة _View -> MIDI Send/Receive_). ستلاحظ أن لديك خيارات _SEND, RECEIVE,_ أو _BOTH_ للإرسال والاستقبال، مع إمكانية اختيار واجهات MIDI التي تريد استخدامها.

{% hint style="danger" %}
استخدم إعداد _BOTH_ بحذر. يمكن تهيئة أجهزة MIDI والبرامج لإعادة إرسال البيانات التي تستقبلها، وقد يؤدي ذلك إلى حلقة تغذية راجعة من بيانات MIDI، وهذا غير مرغوب!
{% endhint %}

### تعيين MIDI

راجع [تعيين MIDI Send/Receive الافتراضي](../reference/midi-send-receive-default-mapping.md)

أخطط لإضافة تعيين MIDI أكثر قابلية للتخصيص في المستقبل، لكن في الوقت الحالي يمكنك استخدام تطبيقات مثل [BOME](https://www.bome.com/products/miditranslator) و[Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) للترجمة بين Liberation والعتاد المخصص لديك.
