# 🟩 Stylisation nodes

## <img src="../../.gitbook/assets/image (2).png" alt="" data-size="line">  Randomise

Creates scattered copies of the incoming elements using a coherent noise field. In other words, it copies and moves your shapes and dots around in a controlled, “noisy” way. Instead of everything sitting neatly in one place, you get multiple versions that shift and spread out, like particles moving in a flow.

* **count** – number of copies per incoming element (1–20). With 1, you get a single jittered version of each element. Higher values create multiple scattered copies.
* **noise offset** – cycles through the noise field (0–100%). It loops seamlessly, so animating this with an Oscillator Node gives smooth, continuous motion of all copies together.
* **noise jitter** – controls the texture scale of the noise. Lower values give broad, smooth variation. Higher values give tighter, more erratic placement. This changes the pattern, not the strength.
* **change between points** – controls how different each copy is from the previous one. Low values keep copies clustered and similar. High values spread them out with greater variation.
* **face direction** – rotates each copy so it faces the direction of travel in the noise field, producing arrows/particles that align with the flow.
* **amount** – overall strength of the effect (0–100%). Scales both the displacement and the rotation from Face direction.

{% hint style="info" %}
The randomise node is at the heart of the Randomise effect!&#x20;
{% endhint %}

## <img src="../../.gitbook/assets/image (2).png" alt="" data-size="line">  Trails

Creates echoes of your content, leaving fading or scaling copies behind the original as it moves.

* **change render profile for trail** – if on, all trail copies use the selected **render profile**. _See_ [render-profile.md](../fundamentals/render-profile.md "mention").&#x20;
* **render profile** – the profile to use for trail copies when the switch above is on. Commonly used when the main content is set to **DETAIL** but the echoes are rendered as **FAST**, which gives you clear detail on the main shapes while rendering the trails more efficiently.
* **delay** – sets the spacing between trail copies in musical time, measured in **1/64-note steps**.\
  For reference:
  * 16 = 1/16 bar (sixteenth note)
  * 32 = 1/8 bar (eighth note)
  * 64 = 1/4 bar (quarter note)
  * 128 = 1/2 bar (half note)
  * 256 = 1 bar
* **trail size** – how many trail copies to draw behind the live content.
* **freeze trails** – turns smoothly flowing trails into a sequence of frozen snapshots. Useful for creating staccato, beat-synced trail effects.
* **brightness start / brightness end** – applies brightness across the trail from the freshest copy (**start**) to the oldest copy (**end**). Typically set **brightness start** at 100% and **brightness end** to 0% and the echoes will fade out.
* **scale start / scale end** – applies scaling across the trail from the freshest copy (start) to the oldest copy (end). For trails that shrink to nothing set **scale start** to 100% and **scale end** to 0%.&#x20;

## <img src="../../.gitbook/assets/image (2).png" alt="" data-size="line">  Shimmer

Adds a twinkling brightness variation to your content, ranging from gentle sparkle to intense strobing.

* **speed** – how quickly the shimmer changes over time. Higher values flicker faster; 0 pauses the effect.
* **separation** – how different neighbouring points/elements are from each other.
  * 0: everything shimmers together.
  * \>0: nearby points get progressively different phases, so the shimmer varies across the shape.
  * <0: same as above, but the phase progression runs the opposite way.
* **threshold** – instead of fading smoothly, points now flash fully on or off depending on their brightness. Brighter elements light up more frequently, but note that elements at 100% brightness are always on, while elements at 0% brightness are always off. Useful for crisp glitter or starlight effects.

{% hint style="info" %}
Turning on **threshold** is one of those great hidden features that can really bring your particles or content to life. Instead of fading, points are rapidly switched on and off based on their brightness. Because fewer points are being drawn at any given time, the result is brighter output and smoother animation.

But bear in mind that if your content is already at 100% brightness, it won't do anything!&#x20;
{% endhint %}

* **use whole shape** – applies one shimmer value uniformly to the entire shape. When off, the node subdivides shapes so different parts can twinkle independently for a speckled look.



## <img src="../../.gitbook/assets/image (2).png" alt="" data-size="line">  Particles

This is an experimental effect that spawns and animates particles based on your content. Any point-based elements going in are treated as emitter positions. Because particle paths are pre-calculated, if your input content changes you may need to refresh/recalculate to update the particles (just change any of the settings)

**General**

* **keep original** – If on, the original content is kept and particles are added on top. Useful when you want the emitter points to remain visible.
* **number of particles** – how many particles are created per emission. Higher values make denser effects, lower values are more minimal.
* **emission period** – the span of the loop (in bars) over which particles are emitted. At 100% they are spread evenly across the loop; smaller values bunch them together for bursts.
* **loop length** – how long the particle loop lasts, measured in musical bars.
* **loop count** – how many times the loop repeats before resetting. If set to 1, the particles will always follow the exact same simulation each time, making it perfectly repeatable. Higher values introduce more variation before the cycle resets.
* **delay** – shifts the start time of emission by a number of 1/64th notes, for timing effects.

**Motion**

* **speed** – how fast the particles move away from the emitter.
* **speed variation** – adds randomness so particles don’t all move at the same rate. Creates a more natural spread.
* **direction** – sets the base direction particles are fired in, defined by **x, y, z angles**. These angles rotate the firing vector in 3D space, so you can aim the particles straight up, sideways, or at any diagonal. Combine with **spread** for wider cones or more chaotic bursts.

{% hint style="info" %}
**Euler angles**\
Liberation uses **Euler angles** to describe orientation in 3D space. These are simply rotations around the three main axes:

* **X** – tilt forward/back (like nodding your head)
* **Y** – turn left/right (like shaking your head “no”)
* **Z** – roll clockwise/counter-clockwise (like tilting your head sideways)

By adjusting these three values, you can point particles in any direction.
{% endhint %}

* **direction variation** – adds random spread around that direction. Useful for creating cones, sprays or explosions.
* **drag** – slows particles down over time. Higher values make them feel heavier and more sluggish.
* **gravity** – pulls particles down (positive) or pushes them up (negative).
* **gravity variation** – adds variation to gravity per particle, making motion more chaotic.

**Life**

* **life duration** – how long particles exist (measured in 1/64th note units). With shorter values particles vanish rapidly, while with longer values they remain visible for an extended time.
* **life variation** – adds randomness to particle lifetime so they don’t all vanish at once.
* **start delay / start delay variation** – delays when each particle becomes visible (in 1/64-note steps). The particle is already spawned and moving during this period, but its brightness is held at 0, so it stays invisible until the delay elapses. It's useful if you want delayed firework "sparkles" to appear.&#x20;

**Colour & brightness**

* **hue start** – initial colour of particles.
* **hue variation** – adds randomness so particles don’t all start with the same colour.
* **hue change** – shifts hue across the particle’s lifetime, creating colour-changing trails.
* **brightness start / brightness end** – applies brightness across the life of the particle. Typically set brightness start high and brightness end low so they fade out naturally.
* **brightness variation** – randomises starting brightness for a more dynamic look.
* **saturation start / saturation end** – sets how vivid the colour is at the start and end.
* **saturation variation** – randomises saturation for variation between particles.

**Simulation**

* **time adjustment** – speeds up or slows down the entire particle simulation. Useful for syncing to different tempos or exaggerating motion.
