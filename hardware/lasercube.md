# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube promotional image courtesy of Wicked Lasers</p></figcaption></figure>

The [LaserCube](https://www.laseros.com/lasercube/) by Wicked Lasers is an extremely compact battery powered laser unit available in a number of different power configurations. They're popular with hobbyists because of the easy to use smart phone app, but recent models are capable enough to be used on professional shows.&#x20;

The phone app (called LaserOS, also available for desktop) is a free download and is great fun to play with and is good enough for most users. But if you're running bigger shows with multiple lasers, you need something more specialised and powerful - and that's where Liberation comes in.&#x20;

### Connecting to a LaserCube

Early LaserCubes are controlled via USB, but the current models all have a built-in network controller. These network controlled cubes are known as "LaserCube Wifi". Liberation supports both types of LaserCube\* whether connected via USB or on a network.

\*(LaserCube network protocol support was introduced in version 0.7.3)

### USB LaserCube

Connect your LaserCube to your computer with a micro USB cable, then look for it in the _Controller Assignment_ window (See [controller-assignment.md](../setting-up/controller-assignment.md "mention")). If it doesn't show up automatically, hit the _REFRESH_ button.&#x20;

### Network LaserCube "Wifi"

{% hint style="danger" %}
Although the "Wifi" cubes are designed to be operated over a wireless network, this is not recommended and you will likely get dropouts and glitches.  Instead use the RJ45 socket to connect your LaserCube to a wired network, just like you would with Ether Dreams.
{% endhint %}

Connect your LaserCube to your wired network.&#x20;

Put your LaserCube into "LAN Client" mode and make sure there is a router on your network. The LaserCube will get an IP address from your router, and it should then show up in the _Controller Assignment_ window.  (See [controller-assignment.md](../setting-up/controller-assignment.md "mention")).&#x20;

{% hint style="info" %}
It is possible to set up a network without a router and give all your devices fixed IP addresses, and this is very common in the events industry. Personally I prefer to add a router on the network and recommend this option to anyone less experienced with networking.&#x20;

The router dynamically allocates an IP address to everything, I find it to be simpler and less error prone.
{% endhint %}

{% hint style="danger" %}
Unlike the Ether Dream, _**LaserCubes DO NOT BLANK THE LASER**_ if they encounter a buffer under-run, lost packet or other corrupt / incorrect data.

Instead, they just carry on from where they left off, and in some cases this can cause a live beam to cross areas that are not within zones, and even worse, will cut across software masks.

I am talking to the designers/coders of LaserCube and I’m hoping this is something that they address in future with a firmware update but in the meantime, you must ensure that you physically mask anywhere that you don’t want the laser to go.

To be fair, you should probably do this anyway, but I myself use software masks for protecting cameras and projectors. So just be aware that it’s more dangerous to do this using the LaserCube network protocol than it is with the Ether Dream (which goes into a safety stop mode as soon as there is any error or missing data).

Also, I've said it already but **use a wired connection to your LaserCube**. Wifi isn’t gonna cut it and will make this issue even worse.
{% endhint %}



