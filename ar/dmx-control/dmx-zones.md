---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ DMX zones

DMX zones هي zones إخراج في Liberation تُرسل Art-Net/DMX بدلاً من نقاط الليزر. تظهر إلى جانب beam zones وcanvas zones، لذلك يمكن تعيين Clips إليها ضمن سير عمل اختيار zone نفسه.

افتح **DMX Zones** من القائمة، أو استخدم قسم DMX في Laser overview لإدارتها.

* **ADD DMX ZONE** - ينشئ DMX zone جديدة.
* **ARM** - يفعّل إخراج DMX لهذه zone. عند عدم تسليح DMX zone، تُمسح القنوات المعيّنة لها إلى الصفر.
* **Node** - يحدد رقم node في Art-Net.
* **Universe** - يحدد universe في Art-Net. القيمة المعروضة تبدأ من 1، لذلك يكون Universe 1 هو أول universe.
* **Address** - يعيّن عنوان البدء للجهاز. القيمة المعروضة تبدأ أيضاً من 1.
* **Preset** - يختار إعداد DMX المسبق الذي يربط محتوى Clip بقنوات DMX.
* **Edit DMX zone settings** (أيقونة القلم) - يفتح إعدادات zone مثل التمرير اليدوي للـ zone واتجاه الجهاز.
* **Edit DMX profile/channel mapping** (أيقونة أشرطة التمرير) - يفتح محرر إعداد DMX المسبق/القنوات.
* **Delete** - يحذف DMX zone.

### حدود التسليح

يعتمد عدد DMX zones التي يمكن تسليحها في الوقت نفسه على مستوى الترخيص لديك. إذا كان مستوى الترخيص لا يسمح بإخراج DMX، أو إذا كنت قد سلّحت بالفعل الحد الأقصى من DMX zones، فسيتم تعطيل زر **ARM** للـ zones الإضافية ويعرض أيقونة منع عند تمرير المؤشر فوقه.

ألغِ تسليح DMX zone أخرى، أو استخدم مستوى ترخيص بحد DMX أعلى، قبل تسليح المزيد من zones.
