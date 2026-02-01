# 🟩 Synchronising tempo to an audio track

{% embed url="https://youtu.be/sL0SsuTf7Pc" %}



Liberation’s timeline is designed to work with fixed or changing tempos, but getting reliable sync always starts with finding the tempo and lining the audio up correctly. This section describes the recommended workflow.

#### 1. Align the First Downbeat

Add your audio track to the timeline and make sure it is snapped to a beat so that the **first musical downbeat** of the track lines up exactly with the start of a bar.

This step is critical.

If the audio does not naturally start on a downbeat, you have two options:

* **Adjust the clip delay**\
  Right-click the audio clip and adjust the Delay value until the first downbeat lines up with a beat or bar marker.
* **Trim the audio externally**\
  Edit the audio file in an external editor such as Audacity so that the file starts exactly on the first downbeat, then re-import it.

{% hint style="info" %}
**Important:**\
If the start of the audio is not aligned to a beat or bar, the perceived start position of the music will shift backwards and forwards as you change the tempo. This makes accurate tempo matching extremely difficult.
{% endhint %}

#### 2. Set an Initial Tempo

If you have a rough idea of the BPM, enter it into the timeline tempo control and start playback from the beginning.

Watch the beat and bar markers carefully as the track plays.

* If the markers drift ahead of the music, reduce the tempo slightly.
* If they fall behind, increase the tempo slightly.
* Stop playback, adjust the tempo, and try again.

For most modern music, the tempo is a fixed whole-number BPM. Once you find the correct value, it should remain locked for the entire track.

#### 3. Use the Waveform as a Visual Guide

The audio waveform is a useful reference when matching tempo.

* Transients and peaks should line up with the vertical bar markers.
* Zoom in closely to check alignment over multiple bars.

**Tip:**\
Use the mouse wheel or trackpad gesture to zoom the timeline. Use the horizontal scroll wheel or gesture to move left and right. Working zoomed-in makes small adjustments much easier.

#### 4. Tracks with Non-Integer BPM

If the track does not use a whole-number BPM, drift will be more gradual.

* Zoom in further.
* Use smaller tempo adjustments.
* Check alignment over longer sections of the track rather than just the first few bars.

#### 5. Music with Tempo Changes

If the music speeds up or slows down, use the Tempo Map:

* Play the track and watch the beat markers.
* When drift becomes noticeable, add a tempo change at that point.
* Adjust the tempo for the new section until it locks again.

Repeat this process for each tempo change in the music.

#### 6. External Tempo Analysis (Optional)

As a last resort, you can analyse the track in a DAW such as Logic Pro and generate a tempo map automatically. Be aware that this often produces a large number of tempo changes, sometimes one per bar, which may be more detailed than necessary for most shows.
