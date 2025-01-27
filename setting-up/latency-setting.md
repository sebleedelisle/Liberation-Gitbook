# ✅ Latency setting

In the bottom of the _Laser Overview_ window, you'll see a slider labelled _Latency(ms)._&#x20;

{% hint style="info" %}
The default latency setting of 150ms should be fine for most cases but if you are having network issues you may want to try to increase it.&#x20;
{% endhint %}

### The complicated explanation

In short, it's the maximum time between Liberation creating a frame, and the laser starting to output it. If you increase this value then you may notice a slight delay between Liberation and your laser output.&#x20;

The benefit of a longer frame latency is that Liberation can fill up the laser controllers' buffers with content as soon as possible; if there is congestion on the network the controller is less likely to run out of points.&#x20;

