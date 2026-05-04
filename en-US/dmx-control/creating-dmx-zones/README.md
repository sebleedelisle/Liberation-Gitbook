---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Creating DMX zones

1. Connect your Art-Net node and set it up in [◼️ Connecting to an Art-Net node](../connecting-to-an-artnet-node.md "mention").
2. Open **DMX Zones** and click **ADD DMX ZONE**.
3. Set the zone's **Node**, **Universe** and **Address** to match the fixture.
4. Choose a **Preset** for the fixture. The preset defines which DMX channels receive fixed values, content on/off values, RGB color, X/Y position, brightness, or explicit DMX Value inputs.
5. Click **Edit DMX profile/channel mapping** (sliders icon) to edit the channel mapping. The default preset starts with a content on/off channel and RGB color channels.
6. Assign clips to the DMX zone the same way you assign them to beam or canvas zones.
7. Press **ARM** when you are ready for the zone to output DMX.

{% hint style="warning" %}
Only armed DMX zones send live values. Unarmed DMX zones clear their mapped channels to zero, which is safer when setting up fixtures.
{% endhint %}

DMX output is also limited by your license tier. If the **ARM** button is disabled, check whether your tier includes DMX output or whether the maximum number of armed DMX zones has already been reached.
