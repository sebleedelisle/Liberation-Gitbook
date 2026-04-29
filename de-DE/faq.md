---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Hardware

#### **Läuft Liberation unter Windows?**

Ja – Liberation unterstützt **Windows 10 und 11 (64-bit)** vollständig, mit exakt demselben Funktionsumfang wie die Mac-Version. Jede Version wird gleichzeitig für beide Plattformen veröffentlicht.

#### **Läuft Liberation auf dem Mac?**

Ja – Liberation unterstützt **Mac (macOS 12 Monterey und neuer)** vollständig, mit demselben Funktionsumfang wie die Windows-Version. Alle Updates werden gemeinsam veröffentlicht.

#### **Welche Mindestanforderungen muss mein Computer erfüllen?**

Das hängt davon ab, wie viele Laser du steuern möchtest. Wenn du nur wenige Laser betreibst, reicht ein Computer mit eher niedriger Leistung aus. Jeder Apple-Silicon-Mac läuft sehr gut und sollte bis zu 100 Laser steuern können. Wenn du komplexe Shows mit hohen Anforderungen betreibst, empfehlen wir den besten Computer, den du dir leisten kannst.

#### **Wie viele Laser kann ich mit Liberation steuern?**

Liberation kann viele Laser auf einem Computer betreiben. Es wurde mit über 100 Laser-Controllern getestet, daher hängt die Antwort ab von:

* der CPU deines Computers
* der Netzwerkgeschwindigkeit
* deinem Abotyp

#### **Welche MIDI-Controller kann ich verwenden?**

Liberation wurde für den beliebten APC40 Mk2 MIDI-Controller entwickelt und optimiert. Es funktioniert auch mit dem APC40 Mk1. Siehe [Live-Steuerung mit dem APC40](midi-control/live-control-with-the-apc40.md "mention")

Wir fügen nach und nach weitere MIDI-Controller hinzu und unterstützen derzeit außerdem den APC Mini Mk2 und den MIDI Fighter Twister.

Zusätzlich gibt es das MIDI Send/Receive-System, das weitere MIDI-Steuerungsmöglichkeiten bietet. Siehe [MIDI Send/Receive](midi-control/midi-send-receive.md "mention")

Weitere Informationen findest du unter [MIDI-Steuerung](midi-control/ "mention").

#### **Kann ich es mit jedem MIDI-Controller verwenden?**

