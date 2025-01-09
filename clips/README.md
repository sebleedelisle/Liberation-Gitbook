# 🟧 Clips & Clip deck

### What is a clip?

All laser content within Liberation is stored inside of clips.

Clips can contain atmospheric beam effects or graphical animations and they are usually a looping cycle. They can be directed into any zone (or Canvas Target Area) and are triggered using the clip buttons inside the clipdeck.

Clip content is created using the versatile node-based clip editor system. (See [clip-editor.md](../../designing-content/clip-editor.md "mention") for more details)

### The clip deck

<figure><img src="../../.gitbook/assets/clips-clip-deck" alt=""><figcaption><p>The default clip deck</p></figcaption></figure>

The clip deck is the on-screen grid of clips and it usually extends beyond the visible area that you can see.

Scroll the clip deck left and right using :

* The left and right arrow keys
* Trackpad 2 finger swipe (or mouse scroll left and right if your mouse can do that!)
* The _Cue Level_ scroll wheel on the APC40

Scroll the clip deck a full page left and right using :

* CMD/CTRL plus the left and right arrow keys
* The _Device <- and ->_ buttons on the APC40

#### The mini clip visualiser

Along the top of the clip deck you will see a small representation of the entire clip deck. The lit up section represents the clips that are currently visible.

### Starting and stopping clips

To start a clip, press the button for that clip (either on screen or on your MIDI controller).

To stop the clip, press it again.

If you start a new clip (in the same group) the first clip will automatically stop.

To start a new clip without stopping other clips you can either

* Press the shift key (or APC40 shift button) while starting the new clip; or
* Re-press the currently running clip(s) while you start the new clip.

The clip groups are independent of each other so starting a clip in one group will not affect clips in any of the others. See [groups.md](groups.md "mention")

### Flash mode

If a clip is within a group that is set to _flash mode_, then it behaves slightly differently; the clip will only continue running as long as you have the clip button pressed. As soon as you let go it stops. (By default clip group 3 - the red one - is set to _flash mode.)_

### The currently selected clip

<figure><img src="../../.gitbook/assets/clips-selected-active.png" alt="" width="269"><figcaption><p>Two clips that are currently running. The white outline denotes that the clip on the right is the <em>currently selected clip.</em></p></figcaption></figure>

That the clip lights up on screen when it is currently running (and its mini clip visualiser representation flashes). You will also notice that the last clip you pressed also has a white outline around it. This indicates that it is the _currently selected clip._

ALT/OPTION click on a clip to select it without activating it. Use ALT/OPTION + SHIFT click to select multiple clips.&#x20;

### Assigning zones

<figure><img src="../../.gitbook/assets/clips-zones" alt=""><figcaption><p>The zone buttons at the top, and the Flip X / Flip Y buttons at the bottom.</p></figcaption></figure>

Underneath the clips, you can see a row of zone buttons (both on-screen and reflected on the APC40), marked _BEAM 1_ to _BEAM 8_ by default. Use these buttons to toggle zones for the _currently selected clip_.

#### Scrolling through the zones

If there are more than 8 zones you can scroll left and right using :

* SHIFT plus the <- and -> cursor keys
* The _DEV ON/OFF_ and _DEV LOCK_ buttons on the APC40

### Flip X and Y

Underneath each zone button you can see buttons marked _X_ and _Y._ These flip the output to each zone horizontally and vertically, respectively.

{% hint style="info" %}
You don't need to make a new zone to have different mirror settings. The X and Y flip settings apply to this clip only, they're not a setting of the zone.
{% endhint %}
