---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Loading and saving

Liberation constantly saves its state to disk so you can be sure that if you have a power outage or system issue, it will start up right where it left off, you shouldn't ever lose your zones, timeline or other content.

However you can export your set up for backup and transferring to another computer.

### Project Import/Export

The Project file stores almost everything in your current set up, including :

* Everything detailed in [#laser-settings-import-export](loading-and-saving.md#laser-settings-import-export "mention")below
* Clips, effects and group settings
* All of your timelines (not including audio and video media)
* Artnet set up
* MIDI send/receive settings
* Tempo / synchronisation settings

It doesn't currently save and load :

* Sound and Midi input settings as used in the MIDI notes node and the Sound Input Oscillator (it _does_ save MIDI send/receive settings as well as the timecode sound input)
* Interface scaling
* Media for Canvas guide images
* Sound and Video media for timelines
* Fonts used in the Text node

{% hint style="danger" %}
Sound and video files in the timeline are not saved with project files so be sure to save them separately if you want to transfer to a different computer. See [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Laser settings Import / Export

* Laser settings for every laser
* Beam zones
* Canvas target areas
* DMX zones
* Laser controller assignment (and aliases for any of your controllers that you have renamed)
* Laser scanner and colour calibration settings and presets
* 3D visualiser settings and presets

### Clip Deck Import / Export

* All of the clips and their zone assignments, settings and parameters
* All of the group settings, flash mode, fade in/out times etc

It doesn't currently save and load :

* All of the effects and their parameters and settings

{% hint style="info" %}
**Load clips from a project file without loading the whole project**

To import just the clips from a project, select _**Clips->Import Clip Deck**_, and instead of selecting a clip deck file (.cpdk), choose a project file.
{% endhint %}

### Append clip deck

You can add clips from an exported clip deck file to your current project using _Append Clip Deck_. Clips are added to the end of your current clip deck, but the effects and group settings within the file are not imported.

### Export Selected Clips

Any currently selected clips will be exported into a file. Group settings and effects will not be saved, only the clips. Note that currently running active clips are not exported unless they are also selected.

{% hint style="info" %}
Option/Alt - shift - click clips to select them (or use the lasso). You can tell which clips are selected by the thick white outline around them. See [starting-stopping-clips.md](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Effects Import / Export

Loads and saves all of the effects along with their group settings and parameters.

{% hint style="info" %}
**Load effects from a project file without loading the whole project**

To import just the effects from a project, select _**Effects->Import Effects**_, and instead of selecting a effects file (.efts), choose a project file.
{% endhint %}

### Timeline Export

Export a timeline file with one or more timelines. Note that the clipdeck is always included with exported timeline files (although you can be selective about which clips you import back in, see [#timeline-import](loading-and-saving.md#timeline-import "mention")below)

If you have more than one timeline in your project file, a panel will open allowing you to select which timeilnes you want to export.

{% hint style="danger" %}
Sound and video files in the timeline are not saved with timeline files so be sure to save them separately if you want to transfer your content to a different computer. See [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Timeline Import

Import one or more timelines from a single timeline file. After you have selected your timeline file, a panel will open with multiple import options.

If the timeline file has more than one timeline they will all be listed. Check the ones that you want to include.

* Replace existing timelines\
  Will delete all of your current timelines with the ones imported
* Import used clips only\
  Will import only the clips used, and will arrange the clips in groups, one for each timeline. If this option is not selected, the timeline file's entire clip deck will be appended to your existing clips.
* Replace existing clip deck\
  Replaces your current clip deck with clips in the timeline file. Only available if _Replace existing timelines_ is selected.

{% hint style="info" %}
**Load timelines from a project file without loading the whole project**

To import just the timelines from a project, select _**Timeline->Import Timeline(s)**_, and instead of selecting a timeline file (.ltml), choose a project file.
{% endhint %}

### DMX / Artnet import / export

Saves and loads the Artnet nodes, along with their IP addresses. Also includes the DMX zones, and all of your DMX presets.

### Important note about timeline media files

Sound and video files **are not** currently exported with the timeline file so if you need to move content to a different computer make sure to include these.

{% hint style="info" %}
**How a timeline looks for media files**

When the timeline is loaded, it will look in the same folder as the timeline (or project) file and search within it and any subfolders. So as long as the files are in the same folder or a subfolder (such as _/videos_ or _/sound_ it will find them when it loads.
{% endhint %}
