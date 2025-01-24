# 🟦 3D Visualiser

### Introduction

Liberation's 3D visualiser is an incredibly useful feature -  you can design and refine your shows without needing any lasers at all! It's proved an invaluable tool for me, especially when there are particularly complex setups with large numbers of lasers.&#x20;

### Navigating around the 3D space&#x20;

* Click and drag to rotate the view around the orbit point
* Mouse wheel to move backwards and forwards towards the orbit point
* Click and drag while keeping the shift key pressed to move the camera around laterally (strafe) left, right, up and down along the XY plane. &#x20;

<figure><img src="../.gitbook/assets/3D View Clear.png" alt="" width="375"><figcaption></figcaption></figure>

### Settings

Open the _3D Visualiser Settings_ window via the _Window_ menu.&#x20;

* **Brightness Adjustment** - changes how bright the lasers appear
* **Show laser numbers** - renders the relevant number above each laser
* &#x20;**Show zone names** - renders the relevant zone names below each laser

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption></figcaption></figure>

### Camera settings

These settings mostly relate to the virtual camera in 3D space. You can see a drop down with presets for these settings that you can save and reload.&#x20;

* **Camera distance -** The camera is always pointed at its _Orbit point_. The camera distance is how far away it is from this point. You can also adjust this setting using the mouse scroll wheel.&#x20;
* **FOV -** Field of view - determines how wide angle / zoomed in the camera is.&#x20;
* **Orbit position** - describes the current rotation around the orbit point. The first value is the rotation around the X axis (pitch) and the second value is the rotation around the Y axis (yaw).&#x20;
* **Orbit centre point** - the position of the orbit point in 3D space, x, y, z.&#x20;
* **Grid height** - the height of the grid from the "ground" (ie where y = 0).&#x20;

### Content settings

These settings determine where the lasers (and canvas) are placed within the 3D environment. You can see a drop down with presets for these settings that you can save and reload.&#x20;

#### Lasers

Each laser has its own group of settings that you can expand using the small white triangle.

* **3D Position** - the laser's x, y and z position.&#x20;
* **3D Orientation** - the laser's rotation around each of the x, y and z axes.&#x20;
* **Flip X / Flip Y** - flips the virtual output of the laser - NOTE that this shouldn't be necessary - it's better to use the laser flip / orientation settings to correct any inconsistencies with your hardware.&#x20;
* **Output Range horizontal / vertical** - relates to the max / min angle of your laser's scanners. 60º is standard but you can adjust this if your lasers are different.&#x20;

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="563"><figcaption></figcaption></figure>

#### Canvas

If you are using the canvas system, you can also choose to include the canvas image within the 3D view. Activate the checkbox to render the canvas within and use the position, orientation and scale settings to determine how it looks within your 3D view.&#x20;

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="563"><figcaption></figcaption></figure>



{% hint style="info" %}
Seeing "ghost" lasers? The 3D Visualiser is somewhat independent of the laser setup and it's possible to have more lasers within the visualiser than you do in Liberation. When you add a laser to your project, a new laser object inside the visualiser will also be added. But if you delete a laser, there will still remain a "ghost" laser object in the visualiser.&#x20;

To get rid of all the ghost lasers, click the _Remove extra 3D laser objects_ button (at the bottom of the 3D Visualiser settings window).&#x20;
{% endhint %}
