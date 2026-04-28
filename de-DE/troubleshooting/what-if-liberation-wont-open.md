---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Was, wenn Liberation nicht startet?

Es kommt selten vor, aber manchmal startet Liberation nicht oder stürzt direkt nach dem Öffnen ab. Das liegt fast immer daran, dass eine der lokalen Konfigurationsdateien beschädigt wurde – meist nach einem Systemabsturz oder einem unerwarteten Ereignis auf deinem Computer.

Zum Glück lässt sich das leicht beheben, indem du deine lokalen Einstellungen zurücksetzt. So gehst du unter macOS und Windows vor.

> **Wichtig**
>
> * Schließe Liberation, bevor du etwas änderst.
> * Diese Schritte betreffen nur lokale Einstellungen, Logs und Caches. Deine Lizenz und dein Konto bleiben sicher.

***

#### Wo du den Arbeitsordner findest

Jede Version von Liberation hat ihren eigenen Arbeitsordner. Wenn du zum Beispiel Version 1.0.0 verwendest, heißt der Ordner 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**So öffnest du den Ordner schnell**

**macOS**

1. Drücke im Finder **Shift + Cmd + G**.
2.  Füge diesen Pfad ein und drücke **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Öffne den Ordner, der zu deiner Versionsnummer passt, zum Beispiel `1.0.0`.

**Windows**

1.  Drücke **Win + R**, füge Folgendes ein und drücke **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Öffne den Ordner, der zu deiner Versionsnummer passt, zum Beispiel `1.0.0`.

> **Tipp für Windows**: Wenn du stattdessen über den File Explorer navigierst, aktiviere ausgeblendete Elemente: **View > Show > Hidden items**.

***

#### Schritt 1 – Deine Einstellungsdatei sicher zurücksetzen

Öffne in deinem Versionsordner:

```
data/liberation/
```

Im liberation-Ordner solltest du eine Datei namens se`ttings.json` finden. Lösche diese Datei.

* **macOS-Beispiel**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows-Beispiel**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Versuche nun, Liberation zu starten. Wenn es sich öffnet, bist du fertig.

***

#### Schritt 2 – Auf einen problematischen Clip prüfen

Wenn Liberation abgestürzt ist, während du einen Clip bearbeitet hast, kann es sein, dass etwas an dieser Clip-Datei das Problem verursacht.

Im selben Ordner wie deine settings.json-Datei solltest du eine Datei namens clipEdit`.json` finden.

Sichere diese Datei an einem sicheren Ort (zum Beispiel auf deinem Desktop) und lösche sie anschließend aus dem Liberation-Arbeitsordner.

Versuche erneut, Liberation zu starten. Wenn es jetzt normal startet, sende die gesicherte Datei bitte per E-Mail an [**info@liberationlaser.com**](mailto:info@liberationlaser.com), damit wir untersuchen können, wodurch das Problem verursacht wurde.

***

#### Schritt 3 - Den gesamten Arbeitsordner sichern und anschließend löschen

Wenn Schritt 1 und Schritt 2 nicht geholfen haben:

1. **Sichere** den gesamten Versionsordner:
   * macOS: Klicke mit der rechten Maustaste auf den Ordner `1.0.0` und wähle **Compress**, um eine ZIP-Datei zu erstellen, oder kopiere ihn an einen sicheren Ort, zum Beispiel auf den Desktop.
   * Windows: Klicke mit der rechten Maustaste auf den Ordner `1.0.0` und wähle **Send to > Compressed (zipped) folder**, oder kopiere ihn an einen sicheren Ort, zum Beispiel auf den Desktop.
2. Nachdem du die Sicherung erstellt hast, **lösche** den ursprünglichen Ordner `1.0.0` aus dem Liberation-Arbeitsordner.
3. Starte Liberation erneut. Es erstellt automatisch einen neuen Arbeitsordner.

Wenn Liberation jetzt startet, fahre mit Schritt 4 fort.

***

#### Schritt 4 - Sende uns die Sicherung

Das hilft uns herauszufinden, wodurch das Problem verursacht wurde, damit wir es in zukünftigen Versionen verhindern können.

Komprimiere deine **Sicherung** aus Schritt 3 als ZIP-Datei, falls du das noch nicht getan hast, und sende sie uns per E-Mail, damit wir die Ursache diagnostizieren können.

* **An**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Betreff**: Liberation start-up fix - working folder backup
* **Nachricht**: Bitte gib Folgendes an:
  * Betriebssystem und Version (z. B. macOS 14.6 oder Windows 11 23H2)
  * Liberation-Version (z. B. 1.0.0)
  * Welcher Schritt das Problem behoben hat, falls einer geholfen hat (Schritt 1, Schritt 2 oder Schritt 3)
  * Eine kurze Beschreibung, was passiert ist, bevor das Problem aufgetreten ist
* **Anhang**: die gezippte Sicherung deines `1.0.0`-Arbeitsordners.

> Wenn die ZIP-Datei zu groß für eine E-Mail ist, lade sie in einen Cloud-Speicher hoch und teile einen Link.

***

#### Startet Liberation nach Schritt 3 immer noch nicht?

Wenn Liberation nach dem Löschen des Arbeitsordners immer noch nicht startet:

* Starte deinen Computer neu und versuche es erneut.
* Deaktiviere vorübergehend Antivirus- oder Sicherheitstools, die neue Ordner blockieren könnten, und versuche dann, Liberation zu starten.
* Installiere den neuesten Liberation-Build über deine bestehende Installation.
* Wenn nichts davon funktioniert, kontaktiere den Support unter [**info@liberationlaser.com**](mailto:info@liberationlaser.com) mit Details und, falls vorhanden, allen Crash-Logs aus dem Unterordner `logs`.

***

#### Zusammenfassung

1. Lösche `data/liberation/settings.json` in deinem versionierten Arbeitsordner.
2. Wenn du einen Clip bearbeitet hast, sichere `data/liberation/clipEdit.json` und lösche die Datei anschließend.
3. Wenn Liberation immer noch nicht startet, sichere den gesamten Ordner `1.0.0` (oder den Ordner deiner Version) und lösche ihn anschließend.
4. Wenn Schritt 3 das Problem behebt (oder auch wenn nicht), zippe die Sicherung und sende sie mit deinem Betriebssystem und deiner Liberation-Version an [**info@liberationlaser.com**](mailto:info@liberationlaser.com).
