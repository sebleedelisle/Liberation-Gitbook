# 🟦 Fills, masks and depth sorting

### Strokes, fills and masks

You'll notice that some Creator nodes have a _Fill state_ option;  you can draw them with a stroke (an outline) or as a mask (covering over stuff underneath) or both.&#x20;

When you render a shape as a mask, it's as though it's filled in with black and anything underneath it will be covered up.&#x20;

{% hint style="info" %}
Drawing a line (or _stroke_) with a laser is easy enough; you scan the laser from the beginning of the line to the end of the line. There's your line!&#x20;

Filled shapes are harder though; If you want a shape filled with colour you could manually cross hatch by drawing lines and filling in, but Liberation can't do that automatically (yet). And even if we did do that, you'd still see other lines underneath it showing through.&#x20;

But what we can do is fill in shapes with _black_. Under the hood, Liberation is making all the calculations to remove content that are underneath the black-filled shape. And trust me, it's fiddly!&#x20;

But it works really well and gives the illusion of a black filled shape.&#x20;
{% endhint %}

### Depth sorting

As some shapes can _cover over_ other shapes, Liberation has to sort them by their depth. And by default, elements are depth sorted by their z position. If they are at the same z position they are sorted by their layer position which can be changed using the _MOVE TO FRONT_ and _MOVE TO BACK_ buttons inside each creator.&#x20;
