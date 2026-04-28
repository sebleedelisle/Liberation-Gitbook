---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation ondersteunt synchronisatie met een extern SMPTE/LTC-timecodesignaal. Dit wordt vaak gebruikt bij livemuziekshows om licht, pyro, video en backingtracks gelijk te laten lopen.

{% hint style="info" %}
Wat is SMPTE/LTC?

SMPTE is een standaard voor timecode, en LTC is deze timecode omgezet naar een audiosignaal. Als je naar deze audio luistert, klinkt het als een vreselijk hoog piepend geluid, maar voor computers is het timinginformatie met hoge resolutie.

**Nerdfeitjes!**

Historisch gezien werd SMPTE gebruikt om video en audio synchroon te houden. Bij synchronisatie met analoge tape werd de timecode-audio op één spoor opgenomen, wat soms "striping" van de tape werd genoemd. Je kon dit timecodespoor gebruiken om meerdere tapedecks met elkaar gelijk te laten lopen, of om een MIDI-sequencer synchroon te houden met de tape. (Zo hoefde je MIDI-instrumenten niet op tape op te nemen; je kon de sequencer ze gewoon live laten afspelen terwijl je aan het mixen was!)

SMPTE staat voor Society of Motion Picture and Television Engineers, de organisatie die de standaard heeft gedefinieerd. LTC staat voor _Linear TimeCode._
{% endhint %}

Je kunt een LTC-timecodesignaal ontvangen via elke audio-interface op je computer, maar het is aan te raden om een professionele interface te gebruiken met minstens één instelbare XLR-ingang en monitoringmogelijkheid.

Ik heb goede ervaringen met de [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), omdat deze hoofdtelefoonmonitoring heeft, 2 XLR-ingangen en geen speciale drivers nodig heeft (in ieder geval op macOS). Als je hem alleen voor timecode gaat gebruiken, kun je de iets goedkopere [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) nemen (die heeft maar één ingang en geen MIDI), maar eerlijk gezegd zou elke redelijk goede audio-interface moeten werken.

{% hint style="info" %}
LTC-timecodesignalen worden meestal via gebalanceerde XLR-kabels verdeeld, omdat die robuust genoeg zijn om audiosignalen op laag niveau over lange afstanden te verzenden. (XLR is de ronde connector die meestal met microfoons wordt gebruikt)
{% endhint %}

### Hardware-aansluitingen

Sluit de XLR-kabel met het timecodesignaal aan op je audio-interface en controleer of je een goed signaal binnenkrijgt. Stel het niveau op de audio-interface zo af dat het signaal sterk is, maar niet clipt. Als je audio-interface een hoofdtelefoonaansluiting heeft, kun je naar de timecode luisteren en controleren of het signaal niet hapert en niet te veel ruis bevat.

{% hint style="info" %}
In theorie is het mogelijk om het signaal via de jackaansluiting op je MacBook te ontvangen, maar daarvoor heb je een aangepaste kabel nodig. Deze aansluitingen zijn meestal 4-polige TRRS-minijacks, en eerlijk gezegd weet ik niet zeker welke van deze contacten als audio-ingang gebruikt kunnen worden. Ik weet ook niet zeker welk spanningsniveau ze aankunnen (ik heb ergens gelezen dat het +/-1V was, maar gebruik dit op eigen risico!)

Ik denk dat je beter gewoon een goedkope USB-audio-interface kunt gebruiken dan dit te proberen.
{% endhint %}

Als je audio-interface geen enkele vorm van input monitoring heeft, kun je in de systeeminstellingen van macOS (onder _Sound_) controleren of je een signaal binnenkrijgt. (Gebruik op Windows het _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS toont het ingangsniveau voor elke audio-interface in het systeeminstellingenpaneel Sound</p></figcaption></figure>

### Instellen in Liberation

1. Selecteer je audio-interface en het juiste ingangskanaal in de Timecode settings Window.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Let op: in het dropdownmenu staan aparte opties voor elk ingangskanaal van je audio-interface

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Let op het vierkant links: als je een geldig timecodesignaal ontvangt, wordt dit groen. Zo niet, dan blijft het rood.

2. Selecteer de juiste framerate voor de binnenkomende timecode. Degene die je de timecode levert, zou je moeten kunnen vertellen wat de framerate is. (Als je dit verkeerd instelt, blijft de synchronisatie werken, maar merk je elke seconde een kleine "skip")
3. Open de timecode-instellingen van de Timeline met het kleine klokpictogram op de timeline-balk en kies de optie SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Stel de start offset in (in uren, minuten, seconden, frames) zodat die overeenkomt met het begin van het nummer. Als je meerdere timelines hebt, moet je deze opties voor elke timeline apart instellen.

{% hint style="info" %}
In de tourwereld is het een gebruikelijke conventie om elk nummer op een ander uur te laten starten, bijvoorbeeld 01:00:00:00 voor het eerste nummer, 02:00:00:00 voor het tweede nummer, enzovoort.

Liberation schakelt automatisch over naar de timeline op basis van de timecode, dus je hoeft tijdens een show nooit handmatig van timeline te wisselen.
{% endhint %}

Let op: in tegenstelling tot MIDI Clock en Ableton Link is SMPTE een _absoluut_ tijdsysteem, gemeten in uren, minuten, seconden en frames. Het kern-tijdsysteem van Liberation is gebaseerd op beats en maten, dus wanneer je timecode ontvangt, gebruikt Liberation het tempo dat in de timeline is ingesteld. Je moet ervoor zorgen dat dit tempo synchroon loopt met de muziek die ook aan de timecode is gekoppeld.