Wir arbeiten derzeit an einem konfigurierbaren MIDI-System, das dies in Zukunft ermöglichen wird. In der Zwischenzeit hatten einige Nutzer Erfolg mit einem MIDI-Interpreter, der beliebige MIDI-Nachrichten für das MIDI Send/Receive-System umwandeln kann. Das ist jedoch ein umständlicher und fortgeschrittener Vorgang. Suche im [forum](https://forum.liberationlaser.com) nach Hinweisen zu dieser Einrichtung – realistisch gesehen ist der APC40 aber die beste Option.

## Laser-Controller

#### **Welche Laser-Controller sind mit Liberation kompatibel?**

* [Ether Dream (recommended)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (du musst eventuell deine Firmware aktualisieren)
* LaserCube USB (und LaserDock)
* LaserCube-Netzwerkprotokoll (mit kabelgebundener Verbindung)
* AVB, wie es von [LASollinger lasers](https://laseranimation.com/en/) verwendet wird (derzeit nur macOS, in der Testphase)

Weitere Informationen findest du unter [Kompatible Laser und Controller (DACs)](hardware/compatible-lasers-and-controllers-dacs.md "mention").

#### **Warum unterstützt ihr \[andere Marke von] Laser-Controllern nicht?**

Um eine bessere Interoperabilität zwischen Software und Hardware zu fördern, unterstützt Liberation nur DACs mit veröffentlichtem Kommunikationsprotokoll. Ich glaube, dass dies der beste Weg für die Laserbranche ist.

#### **Woran erkenne ich, ob mein Laser mit Liberation verwendet werden kann?**

Wenn dein Laser eines der folgenden Merkmale hat, kannst du ihn mit Liberation verwenden:

* Einen externen **ILDA-Eingang** – einen 25-poligen D-Stecker, der mit einem kompatiblen externen Controller verwendet wird.
* Einen intern installierten **Ether Dream**.
* Einen beliebigen **LaserCube** (funktioniert sowohl mit USB- als auch mit Wi-Fi-LaserCube).
* Ein **X-Laser-Gerät mit integriertem Mercury-System** (im Ether Dream-Modus).
* Einen **LaserAnimation Sollinger-Projektor mit integriertem AVB** (nur macOS, erfordert AVB-kompatible Netzwerkgeräte, derzeit in der Testphase).

Weitere Informationen findest du unter [Kompatible Laser und Controller (DACs)](hardware/compatible-lasers-and-controllers-dacs.md "mention").

#### **Kann ich Liberation mit meinem LaserCube verwenden?**

Ja, Liberation funktioniert direkt mit jedem LaserCube. Siehe [LaserCube](hardware/lasercube.md "mention")

## Lizenzen

#### **Was kostet eine Lizenz?**

Die aktuellen Preise findest du auf der [shop](https://liberationlaser.com/shop)-Seite.

#### **Welche Einschränkungen gibt es zwischen den Lizenzstufen?**

Die aktuellen Lizenzoptionen findest du auf der [shop](https://liberationlaser.com/shop)-Seite.

Beachte, dass du Shows mit beliebig vielen Lasern auf **jeder** Lizenzstufe einrichten, vorab ansehen und gestalten kannst – sogar in der kostenlosen Stufe. Es gibt keinerlei weitere Einschränkungen außer der Anzahl der Laser, die du _aktivieren_ kannst. Alle anderen Funktionen von Liberation stehen allen zur Verfügung.

#### **Kann ich auf eine höhere Stufe upgraden?**

Du kannst jederzeit auf eine höhere Stufe upgraden. Für die Restlaufzeit deiner aktuellen Lizenz erhältst du eine anteilige Rückerstattung, und dein neuer Plan beginnt sofort. Siehe [Lizenz upgraden / downgraden](installation/upgrade-downgrade-your-license.md "mention")

#### **Kann ich meine Lizenz downgraden?**

Du kannst jederzeit downgraden, aber die Änderung wird erst am Ende deines aktuellen Lizenzzeitraums wirksam. Siehe [Lizenz upgraden / downgraden](installation/upgrade-downgrade-your-license.md "mention")

#### **Wie autorisiere ich meinen Computer mit meiner Lizenz?**

Sobald du eine Lizenz gekauft hast, kannst du den Computer direkt in der Liberation-Software autorisieren. Auf dem _About_-Bildschirm siehst du einen _Authorise_-Button, der dich auffordert, dich auf der Website anzumelden. Folge den Anweisungen auf dem Bildschirm, um die Autorisierung abzuschließen. Siehe [Autorisieren und Deautorisieren](installation/authorising-and-de-authorising.md "mention")

#### **Wie oft muss ich meinen Computer mit dem Internet verbinden?**

Jedes Mal, wenn die Lizenz verlängert wird, musst du Liberation mit dem Internet verbinden, damit die interne Lizenz aktualisiert werden kann. Bei einer monatlich wiederkehrenden Zahlung musst du jeden Monat eine Verbindung herstellen.

#### **Was passiert, wenn ich meinen Computer nach der Verlängerung nicht mit dem Internet verbinden kann?**

Liberation gibt dir nach der Verlängerung deiner Lizenz eine Kulanzzeit von 7 Tagen, um eine Internetverbindung herzustellen und die interne Lizenz zu aktualisieren. Nach diesem Zeitraum wechselt Liberation zurück in den _Free_-Modus.

#### **Was passiert, wenn meine Kreditkarte abläuft?**

Du erhältst eine E-Mail-Benachrichtigung von unserem Zahlungsanbieter und musst deine Zahlungsdaten aktualisieren. Melde dich auf der Website an und verwende den Link _Update payment details_ auf der Abonnementseite.

#### **Wie kündige ich meine wiederkehrende Lizenz?**

Melde dich auf der Website an, öffne die Seite _Your subscriptions_, wähle das Abonnement aus, das du kündigen möchtest, und klicke dann auf den Link _Cancel Subscription_. Du kannst Liberation bis zum Ende des Lizenzzeitraums weiter verwenden.

#### **Auf wie vielen Computern kann ich Liberation installieren?**

Du kannst Liberation auf beliebig vielen Computern installieren. Lizenzautorisierungen sind nur erforderlich, um Laser- / DMX-Ausgabe zu aktivieren, und deine Lizenzstufe bestimmt, wie viele Computer gleichzeitig für die Ausgabe autorisiert sein können. Siehe [So funktioniert die Lizenzierung](installation/how-licensing-works.md "mention")

#### **Wie verschiebe ich meine Lizenz von einem Computer auf einen anderen?**

* Öffne Liberation auf dem Computer, den du nicht mehr verwenden möchtest
* Stelle sicher, dass du mit dem Internet verbunden bist, und klicke auf dem _About_-Bildschirm auf den Button _De-authorise this computer_
* Öffne jetzt Liberation auf dem neuen Computer
* Klicke auf dem _About_-Bildschirm auf den Button _Authorise this computer_.
* Die Website wird geöffnet. Melde dich an und folge den Anweisungen auf dem Bildschirm, um die Autorisierung abzuschließen

Du kannst auch einen Computer, auf den du keinen Zugriff mehr hast, aus der Ferne de-autorisieren (mit einigen Einschränkungen). Siehe [Autorisieren und Deautorisieren](installation/authorising-and-de-authorising.md "mention")

#### **Kann ich Liberation auf einem Computer de-autorisieren, der verloren gegangen ist oder gestohlen wurde?**

Du kannst den Computer über die Website de-autorisieren. Wenn die Liberation-Installation seit deiner letzten Verlängerung nicht online war, kann dies sofort durchgeführt werden.

Andernfalls wird die De-Autorisierung wirksam, wenn das Abonnement verlängert wird oder wenn der Computer eine Internetverbindung herstellt – je nachdem, was zuerst eintritt. Wenn du dringend einen neuen Computer neu autorisieren musst, wende dich an den Support.

### Liberation verwenden

#### Die Standardeinrichtung hat 8 Laser – wie ändere ich das?

Siehe [Dein Projekt einrichten](setting-up/setting-up-your-project.md "mention") und [Laser hinzufügen / entfernen](setting-up/adding-removing-lasers.md "mention")

#### Kann ich Zoneneinstellungen von einem Laser auf die anderen kopieren?

Ja! Siehe [Zonen zwischen Lasern kopieren](output-view/copy-zones-between-lasers.md "mention")

#### Kann ich eine Zahl eingeben, statt einen Slider zu verwenden?

Ja. Klicke mit `Cmd / Ctrl` auf den Slider, dann kannst du den Wert über die Tastatur eingeben.

#### **Wie synchronisiere ich Liberation mit Musik?**

Liberation hat ein intelligentes „Tap Tempo“-System, das so funktioniert, wie du es erwarten würdest. Du kannst aber auch eine externe MIDI-Clock oder Ableton Link verwenden. Siehe [Tempo / Synchronisation](tempo-synchronisation.md "mention"). Die Timeline kann mit eingehendem LTC/SMPTE-Timecode synchronisiert werden, der über ein beliebiges Audio-Interface eingeht. Siehe [Timecode](timecode.md "mention").

#### Welche Einstellungen muss ich anpassen, um die beste Ausgabe vom Laser zu erhalten?

Die wichtigste Einstellung ist _Colour Shift_. Sie kompensiert die leichte Verzögerung zwischen der Bewegung der Spiegel und der Helligkeitsänderung der Laser. Wenn deine Laserpunkte/-strahlen kleine „Schweife“ haben, musst du diese Einstellung anpassen. (Ein Beispiel für „Schweife“ findest du auf der Seite [Laser-Ausgabe-Einstellungen](setting-up/laser-settings.md "mention") in den Fotos.)

Du kannst auch versuchen, die Scannergeschwindigkeit zu ändern: langsamer, wenn deine Scanner einfach sind, oder schneller, wenn sie hochwertig sind. Aber **verwende diese Einstellung mit Vorsicht, da du deine Scanner beschädigen kannst, wenn du sie zu stark belastest.**

Es gibt außerdem einige voreingestellte Scanner-Einstellungen. Die Standardoption ist konservativ und für die meisten Laserbeam-Anforderungen gut geeignet. Es gibt aber weitere Presets für bessere Scanner sowie Presets, die auf Grafiken abgestimmt sind.

Weitere Informationen findest du unter [Laser-Ausgabe-Einstellungen](setting-up/laser-settings.md "mention"). Informationen dazu, wie du eigene Presets erstellst, findest du unter [◼️ Scanner-Presets & Render-Profile](advanced/scanner-presets.md "mention") (fortgeschritten, in Arbeit).

Du kannst außerdem die Farbbalance mit den Einstellungen _Colour calibration_ korrigieren. Siehe [Farbkalibrierung](advanced/colour-calibration.md "mention") (fortgeschrittene Technik)

#### Was bewirkt die Einstellung _Latency(ms)_?

Das ist die Frame-Latenz, also die maximale Zeitspanne zwischen dem Erzeugen eines Frames und dem anschließenden Senden an einen Laser. Du solltest sie normalerweise nicht anpassen müssen. Wenn du jedoch Netzwerkprobleme hast, kannst du versuchen, sie zu erhöhen. Weitere Details findest du unter [Latenzeinstellung](setting-up/latency-setting.md "mention").

### Clips

#### Wie passe ich Zonen und Einstellungen für einen Clip an, ohne ihn zu starten?

Klicke mit `Alt / Option`, um ihn zum _aktuell ausgewählten Clip_ zu machen, ohne ihn zu aktivieren. Siehe auch [Clips starten / stoppen](clips/starting-stopping-clips.md "mention")

#### Wie kopiere ich Clips?

Klicke und ziehe bei gedrückter `Alt / Option`-Taste. Siehe auch [Dein Clip Deck organisieren](clips/organising-your-clip-deck.md "mention")

#### Wie lösche ich Clips?

Klicke auf sie und ziehe sie aus dem Clip Deck heraus. Siehe auch [Dein Clip Deck organisieren](clips/organising-your-clip-deck.md "mention")

#### Wie wähle ich mehrere Clips aus, lösche sie, kombiniere Clip Decks usw.?

Siehe [Dein Clip Deck organisieren](clips/organising-your-clip-deck.md "mention")

#### Was bedeuten das kleine Mikrofonsymbol und andere Symbole auf dem Clip?

Sie zeigen dir, dass ein Clip Sound- oder MIDI-Eingang verwendet. Die 3 Punkte zeigen an, dass es eine Zonenverzögerung gibt. Siehe [Was bedeuten die kleinen Symbole auf den Clip-Buttons?](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
