# ✅ Sound input oscillator

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line">  Sound input&#x20;

Converts the sound input level to a property value.&#x20;

{% hint style="info" %}
The Sound input oscillator uses the default sound interface, but you can change it in the _App Settings_ window. Open the menu _Settings->App Settings._&#x20;

Under the _Sound Input_ settings, you can select which sound interface you would like to use, along with some other settings for adjusting the volume level.&#x20;
{% endhint %}

* **range min / range max** - the minimum and maximum values the waveform is mapped onto
* **channel** - If your sound interface has more than one input channel, you can select here which one you're picking up.

{% hint style="info" %}
It's a fun technique to get multiple sound feeds from the mixing desk, that way you can have different clips responding to different musical instruments.&#x20;
{% endhint %}

{% hint style="info" %}
You can only use one sound interface at a time across all _Sound Inputs (_&#x73;elected in the _App Settings_ window). If you want to use more than one interface for this, on MacOS you can [create an Aggregate Device](https://support.apple.com/en-gb/HT202000) to combine inputs into a single virtual sound source. (There are many apps on Windows that will do this too, but I haven't tried them).&#x20;
{% endhint %}

* **clamp min / clamp max** - use this to choose which range of levels you want to respond to. You shouldn't need to adjust this if the gate and limit settings (in the _App Settings_ window) are properly adjusted, but they can be used for some creative effects.&#x20;

{% hint style="info" %}
You'll see a little microphone icon on the clip button whenever it has a _Sound Input_ oscillator.

&#x20;<img src="../../.gitbook/assets/image (7).png" alt="" data-size="original">
{% endhint %}

