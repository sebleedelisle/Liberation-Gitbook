---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Schnellstartanleitung

## Einführung

Willkommen bei **Liberation** – der nächsten Generation von Lasershow-Software.

Liberation ist eine leistungsstarke und komplexe moderne Software. Sie basiert auf den Grundprinzipien von Benutzerfreundlichkeit und Zuverlässigkeit und gibt dir die Freiheit, deine Kreativität auszudrücken. Sie ist schnell, effizient und nahtlos zu bedienen. Folge dieser _Schnellstartanleitung_, um in kürzester Zeit loszulegen!

### Laser verwalten

Liberation ist so flexibel, dass du Laser einrichten und visualisieren kannst, ohne dass überhaupt echte Laser angeschlossen sind. Wenn du dann bereit bist, kannst du jeden Ausgang nahtlos einem Laser-Controller zuweisen.

{% hint style="info" %}
Du kannst in Liberation beliebig viele Laser einrichten und visualisieren. Die Lizenzstufen (Hobbyist, Pro usw.) begrenzen nur die Anzahl der Laser, die du _aktivieren_ kannst. Das bedeutet, dass du auch mit einer kostenlosen Lizenz Lasershows mit 100 Lasern entwerfen kannst. Ein Upgrade brauchst du erst, wenn du die Show tatsächlich auf echten Lasern ausgeben möchtest.
{% endhint %}

Standardmäßig sind 8 Laser horizontal verteilt, aber du kannst das nach deinen Wünschen anpassen. Während du die Software kennenlernst, ist es wahrscheinlich am besten, diese Voreinstellung beizubehalten. Später kannst du sie dann an dein Hardware-Setup anpassen. (Siehe [Dein Projekt einrichten](setting-up/setting-up-your-project.md "mention"))

{% hint style="warning" %}
Wichtig: Bevor du Laser aktivierst, stelle sicher, dass du die damit verbundenen Risiken verstehst, und arbeite sorgfältig das Kapitel [Überblick über den Laser-Einrichtungsprozess](setting-up/setting-up-lasers.md "mention") durch.
{% endhint %}

## Überblick über die Software

### Sicherheitsabschaltung

Immer wenn du Laser betreibst, musst du einen **Hardware-Not-Aus-Taster** griffbereit haben (siehe [Not-Aus / Interlocks](hardware/emergency-stop-interlocks.md "mention")). Wenn du jedoch weniger dringend alles deaktivieren möchtest, kannst du den Button _**DISARM ALL**_, die Taste `Escape` oder die Taste _**SESSION**_ auf dem APC40 verwenden. Du kannst außerdem die globale Helligkeit mit dem Bildschirm-Slider oder dem Main-Fader auf dem APC40 reduzieren.

### Slider-Elemente

In Liberation gibt es verschiedene Slider und Bedienelemente.

{% hint style="info" %}
Klicke mit `Cmd / Ctrl` auf einen Slider, um einen neuen Wert einzugeben, wenn du mehr Kontrolle brauchst, als dir der Slider bietet.
{% endhint %}

### Tastenkürzel

Eine vollständige Liste der Tastenkürzel findest du hier: [Tastaturkürzel](reference/keyboard-shortcuts.md "mention")

### Bildschirmaufbau

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Du bist dir nicht sicher, was ein bestimmter Button macht? Fahre mit der Maus darüber, um eine Beschreibung zu sehen!
{% endhint %}

#### Menü

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Im Menü findest du alle Optionen zum Importieren und Exportieren von Dateien sowie zum Öffnen von Panels. Außerdem findest du hier die Option, den Computer mit deinem Abonnement zu autorisieren (unter _Liberation -> Authorise/Deauthorise this computer_).

#### Icon-Leiste

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Hier findest du häufig verwendete Funktionen, etwa alle Laser aktivieren/deaktivieren, globale Helligkeit, Test Pattern sowie das Umschalten zwischen den Ansichten 3D, Canvas und Output.

### Ansichten

Der große Bereich oben links auf dem Bildschirm kann eine von 3 Hauptansichten anzeigen: **3D**, **CANVAS** und **OUTPUT.** Du wechselst zwischen ihnen über die Buttons in der Icon-Leiste (oder mit der Taste `Tab`, um zwischen der 3D- und der OUTPUT-Ansicht zu wechseln und anschließend nacheinander durch jeden Laserausgang zu springen).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D-Ansicht

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

