# ✅ MIDI send/receive default mapping

**Clip on and off are triggered by MIDI note on / off on channels 1 to 14**

Clips have an horizontal (x) and vertical (y) position, right-click on a clip and you’ll see its position. Midi can trigger clips starting at 0,0.

{% hint style="info" %}
Note that clip control with this system is absolute and the clip positions do not change as you scroll the clip deck.&#x20;
{% endhint %}

Midi channel 1, note 1 is clip 0,0, note 2 is clip 0,1 note 3 is clip 0,2 moving down in rows and along in columns. Once it gets to 128 it moves to the next channel and starts again. So you have a total of 128 x 14 = 1792 clips that are accessible via MIDI.

MIDI note for clip co-ordinates :&#x20;

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Note : 1</td><td>Note : 6</td><td>Note : 11</td><td>Note : 16</td><td>Note : 20 </td></tr><tr><td><strong>y : 1</strong></td><td>Note : 2</td><td>Note : 7</td><td>Note : 12</td><td>Note : 17</td><td>...etc</td></tr><tr><td><strong>y : 2</strong></td><td>Note : 3</td><td>Note : 8</td><td>Note : 13</td><td>Note : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Note : 4</td><td>Note : 9</td><td>Note : 14</td><td>Note : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Note : 5</td><td>Note : 10</td><td>Note : 15</td><td>Note : 20</td><td></td></tr></tbody></table>

Note that a MIDI note on event starts the clip, and the equivalent note off event stops the clip. This is irrespective of the trigger mode on the group. The system was originally designed for playback and recording so having the notes toggle a clip would have been undesirable.

### **Effects**

MIDI control change (CC) messages on **channel 15** adjust the effects.\
Effect 1 responds to CC 1-4, value 0-127\
Effect 2 responds to CC 5-8, value 0-127\
Effect 3 responds to CC 9-12, value 0-127\
… and so on.

Note that the effect control changes are in groups of 4. The first in each group controls the effect level, the second in each group control the parameter for that effect. The third and fourth are currently reserved for future use.

### **Global settings**

MIDI control change messages on **channel 16** change the global settings :\
CC 1 : Shift X (horizontal) 0 -127, 64 is in the middle\
CC 2 : Shift Y (vertical) 0 -127, 64 is in the middle\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

And importantly :\
CC 15 : Global brightness

Please note that this system was originally designed for recording and playback, allowing you to use Logic, Ableton or other DAW to create timeline animations. Although you can use it for live control, it has not been optimised for that use, and some functions for live control are missing compared to the APC40 set up.
