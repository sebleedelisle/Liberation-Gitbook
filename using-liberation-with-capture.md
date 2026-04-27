---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Using Liberation with Capture

Liberation supports [Capture](https://capture.se) as an external visualiser (version 1.0.3 onwards). If you’re already using Capture in your workflow, you can use it to visualise Liberation’s live laser output in your 3D scene.

### How it works

There’s no special connection process or manual linking required.

As long as:

* Liberation and Capture are on the same network
* Your firewall allows the connection

…then any lasers you’ve set up in Liberation will automatically appear inside Capture as media sources. You don’t need to configure IP addresses or enable anything special - it just shows up.

### Seeing lasers inside Capture

All configured lasers in Liberation will appear in Capture as available media sources.

To actually see output:

* The laser must be armed in Liberation
* The source must be attached to a laser fixture inside Capture

Once armed, Capture will visualise the live output stream from Liberation. If a laser is disarmed in Liberation, it will remain visible in Capture as a source, but it won’t output anything.

See the documentation at [capture.se](https://www.capture.se/) for more instructions and support for setting up lasers in Capture. <br>

### Licence limits and armed lasers

Capture connections are treated exactly the same as physical laser outputs.

That means:

* You can only arm as many lasers as your licence tier allows
* Only armed lasers will actively send data to Capture

### Do I need Capture?

Not at all.

Liberation includes a built-in 3D visualiser, which is always available and doesn’t depend on your licence tier. You can design and preview shows directly inside Liberation without any external software.

Capture is simply an additional option if you’re already using it for lighting or show design.

### Troubleshooting

If lasers don’t appear in Capture:

* Check both applications are on the same network
* Check your firewall settings
* Make sure the laser is armed in Liberation
