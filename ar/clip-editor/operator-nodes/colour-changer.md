---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 تغيير اللون

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> تغيير اللون

الوصف

* **hue, saturation, brightness** - قيم اللون، راجع [إعدادات اللون و HSB](../fundamentals/colour-settings-and-hsb.md)
* **hue mode** -
  * OFF - لا يتم تغيير درجة اللون
  * FIXED - يتم ضبط درجة لون العناصر على قيمة hue
  * SHIFT - يتم إزاحة درجة لون العناصر بمقدار القيمة، لذلك ستبقى العناصر ذات الألوان المختلفة مختلفة، لكنها ستتحرك فقط على طول قيمة درجة اللون.
* **saturation mode** -
  * OFF - لا يتم تغيير التشبّع
  * FIXED - يتم تثبيت التشبّع على القيمة المحددة.
* **brightness mode** -
  * OFF - لا يتم تغيير السطوع
  * FIXED - يتم ضبط سطوع العناصر على قيمة brightness
  * MULTIPLY - يتم دمج سطوع العناصر مع قيمة brightness، لذلك إذا كانت تومض فستظل تومض، لكن حتى السطوع المحدد هنا فقط.
* **blend** - مدى قوة تطبيق مغيّر اللون؛ 0% يعني عدم تطبيقه إطلاقًا، و100% يعني تطبيقًا كاملًا، و50% يعني مزيجًا بين اللون الحالي والقيم الجديدة.
