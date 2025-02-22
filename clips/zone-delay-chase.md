# 🟦 Zone delay / chase

We all agree that more lasers equals more fun but if they're all doing exactly the same thing you're missing out on creative possibilities.

The zone delay system is a simple yet effective method to introduce variety across zones and can significantly enhance the dynamism of your lasers. It can also be used to make a more traditional chase effect.&#x20;

#### How it works&#x20;

_Zone delay_ adds a delay to the timing of the clip across each zone, creating a kind of sweep across the zones.

It's really effective to introduce zone delay to an already running clip, use the relevant control on the APC40 to adjust the level and pattern. (See [apc40-reference.md](../reference/apc40-reference.md "mention")). Or you can use the _Clip Settings_ window.

Zone delay settings :&#x20;

* **Zone delay** - controls the amount of delay time applied to each zone, measured in 64th notes.&#x20;
* **Pattern** - choose the zone order&#x20;
  * Left to right
  * Right to left&#x20;
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
The pattern works on the zone numbers and assumes your zones are in order from left to right. Zone delay treats canvas zones and DMX zones as separate groups when it comes to calculating the patterns.&#x20;
{% endhint %}

* **Delay mode**
  1. No delay - use this in chase mode
  2. Delay - the default mode, delays the timing of each zone
  3. Delay with re-trigger - Resets the clip back to the start every time across the pattern. This is good with _Chase mode_.&#x20;
* **Chase mode** - with chase mode on, each zone is turned on and off like a traditional chase effect. Adjust the chase appearance using the _Fade in, Hold,_ and _Fade out_ settings. These settings are set as a proportion of the zone delay value, so a value of 1 would be the same time as specified in the _Zone delay_ value. It's a little hard to explain so my advice would be to try for yourself.&#x20;

{% hint style="info" %}
Zone delay is also applied to any active effects. For instance, a flashing effect will be delayed across the zones as well as the animation within the clip itself.&#x20;
{% endhint %}

When a clip has any kind of _Zone delay_ you will see a three-dot icon in the top right of the clip. These dots are animated to show you the style of _Zone delay_ for that clip. See [what-are-the-small-icons-on-the-clip-buttons.md](what-are-the-small-icons-on-the-clip-buttons.md "mention") for more details.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>The three dot symbol that indicate that a clip has a zone delay and its mode</p></figcaption></figure>

{% hint style="info" %}
Zone delay is a setting that belongs to each clip, it's not global; it's part of the creative design of a clip.&#x20;
{% endhint %}



