# ✅ Laser output settings window

Open the _Laser output_ settings window with the menu _Window->Laser Output Settings._&#x20;

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Ouput.png" alt="" width="326"><figcaption></figcaption></figure>

This will show you the settings for the currently selected laser which you can change :&#x20;

* via its number button in the _Laser overview_ window&#x20;
* with a number key on your keyboard, keys 1 to 0 open lasers 1 - 10
* with the _TAB_ key to cycle through the lasers. (_SHIFT + TAB_ goes backwards).&#x20;

At the top of this window you'll see :&#x20;

* a number button - click on this to arm/disarm this laser. It is red when the laser is armed.&#x20;
* a _Brightness_ slider for this laser only. Note that this is combined with the global brightness.
* _Test Pattern_ toggle and pattern selector. This lets you choose a specific test pattern for this laser only. (These controls are mirrored in the Output view toolbar).&#x20;

### Output orientation / mirroring correction

The next elements are for correcting the set up of your laser so that it behaves consistently in Liberation.&#x20;

* **Flip horizontal / vertical** - these options allow you to correct your laser's output

{% hint style="info" %}
You should not need to change the horizontal / vertical flip settings unless your laser has been wired incorrectly or it has X/Y flip buttons on the back that are not set properly. If you want output to be flipped for a particular clip this can be done on the clip itself.&#x20;
{% endhint %}

* **Orientation** - if your laser has been rigged on its side or upside down, you can correct the rotation with this setting .
* **Fine position adjustments** - can be used to correct very minor shifting/rotation. Designed to correct drift/settling if a laser has been left overnight or for long periods.&#x20;

{% hint style="info" %}
Note that the orientation / mirroring corrections do not change anything in the 3D Visualiser, they should be used to correct the output of the actual laser to match what is in the 3D Visualiser!&#x20;
{% endhint %}

### Copy laser settings

See [#copy-laser-settings](./#copy-laser-settings "mention").

### Scanner settings

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

The speed setting determines how fast the scanners move.

{% hint style="danger" %}
Although the default settings are quite conservative, you can still damage your scanners if you drive them too fast. Use caution, particularly when increasing the speed.&#x20;
{% endhint %}

{% hint style="info" %}
This speed setting doesn't change the point rate, instead it adjusts how spread out those points are. For more information see [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Colour shift**

The beam changes colour and turns on and off as the scanners move it around and these two things aren't usually perfectly in sync with each other. Adjust this setting to get them back in line.&#x20;

{% hint style="info" %}
This is sometimes known as _blank shift_ but I personally prefer the term _colour shift_ - it's a little more accurate as it adjusts the timing of all the colour changes, not just when the laser is turned off.&#x20;
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser "tails" - Colour shift not properly set</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>No laser "tails"! Colour shift good!</p></figcaption></figure></div>

If you see little "tails" on your laser output, it's likely because the colour shift needs adjusting. If the tails still appear no matter what, you are likely driving your scanners/laser drivers faster than they can handle. Try slowing the scanner speed down.&#x20;

#### Scanner presets

Use this to choose a pre-designed scanner setting. The default option is usually fine so you shouldn't need to change this setting unless you have particularly bad (or good) scanners. If you want to dig deeper, see [scanner-presets-and-render-profiles.md](../../advanced/scanner-presets-and-render-profiles.md "mention")

#### Colour calibration

You can use this system to correct the brightness curve and white balance of your laser. See [colour-calibration.md](../../advanced/colour-calibration.md "mention")

#### Advanced settings

You shouldn't need to mess with these but if you're curious, see [advanced-laser-settings.md](../../advanced/advanced-laser-settings.md "mention")

