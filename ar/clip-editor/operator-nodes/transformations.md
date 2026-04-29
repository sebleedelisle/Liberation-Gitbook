---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 التحويلات

## &#x20;Translate

ينقل كل المحتوى على محاور x و/أو y و/أو z. لاحظ أن نظام الإحداثيات يتمركز في الوسط، ويمتد من ‎-200 إلى ‎+200 على محوري x و y. راجع [نظام الإحداثيات](../fundamentals/co-ordinate-system.md).

* **x** - المسافة المطلوب نقلها على محور x (يسار - يمين).
* **y** - المسافة المطلوب نقلها على محور y (أعلى - أسفل).

#### خيارات 3D (متاحة عند تحديد 3D)

* **z** - المسافة المطلوب نقلها على محور z (إلى الخلف والأمام داخل الشاشة).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

يدير كل المحتوى. تكون القيم بالدرجات. راجع [نظام الإحداثيات](../fundamentals/co-ordinate-system.md).

* **rotation** - مقدار تدوير المحتوى باتجاه عقارب الساعة بالدرجات. يتم تدوير كل شيء حول نقطة الأصل (0,0)، أي المركز.
* **pivot point x / pivot point y** - استخدم هذه القيم لإزاحة نقطة أصل الدوران.

#### خيارات 3D (متاحة عند تحديد 3D)

* **rotation x** - الدوران حول محور x (pitch).
* **rotation y** - الدوران حول محور y (yaw).
* **pivot point z** - موضع إزاحة الدوران على محور z.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

يغيّر حجم كل المحتوى.

* **scale** - نسبة التحجيم.
* **scale x / scale y** - إذا كنت تريد التحجيم أفقيًا و/أو عموديًا، فاستخدم هذه الخيارات.

{% hint style="warning" %}
عند تحجيم أي شيء إلى 0% على أي محور، فإنه يختفي!
{% endhint %}
