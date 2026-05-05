# ✅ Schnellstartanleitung

## Einführung

Willkommen bei **Liberation** – der nächsten Generation von Lasershow-Software.

Liberation ist eine leistungsstarke und komplexe moderne Software. Sie basiert auf den Grundprinzipien von Benutzerfreundlichkeit und Zuverlässigkeit und gibt dir die Freiheit, deine Kreativität auszudrücken. Sie ist schnell, effizient und nahtlos zu bedienen. Folge dieser _Schnellstartanleitung_, damit du in kürzester Zeit loslegen kannst!

### Laser verwalten

Liberation ist flexibel genug, dass du Laser einrichten und visualisieren kannst, ohne dass echte Laser angeschlossen sind. Wenn du dann bereit bist, kannst du jeden Output nahtlos einem Laser-Controller zuweisen.

{% hint style="info" %}
Du kannst in Liberation beliebig viele Laser einrichten und visualisieren. Die Lizenzstufen (Hobbyist, Pro usw.) begrenzen nur die Anzahl der Laser, die du _aktivieren_ kannst. Das bedeutet, dass du auch mit einer kostenlosen Lizenz Lasershows mit 100 Lasern entwerfen kannst. Ein Upgrade brauchst du erst, wenn du die Show tatsächlich auf echten Lasern ausgeben möchtest.
{% endhint %}

