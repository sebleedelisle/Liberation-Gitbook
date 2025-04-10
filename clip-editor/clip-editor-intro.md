# 🟧 Introduction to the Clip Editor

The clip editor is the heart of Liberation and such a versatile way to create laser content; it's easy to make simple things and yet flexible enough to make some incredibly sophisticated and complex effects.&#x20;

{% hint style="info" %}
The node based editor was the first part of Liberation that was made! It was a quick demo born from a conversation with Rob Stanley at a UK laser meet up in 2018 about what an "object-oriented" laser content designer would look like.

It seems simple but was quite a challenge to build, but early in 2019  I had a working demo that proved the concept. And it started this whole journey!
{% endhint %}

It's a node based visual editor (or [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) that will be familiar to anyone who has used TouchDesigner, MaxMSP or VVVV. Although it's somewhat simpler version as it's been designed specifically for vector graphics.&#x20;

You can edit a clip by right clicking on the clip button and selecting _EDIT CLIP_. Or right click on an empty clip button and select _CREATE AND EDIT CLIP_. This will open the Clip Editor!

You typically start with one or more [creator nodes](creator-nodes.md), and connect [operators](operator-nodes/) from left to right that process the content. Each of these nodes has an array of sockets available along the bottom and each of these represent a setting within the node, such as brightness, position, scale, rotation etc.&#x20;

[Oscillator nodes](oscillators/) can be connected to these sockets from below and used to animate these settings.&#x20;

While you're editing you'll see a preview of the content in a panel on the right, and if you click on a node, you'll see a second preview underneath that shows you the content as it is at the node itself. &#x20;

You can also see what the clip looks like in the 3D visualiser; while you're editing you can use the zone buttons to allocate the clip to the zones you want (If _Preview to lasers_ is enabled, see [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel "mention") below)

### Clip editor panel

Preview to lasers&#x20;
