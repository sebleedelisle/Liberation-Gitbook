# 🟩 Render profile

There is a _Render Profile_ setting in every _Creator_ node, and this determines how the shapes are drawn (or _rendered)_ with the lasers. &#x20;

**For most uses, the&#x20;**_**DEFAULT**_**&#x20;setting is absolutely fine**. But if you're working with graphics, or complex content, you may want more control over how each shape is rendered.&#x20;

{% hint style="info" %}
Unlike most laser software, Liberation generates a point stream in real-time, just before being passed to the laser controllers. This saves you a lot of disk space, clips are just a few kB, instead of MB of pre-rendered point streams.&#x20;

It also means that you can tune the same content for different scanner types on a laser by laser basis, without having to change the clips themselves.&#x20;

For more details see [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

There are three preset _Render Profiles_; _DEFAULT_, _FAST_, and _DETAIL._&#x20;

_**DEFAULT**_ - a good general profile, best for most things

_**FAST** -_ if your clip has a lot of content and some of it is just really simple dots and straight lines, you may get less flicker if you choose this option. &#x20;

_**DETAIL**_ - if you are drawing something that needs sharp corners, use this option. But bear in mind your scanners will move more slowly, making the output flickery.&#x20;

{% hint style="info" %}
Within the clip editor, you can assign creators to different render profiles, but each laser will process these profiles dependent on their scanner settings. See [scanner-presets.md](../../advanced/scanner-presets.md "mention")
{% endhint %}



