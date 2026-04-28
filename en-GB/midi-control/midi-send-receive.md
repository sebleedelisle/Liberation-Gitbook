---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

The MIDI Send/Receive system is separate from the APC40 controls, and is a way to get MIDI data in and out of Liberation. Functions like starting and stopping clips, adjusting global settings, effects and clip parameters all have an associated MIDI command.

{% hint style="info" %}
The MIDI Send/Receive system was initially built before Liberation had any Timeline functionality; it was a workaround you could use to record and play back a show into music software like Logic Pro or Cubase.

It gives you direct control over clips, effects and settings, irrespective of the display and clip deck scroll position. More systemic live control capabilities like tap tempo, assigning zones, and arming/disarming are not implemented.
{% endhint %}

### MIDI Send/Receive settings

Open the _MIDI Send/Receive_ panel (with the menu _View -> MIDI Send/Receive_). You'll notice that you have options to _SEND, RECEIVE,_ or _BOTH_ send and receive, along with the ability to choose which MIDI interfaces you want to use.

{% hint style="danger" %}
Use the _BOTH_ setting with caution. MIDI devices and software can be configured to send back data that they get in, this could cause a feedback loop of MIDI data, and this is not good!
{% endhint %}

### MIDI mapping

See [midi-send-receive-default-mapping.md](../reference/midi-send-receive-default-mapping.md "mention")

I plan to add much more customisable MIDI mapping in the future but in the meantime you can use apps like [BOME](https://www.bome.com/products/miditranslator) and [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) to translate between Liberation and your custom hardware.
