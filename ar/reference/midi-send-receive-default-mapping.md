---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ تعيين MIDI الافتراضي للإرسال/الاستقبال

**يتم تشغيل Clip وإيقافه بواسطة رسائل MIDI note on / off على القنوات من 1 إلى 14**

تحتوي Clips على موضع أفقي (x) وموضع عمودي (y). انقر بزر الماوس الأيمن على Clip وسترى موضعه. يمكن لـ MIDI تشغيل Clips بدءًا من 0,0.

{% hint style="info" %}
لاحظ أن التحكم في Clip باستخدام هذا النظام يكون مطلقًا، ولا تتغير مواضع Clips عند تمرير Clip Deck.
{% endhint %}

القناة 1 في MIDI، النغمة 1، هي Clip عند 0,0، والنغمة 2 هي Clip عند 0,1، والنغمة 3 هي Clip عند 0,2، مع الانتقال إلى أسفل ضمن الصفوف ثم عبر الأعمدة. عند الوصول إلى 128 ينتقل إلى القناة التالية ويبدأ من جديد. لذلك لديك إجمالي 128 × 14 = 1792 من Clips يمكن الوصول إليها عبر MIDI.

نغمة MIDI لإحداثيات Clip:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>النغمة: 1</td><td>النغمة: 6</td><td>النغمة: 11</td><td>النغمة: 16</td><td>النغمة: 20</td></tr><tr><td><strong>y : 1</strong></td><td>النغمة: 2</td><td>النغمة: 7</td><td>النغمة: 12</td><td>النغمة: 17</td><td>...إلخ</td></tr><tr><td><strong>y : 2</strong></td><td>النغمة: 3</td><td>النغمة: 8</td><td>النغمة: 13</td><td>النغمة: 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>النغمة: 4</td><td>النغمة: 9</td><td>النغمة: 14</td><td>النغمة: 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>النغمة: 5</td><td>النغمة: 10</td><td>النغمة: 15</td><td>النغمة: 20</td><td></td></tr></tbody></table>

لاحظ أن حدث MIDI note on يبدأ Clip، وأن حدث note off المكافئ يوقف Clip. يحدث ذلك بغض النظر عن وضع التشغيل في المجموعة. صُمم النظام في الأصل للتشغيل والتسجيل، لذلك لم يكن من المرغوب أن تجعل النغمات Clip يعمل بنمط التبديل.

### **المؤثرات**

تضبط رسائل MIDI control change (CC) على **القناة 15** المؤثرات.\
يستخدم المؤثر 1 رسائل CC 0-3، بقيمة 0-127\
يستخدم المؤثر 2 رسائل CC 4-7، بقيمة 0-127\
يستخدم المؤثر 3 رسائل CC 8-11، بقيمة 0-127\
… وهكذا.

تتحكم كل مجموعة من أربعة عناصر في المستوى و3 معلمات لذلك المؤثر:

<table><thead><tr><th width="164">المؤثر:</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>المستوى</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>المعلمة 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...إلخ</td></tr><tr><td><strong>المعلمة 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>المعلمة 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **الإعدادات العامة**

تغيّر رسائل MIDI control change على **القناة 16** الإعدادات العامة:\
CC 1 : Shift X (أفقي) 0 -127، وتكون 64 في المنتصف\
CC 2 : Shift Y (عمودي) 0 -127، وتكون 64 في المنتصف\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

وبشكل مهم:\
CC 15 : Global Brightness

يرجى ملاحظة أن هذا النظام صُمم في الأصل للتسجيل والتشغيل، مما يتيح لك استخدام Logic أو Ableton أو أي DAW آخر لإنشاء حركات على خط زمني. وعلى الرغم من إمكانية استخدامه للتحكم المباشر أثناء الأداء، فإنه لم يُحسّن لهذا الاستخدام، وبعض وظائف التحكم المباشر غير متوفرة مقارنة بإعداد APC40.
