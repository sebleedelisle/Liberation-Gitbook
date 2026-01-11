# ✅ FAQ

## Hardware

#### **Does Liberation run on Windows?**

Yes - Liberation fully supports **Windows 10 and 11 (64-bit)**, with the exact same features as the Mac version. Every release ships simultaneously for both platforms.

#### **Does Liberation run on Mac**

Yes - Liberation fully supports **Mac (macOS 12 Monterey and later)**, with full feature parity to the Windows version. All updates are released together.

#### **What is the minimum spec machine required?**

It depends how many lasers you want to control. If you're only running a few lasers, you'll be fine with a low spec machine. Any Apple Silicon Mac runs really well, and should be able to control up to 100 lasers. If you're running complex shows with high stakes then we recommend the best machine you can afford.

#### **How many lasers can I control with Liberation?**

Liberation can run many lasers on one computer, it's been tested with over 100 laser controllers so the answer depends on :

* your computer CPU
* network speed
* your subscription type

#### **Which MIDI controllers can I use?**

Liberation has been designed and optimised around the popular APC40 Mk2 MIDI controller. It also works with the APC40 Mk1. See [live-control-with-the-apc40.md](midi-control/live-control-with-the-apc40.md "mention")

We are slowly adding more MIDI controllers as we go and currently also support the APC Mini Mk2 and the MIDI Fighter Twister.&#x20;

There is also the MIDI Send/Receive system that offers additional MIDI control. See [midi-send-receive.md](midi-control/midi-send-receive.md "mention")

See [midi-control](midi-control/ "mention")for more information.

#### **Can I use it with any MIDI controller?**&#x20;

