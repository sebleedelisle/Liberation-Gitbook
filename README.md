# Quick start guide

## Introduction&#x20;

Welcome to **Liberation** - the next generation of laser show software. Liberation is powerful and complex modern software; it's built on the fundamentals of usability and reliability to give you the freedom to express your creativity. It's fast, efficient and seamless, follow this quick start guide to get you up and running.&#x20;

### Screen layout

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

The menu is where you will find all file import / export options, and window opening and closing. You'll also find the option to authorise the computer with your subscription here.

#### Icon bar

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

&#x20;Common tasks can be found here, such as arming/disarming all the lasers, the global brightness, test pattern, and switching between the 3D, Canvas and Output views

### Views

There are 3 main views can can be shown in the top left of the screen; **3D**, **CANVAS** and **OUTPUT.** Switch between them using the icon bar buttons :&#x20;

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

The 3D view shows you what your lasers will look like and can be configured to match your own laser set up. Click and drag to rotate the camera, use the mouse wheel to track forward and back. You can find many other options in the "3D Visualiser settings" window.

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

The output view is used to configure zones and masks for each laser. Notice the massive number in the background so you can easily see which laser you are on!

#### What is a zone?

A zone is a space within a laser's output window that you can direct laser content into. And you can have more than one zone per laser. The simplest type of zone is a _beam_ zone, but there are also _canvas_ zones and _DMX_ zones. For this guide we'll mostly focus on beam zones, which are usually used to create atmospheric beam effects through the air.

#### The output view

This output view is a representation of the entire output of this laser, and where each zone sits within it. By default there is only one zone per laser but you can add as many zones as reasonably practical, and you will see them all in this view.

You can select the laser you want to edit using the numbered buttons in the bar at the top. Click on a numbered button, or cycle through each laser using the **TAB** key. Pressing the "+" button will add a new laser.

You can zoom in and out using the mouse scroll wheel, and click and drag anywhere there isn't a zone to move the view.

Click on a zone to select it and then adjust its corner points with the mouse. Use the ALT key while you are dragging a corner to make it non-uniform. Right-click on the zone to see more options, including changing the type of zone.

Along the left is a bar with a series of icon buttons, hover over any button to get a description of what it does. Buttons here let you add beam zones, canvas zones, and masks. There are also options to set a test pattern for this laser only, along with grid settings.

#### Canvas

The Canvas system is used mostly for graphics and architectural mapping. You can distribute complex images across multiple lasers, and perspective-correct each section.&#x20;

### APC40 MIDI controller

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Although it is possible to control Liberation using the mouse and keyboard, to get the most out of it I highly recommend using an APC40 MIDI control interface (Mk 2 is best but Mk 1 also works). I realise that the APC40 has now been discontinued so will be adding support for other controllers in the future, but for now try to get hold of one if you can.

### Clips and effects

#### Clipdeck overview

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

This grid is known as the _clipdeck_ and it is where all of the laser content is stored. It is designed to map directly to the 8 x 5 grid of buttons on your APC40.

**Navigating the clipdeck.**

You can scroll the clipdeck view using :

* Left and right cursor keys. Add CMD/CTL to scroll one full page at a time.
* Trackpad : Swipe&#x20;
* Mouse : if your mouse has a sideways scroll you can use that while hovered over the clip deck
* APC40 scroll knob or Device left/right buttons.

To help you get your bearings, at the top of the clipdeck is a small grid that represents the entire clipdeck.

#### Starting and stopping clips

Press a clip button (either with the mouse or with the APC40) to start a clip. Press it again to stop it. When you start a clip, all other clips of the same colour will automatically stop unless you hold _shift_.

Some clips will be in _Flash mode_ (by default, the red ones), in which case they will stop as soon as you release the clip button.

#### Selecting zones for the clip

Underneath the clip buttons, you'll see the zone buttons, beam zones 1 to 8 by default. The zone buttons light up to indicate which zones are assigned to the currently selected clip.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Two rows below the zone buttons, you'll see the X/Y flip buttons, toggle these to flip the clip  horizontally and vertically.

Note that these zone allocations and X/Y flip settings are connected to the clip itself; they are retained next time you run that clip. They are not a global setting.

Right click on a clip to edit more settings for the clip.

### Effects

The effects system in Liberation is a powerful and versatile way of changing the clips in real-time. The default effects buttons 1-8 are under the zone buttons.&#x20;

#### Applying an effect

Press an effect button to toggle the effect, or even better, using the APC40 sliders 1-8 to fade effects in and out gradually. &#x20;

#### Effect parameters

Use the rotary controllers 1-8\* to adjust the _parameter_ for each effect. (Or you can right-click with the mouse to adjust the level and parameter). The parameter change does differnet things dependent on how the effect is set up. See the list below for the default effects. &#x20;

_\*Rotary controllers 1-8 are along the top of an APC40 Mk2 and on the top right on the Mk1._&#x20;

#### The default effects

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** : \
   Applies a chaotic movement to the clip output.  The parameter changes the amount of chaos.&#x20;
2. **Sine wave** : \
   Warps all the content across a moving sine wave. The parameter adjusts the wavelength
3. **Rotation** : \
   Spins everything around, the paramete adjusts the spin speed.
