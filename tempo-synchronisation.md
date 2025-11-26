# 🟧 Tempo / synchronisation

Music synchronisation is a fundamental element of Liberation; once you have the tempo and beats matched up to the music, you can be sure that everything will be in sync. If you're lucky enough to get MIDI clock (or Ableton Link) then you don't have to worry about manual syncing at all. But if not don't worry - you can manually match up using the _Live_ tempo feature.&#x20;

If you have experience with music or lighting software then this process will be familiar to you. If not, it's worth spending some time familiarising yourself with the system and practicing at home before you get to a live show.&#x20;

## Tempo panel

The _Tempo_ panel will always be on screen and contains all the synchronisation settings. At the top you'll see the current bar/beat counter and a transport with play/pause and rewind/fastforward buttons.&#x20;

Below that you'll see the beat marker; four squares that "pulse" to the beat. This _beat marker_ is an extremely useful visualisation and you will constantly refer to it while using the _Live_ tempo system.

### Setting the tempo&#x20;

You have options for setting the tempo :&#x20;

* Click and drag on the _Tempo_ slider&#x20;
* Shift-click and drag on the _Tempo_ slider to change the tempo in 0.1 increments
* Double click on the _Tempo_ slider and manually type the number
* Use the _Tempo_ knob on the APC40 (Press shift for 0.1 increments)
* Tap Tempo

{% hint style="info" %}
Tempo is defined in "beats per minute" and the traditional default is usually 120.&#x20;
{% endhint %}

## Tap Tempo

Set the tempo automatically by clicking the _TAP_ button in time with the beat. Set the start of the bar with the _RESET_ button.&#x20;

{% hint style="info" %}
The Tap Tempo system is smart enough to know if you have taken a break from tapping for a while, or if you've missed a couple of beats. If you start tapping in double time, it will understand that you want to double the tempo, the same goes if you tap in half time.&#x20;

It's also smart enough to work out if there are two people both tapping tempo at the same time  (ie one on the keyboard and one on the APC40). Liberation will average out the double taps.&#x20;
{% endhint %}

#### Keyboard commands :&#x20;

T - tap tempo\
R - reset the bar\
Y - round the tempo to the nearest beat per minute.&#x20;

{% hint style="info" %}
As most music these days is created digitally it follows that the tempo is likely to be a rounded whole number. So if tapping a tempo seems to be close, use the Y key (or move the APC40 tempo knob one "tick") to round it to a whole number
{% endhint %}

#### APC40 controls :&#x20;

The APC40 has a dedicated _TAP TEMPO_ button or you can also use a connected footswitch to tap with your foot!&#x20;

Use the _TEMPO_ knob to adjust. Press _SHIFT_ while using the _TEMPO_ knob for fine adjustments.

Use the _METRONOME_ button to **reset the bar**. (Note that the _METRONOME_ button also lights up in time with the beat)

Turn the _TEMPO_ knob one "tick" right or left to **round the tempo** up or down to a whole BPM number.&#x20;

See also [apc40-reference.md](reference/apc40-reference.md "mention")

### Nudge tempo

If you're confident you are close enough to the actual tempo but you find that you're drifting out of time, use the _NUDGE_ buttons to correct.&#x20;

If the Liberation tempo is getting ahead of the music, press and hold _NUDGE -_ to temporarily slow down until it realigns.&#x20;

If the Liberation tempo is falling behind the music, press and hold _NUDGE +_ to temporarily speed up until it realigns.

{% hint style="info" %}
You can use either the on-screen NUDGE buttons or the dedicated buttons on the APC40.
{% endhint %}

### Half time / double time

Use the _÷2_ and _x2_ buttons to half and double the tempo permanently. Unlike the tempo multiplier this is a permanent change to the current tempo.&#x20;

## Tempo Multiplier&#x20;

The _Tempo Multiplier_ system lets you temporarily adjust the tempo before returning to what it was before.&#x20;

Toggle the _Tempo Multiplier_ by hitting the _TEMPO MULTIPLIER_ button or the _BANK_ button on the APC40. Adjust using the on screen slider or by using the APC40 A-B slider. Or use the _25%, 50%, 100% 200%_ preset buttons. &#x20;

## External tempo sources

### MIDI Clock

To sync to an external MIDI clock signal, select the _MIDI CLOCK_ radio button and choose the MIDI device from the drop down menu. Note the coloured status light next to the dropdown menus :&#x20;

* Green -  receiving a MIDI clock signal&#x20;
* Orange - can connect to the MIDI device but there is no clock signed currently
* Red - cannot connect to the MIDI device

{% hint style="info" %}
MIDI Clock broadcasts a series of frames, (24 per quarter note) but there is no position data within the messages. This means that it's helpful for keeping in time but you may still need to reset the bar.&#x20;

The Liberation MIDI Clock tempo source also responds to **MIDI Machine Control (MMC)** messages, so if your clock source transmits these you will not need to manually reset the bar.&#x20;
{% endhint %}

### Ableton Link&#x20;

From the Ableton website :&#x20;

> Link is a technology developed by Ableton that keeps Link-enabled applications in time over a local network. Link synchronizes musical beat, tempo, and phase across multiple applications running on one or more devices. Applications on devices connected to a local network discover each other automatically and form a musical session in which each participant can perform independently. Anyone can start or stop while still staying in time. Anyone can change the tempo, the others will follow. Anyone can join or leave without disrupting the session.

It's designed for multiple performers playing music together over a network, and any one of them can change the tempo. The Liberation implementation is limited so you can't control the tempo (which is  desirable - can you imagine if you changed the performer's tempo mid set?).

There is no configuration required,  if there is another Ableton link device on the network Liberation will sync to it.&#x20;

### Timeline

Each timeline has its own tempo, which can be a fixed value or a _Tempo Map_. The _Tempo Map_ allows you to adjust the tempo at specific times within the timeline.

The timeline tempo will be used when _TIMELINE_ is selected as the tempo source.&#x20;

{% hint style="info" %}
You can run a timeline along with _any_ of the tempo sources! So if you have a live band that doesn't play to a click, you can start the timeline manually and keep it in sync using the _LIVE_ tempo source. Or if you have a MIDI clock signal, you can use that!&#x20;
{% endhint %}