We are currently working on a configurable MIDI system that will allow this in future.  In the meantime, some users have had success using a MIDI interpreter that can convert any MIDI messages for the MIDI Send/Receive system, but this is a fiddly and advanced process. Search the [forum](https://forum.liberationlaser.com) for advice on this set up but realistically the APC40 is the best option.&#x20;

## Laser controllers

#### **Which laser controllers are compatible with Liberation?**

* [Ether Dream (recommended)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (you may need to update your firmware)
* LaserCube USB (and LaserDock)
* LaserCube network protocol (with a wired connection)
* AVB as used by [LASollinger lasers](https://laseranimation.com/en/) (currently MacOS only in testing)

See [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention") for more information

#### **Why don't you support \[other brand of] laser controller?**

To encourage greater interoperability between software and hardware, Liberation will only support DACs that have a published communication protocol. I believe that this is the best way forward for the laser industry.

#### **How can I tell if my laser can be used with Liberation?**

If your laser has one of the following, you can use it with Liberation :

* An external **ILDA input** – a 25-pin D connector, used with a compatible external controller.
* An internally installed **Ether Dream**.
* Any **LaserCube** (works with both USB and Wi-Fi LaserCube).
* An **X-Laser unit with a built-in Mercury system** (In Ether Dream mode).
* A **LaserAnimation Sollinger projector with AVB built in** (MacOS only, requires AVB-compatible network devices, currently in testing).

See [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention") for more information

#### **Can I use Liberation with my LaserCube?**

Yes, Liberation works directly with any LaserCube. See [lasercube.md](hardware/lasercube.md "mention")

## Licenses

#### **What is the price of a license?**

See the [shop](https://liberationlaser.com/shop) page for the current prices.

#### **What are the limitations between the licensing tiers?**

See the [shop](https://liberationlaser.com/shop) page for the current license options.

Note that you can set up, preview and design shows with as many lasers as you want on **every** tier even the free one, and there are no other limitations at all apart from the number of lasers that you can _arm_. Every other Liberation feature is available to all.

#### **Can I upgrade to a new tier?**

You can upgrade to a higher tier at any time. You will get a partial refund for the remaining time on your current license, and your new plan will start immediately. See [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **Can I downgrade my license?**

You can downgrade at any time but the change will take effect at the end of your current license period. See [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **How do I authorise my computer with my license?**

Once you have purchased a license you can then authorise the computer within the Liberation software itself. You will see an _Authorise_ button on the _About_ screen that will prompt you to log in to the website. Follow the on-screen instructions to complete the authorisation process. See [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **How often do I need to connect my computer to the internet?**

Every time the license renews you will need to connect Liberation to the internet to update its internal license. For a monthly recurring payment, you will need to connect every month.

#### **What happens if I can’t connect my computer to the internet after renewal?**

Liberation will give you a grace period of 7 days after your license renews to connect to the internet and update its internal license. After that period Liberation will go back into _Free_ mode.

#### **What happens if my credit card expires?**

You will get an email notification from our payment provider, and you will need to update your payment system. Log in to the website and use the _Update payment details_ link on the subscriptions page.

#### **How do I cancel my recurring license?**

Log in to the website, open the _Your subscriptions_ page, select the subscription you want to cancel, then click the _Cancel Subscription_ link. You can continue to use Liberation for the remainder of the license period.

#### **How many computers can I install Liberation on?**

You can install Liberation on as many computers as you like. Licence authorisations are only required to enable laser / DMX output, and your licence tier determines how many computers can be authorised for output at once. See [how-licensing-works.md](installation/how-licensing-works.md "mention")

#### **How do I move my license from one computer to another?**

* Open Liberation on the computer you do not want to use any more
* Make sure you are connected to the internet and click the _De-authorise this computer_ button on the _About_ screen
* Now open Liberation on the new computer
* Click _Authorise this computer_ button on the _About_ screen.
* The website will open, log-in and follow the on-screen instructions to complete the authorisation

You can also remotely de-authorise a computer you no longer have access to (with some limitations). See [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **Can I deauthorise Liberation on a computer that has been lost or stolen?**

You can deauthorise the computer via the website. If the Liberation installation has not been online since your last renewal, this can be done immediately.

If not, the deauthorisation will take effect when the subscription renews or when the computer connects to the internet, whichever comes first. If you urgently need to re-authorise a new computer get in touch with support.

### Using Liberation

#### The default set up has 8 lasers - how do I change this?

See [setting-up-your-project.md](setting-up/setting-up-your-project.md "mention") and [adding-removing-lasers.md](setting-up/adding-removing-lasers.md "mention")

#### Can I copy zone settings from one laser to the others?

Yes! See [copy-zones-between-lasers.md](output-view/copy-zones-between-lasers.md "mention")

#### Can I type a number instead of using a slider?

Yes! CMD/CTRL click on the slider and you can enter the value using the keyboard.

#### **How do I sync Liberation to music?**

It has an intelligent "tap tempo" system that works as you would expect, but you can also use an external MIDI clock or Ableton Link. See [tempo-synchronisation.md](tempo-synchronisation.md "mention"). The timeline can be synced to incoming LTC/SMPTE timecode coming in via any audio interface. See [timecode.md](timecode.md "mention").

#### What settings do I need to adjust to get the best output from the laser?

The main setting is _Colour Shift,_ which compensates for the slight delay between the mirrors moving and the lasers changing brightness. If your laser dots/beams have little 'tails' then you'll need to adjust this. (See the photos on the [laser-settings](setting-up/laser-settings/ "mention") page for an example of 'tails')

You can also try changing the scanner speed, slower if your scanners are basic, or faster if they are good. But **use with caution as you can damage your scanners if you drive them too hard.**

There are also some preset scanner settings. The default option is conservative and fine for most laser beam requirements. But there are other presets for if you have better scanners, and there are presets that are tuned for graphics.

For more information see [laser-settings](setting-up/laser-settings/ "mention"), and for information on how to create your own presets see [scanner-presets.md](advanced/scanner-presets.md "mention") (advanced, in progress)

You can also correct the colour balance using the _Colour calibration_ settings. See [colour-calibration.md](advanced/colour-calibration.md "mention")(advanced technique)

#### What does the _Latency(ms)_ setting do?

This is the frame latency, or maximum amount of time between a frame being generated and subsequently sent to a laser. You shouldn't need to adjust it, but if you are having network issues you could try increasing it. See [latency-setting.md](setting-up/latency-setting.md "mention") for more details.

### Clips

#### How do I adjust zones and settings for a clip without running it?

ALT/OPTION click to make it the _currently selected clip_ but without activating it. See also [starting-stopping-clips.md](clips/starting-stopping-clips.md "mention")

#### How do I copy clips?

Click and drag while holding the ALT/OPTION key. See also [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### How do I delete clips?

Click and drag them off the clip deck. See also [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### How do I multi-select, delete, combine clip decks etc?

See [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### What do the little microphone symbol and other icons on the clip denote?

They are there to show you that a clip takes sound or MIDI input, and the 3 dots show you that there is a zone delay. See [what-are-the-small-icons-on-the-clip-buttons.md](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