Die 3D-Ansicht zeigt dir, wie deine Laser aussehen werden, und kann so konfiguriert werden, dass sie deinem eigenen Laser-Setup entspricht. Klicke und ziehe, um die Kamera zu drehen, und nutze das Mausrad, um vorwärts und rückwärts zu fahren. Viele weitere Optionen findest du im Panel _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Siehe [3D Visualiser](setting-up/3d-visualiser.md "mention").

#### Output-Ansicht

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Die Output-Ansicht wird verwendet, um Zonen und Masken für jeden Laser zu konfigurieren. (Beachte die riesige Zahl oben links, damit du leicht erkennen kannst, auf welchem Laser du gerade bist!)

Diese Ansicht stellt den gesamten Ausgang dieses Lasers dar und zeigt, wo sich die einzelnen Zonen darin befinden. Standardmäßig gibt es nur eine Zone pro Laser, aber du kannst so viele Zonen hinzufügen, wie sinnvoll und praktikabel sind. Du siehst sie alle in dieser Ansicht.

{% hint style="info" %}
**Was ist eine Zone?**

Eine Zone ist ein Bereich innerhalb des Ausgangs eines Lasers, in den du Laser-Content leiten kannst. Du kannst mehr als eine Zone pro Laser haben. Die einfachste Art von Zone ist eine _Beam_-Zone, es gibt aber auch _Canvas_-Zonen und _DMX_-Zonen. In dieser Anleitung konzentrieren wir uns hauptsächlich auf Beam-Zonen, die normalerweise verwendet werden, um atmosphärische Beam-Effekte in der Luft zu erzeugen.
{% endhint %}

Du kannst den Laser, den du bearbeiten möchtest, auf eine dieser Arten auswählen:

* über die nummerierten Buttons in der Leiste oben
* indem du die Zahlentaste für den gewünschten Laser drückst _(1-9_ keys\_)\_
* mit der Taste `Tab`, um nacheinander durch die Laser zu wechseln

Füge dem Setup einen neuen Laser hinzu, indem du den Button _+_ drückst. (Es gibt außerdem einen Button _ADD LASER_ im Panel _Laser Overview_)

Lösche einen Laser aus dem Setup, indem du im Panel _Laser Overview_ den roten Button ⊖ drückst.

Du kannst mit dem Mausrad hinein- und herauszoomen und überall dort klicken und ziehen, wo keine Zone liegt, um die Ansicht zu verschieben.

Klicke auf eine Zone, um sie auszuwählen, und passe dann ihre Eckpunkte mit der Maus an. Halte beim Ziehen einer Ecke die Taste `Alt / Option` gedrückt, um sie nicht proportional zu verändern. Klicke mit der rechten Maustaste auf die Zone, um weitere Optionen zu sehen, einschließlich der Änderung des Zonentyps.

Links befindet sich eine Leiste mit mehreren Icon-Buttons. Fahre mit der Maus über einen Button, um eine Beschreibung seiner Funktion zu sehen. Mit den Buttons hier kannst du Beam-Zonen, Canvas-Zonen und Masken hinzufügen. Außerdem gibt es Optionen, um nur für diesen Laser ein Test Pattern festzulegen, sowie Grid- und Snapping-Einstellungen.

Weitere Details findest du unter [Output-Ansicht](output-view/ "mention").

#### Canvas

Das Canvas-System wird hauptsächlich für Grafik und Architektur-Mapping verwendet. Du kannst komplexe Bilder auf mehrere Laser verteilen und jeden Abschnitt perspektivisch korrigieren. Siehe [Grafiken und das Canvas-System](graphics-and-the-canvas-system/ "mention").

### APC40 MIDI-Controller

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Du kannst Liberation zwar mit Maus und Tastatur steuern, deutlich besser ist jedoch ein APC40 MIDI-Control-Interface (Mark 2 ist am besten, Mark 1 funktioniert aber ebenfalls).

Siehe auch: [APC40-Referenz](reference/apc40-reference.md "mention")

Wir haben inzwischen auch Unterstützung für APC Mini Mark 2 und MIDI Fighter Twister implementiert, weitere Controller sind in Entwicklung. Für die meisten Fälle ist der APC40 Mark 2 jedoch die beste Option.

### Clips und Effekte

{% hint style="info" %}
**Was ist ein Clip?**

