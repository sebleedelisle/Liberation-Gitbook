---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / synchronisatie

Muzieksynchronisatie is een fundamenteel onderdeel van Liberation. Zodra het tempo en de beats gelijklopen met de muziek, weet je zeker dat alles synchroon blijft. Als je het geluk hebt dat je MIDI clock (of Ableton Link) kunt gebruiken, hoef je je helemaal geen zorgen te maken over handmatig synchroniseren. Zo niet, geen probleem: je kunt handmatig gelijklopen met de _Live_ tempo-functie.

Als je ervaring hebt met muziek- of lichtsoftware, zal dit proces je bekend voorkomen. Zo niet, dan is het de moeite waard om wat tijd te nemen om het systeem te leren kennen en thuis te oefenen voordat je naar een liveshow gaat.

## Tempo-paneel

Het _Tempo_-paneel staat altijd op het scherm en bevat alle synchronisatie-instellingen. Bovenaan zie je de huidige maat-/tel-teller en transportbediening met knoppen voor play/pause en terugspoelen/vooruitspoelen.

Daaronder zie je de beat marker: vier vierkanten die op de beat “pulseren”. Deze _beat marker_ is een bijzonder handige visualisatie en je zult er voortdurend naar kijken wanneer je het _Live_ tempo-systeem gebruikt.

### Het tempo instellen

Je hebt verschillende opties om het tempo in te stellen:

* Klik en sleep op de _Tempo_-slider
* Shift-klik en sleep op de _Tempo_-slider om het tempo in stappen van 0,1 te wijzigen
* Dubbelklik op de _Tempo_-slider en typ het getal handmatig
* Gebruik de _Tempo_-knop op de APC40 (druk op shift voor stappen van 0,1)
* Tap Tempo

{% hint style="info" %}
Tempo wordt gedefinieerd in “beats per minute” en de traditionele standaardwaarde is meestal 120.
{% endhint %}

## Tap Tempo

Stel het tempo automatisch in door de _TAP_-knop in de maat van de beat aan te klikken. Stel het begin van de maat in met de _RESET_-knop.

{% hint style="info" %}
Het Tap Tempo-systeem is slim genoeg om te herkennen of je een tijdje bent gestopt met tikken, of als je een paar beats hebt gemist. Als je in dubbele snelheid begint te tikken, begrijpt het systeem dat je het tempo wilt verdubbelen. Hetzelfde geldt als je in half tempo tikt.

Het is ook slim genoeg om te herkennen of twee mensen tegelijk tempo tikken (bijvoorbeeld één op het toetsenbord en één op de APC40). Liberation middelt de dubbele tikken uit.
{% endhint %}

#### Toetsenbordcommando’s:

T - tap tempo\
R - reset de maat\
Y - rond het tempo af naar de dichtstbijzijnde beat per minute.

{% hint style="info" %}
Omdat de meeste muziek tegenwoordig digitaal wordt gemaakt, is het tempo waarschijnlijk een afgerond heel getal. Dus als een getapt tempo ongeveer klopt, gebruik dan de Y-toets (of draai de APC40-tempo-knop één “tik”) om het af te ronden naar een heel getal.
{% endhint %}

#### APC40-bediening:

De APC40 heeft een speciale _TAP TEMPO_-knop, maar je kunt ook een aangesloten voetschakelaar gebruiken om met je voet te tikken!

Gebruik de _TEMPO_-knop om aan te passen. Druk op _SHIFT_ terwijl je de _TEMPO_-knop gebruikt voor fijne aanpassingen.

Gebruik de _METRONOME_-knop om **de maat te resetten**. (Let op: de _METRONOME_-knop licht ook op in de maat van de beat)

Draai de _TEMPO_-knop één “tik” naar rechts of links om **het tempo af te ronden** naar boven of beneden naar een heel BPM-getal.

Zie ook [APC40-referentie](reference/apc40-reference.md "mention")

### Tempo nudgen

Als je zeker weet dat je dicht genoeg bij het werkelijke tempo zit, maar merkt dat je uit de maat begint te lopen, gebruik dan de _NUDGE_-knoppen om te corrigeren.

Als het Liberation-tempo voorloopt op de muziek, houd je _NUDGE -_ ingedrukt om tijdelijk te vertragen totdat het weer gelijkloopt.

Als het Liberation-tempo achterloopt op de muziek, houd je _NUDGE +_ ingedrukt om tijdelijk te versnellen totdat het weer gelijkloopt.

{% hint style="info" %}
Je kunt zowel de NUDGE-knoppen op het scherm gebruiken als de speciale knoppen op de APC40.
{% endhint %}

### Half time / double time

Gebruik de _÷2_- en _x2_-knoppen om het tempo permanent te halveren of te verdubbelen. In tegenstelling tot de tempo multiplier is dit een permanente wijziging van het huidige tempo.

## Tempo Multiplier

Met het _Tempo Multiplier_-systeem kun je het tempo tijdelijk aanpassen voordat je terugkeert naar de eerdere waarde.

Schakel de _Tempo Multiplier_ in of uit met de _TEMPO MULTIPLIER_-knop of de _BANK_-knop op de APC40. Pas aan met de slider op het scherm of met de APC40 A-B-slider. Of gebruik de preset-knoppen _25%, 50%, 100% 200%_.

## Externe tempo-bronnen

### MIDI Clock

Om te synchroniseren met een extern MIDI clock-signaal, selecteer je de _MIDI CLOCK_-radioknop en kies je het MIDI-apparaat in het dropdownmenu. Let op het gekleurde statuslampje naast de dropdownmenu’s:

* Groen - ontvangt een MIDI clock-signaal
* Oranje - kan verbinding maken met het MIDI-apparaat, maar er is momenteel geen clock-signaal
* Rood - kan geen verbinding maken met het MIDI-apparaat

{% hint style="info" %}
MIDI Clock zendt een reeks frames uit (24 per kwartnoot), maar de berichten bevatten geen positiegegevens. Dit betekent dat het handig is om in de maat te blijven, maar dat je de maat mogelijk nog steeds moet resetten.

De Liberation MIDI Clock-tempo-bron reageert ook op **MIDI Machine Control (MMC)**-berichten, dus als je clock-bron deze verzendt, hoef je de maat niet handmatig te resetten.
{% endhint %}



### Timeline

Elke timeline heeft een eigen tempo. Dit kan een vaste waarde zijn of een _Tempo Map_. Met de _Tempo Map_ kun je het tempo op specifieke momenten binnen de timeline aanpassen.

Het timeline-tempo wordt gebruikt wanneer _TIMELINE_ is geselecteerd als tempo-bron.

{% hint style="info" %}
Je kunt een timeline samen met _elke_ tempo-bron laten lopen! Dus als je een liveband hebt die niet op een click speelt, kun je de timeline handmatig starten en synchroon houden met de _LIVE_ tempo-bron. Of als je een MIDI clock-signaal hebt, kun je dat gebruiken!
{% endhint %}
