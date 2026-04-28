---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation unterstützt die Synchronisation mit einem externen SMPTE/LTC-Timecode-Signal. Das wird häufig bei Live-Musikshows verwendet, um Licht, Pyro, Video und Backing-Tracks synchron zu halten.

{% hint style="info" %}
Was ist SMPTE/LTC?

SMPTE ist ein Standard für Timecode, und LTC ist dieser Timecode, der in ein Audiosignal umgewandelt wurde. Wenn du dir dieses Audiosignal anhörst, klingt es wie ein furchtbares, hochfrequentes Quietschen, für Computer enthält es aber hochauflösende Timing-Informationen.

**Nerd-Fakten!**

Historisch wurde SMPTE verwendet, um Video und Audio synchron zu halten. Beim Synchronisieren mit analogem Band wurde eine Spur mit dem Timecode-Audio bespielt, was manchmal als „Striping“ des Bands bezeichnet wurde. Diese Timecode-Spur konnte verwendet werden, um mehrere Bandmaschinen miteinander synchron zu halten oder einen MIDI-Sequenzer mit dem Band zu synchronisieren. (So musstest du MIDI-Instrumente nicht auf Band aufnehmen, sondern konntest den Sequenzer sie beim Mischen einfach live abspielen lassen!)

SMPTE steht für Society of Motion Picture and Television Engineers, die den Standard definiert haben. LTC steht für _Linear TimeCode._
{% endhint %}

Du kannst ein LTC-Timecode-Signal über jedes Audio-Interface an deinem Computer empfangen. Empfohlen wird aber ein professionelles Interface mit mindestens einem regelbaren XLR-Eingang und einer Monitoring-Funktion.

Ich habe gute Erfahrungen mit dem [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) gemacht, da es Kopfhörer-Monitoring, 2 XLR-Eingänge hat und keine speziellen Treiber benötigt (zumindest unter macOS). Wenn du es ausschließlich für Timecode verwenden willst, kannst du das etwas günstigere [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) nehmen (es hat nur einen Eingang und kein MIDI). Ehrlich gesagt sollte aber jedes halbwegs ordentliche Audio-Interface funktionieren.

{% hint style="info" %}
LTC-Timecode-Signale werden typischerweise über symmetrische XLR-Kabel verteilt, da sie robust genug sind, um Audiosignale mit niedrigem Pegel über lange Strecken zu übertragen. (XLR ist der runde Steckverbinder, der normalerweise bei Mikrofonen verwendet wird.)
{% endhint %}

### Hardware-Verbindungen

Stecke das XLR-Kabel mit dem Timecode-Signal in dein Audio-Interface und stelle sicher, dass du ein gutes Signal bekommst. Passe den Pegel am Audio-Interface so an, dass er kräftig ist, aber nicht übersteuert. Wenn dein Audio-Interface einen Kopfhöreranschluss hat, kannst du den Timecode abhören und prüfen, ob er nicht aussetzt und nicht zu stark rauscht.

{% hint style="info" %}
Theoretisch ist es möglich, das Signal über die Klinkenbuchse deines MacBook zu empfangen, dafür wäre aber ein spezielles Kabel nötig. Diese Buchsen sind typischerweise 4-polige TRRS-Miniklinken, und ich bin ehrlich gesagt nicht sicher, welche dieser Kontakte für einen Audioeingang verwendet werden können. Außerdem bin ich nicht sicher, welchen Spannungspegel sie vertragen (ich habe irgendwo gelesen, es seien +/-1V, aber nutze das auf eigene Gefahr!).

Ich denke, du bist besser dran, wenn du dir einfach ein günstiges USB-Audio-Interface besorgst, statt das zu versuchen.
{% endhint %}

Wenn dein Audio-Interface keine Art von Input-Monitoring hat, kannst du in den macOS-Systemeinstellungen (unter _Sound_) prüfen, ob ein Signal ankommt. (Unter Windows verwendest du das _Sound Control Panel_.)

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS zeigt dir den Eingangspegel für jedes Audio-Interface im Bereich Sound der Systemeinstellungen an</p></figcaption></figure>

### Einrichtung in Liberation

1. Wähle dein Audio-Interface und den richtigen Eingangskanal im Timecode-Einstellungsfenster aus.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Beachte, dass es im Dropdown-Menü separate Optionen für jeden Eingangskanal deines Audio-Interfaces gibt.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Achte auf das Quadrat links: Wenn du ein gültiges Timecode-Signal empfängst, wird es grün. Wenn nicht, bleibt es rot.

2. Wähle die richtige Framerate für den eingehenden Timecode aus. Die Person, die dir den Timecode liefert, sollte dir sagen können, welche Framerate verwendet wird. (Wenn du sie falsch einstellst, synchronisiert es trotzdem, aber du wirst jede Sekunde einen kleinen „Sprung“ bemerken.)
3. Öffne die Timecode-Einstellungen der Timeline über das kleine Uhrsymbol in der Timeline-Leiste und wähle die Option SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Passe den Start-Offset (in Stunden, Minuten, Sekunden, Frames) so an, dass er zum Start des Songs passt. Wenn du mehrere Timelines hast, musst du diese Optionen für jede einzeln einstellen.

{% hint style="info" %}
In der Touring-Welt ist es üblich, jeden Song zu einer anderen Stunde starten zu lassen, z. B. 01:00:00:00 für den ersten Song, 02:00:00:00 für den zweiten Song und so weiter.

Liberation wechselt abhängig vom Timecode automatisch zur passenden Timeline, du musst Timelines während einer Show also nie manuell wechseln.
{% endhint %}

Beachte, dass SMPTE im Gegensatz zu MIDI Clock und Ableton Link ein _absolutes_ Zeitsystem ist, das in Stunden, Minuten, Sekunden und Frames gemessen wird. Das zentrale Zeitsystem von Liberation basiert auf Beats und Takten. Wenn Timecode empfangen wird, verwendet Liberation daher das Tempo, das in der Timeline eingestellt ist. Du musst sicherstellen, dass dieses Tempo mit der Musik synchron ist, die ebenfalls zum Timecode synchronisiert ist.