Standardmäßig sind 8 Laser horizontal verteilt, aber du kannst das beliebig anpassen. Am besten behältst du diese Voreinstellung bei, während du die Software kennenlernst. Später kannst du sie dann an dein Hardware-Setup anpassen. (Siehe [Dein Projekt einrichten](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Wichtig: Bevor du Laser aktivierst, stelle sicher, dass du die damit verbundenen Risiken verstehst, und gehe sorgfältig das Kapitel [Überblick über den Laser-Einrichtungsprozess](../setting-up/setting-up-lasers.md "mention") durch.
{% endhint %}

## Überblick über die Software

### Sicherheitsabschaltung

Immer wenn du Laser betreibst, musst du einen **Hardware-Not-Aus-Schalter** griffbereit haben (siehe [Not-Aus / Interlocks](../hardware/emergency-stop-interlocks.md "mention")). Wenn du aber alles weniger dringend deaktivieren möchtest, kannst du den Button _**DISARM ALL**_ verwenden oder die Taste `Escape` drücken (oder die Taste _**SESSION**_ auf der APC40). Du kannst außerdem die globale Helligkeit über den Bildschirm-Slider oder den Hauptfader auf der APC40 reduzieren.

### Slider-Elemente

In Liberation gibt es verschiedene Slider und Bedienelemente.

{% hint style="info" %}
Klicke mit `Cmd / Ctrl` auf einen Slider, um einen neuen Wert einzugeben, wenn du mehr Kontrolle brauchst, als der Slider bietet.
{% endhint %}

### Tastaturkürzel

Eine vollständige Liste der Tastaturkürzel findest du hier: [Tastaturkürzel](../reference/keyboard-shortcuts.md "mention")

### Bildschirmaufbau

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Du bist dir nicht sicher, was ein bestimmter Button macht? Fahre mit der Maus darüber, um eine Beschreibung zu sehen!
{% endhint %}

#### Menü

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Im Menü findest du alle Optionen für Dateiimport und -export sowie zum Öffnen von Panels. Außerdem findest du hier die Option, den Computer mit deinem Abonnement zu autorisieren (_Liberation -> Authorise/Deauthorise this computer_).

#### Icon-Leiste

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Hier findest du häufige Aufgaben, zum Beispiel alle Laser aktivieren/deaktivieren, globale Helligkeit, Test Pattern und das Umschalten zwischen den Ansichten 3D, Canvas und Output.

### Ansichten

Der große Bereich oben links auf dem Bildschirm kann eine von 3 Hauptansichten anzeigen: **3D**, **CANVAS** und **OUTPUT.** Du wechselst zwischen ihnen über die Buttons in der Icon-Leiste (oder mit der Taste `Tab`, um zwischen 3D und OUTPUT zu wechseln und anschließend nacheinander durch die einzelnen Laser-Outputs zu springen).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

Die 3D-Ansicht zeigt dir, wie deine Laser aussehen werden, und kann an dein eigenes Laser-Setup angepasst werden. Klicke und ziehe, um die Kamera zu drehen. Verwende das Mausrad, um vorwärts und rückwärts zu fahren. Viele weitere Optionen findest du im Panel _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Siehe [3D Visualiser](../setting-up/3d-visualiser.md "mention").

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Die Output-Ansicht wird verwendet, um Zonen und Masken für jeden Laser zu konfigurieren. (Beachte die große Zahl in der linken oberen Ecke, damit du leicht erkennen kannst, auf welchem Laser du gerade bist!)

Diese Ansicht stellt den gesamten Output dieses Lasers dar und zeigt, wo sich die einzelnen Zonen darin befinden. Standardmäßig gibt es nur eine Zone pro Laser, aber du kannst so viele Zonen hinzufügen, wie sinnvoll praktikabel sind. Alle werden in dieser Ansicht angezeigt.

{% hint style="info" %}
**Was ist eine Zone?**

Eine Zone ist ein Bereich innerhalb des Outputs eines Lasers, in den du Laser-Content leiten kannst. Du kannst mehr als eine Zone pro Laser haben. Der einfachste Zonentyp ist eine _Beam_-Zone, es gibt aber auch _Canvas_-Zonen und _DMX_-Zonen. In dieser Anleitung konzentrieren wir uns hauptsächlich auf Beam-Zonen, die normalerweise für atmosphärische Beam-Effekte in der Luft verwendet werden.
{% endhint %}

Du kannst den Laser, den du bearbeiten möchtest, auf eine der folgenden Arten auswählen:

* über die nummerierten Buttons in der Leiste oben
* durch Drücken der Zifferntaste für den gewünschten Laser (_Tasten 1-9_)
* mit der Taste `Tab`, um nacheinander durch die Laser zu wechseln

Füge dem Setup einen neuen Laser hinzu, indem du den Button _+_ drückst. (Es gibt außerdem einen Button _ADD LASER_ im Panel _Laser Overview_)

Lösche einen Laser aus dem Setup, indem du den roten Button ⊖ im Panel _Laser Overview_ drückst.

Du kannst mit dem Mausrad hinein- und herauszoomen und an eine beliebige Stelle klicken und ziehen, an der sich keine Zone befindet, um die Ansicht zu verschieben.

Klicke auf eine Zone, um sie auszuwählen, und passe dann ihre Eckpunkte mit der Maus an. Halte beim Ziehen einer Ecke die Taste `Alt / Option` gedrückt, um sie nicht gleichmäßig zu verzerren. Klicke mit der rechten Maustaste auf die Zone, um weitere Optionen zu sehen, darunter das Ändern des Zonentyps.

Links befindet sich eine Leiste mit mehreren Icon-Buttons. Fahre über einen Button, um eine Beschreibung seiner Funktion zu sehen. Mit den Buttons hier kannst du Beam-Zonen, Canvas-Zonen und Masken hinzufügen. Außerdem gibt es Optionen, um nur für diesen Laser ein Test Pattern zu setzen, sowie Einstellungen für Raster und Snapping.

Weitere Details findest du unter [Output-Ansicht](../output-view/ "mention").

#### Canvas

Das Canvas-System wird hauptsächlich für Grafiken und Architektur-Mapping verwendet. Du kannst komplexe Bilder auf mehrere Laser verteilen und jeden Abschnitt perspektivisch korrigieren. Siehe [Grafiken und das Canvas-System](../graphics-and-the-canvas-system/ "mention").

### APC40 MIDI-Controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Obwohl du Liberation mit Maus und Tastatur steuern kannst, ist es deutlich besser, ein APC40 MIDI-Control-Interface zu verwenden (Mark 2 ist am besten, aber Mark 1 funktioniert ebenfalls).

Siehe auch: [APC40-Referenz](../reference/apc40-reference.md "mention")

Liberation unterstützt außerdem APC Mini und MIDI Fighter Twister. Für die meisten Fälle ist die APC40 Mark 2 weiterhin die beste Option.&#x20;

### Clips und Effekte

{% hint style="info" %}
**Was ist ein Clip?**

Ein Clip ist ein Container für beliebigen Laser-Content innerhalb von Liberation. Clips können Beams oder grafische Animationen enthalten und laufen normalerweise als Loop. Sie können in jede Zone (oder _Canvas target area_) geleitet werden und werden über die Clip-Buttons im Clip Deck ausgelöst.
{% endhint %}

#### Überblick über das Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Dieses Raster wird als _Clip Deck_ bezeichnet. Hier werden alle Laser-Clips gespeichert. Es ist so aufgebaut, dass es direkt dem 8 x 5 Button-Raster deiner APC40 entspricht.

**Im Clip Deck navigieren.**

Du kannst das Clip Deck nach links und rechts scrollen mit:

* Pfeiltasten nach links und rechts. Füge `Cmd / Ctrl` hinzu, um jeweils eine ganze Seite weiterzuscrollen.
* Trackpad: Wischen
* Maus: Wenn deine Maus seitliches Scrollen unterstützt, kannst du dies verwenden, während der Mauszeiger über dem Clip Deck ist.
* APC40-Scroll-Regler
* APC40-Buttons _<- DEVICE ->_

Damit du die Orientierung behältst, gibt es oben eine Mini-Visualisierung des Clip Decks. Siehe auch [Clips & Clip Deck](../clips/ "mention")

#### Clips starten und stoppen

Drücke einen Clip-Button (entweder mit der Maus oder mit der APC40), um einen Clip zu starten. Drücke ihn erneut, um ihn zu stoppen. Wenn du einen Clip startest, stoppen alle anderen Clips derselben Farbe automatisch, außer du hältst _shift_ gedrückt.

Einige Clips befinden sich im _Flash mode_ (standardmäßig die roten). In diesem Fall stoppen sie, sobald du den Clip-Button loslässt.

Der Button _STOP_ stoppt alle aktuell laufenden Clips.

#### Output-Zonen für den Clip festlegen

Unter den Clip-Buttons siehst du die Zonen-Buttons, standardmäßig Beam-Zonen 1 bis 8 (_BEAM 1_, _BEAM 2_ usw.). Die Zonen-Buttons leuchten auf, um anzuzeigen, welche Zonen dem aktuell ausgewählten Clip zugewiesen sind.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Zwei Reihen unter den Zonen-Buttons siehst du die X/Y-Flip-Buttons. Schalte sie um, um den Clip horizontal und vertikal zu spiegeln.

{% hint style="info" %}
Beachte, dass diese Zonenzuweisungen und X/Y-Flip-Einstellungen mit dem Clip selbst verbunden sind. Sie bleiben erhalten, wenn du diesen Clip das nächste Mal ausführst. Sie sind keine globale Einstellung.
{% endhint %}

Klicke mit der rechten Maustaste auf einen Clip, um weitere Clip-Einstellungen zu bearbeiten. Siehe auch [Clip-Einstellungen](../clips/clip-settings.md "mention")

### Gruppen

Du wirst sehen, dass jeder Clip eine farbige Umrandung hat. Diese Farbe zeigt an, zu welcher _Gruppe_ er gehört. Die Clip-Buttons der APC40 leuchten ebenfalls in dieser Farbe.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Gruppe 1</td><td>Zyan</td></tr><tr><td>Gruppe 2</td><td>Orange</td></tr><tr><td>Gruppe 3</td><td>Rot</td></tr><tr><td>Gruppe 4</td><td>Indigo</td></tr><tr><td>Gruppe 5</td><td>Grün</td></tr></tbody></table>

Das Gruppensystem ist sehr flexibel und ermöglicht dir:

* Clips in einer Gruppe weiterlaufen zu lassen, während du Clips in einer anderen Gruppe umschaltest
* Zonen und X/Y-Flips schnell allen Clips innerhalb einer Gruppe zuzuweisen
* _Flash mode_ für einen Clip zu setzen (Gruppe 3 ist standardmäßig auf _Flash mode_ gesetzt)

Gruppen haben außerdem Einstellungen für Transition in/out, die von ihren Clips geerbt oder überschrieben werden können.

Du kannst die Gruppe eines Clips über die Buttons im Rechtsklick-Menü zuweisen. Oder du drückst auf der APC40 den Gruppen-Button und drückst, _während er noch gehalten wird,_ die Clip-Buttons.

Zoneneinstellungen für alle Clips innerhalb einer Gruppe ändern

Drücke auf der APC40 den Gruppen-Button und verwende dann, _während er noch gehalten wird,_ die Zonen- und X/Y-Buttons, um Zoneneinstellungen für alle Clips innerhalb dieser Gruppe umzuschalten.

Siehe auch [Clip-Gruppen](../clips/groups.md "mention")

### Effekte

Das Effektsystem in Liberation ist eine leistungsstarke und vielseitige Möglichkeit, den Clip-Output in Echtzeit zu verändern. Die standardmäßigen Effekt-Buttons 1-8 befinden sich unter den Zonen-Buttons.

#### Einen Effekt anwenden

Drücke einen Effekt-Button, um den Effekt umzuschalten. Noch besser ist es, die APC40-Slider 1-8 zu verwenden, um Effekte ein- und auszublenden.

#### Effektparameter

Verwende die Drehregler 1-8\*, um den _Parameter_ für jeden Effekt anzupassen. (Oder du klickst mit der rechten Maustaste, um Level und Parameter mit der Maus anzupassen.) Die Parameteränderung bewirkt je nach Einrichtung des Effekts unterschiedliche Dinge. In der Liste unten findest du die Standardeffekte.

{% hint style="info" %}
Die kleinen Zahlen auf den Effekt-Buttons beziehen sich auf _Level_ und _Parameter_ des Effekts. Der _Level_ wird über den Fader auf der APC40 gesteuert, oder du kannst auf dem Button klicken und ziehen. Der Parameter wird über die Drehregler auf der APC40 angepasst, oder du kannst mit der rechten Maustaste klicken, um ihn mit der Maus anzupassen.
{% endhint %}

_\*Die Drehregler 1-8 befinden sich bei einer APC40 Mk2 oben und bei der Mk1 oben rechts. Siehe auch:_ [APC40-Referenz](../reference/apc40-reference.md "mention")

#### Die Standardeffekte

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Wendet eine chaotische Bewegung auf den Clip-Output an. Der Parameter passt Stärke/Geschwindigkeit des Chaos an.
2. **Sine wave** :\
   Verzerrt den gesamten Content entlang einer bewegten Sinuswelle. Der Parameter passt die Wellenlänge an.
3. **Rotation** :\
   Dreht alles um den Mittelpunkt. Der Parameter passt die Drehgeschwindigkeit an.
4. **Horizontal flip** :\
   Staucht und streckt alles horizontal. Der Parameter passt die Geschwindigkeit an.
5. **Scale** :\
   Skaliert alles wiederholt von vollständig bis null. Der Parameter passt die Geschwindigkeit an.
6. **Hue** :\
Ändert den Farbton von allem, aber nicht die Sättigung (d. h. alles Weiße bleibt weiß). Der Parameter passt den Farbton an.
7. **Saturation and hue** :\
Ändert den Farbton von allem und sättigt die Farbe außerdem vollständig (d. h. alles Weiße ändert sich zur Farbe). Der Parameter passt den Farbton an.
8. **Flash** :\
   Lässt die Helligkeit von allem wiederholt von vollständig bis null blinken. Der Parameter passt die Blinkgeschwindigkeit an.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

In der unteren Reihe gibt es weitere 16 Farbeffekte, mit denen du voreingestellte Farbton- und Sättigungswerte anwenden kannst.

Beachte, dass dies die Standardeffekte sind, sie aber so bearbeitet werden können, dass sie fast alles tun, was du möchtest!

#### Was ist der _„aktuell ausgewählte Clip“_?

Wenn du einen Clip startest, leuchtet er auf, um anzuzeigen, dass er aktiv ist. Außerdem hat er eine weiße Umrandung, die anzeigt, dass dies der aktuell _ausgewählte_ Clip ist. Immer wenn du Zonen-Buttons umschaltest oder Clip-Einstellungen anpasst, werden diese auf den _aktuell ausgewählten Clip_ angewendet.

{% hint style="info" %}
Um einen Clip auszuwählen, ohne ihn auszulösen, drücke die Taste `Alt / Option`, bevor du den Clip-Button drückst. Das ist eine gute Möglichkeit, seine Zonen und andere Einstellungen anzupassen, ohne ihn laufen zu lassen.
{% endhint %}

### Clip Settings-Panel

Verwende das Panel _Clip Settings_, um Skalierung und X/Y-Position zu bearbeiten und auf das leistungsstarke Zonen-Delay-System zuzugreifen.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings-Panel

Öffne das Panel _Global Settings_, um globale Output-Einstellungen anzupassen, die den gesamten Output über alle Zonen hinweg beeinflussen.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Schalte AUTO RESET ein, um alle _Global settings_ automatisch zurückzusetzen, wenn keine Clips abgespielt werden.&#x20;

### Timing

Fast alle Lasershows haben irgendeine Art von musikalischem Soundtrack. Deshalb basiert das Timing-System in Liberation auf einem Tempo in Beats pro Minute. Im _Tempo Panel_ siehst du eine Darstellung der Zeit: Jedes Quadrat steht für einen Beat, und du kannst sehen, wie sie im Takt aufblinken.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Es gibt mehrere Synchronisationsoptionen, darunter MIDI-Clock und Ableton Link. Wenn du das Tempo der Musik kennst, kannst du es manuell über den Bildschirm-Slider oder den APC40-Tempo-Regler anpassen. Du kannst aber auch mit dem _Tap Tempo_-System im Takt der Musik bleiben.

#### Tap Tempo

_Tap Tempo_ ist ein Begriff, der häufig in Musik-Apps verwendet wird. Damit kannst du im Takt mitklopfen, um das Tempo festzulegen, während die Musik läuft. Du kannst den Button auf dem Bildschirm verwenden, empfohlen ist jedoch die Taste _T_ oder der Button _Tap Tempo_ auf der APC40 (oder auch ein Fußschalter, wenn du das bevorzugst).

Drücke die Taste _R_ oder den Button _Metronome_ (APC40), um das Tempo auf den Anfang des Takts zurückzusetzen.

Drücke die Taste _Y_ oder drehe den Regler _Tempo_ (APC40), um das Tempo auf eine ganze Zahl zu runden. Das kann bei elektronischer Musik nützlich sein, die oft eine ganze Anzahl von Beats pro Minute hat.

### Dein Clip Deck organisieren

Um einen Clip auf deinem Clip Deck zu verschieben, klicke ihn an und ziehe ihn an eine neue Position. Während des Ziehens kannst du die Pfeiltasten verwenden (oder das Scrollrad/die Scroll-Buttons auf deiner APC40), um nach links und rechts zu scrollen.

Halte beim Ziehen die Taste `Alt / Option` gedrückt, um eine Kopie zu erstellen.

Klicke mit `Alt / Option` auf einen Clip, um ihn auszuwählen, ohne ihn zu starten.

Klicke mit `Alt / Option + Shift` auf einen Clip, um mehrere auszuwählen, oder klicke und ziehe außerhalb eines Clips, um mit einem „Lasso“ auszuwählen.&#x20;

Klicken und Ziehen verschiebt ALLE ausgewählten Clips.

Um einen oder mehrere Clips zu löschen, ziehe sie entweder vom Clip Deck herunter (ein Papierkorb-Symbol erscheint) oder verwende den Button DELETE im Rechtsklick-Menü des Clips.

### Laser Overview-Panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Das Panel _Laser overview panel_ gibt dir einen schnellen Überblick über den Status deiner aktuell laufenden Laser. Das grüne Quadrat rechts zeigt dir, dass der Laser-Controller in Ordnung ist. Wenn es orange wird, gibt es gelegentliche Drop-outs, und wenn es rot ist, wurde die Verbindung getrennt. Wenn es grau ist, ist es überhaupt nicht mit einem Controller verbunden.&#x20;

Das Diagramm in der Mitte zeigt den Verlauf der Frame-Längen, und die Zahl rechts ist die aktuelle Framerate. Je komplizierter der Content ist, desto niedriger wird die Framerate (d. h. desto stärker flackert es). Alles unter etwa 25 fps wirkt langsam etwas flackernd.&#x20;

### Mit Lasern verbinden – Controller Assignment-Panel

Klicke auf den Button _Assign Laser Controllers_, um das Panel _Controller Assignment_ zu öffnen. (Dieses Panel ist auch über _View -> Controller Assignment_ in der Menüleiste erreichbar.)

Hier kannst du auswählen, welche Laser-Outputs an welche Laser-Controller gehen. Ziehe Controller aus der Liste rechts per Drag-and-drop in die Slots links. Du kannst deine Controller umbenennen, damit sie dem Laser entsprechen, mit dem sie gekoppelt sind (verwende den Button mit dem Stift-Symbol).

Lies das Kapitel [Controller-Zuweisung](../setting-up/controller-assignment.md "mention") für weitere Details.

{% hint style="danger" %}
Bevor du Laser aktivierst, stelle sicher, dass du das Kapitel [Überblick über den Laser-Einrichtungsprozess](../setting-up/setting-up-lasers.md "mention") durchgehst.
{% endhint %}

### Laser Output-Panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Dieses Panel zeigt dir die Einstellungen für den _currently selected laser_ (dargestellt durch die Zahl oben). Ändere den aktuell ausgewählten Laser mit der Taste _tab_, durch Drücken einer Zifferntaste, durch Klicken auf eine Laser-Nummer im Panel _Laser Overview_ oder in der _output view._

* **Number button** aktiviert und deaktiviert den Laser. Wenn er rot ist, ist der Laser aktiviert.
* **Brightness** passt die Laserhelligkeit unabhängig von den anderen Lasern an (und wird mit der Einstellung _global brightness_ kombiniert – d. h. wenn beide bei 50 % liegen, liegt dein Laser bei 25 %).
* **Test Pattern** schaltet ein Test Pattern nur für diesen Laser ein (überschreibt die globale Test-Pattern-Einstellung)
* **Orientation** korrigiert Laser, die seitlich oder kopfüber montiert sind.
* **Flip Horizontal and Flip Vertical** kehrt den Output des Lasers um. Nützlich zur Output-Korrektur bei uneinheitlich verdrahteten Lasern.
* **Copy Laser Settings** öffnet ein Panel, mit dem du verschiedene Einstellungen von diesem Laser auf andere kopieren kannst.

### Scanner-Einstellungen

Showlaser funktionieren, indem sie einen einzelnen Laserstrahl extrem schnell bewegen und ihn ein- und ausschalten, um Formen in die Luft zu zeichnen. Was du als Linien, Formen und Bilder siehst, ist in Wirklichkeit der Strahl, der Pfade schneller abfährt, als deine Augen folgen können.

Ein Point Stream sind die Daten, die dem Laser sagen, wohin er sich als Nächstes bewegen soll und wann der Strahl ein- oder ausgeschaltet sein soll. In Liberation werden Clips in Echtzeit in diesen Point Stream umgewandelt, während sie an die Laser gesendet werden.

Liberation gibt dir detaillierte Kontrolle darüber, wie dieser Point Stream erzeugt wird. So kannst du für jeden Laser Glätte, Helligkeit und Performance ausbalancieren.

{% hint style="info" %}
Wenn du ältere Lasersoftware gewohnt bist, die auf vorberechneten Point Streams basiert, kann sich dieser Ansatz zunächst ungewohnt anfühlen. Die Point-Erzeugung in Echtzeit ermöglicht jedoch, denselben Content für jeden Laser unterschiedlich zu optimieren. Dadurch ist es einfacher, mit mehreren Lasern zu arbeiten, die unterschiedliche Scanner-Geschwindigkeiten oder Qualitätsstufen haben, ohne Content zu duplizieren oder neu aufzubauen. Außerdem bleiben Clip-Dateien sehr klein. Deshalb ist das gesamte standardmäßige Liberation Clip Deck nur wenige Megabyte groß statt Gigabyte.
{% endhint %}

Die grundlegenden Scanner-Einstellungen sind:

* **Speed** ist die Scanner-Geschwindigkeit, also wie schnell sich der Laser bewegt, um Formen zu zeichnen. Das entspricht dem Anpassen der Point Rate in herkömmlicher Lasersoftware, aber in Liberation kannst du ändern, wie schnell sich der Laser bewegt, _unabhängig von der Point Rate._ Du solltest das normalerweise nicht anpassen müssen.
* **Scanner sync** (manchmal als _blank shift_ bekannt, früher Colour Shift) Die Scanner bewegen den Laser sehr schnell, aber meist ist die Änderung von Helligkeit und Farbe nicht mit der Bewegung synchron. Das zeigt sich als kleine flackernde „Schweife“ aus Licht an den Rändern von Beams und Linien. Verwende diese Einstellung, um Bewegung und Farbe miteinander zu synchronisieren. Siehe [Panel „Laser output“-Einstellungen](../setting-up/laser-settings.md "mention")

Die weiteren erweiterten Scanner-Einstellungen werden im Kapitel [Fortgeschrittene Funktionen](../advanced/ "mention") behandelt.

### Zoning

Eine vollständige Anleitung zum Einrichten und Zoning von Lasern findest du hier: [Überblick über den Laser-Einrichtungsprozess](../setting-up/setting-up-lasers.md "mention")