Ein Clip ist ein Container für beliebigen Laser-Content innerhalb von Liberation. Clips können Beams oder grafische Animationen enthalten und sind normalerweise eine Loop-Sequenz. Sie können in jede Zone (oder _Canvas target area_) geleitet werden und werden über die Clip-Buttons im Clip Deck ausgelöst.
{% endhint %}

#### Überblick über das Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Dieses Raster wird _Clip Deck_ genannt und ist der Ort, an dem alle Laser-Clips gespeichert sind. Es ist so gestaltet, dass es direkt dem 8 x 5 Button-Raster deines APC40 entspricht.

**Durch das Clip Deck navigieren.**

Du kannst das Clip Deck nach links und rechts scrollen mit:

* linker und rechter Pfeiltaste. Füge `Cmd / Ctrl` hinzu, um jeweils eine ganze Seite zu scrollen.
* Trackpad: Wischen
* Maus: Wenn deine Maus seitliches Scrollen unterstützt, kannst du das verwenden, während der Mauszeiger über dem Clip Deck ist.
* APC40-Scroll-Regler
* APC40-Buttons _<- DEVICE ->_

Zur Orientierung gibt es oben eine Mini-Visualisierung des Clip Decks. Siehe auch [Clips & Clip Deck](clips/ "mention")

#### Clips starten und stoppen

Drücke einen Clip-Button (entweder mit der Maus oder mit dem APC40), um einen Clip zu starten. Drücke ihn erneut, um ihn zu stoppen. Wenn du einen Clip startest, stoppen alle anderen Clips derselben Farbe automatisch, es sei denn, du hältst _shift_ gedrückt.

Einige Clips befinden sich im _Flash mode_ (standardmäßig die roten). In diesem Fall stoppen sie, sobald du den Clip-Button loslässt.

Der Button _STOP_ stoppt alle aktuell laufenden Clips.

#### Output-Zonen für den Clip festlegen

Unterhalb der Clip-Buttons siehst du die Zonen-Buttons, standardmäßig Beam-Zonen 1 bis 8 (_BEAM 1_, _BEAM 2_ usw.). Die Zonen-Buttons leuchten auf, um anzuzeigen, welche Zonen dem aktuell ausgewählten Clip zugewiesen sind.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Zwei Reihen unter den Zonen-Buttons siehst du die X/Y-Flip-Buttons. Schalte diese um, um den Clip horizontal und vertikal zu spiegeln.

{% hint style="info" %}
Beachte, dass diese Zonenzuweisungen und X/Y-Flip-Einstellungen mit dem Clip selbst verbunden sind. Sie bleiben erhalten, wenn du diesen Clip das nächste Mal startest. Sie sind keine globale Einstellung.
{% endhint %}

Klicke mit der rechten Maustaste auf einen Clip, um weitere Einstellungen für den Clip zu bearbeiten. Siehe auch [Clip-Einstellungen](clips/clip-settings.md "mention")

### Gruppen

Du wirst bemerken, dass jeder Clip eine farbige Umrandung hat. Diese Farbe zeigt an, zu welcher _Gruppe_ er gehört. Auch die APC40-Clip-Buttons leuchten in dieser Farbe.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyan</td></tr><tr><td>Group 2</td><td>Orange</td></tr><tr><td>Group 3</td><td>Red</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Green</td></tr></tbody></table>

Das Gruppensystem ist sehr flexibel und ermöglicht dir:

* Clips in einer Gruppe weiterlaufen zu lassen, während du Clips in einer anderen Gruppe umschaltest
* Zonen und X/Y-Flips schnell allen Clips innerhalb einer Gruppe zuzuweisen
* den _Flash mode_ für einen Clip festzulegen (Group 3 ist standardmäßig auf _Flash mode_ eingestellt)

Gruppen haben außerdem Einstellungen für Transition in/out, die von ihren Clips übernommen oder überschrieben werden können.

Du kannst die Gruppe eines Clips über die Buttons im Rechtsklick-Menü zuweisen. Oder du nutzt den APC40: Drücke den Group-Button und drücke, _während er weiterhin gehalten wird,_ die Clip-Buttons.

Zoneneinstellungen für alle Clips innerhalb einer Gruppe ändern

Drücke auf dem APC40 den Group-Button und verwende dann, _während er weiterhin gehalten wird,_ die Zonen- und X/Y-Buttons, um die Zoneneinstellungen für alle Clips in dieser Gruppe umzuschalten.

