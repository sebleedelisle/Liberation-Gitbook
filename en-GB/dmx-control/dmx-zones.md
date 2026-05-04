---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# 🟩 DMX zones

DMX zones are Liberation output zones that send Art-Net/DMX instead of laser points. They appear alongside beam and canvas zones, so clips can be assigned to them in the same zone selector workflow.

Open **DMX Zones** from the menu, or use the DMX section in the Laser overview, to manage them.

* **ADD DMX ZONE** - creates a new DMX zone.
* **ARM** - enables DMX output for that zone. An unarmed DMX zone clears its mapped channels to zero.
* **Node** - selects the Art-Net node number.
* **Universe** - selects the Art-Net universe. The displayed value is 1-based, so Universe 1 is the first universe.
* **Address** - sets the fixture's start address. The displayed value is also 1-based.
* **Preset** - chooses the DMX preset that maps clip content to DMX channels.
* **Edit DMX zone settings** (pencil icon) - opens zone settings such as manual zone forwarding and fixture orientation.
* **Edit DMX profile/channel mapping** (sliders icon) - opens the DMX preset/channel editor.
* **Delete** - removes the DMX zone.

### Arm limits

The number of DMX zones that can be armed at the same time depends on your licence tier. If your tier does not allow DMX output, or you have already armed the maximum number of DMX zones, the **ARM** button for additional zones is disabled and shows a no-entry icon when hovered.

Disarm another DMX zone, or use a licence tier with a higher DMX limit, before arming more zones.
