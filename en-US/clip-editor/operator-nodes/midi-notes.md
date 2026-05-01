---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Creates “laser harp” style effects where incoming MIDI notes trigger beams or shapes across a range. The node uses whatever content you pass into it as the _source_ for each note - feed it a dot, and you’ll get a row of dots. Feed it a shape like a circle, and you’ll get a row of circles, and more complex shapes will be replicated just the same.

You can choose which MIDI interface Liberation listens to in **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – which MIDI channel to listen to (0 = all channels, 1–16 = specific channel)
* **width** – total width that the notes spread across.
* **MIDI note min / max** – the lowest and highest MIDI note values in the range.
* **ignore out of range notes** – filters out any notes beyond the set range. If disabled, out-of-range notes are "clamped" to the nearest available note (high notes trigger the top of the range, low notes trigger the bottom).
* **auto extend range** – automatically widens the range if notes are played outside of it.

{% hint style="info" %}
Not sure what range of notes you’re getting? Switch on **auto extend range**, set **MIDI note min** really high and **MIDI note max** really low, then play through your notes. The system will catch them all and expand the range for you. Once you’ve got everything, just turn **auto extend range** off to lock it in.
{% endhint %}

* **leave all notes visible** – creates beams or shapes for all notes in the range whether or not they’re playing, giving you a “laser harp” effect.
* **hit color** – the color that appears when a note is triggered.
* **hit color hold time** – how long the hit color stays at full brightness before fading. Value is in seconds (0–1). _100% = 1 second._
* **hit color decay time** – how long it takes the hit color to fade back after the hold time. Value is in seconds (0–1). _100% = 1 second._

{% hint style="info" %}
If your content is already pure white, setting the hit color to white won’t make any difference. For the best results, use a saturated color for your content and set the hit color to white - this gives a really nice flash effect when notes are triggered.
{% endhint %}

* **note off fade out time** – how long it takes the note to fade after being released. Value is in seconds (0–1). _100% = 1 second._
* **hit scale factor** – how much the note scales up when triggered (e.g. 2 = double size).
* **hit scale hold time** – how long the note stays scaled up before shrinking back. Value is in seconds (0–1). _100% = 1 second._
* **hit scale decay time** – how long it takes for the note to return to its original size. Value is in seconds (0–1). _100% = 1 second._
* **note off shrink time** – how long it takes to shrink back to original size after the note has been released. Value is in seconds (0–1). _100% = 1 second._ (Has no effect when **leave all notes visible** is enabled.)

{% hint style="info" %}
Scaling - Note that if your content is a single dot then the scaling will have no effect!
{% endhint %}
