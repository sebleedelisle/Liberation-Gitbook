# 🟩 Path Modifiers

## <img src="broken-reference" alt="" data-size="line">  Dotter

This node replaces lines and shapes content with evenly spaced dots (existing dots are unchanged).

* **Colour** – the colour of the dots. Ignored if _Inherit Colour_ is enabled, see below. _See also_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – the distance between dots, measured in pixels. Smaller values = more dots, larger values = fewer.
* **Offset** – shifts the starting position of the dots as a percentage of the spacing. Can be animated (e.g. with a sawtooth Oscillator Node) to create "travelling" dot effects.
* **Keep Original** – if enabled, the original lines/shapes are retained and the dots are drawn on top.
* **Render Profile** – chooses the rendering quality. _See_ [render-profile.md](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – automatically adjusts spacing so the path length divides evenly.
* **Fade Out Ends** – gradually reduces the brightness of dots toward the start and end of the path. Useful when animating **Offset** with a sawtooth Oscillator Node, so dots fade smoothly in/out as they move to the end of the shape.

## <img src="broken-reference" alt="" data-size="line">  Trimmer

This node trims the visible length of lines and shapes, letting you reveal, hide, or animate them over time.

* **Offset** – controls where the visible part of the shape starts. Even with _Trim Size_ at 0%, animating Offset from 0% → 100% makes the shape draw in, become fully visible at 50%, then disappear again.
* **Trim Size** – sets how much of the shape is kept, as a percentage of its total length.
* **Loop** – treats the shape as a continuous loop, so the end connects back to the beginning rather than disappearing.
* **All Shapes** – combines all input shapes and trims them as if they were a single path. If off, each shape is trimmed individually.
* **Add Dot at Start / Add Dot at End** – adds a dot of the chosen colour at the trim points. (If no trim is applied, no dots are added.)
* **Colour** – the colour of the trim dots. _See also_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – chooses the render profile for the dots. _See_ [render-profile.md](../fundamentals/render-profile.md "mention")
