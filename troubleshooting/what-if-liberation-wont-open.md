# 🟦 What if Liberation won't open?

If Liberation refuses to launch or crashes immediately when opening, the most common fix is to reset your local settings. Here’s how to reset them on macOS and Windows.

> **Important**
>
> * Close Liberation before doing anything.
> * These steps only affect local settings, logs and caches. Your licence and account are safe.

***

#### Where to find the working folder

Each version of Liberation has its own working folder. For example, if you’re running version 1.0.0, the folder name will be 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**How to open the folder quickly**

**macOS**

1. In Finder, press **Shift+Cmd+G**.
2.  Paste this path and press **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Open the folder that matches your version number, for example `1.0.0`.

**Windows**

1.  Press **Win+R**, paste this and press **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Open the folder that matches your version number, for example `1.0.0`.

> **Tip for Windows**: If you browse via File Explorer instead, enable hidden items: **View > Show > Hidden items**.

***

#### Step 1 – Safely reset your settings file

Inside your version folder, open:

```
data/liberation/
```

Inside the liberation folder you should find a file called se`ttings.json`. Delete this file.&#x20;

* **macOS example**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows example**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Now try launching Liberation. If it opens, you are done.

***

#### Step 2 – Check for a problematic clip

If Liberation crashed while you were editing a clip, it’s possible that something about that clip file is causing the problem.

In the same folder as your settings.json file you should find a file called clipEdit`.json`

Back up this file somewhere safe (for example, your Desktop), then delete it from the Liberation working folder.

Try launching Liberation again. If it now opens normally, please email the backed-up file to [**info@liberationlaser.com**](mailto:info@liberationlaser.com) so we can investigate what caused the issue.

***

#### Step 3 - Back up, then delete the whole working folder

If Step 1 and Step 2 did not help:

1. **Back up** the entire version folder:
   * macOS: Right click the `1.0.0` folder and choose **Compress** to make a zip, or copy it somewhere safe like Desktop.
   * Windows: Right click the `1.0.0` folder and choose **Send to > Compressed (zipped) folder**, or copy it somewhere safe like Desktop.
2. After backing up, **delete** the original `1.0.0` folder from the Liberation working location.
3. Launch Liberation again. It will recreate a fresh working folder.

If Liberation now opens, proceed to Step 4.

***

#### Step 4 - Send us the backup

This helps us identify what caused the issue so we can prevent it in future versions.

Zip up your **backup** from Step 3 if you did not already, then email it so we can diagnose the cause.

* **To**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Subject**: Liberation start-up fix - working folder backup
* **Body**: Please include:
  * Operating system and version (e.g. macOS 14.6 or Windows 11 23H2)
  * Liberation version (e.g. 1.0.0)
  * Which step fixed it, if any (Step 1, Step 2 or Step 3)
  * A brief description of what happened before the issue started
* **Attachment**: the zipped backup of your `1.0.0` working folder.

> If the zip is too large for email, upload it to a cloud drive and share a link.

***

#### Still not launching after Step 3?

If Liberation still won’t open after deleting the working folder:

* Reboot your computer and try again.
* Temporarily disable antivirus or security tools that might block new folders, then try launching.
* Reinstall the latest Liberation build over the top of your existing install.
* If none of the above works, contact support at [**info@liberationlaser.com**](mailto:info@liberationlaser.com) with details and any crash logs from the `logs` subfolder if present.

***

#### Summary

1. Delete `data/liberation/settings.json` in your versioned working folder.
2. If you were editing a clip, back up then delete `data/liberation/clipEdit.json`.
3. If it still doesn’t open, back up then delete the whole `1.0.0` (or your version) folder.
4. If Step 3 fixes it (or if it doesn't), zip the backup and send it to [**info@liberationlaser.com**](mailto:info@liberationlaser.com) with your OS, Liberation version.
