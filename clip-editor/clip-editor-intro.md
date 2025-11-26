# 🟩 Introduction to the Clip Editor

The clip editor is a versatile way to create laser content and it's at the heart of Liberation. It's easy to make simple things and yet flexible enough to make some incredibly sophisticated and complex effects.&#x20;

{% hint style="info" %}
The node based editor was the first part of Liberation that was made! It was born from a conversation with Rob Stanley at a UK laser meet up in 2018 about what an "object-oriented" laser content designer would look like.

Although it seems simple, it's quite a complex system to build, but by the start of 2019 I had a working demo that proved the concept - and it started this whole journey!
{% endhint %}

It's a node based visual editor (or [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) that will be familiar if you have used products like TouchDesigner, MaxMSP or VVVV. Although the clip editor is a little different and somewhat simpler as it's been designed specifically for vector graphics.&#x20;

You can open the Clip Editor by right clicking on the clip button and selecting _EDIT CLIP_. Or right click on an empty clip button and select _CREATE AND EDIT CLIP_.&#x20;

### Overview

What you'll see in the clip editor :&#x20;

* The **Creator** and **Operator node buttons** along the top&#x20;
* The **Oscillator node buttons** along the left
* A preview of the content in a panel on the right, and if you click on a node, you'll see a second preview that shows you the content at the node itself.
* All of the nodes and connections for the clip that you are editing (if it's a new clip this will be empty)
* The Clip Editor panel with various options

While you're editing, you will also see what the clip looks like in the 3D visualiser in the background.&#x20;

{% hint style="info" %}
If you don't see any output in the 3D visualiser, you may need to use the zone buttons to turn on the zones you want. You'll also need to make sure that _Preview to lasers_ is enabled, see [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel "mention") below.
{% endhint %}

### Building a clip

You typically start with one or more [creator nodes](creator-nodes.md), and connect [operators](operator-nodes/) from left to right that process the content. As you move creators and/or operators together you'll notice that they automatically connect to each other. And you can drag them apart to disconnect them again.&#x20;

### Adding nodes to your clip

Click and drag from one of the node buttons along the top or left into an empty space within the clip editor.&#x20;

### Adjusting settings for a node

Click on the cog icon button  (top right of the node) to open the properties panel for that node.&#x20;

### Enabling and disabling a node

Click on the power icon button (top left of the node) to enable and disable the node. The node will dim to show that it is not currently active. Note that content still passes through an operator even if it is disabled, but the node doesn't affect the content.&#x20;

### Connecting nodes together

Content is made with a creator node, and is passed along nodes from left to right; each operator affects the content in some way and passes it along to the next operator. Whatever is left at the end of the path is the clip's content. Creators and Operators are automatically connected to each other when you move them close together. To separate them, drag them apart again.&#x20;

{% hint style="info" %}
You can connect more than one node into the next node's input. This is helpful to combine multiple pieces of content
{% endhint %}

### Node properties and sockets

Each node has an array of sockets along the bottom and each one represents a property within the node, such as brightness, position, scale, rotation etc.&#x20;

[Oscillator nodes](oscillators/) can be connected to these sockets from below and used to animate these settings. Oscillator nodes have an output at the top, click and drag to pull out the connection and drop it into one of the other nodes' property sockets.&#x20;

### Oscillator nodes

Oscillator nodes are used to change properties over time. They typically represent waveforms such as a sawtooth or sine wave but some oscillator nodes use external inputs (such as the microphone input level) as their source.&#x20;

{% hint style="info" %}
If you've ever used an analog synth, you'll be familiar with the concept of oscillators which are commonly used to create waveforms or adjust the sound over time. Oscillators in Liberation do a similar job.&#x20;

**Fun fact:** the name _Liberation_ was inspired by the Moog Liberation, a synthesizer "keytar" released in 1980 and made famous by Herbie Hancock, Jean-Michel Jarre and even James Brown! &#x20;
{% endhint %}

Oscillators always have _range_ settings that control the minimum and maximum value of the property to be adjusted. And _Wave Oscillators_ always have a _duration_ setting that determines how fast the oscillator changes the value. See [wave-oscillators.md](oscillators/wave-oscillators.md "mention") for more information.&#x20;





&#x20;

### Clip editor panel

* Timer - at the top of the panel you'll see the current time for the clip as it progresses
* _RETRIGGER_ - restarts the clip from the beginning; extra useful if your clip doesn't loop
* _Preview to lasers_ - when this is checked, you'll see the 3D visualiser update as you edit this clip. If you turn it off, you'll see whatever clips are running outside of the editor. This is a global setting, not per clip.&#x20;
* _UNDO/REDO_ - for the clip editor itself. Also mapped to CTL/CMD Z and CTL/CMD SHIFT Z.
* _SAVE CLIP_ - saves your edits but warns you about overwriting
* _SAVE AS A COPY_ - saves your clip in the next available slot in the clip deck. This becomes the new position for your clip and all subsequent saves will be in this new place.&#x20;
* _EXIT EDITOR_ - closes the clip editor. If you have unsaved changes you will get a confirmation panel.&#x20;