Siehe auch [Clip-Gruppen](clips/groups.md "mention")

### Effekte

Das Effektsystem in Liberation ist eine leistungsstarke und vielseitige Möglichkeit, den Clip-Output in Echtzeit zu verändern. Die Standard-Effect-Buttons 1–8 befinden sich unter den Zonen-Buttons.

#### Einen Effekt anwenden

Drücke einen Effect-Button, um den Effekt umzuschalten. Noch besser ist es, die APC40-Slider 1–8 zu verwenden, um Effekte ein- und auszublenden.

#### Effektparameter

Verwende die Rotary-Controller 1–8\*, um den _Parameter_ jedes Effekts anzupassen. (Oder du kannst mit der rechten Maustaste klicken, um Level und Parameter anzupassen.) Die Parameteränderung bewirkt je nach Einrichtung des Effekts unterschiedliche Dinge. Die Standard-Effekte findest du in der folgenden Liste.

{% hint style="info" %}
Die kleinen Zahlen auf den Effect-Buttons beziehen sich auf _Level_ und _Parameter_ des Effekts. Das _Level_ wird über den Fader auf dem APC40 gesteuert, oder du kannst auf dem Button klicken und ziehen. Der Parameter wird über die Rotarys auf dem APC40 angepasst, oder du kannst ihn per Rechtsklick mit der Maus ändern.
{% endhint %}

_\*Rotary-Controller 1–8 befinden sich beim APC40 Mk2 oben und beim Mk1 oben rechts. Siehe auch:_ [APC40-Referenz](reference/apc40-reference.md "mention")

#### Die Standard-Effekte

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Wendet eine chaotische Bewegung auf den Clip-Output an. Der Parameter steuert Stärke/Geschwindigkeit des Chaos.
2. **Sine wave** :\
   Verformt den gesamten Content entlang einer bewegten Sinuswelle. Der Parameter steuert die Wellenlänge.
3. **Rotation** :\
   Dreht alles um den Mittelpunkt. Der Parameter steuert die Drehgeschwindigkeit.
4. **Horizontal flip** :\
   Staucht und streckt alles horizontal. Der Parameter steuert die Geschwindigkeit.
5. **Scale** :\
   Skaliert alles wiederholt von voller Größe auf null. Der Parameter steuert die Geschwindigkeit.
6. **Hue** :\
   Ändert den Farbton von allem, aber nicht die Sättigung (d. h. alles Weiße bleibt weiß). Der Parameter steuert den Farbton.
7. **Saturation and hue** :\
   Ändert den Farbton von allem und sättigt die Farbe zusätzlich vollständig (d. h. alles Weiße wird zur Farbe). Der Parameter steuert den Farbton.
8. **Flash** :\
   Lässt die Helligkeit von allem wiederholt von voll auf null blitzen. Der Parameter steuert die Flash-Geschwindigkeit.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

In der unteren Reihe gibt es weitere 16 Farbeffekte, mit denen du voreingestellte Hue- und Saturation-Werte anwenden kannst.

Beachte, dass dies die Standard-Effekte sind. Sie können jedoch so bearbeitet werden, dass sie fast alles tun, was du möchtest!

#### Was ist der _„aktuell ausgewählte Clip“_?

Wenn du einen Clip startest, leuchtet er auf, um anzuzeigen, dass er aktiv ist. Außerdem hat er eine weiße Umrandung. Diese zeigt an, dass dies der aktuell _ausgewählte_ Clip ist. Immer wenn du Zonen-Buttons umschaltest oder Clip-Einstellungen anpasst, werden diese auf den _aktuell ausgewählten Clip_ angewendet.

{% hint style="info" %}
Um einen Clip auszuwählen, ohne ihn auszulösen, drücke die Taste `Alt / Option`, bevor du den Clip-Button drückst. Das ist eine gute Möglichkeit, seine Zonen und andere Einstellungen anzupassen, ohne ihn laufen zu lassen.
{% endhint %}

### Panel Clip Settings

Verwende das Panel _Clip Settings_, um Skalierung und X/Y-Position zu bearbeiten und auf das leistungsstarke Zone-Delay-System zuzugreifen.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

Im Panel _Global Settings_ kannst du globale Output-Einstellungen anpassen, die alle Ausgaben über alle Zonen hinweg beeinflussen.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Aktiviere AUTO RESET, um alle _Global settings_ automatisch zurückzusetzen, sobald keine Clips mehr laufen.

