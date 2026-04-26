# ✅ Latency setting

In the _Settings_ panel (_Liberation->Settings_ or CMD/CTRL ,) you'll see a slider labelled _Latency(ms)._ (In older versions of Liberation this was in the Laser Overview panel)

{% hint style="info" %}
The default latency setting of 150ms should be fine for most cases but if you are having network issues you may want to try to increase it.
{% endhint %}

### The complicated explanation

This "frame latency" setting is the maximum time between Liberation creating a frame, and the laser starting to output it. If you increase this value then you may notice a slight delay between Liberation and your laser output.

The benefit of a longer frame latency is that Liberation can fill up the laser controllers' buffers with content as soon as possible; if there is congestion on the network the controller is less likely to run out of points.

This usually only applies to network DACs.&#x20;

