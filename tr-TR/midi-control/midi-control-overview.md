---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 MIDI kontrolüne genel bakış

Liberation, MIDI’yi birkaç farklı şekilde kullanır:

* Canlı MIDI kontrolcüsü olarak. APC40 Mk1/Mk2, APC Mini ve MIDI Fighter Twister, eşleşen cihaz kullanılabilir olduğunda otomatik olarak bağlanabilir. Bkz. [Canlı MIDI kontrolcüleri](live-control-with-the-apc40.md "mention").
* MIDI clock ve MIDI song position mesajlarını kullanarak saat senkronizasyon kaynağı olarak. Bkz. [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* “Lazer arpı” tarzı efektler oluşturmak için MIDI notes node öğesinde etkileşimli giriş olarak. Bkz. [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* MIDI Send/Receive sistemini kullanarak daha genel bir giriş/çıkış sistemi olarak. Bkz. [MIDI Send/Receive](midi-send-receive.md "mention")

Desteklenen canlı kontrolcüler, Liberation ekranındaki durumu takip eder: Clip düğmeleri grup renkleriyle yanar, zone düğmeleri zone durumunu gösterir ve eşlenmiş knob’lar veya encoder’lar geçerli efektin ya da Parameters panelindeki kontrollerin durumunu izler.