### Timing

Fast alle Laser-Shows haben eine Art musikalischen Soundtrack, daher basiert das Timing-System in Liberation auf einem Tempo in Beats per Minute. Im _Tempo Panel_ siehst du eine Darstellung der Zeit. Jedes Quadrat steht für einen Beat, und du siehst sie im Takt blinken.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Es gibt mehrere Synchronisationsoptionen, darunter MIDI Clock und Ableton Link. Wenn du das Tempo der Musik kennst, kannst du es manuell mit dem Bildschirm-Slider oder dem APC40 Tempo-Regler anpassen. Du kannst aber auch mit dem _Tap Tempo_-System\_ im Takt der Musik bleiben.\_

#### Tap Tempo

_Tap Tempo_ ist ein Begriff, der häufig in Musik-Apps verwendet wird. Damit kannst du während der laufenden Musik im Takt tippen, um das Tempo festzulegen. Du kannst den Button auf dem Bildschirm verwenden, empfohlen wird jedoch die Taste _T_ oder der Button _Tap Tempo_ auf dem APC40 (oder sogar ein Fußschalter, wenn dir das lieber ist).

Drücke die Taste _R_ oder den Button _Metronome_ (APC40), um das Tempo auf den Anfang des Takts zurückzusetzen.

Drücke die Taste _Y_ oder drehe den _Tempo_-Regler (APC40), um das Tempo auf eine ganze Zahl zu runden. Das kann bei elektronischer Musik nützlich sein, die oft eine glatte Anzahl von Beats per Minute hat.

### Dein Clip Deck organisieren

Um einen Clip in deinem Clip Deck zu verschieben, klicke ihn an und ziehe ihn an eine neue Position. Während des Ziehens kannst du die Pfeiltasten (oder das Scrollrad/die Scroll-Buttons auf deinem APC40) verwenden, um nach links und rechts zu scrollen.

Halte beim Ziehen die Taste `Alt / Option` gedrückt, um eine Kopie zu erstellen.

Klicke mit `Alt / Option` auf einen Clip, um ihn auszuwählen, ohne ihn zu starten.

Klicke mit `Alt / Option + Shift` auf einen Clip, um mehrere Clips auszuwählen, oder klicke und ziehe außerhalb eines Clips, um per „Lasso“ auszuwählen.

Klicken und Ziehen verschiebt ALLE ausgewählten Clips.

Um einen oder mehrere Clips zu löschen, ziehe sie entweder aus dem Clip Deck heraus (ein Papierkorb-Symbol erscheint) oder verwende den Button DELETE im Rechtsklick-Menü des Clips.

### Panel Laser Overview

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Das Panel _Laser Overview_ gibt dir einen schnellen Überblick über den Status deiner aktuell laufenden Laser. Das grüne Quadrat rechts zeigt an, dass der Laser-Controller einwandfrei arbeitet. Wenn es orange wird, treten gelegentliche Drop-outs auf, und wenn es rot ist, wurde die Verbindung getrennt. Wenn es grau ist, ist überhaupt kein Controller verbunden.

Das Diagramm in der Mitte zeigt den Verlauf der Frame-Längen, und die Zahl rechts ist die aktuelle Framerate. Je komplexer der Content, desto niedriger wird die Framerate sein (d. h. desto stärker kann es flackern). Alles unter etwa 25 fps beginnt etwas flackernd auszusehen.

### Verbindung zu Lasern herstellen – Panel Controller Assignment

Klicke auf den Button _Assign Laser Controllers_, um das Panel _Controller Assignment_ zu öffnen. (Dieses Panel ist auch über _View -> Controller Assignment_ in der Menüleiste erreichbar.)

Hier kannst du auswählen, welche Laserausgänge an welche Laser-Controller gesendet werden. Ziehe Controller per Drag-and-drop aus der Liste rechts in die Slots links. Du kannst deine Controller umbenennen, damit sie zu dem Laser passen, mit dem sie gekoppelt sind (verwende den Button mit dem Stift-Symbol).

Weitere Details findest du im Kapitel [Controller-Zuweisung](setting-up/controller-assignment.md "mention").

{% hint style="danger" %}
Bevor du Laser aktivierst, arbeite unbedingt das Kapitel [Überblick über den Laser-Einrichtungsprozess](setting-up/setting-up-lasers.md "mention") durch.
{% endhint %}

