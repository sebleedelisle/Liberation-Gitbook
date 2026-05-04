---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 MIDI-styrenheter för livekontroll

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40-kontroller**

Det här är standardkontrollern för Liberation. Den rekommenderas starkt, och det är rimligt att säga att Liberation har designats kring den här hårdvaran från allra första början. Så snart du kopplar in APC40 ansluter Liberation automatiskt till den direkt.

{% hint style="warning" %}
_Åh nej! Min USB-kontakt drogs ur mitt under en show!_

Ingen panik – koppla bara in den igen. Liberation återansluter automatiskt, utan krångel.
{% endhint %}

### APC40 Mark 1 eller Mark 2?

Kort sagt rekommenderas Mark 2, eftersom den har knappar i full färg som bättre matchar Liberation Clip Deck-gränssnittet. Mark 1-versionen fungerar om det behövs, men den blir lite mer förvirrande eftersom layouten skiljer sig något från det som visas på skärmen, och knapparna kan bara lysa rött, orange eller grönt, så de matchar inte klippens färger.

{% hint style="info" %}
Den ursprungliga APC40 Mark 1 kom ut 2009(!), och vissa föredrar den fortfarande för dess metallkonstruktion och robusta, konsolliknande format. Den uppdaterade Mark 2 kom ut 2014, och även om den slutade tillverkas 2024 sätts den i produktion igen 2025 på grund av efterfrågan från visual-artister (Resolume med flera) och laserister.
{% endhint %}

En komplett lista över de kontroller som finns på APC40 finns i [APC40-referens](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 innehåller även en profil för APC Mini. Den mappar rutnätet med Clips (8x5), knappar för zones, reglage för X/Y-vändning av zones, gruppknappar, stoppa alla Clips, sidförflyttning för Clips, sidförflyttning för zones, tap tempo, taktåterställning och tempojustering. Dess faders styr effektnivåer, och faders som används med Shift styr effektparametrar. Den sista fadern styr Global Brightness.

### MIDI Fighter Twister

Profilen för MIDI Fighter Twister är avsedd för kontroll med många encoders snarare än för att starta Clips. En rad encoders styr parameter 1 för effect slots 1–8, och en annan rad följer de åtta kontextuella reglagen i panelen Parameters, inklusive förskjutning av Clip, fördröjning av zone, global rotation/skalning och gruppfades.
