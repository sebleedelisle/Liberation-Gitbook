---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ مذبذب إدخال الصوت

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

يحوّل مستوى إدخال الصوت إلى قيمة خاصية.

{% hint style="info" %}
يستخدم مذبذب إدخال الصوت واجهة الصوت الافتراضية، لكن يمكنك تغييرها من _Preferences_. افتح القائمة _Liberation -> Preferences._

ضمن إعدادات _Sound Input_، يمكنك تحديد واجهة الصوت التي تريد استخدامها، إلى جانب بعض الإعدادات الأخرى لضبط مستوى الصوت.
{% endhint %}

* **range min / range max** - القيمتان الدنيا والعليا اللتان يتم تعيين شكل الموجة ضمنهما
* **channel** - إذا كانت واجهة الصوت لديك تحتوي على أكثر من قناة إدخال، يمكنك هنا تحديد القناة التي تريد التقاطها.

{% hint style="info" %}
من التقنيات الممتعة الحصول على عدة تغذيات صوتية من طاولة المزج، وبهذه الطريقة يمكن أن تستجيب Clips مختلفة لآلات موسيقية مختلفة.
{% endhint %}

{% hint style="info" %}
يمكنك استخدام واجهة صوت واحدة فقط في كل مرة عبر جميع _Sound Inputs_ (المحددة في لوحة _App Settings_). إذا أردت استخدام أكثر من واجهة لهذا الغرض، يمكنك على macOS [إنشاء Aggregate Device](https://support.apple.com/en-gb/HT202000) لدمج الإدخالات في مصدر صوت افتراضي واحد. (توجد أيضًا تطبيقات كثيرة على Windows يمكنها فعل ذلك، لكنني لم أجرّبها).
{% endhint %}

* **clamp min / clamp max** - استخدم هذا لتحديد نطاق المستويات الذي تريد الاستجابة له. لن تحتاج عادةً إلى ضبط هذا إذا كانت إعدادات gate و limit (في لوحة _App Settings_) مضبوطة بشكل صحيح، لكن يمكن استخدامها لبعض المؤثرات الإبداعية.

{% hint style="info" %}
سترى أيقونة ميكروفون صغيرة على زر Clip عندما يحتوي على مذبذب _Sound Input_.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
