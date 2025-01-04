# 🟦 Zones

The main type of zone you will use for most of your projects is the _Beam zone_. This is a zone designed for atmospheric beam effects through the air. The other type of zone is a _Canvas zone_ (See [graphics-and-the-canvas-system](../../graphics-and-the-canvas-system/ "mention")).&#x20;

{% hint style="danger" %}
**WARNING - Use extreme caution when moving zones while the laser is running** and turn the brightness down as low as it can go. See [setting-up-lasers.md](../setting-up-lasers.md "mention") for a comprehensive guide for activating and zoning lasers safely
{% endhint %}

You can click and drag the zones around with the mouse. Turn on a test pattern to see where that zone goes.&#x20;

{% hint style="info" %}
Use the arrow keys to **nudge** the currently selected zone/point. Press the SHIFT key to nudge in larger steps.&#x20;
{% endhint %}

### Zone shape types

There are 3 zone shape types :&#x20;

* **Quad** - the default rectangle zone shape which can be uniform (axis aligned) or distorted. Best for larger rectangular zones or canvas zones that require perspective correction. &#x20;
* **Line/Curve** - A zone defined by 2 or more points and a thickness. Ideal for thin zones or for terminating on balconies, bridges or other curved shapes. &#x20;
* **Segmented** - A zone that can be subdivided into smaller quads. Ideal for architectural mapping.&#x20;

Right click on any zone to open up its settings. From this right click menu you can :

* Rename the zone (this can be helpful to identify it in the clip deck, especially if you have a lot of zones!)
* Enable/disable the zone&#x20;
* Lock its position&#x20;
* Change its shape type
* Reset it to the default position
* Access settings specific to the shape type
* Delete it&#x20;
* Add an _Alt Zone_ (See [alt-zone-system.md](alt-zone-system.md "mention"))

{% hint style="danger" %}
**WARNING -** be very careful when changing the zone type while the laser is active. The zone will return to the last position / size for that shape so the output could change suddenly. It's best to turn the laser off before changing the zone type. &#x20;
{% endhint %}

### Quad zone shape

You can move each corner of the quad with the mouse. ALT/OPTION click a corner to move it independently from the others and distort the quad. Once the quad is distorted, all the corners can move freely.&#x20;

You can remove the distortion and return it to an axis-aligned rectangle using the _REMOVE DISTORTION_ button in the right click menu.&#x20;

#### Perspective correction

This option can be set using the toggle button in the right click menu and it determines the distortion method. It's best to keep this turned off for beams but If this zone is projecting graphics on to a flat plane, turn it on and the output will be perspective corrected.&#x20;

{% hint style="info" %}
If _Perspective correction_ is turned off, content is distorted using _bi-linear interpolation_. In other words, content is spaced evenly across the quad. That's why it's best for beams.

With perspective correction turned on, content is distorted using perspective warping which adjusts for foreshortening. So if you're projecting graphics onto a wall at an oblique angle, you can use this to undistort the output and fix the projection distortion.&#x20;
{% endhint %}

### Line / Curve zone shape

The Line / Curve zone shape has become my go-to option in recent shows, and it could be argued that this should be the default for beam zones.&#x20;

More often than not, my zones have to be thin to fit into awkward thin spaces at venues or between windows on buildings, and I found that it could be super fiddly to adjust four corners of a quad when they're so close together. And so the Line / Curve zone was born!&#x20;

For straight lines, all you need is two points, and then adjust the _Zone thickness_ in the right click menu. It's the fastest way to create simple zones.&#x20;

ALT/OPTION click on the line to create additional points. These points are automatically smoothed to create a flowing shape, and you can adjust the _Smooth level_ to iron out any kinks.&#x20;

ALT/OPTION click on a point to delete it.&#x20;

Or if you're experienced with vector graphics apps (Inkscape, Illustrator etc) you can use the _Manually adjust bezier curves_ option to give yourself fine ajdustment of all the control points.&#x20;

### Segmented zone shape

This subdivided zone lets you make extremely detailed corrections and is useful for when you are mapping onto complex shapes. You can add or remove subdivisions using the + and - buttons in the right click menu.&#x20;

### How to edit a zone that is entirely covered by another zone

Right click on the zone on top, and click the padlock button to lock it. You should now be able to edit and adjust the zone underneath.&#x20;



\


{% hint style="info" %}
Once you add a Beam zone to your output it will be available to add to a clip in the clip deck.&#x20;
{% endhint %}
