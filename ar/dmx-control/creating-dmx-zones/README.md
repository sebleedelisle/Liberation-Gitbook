---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 إنشاء DMX zones

1. وصّل Art-Net node واضبطه كما هو موضح في [الاتصال بعقدة Art-Net](../connecting-to-an-artnet-node.md "mention").
2. افتح **DMX Zones** وانقر على **ADD DMX ZONE**.
3. اضبط **Node** و**Universe** و**Address** الخاصة بالـ zone لتطابق الجهاز.
4. اختر **Preset** للجهاز. يحدد الإعداد المسبق قنوات DMX التي تتلقى قيماً ثابتة، أو قيم تشغيل/إيقاف المحتوى، أو لون RGB، أو موضع X/Y، أو السطوع، أو مدخلات DMX Value الصريحة.
5. انقر على **Edit DMX profile/channel mapping** (أيقونة أشرطة التمرير) لتعديل ربط القنوات. يبدأ الإعداد المسبق الافتراضي بقناة تشغيل/إيقاف للمحتوى وقنوات لون RGB.
6. عيّن Clips إلى DMX zone بالطريقة نفسها التي تعيّنها بها إلى beam zone أو canvas zone.
7. اضغط على **ARM** عندما تكون جاهزاً لجعل الـ zone يخرج DMX.

{% hint style="warning" %}
ترسل DMX zones المفعّلة فقط قيماً مباشرة. أما DMX zones غير المفعّلة فتمسح قنواتها المرتبطة إلى الصفر، وهذا أكثر أماناً عند إعداد الأجهزة.
{% endhint %}

يكون خرج DMX محدوداً أيضاً بمستوى ترخيصك. إذا كان زر **ARM** معطلاً، فتحقق مما إذا كان مستوى ترخيصك يتضمن خرج DMX، أو ما إذا كان قد تم بالفعل الوصول إلى الحد الأقصى لعدد DMX zones المفعّلة.
