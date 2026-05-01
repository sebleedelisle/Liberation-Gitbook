---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Fills, masks and depth sorting

### Strokes, fills and masks

You'll notice that some Creator nodes have a _Fill state_ option; you can draw them with a stroke (an outline) or as a mask (covering over stuff underneath) or both.

When you render a shape as a mask, it's as though it's filled in with black and anything underneath it will be covered up.

{% hint style="info" %}
Drawing a line (or _stroke_) with a laser is easy enough; you scan the laser from the beginning of the line to the end of the line. There's your line!

Filled shapes are harder though; If you want a shape filled with color you could manually cross hatch by drawing lines and filling in, but Liberation can't do that automatically (yet). And even if we did do that, you'd still see other lines underneath it showing through.

But what we can do is fill in shapes with _black_. Under the hood, Liberation is making all the calculations to remove content that are underneath the black-filled shape. And trust me, it's tricky!

But it works really well and gives the illusion of a black filled shape.
{% endhint %}

### Depth sorting

As some shapes can _cover_ other shapes, Liberation has to sort them by their depth. And by default, elements are depth sorted by their z position. If they are at the same z position they are sorted by their layer position which can be changed using the _MOVE TO FRONT_ and _MOVE TO BACK_ buttons inside each creator.