### Panel Laser Output

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Dieses Panel zeigt dir die Einstellungen für den _aktuell ausgewählten Laser_ (dargestellt durch die Zahl oben). Du änderst den aktuell ausgewählten Laser mit der Taste _tab_, durch Drücken einer Zahlentaste, durch Klicken auf eine Lasernummer im Panel _Laser Overview_ oder in der _Output_-Ansicht.

* **Number button** aktiviert und deaktiviert den Laser. Wenn er rot ist, ist der Laser aktiviert.
* **Brightness** passt die Laserhelligkeit unabhängig von den anderen Lasern an (und wird mit der Einstellung _global brightness_ kombiniert – d. h. wenn beide bei 50 % stehen, liegt dein Laser bei 25 %).
* **Test Pattern** schaltet nur für diesen Laser ein Test Pattern ein (überschreibt die globale Test-Pattern-Einstellung).
* **Orientation** korrigiert Laser, die seitlich oder kopfüber montiert sind.
* **Flip Horizontal and Flip Vertical** kehrt den Ausgang des Lasers um. Nützlich zur Output-Korrektur bei uneinheitlich verdrahteten Lasern.
* **Copy Laser Settings** öffnet ein Panel, mit dem du verschiedene Einstellungen von diesem Laser auf andere kopieren kannst.

### Scanner-Einstellungen

Showlaser funktionieren, indem ein einzelner Laserstrahl extrem schnell bewegt und ein- und ausgeschaltet wird, um Formen in die Luft zu zeichnen. Was du als Linien, Formen und Bilder siehst, ist in Wirklichkeit der Strahl, der Pfade schneller abfährt, als deine Augen folgen können.

Ein Point Stream sind die Daten, die dem Laser sagen, wohin er sich als Nächstes bewegen soll und wann der Strahl ein- oder ausgeschaltet sein soll. In Liberation werden Clips in Echtzeit in diesen Point Stream umgewandelt, während sie an die Laser gesendet werden.

Liberation gibt dir detaillierte Kontrolle darüber, wie dieser Point Stream erzeugt wird. So kannst du für jeden Laser Laufruhe, Helligkeit und Performance ausbalancieren.

{% hint style="info" %}
Wenn du ältere Lasersoftware gewohnt bist, die auf vorberechneten Point Streams basiert, kann sich dieser Ansatz zunächst anders anfühlen. Die Point-Generierung in Echtzeit ermöglicht jedoch, denselben Content für jeden Laser unterschiedlich zu optimieren. Dadurch wird es einfacher, mit mehreren Lasern zu arbeiten, die unterschiedliche Scanner-Geschwindigkeiten oder Qualitätsstufen haben, ohne Content zu duplizieren oder neu aufzubauen. Außerdem bleiben Clip-Dateien sehr klein. Deshalb ist das gesamte standardmäßige Liberation Clip Deck nur wenige Megabyte groß statt Gigabyte.
{% endhint %}

Die grundlegenden Scanner-Einstellungen sind:

* **Speed** ist die Scanner-Geschwindigkeit, also wie schnell sich der Laser bewegt, um Formen zu zeichnen. Das entspricht dem Anpassen der Point Rate in herkömmlicher Lasersoftware, aber in Liberation kannst du ändern, wie schnell sich der Laser bewegt, _unabhängig von der Point Rate._ Du solltest das normalerweise nicht anpassen müssen.
* **Scanner sync** (manchmal auch _blank shift_ genannt, früher Colour Shift) Die Scanner bewegen den Laser sehr schnell, aber normalerweise ist die Änderung von Helligkeit und Farbe nicht mit der Bewegung synchron. Das zeigt sich als kleine flackernde „Schweife“ aus Licht am Rand von Beams und Linien. Verwende diese Einstellung, um Bewegung und Farbe miteinander zu synchronisieren. Siehe [Laser-Ausgabe-Einstellungen](setting-up/laser-settings.md "mention")

Die weiteren erweiterten Scanner-Einstellungen werden im Kapitel [Fortgeschrittene Funktionen](advanced/ "mention") behandelt.

### Zoning

Eine vollständige Anleitung zum Einrichten und Zoning von Lasern findest du hier: [Überblick über den Laser-Einrichtungsprozess](setting-up/setting-up-lasers.md "mention")