4. **Horizontal flip** : \
   Squishes and stretches everything horizontally. The parameter adjusts the speed.&#x20;
5. **Scale** : \
   Repeatedly scales everything from full to zero. The parameter adjusts the speed.&#x20;
6. **Hue** : \
   Changes the hue of everything, but doesn't change the saturation (ie anything white stays white). The parameter sets the hue.&#x20;
7. **Saturation and hue** :  \
   Changes the hue of everything and also fully saturates the colour (ie whites change to the colour). The parameter sets the hue.&#x20;
8. **Flash** : \
   Repeatedly changes the brightness of everything from full to zero. The parameter sets the speed.&#x20;

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

There are a further 16 colour effects along the bottom row to apply pre-set hue and saturation.

Note that these are the default effects but they can be edited to do almost whatever you want!&#x20;

#### What is the "currently selected clip"?

When you start a clip, it lights up to show that it is active. It also has a white outline around it which indicates that this is the currently _selected_ clip. Whenever you toggle zone buttons or adjust the clip settings, these are applied to the _currently selected clip._

### Clip settings panel

Use the _Clip Settings_ panel to edit scaling, X/Y position, and access the powerful zone delay system.

### Global settings panel

Find the _Global Settings_ panel to adjust global output settings that affect all output across all zones.

### Timing

Almost all laser displays have some kind of musical soundtrack, so the timing system in Liberation is based around a tempo in beats per minute. In the _Tempo Panel_ you can see a representation of the time; each square represents a beat and you can see them flash in time.&#x20;



<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

There are multiple synchronisation options, including MIDI clock and Ableton Link. If you know the tempo of the music you can manually adjust it using the on-screen slider or the APC40 Tempo knob, but you can also keep in time with the music using the _Tap Tempo_ system_._

#### Tap Tempo

_Tap Tempo_ is a term commonly used in music apps, and it lets you tap in time with the beat to set the tempo while the music is playing. You can use the button on screen, although it's recommended to use the _T_ key or the _Tap Tempo_ button on the APC40 (or even a foot switch if you prefer).&#x20;

Press the _R_ key or the _Metronome_ button (APC40) to reset the tempo to the beginning of the bar.&#x20;

Press the _Y_ key or turn the _Tempo_ knob(APC40) to round the tempo to a whole number. This can be useful for electronic music which tends to have a round number of beats per minute.&#x20;

### Laser overview panel

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

The _Laser overview panel_ gives you a quick look into the status of your currently running lasers. The green square on the right shows you that the laser controller is happy. If it goes orange, you have occasional drop-outs, and if it's red it's been disconnected.&#x20;

The graph in the middle is a history of frame lengths, and the number on the right is the current frame rate. The more complicated the content, the slower the frame rate will be (ie more flickery).&#x20;

Click on the _Assign Laser Controllers_ button to open the _Controller Assignment_ panel. (This panel can also be accessed via _Window->Controller Assignment_ in the menu bar).&#x20;

#### Connecting to lasers - Controller Assignment panel

You can choose which laser outputs go to which laser controllers here. Drag and drop controllers from the list on the right into slots on the left. You can rename your controllers to match which laser they are paired with (use the pen icon button).&#x20;

For even faster assignment you can double click on a controller on the right to assign it to the next open slot on the left (trust me, when you have 50 lasers this is very helpful!)

#### Laser Settings panel

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

This panel shows you the settings for the _currently selected laser_ (represented by the number at the top). Change which laser is currently selected using the _tab_ key, hitting a number key, clicking a laser number in the _Laser Overview_ panel or in the _output view._

* **Number button** arm and disarm the laser.&#x20;
* **Brightness** adjust laser brightness independent of the other lasers (and it's combined with the _global brightness_ setting - ie, if they're both at 50%, you're laser will be at 25%).&#x20;
* **Test Pattern** turns on a test pattern for this laser only (overrides the global test pattern setting)
* **Orientation -** corrects for lasers rigged sideways or upside-down.&#x20;
* **Flip Horizontal and Flip Vertical** reverses the output of the laser. Useful for output correction on inconsistently wired lasers.&#x20;
* **Copy Laser Settings** opens a panel that lets you copy various settings from this laser to others.&#x20;

#### Scanner Settings

Unlike older systems, Liberation laser content is converted to a point stream as it is sent to the laser and there are many adjustments you can make as to how that point stream is calculated. Full details of this will be covered elsewhere in the manual, but for now, stick with the default scanner preset as it should work with most lasers.&#x20;

* **Speed** is the scanner speed, ie how fast the laser moves around to draw shapes. This is equivalent to adjusting the point rate on traditional laser software but on liberation you can change how fast the laser moves _independent of the point rate._ You shouldn't need to adjust this.&#x20;
* **Colour shift** (sometimes known as _blank shift_) The scanners move the laser around really fast but usually the change of brightness and colour is out of synch with the movement. This shows up as little flickering "tails" of light on the edge of beams and lines. Use this adjustment to get the movement and colour in synch with each other. &#x20;



### Zoning

#### Test patterns

[Jump to the start!](https://github.com/sebleedelisle/LiberationLaser/wiki/Quick-Start#hello-world)
