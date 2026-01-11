# ✅ Compatible lasers and controllers (DACs)

### Which lasers are compatible with Liberation?

If your laser has a standard ILDA input then you can use it with Liberation (along with a compatible laser controller such as the Ether Dream or Helios DAC - [see full list below](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>The Helios DAC - the cheapest option for home use</p></figcaption></figure>

You do not need an external controller or an ILDA input if :

* Your laser has Ether Dream installed inside, or;
* You have a LaserCube from Wicked Lasers
* You have a Laser Animation Sollinger laser with an AVB controller built-in (currently in testing on MacOS only)

{% hint style="info" %}
#### What is a laser controller?

A laser controller (or DAC) is a hardware device that can take the digital data from Liberation and convert it to the analog signals that are required to control the scanners and output of your laser. (Hence DAC: Digital to Analog Converter.)

The controller connects to your computer via USB or over a standard computer network; it will either be an external device, or installed inside the laser.

If it's external, you connect it to your laser via the ILDA connection. ILDA is an industry standard that uses an old school 25 pin 'D' connector. Get yourself an ILDA cable, plug one end into the controller, and the other into the laser.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>The ILDA output on an external Ether Dream</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>The rear panel of a laser showing the various connections, including the ILDA input</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>A standard ILDA cable</p></figcaption></figure>

### Which controller is best for me?

If you are a home user, or run small shows with 4 or fewer lasers that are close to the computer, then USB controllers like the **Helios DAC** are the **most affordable** option.

Network DACs like the **Ether Dream** are the **best option for professional** laserists who are happy to set up a network and want to run a large number of lasers; all of the large Liberation shows so far have been run on Ether Dreams.

If you have a **LaserCube** then you don't need a separate laser controller at all - Liberation is compatible with all LaserCubes. The earlier models connect with a USB cable, and the newer models connect over a network.

### Compatible laser controllers

#### Ether Dream (Network)

The [Ether Dream](https://ether-dream.com) has been around for over ten years and is currently at version 4 (although Liberation also works with Ether Dream version 1, 2, and 3). They are extremely reliable.

You connect to them over a standard network. They can be bought as standalone units, or even better, can be fitted inside lasers.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) is the best option for beginners and they are cheaper than Ether Dreams, but as they connect over USB, it's not recommended for long cable runs. Also you may have USB data and driver issues once you connect to more than 4 (especially on Windows).

But if you just want to run a couple of lasers at home, it's the cheapest and simplest option.

#### Mercury (Built-in to X-Laser units)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) is X-Laser’s powerful DMX laser control system, designed for lighting designers who want to run lasers directly from a traditional lighting console. With the latest firmware update, Mercury also includes **Ether Dream emulation**, which means it now works seamlessly with Liberation - as well as any other software that supports Ether Dream.

#### AVB (Built into Laser Animation Sollinger units)

**AVB** is an open network-based protocol for high-performance, low-latency audio and data streaming. Many LaserAnimation Sollinger projectors include AVB support directly in the hardware, which allows Liberation to connect to them over the network without the need for external DACs. AVB support in Liberation is currently **MacOS-only and in testing**, and it requires **compatible AVB-enabled network devices**. When set up correctly, it offers a simpler workflow, fewer external devices, and robust reliability for professional shows. I

#### Controllers that will be supported in the future :

* [IDN](http://www.ilda-digital.com) (an open network protocol from ILDA, can be implemented by any manufacturer)

### Cabling suggestions

For optimal performance, keep USB DACs near your computer and connect them to the lasers using longer ILDA cables. (Although watch out as ILDA cables can act as a grappling hook during de-rigging!)

If you're using Ether Dreams you can still keep them all together and connect to the lasers using long ILDA cables, or you can rig them close to the lasers, and use longer network cables.

The ideal set up is to have Ether Dreams installed directly inside your lasers (Rob at Stanwax Laser will do this for you in the UK)
