---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Live-MIDI-Controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40-Controller**

Das ist der Standard-Hardware-Controller für Liberation. Er wird dringend empfohlen, und man kann durchaus sagen, dass Liberation von Anfang an um diese Hardware herum entwickelt wurde. Sobald du den APC40 anschließt, verbindet sich Liberation automatisch damit.

{% hint style="warning" %}
_Oh nein! Mein USB-Stecker wurde mitten in der Show herausgezogen!_

Keine Panik – steck ihn einfach wieder ein. Liberation verbindet sich automatisch neu, ganz ohne Drama.
{% endhint %}

### APC40 Mark 1 oder Mark 2?

Kurz gesagt: Mark 2 wird empfohlen, weil er vollfarbige Buttons hat, die deutlich besser zur Clip Deck-Oberfläche von Liberation passen. Die Mark-1-Version funktioniert zur Not auch, ist aber etwas verwirrender, weil das Layout leicht von der Bildschirmdarstellung abweicht. Außerdem können die Buttons nur rot, orange oder grün leuchten und passen daher nicht zu den Clip-Farben.

{% hint style="info" %}
Der ursprüngliche APC40 Mark 1 erschien 2009(!), und manche bevorzugen ihn immer noch wegen seines Metallgehäuses und seines robusten, konsolenartigen Formfaktors. Der aktualisierte Mark 2 erschien 2014. Obwohl er 2024 eingestellt wurde, geht er 2025 aufgrund der Nachfrage von Visual Artists (Resolume usw.) und Laserists wieder in Produktion.
{% endhint %}

Die vollständige Liste der auf dem APC40 verfügbaren Bedienelemente findest du in der [APC40-Referenz](../reference/apc40-reference.md "mention").

### APC Mini

Liberation 1.0.3 enthält außerdem ein APC-Mini-Profil. Es belegt das 8x5-Clip-Raster, Buttons für zones, X/Y-Flip-Steuerungen für zones, Gruppen-Buttons, Stoppen aller Clips, Clip-Seitenwechsel, zone-Seitenwechsel, Tap Tempo, Bar Reset und Tempo Nudge. Die Fader steuern Effektpegel, und geshiftete Fader steuern Effektparameter. Der letzte Fader steuert Global Brightness.

### MIDI Fighter Twister

Das MIDI-Fighter-Twister-Profil ist für encoderlastige Steuerung gedacht, nicht für das Starten von Clips. Eine Encoder-Reihe steuert Parameter 1 für die Effekt-Slots 1–8, und eine weitere Reihe folgt den acht kontextbezogenen Bedienelementen im Parameters-Panel, einschließlich Clip Shift, zone Delay, globalem Spin/Scale und Gruppen-Fades.
