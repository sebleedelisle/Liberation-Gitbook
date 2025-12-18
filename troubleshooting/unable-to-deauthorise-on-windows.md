# ✅ Unable to deauthorise on Windows?

#### Unable to deauthorise on Windows?

If you are unable to deauthorise a computer on Windows, first make sure you deauthorise the licence using the same version of Liberation that was originally authorised, before authorising it again in a different version.

If this does not work and you are using a version earlier than 1.0, the issue is likely due to how older Windows builds of Liberation identified the computer. In those versions, the system used to generate a machine ID was less reliable, and in some cases the ID could change between restarts, even if no hardware had obviously changed.

If you are stuck trying to deauthorise and have not switched versions, please contact support@liberationlaser.com and we can deauthorise the machine manually for you.

**Why this happens**

In early Windows builds of Liberation (pre-1.0), we used the recommended Windows system method for generating a machine ID. Unfortunately, this proved to be inconsistent in some situations. Because of this, the licensing system was rewritten for version 1.0 to use a more robust combination of methods, which now works reliably.

As a result, the computer ID used by older versions of Liberation may differ from the one used by current versions. If the ID has already changed, deauthorisation must be handled manually by support.

***
