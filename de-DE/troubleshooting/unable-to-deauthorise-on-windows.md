---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/unable-to-deauthorise-on-windows
---

# ✅ Deautorisierung unter Windows nicht möglich?

#### Deautorisierung unter Windows nicht möglich?

Wenn du einen Computer unter Windows nicht deautorisieren kannst, stelle zuerst sicher, dass du die Lizenz mit derselben Version von Liberation deautorisierst, mit der sie ursprünglich autorisiert wurde, bevor du sie erneut in einer anderen Version autorisierst.

Wenn das nicht funktioniert und du eine Version vor 1.0 verwendest, liegt das Problem wahrscheinlich daran, wie ältere Windows-Builds von Liberation den Computer identifiziert haben. In diesen Versionen war das System zur Erzeugung einer Maschinen-ID weniger zuverlässig. In einigen Fällen konnte sich die ID zwischen Neustarts ändern, auch wenn sich offensichtlich keine Hardware geändert hatte.

Wenn du beim Deautorisieren nicht weiterkommst und die Version nicht gewechselt hast, kontaktiere bitte support@liberationlaser.com. Wir können den Computer dann manuell für dich deautorisieren.

**Warum das passiert**

In frühen Windows-Builds von Liberation (vor 1.0) haben wir die von Windows empfohlene Systemmethode zur Erzeugung einer Maschinen-ID verwendet. Leider hat sich diese in manchen Situationen als uneinheitlich erwiesen. Deshalb wurde das Lizenzsystem für Version 1.0 neu geschrieben und verwendet jetzt eine robustere Kombination von Methoden, die zuverlässig funktioniert.

Dadurch kann sich die Computer-ID, die von älteren Versionen von Liberation verwendet wird, von der ID unterscheiden, die aktuelle Versionen verwenden. Wenn sich die ID bereits geändert hat, muss die Deautorisierung manuell durch den Support durchgeführt werden.

***
