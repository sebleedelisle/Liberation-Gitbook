---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 نظرة عامة على التحكم عبر MIDI

يستخدم Liberation ‏MIDI بعدة طرق:

* كوحدة تحكم للعروض المباشرة. يمكن لأجهزة APC40 Mk1/Mk2 وAPC Mini وMIDI Fighter Twister الاتصال تلقائيًا عند توفر الجهاز المطابق. راجع [وحدات تحكم MIDI للعروض المباشرة](live-control-with-the-apc40.md).
* كمصدر لمزامنة الساعة، باستخدام رسائل MIDI clock ورسائل موضع الأغنية في MIDI. راجع [ساعة MIDI](../tempo-synchronisation.md#midi-clock)
* كإدخال تفاعلي في node ‏MIDI notes لإنشاء مؤثرات بأسلوب "قيثارة الليزر". راجع [MIDI notes](../clip-editor/operator-nodes/midi-notes.md)
* كنظام إدخال/إخراج أكثر عمومية باستخدام نظام MIDI Send/Receive. راجع [إرسال/استقبال MIDI](midi-send-receive.md)

تتبع وحدات التحكم المباشرة المدعومة حالة Liberation المعروضة على الشاشة: تضيء أزرار Clip بألوان مجموعاتها، وتعرض أزرار zone حالة كل zone، وتتبع المقابض أو المشفرات المعينة عناصر التحكم في التأثير الحالي أو في لوحة Parameters.
